"""Package prospective records, exact raw response texts, mechanical results and reproduction sources."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json,hashlib

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent.parent/'outputs'/'active-inquiry-data.json'
def readj(name): return json.loads((ROOT/name).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
freeze=readj('run-freeze.json')
for name,expected in freeze['file_sha256'].items():
    assert sha(ROOT/name)==expected,name
treatment_freeze=readj('treatment-freeze.json')
for record in treatment_freeze['treatments'].values():
    assert sha(ROOT/record['file'])==record['sha256']
manifest=readj('run-manifest.json')
runs=[]
for number,batch in enumerate(manifest['batches'],1):
    directory=ROOT/'runs'/batch['batch']
    state=json.loads((directory/'state.json').read_text())
    assert state['round']==3 and all(ep['closed'] for ep in state['episodes'].values())
    rounds=[{'round':n,'raw_response_text':(directory/f'response-{n}.txt').read_text(),
             'mechanical_feedback':json.loads((directory/f'feedback-{n}.json').read_text())} for n in range(state['round'])]
    runs.append({**batch,'participant':f'/root/active_p{number:02d}',
                 'prompt_text':(directory/'prompt.txt').read_text(),'rounds':rounds,'final_state':state})
audit_names=['design-audit.md','audit.txt','engine-audit.md','scorer-audit.md','results-audit.md']
files=list(freeze['file_sha256'])+['scorer-audit.md','results-audit.md','conceptual-implications.md']
superseded=ROOT/'design-history'/'paired-draw-pre-run-draft'
bundle={
 'schema_version':'root-of-wisdom-active-inquiry-evidence-v1',
 'packaged_at':datetime.now(ZoneInfo('Asia/Bangkok')).isoformat(),
 'status':'All six planned contexts complete; no comparative advantage observed; no extra runs added.',
 'scope':'Synthetic active query selection under fully specified finite priors, losses and constraints; not unbounded discovery or ethical wisdom.',
 'protocol':readj('protocol.json'),'pre_run_amendments':readj('pre-run-amendments.json'),
 'treatment_freeze':treatment_freeze,'run_freeze':freeze,
 'environment':readj('environment.json'),'public_cases':readj('public-cases.json'),
 'independent_verification':readj('verification.json'),
 'treatments':{c:(ROOT/f'treatment-{c}.txt').read_text() for c in manifest['conditions']},
 'run_manifest':manifest,'runs':runs,'scores':readj('scores.json'),
 'audits':{name:(ROOT/name).read_text() for name in audit_names},
 'frozen_and_supporting_file_contents':{name:{'sha256':sha(ROOT/name),'text':(ROOT/name).read_text()} for name in files},
 'superseded_pre_run_draft':{str(p.relative_to(superseded)):{'sha256':sha(p),'text':p.read_text()} for p in sorted(superseded.iterdir()) if p.is_file()},
 'source_record':{'title':'Bellman, On the Theory of Dynamic Programming (1952)',
  'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/',
  'examined':'Page images 716 and 717 visually inspected; not a full reading of all four pages.',
  'images':{p.name:sha(p) for p in sorted((ROOT/'sources').glob('*.png'))}},
 'record_limitations':['Raw final response texts were copied from participant messages by the coordinator; full participant tool traces are not included.',
   'Mechanical feedback is preserved as JSON; delivery used the same JSON content with compact whitespace.',
   'No model override, sampling seed, actual hidden computation measurement, or independent external preregistration.',
   'Six context-level batches; episodes and visited choices are not independent participant replications.',
   'Auditors were separate agents in this research session, not independent scientific replication.'],
 'reproduction':'Extract frozen_and_supporting_file_contents into a directory retaining their relative names, restore the listed raw response-N.txt files under runs/<batch>, and use engine.initialize with manifest entries to create initial state.json. Apply engine.apply_saved_round for rounds 0,1,2, then score.py. Existing final states are also preserved for comparison.'
}
OUT.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'output':str(OUT),'bytes':OUT.stat().st_size,'runs':len(runs),'rounds':sum(len(r['rounds']) for r in runs),'frozen_hashes_verified':len(freeze['file_sha256'])}))
