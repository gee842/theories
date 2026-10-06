"""Independent inquiry-controller reconstruction; no producer imports.

Reuses the separately authored, source-bound preparation/ancestry/acquisition
checker. Only this file implements the expected inquiry continuation.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import refinement_check_review as prior

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
PARENT = HERE.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def compatible(table):
    return [list(bits) for bits in product((0,1),repeat=3)
            if all(value is None or bits[q]==value for q,value in enumerate(table))]


class Denied(Exception):
    pass


def reconstruct(case):
    params,prefix = case['parameters'],case['prefix']
    first_word = prefix['effect']['word']
    reserve = start = F(prefix['effect']['fuel_after_return'])
    spent = income = F(0)
    live = peak_seen = 15
    workspace = len(first_word)+2
    source = prefix['effect']['source']
    phase = len(first_word)%3
    wasted = receipts = 0
    events,effects,history,denials = [],[],[],[]
    table = []
    installed = retained = False
    status = 'not_started'

    def charge(kind,work=0,next_live=None,temporary=0,extra=F(0),rewrites=0):
        nonlocal reserve,spent,live,peak_seen
        following = live if next_live is None else next_live
        peak = max(live,following)+workspace+temporary
        bill = F(work,64)+F(peak*(work+1),65536)+F(max(0,following-live)+rewrites,64)+extra
        if peak>256 or reserve<bill:
            reason = ('capacity:' if peak>256 else 'funding:')+kind
            denials.append(dict(reason=reason,available=str(reserve),required=str(bill),peak=peak))
            raise Denied(reason)
        reserve -= bill
        spent += bill
        live,peak_seen = following,max(peak_seen,peak)
        events.append(dict(kind=kind,work=work,live=live,temporary=temporary,
                           workspace=workspace,peak=peak,rewrites=rewrites,
                           extra=str(extra),bill=str(bill),fuel=str(reserve)))
        assert reserve+spent == start+income

    def native(word,first):
        nonlocal source,phase,wasted,income,reserve,receipts
        if first:
            actual = int(prefix['effect']['success'])
        else:
            if source<10:
                denials.append(dict(reason='source_unavailable',available=source,required=10))
                raise Denied('source_unavailable')
            charge('native_reset',temporary=2,extra=F(1,4))
            phase = 0
            for _ in word:
                charge('native_action',temporary=2,extra=F(1,4))
                phase = (phase+1)%3
            charge('native_extraction',temporary=2,extra=F(1,4))
            source -= 10
            actual = params['readiness'][phase]
            if actual:
                income += 10
                reserve += 10
                events.append(dict(kind='actual_arrival',amount=10,fuel=str(reserve)))
            else:
                wasted += 10
            effects.append(dict(kind='effect',word=word,state=phase,arrived=actual,source=source))
        charge('consequence_contact',temporary=2,extra=F(1,4))
        if first and params['lost_first']:
            raise Denied('receipt_unavailable')
        receipts += 1
        bit = actual ^ int(receipts==params['flip_at'])
        effects.append(dict(kind='receipt',actual=actual,observed=bit))
        return bit

    def acquire(word,first=False):
        charge('bind_phase_word',work=len(word)+1,temporary=2)
        q = len(word)%3
        assert table[q] is None
        bit = native(word,first)
        charge('write_outcome_slot',work=1,temporary=2,rewrites=1)
        table[q] = bit
        history.append(dict(kind='record',word=word,phase=q,observed=bit,table=table[:]))

    try:
        charge('inquiry_installation',work=8,next_live=23,temporary=8,extra=F(1))
        charge('form_outcome_table',work=3,next_live=26,temporary=3)
        table = [None,None,None]
        installed = True
        acquire(first_word,True)
        workspace = 0
        while True:
            charge('read_episode_completion',work=3,temporary=1)
            reported = 1 in table
            stop = reported and not params['disconnect_completion']
            history.append(dict(kind='completion_read',table=table[:],reported=reported,stop=stop))
            if stop:
                status = 'reported_episode_complete'
                break
            charge('begin_inquiry_search',work=1,temporary=2)
            selected = None
            for depth in range(3):
                charge('inspect_inquiry_slot',work=1,temporary=depth+2)
                if table[depth] is None:
                    selected = ['a']*depth
                    history.append(dict(kind='selected_inquiry',phase=depth,word=selected))
                    break
                if depth<2:
                    charge('extend_inquiry_word',work=depth+3,temporary=depth+3)
            if selected is None:
                status = 'all_phase_outcomes_recorded'
                break
            workspace = len(selected)+2
            acquire(selected)
            workspace = 0
    except Denied as error:
        status = str(error)
    workspace = 0
    retention_status = 'not_committed'
    try:
        if installed:
            charge('inquiry_retention',work=1,extra=F(live,64))
            retained,retention_status = True,'retained'
    except Denied as error:
        retention_status = str(error)
    fulfilled = bool(prefix['effect']['success'] or income)
    final = dict(fuel=reserve,source=source,extension_spent=spent,extension_income=income,
                 extension_wasted=wasted,table=table,installed=installed,retained=retained,
                 retention_status=retention_status,live=live,peak=peak_seen,workspace=0,
                 actual_episode_fulfilled=fulfilled)
    for key,value in dict(account_start=start,status=status,history=history,effects=effects,
                           events=events,final=final).items():
        assert case[key] == prior.serial(value),(case['name'],key)
    assert case['model_before'] == case['model_after'] == prior.H
    anc = case['ancestry']
    total = 4+1+anc['spent']+anc['waste']+F(prefix['spent'])+prefix['effect']['wasted']+spent+reserve+source+wasted
    assert total==145 and case['whole_account']==[145,'145']
    table_family = compatible(table) if installed else None
    if installed:
        assert len(table_family)==2**table.count(None)
        if params['flip_at'] is None:
            assert params['readiness'] in table_family
        for entry in history:
            if entry['kind']=='record':
                assert len(compatible(entry['table']))==2**entry['table'].count(None)
    return dict(name=case['name'],status=status,extension_events=len(events),
                table=table,compatible_with_table_alone=table_family,
                reported_positive=1 in table,actual_episode_fulfilled=fulfilled,
                actual_extractions=1+sum(e['kind']=='effect' for e in effects),
                source=source,final_fuel=str(reserve),retained=retained,denials=denials)


def main():
    data = json.loads((HERE/'inquiry-results.json').read_text())
    saved = json.loads((PARENT/'results.json').read_text())
    bindings = {}
    for origin,items in ((ROOT,data['source_hashes']),
                         (PARENT,saved['source_hashes']),(ROOT,saved['inherited']['source_hashes'])):
        for relative,expected in items.items():
            path = origin/relative
            assert digest(path)==expected,relative
            bindings[str(path.relative_to(ROOT))]=expected
    helper = HERE/'refinement_check_review.py'
    assert digest(helper)=='456b2aec248f1a36eab3845eff18903b1f7a3789b927918924950127a6411202'
    bindings[str(helper.relative_to(ROOT))]=digest(helper)
    prepared,preparation = prior.preparation()
    assert prepared==saved['inherited']['preparation_record']
    ancestors = {cut:prior.predecessor(cut,prepared) for cut in (8,9,10)}
    assert all(ancestors[cut]['path']==saved['inherited']['path'][:cut] for cut in ancestors)
    assert len(data['cases'])==15
    rows=[]
    for case in data['cases']:
        assert case['ancestry']==ancestors[case['parameters']['cut']]
        old_count=prior.check_acquisition(case,saved['cases']['inverted_sensor'])
        row=reconstruct(case)
        row['acquisition_and_first_use_events']=old_count
        rows.append(row)
    by={case['name']:case for case in data['cases']}
    pairs=[]
    for ordinary_name,masked_name in [('completion_sensitive','completion_reader_disconnected'),
                                      ('both_later_ready','both_ready_reader_disconnected')]:
        ordinary,masked=by[ordinary_name],by[masked_name]
        assert ordinary['prefix']==masked['prefix'] and ordinary['ancestry']==masked['ancestry']
        # The last ordinary event is retention. Every preceding event is the
        # shared acquired-success prefix through the second completion read.
        prefix=ordinary['events'][:-1]
        assert prefix[-1]['kind']=='read_episode_completion'
        assert prefix==masked['events'][:len(prefix)]
        assert ordinary['history'][:-1]==masked['history'][:len(ordinary['history'])-1]
        assert ordinary['history'][-1]['table']==masked['history'][len(ordinary['history'])-1]['table']
        assert ordinary['history'][-1]['stop'] and not masked['history'][len(ordinary['history'])-1]['stop']
        assert ordinary['final']['table']==[0,1,None] and ordinary['final']['source']==10
        assert masked['final']['source']==0
        pairs.append(dict(ordinary=ordinary_name,disconnected=masked_name,shared_extension_events=len(prefix)))
    assert by['blocked']['final']['table']==[0,0,None] and by['blocked']['final']['source']==0
    assert by['blocked']['status']=='funding:consequence_contact'
    assert compatible(by['blocked']['final']['table'])==[[0,0,0],[0,0,1]]
    assert by['both_ready_reader_disconnected']['final']['extension_income']=='20'
    assert by['completion_reader_disconnected']['final']['extension_wasted']==10
    for name in ('false_positive_first','false_positive_second'):
        assert by[name]['status']=='reported_episode_complete' and not by[name]['final']['actual_episode_fulfilled']
    assert by['false_negative_second']['final']['actual_episode_fulfilled']
    assert by['false_negative_second']['final']['table']==[0,0,0]
    for name in ('completion_sensitive','last_phase_ready','both_later_ready'):
        assert by[name]['final']['retained'] and by[name]['final']['actual_episode_fulfilled']
    assert by['original_ten_novel']['prefix']['events']==saved['cases']['inverted_sensor']['events']
    report=dict(status='passed',scope='Independent finite inquiry reconstruction with a bound independent ancestry helper',
                check_source_sha256=digest(Path(__file__)),results_sha256=digest(HERE/'inquiry-results.json'),
                source_bindings=bindings,unique_source_bindings=len(bindings),preparation=preparation,
                ancestry_cuts=[8,9,10],overlapping_ancestry_transition_checks=27,case_count=len(rows),
                extension_events=sum(r['extension_events'] for r in rows),
                acquisition_and_first_use_events=sum(r['acquisition_and_first_use_events'] for r in rows),
                completion_reader_pairs=pairs,cases=rows,
                limitations=['Reviewer advised design; independent controller reconstruction is not blind replication.',
                             'The reused helper reconstructs ancestry and bills against archived acquisition; no second learning implementation is claimed.',
                             'Table-compatible worlds concern the table alone, not all possible information in account or denial signals.',
                             'Fixed episode, contact, correspondence, recipe and risk remain supplied; no purpose-origin or ethical result.'])
    (HERE/'inquiry-independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','case_count','unique_source_bindings','extension_events','acquisition_and_first_use_events','completion_reader_pairs')},indent=2))


if __name__=='__main__':
    main()
