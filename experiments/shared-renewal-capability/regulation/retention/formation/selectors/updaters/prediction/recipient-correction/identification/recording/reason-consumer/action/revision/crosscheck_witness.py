"""Read-only comparison of frozen concrete Lean witness and saved runtime stages.

This does not compile Lean or execute transitions. It compares the constants in
the final witness statements with the actual matching-orientation saved path.
"""
from pathlib import Path
import gzip
import hashlib
import json

HERE=Path(__file__).resolve().parent
FORMAL_HASHES={
    'RevisionPreparation.lean':'11278b802f0221eb229fe6eefdcf5a439c72851558cec862d8cfc1e1f35d4b94',
    'FreshRevision.lean':'2752540ebf8680e35ef28b37d0731dca6e3abdb4f175f693797491af435afd38',
    'RevisionWitness.lean':'2f2575d664a5436ee341a37488146b84e94a18414a911e1b13385057df6b831f'}


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def reduced(s):
    a=s['parent'];w=a['parent'];p=w['producer'];c=p['core']
    energy=sum(c[k] for k in ('fuel','recipient','source','escrow'))
    energy+=sum(p[k] for k in ('archive_fuel','reader_fuel','idle_fuel','packet_inflight','archive_escrow'))
    energy+=w['extra_reserve']+w['external_idle']
    energy+=sum(a[k] for k in ('command_reserve','later_reserve','source_reserve','saved_assembly'))
    energy+=sum(s[k] for k in ('actor_reserve','writer_fuel','writer_escrow','reader_reserve',
                              'source_reserve','idle_fuel','idle_source','saved_assembly'))
    return dict(fuel=c['fuel'],patient=c['recipient'],source=c['source'],q=c['q'],
        qualified=bool(c['last']),energy=energy,old_context=p['context'],old_next=p['query_pointer'],
        new_next=s['fresh']['next'],new_cells=s['fresh']['cells'],reader=p['reader_fuel'])


def main():
    for name,h in FORMAL_HASHES.items():assert sha(HERE/'formal'/name)==h,name
    packed=(HERE/'results.json.gz').read_bytes();r=json.loads(gzip.decompress(packed))
    rows=r['cases']['primary']['producers']['variable']['paths']
    index=next(i for i,row in enumerate(rows) if row['observer']['strict_parent'] and row['observer']['old_law']==1)
    row=rows[index]
    expected={
        'actual_parent_with_protected_extension':(0,30,0,2,True,117,0),
        'paid_open_reset_unknown':(26,30,30,2,False,115,0),
        'fresh_paid_bit_write':(10,40,10,0,True,84,2),
        'publish_current_reason':(10,40,10,0,True,60,2),
        'paid_command_import':(8,40,10,0,True,58,2),
        'final_ri_write':(0,50,0,0,True,50,2)}
    stages={}
    for event,values in expected.items():
        state=[x['state'] for x in row['runtime_trace'] if x['event']==event][-1]
        got=reduced(state)
        assert tuple(got[k] for k in ('fuel','patient','source','q','qualified','energy','new_next'))==values,event
        assert got['old_context'] is False and got['old_next']==3 and got['reader']==0
        if got['new_next']==2:assert got['new_cells']==[1,0,1,1]
        if event=='paid_command_import':assert state['latch'] is None and state['imported']['command']==0
        if event=='final_ri_write':assert state['latch'] is None and state['imported'] is None
        stages[event]=got
    locked=r['cases']['locked_qualification']['producers']['variable']['paths'][index]
    locked_after_queries=[x['state'] for x in locked['runtime_trace'] if x['event']=='probe1_ri_write'][-1]
    lc=reduced(locked_after_queries)
    assert (lc['fuel'],lc['patient'],lc['source'],lc['q'],lc['qualified'])==(10,30,10,2,True)
    assert locked['state']['parent']['parent']['producer']['core']['fuel']==9
    # The formal locked theorem stops after probes. The numerical full control
    # subsequently pays an unsupported command-read1, hence ends at9, not10.
    fx=json.loads((HERE/'fixtures.json').read_text())['preparations']['primary']
    assert fx['trace'][58]['plant']==[20,21,1,1,1,196,170]
    assert fx['construction_spent']==65 and fx['trace'][-1]['parent_fuel']==119
    assert fx['trace'][-1]['parent_source']==140
    result=dict(scope='Frozen concrete-theorem constants versus actual saved same-orientation runtime; no transition rerun or new compiler validation.',
        formal_source_sha256=FORMAL_HASHES,model_sha256=sha(HERE/'model.py'),
        compressed_results_sha256=hashlib.sha256(packed).hexdigest(),checker_sha256=sha(Path(__file__)),
        path=dict(case='primary',producer='variable',index=index),stages=stages,
        locked_after_queries=lc,locked_complete_actor=9,all_assertions_passed=True)
    (HERE/'formal-runtime-crosscheck.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Passed matching orientation at path',index,'and paid locked-control probe boundary.')


if __name__=='__main__':main()
