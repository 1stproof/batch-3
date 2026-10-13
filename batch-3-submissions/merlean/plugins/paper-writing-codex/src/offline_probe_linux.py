"""Fail-closed Linux child confinement for trusted offline probe runtimes.

Requires native aarch64/x86_64, Landlock ABI >= 3 and libseccomp. No user
namespaces, capabilities, Docker daemon, or unsandboxed fallback are used.
Landlock confines file contents/actions, not all pathname metadata. Runtime and
library roots are trusted installation inputs, never selected by probe source.
"""
from __future__ import annotations
import ctypes
import errno
import os
from pathlib import Path
import platform

# No sockets, process creation, process-memory access, signal sending, mount,
# namespaces, io_uring, bpf, device ioctl, or privilege-changing operations.
SYSCALLS = (
    'read', 'write', 'readv', 'writev', 'close', 'close_range',
    'pipe2', 'epoll_create1', 'epoll_ctl', 'epoll_wait', 'epoll_pwait', 'eventfd2', 'sysinfo', 'fstat', 'newfstatat', 'statx',
    'lseek', 'pread64', 'openat', 'access', 'faccessat', 'faccessat2',
    'readlink', 'readlinkat', 'getdents64', 'mmap', 'mprotect', 'munmap',
    'mremap', 'brk', 'madvise', 'rt_sigaction', 'rt_sigprocmask', 'rt_sigreturn',
    'sigaltstack', 'futex', 'futex_waitv', 'set_tid_address', 'set_robust_list',
    'rseq', 'getrandom', 'clock_gettime', 'clock_nanosleep',
    'nanosleep', 'sched_yield', 'sched_getaffinity', 'getpid', 'gettid',
    'getppid', 'getpgrp', 'getpgid', 'getuid', 'geteuid', 'getgid', 'getegid', 'uname', 'getcwd',
    'arch_prctl', 'execve', 'exit', 'exit_group',
)
ALLOW = 0x7fff0000
DENY = 0x50000 | errno.EPERM
# glibc pthread clone: VM, FS, FILES, SIGHAND, THREAD, SYSVSEM, SETTLS,
# PARENT_SETTID, CHILD_CLEARTID. Exact equality excludes process/namespace flags.
THREAD_FLAGS = 0x3d0f00

class _Rules(ctypes.Structure):
    _fields_ = [('handled_access_fs', ctypes.c_uint64)]

class _PathRule(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('allowed_access', ctypes.c_uint64), ('parent_fd', ctypes.c_int)]

class _Compare(ctypes.Structure):
    _fields_ = [('arg', ctypes.c_uint), ('op', ctypes.c_int),
                ('datum_a', ctypes.c_uint64), ('datum_b', ctypes.c_uint64)]

def runtime_paths():
    machine = platform.machine()
    if machine not in ('aarch64', 'x86_64'):
        raise OSError('unsupported native Linux architecture')
    triple, loader = {'aarch64': ('aarch64-linux-gnu', 'ld-linux-aarch64.so.1'),
                      'x86_64': ('x86_64-linux-gnu', 'ld-linux-x86-64.so.2')}[machine]
    libraries = Path('/usr/lib') / triple
    dynamic_loader = libraries / loader
    if not libraries.is_dir() or not dynamic_loader.is_file():
        raise OSError('supported Linux dynamic runtime unavailable')
    return libraries.resolve(), dynamic_loader.resolve()

def python_runtime():
    executable = Path('/usr/bin/python3').resolve()
    # Only the distribution's versioned system interpreter and stdlib are trusted.
    version = executable.name.removeprefix('python')
    if not version or any(c not in '0123456789.' for c in version):
        raise OSError('supported Linux system Python unavailable')
    stdlib = Path('/usr/lib') / ('python' + version)
    if not executable.is_file() or not stdlib.is_dir():
        raise OSError('supported Linux Python standard library unavailable')
    return executable, stdlib

