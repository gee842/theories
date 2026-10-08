"""Verify owned documentary links, actual proof bindings and the paired M26 row."""
from datetime import datetime, timezone
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
sys.path.insert(0,str(ROOT))
from tools.research import generative_chain as chain

FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
RECORDS = ROOT / 'theories/becoming/results/records'
IDS = ['acquired-binding-compositional-use','enacted-scene-binding','encounter-selection-and-revision',
       'naming-attention-coverage','encounter-control-and-retention','retrospective-source-binding']
OUTPUT = HERE / 'RETROSPECTIVE-BINDING-CHECKS.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec=importlib.util.spec_from_file_location('proof_check',FORMAL/'check_retrospective_binding.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    receipt_path=FORMAL/'retrospective-binding-verification.json'
    receipt=json.loads(receipt_path.read_text());assert receipt['status']=='passed'
    frozen=FORMAL/receipt['retained_run']
    assert json.loads((frozen/'verification.json').read_text())==receipt
    for name,path in module.SOURCES.items():
        assert digest(path)==receipt['source_sha256'][name]==digest(frozen/(name+'.lean'))
    assert digest(FORMAL/'check_retrospective_binding.py')==receipt['checker_sha256']['check_retrospective_binding.py']
    for filename,h in receipt['artifact_sha256'].items():assert digest(frozen/filename)==h,filename
    own=receipt['modules'][-1]
    assert own['module']=='RetrospectiveBinding' and own['kernel_checked']
    assert own['declarations']==module.inventory('RetrospectiveBinding',(FORMAL/'RetrospectiveBinding.lean').read_bytes())
    assert own['theorems']==20 and len(own['declarations'])==36
    assert sum(len(x['declarations']) for x in receipt['modules'][:-1])==513
    assert all(set(deps)<=module.audit.STANDARD_AXIOMS for m in receipt['modules'] for deps in m['axiom_dependencies'].values())
    for name in IDS:
        record=json.loads((RECORDS/(name+'.json')).read_text())
        for ref in record['references']:assert digest(ROOT/ref['path'])==ref['sha256'],ref['path']
    files=[HERE/'ACQUIRED-SEGMENTATION-INTEGRATION.md',FORMAL/'README.md',
           ROOT/'theories/becoming/chapters/COGNITION-LEARNING-AND-EVOLUTION.md',
           *[RECORDS/(name+'.md') for name in IDS]]
    checked=0
    for path in files:
        for ref in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            if ref.startswith(('https://','http://')):continue
            p,_,fragment=ref.partition('#');target=(path.parent/unquote(p)).resolve() if p else path
            assert target.is_relative_to(ROOT) and (target.exists() or target==OUTPUT),(path,ref)
            if fragment and target.suffix=='.md':assert unquote(fragment) in chain.heading_ids(target),(path,ref)
            checked+=1
    data=chain.read_data();edit=json.loads((HERE/'RETROSPECTIVE-BINDING-INDEX-EDITS.json').read_text())
    entry=next(e for section in data['sections'] for e in section['entries'] if e['id']=='M26')
    assert entry==edit['updated_entry']
    assert all(link in entry['links'] for link in edit['before_entry']['links'])
    for p,h in edit['reviewed_owned_sources'].items():assert digest(ROOT/p)==h==data['reviewed_sources'][p],p
    row=next(line for line in chain.render(data).splitlines() if line.startswith('| M26 |'))
    assert row in chain.OUTPUT.read_text().splitlines()
    report=dict(status='passed',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        scope='Owned links, six source-bound records, current/frozen Lean receipt and M26. Canonical navigation checked separately. No empirical identification, independent-agent acceptance or full-goal completion.',
        new_theorems=20,new_declaration_audits=36,inherited_theorems=284,inherited_declaration_audits=513,
        proof_receipt_sha256=digest(receipt_path),retained_run=receipt['retained_run'],
        result_ids=IDS,local_links_checked=checked,owned_entry='M26',
        file_sha256={str(p.relative_to(ROOT)):digest(p) for p in files},full_goal_complete=False)
    OUTPUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='file_sha256'},indent=2))


if __name__=='__main__':main()
