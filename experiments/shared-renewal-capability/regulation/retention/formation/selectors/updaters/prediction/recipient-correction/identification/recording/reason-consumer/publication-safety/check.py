"""Reproduce finite graphs; independent event reconstruction is separate."""
from pathlib import Path
import json
import model as m

HERE=Path(__file__).resolve().parent


def main():
    before=m.sources();saved=json.loads((HERE/'results.json').read_text())
    result=json.loads(json.dumps(m.compute()))
    assert result==saved
    assert len(saved['event_values'])==19
    summary=saved['summary']
    assert summary['actual_histories']==666 and summary['actual_seed_occurrences']==1332
    assert summary['synthetic_inputs']==768 and summary['depth_cutoff'] is None
    assert summary['actual_facts_holding_seed_occurrences']==1296
    assert summary['actual_false_facts_seed_occurrences']==36
    assert summary['states']==68536 and summary['edges']==302972
    assert summary['current_publication_states']==458 and summary['maximum_actual_publications']==2
    assert sum(len(g['seed_ids']) for g in saved['graphs'])==2100
    assert all(g['maximum_bound_slack']<=0 and g['positive_publication_cycles']==0 for g in saved['graphs'])
    # Every physical history has both exact event-state boundaries and survives
    # quotienting, including repeated histories and faults outside the kernel.
    ids={x['id']:x for x in saved['inputs']}
    for ref in saved['history_manifest']:
        a,b=(ids[i] for i in ref['seed_ids'])
        assert a['label']=='unread' and b['label']=='handoff'
        assert a['credit']==0 and b['credit'] in (10,14)
        assert a['physical']==b['physical']==ref['physical_signature']
        assert a['state']['fuel']+a['state']['reserve']==b['state']['fuel']+b['state']['reserve']+b['credit']
        assert ref['paid_reader_prefix'][0]=='reader_activate'
        assert a['state']['active']==0 and a['state']['token']==-1 and a['state']['next']==0
        assert b['state']['active']==ref['interpreted_reader_fields'][0]
        assert b['state']['token']==ref['interpreted_reader_fields'][1]
        assert b['state']['next']==ref['interpreted_reader_fields'][2]
    examples=saved['countermodels']
    withheld=examples['full_cache_completeness']['trace'][-1]
    assert withheld['spent']==10 and withheld['publishes']==1
    assert withheld['state']['pubmask']==0 and withheld['state']['cache']==[-1,0,1]
    forged=examples['fabricated_complete_cache']['trace'][-1]
    assert forged['spent']==10 and forged['publishes']==1 and forged['state']['pubmask']==2
    corrupt=examples['consistently_corrupt']['trace'][-1]
    assert corrupt['spent']==10 and corrupt['publishes']==1 and corrupt['state']['conflict']==0
    trap=examples['partial_reserve_trap']
    assert trap['state']['fuel']==3 and trap['state']['reserve']==28 and trap['state']['active']==1
    assert trap['state']['next']==2 and trap['state']['token']==trap['state']['context']
    assert trap['current_publications']==0 and trap['reachable_states']>1
    old=examples['python_scheduler_not_general_refinement']
    assert old['before']['phase']=='published' and old['after']['phase']=='published'
    assert old['after']['reason_spent']==old['before']['reason_spent']+10
    assert old['after']['decode_spent']==old['before']['decode_spent']
    assert old['unchanged_lean_activate_enabled'] is False
    # Decode quotient is exact for every possible valid reader read index and
    # archive context represented by a physical signature. These are read-law
    # comparisons, not new evidence observations.
    quotient_reads=0
    for signature in saved['physical_signatures'].values():
        decoder=tuple(tuple(v) for v in signature['decoder'])
        assert m.objsha(signature['frame'])==signature['frame_sha256']
        for context in (0,1):
            for index in range(3):
                cache=tuple(decoder[context][i] if i<index else -1 for i in range(3))
                s=m.initial(context,4,1,context,index,cache,0,1)
                t=m.advance(s,'reader_read',decoder)
                assert t.cache[index]==decoder[context][index] and t.fuel==0
                assert t.cache[:index]==s.cache[:index]
                quotient_reads+=1
    assert before==m.sources()
    report=dict(status='passed',summary=summary,exact_decoder_read_comparisons=quotient_reads,
        source_sha256=before,checker_sha256=m.sha(__file__),results_sha256=m.sha(HERE/'results.json'),
        scope='Reproduces all finite memoized graphs and stronger per-state invariants; verifies actual signature mapping, cost-count SCC audit, countermodels, and conditional quotient. Independent implementation and Lean induction are separate.')
    (HERE/'check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(status='passed',states=summary['states'],edges=summary['edges'],quotient_read_checks=quotient_reads)))


if __name__=='__main__':main()
