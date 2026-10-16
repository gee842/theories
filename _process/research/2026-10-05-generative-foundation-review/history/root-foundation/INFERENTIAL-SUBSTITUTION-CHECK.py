#!/usr/bin/env python3
"""Verify the frozen substitution build and owned integration; never recompile."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))
from tools.research import generative_chain as chain
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
THEORY = ROOT / 'theories/becoming/chapters/GENERATED-LOGIC.md'
SOURCE = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md'
STUDY = HERE / 'RECOGNITIONAL-BINDING-INTEGRATION.md'
RECORD = ROOT / 'theories/becoming/results/records/binding-preserving-substitution.json'
BEFORE = HERE / 'development/inferential-substitution-before'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def parsed_audits(log):
    out = {n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", log)}
    out.update({n: [x.strip() for x in ds.split(',')]
                for n, ds in re.findall(r"'([^']+)' depends on axioms: \[(.*?)\]", log, re.S)})
    return out

def main():
    proof = LEAN / 'inferential-substitution-checks/20261008T181823.552825Z/receipt.json'
    receipt = json.loads(proof.read_text())
    assert receipt['passed'] and receipt['new_theorems'] == 9
    assert receipt['total_audits'] == 19 and receipt['total_empty_axiom_audits'] == 13
    assert receipt['inherited_audits'] == 10
    assert sha((LEAN / 'check_inferential_substitution.py').read_bytes()) == receipt['checker_sha256']
    expected = [('InferentialGrounds.lean', 10), ('InferentialSubstitution.lean', 9)]
    for item, (name, count) in zip(receipt['modules'], expected):
        source = ROOT / item['source']
        assert source.name == name
        assert sha(source.read_bytes()) == sha((ROOT / item['snapshot']).read_bytes()) == item['sha256']
        assert item['passed'] and item['exit_code'] == 0 and item['source_unchanged_during_check']
        log = (ROOT / item['log']).read_text()
        assert sha(log.encode()) == item['log_sha256']
        audits = parsed_audits(log)
        reported = {n: [] for n in item['empty_axiom_audits']}
        reported.update(item['standard_axiom_audits'])
        assert audits == reported
        names = re.findall(r'^#print axioms (\S+)$', source.read_text(), re.M)
        assert set(names) == set(audits) and len(names) == len(set(names)) == count
        assert all(set(ds) <= {'Quot.sound'} for ds in audits.values())
        assert 'warning:' not in log and 'error:' not in log
        assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|^\s*(axiom|constant)\s', source.read_text(), re.M)
    assert len(receipt['modules']) == 2
    assert len(re.findall(r'^theorem ', (LEAN / 'InferentialSubstitution.lean').read_text(), re.M)) == 9
    # Credit the prior result, verify its unchanged evidence, do not recount it.
    prior_path = LEAN / 'recognitional-binding-checks/20261008T120159.334011Z/receipt.json'
    prior = json.loads(prior_path.read_text())
    assert prior['passed'] and prior['total_empty_axiom_audits'] == 21
    assert prior['modules'][0]['sha256'] == receipt['modules'][0]['sha256']
    for item in prior['modules']:
        assert sha((ROOT / item['snapshot']).read_bytes()) == item['sha256']
        assert sha((ROOT / item['source']).read_bytes()) == item['sha256']
        log = (ROOT / item['log']).read_text()
        assert sha(log.encode()) == item['log_sha256']
        assert parsed_audits(log) == {n: [] for n in item['empty_axiom_audits']}
    manifest = json.loads((BEFORE / 'manifest.json').read_text())
    for item in manifest:
        assert sha((ROOT / item['snapshot']).read_bytes()) == item['sha256']
    assert SOURCE.read_bytes().startswith((BEFORE / SOURCE.name).read_bytes())
    assert STUDY.read_bytes().startswith((BEFORE / STUDY.name).read_bytes())
    assert re.findall(r'^## (\d+)\.', THEORY.read_text(), re.M) == [str(i) for i in range(1,16)]
    old_report = json.loads((BEFORE / 'RECOGNITIONAL-BINDING-CHECKS.json').read_text())
    prior_document_agreement = {i['path']: i['sha256'] == old_report['documents'][i['path']]
                                for i in manifest if i['path'] in old_report['documents']}
    edits = json.loads((HERE / 'INFERENTIAL-SUBSTITUTION-INDEX-EDITS.json').read_text())
    data = chain.read_data()
    entry = next(e for section in data['sections'] for e in section['entries'] if e['id'] == 'F01')
    assert entry == edits['entry_after']
    expected_row = next(x for x in chain.render(data).splitlines() if x.startswith('| F01 |'))
    actual_row = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith('| F01 |'))
    assert actual_row == expected_row == edits['new_rendered_row']
    assert edits['other_entries_preserved'] and edits['other_rendered_lines_preserved'] and edits['discovery_unchanged']
    for path, fingerprint in edits['authored_fingerprints'].items():
        assert fingerprint == sha((ROOT / path).read_bytes()) == data['reviewed_sources'][path]
    for fragment in edits['shared_fragments']:
        assert (ROOT / fragment['path']).read_text().count(fragment['text']) == 1
        assert fragment['insertion_only']
    documents = [THEORY, SOURCE, STUDY]
    snippets = [(p,p.read_text()) for p in documents]
    snippets.extend((ROOT/f['path'],f['text']) for f in edits['shared_fragments'])
    links = []
    for doc, text in snippets:
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if target.startswith(('https://','http://')): continue
            name, _, anchor = unquote(target).partition('#')
            dest = (doc.parent / name).resolve() if name else doc
            assert dest.is_relative_to(ROOT) and dest.exists(), (doc,target)
            if anchor and dest.suffix == '.md':
                assert anchor in chain.heading_ids(dest), (doc,target)
            links.append(dict(document=str(doc.relative_to(ROOT)),target=target))
    focused = subprocess.run([sys.executable,'-B',str(ROOT/'tools/research/research.py'),'check','--ids','binding-preserving-substitution'],cwd=ROOT,text=True,capture_output=True)
    focused_data = json.loads(focused.stdout)
    assert focused.returncode == 0, focused.stdout + focused.stderr
    assert not focused_data['errors'] and not focused_data['source_drift']
    pending = chain.changes(data)
    errors = chain.validate(data)
    owned_errors = [e for e in errors if any(path in e for path in edits["authored_fingerprints"])]
    assert not owned_errors, owned_errors
    combined = {}
    if pending['modified_sources'] or pending['missing_sources']:
        before = chain.OUTPUT.read_bytes()
        for mode in ('--render','--check'):
            p = subprocess.run([sys.executable,'-B',str(HERE/'build_generative_chain.py'),mode],cwd=ROOT,text=True,capture_output=True)
            assert p.returncode == 2
            combined[mode] = json.loads(p.stdout)
        assert chain.OUTPUT.read_bytes() == before
    report = dict(passed_owned_scope=True,new_theorems=9,inherited_declaration_audits=10,total_audits=19,empty_reports=13,quot_sound_only=6,
                  receipt=str(proof.relative_to(ROOT)),receipt_sha256=sha(proof.read_bytes()),
                  prior_unchanged_receipt=str(prior_path.relative_to(ROOT)),prior_receipt_sha256=sha(prior_path.read_bytes()),
                  historical_editions=manifest,prior_document_agreement=prior_document_agreement,
                  documents={str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in documents+[RECORD]},
                  local_links=links,paired_entry='F01',focused_registry_check=focused_data,
                  pending_shared_reviews=pending,global_chain_link_errors=errors,combined_chain_checks=combined,
                  complete_presuppositionless_grounding=False,whole_table_certified=False,independent_agent_review=False)
    (HERE/'INFERENTIAL-SUBSTITUTION-CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed_owned_scope=True,new_theorems=9,total_audits=19,local_links=len(links),focused_registry_check='passed',unrelated_registry_drift=len(focused_data.get('unrelated_source_drift',[])),pending_chain_sources=len(pending['modified_sources']),whole_table_certified=False)))

if __name__ == '__main__':
    main()
