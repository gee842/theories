#!/usr/bin/env python3
"""Fresh pinned proof build and independent finite protocol reconstruction.

Does not alter ancestor laws or verification receipts. The 80 blocked words
are recorded at their first inadmissible event, not advanced past that event.
"""
from pathlib import Path
import hashlib, json, os, re, subprocess, tempfile, time

HERE = Path(__file__).resolve().parent
FORMAL = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())

def sha(data):
    return hashlib.sha256(data).hexdigest()

def oracle(own, recipient):
    """Integer/event reconstruction, independent of Lean's state evaluator."""
    s = dict(count=0, n=0, p=40, fuel=10, training=22, revision=12,
             ownSource=[2]*6, recipientSource=[2]*6, links=[0,0],
             blanks=2, retired=0, ownBit=False, recipientBit=False,
             phase=0, energy=118, steps=0)
    done = True
    for i in range(4):
        y, x = bool(own & (1 << i)), bool(recipient & (1 << i))
        events = [('ownPay',None),('ownReturn',not y),('recipientPay',None),
                  ('recipientReturn',not x),('ownRead',None),('recipientRead',None),
                  ('bind' if x else 'skip',None),('nativeWrite',None)]
        for event, arg in events:
            c, phase = s['count'], s['phase']
            tr = min(6,s['training']) if c < 4 else min(7 if c == 4 else 5,s['revision'])
            ok = {
                'ownPay': phase == 0 and c < 6 and s['ownSource'][c] >= 2
                    and s['recipientSource'][c] >= 2 and s['p'] >= 2 and s['fuel']+tr >= 2,
                'ownReturn': phase == 1 and (2 if arg else 0) <= s['ownSource'][c],
                'recipientPay': phase == 2 and s['p'] >= 2,
                'recipientReturn': phase == 3 and (2 if arg else 0) <= s['recipientSource'][c],
                'ownRead': phase == 4 and s['fuel'] >= 1,
                'recipientRead': phase == 5 and s['fuel'] >= 1,
                'bind': phase == 6 and s['recipientBit'] and c < 6 and 0 in s['links']
                    and s['blanks'] >= 1 and s['fuel'] >= 1,
                'skip': phase == 6 and not s['recipientBit'],
                'nativeWrite': phase == 8 and c < 6 and s['fuel'] >= 1,
            }[event]
            if not ok:
                done = False
                break
            s['steps'] += 1
            charge = {'ownPay':2,'recipientPay':2,'ownRead':1,'recipientRead':1,
                      'bind':1,'nativeWrite':1}.get(event,0)
            s['energy'] -= charge
            if event == 'ownPay':
                s['fuel'] += tr-2
                s['training' if c < 4 else 'revision'] -= tr
                s['phase'] = 1
            elif event == 'ownReturn':
                r = 2 if arg else 0
                s['fuel'] += r; s['ownSource'][c] -= r
                s['ownBit'] = arg; s['phase'] = 2
            elif event == 'recipientPay':
                s['p'] -= 2; s['phase'] = 3
            elif event == 'recipientReturn':
                r = 2 if arg else 0
                s['p'] += r; s['recipientSource'][c] -= r
                s['recipientBit'] = arg; s['phase'] = 4
            elif event == 'ownRead':
                s['fuel'] -= 1; s['ownBit'] = not s['ownBit']; s['phase'] = 5
            elif event == 'recipientRead':
                s['fuel'] -= 1; s['recipientBit'] = not s['recipientBit']; s['phase'] = 6
            elif event == 'bind':
                s['fuel'] -= 1
                s['links'][s['links'].index(0)] = 1 if s['ownBit'] else -1
                s['blanks'] -= 1; s['phase'] = 8
            elif event == 'skip':
                s['phase'] = 8
            elif event == 'nativeWrite':
                s['fuel'] -= 1; s['n'] = s['n']//2 + 4*int(s['ownBit'])
                s['count'] += 1; s['ownBit'] = s['recipientBit'] = False; s['phase'] = 0
        if not done:
            break
    c = s['count']
    tr = min(6,s['training']) if c < 4 else min(7 if c == 4 else 5,s['revision'])
    next_pay = s['phase'] == 0 and c < 6 and s['ownSource'][c] >= 2 and s['recipientSource'][c] >= 2 and s['p'] >= 2 and s['fuel']+tr >= 2
    return [own,recipient,int(done),s['steps'],s['count'],s['n'],s['p'],s['fuel'],
            sum(x != 0 for x in s['links']),s['retired'],s['blanks'],*s['links'],
            int(s['ownBit']),int(s['recipientBit']),s['phase'],s['training'],s['revision'],
            sum(s['ownSource']),sum(s['recipientSource']),s['energy'],int(next_pay)]

