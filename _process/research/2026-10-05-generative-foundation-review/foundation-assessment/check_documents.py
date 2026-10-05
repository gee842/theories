"""Check final assessment documents and refresh package provenance records."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
PACKAGE=HERE.parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def save(p,x):
    p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')


original='91efaed68a9746e8213437a810a6bb9b0864a572467a9956010fe2711cb92460'
assert sha(PACKAGE/'FOUNDATION-ALTERNATIVE-ORIGINAL.md')==original
for name in ('DOCUMENT-CHECKS.json','MANIFEST.json'):
    if not (HERE/name).exists():save(HERE/name,{})
docs,links,errors=[],[],[]
for p in sorted(HERE.rglob('*.md')):
    text=p.read_text()
    relative=str(p.relative_to(HERE))
    tags=re.findall(r'\\tag\{([^}]+)\}',text)
    display=[text.count('\\['),text.count('\\]')]
    inline=[text.count('\\('),text.count('\\)')]
    placeholders=re.findall(r'\b(?:TODO|TBD|FIXME)\b',text)
    if display[0]!=display[1] or inline[0]!=inline[1] or len(tags)!=len(set(tags)) or placeholders:
        errors.append({'file':relative,'error':'math delimiter, duplicate tag, or placeholder'})
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
        if re.match(r'[a-zA-Z]+:',target) or target.startswith('#'):continue
        local=unquote(target.split('#',1)[0]).strip('<>')
        local=re.sub(r':\d+(?::\d+)?$','',local)
        exists=(p.parent/local).resolve().exists()
        links.append({'file':relative,'target':target,'exists':exists})
        if not exists:errors.append({'file':relative,'missing':target})
    docs.append({'file':relative,'sha256':sha(p),'words':len(text.split()),
        'equation_tags':tags,'display_delimiters':display,'inline_delimiters':inline,
        'placeholders':placeholders})
checks=json.loads((HERE/'INDEPENDENT-CHECKS.json').read_text())
benchmark=json.loads((HERE/'benchmark/VERIFICATION.json').read_text())
assert checks['status']=='passed'
report={'date':'2026-10-05','primary':'ASSESSMENT.md','documents':docs,'local_links':links,
    'errors':errors,'original_preserved_sha256':original,'independent_check_groups':checks['check_groups'],
    'independent_checks':'INDEPENDENT-CHECKS.json','benchmark_verification':'benchmark/VERIFICATION.json',
    'review_scope':'Three internal agent assessments with cross-review and root verification; reported corrections resolved. No independent human peer review.',
    'empirical_scope':'Exploratory reanalysis of reused measured data. No new intervention trial; no priority or universality certification.',
    'full_document_render_audit':False}
save(HERE/'DOCUMENT-CHECKS.json',report)
assert not errors,errors
inputs=[PACKAGE/'root-foundation/ROOT-FOUNDATION.md',PACKAGE/'root-foundation/TURNOVER-AND-CLOSURE.md',
    PACKAGE/'root-foundation/INFORMATION-AND-RENEWAL.md',PACKAGE/'final-synthesis/INTEGRATED-THEORY.md',
    PACKAGE/'FOUNDATION-ALTERNATIVE-ORIGINAL.md',
    Path(json.loads((HERE/'benchmark/analysis.json').read_text())['source_path'])]
manifest={'date':'2026-10-05','title':'Physical scope originality and measured performance assessment',
    'primary':'ASSESSMENT.md','hash_algorithm':'SHA-256','self_hash_excluded':True,
    'files':[{'path':str(p.relative_to(HERE)),'sha256':sha(p),'bytes':p.stat().st_size}
        for p in sorted(HERE.rglob('*')) if p.is_file() and p!=HERE/'MANIFEST.json' and '__pycache__' not in p.parts],
    'inputs':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in inputs]}
save(HERE/'MANIFEST.json',manifest)
parent_checks=json.loads((PACKAGE/'DOCUMENT-CHECKS.json').read_text())
parent_checks['foundation_assessment']={'file':'foundation-assessment/ASSESSMENT.md',
    'checks':'foundation-assessment/DOCUMENT-CHECKS.json','independent_check_groups':checks['check_groups'],
    'empirical_comparison':'Exploratory reused-data comparison: no primary gain',
    'new_causal_intervention_study':False,'review_scope':report['review_scope']}
save(PACKAGE/'DOCUMENT-CHECKS.json',parent_checks)
parent_manifest=json.loads((PACKAGE/'MANIFEST.json').read_text())
parent_manifest['foundation_assessment']='foundation-assessment/ASSESSMENT.md'
parent_manifest['assessment_status']='Scope and originality audit; stochastic extension; measured primary predictive gain absent.'
parent_manifest['package_files']=[{'path':str(p.relative_to(PACKAGE)),'sha256':sha(p),'bytes':p.stat().st_size}
    for p in sorted(PACKAGE.rglob('*')) if p.is_file() and p!=PACKAGE/'MANIFEST.json' and '__pycache__' not in p.parts]
save(PACKAGE/'MANIFEST.json',parent_manifest)
print(json.dumps({'documents':len(docs),'local_links':len(links),'errors':len(errors),
                  'independent_check_groups':checks['check_groups'],'original_preserved':True}))
