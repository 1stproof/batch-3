"""Real host-denial tests; synthetic sentinels only, no private data reads."""
import errno
import os
import socket
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import offline_probe as probe


class PortableProbeTests(unittest.TestCase):
    def test_fail_closed(self):
        with patch.object(probe.sys, 'platform', 'unsupported'):
            self.assertEqual(probe.run_python_probe('print(1)')['status'], 'unavailable')

    def test_reject(self):
        self.assertEqual(probe.run_python_probe('x' * (probe.MAX_SOURCE_BYTES + 1))['status'], 'rejected')
        self.assertEqual(probe.run_python_probe('\0')['status'], 'rejected')


@unittest.skipUnless(sys.platform == 'linux' or (sys.platform == 'darwin' and probe._PYTHON.is_file() and probe._SANDBOX.is_file()),
                     'requires a supported kernel sandbox and Python runtime')
class NativeSandboxTests(unittest.TestCase):
    def completed(self, source):
        result = probe.run_python_probe(source)
        self.assertEqual(result['status'], 'completed', result)
        return result

    def test_arithmetic_runtime(self):
        result = self.completed('import math, fractions, json; print(json.dumps([math.factorial(6), str(fractions.Fraction(2, 3))]))')
        self.assertEqual(result['stdout'], '[720, "2/3"]\n')

    def test_denials(self):
        # All target files are test-created, outside the runtime allowlist.
        with tempfile.TemporaryDirectory(prefix='offline-probe-denial-') as directory:
            root = Path(directory)
            sentinel = root / 'sentinel'
            sentinel.write_text('PRIVATE_TEST_SENTINEL')
            link = root / 'link'
            link.symlink_to(sentinel)
            tcp = socket.socket()
            tcp.bind(('127.0.0.1', 0))
            tcp.listen()
            self.addCleanup(tcp.close)
            local = socket.socket(socket.AF_UNIX)
            local.bind(str(root / 'socket'))
            local.listen()
            self.addCleanup(local.close)
            source = f'''import os, socket, errno
checks = {{}}
def denied(name, fn):
    try:
        fn()
    except OSError as exc:
        checks[name] = exc.errno in (errno.EPERM, errno.EACCES)
    else:
        checks[name] = False
denied('read', lambda: open({str(sentinel)!r}).read())
denied('symlink_read', lambda: open({str(link)!r}).read())
denied('write', lambda: open({str(root / 'output')!r}, 'w'))
denied('overwrite', lambda: open({str(sentinel)!r}, 'w'))
denied('network', lambda: socket.create_connection(('127.0.0.1', {tcp.getsockname()[1]}), 1))
denied('unix_network', lambda: socket.socket(socket.AF_UNIX, socket.SOCK_STREAM).connect({str(root / 'socket')!r}))
denied('fork', os.fork)
denied('exec', lambda: os.execv('/bin/echo', ['echo', 'escape']))
print(checks)
assert all(checks.values()), checks
'''
            result = self.completed(source)
            self.assertEqual(sentinel.read_text(), 'PRIVATE_TEST_SENTINEL')
            self.assertFalse((root / 'output').exists())
            self.assertNotIn('PRIVATE_TEST_SENTINEL', result['stdout'])

    def test_environment_and_import_isolation(self):
        with patch.dict(os.environ, {'PROBE_SECRET': 'do-not-inherit', 'PYTHONPATH': '/tmp'}):
            result = self.completed("import os, sys; assert 'PROBE_SECRET' not in os.environ; assert 'PYTHONPATH' not in os.environ; assert '' not in sys.path; print('isolated')")
        self.assertEqual(result['stdout'], 'isolated\n')

    def test_output_cap(self):
        result = probe.run_python_probe("import os;\nwhile True: os.write(1, b'x' * 65536)")
        self.assertEqual(result['status'], 'output_limit', result)
        self.assertLessEqual(len(result['stdout'].encode()) + len(result['stderr'].encode()), probe.MAX_OUTPUT_BYTES)

    def test_invalid_output_cap(self):
        result = probe.run_python_probe("import os;\nwhile True: os.write(2, b'\\xff' * 65536)")
        self.assertEqual(result['status'], 'output_limit', result)
        self.assertLessEqual(len(result['stdout'].encode()) + len(result['stderr'].encode()), probe.MAX_OUTPUT_BYTES)

    def test_cli_child_shares_helper_process_group(self):
        import json
        import subprocess
        helper = subprocess.Popen(
            [sys.executable, '-I', str(Path(probe.__file__).resolve())],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            start_new_session=True, text=True)
        stdout, stderr = helper.communicate(
            json.dumps({'kind': 'python', 'code': 'import os; print(os.getpgrp())'}), timeout=12)
        self.assertEqual(helper.returncode, 0, stderr)
        result = json.loads(stdout)
        self.assertEqual(result['status'], 'completed', result)
        self.assertEqual(int(result['stdout'].strip()), helper.pid)

    def test_cli_overflow_cleanup_preserves_helper(self):
        import json
        import subprocess
        helper = subprocess.run(
            [sys.executable, '-I', str(Path(probe.__file__).resolve())],
            input=json.dumps({'kind': 'python',
                              'code': "import os;\nwhile True: os.write(1, b'x' * 65536)"}),
            capture_output=True, text=True, start_new_session=True, timeout=12)
        self.assertEqual(helper.returncode, 0, helper.stderr)
        self.assertEqual(json.loads(helper.stdout)['status'], 'output_limit')

    def test_timeout(self):
        result = probe.run_python_probe('import time; time.sleep(30)')
        self.assertEqual(result['status'], 'timeout', result)
        self.assertLess(result['elapsed_seconds'], 12)



