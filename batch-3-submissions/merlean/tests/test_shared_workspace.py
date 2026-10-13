"""Offline shared-workspace contracts; no network, actual Git dependency fixtures."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import shared_workspace as sw


class SharedWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='merlean-shared-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.provider = self.base / 'provider'
        self.store = self.base / 'registry'
        self.project = self.base / 'project'
        self.package = self.provider / '.lake/packages/mathlib'
        self.package.mkdir(parents=True)
        self.toolchain = 'leanprover/lean4:v4.32.2'
        (self.provider / 'lean-toolchain').write_text(self.toolchain + '\n')
        (self.provider / 'lakefile.toml').write_text('name = "provider"\n')
        (self.package / 'lean-toolchain').write_text(self.toolchain + '\n')
        (self.package / 'lakefile.lean').write_text('-- fixture\n')
        (self.package / '.gitignore').write_text('.lake/\n')
        self.git('init', '-q')
        self.git('add', '.')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture')
        self.git('remote', 'add', 'origin', 'https://github.com/leanprover-community/mathlib4.git')
        self.manifest = {'version': '1.2.0', 'packagesDir': '.lake/packages', 'lakeDir': '.lake',
                         'name': 'provider', 'packages': [{
                             'name': 'mathlib', 'type': 'git', 'subDir': None,
                             'url': 'https://github.com/leanprover-community/mathlib4.git',
                             'rev': self.git('rev-parse', 'HEAD'), 'inputRev': 'v4.32.2',
                             'configFile': 'lakefile.lean', 'manifestFile': 'lake-manifest.json',
                             'inherited': False}]}
        self.save_manifest()

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.package), *args], text=True).strip()

    def save_manifest(self):
        (self.provider / 'lake-manifest.json').write_bytes(sw.encoded(self.manifest))

    def init(self):
        sw.register(self.provider, self.store, 'pinned')
        sw.init_project(self.project, self.store, 'pinned', 'experiment')

    def test_two_projects_share_packages_not_builds(self):
        self.init()
        second = self.base / 'second'
        sw.init_project(second, self.store, 'pinned', 'experiment_two')
        for project in (self.project, second):
            self.assertEqual((project / '.lake/packages/mathlib').resolve(), self.package)
            self.assertTrue((project / '.lake/packages').is_symlink())
            self.assertEqual(sw.validate_project(project)['toolchain'], self.toolchain)
            self.assertFalse((project / '.lake/build').exists())
        self.assertNotEqual((self.project / '.lake/build').resolve(), (second / '.lake/build').resolve())

    def test_existing_paths_and_profiles_are_preserved(self):
        self.init()
        before = (self.project / 'lakefile.toml').read_bytes()
        with self.assertRaises(FileExistsError):
            sw.register(self.provider, self.store, 'pinned')
        with self.assertRaisesRegex(ValueError, 'new directory'):
            sw.init_project(self.project, self.store, 'pinned', 'other')
        self.assertEqual(before, (self.project / 'lakefile.toml').read_bytes())

    def test_configuration_drift_rejected(self):
        self.init()
        for filename in ('lean-toolchain', 'lakefile.toml', 'lake-manifest.json'):
            with self.subTest(filename=filename):
                path = self.project / filename
                before = path.read_bytes()
                path.write_bytes(before + b'\n')
                with self.assertRaisesRegex(ValueError, 'configuration drift'):
                    sw.validate_project(self.project)
                path.write_bytes(before)

    def test_provider_drift_rejected(self):
        self.init()
        (self.provider / 'lakefile.toml').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'Provider drift'):
            sw.validate_project(self.project)

    def test_dirty_dependency_rejected(self):
        (self.package / 'new-source.lean').write_text('-- untracked\n')
        with self.assertRaisesRegex(ValueError, 'dirty'):
            sw.provider_snapshot(self.provider)

    def test_ignored_build_artifacts_allowed(self):
        build = self.package / '.lake/build'
        build.mkdir(parents=True)
        (build / 'test.olean').write_bytes(b'not a provenance certificate')
        sw.provider_snapshot(self.provider)

    def test_dependency_revision_and_origin_checked(self):
        self.manifest['packages'][0]['rev'] = '0' * 40
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'revision drift'):
            sw.provider_snapshot(self.provider)
        self.manifest['packages'][0]['rev'] = self.git('rev-parse', 'HEAD')
        self.save_manifest()
        self.git('remote', 'set-url', 'origin', 'https://example.invalid/other')
        with self.assertRaisesRegex(ValueError, 'origin drift'):
            sw.provider_snapshot(self.provider)

    def test_nonstandard_dependencies_rejected(self):
        entry = self.manifest['packages'][0]
        for key, bad in [('name', '../escape'), ('type', 'path'), ('subDir', 'sub'),
                         ('rev', 'main'), ('url', 'https://secret@example.invalid/repo'),
                         ('configFile', '../lakefile.lean'), ('manifestFile', '../manifest.json')]:
            with self.subTest(key=key):
                good = entry[key]
                entry[key] = bad
                self.save_manifest()
                with self.assertRaises(ValueError):
                    sw.provider_snapshot(self.provider)
                entry[key] = good

    def test_floating_toolchain_and_custom_packages_rejected(self):
        (self.provider / 'lean-toolchain').write_text('stable\n')
        with self.assertRaisesRegex(ValueError, 'pinned released'):
            sw.provider_snapshot(self.provider)
        (self.provider / 'lean-toolchain').write_text(self.toolchain + '\n')
        self.manifest['packagesDir'] = 'elsewhere'
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'standard'):
            sw.provider_snapshot(self.provider)

    def test_overrides_rejected_in_project_provider_and_dependency(self):
        self.init()
        for workspace in (self.project, self.provider, self.package):
            with self.subTest(workspace=workspace.name):
                path = workspace / '.lake/package-overrides.json'
                path.parent.mkdir(exist_ok=True)
                path.symlink_to(self.base / 'missing.json')
                with self.assertRaisesRegex(ValueError, 'overrides'):
                    sw.validate_project(self.project)
                path.unlink()

    def test_package_name_collision_and_overlap_rejected(self):
        sw.register(self.provider, self.store, 'pinned')
        with self.assertRaisesRegex(ValueError, 'collide'):
            sw.init_project(self.project, self.store, 'pinned', 'mathlib')
        with self.assertRaisesRegex(ValueError, 'separate'):
            sw.init_project(self.provider / 'nested', self.store, 'pinned', 'research')
        with self.assertRaisesRegex(ValueError, 'safe basename'):
            sw.profile_path(self.store, '../escape')

    def test_symlink_and_build_isolation_checked(self):
        self.init()
        (self.project / '.lake/build').symlink_to(self.base)
        with self.assertRaisesRegex(ValueError, 'build state'):
            sw.validate_project(self.project)
        (self.project / '.lake/build').unlink()
        (self.project / '.lake/packages').unlink()
        (self.project / '.lake/packages').mkdir()
        with self.assertRaisesRegex(ValueError, 'no longer refers'):
            sw.validate_project(self.project)

    def test_provider_lock_shared_by_canonical_path(self):
        alias = self.base / 'alias'
        alias.symlink_to(self.provider / '.lake/packages')
        with sw.provider_lock(str(alias)):
            with self.assertRaisesRegex(ValueError, 'busy'):
                with sw.provider_lock(str(self.provider / '.lake/packages')):
                    self.fail('second provider lock acquired')

    def test_individual_package_alias_rejected(self):
        elsewhere = self.base / 'aliased-mathlib'
        self.package.rename(elsewhere)
        self.package.symlink_to(elsewhere)
        with self.assertRaisesRegex(ValueError, 'directory aliases'):
            sw.provider_snapshot(self.provider)

    def test_command_options_and_outside_source_rejected(self):
        self.init()
        with self.assertRaisesRegex(ValueError, 'names only'):
            sw.run_project(self.project, 'build', ['--update'])
        outside = self.base / 'outside.lean'
        outside.write_text('-- outside\n')
        with self.assertRaisesRegex(ValueError, 'project-local'):
            sw.run_project(self.project, 'check', [str(outside)])

    def test_pinned_compiler_environment_and_exit_code(self):
        self.init()
        # Preserve real git calls used by validation; replace only compiler calls.
        real_run = subprocess.run
        calls = []
        def fake_run(command, **kwargs):
            if command[0] != 'elan':
                return real_run(command, **kwargs)
            calls.append((command, kwargs))
            if command[-1] == '--version':
                return subprocess.CompletedProcess(command, 0, 'Lean (version 4.32.2, fixture)\n')
            return subprocess.CompletedProcess(command, 7)
        with patch.dict(os.environ, {'ELAN_TOOLCHAIN': 'wrong', 'LEAN_PATH': 'wrong', 'LAKE_PKG_URL_MAP': '{}'}):
            with patch.object(sw.subprocess, 'run', side_effect=fake_run):
                self.assertEqual(sw.run_project(self.project, 'build', []), 7)
        command, options = calls[-1]
        self.assertEqual(command, ['elan', 'run', self.toolchain, 'lake', '--no-cache', 'build'])
        for name in ('ELAN_TOOLCHAIN', 'LEAN_PATH', 'LAKE_PKG_URL_MAP'):
            self.assertNotIn(name, options['env'])

    def test_wrapper_not_shadowed_by_cwd_module(self):
        (self.base / 'shared_workspace.py').write_text('raise RuntimeError("shadowed")\n')
        result = subprocess.run([str(ROOT / 'scripts/merlean-workspace'), '--help'],
                                cwd=self.base, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('register', result.stdout)

    def test_wrong_compiler_prevents_build(self):
        self.init()
        real_run = subprocess.run
        compiler_calls = []
        def fake_run(command, **kwargs):
            if command[0] != 'elan':
                return real_run(command, **kwargs)
            compiler_calls.append(command)
            return subprocess.CompletedProcess(command, 0, 'Lean (version 4.0.0, wrong)\n')
        with patch.object(sw.subprocess, 'run', side_effect=fake_run):
            with self.assertRaisesRegex(ValueError, 'version mismatch'):
                sw.run_project(self.project, 'build', [])
        self.assertEqual(len(compiler_calls), 1)

    def test_post_build_configuration_drift_rejected(self):
        self.init()
        real_run = subprocess.run
        def fake_run(command, **kwargs):
            if command[0] != 'elan':
                return real_run(command, **kwargs)
            if command[-1] == '--version':
                return subprocess.CompletedProcess(command, 0, 'Lean (version 4.32.2, fixture)\n')
            (self.project / 'lake-manifest.json').write_text('{}')
            return subprocess.CompletedProcess(command, 0)
        with patch.object(sw.subprocess, 'run', side_effect=fake_run):
            with self.assertRaisesRegex(ValueError, 'configuration drift'):
                sw.run_project(self.project, 'build', [])


if __name__ == '__main__':
    unittest.main()
