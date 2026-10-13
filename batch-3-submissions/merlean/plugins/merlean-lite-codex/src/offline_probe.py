"""Bounded, offline Python and Lean experiments under an OS kernel sandbox.

This is a host boundary, not a Python language filter. macOS uses Apple's CLT
Python; Linux uses its system Python, Landlock and seccomp. Missing enforcement
or unsupported runtimes fail closed.
The system runtime is trusted; benchmark files and provider credentials are never
passed to the child. Results are evidence, never proof or research grades.
"""
from __future__ import annotations

import hashlib
import functools
import json
import tempfile
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import time

MAX_SOURCE_BYTES = 64 * 1024
MAX_OUTPUT_BYTES = 1024 * 1024
MAX_SECONDS = 8
_SANDBOX = Path('/usr/bin/sandbox-exec')
_FRAMEWORK = Path('/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework')
_PYTHON = _FRAMEWORK / 'Versions/Current/Resources/Python.app/Contents/MacOS/Python'
# CLI children stay in the caller-created helper process group so cancellation
# kills helper and compiler together. Direct library calls own their group.
_OWN_PROCESS_GROUP = True


def _quote(path: Path) -> str:
    return '"' + str(path).replace('\\', '\\\\').replace('"', '\\"') + '"'


def _profile() -> str:
    roots = [_FRAMEWORK.resolve(), Path('/System/Library'), Path('/usr/lib')]
    reads = '\n'.join('(subpath ' + _quote(p) + ')' for p in roots)
    return f'''(version 1)
(deny default)
(import "dyld-support.sb")
(allow mach-bootstrap)
(allow syscall*)
(allow process-exec (literal {_quote(_PYTHON.resolve())}))
(allow file-read* file-map-executable
{reads}
(literal {_quote(_PYTHON.resolve())}))
(allow file-read-metadata (literal "/")
(path-ancestors {_quote(_PYTHON.resolve())})
(path-ancestors {_quote(_FRAMEWORK.resolve())}))
(allow sysctl-read)
(allow file-read-data (literal "/dev/urandom"))
'''


def _limits(seconds: int = MAX_SECONDS, descriptors: int = 32) -> None:
    import resource
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds))
    resource.setrlimit(resource.RLIMIT_FSIZE, (0, 0))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_NOFILE, (descriptors, descriptors))


def run_python_probe(code: str) -> dict:
    """Run one source string; return capped streams without creating any files.

    Invalid UTF-8 output bytes are discarded; captured bytes stay within the
    combined cap, and decoding cannot expand malformed bytes beyond that cap.

    Invoke from a dedicated host process: POSIX preexec resource-limit setup is
    not suitable for multithreaded hosts. Wall time and combined output are hard
    host limits; macOS offers no equivalent hard RSS guarantee here. A process
    group is killed on timeout, output overflow, or host exception for library
    calls. CLI children share the helper group for caller cancellation and are
    individually killed by helper cleanup (the sandbox denies forks).
    """
    if not isinstance(code, str):
        raise TypeError('code must be a string')
    encoded = code.encode('utf-8')
    result = dict(status='unavailable', source_sha256=hashlib.sha256(encoded).hexdigest(),
                  stdout='', stderr='', exit_code=None, elapsed_seconds=0.0,
                  output_limit_bytes=MAX_OUTPUT_BYTES, timeout_seconds=MAX_SECONDS)
    if len(encoded) > MAX_SOURCE_BYTES or '\x00' in code:
        result.update(status='rejected', reason='source too large or contains NUL')
        return result
    if sys.platform == 'linux':
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        try:
            from offline_probe_linux import Policy, python_runtime
            executable, stdlib = python_runtime()
            policy = Policy(executable, [stdlib])
        except (OSError, ValueError) as exc:
            result['reason'] = 'Linux confinement unavailable: ' + str(exc)
            return result
        return _execute(result, [str(executable), '-I', '-S', '-B', '-c', code],
                        '', MAX_SECONDS, confinement=policy)
    if sys.platform != 'darwin' or not _SANDBOX.is_file() or not _PYTHON.is_file() or not _FRAMEWORK.is_dir():
        result['reason'] = 'supported macOS sandbox and Apple Python runtime unavailable'
        return result
    return _execute(result, [str(_PYTHON.resolve()), '-I', '-S', '-B', '-c', code],
                    _profile(), MAX_SECONDS)


