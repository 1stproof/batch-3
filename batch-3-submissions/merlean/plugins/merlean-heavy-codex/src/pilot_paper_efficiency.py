"""Lossless paper input aliases and explicit unchanged-source dispositions."""
import hashlib


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def compact_artifacts(payload):
    """Share only byte-identical long strings; no scientific text is summarized."""
    artifacts = payload.get('artifacts', {})
    if payload.get('artifact_aliases'):
        for name in payload['artifact_aliases']:
            artifact_text(payload, name)
        return payload  # Already encoded: preserve its exact names and bindings.
    unique, aliases, seen = {}, {}, {}
    for name, text in artifacts.items():
        if not isinstance(text, str):
            raise ValueError('paper context artifact must be text')
        key = digest(text)
        target = seen.get(key)
        if len(text) >= 4096 and target is not None and unique[target] == text:
            aliases[name] = {'artifact': target, 'sha256': key, 'media_type': 'text/plain'}
        else:
            unique[name] = text
            seen[key] = name
    if not aliases:
        return payload
    return {**payload, 'artifacts': unique, 'artifact_aliases': aliases,
            'artifact_alias_instructions': 'Each artifact_aliases entry has exactly the UTF-8 bytes of its named '
            'artifacts target, verified by sha256. Read that full target once for all identical aliases. '
            'These are exact duplicate files, not summaries. The original alias name remains requestable as work/<name>.'}


def artifact_text(payload, name):
    artifacts = payload.get('artifacts', {})
    aliases = payload.get('artifact_aliases', {})
    if not isinstance(artifacts, dict) or not isinstance(aliases, dict):
        raise ValueError('invalid paper artifact maps')
    if name in artifacts:
        if name in aliases:
            raise ValueError('paper artifact alias conflicts with content')
        return artifacts[name]
    if name not in aliases:
        return None
    ref = aliases[name]
    if (not isinstance(ref, dict) or set(ref) != {'artifact', 'sha256', 'media_type'}
            or ref['media_type'] != 'text/plain' or not isinstance(ref['artifact'], str)
            or not isinstance(ref['sha256'], str) or ref['artifact'] in aliases):
        raise ValueError('invalid paper artifact alias')
    text = artifacts.get(ref['artifact'])
    if not isinstance(text, str) or digest(text) != ref['sha256']:
        raise ValueError('paper artifact alias bytes changed')
    return text


def revision_edits(answer, manuscript):
    """Omitting source requires explicit equality and substantive author disposition."""
    unchanged = answer.get('unchanged_manuscript_sha256')
    if unchanged is None:
        return True  # Existing full-source response contract stays valid.
    if 'tex' in answer or unchanged != digest(manuscript):
        raise ValueError('unchanged revision conflicts with current manuscript')
    if (not isinstance(answer.get('revision_summary'), str) or len(answer['revision_summary'].strip()) < 20
            or not isinstance(answer.get('no_change_reason'), str) or len(answer['no_change_reason'].strip()) < 20
            or not isinstance(answer.get('responses'), list)):
        raise ValueError('unchanged revision requires substantive original-author disposition')
    return False


def author_sources(root, raw_checkpoint):
    """Optional exact restoration sources; never infer a missing historical argument."""
    import json
    from pathlib import Path
    import pilot_document_tools as documents
    root=Path(root)
    result={};unavailable=[]
    raw=root/'raw-source.tex'
    manifest_path=Path(raw_checkpoint['manifest']) if raw_checkpoint else None
    if manifest_path is not None and manifest_path.exists() and raw.exists():
        manifest_bytes=documents.regular_bytes(manifest_path)
        if documents.digest(manifest_bytes)!=raw_checkpoint['manifest_sha256']:
            raise ValueError('preserved raw manifest changed')
        manifest=json.loads(manifest_bytes)
        matches=[item for item in manifest['files'] if item.get('kind')=='manuscript'
                 and item.get('source')==manifest['source']]
        if len(matches)!=1:
            raise ValueError('preserved raw manuscript binding is ambiguous')
        body=documents.regular_bytes(raw)
        if documents.digest(body)!=matches[0]['sha256']:
            raise ValueError('preserved raw author source changed')
        result['preserved-author:raw']=body
    else:
        unavailable.append('preserved-author:raw')
    before=root/'work/05-pre-shrink-inventory.json'
    found=False
    if before.exists():
        expected=json.loads(documents.regular_bytes(before))['source_sha256']
        for path in sorted(root.glob('draft-*.tex')):
            body=documents.regular_bytes(path)
            if documents.digest(body)==expected:
                result['preserved-author:pre-shrink']=body
                found=True
                break
    if not found:
        unavailable.append('preserved-author:pre-shrink')
    for body in result.values():body.decode('utf-8')
    return result,unavailable