@unittest.skipUnless(sys.platform == 'linux', 'Linux confinement checks')
class LinuxConfinementTests(unittest.TestCase):
    def test_cross_process_prlimit_and_fcntl_owner_denied(self):
        code = """import ctypes, errno, fcntl, os, resource
try: os.kill(os.getppid(), 0)
except PermissionError: pass
else: raise AssertionError('other-process signal permitted')
try: resource.prlimit(os.getppid(), resource.RLIMIT_CORE, (0, 0))
except PermissionError: pass
else: raise AssertionError('cross-process resource mutation permitted')
try: fcntl.fcntl(1, fcntl.F_SETOWN, os.getppid())
except PermissionError: pass
else: raise AssertionError('pipe signal ownership permitted')
libc = ctypes.CDLL(None, use_errno=True)
for name, args in [('ptrace', (2, os.getppid(), 0, 0)), ('process_vm_readv', (os.getppid(), 0, 0, 0, 0, 0)), ('unshare', (0,))]:
    ctypes.set_errno(0)
    assert getattr(libc, name)(*args) == -1 and ctypes.get_errno() == errno.EPERM, name
print('DENIED')
"""
        result = probe.run_python_probe(code)
        self.assertEqual(result['status'], 'completed', result)
        self.assertEqual(result['stdout'], 'DENIED\n')

    def test_proc_and_inherited_descriptor_denied(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'synthetic-secret'
            path.write_text('SYNTHETIC_PRIVATE_BYTES')
            with path.open() as stream:
                import fcntl
                high_fd = fcntl.fcntl(stream.fileno(), fcntl.F_DUPFD, 200)
                os.set_inheritable(high_fd, True)
                self.addCleanup(os.close, high_fd)
                code = f"""import os
for path in ['/proc/'+str(os.getppid())+'/environ', '/proc/self/fd/{stream.fileno()}']:
    try: open(path).read()
    except OSError as exc:
        assert exc.errno in (1, 2, 13), exc
    else: raise AssertionError('proc file readable')
for fd in ({stream.fileno()}, {high_fd}):
    try: os.read(fd, 32)
    except OSError as exc: assert exc.errno == 9, exc
    else: raise AssertionError('inherited private descriptor readable')
print('DENIED')
"""
                result = probe.run_python_probe(code)
            self.assertEqual(result['status'], 'completed', result)
            self.assertEqual(result['stdout'], 'DENIED\n')

    def test_policy_setup_failure_never_executes_source(self):
        import offline_probe_linux as linux
        with patch.object(linux.Policy, '__call__', side_effect=OSError('synthetic setup failure')):
            result = probe.run_python_probe("print('PAYLOAD_EXECUTED')")
        self.assertEqual(result['status'], 'unavailable', result)
        self.assertNotIn('PAYLOAD_EXECUTED', result['stdout'])

    def test_multithread_library_caller_fails_closed(self):
        import threading
        stop = threading.Event()
        thread = threading.Thread(target=stop.wait)
        thread.start()
        try:
            result = probe.run_python_probe("print('PAYLOAD_EXECUTED')")
        finally:
            stop.set(); thread.join()
        self.assertEqual(result['status'], 'unavailable', result)
        self.assertIn('single-thread', result['reason'])
        self.assertEqual(result['stdout'], '')

    def test_missing_landlock_fails_closed(self):
        import offline_probe_linux as linux
        with patch.object(linux, 'Policy', side_effect=OSError('Landlock unavailable')):
            result = probe.run_python_probe("print('PAYLOAD_EXECUTED')")
        self.assertEqual(result['status'], 'unavailable', result)
        self.assertEqual(result['stdout'], '')

@unittest.skipUnless(os.environ.get('MERLEAN_TEST_LEAN') and os.environ.get('MERLEAN_TEST_LEAN_PATH'),
                     'requires explicit trusted prebuilt Lean test runtime')
class LeanSandboxTests(unittest.TestCase):
    def run_lean(self, source):
        return probe.run_lean_probe(source, os.environ['MERLEAN_TEST_LEAN'],
                                    os.environ['MERLEAN_TEST_LEAN_PATH'].split(os.pathsep))

    def test_arithmetic_and_exact_source(self):
        import hashlib
        source = 'import Mathlib\ntheorem probe_arithmetic : 2 + 2 = (4 : Nat) := by norm_num\n#print axioms probe_arithmetic\n'
        result = self.run_lean(source)
        self.assertEqual(result['status'], 'completed', result)
        self.assertEqual(result['source'], source)
        self.assertEqual(result['source_sha256'], hashlib.sha256(source.encode()).hexdigest())
        self.assertIn('probe_arithmetic', result['stdout'])
        self.assertIn('axioms', result['stdout'])
        self.assertFalse(result['theorem_verified'])
        self.assertIsNone(result['grade_claim'])

    def test_file_denials(self):
        import json
        with tempfile.TemporaryDirectory(prefix='lean-probe-denial-') as directory:
            secret = Path(directory) / 'sentinel'
            secret.write_text('TEST_ONLY_SECRET')
            target = Path(directory) / 'output'
            source = f'''import Lean
#eval do
  let readDenied ← try
    let _ ← IO.FS.readFile {json.dumps(str(secret))}
    pure false
  catch _ => pure true
  let writeDenied ← try
    IO.FS.writeFile {json.dumps(str(target))} "escape"
    pure false
  catch _ => pure true
  if !readDenied || !writeDenied then throw (IO.userError "sandbox denial failed")
  IO.println "DENIED"
'''
            result = self.run_lean(source)
            self.assertEqual(result['status'], 'completed', result)
            self.assertIn('DENIED', result['stdout'])
            self.assertFalse(target.exists())
            self.assertEqual(secret.read_text(), 'TEST_ONLY_SECRET')

    def test_environment_and_process_denial(self):
        source = '''import Lean
def environmentAndProcessProbe : IO Unit := do
  let secret ← IO.getEnv "PROBE_SECRET"
  if secret.isSome then throw (IO.userError "environment secret inherited")
  let denied ← try
    let _ ← IO.Process.output { cmd := "/bin/echo", args := #["escape"] }
    pure false
  catch _ => pure true
  if !denied then throw (IO.userError "subprocess unexpectedly allowed")
  IO.println "PROCESS_DENIED"
#eval environmentAndProcessProbe
'''
        with patch.dict(os.environ, {'PROBE_SECRET': 'synthetic-environment-secret'}):
            result = self.run_lean(source)
        self.assertEqual(result['status'], 'completed', result)
        self.assertIn('PROCESS_DENIED', result['stdout'])

    def test_network_denial(self):
        result = self.run_lean('''import Std.Internal.UV.TCP
#eval do
  let denied ← try
    let sock ← Std.Internal.UV.TCP.Socket.new
    sock.bind (.v4 { addr := Std.Net.IPv4Addr.ofParts 127 0 0 1, port := 0 })
    pure false
  catch e => do
    IO.println e
    pure true
  if !denied then throw (IO.userError "network unexpectedly allowed")
  IO.println "NETWORK_DENIED"
''')
        self.assertEqual(result['status'], 'completed', result)
        self.assertIn('NETWORK_DENIED', result['stdout'])
        self.assertTrue('permission' in result['stdout'].lower() or
                        'permitted' in result['stdout'].lower(), result)


if __name__ == '__main__':
    unittest.main()
