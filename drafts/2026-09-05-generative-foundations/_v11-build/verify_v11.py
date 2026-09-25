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
for name in ['WHITEPAPER-v1.1.md','宣言-v1.1.md']:
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

s=(BASE/'WHITEPAPER-v1.1.md').read_text()
heads=re.findall(r'^### (\d+)\.(\d+) ',s,re.M)
by_chapter={}
for a,b in heads:by_chapter.setdefault(int(a),[]).append(int(b))
check('Twelve consecutive chapters',sorted(by_chapter)==list(range(1,13)))
check('Consecutive subsection numbering',all(nums==list(range(1,len(nums)+1)) for nums in by_chapter.values()))
sections={f'{a}.{b}' for a,b in heads}
broken_refs=sorted(set(re.findall(r'§(\d+\.\d+)',s))-sections)
check('Section reference destinations',not broken_refs,str(broken_refs))
check('Three appendices',all(f'id="appendix-{a}"' in s for a in 'abc'))
coverage=json.loads((BASE/'_v11-build/coverage-v11.json').read_text())
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

required=['每一次实际转移都属于模型 T','违规行动的收益为 λ+1',
          '没有独立识别成绩对过滤与确信的因果作用','在所评价的当前信息下严格为正',
          '合取要求保护实际同时成立','若 x∈S 但 x∉V','固定实对称矩阵 C']
check('Reviewed mathematical qualifications retained',all(x in s for x in required))

baseline=json.loads((BASE/'v1.1-修订前校验.json').read_text())
changed=[n for n,h in baseline.items() if not (BASE/n).exists() or hashlib.sha256((BASE/n).read_bytes()).hexdigest()!=h]
check('v1.0 and all 68 pre-revision local files preserved',not changed,str(changed))
check('Under 50000 Han characters including appendices',stats['WHITEPAPER-v1.1.md']['han_characters']<50000)
check('No Downloads links in whitepaper', '/Users/ren/Downloads' not in s)
concepts=['七尺','真实','再生','主体','关系','多样','可纠','代际','绝生之限','成生之限','一身','一家','一组织','一国','天下','邪理','良知','修身','真善美','大道','冻结','烧尽','有了未来','不可否定','間','文言','开境','护闭','SSBX','未、可、应、转']
check('Restored concepts and scope present',all(x in s for x in concepts))
check('Three stewardship rules present',all(x in s for x in ['不静默关闭','关闭者不能独持重开的钥匙','不使原本可能的事变为不可能']))
check('P1 P2 P4 classified as definitional corollaries',all('定义性推论 '+x in s for x in ['P1','P2','P4']) and not re.search(r'\*\*命题 P[124]',s))
check('P3 retains monotonicity proof', '命题 P3' in s and '积分与条件期望的单调性' in s)
check('Nine objections retained',len(re.findall(r'^\*\*[一二三四五六七八九]、“',s,re.M))==9)
check('Normative premise status explicit','R3 是明确的规范承诺' in s and '本文的“必然”是论证关系的必然' in s)
check('Updated formal version locator exists',(BASE/'formal/README-v1.1.md').exists() and '旧 README 与源码头注' in s)
check('Ell typo and editorial phrase fixed',r'\(ell_t\)' not in s and '新材料将' not in s)
check('Research precedent names present',all(x in s for x in ['Gewirth','Nagel','Jonas','Lande','Schluter','Boyd','Richerson','Lukes','Espeland','Sauder','Zwetsloot','Gabriel']))
body=s.split('## 附录 A')[0]
check('Previously unused references cited in body',all(x in body for x in ['Beer','Adami','Ratcliff']))

rec=json.loads((BASE/'宣言-v1.1-编辑记录.json').read_text())
archive=BASE/'../../sources/15-user-provided-2026-09-06/智能向善，天下生生.md'
original=archive.read_bytes();rebuilt=original.decode('utf-8')
for e in rec['edits']:
    if e['operation']=='insert_after_unique_anchor':
        assert rebuilt.count(e['anchor'])==1
        rebuilt=rebuilt.replace(e['anchor'],e['anchor']+e['inserted_text'],1)
    elif e['operation']=='replace_exact_block':
        assert rebuilt.count(e['old_text'])==1
        rebuilt=rebuilt.replace(e['old_text'],e['new_text'],1)
    else:
        raise ValueError('Unknown manifesto edit operation')
manifest=(BASE/'宣言-v1.1.md').read_bytes()
restored=manifest.decode('utf-8')
for e in reversed(rec['edits']):
    if e['operation']=='replace_exact_block':
        assert restored.count(e['new_text'])==1
        restored=restored.replace(e['new_text'],e['old_text'],1)
    else:
        assert restored.count(e['anchor']+e['inserted_text'])==1
        restored=restored.replace(e['anchor']+e['inserted_text'],e['anchor'],1)
ops=[e['operation'] for e in rec['edits']]
check('Manifesto two insertions and approved Datong replacement are reversible',
      ops==['insert_after_unique_anchor','insert_after_unique_anchor','replace_exact_block']
      and rebuilt.encode('utf-8')==manifest and restored.encode('utf-8')==original)
check('Manifesto published-status notes moved to README',all(x not in manifest.decode('utf-8') for x in ['拟议名称','不代表任何组织','未对外发布','AI 协助']))

archive_records=json.loads((BASE/'../../sources/15-user-provided-2026-09-06/入库记录.json').read_text())
check('Three archived source hashes',all(hashlib.sha256((archive.parent/r['file']).read_bytes()).hexdigest()==r['sha256'] for r in archive_records))
# Exact arithmetic witnesses for the new resource-capacity model, supplementary to its paper derivation.
u,d,g,k,a,delta=map(Fraction,[2,5,6,1,2,Fraction(1,2)])
c=Fraction(3,4);i=a*delta*c;L=d+k*c+i;r=L
stable=True
for n in range(20):
    stable &= r>=d+k*c+i
    rn=r+u+g*c-d-k*c-i;cn=(1-delta)*c+i/a
    stable &= rn==L and cn==Fraction(3,4)
    r,c=rn,cn
check('Regeneration exact boundary witness and prior-payment feasibility',stable)
identity=True
for r in map(Fraction,[0,2,9]):
 for c in map(Fraction,[0,1,3]):
  for i in map(Fraction,[0,2,7]):
   rn=r+u+g*c-d-k*c-i;cn=(1-delta)*c+i/a
   identity &= rn+a*cn-(r+a*c)==u-d+(g-k-a*delta)*c
check('Resource-capacity accounting identity exact samples',identity)
# Check relevant source inputs remain explicitly named in the written model.
check('Regeneration model cashflow, supply and budget premises',all(x in s for x in [r'R\ge a\bar c+L',r'L\ge d+(k+a\delta)\bar c','每期实际可得','累计支出上限',r'W_t=r_t+ac_t']))

old=(BASE/'WHITEPAPER-v1.0.md').read_text()
terms=['不能','不要求','不等于','并不','不意味着','不声称','没有证明','不证明']
style={'before':{x:old.count(x) for x in terms},'after':{x:s.count(x) for x in terms}}

out={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'stats':stats,'checks':reports,
     'errors':errors,'style_counts':style,'lean_rerun':False,'notes':'Existing Lean logs were matched by source hash; no new machine proof or empirical study is claimed.'}
(BASE/'v1.1-检查记录.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(BASE/'v1.1-检查记录.txt').write_text('Unified version v1.1 verification\n'+out['checked_at_utc']+'\n\n'+'\n'.join(reports)+'\n\n'+json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(reports),'errors':errors,'stats':stats},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
