"""Check preservation, documentary links, evidence bindings and the owned index row."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAN = ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXP = ROOT/'experiments/integrated-correction/general-framework/generative-basis/semantic-evidence'
SOURCE = ROOT/'sources/knowledge-semantics'
OUTPUT = HERE/'SEMANTIC-SUFFICIENCY-CHECKS.json'
DOCUMENTS = [HERE/'SEMANTIC-SUFFICIENCY-INTEGRATION.md',HERE/'SEMANTIC-SUFFICIENCY-SOURCES.md',CAN/'KNOWLEDGE.md',CAN/'PHILOSOPHICAL-ACCOUNT.md',SOURCE/'README.md',EXP/'README.md',ROOT/'sources/15-codex-theory-conversations/2026-10-08-knowledge-content-continuation.md']
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
spec = importlib.util.spec_from_file_location('chain',HERE/'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)
errors=[]
count=0
for document in DOCUMENTS:
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',document.read_text()):
        if target.startswith(('https:','http:','mailto:')):continue
        name,_,fragment=target.partition('#')
        p=(document.parent/unquote(name)).resolve() if name else document
        count+=1
        if not p.is_file():errors.append(f'{document.name}: missing {target}')
        elif fragment and p.suffix=='.md' and unquote(fragment) not in chain.heading_ids(p):errors.append(f'{document.name}: missing heading {target}')
manifest=json.loads((SOURCE/'manifest.json').read_text())
source_bindings={x['file']:sha(SOURCE/x['file'])==x['sha256'] for x in manifest['files']}
if not all(source_bindings.values()):errors.append('Original source bytes changed')
evidence=json.loads((EXP/'verification.json').read_text())
analysis_bindings={p:sha(ROOT/p)==h for p,h in evidence['file_sha256'].items()}
if not all(analysis_bindings.values()):errors.append('Current analysis no longer matches executed receipt')
if evidence['status']!='passed_four_selected_statistic_reproductions':errors.append('Numerical checking failed')
if len(evidence['statistics'])!=4 or not all(x['matches_reported_rounding'] for x in evidence['statistics']):errors.append('Missing statistic reproduction')

# Preserve the earlier formal scope without rerunning unchanged mathematics.
proofs=[]
PROOFS=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
for stem,source,checker in [('knowledge-correspondence','KnowledgeCorrespondence.lean','check_knowledge_correspondence.py'),('inquiry-adequacy','InquiryAdequacy.lean','check_inquiry_adequacy.py')]:
    receipt=PROOFS/f'{stem}-verification.json'
    record=json.loads(receipt.read_text()); frozen=ROOT/record['snapshot']
    binding={'receipt_passed':record['status']=='passed','current_source':sha(PROOFS/source)==record['source_sha256'],'current_checker':sha(PROOFS/checker)==record['checker_sha256'],'frozen_source':sha(frozen/source)==record['source_sha256'],'frozen_checker':sha(frozen/checker)==record['checker_sha256'],'frozen_receipt':sha(frozen/'verification.json')==sha(receipt)}
    binding.update({name:sha(frozen/name)==h for name,h in record['log_sha256'].items()})
    if not all(binding.values()):errors.append('Inherited proof binding failed: '+stem)
    proofs.append({'receipt':str(receipt.relative_to(ROOT)),'sha256':sha(receipt),'bindings':binding,'theorems':record['theorems'],'declarations':record['explicit_declaration_audits'],'scope':record['scope']})

data=chain.read_data();entry=next(e for s in data['sections'] for e in s['entries'] if e['id']=='M21')
versions={}
for link in entry['links']:
    p,_=chain.local_target(link['path']);name=str(p.relative_to(ROOT))
    versions[name]=data['reviewed_sources'].get(name)==sha(p)
row=next(l for l in chain.render(data).splitlines() if l.startswith('| M21 |'))
actual=next(l for l in chain.OUTPUT.read_text().splitlines() if l.startswith('| M21 |'))
if row!=actual or not all(versions.values()):errors.append('Owned M21 row or source versions mismatch')
quoted='keep pushing frontier, till you see you reach an end'
if '\n> '+quoted+'\n' not in DOCUMENTS[-1].read_text():errors.append('Active-goal quotation missing')
changes=chain.changes(data)
validation=chain.validate(data)
result={'status':'passed_scoped_documentary_source_and_execution_bindings' if not errors else 'failed','checked_at_utc':datetime.now(timezone.utc).isoformat(),'errors':errors,'local_links_checked':count,'document_sha256':{str(p.relative_to(ROOT)):sha(p) for p in DOCUMENTS},'checker_sha256':sha(Path(__file__)),'original_source_bindings':source_bindings,'analysis_execution_bindings':analysis_bindings,'numerical_receipt':str((EXP/'verification.json').relative_to(ROOT)),'numerical_receipt_sha256':sha(EXP/'verification.json'),'selected_statistic_reproductions':4,'new_mathematical_theorems':0,'new_experiments':0,'new_lean_compiler_run':False,'independent_agent_acceptance':False,'inherited_proof_bindings':proofs,'chain':{'owned_entry':'M21','paired_row_matches':row==actual,'source_versions':versions,'remaining_changes':changes,'validation_errors':validation,'full_table_current':not changes['modified_sources'] and not changes['missing_sources'] and not validation and chain.OUTPUT.read_text()==chain.render(data)},'scope':'Checks establish local preservation, reported numerical reproduction bindings and navigation. Philosophical sufficiency, consciousness and whole-theory necessity remain open. The active frontier goal is not marked complete.'}
OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','local_links_checked','selected_statistic_reproductions','errors']},indent=2))
if errors:raise SystemExit(1)