class Policy:
    """Preload libraries in the dedicated single-thread host, enforce in child."""
    def __init__(self, executable, read_roots, read_files=(), *, threads=False):
        if len(list(Path('/proc/self/task').iterdir())) != 1:
            raise OSError('Linux probes require a dedicated single-thread helper')
        libraries, loader = runtime_paths()
        executable = Path(executable).resolve()
        self.grants = [(executable, 5), (loader, 5), (libraries, 12)]
        self.grants += [(Path(p).resolve(), 12) for p in read_roots]
        self.grants += [(Path(p).resolve(), 4) for p in read_files]
        self.grants += [(Path('/dev/urandom'), 4)]
        if Path('/etc/ld.so.cache').is_file():
            self.grants.append((Path('/etc/ld.so.cache'), 4))
        for path, rights in self.grants:
            if path == Path('/') or not path.exists() or (rights == 12 and not path.is_dir()):
                raise OSError('invalid trusted Linux runtime grant')
        self.libc = ctypes.CDLL(None, use_errno=True)
        self.sec = ctypes.CDLL('libseccomp.so.2', use_errno=True)
        self.sec.seccomp_init.argtypes = [ctypes.c_uint32]
        self.sec.seccomp_init.restype = ctypes.c_void_p
        self.sec.seccomp_syscall_resolve_name.argtypes = [ctypes.c_char_p]
        self.sec.seccomp_syscall_resolve_name.restype = ctypes.c_int
        self.sec.seccomp_rule_add_array.argtypes = [ctypes.c_void_p, ctypes.c_uint32,
                                                   ctypes.c_int, ctypes.c_uint,
                                                   ctypes.POINTER(_Compare)]
        self.sec.seccomp_load.argtypes = [ctypes.c_void_p]
        self.sec.seccomp_release.argtypes = [ctypes.c_void_p]
        self.threads = threads
        self.abi = self.libc.syscall(444, 0, 0, 1)
        if self.abi < 3:
            raise OSError('Landlock ABI >= 3 unavailable')

    @staticmethod
    def _check(value):
        if value < 0:
            raise OSError('Linux confinement installation failed')
        return value

    def __call__(self):
        self._check(self.libc.prctl(38, 1, 0, 0, 0))  # no_new_privs
        # All filesystem rights through ABI 3, including REFER and TRUNCATE.
        # Later device ioctl operations are independently denied by seccomp.
        rules = _Rules((1 << 15) - 1)
        fd = self._check(self.libc.syscall(444, ctypes.byref(rules), ctypes.sizeof(rules), 0))
        try:
            for path, rights in self.grants:
                path_fd = os.open(path, os.O_PATH | os.O_CLOEXEC)
                try:
                    rule = _PathRule(rights, path_fd)
                    self._check(self.libc.syscall(445, fd, 1, ctypes.byref(rule), 0))
                finally:
                    os.close(path_fd)
            self._check(self.libc.syscall(446, fd, 0))
        finally:
            os.close(fd)
        ctx = self.sec.seccomp_init(DENY)
        if not ctx:
            raise OSError('seccomp allocation failed')
        try:
            def add(name, action, comparison=None):
                number = self.sec.seccomp_syscall_resolve_name(name.encode())
                if number >= 0:
                    self._check(self.sec.seccomp_rule_add_array(
                        ctx, action, number, int(comparison is not None),
                        ctypes.byref(comparison) if comparison is not None else None))
            for name in SYSCALLS:
                add(name, ALLOW)
            add('prlimit64', ALLOW, _Compare(0, 4, 0, 0))
            for command in (1, 2, 3):  # F_GETFD, F_SETFD, F_GETFL only
                add('fcntl', ALLOW, _Compare(1, 4, command, 0))
            if self.threads:
                add('clone', ALLOW, _Compare(0, 4, THREAD_FLAGS, 0))
                # libc must fall back to clone, where flags are inspected.
                add('clone3', 0x50000 | errno.ENOSYS)
            self._check(self.sec.seccomp_load(ctx))
        finally:
            self.sec.seccomp_release(ctx)
