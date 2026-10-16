#!/usr/bin/env python3
"""Documentary verification of the scoped argument; no new proof or Lean run."""
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
RECORDS = ROOT / 'theories/becoming/results/records'
THEORY = ROOT / 'theories/becoming/chapters/GENERATED-LOGIC.md'
SOURCE = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md'
STUDY = HERE / 'RECOGNITIONAL-BINDING-INTEGRATION.md'
BEFORE = HERE / 'development/binding-constitution-before'
OUTPUT = HERE / 'BINDING-CONSTITUTION-CHECKS.json'
IDS = ['constitutive-binding-assessment', 'binding-preserving-substitution']

def sha(raw): return hashlib.sha256(raw).hexdigest()
def audits(log):
    out = {n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", log)}
    out.update({n: [x.strip() for x in ds.split(',')]
                for n, ds in re.findall(r"'([^']+)' depends on axioms: \[(.*?)\]", log, re.S)})
    return out

def main():
    packages = [
        ('reflective-identity-checks/20261008T114343.985843Z/receipt.json', 'check_reflective_identity.py'),
        ('recognitional-binding-checks/20261008T120159.334011Z/receipt.json', 'check_recognitional_binding.py'),
        ('inferential-substitution-checks/20261008T181823.552825Z/receipt.json', 'check_inferential_substitution.py')]
    retained, declarations = [], {}
    for relative, checker in packages:
        path = LEAN / relative
        receipt = json.loads(path.read_text())
        assert receipt['passed']
        assert sha((LEAN / checker).read_bytes()) == receipt['checker_sha256']
        for item in receipt.get('modules', [receipt]):
            fingerprint = item.get('sha256', item.get('source_sha256'))
            source = ROOT / item['source']
            assert sha(source.read_bytes()) == sha((ROOT / item['snapshot']).read_bytes()) == fingerprint
            assert item['passed'] and item['exit_code'] == 0 and item['source_unchanged_during_check']
            log = (ROOT / item['log']).read_text()
            assert sha(log.encode()) == item['log_sha256']
            reported = {n: [] for n in item['empty_axiom_audits']}
            reported.update(item.get('standard_axiom_audits', {}))
            assert audits(log) == reported
            printed = re.findall(r'^#print axioms (\S+)$', source.read_text(), re.M)
            namespace = re.search(r'^namespace (\S+)$', source.read_text(), re.M).group(1)
            qualified = {n if n in reported else namespace+'.'+n for n in printed}
            assert qualified == set(reported), (source, qualified, set(reported))
            for name, deps in reported.items():
                assert name not in declarations or declarations[name] == deps
                declarations[name] = deps
            assert 'warning:' not in log and 'error:' not in log
        retained.append(dict(path=str(path.relative_to(ROOT)),sha256=sha(path.read_bytes())))
    assert len(declarations) == 41
    assert sum(not ds for ds in declarations.values()) == 35
    assert all(set(ds) <= {'Quot.sound'} for ds in declarations.values())
    manifest = json.loads((BEFORE / 'manifest.json').read_text())
    for item in manifest:
        assert sha((ROOT / item['snapshot']).read_bytes()) == item['sha256']
    for path in (SOURCE, STUDY):
        assert path.read_bytes().startswith((BEFORE / path.name).read_bytes())
    assert re.findall(r'^## (\d+)\.', THEORY.read_text(), re.M) == [str(i) for i in range(1,17)]
    old_record = json.loads((BEFORE / (IDS[1]+'.json')).read_text())
    current = json.loads((RECORDS / (IDS[1]+'.json')).read_text())
    for key in old_record:
        if key not in ('reviewed_at_utc','references','related','next_delta','history'):
            assert current[key] == old_record[key], key
    for ref in old_record['references']:
        if ref['role'] in ('proof','receipt'):
            assert ref in current['references']
    edits = json.loads((HERE / 'BINDING-CONSTITUTION-INDEX-EDITS.json').read_text())
    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id']=='F01')
    assert entry == edits['entry_after']
    row = next(x for x in chain.render(data).splitlines() if x.startswith('| F01 |'))
    assert row == edits['new_rendered_row'] == next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith('| F01 |'))
    for path,fingerprint in edits['authored_fingerprints'].items():
        assert sha((ROOT/path).read_bytes()) == fingerprint == data['reviewed_sources'][path]
    documents = [THEORY, STUDY, SOURCE]
    snippets = [(p,p.read_text()) for p in documents]
    for f in edits['shared_fragments']:
        assert (ROOT/f['path']).read_text().count(f['text']) == 1
        snippets.append((ROOT/f['path'],f['text']))
    links = []
    for doc,text in snippets:
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
            if target.startswith(('http://','https://')): continue
            name,_,anchor = unquote(target).partition('#')
            dest = (doc.parent/name).resolve() if name else doc
            assert dest.is_relative_to(ROOT) and (dest.exists() or dest==OUTPUT), (doc,target)
            if anchor and dest.suffix=='.md': assert anchor in chain.heading_ids(dest), (doc,target)
            links.append(dict(document=str(doc.relative_to(ROOT)),target=target))
    p = subprocess.run([sys.executable,'-B',str(ROOT/'tools/research/research.py'),'check','--ids',*IDS],cwd=ROOT,text=True,capture_output=True)
    focused = json.loads(p.stdout)
    own_errors = [e for e in focused.get('errors',[]) if any(e.startswith(i+':') for i in IDS)]
    own_drift = [e for e in focused.get('source_drift',[]) if e['id'] in IDS]
    assert not own_errors and not own_drift, (own_errors,own_drift)
    # Per-record source versions are checked explicitly even if unrelated global
    # metadata errors made the standard command return before scoped validation.
    for ident in IDS:
        rec = json.loads((RECORDS/(ident+'.json')).read_text())
        for ref in rec['references']:
            assert sha((ROOT/ref['path']).read_bytes()) == ref['sha256']
    report = dict(passed_owned_documentary_scope=True,new_theorems=0,lean_recompiled=False,
        reused_receipts=retained,unique_retained_declaration_audits=41,empty_reports=35,quot_sound_only=6,
        historical_editions=manifest,documents={str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in documents},
        local_links=links,focused_registry_command_exit=p.returncode,focused_registry_command=focused,
        pending_shared_reviews=chain.changes(data),global_chain_link_errors=chain.validate(data),
        complete_presuppositionless_grounding=False,whole_table_certified=False,independent_agent_review=False)
    OUTPUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed_owned_documentary_scope=True,new_theorems=0,reused_receipts=3,
        local_links=len(links),registry_command_exit=p.returncode,global_metadata_errors=len(focused.get('errors',[])))))

if __name__ == '__main__': main()
