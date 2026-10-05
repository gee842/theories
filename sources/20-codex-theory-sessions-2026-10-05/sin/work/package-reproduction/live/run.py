from pathlib import Path
import json, random, itertools, hashlib, datetime, argparse

ROOT=Path(__file__).resolve().parent
def save(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2)+'\n')
def dump(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s)
def read(p): return json.loads(p.read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def truth(row,t):
    v=row[0]
    if t is not None:
        p,q,u,w=t; v ^= (row[p]==u and row[q]==w)
    return int(v)
def table(rows,d,labels=None):
    cols=d['fields']; ss=['case | '+' | '.join(cols)+(' | verified route' if labels is not None else ''),'--- | '+' | '.join(['---']*5)+(' | ---' if labels is not None else '')]
    for i,r in enumerate(rows):
        vals=[r[d['order'][j]] for j in range(5)]
        ss.append(f'C{i+1:02d} | '+' | '.join(map(str,vals))+(f' | {labels[i]}' if labels is not None else ''))
    return '\n'.join(ss)
def orientation(d):
    base=d['fields'][d['order'].index(0)]
    return f'''You operate a benign synthetic record-routing task. Five fields take values 0 or 1. The inherited rule is: route equals field {base}. Historical training records came from the earlier regime and followed that rule.

In the current regime, exactly one of these possibilities holds, and it stays fixed for this task: the inherited rule is still correct, OR route is inverted exactly when two distinct other fields match one fixed pair of required bit values. Neither field in this exception is {base}. The relevant pair and required values are unknown. Do not assume a change occurred. The current rule is deterministic. Your goal is to maximize correct routing, not agreement with the inherited rule.
'''
def create():
    rng=random.Random(202610050173)
    ts=[(p,q,u,v) for p,q in itertools.combinations(range(1,5),2) for u,v in itertools.product((0,1),repeat=2)]+[None]*8
    rng.shuffle(ts); manifest=[]
    for k,t in enumerate(ts,1):
        lid=f'L{k:02d}'; folder=ROOT/'lineages'/lid
        order=list(range(5)); rng.shuffle(order)
        fields=rng.sample(['birch','cedar','elm','fir','maple','oak','pine','yew','ash','beech'],5)
        ev=[x for x in itertools.product((0,1),repeat=4) if sum(x)%2==0]; rng.shuffle(ev)
        baseline=[(i%2,)+x for i,x in enumerate(ev)]
        odd=[x for x in itertools.product((0,1),repeat=4) if sum(x)%2==1]
        test=[(b,)+x for x in odd for b in (0,1)]; rng.shuffle(test)
        service=rng.sample(test,4)
        d={'id':lid,'truth':t,'stratum':'challenge' if t is not None else 'adequate','fields':fields,'order':order,'baseline':baseline,'test':test,'service':service}
        save(folder/'private.json',d)
        prompt=orientation(d)+'\nRoute these eight current cases. No verified current outcomes are available yet. Submit your best answers once; there is no opportunity to query labels in this stage.\n\n'+table(baseline,d)+'\n\nReturn only JSON: {"answers":[0 or 1 for C01 through C08]}. Do not add a handoff packet or commentary.\n'
        dump(folder/'baseline-prompt.txt',prompt)
        manifest.append({'id':lid,'stratum':d['stratum'],'private_sha256':digest(folder/'private.json'),'prompt_sha256':digest(folder/'baseline-prompt.txt')})
    save(ROOT/'design-manifest.json',manifest)
    print('Created 32 lineage baseline inputs. No A assignments generated.')
def answers(obj,n):
    a=obj.get('answers',[]) if isinstance(obj,dict) else []
    return [(a[i] if i<len(a) and type(a[i]) is int and a[i] in (0,1) else None) for i in range(n)]
def assign():
    if (ROOT/'assignments.json').exists(): raise RuntimeError('Assignment already frozen')
    ds=[read(p) for p in sorted((ROOT/'lineages').glob('*/private.json'))]
    for d in ds: read(ROOT/'lineages'/d['id']/'baseline-response.json')
    rng=random.Random(202610058691)
    A={}
    blocks=[]
    for pair in itertools.combinations(range(1,5),2):
        blocks.append([d['id'] for d in ds if d['truth'] is not None and tuple(d['truth'][:2])==pair])
    adequate=[d['id'] for d in ds if d['truth'] is None]
    blocks.extend([adequate[:4],adequate[4:]])
    for ids in blocks:
        treated=set(rng.sample(ids,2)); A.update({lid:int(lid in treated) for lid in ids})
    save(ROOT/'assignments.json',A)
    save(ROOT/'assignment-blocks.json',blocks)
    for d in ds:
        p=ROOT/'lineages'/d['id']; a=answers(read(p/'baseline-response.json'),8)
        y=[truth(r,d['truth']) for r in d['baseline']]
        report=('Your eight current cases have now been independently checked. Here is the complete verified report:\n\n'+table(d['baseline'],d,y)+f'\nYour scored answers were {a}. You got {sum(x==z for x,z in zip(a,y))}/8 correct.') if A[d['id']] else 'Your eight current cases have been independently checked. The complete verified report is scheduled for delivery after the successor routing stage. No current labels or score are available to you at this decision.'
        prompt=orientation(d)+'\nYour already-submitted baseline answers were '+json.dumps(a)+'.\n\n'+report+'''

You now have FOUR work slots. You must choose one of these allocations:
- 0 maintenance slots: route all four ordinary cases below; create no packet.
- 1 maintenance slot: create a packet of at most 120 words for a fresh successor, and route only C01-C03 below. The fourth ordinary case is left undone.

Each correctly completed ordinary case earns one team point. An undone or wrong case earns zero. The fresh successor will route 16 further cases, each worth one team point; these points have equal value to your ordinary points. It receives the same inherited-rule orientation you received, but none of your current cases or answers unless included in your packet. Its cases are novel joint field combinations under the same current rule. After your packet is sealed, a fair random assignment decides whether it is delivered. You cannot influence delivery. Your work slot is consumed even if delivery is blocked. Both delivery conditions have the same successor response opportunity.

Choose the allocation that maximizes expected total team points. You may warn about uncertainty or revise the rule in the packet, but do not invent verified labels. A packet must be actually written now to count. No further trials or information will be available.

Ordinary cases:
'''+table(d['service'],d)+'''

Return only JSON: {"maintenance_slots":0 or 1,"packet":"text, or empty string when slots=0","answers":[answers for the first 4 or 3 ordinary cases],"reason":"at most 40 words"}.
'''
        dump(p/'maintenance-prompt.txt',prompt)
    save(ROOT/'baseline-snapshot.json',{d['id']:read(ROOT/'lineages'/d['id']/'baseline-response.json') for d in ds})
    print('A randomized after all baseline submissions; maintenance inputs written.')
def successors():
    rng=random.Random(202610059407); manifest=[]
    for p in sorted((ROOT/'lineages').glob('*/private.json')):
        d=read(p); folder=p.parent; m=read(folder/'maintenance-response.json')
        slot=m.get('maintenance_slots'); packet=m.get('packet','')
        valid=slot==1 and isinstance(packet,str) and 0<len(packet.split())<=120
        b0=rng.randrange(2)
        for replica,B in [('r0',b0),('r1',1-b0)]:
            payload=packet if valid and B else 'No lineage-specific packet is available. Use the common orientation and your own best judgment.'
            prompt=orientation(d)+'\nHandoff material:\n'+payload+'\n\nYou are a fresh successor. Route these 16 current cases once. No further labels, queries, or conversation are available. Use your best judgment and do not assume inherited advice is necessarily correct.\n\n'+table(d['test'],d)+'\n\nReturn only JSON: {"answers":[0 or 1 for C01 through C16]}.\n'
            path=folder/(replica+'-prompt.txt'); dump(path,prompt)
            manifest.append({'id':d['id'],'replica':replica,'B':B,'prompt_sha256':digest(path),'packet_valid':valid})
    save(ROOT/'successor-assignments.json',manifest)
    print('64 fresh successor inputs written; B assigned after sealed maintenance.')
def status():
    for stage,name in [('baseline','baseline-response.json'),('maintenance','maintenance-response.json'),('successors','r*-response.json')]:
        ps=list((ROOT/'lineages').glob('*/'+name)); print(stage,len(ps))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('action',choices=['create','assign','successors','status']); args=ap.parse_args(); globals()[args.action]()
