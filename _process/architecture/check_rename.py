#!/usr/bin/env python3
"""Verify the directory renames of 9 October 2026 against their base commit.

The receipt holds the substitution rules, every file whose bytes changed and
every reviewed hash that changed with them. Each file is re-derived from its
bytes at the base commit: the rules are applied to the whole text ("paths") or
only to Markdown link targets outside quotations ("links"), then the hashes it
carried are applied when the file is a register. The result must match the
recorded hash. A carried hash must move exactly from a file's hash before the
rename to its hash after it; any other change is listed as reviewed, with a note.
Files edited in the same change are compared at the substitution step only.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RECEIPT = Path(__file__).with_name('rename-2026-10-09.json')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True).stdout


def blobs(commit, paths):
    """Bytes of each path at a commit, read through one git process."""
    request = ''.join(f'{commit}:{p}\n' for p in paths).encode()
    out = subprocess.run(['git', 'cat-file', '--batch'], cwd=ROOT, input=request,
                         capture_output=True, check=True).stdout
    result, at = {}, 0
    for path in paths:
        header_end = out.index(b'\n', at)
        size = int(out[at:header_end].split()[2])
        result[path] = out[header_end + 1:header_end + 1 + size]
        at = header_end + 2 + size
    return result


def transforms(receipt):
    rules = [(re.compile(pattern), new) for pattern, new in receipt['rules']]
    inline = re.compile(receipt['links']['inline'])
    definition = re.compile(receipt['links']['definition'])
    quotation = re.compile(receipt['links']['quotation'])

    def paths(text):
        for rule, new in rules:
            text = rule.sub(new, text)
        return text

    def links(text):
        lines = []
        for line in text.splitlines(keepends=True):
            if not quotation.match(line):
                line = inline.sub(lambda m: m[1] + paths(m[2]) + m[3], line)
                line = definition.sub(lambda m: m[1] + paths(m[2]), line)
            lines.append(line)
        return ''.join(lines)

    return {'paths': paths, 'links': links, 'none': lambda text: text}


def carry(text, pins):
    """Apply carried hashes to a register at the places its kind names."""
    data = json.loads(text)
    for pin in pins:
        if pin['kind'] == 'record-reference':
            [entry] = [r for r in data['references'] if r['path'] == pin['key']]
            field = 'sha256'
        elif pin['kind'] == 'catalogue-source':
            [entry] = [r for r in data if r['source'] == pin['key']]
            field = 'source_sha256'
        else:
            entry = data[{'chain-source': 'reviewed_sources', 'inventory-output': 'catalogue_output_sha256'}[pin['kind']]]
            field = pin['key']
        assert entry[field] == pin['from'], pin
        entry[field] = pin['to']
    return json.dumps(data, ensure_ascii=False, indent=2) + '\n'


def main():
    receipt = json.loads(RECEIPT.read_text())
    apply = transforms(receipt)
    files = {f['to']: f for f in receipt['files']}
    pins = {}
    for pin in receipt['pins']:
        pins.setdefault(pin['register'], []).append(pin)
    before = blobs(receipt['base_commit'], [f['from'] for f in receipt['files']])
    for f in receipt['files']:
        old = before[f['from']]
        assert sha(old) == f['sha256_before'], ('base bytes differ', f['from'])
        text = apply[f['transform']](old.decode())
        if f['to'] in pins:
            text = carry(text, pins[f['to']])
        assert sha(text.encode()) == f['sha256_after'], ('not the recorded substitution', f['to'])
    for pin in receipt['pins']:
        f = files[pin['key']]
        assert (pin['from'], pin['to']) == (f['sha256_before'], f['sha256_after']), ('hash carried without substitution', pin)
    for pin in receipt['reviewed']:
        assert pin['note'].strip(), ('reviewed change needs a note', pin)
    added = git('log', '--diff-filter=A', '--format=%H', '--', str(RECEIPT.relative_to(ROOT))).decode().split()
    commit = added[-1] if added else None
    present = set(git('ls-tree', '-r', '--name-only', commit).decode().splitlines()) if commit else \
        set(git('ls-files').decode().splitlines())
    old_tree = git('ls-tree', '-r', '--name-only', receipt['base_commit'], '--', receipt['moves'][0][0]).decode().split('\n')
    missing = []
    for path in filter(None, old_tree):
        for old, new in receipt['moves']:
            if path.startswith(old + '/'):
                path = new + path[len(old):]
        if path not in present:
            missing.append(path)
    assert not missing, ('moved paths missing', missing[:10])
    current = blobs(commit, [f['to'] for f in receipt['files']]) if commit else \
        {f['to']: (ROOT / f['to']).read_bytes() for f in receipt['files']}
    for f in receipt['files']:
        if 'edited' not in f:
            assert sha(current[f['to']]) == f['sha256_after'], ('file differs from the rename', f['to'])
    print(json.dumps({'status': 'passed', 'checked_at': commit or 'working tree',
                      'files': len(receipt['files']), 'carried_hashes': len(receipt['pins']),
                      'reviewed_hashes': len(receipt['reviewed']),
                      'edited_in_same_change': sum('edited' in f for f in receipt['files']),
                      'moved_paths': len([p for p in old_tree if p])}, indent=2))


if __name__ == '__main__':
    main()
