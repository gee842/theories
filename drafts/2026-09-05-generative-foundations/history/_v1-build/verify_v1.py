from pathlib import Path
from fractions import Fraction
import hashlib
import json
import re
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent.parent
reports = []
errors = []
def check(name, ok, detail=''):
    reports.append(f'{"PASS" if ok else "FAIL"} | {name}' + (f' | {detail}' if detail else ''))
    if not ok: errors.append(name)

stats={}
for name in ['WHITEPAPER-v1.0.md','宣言-v1.0.md']:
    p=BASE/name;s=p.read_text()
    stats[name]={'characters':len(s),'han_characters':len(re.findall(r'[\u3400-\u9fff]',s)),
                 'lines':len(s.splitlines()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    check(name+' math delimiters',s.count('\\[')==s.count('\\]') and s.count('\\(')==s.count('\\)'))
    check(name+' fenced blocks',len(re.findall(r'^```',s,re.M))%2==0)
    check(name+' no control characters',not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',s))
    check(name+' no editorial placeholders',not re.search(r'TODO|FIXME|PLACEHOLDER|THEOREM_TABLE|本轮|上一版|作者补充|你提出',s))
    missing=[]
    anchors=set(re.findall(r'<a id="([^"]+)">',s))
    for dest in re.findall(r'\]\(([^)]+)\)',s):
        dest=dest.strip('<>')
        if dest.startswith(('https://','http://')):continue
        if dest.startswith('#'):
            if dest[1:] not in anchors:missing.append(dest)
            continue
        target=Path(dest) if dest.startswith('/') else BASE/dest.split('#')[0]
        if not target.exists():missing.append(dest)
    check(name+' local links and anchors',not missing,str(missing))
    # All current tables use ordinary pipes; no unescaped pipes in math cells.
    bad_tables=[];width=None
    for n,line in enumerate(s.splitlines(),1):
        if line.startswith('|'):
            cells=len(re.split(r'(?<!\\)\|',line))-2
            if width is None:width=cells
            elif cells!=width:bad_tables.append(n)
        else:width=None
    check(name+' table widths',not bad_tables,str(bad_tables))

s=(BASE/'WHITEPAPER-v1.0.md').read_text()
heads=re.findall(r'^### (\d+)\.(\d+) ',s,re.M)
by_chapter={}
for a,b in heads:by_chapter.setdefault(int(a),[]).append(int(b))
check('Twelve consecutive chapters',sorted(by_chapter)==list(range(1,13)))
check('Consecutive subsection numbering',all(nums==list(range(1,len(nums)+1)) for nums in by_chapter.values()))
sections={f'{a}.{b}' for a,b in heads}
broken_refs=sorted(set(re.findall(r'§(\d+\.\d+)',s))-sections)
check('Section reference destinations',not broken_refs,str(broken_refs))
check('Three appendices',all(f'id="appendix-{a}"' in s for a in 'abc'))
coverage=json.loads((BASE/'_v1-build/coverage-v1.json').read_text())
check('29 source principle mappings',len(coverage['principles'])==29)
check('28 named theorem index entries',len(coverage['theorems'])==28)

snapshot=json.loads((BASE/'v1.0-原版校验.json').read_text());changed=[]
for it in snapshot['files']:
    f=(BASE.parent if it.get('base')=='drafts' else BASE)/it['path']
    if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=it['sha256']:changed.append(str(f))
check('All recorded earlier files unchanged',not changed,f'{len(snapshot["files"])} files; changed={changed}')
for module,log,expected in [('GenerativeCore','verification.txt',20),('OpenFuture','OpenFuture-verification.txt',3),('ExistenceConditions','ExistenceConditions-verification.txt',5)]:
    f=BASE/'formal'/f'{module}.lean';source=f.read_text();logs=(BASE/'formal'/log).read_text()
    check(module+' hash matches existing successful verification',hashlib.sha256(f.read_bytes()).hexdigest() in logs)
    check(module+' expected theorem count',len(re.findall(r'^theorem ',source,re.M))==expected)
    check(module+' no sorry or user axiom declarations',not re.search(r'\bsorry\b|^axiom ',re.sub(r'/\-.*?\-/','',source,flags=re.S),re.M))

# Verify the illustrative H1 table with exact arithmetic; no simulated reality.
expected={0:(10,1,Fraction(1),Fraction(1,2)),2:(12,3,Fraction(3,4),Fraction(7,8)),
          4:(14,5,Fraction(5,16),Fraction(31,32)),5:(15,6,Fraction(3,16),Fraction(63,64))}
actual={t:(10+t,1+t,Fraction(1+t,2**t),1-Fraction(1,2**(t+1))) for t in expected}
check('H1 exact example values',actual==expected)

required=['相同任务含义、期限 H、剩余预算 B','每一次实际转移都属于模型 T',
          '违规行动的收益为 λ+1','没有独立识别成绩对过滤与确信的因果作用',
          '在所评价的当前信息下严格为正','不能把“已经考虑”当作“已经实现”']
check('Reviewed mathematical qualifications retained',all(x in s for x in required))

out={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'stats':stats,'checks':reports,
     'errors':errors,'lean_rerun':False,'notes':'Existing Lean logs were matched by source hash; no new machine proof or empirical study is claimed.'}
(BASE/'v1.0-检查记录.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(BASE/'v1.0-检查记录.txt').write_text('Unified version v1.0 verification\n'+out['checked_at_utc']+'\n\n'+'\n'.join(reports)+'\n\n'+json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(reports),'errors':errors,'stats':stats},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
