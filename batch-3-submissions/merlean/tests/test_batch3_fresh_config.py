"""Actual fresh CLI config uses startup clock and nested lightweight policy."""
import contextlib,io,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch,AsyncMock
import codex_pilot as pilot

class FreshConfigTests(unittest.TestCase):
    def test_fresh_clock_and_engine_policy(self):
        with tempfile.TemporaryDirectory() as folder:
            base=Path(folder);source=base/'input.md';source.write_text('Synthetic problem')
            inputs=base/'inputs.json';inputs.write_text(json.dumps({'P1':'input.md'}));root=base/'run'
            fake=type('Pilot',(),{'run':AsyncMock(return_value={})})()
            argv=['pilot',str(root),'--problems',str(inputs),'--exam-start-utc','2026-01-01T00:00:00Z']
            with patch('sys.argv',argv),patch.object(pilot,'subscription_preflight',return_value={'authentication':'api','cli_version':'codex-cli 0.159.2'}),patch.object(pilot,'freeze_runtime',return_value=({},{})),patch.object(pilot.Campaign,'initialize'),patch.object(pilot,'Pilot',return_value=fake),contextlib.redirect_stdout(io.StringIO()):pilot.main()
            config=json.loads((root/'host-config.json').read_text())
            self.assertEqual(config['exam']['paper_engine'],'lightweight-v1')
            self.assertEqual(config['paper_engine'],'lightweight-v1')
            self.assertEqual(config['exam']['start_utc'],'2026-01-01T00:00:00+00:00')
            self.assertEqual(config['exam']['research_close_utc'],'2026-01-01T22:45:00+00:00')

    def test_start_override_rejects_existing_run(self):
        with tempfile.TemporaryDirectory() as folder,patch('sys.argv',['pilot',folder,'--exam-start-utc','2026-01-01T00:00:00Z']),contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):pilot.main()

    def test_actual_frozen_engine_loads_both_policies_and_sibling_compiler(self):
        import subprocess,sys
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve();code,policies=pilot.freeze_runtime(root)
            (root/'hashes.json').write_text(json.dumps(policies))
            script='''
import sys,json
from pathlib import Path
from types import SimpleNamespace
root=Path(sys.argv[1]);sys.path[:0]=[str(root/'code'),sys.argv[2]]
import codex_pilot as native,pilot_paper_light as light,test_pilot_paper_light as fixtures
assert Path(light.__file__).parent==root/'code'
real=light.LightPaper
host=SimpleNamespace(root=root,config={'policy_hashes':json.loads((root/'hashes.json').read_text())})
def construct(problem,snapshot,runtime):
 problem.pilot.policy=lambda name:native.Pilot.policy(host,name)
 return real(problem,snapshot,runtime)
light.LightPaper=construct
fixture=fixtures.LightTests();fixture.setUp()
try:
 assert fixture.engine.policy and fixture.engine.reader_policy
 assert Path(light.__file__).with_name('pilot_paper_tools.py').is_file()
 assert native.Pilot.policy(host,'workflows/paper/mathematical-writing.md')
finally:fixture.doCleanups()
'''
            result=subprocess.run([sys.executable,'-B','-c',script,str(root),str(Path(__file__).parent)],capture_output=True,text=True,timeout=30)
            self.assertEqual(result.returncode,0,result.stderr)
