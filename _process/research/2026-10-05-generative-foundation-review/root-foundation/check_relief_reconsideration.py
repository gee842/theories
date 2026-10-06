#!/usr/bin/env python3
"""Check the owned integration and source preservation; no scientific rerun."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / 'RELIEF-AND-RECONSIDERATION-CHECKS.json'
SOURCES = ROOT / 'sources/37-ethical-minimum-primary-2026-10-06/relief-reconsideration'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    ledger = json.loads((HERE / 'RELIEF-AND-RECONSIDERATION-EDITS.json').read_text())
    docs = list(HERE.glob('RELIEF-AND-*.md')) + [SOURCES / 'README.md']
    texts = [(p, p.read_text()) for p in docs]
    for edit in ledger['edits']:
        p = ROOT / edit['path']
        assert p.read_text().count(edit['new']) == 1, edit['path']
        texts.append((p, edit['new']))
    recovered = {}
    for prior in ledger['before']:
        assert sha(prior['text'].encode()) == prior['sha256'], prior['path']
        current = (ROOT / prior['path']).read_text()
        for edit in reversed(ledger['edits']):
            if edit['path'] == prior['path']:
                assert current.count(edit['new']) == 1, edit['path']
                current = current.replace(edit['new'], edit['old'], 1)
        recovered[prior['path']] = current == prior['text']
    assert all(recovered.values()), recovered

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

    imported = {}
    manifest = json.loads((SOURCES / 'manifest.json').read_text())
    for item in manifest['sources']:
        data = (SOURCES / item['file']).read_bytes()
        assert len(data) == item['bytes'] and sha(data) == item['sha256'], item['file']
        imported[item['file']] = item['sha256']
    result = {
        'status': 'passed',
        'scope': 'Owned integration fragments, local links and preservation hashes only; no scientific or ethical verification.',
        'owned_fragments': len(ledger['edits']),
        'recovered_files': recovered,
        'local_link_targets': len(links),
        'imported_source_hashes': imported,
        'cited_code_hashes_at_check': code,
        'documents': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in docs},
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'new_lean_declarations': 0,
        'new_empirical_runs': 0,
        'assumption_free_foundation_established': False,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in {'documents', 'cited_code_hashes_at_check'}}))


if __name__ == '__main__':
    main()
