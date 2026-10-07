# Fresh closure build + axiom audit used by the process-law thread (7 October 2026).
# Usage, from experiments/integrated-correction/general-framework/generative-basis/lean:
#   LEAN=/path/to/lean EXTRA=dir1:dir2 python3 <this file> . Module1 Module2 ...
# Builds the import closure of the named modules in a temp dir, one module at a time,
# and prints module count, audit count and any module with warnings, errors or nonempty #print axioms.
import re,sys,subprocess,tempfile,os,pathlib
CORE=pathlib.Path(sys.argv[1]); L=os.environ.get('LEAN','/opt/lean/lean-4.29.1-linux/bin/lean')
idx={}
roots=[CORE]+[pathlib.Path(x) for x in os.environ.get('EXTRA','').split(':') if x]
for p in (q for r in roots for q in r.rglob('*.lean')):
    if 'sources' in p.parts or 'snapshots' in p.parts or 'legacy' in str(p) or 'verification' in str(p) or 'runs' in str(p): continue
    idx.setdefault(p.stem,[]).append(p)
order=[];seen=set()
def visit(n):
    if n in seen: return
    seen.add(n); ps=idx[n]; assert len(ps)==1,(n,ps)
    for m in re.findall(r'^import\s+(\S+)',ps[0].read_text(),re.M):
        if m in idx: visit(m)
        else: assert m.startswith(('Init','Std','Lean')),m
    order.append(n)
for e in sys.argv[2:]: visit(e)
b=tempfile.mkdtemp(); A=re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
tot=0;bad=[]
for n in order:
    (pathlib.Path(b)/(n+'.lean')).write_bytes(idx[n][0].read_bytes())
    r=subprocess.run([L,'-o',n+'.olean',n+'.lean'],cwd=b,env=dict(os.environ,LEAN_PATH=b),capture_output=True,text=True)
    out=r.stdout+r.stderr; au=A.findall(out); tot+=len(au)
    ne=[d for d,a in au if a.strip()]
    if r.returncode or re.search(r'warning|error',out) or ne: bad.append((n,r.returncode,ne,out[-800:]))
print(len(order),'modules',tot,'audits'); print('bad',bad)