def main():
    ancestor_bytes = (FORMAL/'verification.json').read_bytes()
    ancestor = json.loads(ancestor_bytes)
    assert ancestor['status'] == 'passed'
    sources = {}
    for m in ancestor['modules']:
        p = REPO/m['source']; data = p.read_bytes()
        assert sha(data) == m['sha256'], m['module']
        sources[m['module']] = (p,data)
    sources['PretrainingEvidence'] = (FORMAL/'PretrainingEvidence.lean',(FORMAL/'PretrainingEvidence.lean').read_bytes())
    sources['Enumeration'] = (HERE/'Enumeration.lean',(HERE/'Enumeration.lean').read_bytes())
    requested = set(re.findall(r'^#print axioms ([\w.]+)$',sources['PretrainingEvidence'][1].decode(),re.M))
    declared = set(re.findall(r'^theorem (\w+)',sources['PretrainingEvidence'][1].decode(),re.M))
    assert {n.rsplit('.',1)[-1] for n in requested} == declared
    for name,(_,data) in sources.items():
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b',data.decode()),name
        assert not re.search(r'^\s*(axiom|constant)\s',data.decode(),re.M),name
        assert set(re.findall(r'^import\s+(\S+)',data.decode(),re.M)) <= set(sources)|{'Std'},name
    run_dir = HERE/'runs'/str(time.time_ns()); run_dir.mkdir(parents=True)
    checker = Path(__file__).read_bytes(); (run_dir/'check.py').write_bytes(checker)
    for name in ('PretrainingEvidence','Enumeration'):
        (run_dir/(name+'.lean')).write_bytes(sources[name][1])
    tool = (FORMAL/'lean-toolchain').read_bytes()
    (run_dir/'lean-toolchain').write_bytes(tool)
    rows = []; enumeration = []
    with tempfile.TemporaryDirectory(prefix='pretraining-evidence-fresh-') as tmp:
        b = Path(tmp); (b/'lean-toolchain').write_bytes(tool)
        for name,(_,data) in sources.items(): (b/(name+'.lean')).write_bytes(data)
        env = dict(os.environ,LEAN_PATH=str(b))
        for name,(p,data) in sources.items():
            result = subprocess.run(['lean','-o',name+'.olean',name+'.lean'],cwd=b,env=env,
                text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=240)
            (run_dir/(name+'.txt')).write_text(result.stdout)
            audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",result.stdout)
            expected = next((set(m['declarations']) for m in ancestor['modules'] if m['module']==name), requested if name=='PretrainingEvidence' else set())
            deps = sorted({x.strip() for _,v in audits for x in v.split(',') if x.strip()})
            assert result.returncode == 0 and 'warning:' not in result.stdout,(name,result.stdout)
            assert {n for n,_ in audits} == expected and len(audits)==len(expected),name
            assert set(deps) <= {'propext','Quot.sound','Classical.choice'},(name,deps)
            rows.append(dict(module=name,source=str(p.relative_to(REPO)),sha256=sha(data),audits=len(audits),axioms=deps,log_sha256=sha(result.stdout.encode())))
            if name == 'Enumeration':
                enumeration = [json.loads(x) for x in re.findall(r'^PRETRAINING (\[.*\])$',result.stdout,re.M)]
            print(name+' passed',flush=True)
    independent = [oracle(a,b) for a in range(16) for b in range(16)]
    assert enumeration == independent
    admitted = [r for r in enumeration if r[2]]; blocked = [r for r in enumeration if not r[2]]
    assert len(admitted)==176 and len(blocked)==80
    assert all(r[6]+2*r[8]==40 and r[4]==4 and r[13:16]==[0,0,0] for r in admitted)
    assert all(r[8]==2 and r[6]==34 and r[14]==1 and r[15]==6 for r in blocked)
    assert all(p.read_bytes()==data for p,data in sources.values())
    assert (FORMAL/'verification.json').read_bytes()==ancestor_bytes and Path(__file__).read_bytes()==checker
    result = dict(status='passed',fresh_build=True,ancestor_receipt_sha256=sha(ancestor_bytes),
        checker_sha256=sha(checker),toolchain=tool.decode().strip(),modules=rows,new_theorems=len(requested),
        new_axioms=next(x['axioms'] for x in rows if x['module']=='PretrainingEvidence'),
        schedules=256,admitted=len(admitted),blocked=len(blocked),compared_coordinates=256*22,
        admitted_patient_distribution={str(v):sum(r[6]==v for r in admitted) for v in (40,38,36)},
        unchanged_inputs=True,rows=enumeration,columns=['own_mask','recipient_mask','complete','admitted_events','count','n','patient','fuel','occupied','retired','blanks','link0','link1','own_bit','recipient_bit','phase','training','revision','own_source_total','recipient_source_total','energy','next_ownPay_enabled'])
    (run_dir/'receipt.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 16 new theorem audits; 256 exact rows, 176 admitted and 80 blocked.',flush=True)

if __name__ == '__main__':
    main()