def _kill_child(proc: subprocess.Popen) -> None:
    try:
        if _OWN_PROCESS_GROUP:
            os.killpg(proc.pid, signal.SIGKILL)
        else:
            # The sandbox denies fork; no descendant tree can escape cleanup.
            # Never signal our own helper group from inside the helper.
            proc.kill()
    except ProcessLookupError:
        pass


def _child_setup(seconds, descriptors, confinement):
    _limits(seconds, descriptors)
    if confinement is not None:
        confinement()


def _execute(result: dict, command: list[str], profile: str, seconds: int,
             extra_env: dict | None = None, descriptors: int = 32, confinement=None) -> dict:
    started = time.monotonic()
    proc = None
    output = {'stdout': bytearray(), 'stderr': bytearray()}
    total = 0
    status = None
    try:
        proc = subprocess.Popen(
            command if confinement is not None else [str(_SANDBOX), '-p', profile, *command],
            cwd='/', env={'LANG': 'C', 'LC_ALL': 'C', 'HOME': '/nonexistent', 'TMPDIR': '/nonexistent', **(extra_env or {})},
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            close_fds=True, start_new_session=_OWN_PROCESS_GROUP, preexec_fn=functools.partial(_child_setup, seconds, descriptors, confinement))
        with selectors.DefaultSelector() as selector:
            for name, stream in [('stdout', proc.stdout), ('stderr', proc.stderr)]:
                os.set_blocking(stream.fileno(), False)
                selector.register(stream, selectors.EVENT_READ, name)
            while selector.get_map():
                remaining = seconds - (time.monotonic() - started)
                if remaining <= 0:
                    status = 'timeout'
                    break
                for key, _ in selector.select(min(remaining, 0.1)):
                    chunk = os.read(key.fileobj.fileno(), 65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        continue
                    room = MAX_OUTPUT_BYTES - total
                    output[key.data].extend(chunk[:room])
                    total += min(room, len(chunk))
                    if len(chunk) > room:
                        status = 'output_limit'
                        break
                if status:
                    break
        if status:
            _kill_child(proc)
        try:
            proc.wait(timeout=max(0.01, seconds - (time.monotonic() - started)))
        except subprocess.TimeoutExpired:
            status = 'timeout'
            _kill_child(proc)
            proc.wait()
        result.update(status=status or ('completed' if proc.returncode == 0 else 'failed'),
                      exit_code=proc.returncode)
    except (OSError, subprocess.SubprocessError) as exc:
        result['reason'] = 'sandbox launch/execution failed: ' + str(exc)
    finally:
        if proc is not None:
            if proc.poll() is None:
                _kill_child(proc)
                proc.wait()
            for stream in (proc.stdout, proc.stderr):
                if stream:
                    stream.close()
        result.update(stdout=output['stdout'].decode('utf-8', errors='ignore'),
                      stderr=output['stderr'].decode('utf-8', errors='ignore'),
                      elapsed_seconds=round(time.monotonic() - started, 6))
    return result


def _lean_profile(executable: Path, libraries: list[Path], source: Path) -> str:
    # Configuration is trusted host input, never model-selected paths. Only the
    # pinned executable's lib tree and prebuilt dependency libraries are exposed.
    roots = [executable.parent.parent / 'lib', *libraries,
             Path('/System/Library'), Path('/usr/lib')]
    reads = '\n'.join('(subpath ' + _quote(p) + ')' for p in roots)
    ancestors = '\n'.join('(path-ancestors ' + _quote(p) + ')'
                          for p in [executable, source, *roots])
    return f'''(version 1)
(deny default)
(import "dyld-support.sb")
(allow mach-bootstrap)
(allow syscall*)
(allow process-exec (literal {_quote(executable)}))
(allow file-read* file-map-executable
{reads}
(literal {_quote(executable)})
(literal {_quote(source)}))
(allow file-read-metadata {ancestors})
(allow sysctl-read)
(allow file-read-data (literal "/dev/urandom"))
'''


def run_lean_probe(code: str, executable: str | Path,
                   library_paths: list[str | Path], *, policy_root=None, nl_only=False) -> dict:
    """Compile exact source with trusted host-provided preinstalled dependencies.

    The caller must retain source/result evidence and compare the intended
    declaration and its explicit #print axioms output independently. Compiler
    success alone accepts sorry/axioms and is never theorem validation or a grade.
    No Lake/Elan/build/install is invoked. Arbitrary elaborator code remains inside
    the OS boundary; all supplied library trees are trusted executable code.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lean_capability import require_lean
    require_lean(policy_root, config={"nl_only": nl_only})
    if not isinstance(code, str):
        raise TypeError('code must be a string')
    encoded = code.encode('utf-8')
    result = dict(status='unavailable', source_sha256=hashlib.sha256(encoded).hexdigest(),
                  stdout='', stderr='', exit_code=None, elapsed_seconds=0.0,
                  output_limit_bytes=MAX_OUTPUT_BYTES, timeout_seconds=60,
                  grade_claim=None, theorem_verified=False,
                  source=code, kind='lean')
    if len(encoded) > MAX_SOURCE_BYTES or '\x00' in code:
        result.update(status='rejected', reason='source too large or contains NUL')
        return result
    executable = Path(executable).resolve()
    libraries = [Path(p).resolve() for p in library_paths]
    if (sys.platform not in ('darwin', 'linux') or
            (sys.platform == 'darwin' and not _SANDBOX.is_file()) or
            executable.name != 'lean' or not executable.is_file() or
            not (executable.parent.parent / 'lib/lean').is_dir() or
            not libraries or any(not p.is_dir() for p in libraries)):
        result['reason'] = 'supported sandbox or supplied prebuilt Lean runtime unavailable'
        return result
    # Reject obvious broad grants even though configuration is trusted host input.
    if any(p == Path('/') or p == Path.home() or '.lake/build/lib/lean' not in p.as_posix()
           for p in libraries):
        result.update(status='rejected', reason='expected narrow prebuilt Lean library roots')
        return result
    with tempfile.TemporaryDirectory(prefix='offline-lean-') as directory:
        source = Path(directory).resolve() / 'Probe.lean'
        source.write_bytes(encoded)
        source.chmod(0o400)
        confinement = None
        if sys.platform == 'linux':
            try:
                from offline_probe_linux import Policy
                confinement = Policy(executable, [executable.parent.parent / 'lib', *libraries],
                                     [source], threads=True)
            except (OSError, ValueError) as exc:
                result['reason'] = 'Linux confinement unavailable: ' + str(exc)
                return result
        result = _execute(result, [str(executable), '-j1', str(source)],
                          _lean_profile(executable, libraries, source), 60,
                          {'LEAN_PATH': os.pathsep.join(map(str, libraries))}, 128, confinement=confinement)
    return result


def main() -> int:
    """Dedicated helper: bounded JSON stdin; settings must come from trusted host."""
    global _OWN_PROCESS_GROUP
    _OWN_PROCESS_GROUP = False
    raw = sys.stdin.buffer.read(256 * 1024 + 1)
    try:
        if len(raw) > 256 * 1024:
            raise ValueError('helper request exceeds limit')
        request = json.loads(raw)
        if request.get('kind') == 'python':
            result = run_python_probe(request['code'])
        elif request.get('kind') == 'lean':
            result = run_lean_probe(request['code'], request['executable'], request['library_paths'], policy_root=request.get('policy_root'), nl_only=request.get('nl_only', False))
        else:
            raise ValueError('unsupported probe kind')
    except (ValueError, TypeError, KeyError) as exc:
        result = {'status': 'rejected', 'reason': str(exc)}
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
