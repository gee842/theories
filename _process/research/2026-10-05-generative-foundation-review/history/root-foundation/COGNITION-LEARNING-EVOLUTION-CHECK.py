#!/usr/bin/env python3
"""Scoped documentary/receipt audit; does not rerun or certify empirical science."""
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
THEORY = ROOT / 'theories/becoming/chapters/COGNITION-LEARNING-AND-EVOLUTION.md'
STUDY = HERE / 'COGNITION-LEARNING-EVOLUTION-INTEGRATION.md'
DIRECTIVE = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-cognition-learning-evolution-goal.md'
FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    inspected_links = []
    def check_links(p, content):
        for ref in re.findall(r'\]\(([^)]+)\)', content):
            if ref.startswith(('https://','http://')):
                continue
            name,_,fragment = ref.partition('#')
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and target.exists(), (p,ref)
            if fragment and target.suffix == '.md':
                assert unquote(fragment) in chain.heading_ids(target), (p,ref)
            inspected_links.append((str(p.relative_to(ROOT)),ref))
    for p in [THEORY, STUDY, DIRECTIVE]:
        check_links(p, p.read_text())
    receipt_path = FORMAL / 'compositional-acquisition-verification.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['status'] == 'passed'
    frozen = FORMAL / receipt['retained_run']
    for name,sha in receipt['source_sha256'].items():
        assert digest(FORMAL / (name + '.lean')) == sha
        assert digest(frozen / (name + '.lean')) == sha
    for name,sha in receipt['artifact_sha256'].items():
        assert digest(frozen / name) == sha, name
    new = receipt['modules'][-1]
    inherited = receipt['modules'][0]
    assert new['module'] == 'CompositionalAcquisition'
    assert new['theorems'] == 25 and len(new['declarations']) == 52
    assert len(inherited['declarations']) == 34
    assert len(new['axiom_dependencies']) == 52
    assert all(set(a) <= {'propext','Quot.sound','Classical.choice'} for a in new['axiom_dependencies'].values())
    edits = json.loads((HERE / 'COGNITION-LEARNING-EVOLUTION-INDEX-EDITS.json').read_text())
    data = chain.read_data()
    found = [e for s in data['sections'] for e in s['entries'] if e['id'] == edits['added_entry']['id']]
    assert found == [edits['added_entry']]
    canonical = next(l for l in chain.render(data).splitlines() if l.startswith('| '+found[0]['id']+' |'))
    rendered = chain.OUTPUT.read_text().splitlines()
    assert canonical in rendered
    for name,sha in edits['reviewed_owned_sources'].items():
        assert digest(ROOT / name) == sha and data['reviewed_sources'][name] == sha, name
    for name,text in edits['navigation_insertions'].items():
        assert text in (ROOT / name).read_text(), name
        check_links(ROOT / name, text)
    for name in edits['discovery_added']:
        assert name in data['known_discovery_paths']
    report = {'status':'passed','scope':'Owned cognition/composition documents, links, current/frozen proof bindings and canonical bilingual row only.',
        'local_links_checked':len(inspected_links),'new_theorems':25,'new_declaration_audits':52,
        'inherited_declaration_audits':34,'owned_entry':found[0]['id'],
        'proof_receipt_sha256':digest(receipt_path),
        'files_sha256':{str(p.relative_to(ROOT)):digest(p) for p in [THEORY,STUDY,DIRECTIVE]},
        'other_source_reviews':chain.changes(data),
        'full_goal_complete':False,'independent_review':False}
    (HERE / 'COGNITION-LEARNING-EVOLUTION-CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['other_source_reviews','files_sha256']}))


if __name__ == '__main__':
    main()
