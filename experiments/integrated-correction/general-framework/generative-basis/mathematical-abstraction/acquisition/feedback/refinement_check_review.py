"""Independent finite reconstruction: no producer or legacy-module imports.

Checks the small material preparation, selected predecessor path, archived
acquisition event correspondence, and every declared refinement continuation.
This is not a broad legacy sweep or a physical realization test.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
PARENT = HERE.parent
H = dict(alphabet=['a'],outputs=[1,1,0],transitions=[[1],[2],[0]],initial=0)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def serial(x):
    if isinstance(x,F):
        return str(x)
    if isinstance(x,dict):
        return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [serial(v) for v in x]
    return x


def preparation():
    """Independently enumerate only the original material-two entrance law."""
    seen = set()

    @lru_cache(None)
    def finish(s):
        seen.add(s)
        a,h,resident,intact,local,common,source = s
        available = 2-a-h-int(resident != 0)
        links = []

        def add(rate,**changes):
            if rate:
                vals = dict(a=a,h=h,resident=resident,intact=intact,local=local,common=common,source=source)
                vals.update(changes)
                links.append((tuple(vals.values()),F(rate)))

        rate = (1-intact)*available*common
        add(rate,a=a+1,common=common-1)
        add(rate,h=h+1,common=common-1)
        if not resident:
            add(a*common,a=a-1,resident=1,common=common-1)
            add(h*common,h=h-1,resident=2,common=common-1)
        if resident == 1 and not intact:
            add(common,intact=1,common=common-1)
        if intact and not local:
            add(source,local=1,source=source-1)
        if resident == 1:
            add(available*local,a=a+1,local=0)
        if resident == 2:
            add(available*local,h=h+1,local=0)
        if not links:
            return {s:F(1)}
        total = sum(rate for _,rate in links)
        endings = defaultdict(F)
        for t,rate in links:
            for end,mass in finish(t).items():
                endings[end] += rate/total*mass
        return dict(endings)

    endings = finish((0,0,0,0,0,24,121))
    assert sum(endings.values()) == 1
    eligible = [(s,p) for s,p in endings.items()
                if s[0]+int(s[2]==1) == s[1]+int(s[2]==2) == 1
                and s[3] == s[4] == 1 and s[5] >= 1]
    assert eligible == [((0,1,1,1,1,20,120),F(2,9))]
    state,mass = eligible[0]
    record = dict(state=list(state),probability=str(mass),commissioned=True,
                  preparation_spent=145-sum(state[4:]),remaining_energy=sum(state[4:]),
                  reserve=state[5]-1+state[4],packets=state[6]//10,remainder=state[6]%10,
                  transformed_A=1,transformed_H=1,backing_slots=2)
    return record,dict(states=len(seen),terminal_states=len(endings),commissioning_probability=str(mass))


def predecessor(cut,prepared):
    state = dict(fuel=20,gate=-1,gate_life=0,stage=0,life=0,q=2,last=0,
                 written=False,prelearn=False,stale=-1,corrected=False,witness=False)
    total_spent = total_waste = 0
    probability = F(prepared['probability'])/2
    path = []
    for t in range(cut):
        before_fuel = state['fuel']
        spent,waste,branch = 0,0,F(1)
        if not state['gate_life']:
            assert t == 0 and state['fuel'] >= 2
            state.update(fuel=state['fuel']-2,gate=1,gate_life=2)
            spent += 2
            branch *= F(1,2)
        if not state['life'] and state['stage'] != 1:
            assert t == 0 and state['fuel'] >= 1
            state.update(fuel=state['fuel']-1,stage=1,q=2,last=1)
            spent += 1
            branch *= F(1,2)
        if state['stage'] == 1:
            assert state['fuel'] >= 3
            state.update(fuel=state['fuel']-3,stage=2,life=6,q=2)
            spent += 3
        assert state['fuel'] >= 5
        state['fuel'] -= 1
        spent += 1
        action = int(state['q'] > 2) if state['q'] != 2 else state['last']
        success = action == int(t < 6)
        label = action if success else 1-action
        newq = 4*label
        after = t >= 6
        prelearn = state['prelearn'] or (not after and success and state['written'] and state['q'] != 2)
        stale = state['stale']
        if after and not success and state['prelearn'] and stale == -1:
            stale = action
        corrected = state['corrected'] or (after and newq != state['q'] and stale >= 0
                                            and (int(state['q']>2) if state['q']!=2 else action) == stale
                                            and (int(newq>2) if newq!=2 else action) != stale)
        witness = state['witness'] or (after and success and state['corrected'] and stale >= 0 and action != stale)
        state.update(fuel=state['fuel']-4+8*int(success),q=newq,last=action,
                     gate_life=2 if success else state['gate_life']-1,
                     life=6 if success else state['life']-1,written=True,
                     prelearn=bool(prelearn),stale=stale,corrected=bool(corrected),witness=bool(witness))
        spent += 4+2*int(success)
        waste = 10*int(not success)
        assert before_fuel+10 == state['fuel']+spent+waste
        total_spent += spent
        total_waste += waste
        probability *= branch
        path.append(dict(exposure=t+1,state=state.copy(),probability=str(branch)))
    source = 120-10*cut
    assert 145 == 4+1+total_spent+total_waste+state['fuel']+source
    assert state['witness'] and state['stage'] == 2 and state['q'] == 0 and state['life'] == 6
    return dict(cut=cut,original_energy=145,preparation=prepared,adapter_spent=1,
                spent=total_spent,waste=total_waste,fuel=state['fuel'],source=source,
                state=state,probability=str(probability),path=path)


def check_acquisition(case,reference):
    p,ancestor = case['prefix'],case['ancestry']
    reserve,spent,live = F(ancestor['fuel']),F(0),0
    for i,event in enumerate(p['events']):
        if i < 88:
            original = reference['events'][i]
            assert {k:v for k,v in event.items() if k!='fuel'} == {k:v for k,v in original.items() if k!='fuel'}
            assert F(event['fuel']) == F(original['fuel'])+ancestor['fuel']-36
        work,following,kind = event['work'],event['live'],event['kind']
        peak = max(live,following)+event['workspace']+event['temporary']
        extra = (F(6) if kind=='installation' else F(1,4) if kind in
                 {'target_reset','target_action','endpoint_read','extraction_work'} else
                 F(following,64) if kind=='retention_epoch' else F(0))
        bill = F(work,64)+F(peak*(work+1),65536)+F(max(0,following-live),64)+extra
        assert event['peak'] == peak and event['duration'] == work+1 and peak <= 256
        assert F(event['bill']) == bill and reserve >= bill
        reserve -= bill
        spent += bill
        assert F(event['fuel']) == reserve
        live = following
        if i == 87:
            assert p['acquisition_end'] == dict(fuel=str(reserve),spent=str(spent),event_count=88,live=15)
    expected_word = '' if p['first_policy']=='shortest' else 'aaaaaa'
    expected_tail = ([('generate_plan',1,1,0),('simulate_candidate',1,2,0),
                      ('target_reset',0,0,2),('extraction_work',0,0,2)]
                     if not expected_word else
                     [(e['kind'],e['work'],e['temporary'],e['workspace']) for e in reference['events'][88:]])
    assert [(e['kind'],e['work'],e['temporary'],e['workspace']) for e in p['events'][88:]] == expected_tail
    assert p['queries'] == [[v['word'],v['output']] for v in reference['queries']]
    for word,reading in p['queries']:
        assert H['outputs'][len(word)%3] == reading
    assert p['certified'] and p['retained'] and p['model'] == H
    assert p['initial_fuel'] == ancestor['fuel'] and p['initial_source'] == ancestor['source']
    assert p['spent'] == str(spent) and p['fuel'] == str(reserve)
    bit = case['parameters']['readiness'][len(expected_word)%3]
    assert p['effect'] == dict(word=expected_word,success=bool(bit),transferred=10*bit,
                               wasted=10*(1-bit),source=ancestor['source']-10,
                               fuel_after_return=str(reserve+10*bit))
    return len(p['events'])


class Denied(Exception):
    pass


def continuation(case):
    par,prefix = case['parameters'],case['prefix']
    word = prefix['effect']['word']
    start = reserve = F(prefix['effect']['fuel_after_return'])
    spent = income = F(0)
    live = peak_seen = 15
    workspace = len(word)+2
    source = prefix['effect']['source']
    physical_phase = len(word)%3
    readiness = par['readiness'][:]
    wasted = 0
    partition,records = [],[]
    installed = pending = retained = False
    valid = True
    uses,receipt_count = 1,0
    events,effects,history,denials = [],[],[],[]
    status,audit,selected = 'complete',None,None

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

    def native(word,first=False):
        nonlocal source,physical_phase,wasted,income,reserve,uses,readiness,receipt_count
        if first:
            bit = int(prefix['effect']['success'])
        else:
            uses += 1
            if par['change_before_third'] and uses == 3:
                readiness = [0,0,1]
                effects.append(dict(kind='readiness_change',readiness=readiness[:]))
            if source<10:
                denials.append(dict(reason='source_unavailable',available=source,required=10))
                raise Denied('source_unavailable')
            charge('native_reset',temporary=2,extra=F(1,4))
            physical_phase = 0
            for _ in word:
                charge('native_action',temporary=2,extra=F(1,4))
                physical_phase = (physical_phase+1)%3
            charge('native_extraction',temporary=2,extra=F(1,4))
            source -= 10
            bit = readiness[physical_phase]
            if bit:
                income += 10
                reserve += 10
                events.append(dict(kind='actual_arrival',amount=10,fuel=str(reserve)))
            else:
                wasted += 10
            effects.append(dict(kind='effect',word=word,state=physical_phase,arrived=bit,source=source))
        charge('consequence_contact',temporary=2,extra=F(1,4))
        if first and par['lost_first']:
            raise Denied('receipt_unavailable')
        receipt_count += 1
        observed = bit ^ int(receipt_count == par['flip_at'])
        effects.append(dict(kind='receipt',actual=bit,observed=observed))
        return observed

    def acquire(word,first=False):
        nonlocal partition,records,pending,valid
        charge('bind_phase_word',work=len(word)+1,temporary=2)
        q = len(word)%3
        if par['misbind_second'] and len(records)==1:
            q = records[0][0]
        observed = native(word,first)
        next_records = records+[[q,observed]]
        charge('retain_phase_outcome',work=2,next_live=26+2*len(next_records),temporary=2,rewrites=1)
        records = next_records
        pending = True
        history.append(dict(kind='record',word=word,phase=q,observed=observed))
        count = len(records)
        charge('compare_application_evidence',work=3+count*count,temporary=3+2*count)
        if any(q==p and b!=c for q,b in records for p,c in records):
            charge('reject_phase_conflict',work=1,rewrites=2)
            valid,pending = False,False
            history.append(dict(kind='phase_conflict',partition=partition[:]))
            raise Denied('inconsistent_phase_evidence')
        conflicted = sorted({partition[q] for q,b in records for p,c in records
                             if partition[q]==partition[p] and b!=c})
        if conflicted:
            before,following = partition[:],partition[:]
            label = max(before)+1
            for old in conflicted:
                members = [q for q in range(3) if before[q]==old]
                for q in members[1:]:
                    following[q] = label
                    label += 1
            charge('split_application_class',work=3+count,temporary=3,rewrites=4)
            assert all(following[q]!=following[p] for q in range(3) for p in range(3) if before[q]!=before[p])
            assert any(before[q]==before[p] and following[q]!=following[p] for q in range(3) for p in range(3))
            assert all(following[q]!=following[p] for q,b in records for p,c in records if b!=c)
            partition,pending = following,False
            history.append(dict(kind='partition_refinement',before=before,after=partition[:],records=[r[:] for r in records]))
        else:
            charge('accept_application_partition',work=1,rewrites=1)
            pending = False

    try:
        charge('refinement_installation',work=8,next_live=23,temporary=8,extra=F(1))
        charge('form_application_partition',work=3,next_live=26,temporary=3)
        partition = [0,1,2] if par['static_phase'] else [1,1,0]
        installed = True
        history.append(dict(kind='initial_partition',partition=partition[:]))
        acquire(word,True)
        workspace = 0
        charge('select_same_output_audit',work=18,temporary=9)
        first_phase = records[0][0]
        audit = next((w for w in ('','a','aa') if len(w)%3!=first_phase and
                      H['outputs'][len(w)%3]==H['outputs'][first_phase]),None)
        if audit is not None:
            workspace = len(audit)+2
            acquire(audit)
            workspace = 0
        if pending or not valid:
            raise Denied('application_not_ready')
        charge('consume_application_partition',work=3*len(records)+6,temporary=3+2*len(records))
        view = [1,1,0] if par['mask_consumer'] else partition[:]
        eligible = []
        for q in range(3):
            observations = [b for p,b in records if view[p]==view[q]]
            if observations and all(observations):
                eligible.append(q)
        selected = next((w for w in ('','a','aa') if len(w)%3 in eligible),None)
        history.append(dict(kind='application_read',partition=partition[:],read_view=view,
                            records=[r[:] for r in records],eligible=eligible,selected=selected))
        if selected is None:
            status = 'no_supported_response'
        else:
            workspace = len(selected)+2
            acquire(selected)
            workspace = 0
    except Denied as error:
        status = str(error)
    workspace = 0
    retention_status = 'not_committed'
    try:
        if installed and not pending:
            charge('refinement_retention',work=1,extra=F(live,64))
            retained,retention_status = True,'retained'
    except Denied as error:
        retention_status = str(error)
    final = dict(fuel=reserve,source=source,extension_spent=spent,extension_income=income,
                 extension_wasted=wasted,partition=partition,records=records,valid=valid,
                 pending=pending,installed=installed,retained=retained,
                 retention_status=retention_status,live=live,peak=peak_seen,workspace=workspace)
    for key,value in dict(account_start=start,status=status,audit_word=audit,selected_use=selected,
                           history=history,effects=effects,events=events,final=final).items():
        assert case[key] == serial(value),(case['name'],key)
    assert case['model_before'] == case['model_after'] == H
    anc = case['ancestry']
    total = 4+1+anc['spent']+anc['waste']+F(prefix['spent'])+prefix['effect']['wasted']+spent+reserve+source+wasted
    assert total == 145 and case['whole_account'] == [145,'145']
    return dict(name=case['name'],status=status,extension_events=len(events),
                actual_extractions=1+sum(e['kind']=='effect' for e in effects),
                selected_use=selected,partition=partition,valid=valid,retained=retained,
                source=source,fuel=str(reserve),denials=denials)


def main():
    data = json.loads((HERE/'refinement-results.json').read_text())
    old = json.loads((PARENT/'results.json').read_text())
    bindings = {}
    for root,table in ((ROOT,data['source_hashes']),
                       (PARENT,old['source_hashes']),(ROOT,old['inherited']['source_hashes'])):
        for relative,expected in table.items():
            path = root/relative
            assert digest(path) == expected,relative
            bindings[str(path.relative_to(ROOT))] = expected
    prepared,preparation_summary = preparation()
    assert prepared == old['inherited']['preparation_record']
    ancestors = {cut:predecessor(cut,prepared) for cut in (8,9,10)}
    assert all(ancestors[cut]['path']==old['inherited']['path'][:cut] for cut in ancestors)
    cases = data['cases']
    assert len(cases)==16
    rows = []
    for case in cases:
        assert case['ancestry'] == ancestors[case['parameters']['cut']]
        count = check_acquisition(case,old['cases']['inverted_sensor'])
        row = continuation(case)
        row['acquisition_and_first_use_events'] = count
        rows.append(row)
    by = {c['name']:c for c in cases}
    ordinary,masked = by['acquired_refinement'],by['consumer_masked']
    assert ordinary['ancestry']==masked['ancestry'] and ordinary['prefix']==masked['prefix']
    # Same record, split and every extension event through the costed consumer.
    end = next(i for i,e in enumerate(ordinary['events']) if e['kind']=='consume_application_partition')+1
    assert ordinary['events'][:end] == masked['events'][:end]
    assert ordinary['history'][:4] == masked['history'][:4]
    assert ordinary['selected_use']=='a' and masked['selected_use'] is None
    assert ordinary['final']['source']==0 and masked['final']['source']==10
    static = by['static_phase']
    assert all((ordinary['final']['partition'][p]==ordinary['final']['partition'][q]) ==
               (static['final']['partition'][p]==static['final']['partition'][q]) for p in range(3) for q in range(3))
    assert static['effects'] == ordinary['effects']
    assert F(static['final']['extension_spent']) < F(ordinary['final']['extension_spent'])
    novel = by['original_ten_novel']['prefix']
    assert novel['events'] == old['cases']['inverted_sensor']['events']
    assert novel['effect'] == old['cases']['inverted_sensor']['use']
    assert by['unobserved_phase_also_ready']['history'] == ordinary['history']
    assert by['unobserved_phase_also_ready']['effects'] == ordinary['effects']
    assert by['original_readiness']['history'] == by['blocked']['history']
    assert by['false_positive_second']['status']=='funding:native_extraction'
    assert by['false_positive_second']['final']['source']==10
    # Complete finite partition check, independent of the implemented split.
    # Canonical restricted-growth labels enumerate each partition exactly once.
    partitions = [list(p) for p in product(range(3),repeat=3)
                  if p[0]==0 and all(p[i]<=max(p[:i])+1 for i in (1,2))]
    old_partition = [1,1,0]
    observed = [[0,0],[1,1]]
    fitting = [p for p in partitions if all(p[q]!=p[r] or b==c
                                            for q,b in observed for r,c in observed)]
    refining = [p for p in partitions if all(p[q]!=p[r]
                  for q in range(3) for r in range(3) if old_partition[q]!=old_partition[r])]
    admissible = [p for p in refining if p in fitting]
    assert len(partitions)==5 and len(fitting)==3 and len(refining)==2
    assert admissible == [[0,1,2]]
    partition_check = dict(domain=[0,1,2],old_partition=old_partition,records=observed,
                           partitions=partitions,fitting_records=fitting,
                           refining_old_partition=refining,admissible=admissible,
                           scope='Unique partition up to relabeling only under this fixed three-state deterministic record-fitting refinement contract')
    report = dict(status='passed',scope='Independent source-bound finite reconstruction; no producer imports or broad legacy rerun',
                  check_source_sha256=digest(Path(__file__)),results_sha256=digest(HERE/'refinement-results.json'),
                  source_bindings=bindings,unique_source_bindings=len(bindings),
                  preparation=preparation_summary,ancestry_cuts=[8,9,10],ancestry_transitions=sum(anc['cut'] for anc in ancestors.values()),
                  case_count=len(rows),extension_events=sum(r['extension_events'] for r in rows),
                  acquisition_and_first_use_events=sum(r['acquisition_and_first_use_events'] for r in rows),
                  matched_consumer_prefix_events=end,cases=rows,
                  finite_partition_characterization=partition_check,
                  limitations=['Reviewer advised design; computational reconstruction is independent code.',
                               'Archived acquisition schedule is source-bound and independently costed, not relearned by a separate learner.',
                               'Native information access was inspected, not proved by a verified noninterference system.',
                               'Conditional finite construction is not empirical validation or assumption-free grounding.'])
    (HERE/'refinement-independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','case_count','unique_source_bindings','preparation','ancestry_transitions','extension_events','acquisition_and_first_use_events','matched_consumer_prefix_events')},indent=2))


if __name__ == '__main__':
    main()
