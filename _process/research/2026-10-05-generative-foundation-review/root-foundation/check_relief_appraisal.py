#!/usr/bin/env python3
"""Preservation and link checks for the appraisal continuation only."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import difflib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / 'RELIEF-APPRAISAL-CHECKS.json'
SOURCE = ROOT / 'sources/37-ethical-minimum-primary-2026-10-06/relief-reconsideration'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    ledger = json.loads((HERE / 'RELIEF-APPRAISAL-EDITS.json').read_text())
    concurrent = {x['path']: x for x in json.loads(
        (HERE / 'development/RELIEF-APPRAISAL-CONCURRENT.json').read_text())['files']}
    docs = list(HERE.glob('RELIEF-*.md')) + list(SOURCE.rglob('README.md'))
    texts = [(p, p.read_text()) for p in docs]
    recovery = {}
    for item in ledger['before']:
        assert sha(item['text'].encode()) == item['sha256'], item['path']
        live = (ROOT / item['path']).read_text()
        for edit in reversed(ledger['edits']):
            if edit['path'] != item['path']:
                continue
            if edit['kind'] == 'append':
                assert live.endswith(edit['new']), item['path']
                live = live[:-len(edit['new'])]
            else:
                assert live.count(edit['new']) == 1, item['path']
                live = live.replace(edit['new'], edit['old'] if edit['kind'] == 'replace' else '', 1)
        if item['path'] in concurrent:
            extra = concurrent[item['path']]
            assert extra['before_sha256'] == item['sha256']
            assert sha(extra['projected_text'].encode()) == extra['projected_sha256']
            difference = ''.join(difflib.unified_diff(
                item['text'].splitlines(keepends=True), extra['projected_text'].splitlines(keepends=True),
                fromfile=item['path'] + ' before', tofile=item['path'] + ' concurrent', n=1))
            assert difference == extra['diff']
            recovery[item['path']] = live == extra['projected_text']
        else:
            recovery[item['path']] = live == item['text']
    assert all(recovery.values()), recovery
    texts += [(ROOT / e['path'], e['new']) for e in ledger['edits']]
    links = set()
    code = {}
    for p, text in texts:
        targets = re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)', text)
        targets += re.findall(r'^\[[^\]]+\]:\s+(\S+)', text, re.M)
        for raw in targets:
            url = urlsplit(raw.strip('<>'))
            if url.scheme or url.netloc:
                continue
            target = (p.parent / unquote(url.path)).resolve() if url.path else p
            assert target.exists() or target == OUTPUT, (p.name, raw)
            if url.fragment and target.suffix == '.md':
                headings = re.findall(r'^#+\s+(.+?)\s*$', target.read_text(), re.M)
                anchors = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                assert unquote(url.fragment) in anchors, (p.name, raw)
            links.add((str(p.relative_to(ROOT)), raw))
            if target.suffix in {'.lean', '.py'}:
                code[str(target.relative_to(ROOT))] = sha(target.read_bytes())
    originals = {}
    for manifest_path in SOURCE.rglob('manifest.json'):
        manifest = json.loads(manifest_path.read_text())
        for item in manifest['sources']:
            p = manifest_path.parent / item['file']
            data = p.read_bytes()
            assert len(data) == item['bytes'] and sha(data) == item['sha256'], p
            originals[str(p.relative_to(ROOT))] = item['sha256']
    result = dict(
        status='passed',
        scope='Local links, owned edits and imported-byte preservation; no scientific rerun or ethical verification.',
        owned_fragments=len(ledger['edits']), recovered_files=recovery,
        concurrent_changes_preserved=list(concurrent),
        local_link_targets=len(links), imported_sources=originals,
        cited_code_hashes_at_check=code,
        documents={str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in docs},
        checker_sha256=sha(Path(__file__).read_bytes()),
        new_lean_declarations=0, new_empirical_runs=0,
        assumption_free_foundation_established=False,
    )
    OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in {'documents', 'cited_code_hashes_at_check', 'imported_sources'}}))


if __name__ == '__main__':
    main()
