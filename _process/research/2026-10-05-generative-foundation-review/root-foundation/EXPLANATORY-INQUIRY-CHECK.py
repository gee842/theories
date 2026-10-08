#!/usr/bin/env python3
"""Check this study's documents, owned index edits and frozen Lean receipt.
Does not rerun proofs or certify concurrently edited research branches.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
OUTPUT = HERE / 'EXPLANATORY-INQUIRY-CHECKS.json'
RECEIPT = LEAN / 'explanatory-inquiry-checks/20261007T212138.087503Z/receipt.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    docs = [ROOT / 'theories/becoming/chapters/EXPLANATORY-NECESSITY.md',
            ROOT / 'sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md',
            HERE / 'EXPLANATORY-INQUIRY-INTEGRATION.md', HERE / 'EXPLANATORY-VARIATION-INTEGRATION.md']
    edits = json.loads((HERE / 'EXPLANATORY-INQUIRY-INDEX-EDITS.json').read_text())
    contents = [(p, p.read_text()) for p in docs]
    for item in edits['shared_file_insertions']:
        p = ROOT / item['path']
        assert item['preserved_other_bytes'] and item['inserted_text'] in p.read_text(), item['path']
        contents.append((p, item['inserted_text']))
    links = []
    for p, content in contents:
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if re.match(r'^[a-zA-Z]+:', ref):
                continue
            name, _, fragment = ref.partition('#')
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT), ref
            assert target.is_file() or target == OUTPUT, (p, ref)
            if fragment:
                assert unquote(fragment) in chain.heading_ids(target), (p, ref)
            links.append({'from': str(p.relative_to(ROOT)), 'reference': ref})
    receipt = json.loads(RECEIPT.read_text())
    assert receipt['passed'] and receipt['total_empty_axiom_audits'] == 128
    assert receipt['checker_sha256'] == sha(LEAN / 'check_explanatory_inquiry.py')
    bindings = []
    for m in receipt['modules']:
        source = ROOT / m['source']
        frozen = RECEIPT.parent / 'sources' / source.name
        log = RECEIPT.parent / (source.stem + '.log')
        assert sha(source) == sha(frozen) == m['sha256'], source
        assert m['passed'] and m['exit_code'] == 0 and m['source_unchanged_during_check']
        assert re.findall(r"'([^']+)' does not depend on any axioms", log.read_text()) == m['empty_axiom_audits']
        assert len(m['empty_axiom_audits']) == m['expected_audits']
        assert 'depends on axioms' not in log.read_text() and 'warning:' not in log.read_text()
        bindings.append({'source': m['source'], 'sha256': m['sha256'],
                         'log_sha256': sha(log), 'audits': m['expected_audits']})
    new_source = (LEAN / 'ExplanatoryInquiry.lean').read_text()
    new_names = re.findall(r'^theorem (\w+)', new_source, re.M)
    assert len(new_names) == len(set(new_names)) == 40
    audited = [name.rsplit('.', 1)[-1] for name in receipt['modules'][-1]['empty_axiom_audits']]
    assert audited[0] == 'calibrated_pair_exact' and set(audited[1:]) == set(new_names)
    data = chain.read_data()
    rows = {e['id']: e for s in data['sections'] for e in s['entries']}
    assert edits['preserved_other_entries']
    for key, value in edits['rows_after'].items():
        assert rows[key] == value, key
    result = {'passed': True, 'scope': 'This study only; global index freshness is a separate concurrent maintenance check.',
              'new_theorems': 40, 'inherited_audits': 88, 'total_empty_axiom_audits': 128,
              'receipt': str(RECEIPT.relative_to(ROOT)), 'receipt_sha256': sha(RECEIPT),
              'local_links_checked': len(links), 'links': links,
              'source_and_frozen_log_bindings': bindings,
              'owned_rows': ['C30', 'F22'], 'preserved_other_entries_at_edit': True,
              'sha256': {str(p.relative_to(ROOT)): sha(p) for p in docs + [Path(__file__), HERE / 'EXPLANATORY-INQUIRY-INDEX-EDITS.json']}}
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['passed', 'new_theorems', 'total_empty_axiom_audits', 'local_links_checked']}))

if __name__ == '__main__':
    main()
