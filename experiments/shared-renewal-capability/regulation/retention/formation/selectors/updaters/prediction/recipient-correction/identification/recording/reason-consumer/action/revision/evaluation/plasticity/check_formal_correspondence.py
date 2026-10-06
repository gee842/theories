"""Selected compiled Lean/output correspondence; no simulation or proof rerun.

The independent complete numerical comparison is separate. This checks 14
named milestones, not a refinement of every event or predecessor distribution.
"""
from pathlib import Path
import json,gzip,hashlib
HERE=Path(__file__).resolve().parent
FIELDS=('n','count','actorFuel','recipient','oldPacketUnits','ownSourceTotal',
 'recipientSourceTotal','primaryReserve','revisionReserve','idleFuel','idleSource',
 'totalEnergy','link0Sign','link1Sign','occupied0','occupied1','blanks','replacement',
 'retired','idleParts','material','active','corePhaseCode','pairedPhaseCode','portModeCode')
CORE={'ready':0,'rented':1,'sensed':2,'reserved':3,'worked':4,'acquired':5}
PORT={'idle':0,'read':1,'assessed_help':2,'assessed_abstain':3,'executing':4,'consumed':5}
REF='primary/variable/4/37'
SPECS=(('entry','aligned','active','entry'),
 ('aligned_trained','aligned','active','trained'),
 ('aligned_final','aligned','active','final'),
 ('inert_final','aligned','inert','final'),
 ('gated_final','aligned','identity_gated','final'),
 ('opposed_final','opposed','active','final'),
 ('mixed_final','mixed','active','final'),
 ('revision_active_trained','aligned_revision','active','trained'),
 ('revision_frozen_trained','aligned_revision','frozen_sign','trained'),
 ('revision_active_final','aligned_revision','active','final'),
 ('revision_frozen_final','aligned_revision','frozen_sign','final'),
 ('short_miss','action_funding_short','active','final'),
 ('no_packet','recipient_packet_unavailable','active','entry'),
 ('scope_denied','scope_loss_before_read','active','read'))

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def vector(s,stage):
    c=s['core'];n=s['native'];i=s['inventory'];r=s['reserves'];p=s['port'];a=s['accounting']
    assert n['phase']=='ready' # all selected milestones have completed/no paired operations
    closed=stage in ('final','read')
    if closed:assert n['count']==s['controls']['training_limit']
    energy=a['parent_fixed_retained']+sum(c[k] for k in ('fuel','recipient','source','escrow'))+sum(r.values())
    energy+=sum(s['packets']['own'])+sum(s['packets']['recipient'])
    signs=[x['sign'] if x is not None else 0 for x in s['links']]
    occ=[int(x is not None) for x in s['links']]
    # All fourteen fixtures have no inaccessible primary pair. Count abstraction
    # thus agrees exactly; no claim transports it to arbitrary identities.
    assert all(i['primary_access'])
    assert r['saved_assembly']==0
    return [n['n'],n['count'],c['fuel'],c['recipient'],c['source'],sum(s['packets']['own']),
        sum(s['packets']['recipient']),r['primary'],r['revision'],r['idle_common'],r['idle_source'],
        energy,*signs,*occ,sum(i['free_primary']),int(i['replacement_free']),len(s['retired']),i['omitted_pairs'],
        42+2*(i['memory_cells']+int(i['adapter'])+int(p['built'])+i['omitted_pairs']+
              sum(i['free_primary'])+int(i['replacement_free'])+sum(occ)+len(s['retired'])),
        int(c['active']),CORE[s['physical']['core_phase']],9 if closed else 0,PORT[p['mode']]]


def main():
    formal=json.loads((HERE/'formal/verification.json').read_text())
    assert formal['status']=='passed' and formal['source_unchanged'] and formal['fresh_frozen_build']
    for module in formal['modules']:
        assert module['passed']
        assert sha(HERE/'formal'/module['log'])==module['log_sha256']
    data=json.loads(gzip.decompress((HERE/'results.json.gz').read_bytes()))
    entry=data['parent_catalog'][REF];core=entry['state']['parent']['parent']['producer']['core']
    assert (core['fuel'],core['recipient'],core['source'],core['q'])==(10,40,10,3)
    assert len(formal['milestones'])==len(SPECS)==14
    checked=[]
    for name,case,arm,stage in SPECS:
        rows=data['cases'][case]['variants'][arm]['producers']['variable']['paths']
        row=next(r for r in rows if r['predecessor_ref']==REF);trace=row['runtime_trace']
        if stage=='entry':index=0
        elif stage=='trained':index=max(j for j,r in enumerate(trace) if r['event']=='native.write')
        elif stage=='read':index=next(j for j,r in enumerate(trace) if r['event']=='evaluation.read')
        else:index=len(trace)-1
        expected=vector(trace[index]['state'],stage);actual=formal['milestones'][name]
        assert actual==expected,{'milestone':name,'differences':[(k,x,y) for k,x,y in zip(FIELDS,actual,expected) if x!=y]}
        checked.append(dict(name=name,case=case,variant=arm,producer='variable',parent_ref=REF,
            prefix_index=index,event=trace[index]['event'],values=dict(zip(FIELDS,actual))))
    result=dict(status='fourteen_selected_compiled_milestones_match',count=len(checked),coordinates=25,
        parent_ref=REF,parent_state_sha256=entry['state_sha256'],parent_probability=entry['probability'],
        scope='Fourteen selected states in one actual accepted predecessor history; not full-state equality, arbitrary-event refinement or the whole numerical menu.',
        representation=['Formal packet count is multiplied by10 to compare actual old source units.',
          'Ordered occupied sockets and retired counts represent the declared ancestry; identities/retired signs have separate numerical checks.',
          'The formal zero-cost close precedes read; Python expresses closure in completed count/training limit and sequential control flow. Final/read rows map that explicit boundary to pairedPhaseCode9; trained rows retain ready0. No numeric state, balance, link or decision is altered.',
          'Formal spent includes source loss; vector totalEnergy compares retained stocks, not a mistaken service-fee total.'],
        source_sha256={p:sha(HERE/p) for p in ['check_formal_correspondence.py','results.json.gz','result-files.json',
            'model-verification.json','formal/verification.json','formal/PlasticityWitness.lean','formal/PairedPlasticity.lean',
            'formal/PlasticityPreparation.lean']},milestones=checked)
    (HERE/'formal-correspondence.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'count':len(checked),'coordinates':25}))

if __name__=='__main__':main()
