#!/usr/bin/env python3
"""Check this integration's links, owned edits and preserved evidence; no reruns."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BUILD = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/connected/pretraining'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    ledger = json.loads((HERE / 'PRETRAINING-EVIDENCE-EDITS.json').read_text())
    before = json.loads((HERE / 'development/PRETRAINING-EVIDENCE-BEFORE.json').read_text())['files']
    concurrent = {x['path']: x for x in json.loads(
        (HERE / 'development/PRETRAINING-EVIDENCE-CONCURRENT.json').read_text())['files']}
    documents = list(HERE.glob('PRETRAINING-EVIDENCE-*.md')) + [BUILD / 'README.md']
    source_dir = ROOT / 'sources/37-ethical-minimum-primary-2026-10-06/pretraining-evidence'
    documents.append(source_dir / 'README.md')
    texts = [(p, p.read_text()) for p in documents]
    for entry in ledger['edits']:
        p = ROOT / entry['path']
        assert p.read_text().count(entry['after']) == 1, entry['path']
        texts.append((p, entry['after']))
    recovered = {}
    for rel, snapshot in before.items():
        assert sha(snapshot['text'].encode()) == snapshot['sha256'], rel
        text = (ROOT / rel).read_text()
        for entry in reversed(ledger['edits']):
            if entry['path'] == rel:
                assert text.count(entry['after']) == 1, rel
                text = text.replace(entry['after'], entry['before'], 1)
        if rel in concurrent:
            assert sha(text.encode()) == concurrent[rel]['projected_sha256'], rel
            for change in reversed(concurrent[rel]['changes']):
                assert text.count(change['after']) == 1, rel
                text = text.replace(change['after'], change['before'], 1)
        recovered[rel] = text == snapshot['text']
    assert all(recovered.values()), recovered

    links = set()
    for p, text in texts:
        targets = re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)', text)
        targets += re.findall(r'^\[[^\]]+\]:\s+(\S+)', text, re.M)
        for raw in targets:
            url = urlsplit(raw.strip('<>'))
            if url.scheme or url.netloc:
                continue
            target = (p.parent / unquote(url.path)).resolve() if url.path else p
            assert target.exists(), (str(p.relative_to(ROOT)), raw)
            if url.fragment and target.suffix == '.md':
                headings = re.findall(r'^#+\s+(.+?)\s*$', target.read_text(), re.M)
                anchors = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                assert unquote(url.fragment) in anchors, (str(p.relative_to(ROOT)), raw)
            links.add((str(p.relative_to(ROOT)), raw))

    manifest_bytes = (BUILD / 'INPUTS.json').read_bytes()
    manifest = json.loads(manifest_bytes)
    receipt = json.loads((BUILD / 'verification.json').read_text())
    assert receipt['build_status'] == 'passed'
    assert receipt['manifest_sha256'] == sha(manifest_bytes)
    assert receipt['checker_sha256'] == sha((BUILD / 'check.py').read_bytes())
    assert len(manifest['sources']) == len(receipt['modules']) == 60
    pins = 0
    for item in manifest['sources']:
        live = (ROOT / item['path']).read_bytes()
        assert sha(live) == item['sha256']
        assert live == (BUILD / item['snapshot']).read_bytes()
        pins += 1
    for item in manifest['receipt_sources']:
        assert sha((BUILD / item['saved']).read_bytes()) == item['sha256']
        pins += 1
    for item in receipt['modules']:
        assert item['checked']
        assert sha((BUILD / item['log']).read_bytes()) == item['log_sha256']
    assert sum(len(x.get('require_empty', [])) for x in manifest['sources']) == 39
    new = next(x for x in receipt['modules'] if x['module'] == 'PretrainingEvidence')
    assert len(new['axioms_by_declaration']) == 16
    assert {a for deps in new['axioms_by_declaration'].values() for a in deps} == {'propext', 'Quot.sound'}
    assert receipt['assumption_free_foundation_established'] is False

    raw = json.loads((source_dir / 'manifest.json').read_text())
    data = (source_dir / raw['file']).read_bytes()
    assert len(data) == raw['bytes'] and sha(data) == raw['sha256']
    independent = json.loads((HERE / 'pretraining-review/results.json').read_text())
    assert independent['status'] == 'passed'
    assert (independent['four_pair_schedules'], independent['completed'], independent['blocked']) == (256, 176, 80)
    byname = {x['module'] + '.lean': x for x in manifest['sources']}
    for name, expected in independent['source_sha256'].items():
        assert byname[name]['sha256'] == expected
        pins += 1
    local = json.loads((BUILD / 'inputs/pretraining-verification.json').read_text())
    assert local['status'] == 'passed' and local['compared_coordinates'] == 5632
    assert len(local['modules']) == 28 and local['new_theorems'] == 16
    result = dict(status='passed', scope='Links, owned-fragment recovery and saved evidence; no scientific rerun.',
                  local_link_targets=len(links), owned_edits=len(ledger['edits']), recovered_files=recovered,
                  concurrent_changes_preserved=list(concurrent),
                  checked_source_and_receipt_pins=pins, source_original_sha256=raw['sha256'],
                  combined_modules=60, new_theorem_audits=16, retained_empty_contracts=39,
                  complete_schedules=176, blocked_schedules=80,
                  complete_foundation_established=False,
                  checker_sha256=sha(Path(__file__).read_bytes()),
                  documents={str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in documents})
    (HERE / 'PRETRAINING-EVIDENCE-CHECKS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['documents', 'recovered_files']}))


if __name__ == '__main__':
    main()
