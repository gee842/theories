"""Prepare a P89-only validation tree without changing parallel working files.

Run from the main repository. Hard links are read-only inputs; every writable
snapshot path is unlinked before writing. Only the scoped reconstruction is
eligible for the later commit. No Git staging or commit is performed here.
"""
from pathlib import Path
import subprocess, tempfile, os, json, shutil, re, hashlib
ROOT=Path.cwd(); BASE='adf335a8ffdb2b17a7eca53c7048b48605d4ed4a'
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==BASE
DEST=Path(tempfile.mkdtemp(prefix='p89-closure-'))
def head(p): return subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
def write(p,data):
 t=DEST/p;t.parent.mkdir(parents=True,exist_ok=True)
 if t.exists() or t.is_symlink():t.unlink()
 t.write_bytes(data.encode() if isinstance(data,str) else data)
def copy(p):write(p,(ROOT/p).read_bytes())
def sha(p):return hashlib.sha256((DEST/p).read_bytes()).hexdigest()
tracked=subprocess.check_output(['git','ls-files','-z'],text=True).split('\0');tracked=[p for p in tracked if p]
for p in tracked:
 s=ROOT/p;t=DEST/p;t.parent.mkdir(parents=True,exist_ok=True)
 if s.is_file():os.link(s,t)
 elif s.is_dir():t.mkdir(exist_ok=True)
 else:write(p,head(p))
print('Snapshot inputs linked:',len(tracked),flush=True)
# Restore all uncommitted tracked changes to HEAD in the private tree.
dirty=subprocess.check_output(['git','diff','--name-only','HEAD','-z'],text=True).split('\0')
for p in filter(None,dirty):write(p,head(p))
# Renderer outputs must never share writable inodes with the live tree.
manifest=json.loads((DEST/'_process/architecture/generated-manifest.json').read_text())
print('Manifest keys',list(manifest),flush=True)
for p in list((DEST/'theories/becoming/results/records').glob('*.md')):
 write(str(p.relative_to(DEST)),p.read_bytes())
for p in ['README.md','RESEARCH.md','ROADMAP.md','RESULTS.md','GOALS.md','DEPENDENCIES.md','_process/BRIEF.md','_process/architecture/generated-manifest.json']:
 if (DEST/p).exists():write(p,(DEST/p).read_bytes())
# The gitdir is used only for reading historical objects and the renderer lock.
gitdir=subprocess.check_output(['git','rev-parse','--absolute-git-dir'],text=True).strip()
write('.git','gitdir: '+gitdir+'\n')
root='_process/research/2026-10-05-generative-foundation-review/root-foundation/'
core='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
per='experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/'
own=[root+'RISK-CONDITIONING-INTEGRATION.md',root+'OPEN-FORM-BRIDGE-CHECKS.json',root+'development/complete_open_form_bridge.py','theories/becoming/chapters/CHOICE-AND-GENERATIVE-CONTEXT.md',core+'Becoming/Bridge.lean']
for p in own:copy(p)
for directory in [core+'becoming-checks/20261013T102207.009826Z',per+'correction-inquiry-checks/20261013T102329.171691Z']:
 for p in (ROOT/directory).rglob('*'):
  if p.is_file():copy(str(p.relative_to(ROOT)))
