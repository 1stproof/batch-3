"""Persisted NL capability policy, shared by maintained entrypoints and runtimes.

This is a tool capability, not a proof grade. Ancestor NL policies cannot be
shadowed by descendants. General provider shells remain instruction-bound.
"""
from pathlib import Path
import json

MARKER = '.merlean-capabilities.json'
NOTICE = ('NL mode: Lean execution and formalization are disabled. Preserve discovery, '
          'independent review, selected obligations, unknowns and original-scope/Silver gates. '
          'No automatic certificate deselection, grade downgrade or Gold claim.')


def config_nl(config=None):
    value = (config or {}).get('nl_only', False)
    if type(value) is not bool:
        raise ValueError('nl_only must be boolean')
    return value


def nl_only(*paths, config=None):
    disabled = config_nl(config)
    for raw in (*paths, Path.cwd()):
        if raw is None:
            continue
        lexical = Path(raw).absolute()
        roots = set()
        for path in (lexical, lexical.resolve()):
            if path.is_file():
                path = path.parent
            roots.update((path, *path.parents))
        for root in roots:
            host = root / 'host-config.json'
            if host.is_symlink():
                raise ValueError('host capability config cannot be a symlink')
            if host.is_file():
                host_config = json.loads(host.read_text())
                if not isinstance(host_config, dict):
                    raise ValueError('invalid host capability config')
                disabled = config_nl(host_config) or disabled
            marker = root / MARKER
            if marker.is_symlink():
                raise ValueError('capability policy cannot be a symlink')
            if marker.exists():
                value = json.loads(marker.read_text())
                if (not isinstance(value, dict) or set(value) != {'schema_version', 'nl_only'}
                        or type(value.get('schema_version')) is not int or value['schema_version'] != 1):
                    raise ValueError('invalid persisted capability policy')
                disabled = config_nl(value) or disabled
    return disabled


def require_lean(*paths, config=None):
    if nl_only(*paths, config=config):
        raise ValueError(NOTICE)


def initialize(root, requested=None):
    """Explicit fresh policy only; existing plans/campaigns cannot silently migrate."""
    inherited = nl_only(root)
    root = Path(root).resolve()
    if requested is not None and type(requested) is not bool:
        raise ValueError('NL selection must be boolean or None')
    if inherited and requested is False:
        raise ValueError('cannot enable Lean inside persisted NL policy')
    marker = root / MARKER
    if marker.exists():
        current = config_nl(json.loads(marker.read_text()))
        if inherited and not current:
            raise ValueError('conflicting persisted capability; use a separate fresh project')
        if requested is not None and requested != current:
            raise ValueError('capability policy is immutable; use a separate fresh project')
        return inherited
    if requested is not True and not inherited:
        return False
    existing = ('host-config.json', 'statements.json', '.merlean-offline.json', 'progress.json',
                'campaign/registry.json', 'registry.json')
    if any((root / name).exists() for name in existing) or any(root.glob('*_data/statements.json')):
        raise ValueError('cannot migrate existing research to NL; use a separate fresh project')
    root.mkdir(parents=True, exist_ok=True)
    with marker.open('x') as stream:
        json.dump({'schema_version': 1, 'nl_only': True}, stream, indent=2)
        stream.write('\n')
    return True


def continuation_nl(old, requested=None):
    current = config_nl(old)
    if requested is not None and (type(requested) is not bool or requested != current):
        raise ValueError('continuation must inherit unchanged NL capability; use a fresh campaign')
    return current


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('-NL', '--nl', action='store_true', default=None)
    args = parser.parse_args()
    print('nl' if initialize(args.root, args.nl) else 'lean-enabled')
