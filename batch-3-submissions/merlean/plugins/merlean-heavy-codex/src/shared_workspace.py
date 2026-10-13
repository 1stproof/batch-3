"""External Lean projects sharing a pinned, existing dependency installation.

No downloader, dependency updater, migration, or research-grade authority.
POSIX advisory locks coordinate this wrapper only, not arbitrary Lake/IDE commands.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKER = '.merlean-workspace.json'
NAME = re.compile(r'[A-Za-z][A-Za-z0-9_-]{0,79}')
SHA = re.compile(r'[0-9a-f]{40}')
TOOLCHAIN = re.compile(r'leanprover/lean4:v\d+\.\d+\.\d+(?:-rc\d+)?')


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(value: dict) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def regular(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Expected a regular non-symlink file: {path}')
    return path.read_bytes()


def git(path: Path, *args: str) -> str:
    result = subprocess.run(['git', '-C', str(path), *args], capture_output=True,
                            text=True, timeout=30)
    if result.returncode:
        raise ValueError(f'Git inspection failed at {path}: {args[0]}')
    return result.stdout.strip()


def overlaps(a: Path, b: Path) -> bool:
    return a == b or a in b.parents or b in a.parents


def reject_overrides(workspace: Path) -> None:
    path = workspace / '.lake/package-overrides.json'
    if path.exists() or path.is_symlink():
        raise ValueError(f'Lake package overrides are not supported: {path}')


def provider_snapshot(workspace: Path) -> dict:
    workspace = workspace.expanduser().resolve(strict=True)
    if overlaps(workspace, ROOT):
        raise ValueError('Dependency provider must be separate from the tool checkout')
    reject_overrides(workspace)
    manifest_bytes = regular(workspace / 'lake-manifest.json')
    manifest = json.loads(manifest_bytes)
    if not isinstance(manifest, dict) or manifest.get('version') != '1.2.0':
        raise ValueError('Supported Lake manifest version is 1.2.0')
    if manifest.get('packagesDir') != '.lake/packages' or manifest.get('lakeDir', '.lake') != '.lake':
        raise ValueError('Only the standard .lake/packages layout is supported')
    toolchain_bytes = regular(workspace / 'lean-toolchain')
    toolchain = toolchain_bytes.decode().strip()
    if not TOOLCHAIN.fullmatch(toolchain):
        raise ValueError('Use a pinned released Lean toolchain, not stable/nightly/a local alias')
    configs = [workspace / name for name in ('lakefile.toml', 'lakefile.lean')
               if (workspace / name).exists() or (workspace / name).is_symlink()]
    if len(configs) != 1:
        raise ValueError('Provider must have exactly one Lake configuration')
    config = configs[0]
    packages_dir = (workspace / '.lake/packages').resolve(strict=True)
    if overlaps(packages_dir, ROOT):
        raise ValueError('Shared dependency storage must be outside the tool checkout')
    entries = manifest.get('packages')
    if not isinstance(entries, list) or not entries:
        raise ValueError('Provider must have a resolved nonempty dependency manifest')
    records = []
    names: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError('Invalid dependency record')
        name = entry.get('name')
        if not isinstance(name, str) or not NAME.fullmatch(name) or name in names:
            raise ValueError('Dependency names must be unique safe basenames')
        names.add(name)
        if entry.get('configFile') not in ('lakefile.toml', 'lakefile.lean') or entry.get('manifestFile') != 'lake-manifest.json':
            raise ValueError(f'Only standard dependency configuration/manifest filenames: {name}')
        rev = entry.get('rev')
        url = entry.get('url')
        if (entry.get('type') != 'git' or entry.get('subDir') not in (None, '')
                or not isinstance(rev, str) or not SHA.fullmatch(rev)
                or not isinstance(url, str) or not url.startswith('https://')
                or '@' in url):
            raise ValueError(f'Only pinned HTTPS git dependencies without subdirectories: {name}')
        package = (packages_dir / name).resolve(strict=True)
        if package != packages_dir / name:
            raise ValueError(f'Individual dependency directory aliases are not supported: {name}')
        reject_overrides(package)
        if overlaps(package, ROOT) or package == workspace:
            raise ValueError('Dependency overlaps tool or provider root')
        if Path(git(package, 'rev-parse', '--show-toplevel')).resolve() != package:
            raise ValueError(f'Dependency must be its own Git checkout: {name}')
        if git(package, 'rev-parse', 'HEAD') != rev:
            raise ValueError(f'Dependency revision drift: {name}')
        if git(package, 'status', '--porcelain', '--untracked-files=normal'):
            raise ValueError(f'Dependency checkout is dirty: {name}')
        actual_url = git(package, 'remote', 'get-url', 'origin')
        if actual_url.removesuffix('.git').rstrip('/') != url.removesuffix('.git').rstrip('/'):
            raise ValueError(f'Dependency origin drift: {name}')
        records.append({'name': name, 'path': str(package), 'rev': rev, 'url': url})
    mathlib = next((p for p in records if p['name'] == 'mathlib'), None)
    if not mathlib or mathlib['url'].removesuffix('.git').rstrip('/') != 'https://github.com/leanprover-community/mathlib4':
        raise ValueError('Provider needs the official mathlib Git dependency')
    if regular(Path(mathlib['path']) / 'lean-toolchain').decode().strip() != toolchain:
        raise ValueError('Provider and Mathlib Lean toolchains differ')
    return {'schema_version': 1, 'workspace': str(workspace),
            'packages_dir': str(packages_dir), 'toolchain': toolchain,
            'toolchain_sha256': digest(toolchain_bytes),
            'config_file': config.name, 'config_sha256': digest(regular(config)),
            'manifest_sha256': digest(manifest_bytes), 'manifest': manifest,
            'packages': records}


def home() -> Path:
    return Path(os.environ.get('MERLEAN_SHARED_HOME', str(Path.home() / '.cache/merlean/shared-lean'))).expanduser().resolve()


def profile_path(store: Path, name: str) -> Path:
    if not NAME.fullmatch(name):
        raise ValueError('Profile name must be a safe basename')
    store = store.expanduser().resolve()
    if overlaps(store, ROOT):
        raise ValueError('Machine-specific registry must be outside the tool checkout')
    return store / 'profiles' / (name + '.json')


def write_new(path: Path, value: bytes) -> None:
    with path.open('xb') as stream:
        stream.write(value)


def register(workspace: Path, store: Path, name: str) -> dict:
    record = provider_snapshot(workspace)
    path = profile_path(store, name)
    if overlaps(path.parent.parent, Path(record['workspace'])):
        raise ValueError('Registry must be outside the provider workspace')
    path.parent.mkdir(parents=True, exist_ok=True)
    write_new(path, encoded(record))
    return {'profile': name, 'record': str(path), 'toolchain': record['toolchain'],
            'packages': len(record['packages']), 'copied_dependencies': False}


def load_profile(path: Path) -> dict:
    record = json.loads(regular(path))
    if not isinstance(record, dict) or record.get('schema_version') != 1:
        raise ValueError('Unsupported shared dependency profile')
    actual = provider_snapshot(Path(record['workspace']))
    if actual != record:
        raise ValueError('Provider drift: keep the old profile; register a separately named profile after review')
    return record


@contextmanager
def provider_lock(packages: str):
    try:
        import fcntl
    except ImportError as error:
        raise ValueError('Shared builds currently require POSIX advisory locking') from error
    # Independent of --store/profile name: the same provider uses one per-user lock.
    locks = Path.home() / '.cache/merlean/shared-lean-locks'
    locks.mkdir(parents=True, exist_ok=True)
    path = locks / (digest(str(Path(packages).resolve()).encode()) + '.lock')
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise ValueError('Shared dependency provider is busy; retry after its active build') from error
        yield
    finally:
        os.close(fd)


def init_project(project: Path, store: Path, profile: str, name: str) -> dict:
    from lean_capability import require_lean
    require_lean(project)
    if not NAME.fullmatch(name):
        raise ValueError('Project package name must be a safe basename')
    profile_file = profile_path(store, profile)
    record = load_profile(profile_file)
    if name in {p['name'] for p in record['packages']}:
        raise ValueError('Project name must not collide with a dependency package')
    project = project.expanduser().absolute()
    if project.exists() or project.is_symlink():
        raise ValueError('init requires a new directory; existing projects are never rewritten')
    resolved = project.resolve()
    excluded = [ROOT, Path(record['workspace']), Path(record['packages_dir']), profile_file.parent.parent]
    excluded.extend(Path(p['path']) for p in record['packages'])
    if any(overlaps(resolved, p) for p in excluded):
        raise ValueError('Project must be separate from the tool, registry and dependency provider')
    with provider_lock(record['packages_dir']):
        record = load_profile(profile_file)
        mathlib = next(p for p in record['packages'] if p['name'] == 'mathlib')
        config = (f'name = {json.dumps(name)}\nversion = "0.1.0"\n'
                  'defaultTargets = ["MerLeanExperiment"]\n\n[[require]]\nname = "mathlib"\n'
                  f'git = {json.dumps(mathlib["url"])}\nrev = {json.dumps(mathlib["rev"])}\n\n'
                  '[[lean_lib]]\nname = "MerLeanExperiment"\n').encode()
        manifest = json.loads(json.dumps(record['manifest']))
        manifest['name'] = name
        for dependency in manifest['packages']:
            dependency['inherited'] = dependency['name'] != 'mathlib'
            if dependency['name'] == 'mathlib':
                dependency['inputRev'] = mathlib['rev']
        payloads = {'lakefile.toml': config, 'lake-manifest.json': encoded(manifest),
                    'lean-toolchain': regular(Path(record['workspace']) / 'lean-toolchain')}
        # Exclusive creation leaves partial failures visible, never deletes user data.
        project.mkdir(parents=True, exist_ok=False)
        (project / '.lake').mkdir()
        (project / '.lake/packages').symlink_to(record['packages_dir'], target_is_directory=True)
        for filename, data in payloads.items():
            write_new(project / filename, data)
        write_new(project / 'MerLeanExperiment.lean',
                  b'import Mathlib.Data.Nat.Basic\n\ntheorem merlean_smoke (n : Nat) : 0 + n = n := by simp\n')
        write_new(project / '.gitignore', b'.lake/\n.merlean-workspace.json\n.env\n.venv/\n')
        write_new(project / MARKER, encoded({
            'schema_version': 1, 'profile': str(profile_file),
            'profile_sha256': digest(regular(profile_file)), 'project': str(resolved),
            'files': {key: digest(value) for key, value in payloads.items()}}))
    return {'project': str(resolved), 'profile': profile, 'packages_dir': record['packages_dir'],
            'copied_dependencies': False, 'build_dir': str(resolved / '.lake/build')}


def validate_project(project: Path) -> dict:
    project = project.expanduser().resolve(strict=True)
    reject_overrides(project)
    marker = json.loads(regular(project / MARKER))
    if marker.get('schema_version') != 1 or marker.get('project') != str(project):
        raise ValueError('Project moved or shared workspace marker is invalid')
    profile_file = Path(marker['profile'])
    if digest(regular(profile_file)) != marker['profile_sha256']:
        raise ValueError('Shared dependency profile was modified')
    record = load_profile(profile_file)
    if set(marker['files']) != {'lakefile.toml', 'lake-manifest.json', 'lean-toolchain'}:
        raise ValueError('Missing pinned project configuration')
    for filename, sha in marker['files'].items():
        if digest(regular(project / filename)) != sha:
            raise ValueError(f'Project configuration drift: {filename}; reconfigure deliberately, not through shared build')
    if (project / 'lakefile.lean').exists() or (project / 'lakefile.lean').is_symlink():
        raise ValueError('Additional Lake configuration would shadow the pinned configuration')
    link = project / '.lake/packages'
    if not link.is_symlink() or link.resolve(strict=True) != Path(record['packages_dir']):
        raise ValueError('Project no longer refers to the registered dependency provider')
    if (project / '.lake').is_symlink() or (project / '.lake/build').is_symlink():
        raise ValueError('Project build state must stay local, not symlink to another workspace')
    return record


def run_project(project: Path, action: str, targets: list[str]) -> int:
    from lean_capability import require_lean
    require_lean(project)
    project = project.expanduser().resolve(strict=True)
    record = validate_project(project)
    if action == 'build':
        if any(not re.fullmatch(r'[A-Za-z][A-Za-z0-9_.]*', t) for t in targets):
            raise ValueError('build accepts module/target names only, not Lake options or commands')
        command = ['lake', '--no-cache', 'build', *targets]
    else:
        if len(targets) != 1:
            raise ValueError('check requires one project-local Lean source file')
        source = (project / targets[0]).resolve(strict=True)
        if project not in source.parents or source.suffix != '.lean':
            raise ValueError('check requires a project-local .lean file')
        command = ['lake', '--no-cache', 'env', 'lean', str(source)]
    with provider_lock(record['packages_dir']):
        record = validate_project(project)
        env = dict(os.environ)
        # Elan must use the pinned project file, never an inherited toolchain override.
        for key in list(env):
            if key == 'ELAN_TOOLCHAIN' or key in ('LEAN', 'LAKE') or key.startswith(('LEAN_', 'LAKE_')):
                env.pop(key)
        # Explicit elan selection ignores directory overrides; omitting --install
        # refuses unavailable toolchains rather than downloading them.
        prefix = ['elan', 'run', record['toolchain']]
        version = subprocess.run([*prefix, 'lean', '--version'], cwd=project, env=env,
                                 capture_output=True, text=True, timeout=30)
        expected = record['toolchain'].split(':v', 1)[1]
        if version.returncode or not version.stdout.startswith(f'Lean (version {expected},'):
            raise ValueError('Pinned installed Lean toolchain unavailable or version mismatch')
        result = subprocess.run([*prefix, *command], cwd=project, env=env)
        validate_project(project)
        return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('register', help='Record an existing trusted provider without copying or downloading')
    p.add_argument('--workspace', type=Path, required=True)
    p.add_argument('--name', required=True)
    p.add_argument('--store', type=Path, default=home())
    p = sub.add_parser('init', help='Create an external new project sharing a registered provider')
    p.add_argument('--project', type=Path, required=True)
    p.add_argument('--profile', required=True)
    p.add_argument('--name', default='merlean_experiment')
    p.add_argument('--store', type=Path, default=home())
    for action in ('doctor', 'build', 'check'):
        p = sub.add_parser(action)
        p.add_argument('--project', type=Path, required=True)
        if action != 'doctor':
            p.add_argument('targets', nargs='*')
    args = parser.parse_args()
    try:
        if args.command == 'register':
            result = register(args.workspace, args.store, args.name)
        elif args.command == 'init':
            result = init_project(args.project, args.store, args.profile, args.name)
        elif args.command == 'doctor':
            result = validate_project(args.project)
            result = {'valid': True, 'toolchain': result['toolchain'],
                      'packages_dir': result['packages_dir'], 'packages': len(result['packages']),
                      'note': 'Configuration/source identity only; not a build or Gold certificate'}
        else:
            return run_project(args.project, args.command, args.targets)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
        print(f'merlean-workspace: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
