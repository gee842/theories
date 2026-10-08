"""Integration/preservation check; does not rerun the scientific experiments."""
from pathlib import Path
import gzip
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').exists())
ACTION=REPO/'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action'
CANONICAL=REPO/'theories/becoming/chapters/RECIPIENT-REASON-ACTION.md'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
verified={}
def match(p,h):
    assert p.exists(),p
    assert digest(p)==h,p
    verified[str(p.relative_to(REPO))]=h

formal=read(ACTION/'formal/verification.json')
assert formal['status']=='passed' and formal['new_audited_declarations']==79
assert len(formal['modules'])==17 and formal['source_unchanged_during_check']
match(ACTION/'formal/check.py',formal['checker_sha256'])
match(ACTION/'formal/lean-toolchain',formal['toolchain_sha256'])
for m in formal['modules']:
    assert m['exit_code']==0 and m['clean_dependency_audit']
    assert set(m['axioms'])<= {'propext','Quot.sound','Classical.choice'}
    match(REPO/m['source'],m['source_sha256'])
    match(ACTION/'formal'/m['output'],m['output_sha256'])
producer=read(ACTION/'check.json')
independent=read(ACTION/'model-verification.json')
assert producer['status']==independent['status']=='passed'
assert producer['cases']==37 and producer['histories']==1406
assert independent['totals']['comparison_arms']==111
assert independent['totals']['prefix_states']==30938
assert not independent['imports_model_transition_functions']
for receipt in (producer,independent):
    for k in ('source_sha256','inherited_source_sha256'):
        for path,h in receipt.get(k,{}).items():
            p=REPO/path
            if not p.exists():p=ACTION/path
            match(p,h)
for path,h in producer['data_sha256'].items():match(ACTION/path,h)
match(ACTION/'check.py',producer['checker_sha256'])
data=read(ACTION/'result-files.json')
match(ACTION/'results.json.gz',data['compressed_sha256'])
raw=gzip.decompress((ACTION/'results.json.gz').read_bytes())
assert hashlib.sha256(raw).hexdigest()==producer['uncompressed_results_sha256']
result=json.loads(raw)
for mode,expected in [('primary','15/8'),('conventional_command','15/8'),
                      ('learned_register','5/2'),('unaudited_voluntary','5/2')]:
    metrics=result['cases'][mode]['producers']['variable']['metrics']
    assert metrics['delivered']==expected
    assert metrics['strict_action_capture']=='9/64'

preview=read(HERE/'reason-action-evidence/preview-check.json')
for path,h in preview['file_sha256'].items():match(HERE/'reason-action-evidence'/path,h)
assert preview['paired_focal_ids']==24 and not preview['original_csv_bytes_verified']

documents=[CANONICAL,ACTION/'README.md',ACTION/'formal/README.md',
           HERE/'REASON-ACTION-MATH.md',HERE/'REASON-ACTION-REVIEW.md',
           HERE/'REASON-ACTION-EMPIRICAL-CANDIDATES.md',HERE/'reason-action-evidence/README.md',
           HERE/'FOUNDATION-COMPLETION-AUDIT.md',HERE/'CONCERN-WISDOM-INPUTS.md']
links=0
for p in documents:
    for url in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if url.startswith(('http:','https:','#')):continue
        target=(p.parent/url.split('#')[0]).resolve()
        assert target.exists(),(p,url)
        links+=1
    verified[str(p.relative_to(REPO))]=digest(p)
for p in (ACTION/'formal/verification.json',ACTION/'check.json',ACTION/'model-verification.json',
          ACTION/'result-files.json',ACTION/'first-run-receipt.json',Path(__file__)):
    verified[str(p.relative_to(REPO))]=digest(p)
report=dict(status='passed',scope='Integration of already checked receipts, saved outcomes and local links; no new scientific run.',
            new_lean_audits=79,formal_modules=17,comparison_arms=111,histories=1406,
            runtime_states=30938,relative_links=links,verified_sha256=verified,
            empirical_scope='Derived public-preview arithmetic; original CSV unverified and n23/n24 discrepancy unresolved.')
(HERE/'REASON-ACTION-INTEGRATION.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='verified_sha256'},indent=2))
