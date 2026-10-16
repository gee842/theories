#!/usr/bin/env python3
"""Check only the joining-refinement proof receipt and owned integration delta."""
from pathlib import Path
from collections import Counter
import hashlib, importlib.util, json, re, sys
from urllib.parse import unquote
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
RECEIPT = LEAN / 'explanatory-joining-refinement-checks/20261008T134730.060831Z/receipt.json'
OUT = HERE / 'EXPLANATORY-JOINING-REFINEMENT-CHECKS.json'
IDS = ['functional-joining-common-structure', 'multivalued-joining-common-structure',
       'joining-questions-survive-encoding', 'finite-joining-tree-lifting',
       'incidence-common-refinement', 'joining-open-map-factor', 'unanchored-incidence-collapse',
       'retained-reference-joining-recovery']
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    receipt = json.loads(RECEIPT.read_text())
    assert receipt['passed'] and receipt['total_declaration_audits'] == 256
    assert receipt['checker_sha256'] == sha(LEAN / 'check_explanatory_joining_refinement.py')
    assert receipt['total_empty_axiom_audits'] == 175 and receipt['total_standard_axiom_audits'] == 81
    bindings = []
    for m in receipt['modules']:
        p = ROOT / m['source']; frozen = RECEIPT.parent / 'sources' / p.name
        log = RECEIPT.parent / (p.stem + '.log'); txt = log.read_text()
        assert sha(p) == sha(frozen) == m['sha256'], p
        assert m['passed'] and m['exit_code'] == 0 and m['source_unchanged_during_check']
        assert 'error:' not in txt and 'warning:' not in txt
        empty = re.findall(r"'([^']+)' does not depend on any axioms", txt)
        standard = {n: [x.strip() for x in ds.split(',')] for n, ds in re.findall(r"'([^']+)' depends on axioms: \[([^\]]+)\]", txt)}
        assert empty == m['empty_axiom_audits'] and standard == m['standard_axiom_audits']
        assert len(empty) + len(standard) == m['expected_audits']
        assert all(set(x) <= {'propext', 'Quot.sound', 'Classical.choice'} for x in standard.values())
        bindings.append({'source': m['source'], 'sha256': m['sha256'], 'log_sha256': sha(log)})
    new, inherited = receipt['modules'][-4:], receipt['modules'][:-4]
    assert sum(x['expected_audits'] for x in new) == 43
    assert sum(x['expected_audits'] for x in inherited) == 213
    assert sum(len(x['empty_axiom_audits']) for x in new) == 9
    assert Counter(tuple(sorted(a)) for x in new for a in x['standard_axiom_audits'].values()) == Counter({('propext',): 23, ('Quot.sound', 'propext'): 4, ('Classical.choice', 'Quot.sound', 'propext'): 7})
    older = json.loads((LEAN / 'explanatory-joining-branches-checks/20261008T130611.816353Z/receipt.json').read_text())
    oldmap = {m['source']: m for m in older['modules']}
    for m in inherited:
        for k in ['sha256', 'expected_audits', 'empty_axiom_audits', 'standard_axiom_audits']:
            assert m[k] == oldmap[m['source']][k]
    inventory = {}
    for m in new:
        ns = re.findall(r'^theorem (\w+)', (ROOT / m['source']).read_text(), re.M)
        assert len(ns) == len(set(ns)) == m['expected_audits']
        assert set(ns) == {n.rsplit('.', 1)[-1] for n in m['empty_axiom_audits'] + list(m['standard_axiom_audits'])}
        inventory[m['source']] = ns
    edits = json.loads((HERE / 'EXPLANATORY-JOINING-REFINEMENT-INDEX-EDITS.json').read_text())
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec); spec.loader.exec_module(chain)
    links = []
    for e in edits['owned_continuations']:
        p = ROOT / e['path']; txt = p.read_text(); delta = e['appended_text']
        assert delta and txt.endswith(delta) and e['prior_bytes_preserved']
        assert hashlib.sha256(txt[:-len(delta)].encode()).hexdigest() == e['before_sha256']
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', delta):
            if re.match(r'^[a-zA-Z]+:', ref): continue
            name, _, fragment = ref.partition('#'); target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and (target.is_file() or target == OUT), (p, ref)
            if fragment: assert unquote(fragment) in chain.heading_ids(target), (p, ref)
            links.append({'from': e['path'], 'reference': ref})
    for p, h in edits['reviewed_owned_sources'].items(): assert sha(ROOT / p) == h
    for edit in edits['record_edits']['updated_records']:
        p = ROOT / 'theories/becoming/results/records' / (edit['id']+'.json')
        assert sha(p) == edit['after_sha256'] and edit['claim_hypotheses_and_bindings_preserved']
    data = chain.read_data(); rows = {e['id']: e for s in data['sections'] for e in s['entries']}
    assert edits['preserved_other_entries'] and edits['preserved_other_rendered_lines']
    expected = chain.render(data).splitlines(); actual = chain.OUTPUT.read_text().splitlines()
    for k, after in edits['rows_after'].items():
        before = edits['rows_before'][k]; assert rows[k] == after
        for fld in ['claim_zh', 'claim_en', 'scope_zh', 'scope_en']: assert after[fld].startswith(before[fld])
        assert after['links'][:len(before['links'])] == before['links']
        assert [x for x in actual if x.startswith('| '+k+' |')] == [x for x in expected if x.startswith('| '+k+' |')]
    chapter = ROOT / 'theories/becoming/chapters/EXPLANATORY-NECESSITY.md'
    assert [int(n) for n in re.findall(r'^## (\d+)\.', chapter.read_text(), re.M)] == list(range(1, 101))
    sys.path.insert(0, str(ROOT))
    from tools.research import registry
    records, load_errors = registry.load_records(); errors, drift = registry.validate(records)
    assert not load_errors and not errors, (load_errors, errors)
    assert not [d for d in drift if d['id'] in IDS]
    record_hashes = {ident: sha(ROOT / 'theories/becoming/results/records' / (ident+'.json')) for ident in IDS}
    result = {'passed': True, 'scope': 'Owned proof sources, exact receipt/logs, result metadata and appended integration; no global freshness or independent scientific acceptance.',
      'new_declarations': 43, 'inherited_audits': 213, 'total_audits': 256, 'new_empty': 9, 'new_standard': 34, 'new_classical_choice': 7,
      'receipt': str(RECEIPT.relative_to(ROOT)), 'receipt_sha256': sha(RECEIPT), 'proof_bindings': bindings, 'new_inventory': inventory,
      'preserved_prior_study_and_chapter': True, 'preserved_prior_chain_contributions': True, 'owned_rows': ['C30', 'F22'],
      'local_links_checked': len(links), 'links': links, 'result_records': record_hashes,
      'reused_record': 'branching-tests-bisimulation', 'inherited_audit_inventories_unchanged': True, 'prior_record_claims_preserved': True, 'unrelated_registry_drift': drift,
      'pending_chain_changes': chain.changes(data),
      'sha256': {str((HERE / n).relative_to(ROOT)): sha(HERE / n) for n in ['EXPLANATORY-JOINING-REFINEMENT-CHECK.py', 'EXPLANATORY-JOINING-REFINEMENT-INDEX-EDITS.json', 'EXPLANATORY-JOINING-CONTEXTS-INTEGRATION.md']}}
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed','new_declarations','inherited_audits','total_audits','local_links_checked']}))

if __name__ == '__main__': main()