write(core+'becoming-verification.json',(DEST/(core+'becoming-checks/20261013T102207.009826Z/verification.json')).read_bytes())
write(per+'correction-inquiry-verification.json',(DEST/(per+'correction-inquiry-checks/20261013T102329.171691Z/verification.json')).read_bytes())
# Shared chapter: only P89 prose, Bridge count and P89-frozen totals.
chapter='theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
b=head(chapter).decode();c=(ROOT/chapter).read_text();start=c.index('**既有开放形态成果的正式接入，P89');end=c.index('\nRen 2026-10-11 问：',start);addition=c[start:end]
anchor='### 6.13 生成的空间，不用公理（P56）/ The generative space, with no axiom (P56)\n\n';assert anchor in b;b=b.replace(anchor,anchor+addition+'\n')
oldline=next(l for l in b.splitlines() if l.startswith('| 桥接 / Bridge |'));b=b.replace(oldline,oldline.removesuffix('40 |')+'48 |')
b=b.replace('与[回执](../../../'+core+'becoming-verification.json)覆盖 4518 项定理、6370 项声明审计','的[P89 冻结回执](../../../'+core+'becoming-checks/20261013T102207.009826Z/verification.json)覆盖 4522 项定理、6374 项声明审计')
b=b.replace('15 个继承模块的当前字节须与已通过的回执一致。','24 个继承模块按该回执的检查器口径分列，所核查源文由回执哈希绑定。')
b=b.replace('The consolidated checker and receipt cover 4518 theorems and 6370 declaration audits','The P89 frozen receipt covers 4522 theorems and 6374 declaration audits').replace('The current bytes of 15 inherited modules must match passed receipts.','Its checker counts 24 inherited modules separately, binding the checked source versions by hash.')
assert 'P91' not in b;write(chapter,b)
# Reapply the preserved one-shot procedure solely against original HEAD records.
script=(DEST/(root+'development/complete_open_form_bridge.py')).read_text();script=script[script.index('from pathlib import Path'):];script=script.replace("ROOT=Path('/Users/ren/theories')",'ROOT=Path('+repr(str(DEST))+')')
# Retain the original P89 review timestamp, not a spurious new scientific review.
review=json.loads((ROOT/'theories/becoming/results/records/open-form-realization-under-revision.json').read_text())['reviewed_at_utc'];script=script.replace('now=datetime.now(timezone.utc).isoformat()','now='+repr(review))
# Break record hard links before this historical procedure writes them.
for p in (DEST/'theories/becoming/results/records').glob('*.json'):write(str(p.relative_to(DEST)),p.read_bytes())
exec(compile(script,'historical-P89-procedure','exec'),{})
# Only P89's workboard row and completion section.
p='_process/BECOMING-WORKBOARD.md';b=head(p).decode();c=(ROOT/p).read_text();row=next(l for l in c.splitlines() if l.startswith('| P89 '));anchor='|---|---|---|---|---|\n';assert b.count(anchor)==1;b=b.replace(anchor,anchor+row+'\n');section=c[c.index('### P89 queue / P89 队列'):].split('\n### ',1)[0];write(p,b+'\n'+section.rstrip()+'\n')
# Curated chain: M20 alone and the five actually reviewed P89 sources.
p='theories/becoming/results/data/generativity-chain.json';b=json.loads(head(p));c=json.loads((ROOT/p).read_text());m20=next(e for s in c['sections'] for e in s['entries'] if e['id']=='M20')
for s in b['sections']:
 for i,e in enumerate(s['entries']):
  if e['id']=='M20':s['entries'][i]=m20
b['updated']='2026-10-13'
reviewed=[root+'RISK-CONDITIONING-INTEGRATION.md','theories/becoming/chapters/CHOICE-AND-GENERATIVE-CONTEXT.md','theories/becoming/results/records/open-form-realization-under-revision.json',core+'Becoming/Bridge.lean',core+'becoming-checks/20261013T102207.009826Z/verification.json']
for p2 in reviewed:b['reviewed_sources'][p2]=sha(p2)
write(p,json.dumps(b,ensure_ascii=False,indent=2)+'\n')
import importlib.util
spec=importlib.util.spec_from_file_location('p89_gc',DEST/'tools/research/generative_chain.py');gc=importlib.util.module_from_spec(spec);spec.loader.exec_module(gc)
render=gc.render(b);p='theories/becoming/results/GENERATIVITY-CHAIN.md';lines=head(p).decode().splitlines();newrow=next(l for l in render.splitlines() if l.startswith('| M20 |'));date=next(l for l in render.splitlines() if l.startswith('内容更新 /'));write(p,'\n'.join(newrow if l.startswith('| M20 |') else date if l.startswith('内容更新 /') else l for l in lines)+'\n')
p=root+'GENERATIVITY-CHAIN-INDEX-RECORD.md';c=(ROOT/p).read_text();s=c[c.index('## 开放形态成果的脊柱结项 /'):].split('\n## ',1)[0];write(p,head(p).decode()+'\n\n'+s.rstrip()+'\n')
# Historical-object reads are finished; use a private renderer lock.
(DEST/'.git').unlink()
subprocess.run(['git','init','-q',str(DEST)],check=True)
# Preserve this finite preparation procedure, not the private tree or caches.
write(root+'development/prepare_open_form_closure.py',Path(__file__).read_bytes())
# Break remaining generated outputs named in the manifest.
paths=[]
def visit(x):
 if isinstance(x,dict):
  for k,v in x.items():
   if isinstance(k,str) and (DEST/k).is_file():paths.append(k)
   visit(v)
 elif isinstance(x,list):
  for y in x:visit(y)
 elif isinstance(x,str) and '\n' not in x and len(x)<300 and (DEST/x).is_file():paths.append(x)
visit(manifest)
for p in set(paths):write(p,(DEST/p).read_bytes())
Path('/tmp/p89-closure-location.json').write_text(json.dumps({'root':str(ROOT),'snapshot':str(DEST),'base':BASE,'owned_sources':own,'receipt':core+'becoming-checks/20261013T102207.009826Z/verification.json'})+'\n')
print('Prepared P89-only tree:',DEST,flush=True)
