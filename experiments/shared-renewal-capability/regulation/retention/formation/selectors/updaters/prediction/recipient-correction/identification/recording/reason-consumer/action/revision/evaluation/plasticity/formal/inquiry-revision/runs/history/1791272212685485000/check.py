#!/usr/bin/env python3
"""Fresh additive proof build; pin and preserve all source bytes per attempt."""
from pathlib import Path
import hashlib, json, os, re, subprocess, tempfile, time

HERE=Path(__file__).resolve().parent
FORMAL=HERE.parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').exists())
def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    inherited=json.loads((FORMAL/'verification.json').read_text())
    assert inherited['status']=='passed'
    sources={m['module']:REPO/m['source'] for m in inherited['modules']}
    for m in inherited['modules']:
        assert sha(sources[m['module']].read_bytes())==m['sha256'],m['module']
    sources['PretrainingEvidence']=FORMAL/'PretrainingEvidence.lean'
    sources['InquiryRevision']=HERE/'InquiryRevision.lean'
    frozen={n:p.read_bytes() for n,p in sources.items()}
    requested={}
    for n,b in frozen.items():
        text=b.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b',text),n
        assert not re.search(r'^\s*(axiom|constant)\s',text,re.M),n
        assert set(re.findall(r'^import\s+(\S+)',text,re.M))<=set(sources)|{'Std'},n
        requested[n]=set(re.findall(r'^#print axioms ([\w.]+)',text,re.M))
        if n=='InquiryRevision':
            assert {x.rsplit('.',1)[-1] for x in requested[n]}==set(re.findall(r'^theorem (\w+)',text,re.M))
    attempt=HERE/'runs'/str(time.time_ns());attempt.mkdir(parents=True)
    tool=(FORMAL/'lean-toolchain').read_bytes()
    checker=Path(__file__).read_bytes()
    (attempt/'check.py').write_bytes(checker)
    (attempt/'lean-toolchain').write_bytes(tool)
    for n,b in frozen.items():(attempt/(n+'.lean')).write_bytes(b)
    rows=[];milestones={}
    with tempfile.TemporaryDirectory(prefix='inquiry-revision-lean-') as tmp:
        build=Path(tmp);(build/'lean-toolchain').write_bytes(tool)
        for n,b in frozen.items():(build/(n+'.lean')).write_bytes(b)
        env=dict(os.environ,LEAN_PATH=str(build))
        for n,p in sources.items():
            result=subprocess.run(['lean','-o',n+'.olean',n+'.lean'],cwd=build,env=env,
                text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=240)
            (attempt/(n+'.txt')).write_text(result.stdout)
            audits=re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",result.stdout)
            axioms=sorted({x.strip() for _,a in audits for x in a.split(',') if x.strip()})
            passed=result.returncode==0 and 'warning:' not in result.stdout and {x[0] for x in audits}==requested[n] and len(audits)==len(requested[n]) and set(axioms)<={'propext','Quot.sound','Classical.choice'}
            rows.append(dict(module=n,source=str(p.relative_to(REPO)),sha256=sha(frozen[n]),passed=passed,
                declarations=[x[0] for x in audits],axioms=axioms,log=str((attempt/(n+'.txt')).relative_to(REPO))))
            if n=='InquiryRevision':
                milestones={k:json.loads(v) for k,v in re.findall(r'^INQUIRY (\w+) (\[.*\])$',result.stdout,re.M)}
            print(n+' '+('passed' if passed else 'FAILED'),flush=True)
            if not passed:
                print(result.stdout,flush=True);break
    stable=all(p.read_bytes()==frozen[n] for n,p in sources.items()) and Path(__file__).read_bytes()==checker
    passed=len(rows)==len(sources) and all(x['passed'] for x in rows) and stable
    receipt=dict(status='passed' if passed else 'failed',fresh_build=True,source_unchanged=stable,
        toolchain=tool.decode().strip(),checker_sha256=sha(checker),modules=rows,
        new_audits=sum(len(x['declarations']) for x in rows if x['module']=='InquiryRevision'),
        inherited_audits=sum(len(x['declarations']) for x in rows if x['module']!='InquiryRevision'),milestones=milestones)
    (attempt/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    if passed:(HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('RECEIPT '+str(attempt/'receipt.json'),flush=True)
    raise SystemExit(0 if passed else 1)

if __name__=='__main__':main()
