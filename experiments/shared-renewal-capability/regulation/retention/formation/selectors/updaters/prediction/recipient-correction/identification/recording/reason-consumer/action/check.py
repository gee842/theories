"""Producer checks; independent event-law reconstruction is check_model.py."""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import json
import gzip
import hashlib
import model as m

HERE=Path(__file__).resolve().parent


def main():
    m.verify_freezes();before=m.sources()
    fx=json.loads((HERE/'fixtures.json').read_text())
    raw=gzip.decompress((HERE/'results.json.gz').read_bytes())
    files=json.loads((HERE/'result-files.json').read_text())
    assert m.digest(HERE/'results.json.gz')==files['compressed_sha256']
    assert hashlib.sha256(raw).hexdigest()==files['uncompressed_sha256']
    result=json.loads(raw)
    assert m.object_hash(result['cases'])==files['semantic_cases_sha256']
    assert fx['source_sha256']==result['source_sha256']==before
    histories=events=0
    for name,case in m.cases().items():
        arm=result['cases'][name]
        assert arm['law']==case
        for producer in m.PRODUCERS:
            rows=arm['producers'][producer]['paths']
            assert sum(Q(r['probability']) for r in rows)==1
            for row in rows:
                histories+=1
                first=row['runtime_trace'][0]['state'];last=row['state']
                op=first['parent']['producer'];np=last['parent']['producer']
                assert row['runtime_trace'][-1]['state']==last
                for event in row['runtime_trace']:
                    events+=1;s=event['state'];p=s['parent']['producer'];c=p['core']
                    assert m.retained(s)+m.inherited_spending(s)+sum(s[k] for k in
                        ('binding_spent','action_spent','action_waste'))==s['initial_extension_total']
                    for field in ('cells','frames','query_pointer','pending','archive_escrow',
                                  'archive_fuel','core_spent','core_waste','archive_spent'):
                        assert p[field]==op[field],(name,event['event'],field)
                    assert c['q']&1==op['core']['q']&1
                    assert c['recipient']>=op['core']['recipient']
                    assert 'recipient_law' not in s and 'strict_parent' not in s
                assert np['core']['fuel']==op['core']['fuel']+first['command_reserve']-last['binding_spent']-last['action_spent']-(np['core']['escrow']-op['core']['escrow'])
                assert np['core']['recipient']-op['core']['recipient']==10*last['captured']
                if last['completed']:assert last['action_spent']==8 and np['core']['escrow']==0
                assert last['saved_assembly']==int(not case['port'] and not case['old_endpoint'])
    def strict(name):
        return [r for r in result['cases'][name]['producers']['variable']['paths'] if r['observer']['strict_parent']]
    def endpoint(name):
        rows=strict(name);assert rows
        return [r['state'] for r in rows]
    orientations=set()
    for r in strict('primary'):
        s=r['state'];p=s['parent']['producer'];orientations.add(r['observer']['recipient_law'])
        assert (p['core']['fuel'],p['core']['recipient'],p['core']['source'],p['reader_fuel'])==(0,30,0,0)
        assert s['binding_spent']==2 and s['action_spent']==8 and s['captured']
        assert p['decode_spent']==42 and s['parent']['reason_spent']==30
        assert m.retained(s)==30
        assert 309==50+78+54+15+72+10+30
    assert orientations=={0,1}
    for s in endpoint('no_later'):
        assert m.retained(s)==30 and s['parent']['producer']['decode_spent']==28
        assert 285==50+78+54+15+48+10+30
    for s in endpoint('command_short'):
        assert s['action_waste']==10 and s['action_spent']==0
        assert s['parent']['producer']['core']['fuel']==7
    for name,remainder in (('source_none',0),('source_partial',9)):
        for s in endpoint(name):
            assert not s['attempted'] and s['source_reserve']==remainder
            assert s['action_waste']==0 and s['binding_spent']==2
    for name in ('no_command_pair','no_extension'):
        for s in endpoint(name):assert s['binding_spent']==s['action_spent']==0 and not s['attempted']
    for name in ('no_opportunity','inverted_import','parent_consistently_corrupt'):
        for s in endpoint(name):
            assert s['completed'] and not s['captured'] and s['action_waste']==10
            assert s['parent']['producer']['core']['last']==1
    for name in ('permission_lost','delivery_lost','parent_changed_context','parent_remove_both_grounds','parent_same_context_reopen'):
        for s in endpoint(name):assert not s['attempted'] and s['parent']['producer']['core']['source']==10
    for name,case in m.cases().items():
        if case['intervention'] and case['intervention'].split(':')[1] in ('after_read','after_import'):
            for s in endpoint(name):assert not s['attempted'] and s['action_waste']==0
    for s in endpoint('scope_loss_after_rent'):
        assert s['action_spent']==1 and s['parent']['producer']['core_phase']=='rented'
        assert s['parent']['producer']['core']['source']==10
    for name in ('scope_loss_after_work','scope_loss_after_acquire'):
        for s in endpoint(name):
            assert s['completed'] and s['captured'] and s['action_spent']==8
            assert s['parent']['producer']['core']['escrow']==0
    for name in ('learned_register','unaudited_voluntary','unaudited_then_first_replay'):
        for s in endpoint(name):assert s['captured'] and s['binding_spent']==0 and not s['port']
    for s in endpoint('unaudited_voluntary'):
        assert not m.reason.current(s['parent']) and s['parent']['publication'] is None
        assert s['parent']['reason_spent']==0 and s['parent']['producer']['decode_spent']==14
        assert s['parent']['extra_reserve']==28 and s['parent']['producer']['reader_fuel']==6
        assert m.retained(s)==67
    for s in endpoint('unaudited_then_first_replay'):
        assert s['parent']['reason_spent']==10 and s['parent']['producer']['decode_spent']==28
        assert s['parent']['extra_reserve']==28 and s['parent']['producer']['reader_fuel']==6
    for s in endpoint('later_changed_context'):
        assert s['captured'] and m.reason.current(s['parent'])
        assert s['parent']['publication']['mask']==[True,False,False]
    # Conventional finite dispatch shares tariff/apparatus, not a second solver.
    for producer in m.PRODUCERS:
        a=result['cases']['primary']['producers'][producer]
        b=result['cases']['conventional_command']['producers'][producer]
        assert a['metrics']==b['metrics']
        for x,y in zip(a['paths'],b['paths']):
            xx,yy=deepcopy(x['state']),deepcopy(y['state'])
            xx['mode']=yy['mode']='same'
            assert xx==yy
    m.verify_freezes();assert m.sources()==before
    report=dict(status='passed',cases=len(m.cases()),histories=histories,runtime_snapshots=events,
        strict_orientations=sorted(orientations),source_sha256=before,
        checker_sha256=m.digest(__file__),data_sha256={n:m.digest(HERE/n) for n in ('fixtures.json','results.json.gz','result-files.json')},
        uncompressed_results_sha256=files['uncompressed_sha256'],
        scope='Producer invariants and actual failed/successful physical prefixes; independent oracle is separate.')
    (HERE/'check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','cases','histories','runtime_snapshots')}))


if __name__=='__main__':main()
