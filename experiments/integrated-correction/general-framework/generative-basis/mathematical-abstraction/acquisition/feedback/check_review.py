"""Independent serialized-artifact check; imports no producer or legacy model.

Reconstructs the declared finite feedback experiment and exact account using
Python's standard library. No broad legacy experiment is rerun. The reviewer
also inspected the producer's native access discipline separately.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def jsonable(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    return x


class Denied(Exception):
    pass


def independent_case(case, baseline):
    par = case['parameters']
    inverted = par['invert']
    outputs = (1, 1, 0) if inverted else (0, 0, 1)
    H = dict(alphabet=['a'], outputs=list(outputs), transitions=[[1], [2], [0]], initial=0)
    assert case['model_before'] == case['model_after'] == H
    # An independently represented actual phase advances modulo three. Its
    # transition correspondence to H is checked above, not delegated to H.
    first_word = 'aaaaaa' if inverted else 'aaaaa'
    phase = len(first_word) % 3
    first_bit = par['readiness'][phase]
    assert case['reached_phase'] == phase
    reference = baseline['inverted_sensor' if inverted else 'primary_unary']
    expected_prefix = {k: reference[k] for k in case['prefix']}
    expected_prefix['use'] = dict(word=first_word, success=bool(first_bit),
                                 transferred=10*first_bit, wasted=10*(1-first_bit),
                                 source=10, fuel_after_return=str(F(reference['fuel'])+10*first_bit))
    assert case['prefix'] == expected_prefix
    assert reference['model'] == H
    assert reference['certified'] and reference['retained']
    for query in reference['queries']:
        assert outputs[len(query['word']) % 3] == query['output']

    reserve = start = F(expected_prefix['use']['fuel_after_return'])
    spent = income = F(0)
    live = peak_seen = 15
    workspace = len(first_word)+2
    source = 10
    wasted = 0
    generated_events, effects, history = [], [], []
    width = 2 if par['family'] == 'output' else 3
    candidates, mode, record = [], 'legacy_positive', None
    retained = False
    decision = None
    status = 'complete'
    rejected = None
    base = 23

    def transaction(kind, work=0, new_live=None, temporary=0, extra=F(0), rewrites=0):
        nonlocal reserve, spent, live, peak_seen, rejected
        new_live = live if new_live is None else new_live
        peak = max(live, new_live)+workspace+temporary
        amount = (F(work,64) + F(peak*(work+1),65536)
                  + F(max(0,new_live-live)+rewrites,64) + extra)
        if peak > 256 or reserve < amount:
            status = ('capacity:' if peak > 256 else 'funding:') + kind
            rejected = dict(status=status, required=str(amount), available=str(reserve), peak=peak)
            raise Denied(status)
        reserve -= amount
        spent += amount
        live, peak_seen = new_live, max(peak_seen, peak)
        generated_events.append(dict(kind=kind, work=work, live=live,
                                     temporary=temporary, workspace=workspace,
                                     peak=peak, rewrites=rewrites, extra=str(extra),
                                     bill=str(amount), fuel=str(reserve)))
        assert reserve+spent == start+income

    def credit():
        nonlocal income, reserve
        income += 10
        reserve += 10
        generated_events.append(dict(kind='actual_arrival',amount=10,fuel=str(reserve)))

    def index(word):
        p = len(word) % 3
        return outputs[p] if width == 2 else p

    def observation(word, is_first):
        nonlocal phase, source, wasted
        if is_first:
            actual = first_bit
        else:
            if source < 10:
                raise Denied('source_unavailable')
            transaction('native_reset',temporary=2,extra=F(1,4))
            phase = 0
            for _ in word:
                transaction('native_action',temporary=2,extra=F(1,4))
                phase = (phase+1) % 3
            transaction('native_extraction',temporary=2,extra=F(1,4))
            source -= 10
            actual = par['readiness'][phase]
            if actual:
                credit()
            else:
                wasted += 10
            effects.append(dict(kind='effect',word=word,state=phase,arrived=actual,source=source))
        transaction('consequence_contact',temporary=2,extra=F(1,4))
        if is_first and par['lost_first']:
            raise Denied('receipt_unavailable')
        read = actual ^ int(is_first and par['first_flip'])
        effects.append(dict(kind='receipt',actual=actual,observed=read))
        return read

    def encounter(word, is_first=False):
        nonlocal candidates, mode, record
        transaction('bind_issued_word',work=len(word)+1,temporary=2)
        ix = index(word)
        bit = observation(word,is_first)
        transaction('retain_consequence',work=2,rewrites=2,temporary=2)
        record = [ix,bit]
        prior = candidates[:]
        survivors = [row for row in prior if row[ix] == bit]
        transaction('revise_application',work=width*len(prior)+1,
                    new_live=base+width*len(survivors),temporary=width*len(prior),
                    rewrites=width*len(survivors)+1)
        candidates = survivors
        if not par['disable_consumer']:
            mode = 'qualified'
        history.append(dict(word=word,index=ix,observed=bit,
                            before=prior,after=survivors,mode=mode))

    try:
        transaction('application_installation',work=8,new_live=base,temporary=8,extra=F(1))
        size = 2**width
        transaction('candidate_formation',work=width*size,new_live=base+width*size,
                    temporary=width*size)
        candidates = [list(row) for row in product((0,1),repeat=width)]
        encounter(first_word,True)
        workspace = 0
        words = ['', 'a', 'aa']
        transaction('select_continuation',work=sum(len(w)+1+width*len(candidates) for w in words),
                    temporary=sum(len(w)+2 for w in words))
        if mode == 'legacy_positive':
            chosen = next((w for w in words if outputs[len(w)%3] == 1), None)
            if chosen is not None:
                decision = [chosen,'legacy_reliance']
        else:
            if not candidates:
                raise Denied('application_family_inadequate')
            common = [w for w in words if all(row[index(w)] == 1 for row in candidates)]
            distinguishing = [w for w in words if len({row[index(w)] for row in candidates}) > 1]
            if common:
                decision = [common[0],'common_productive_response']
            elif distinguishing:
                decision = [distinguishing[0],'uncertain_probe']
        if decision is not None:
            workspace = len(decision[0])+2
            encounter(decision[0])
            workspace = 0
        transaction('application_retention',work=1,extra=F(live,64))
        retained = True
    except Denied as error:
        status = str(error)

    final = dict(fuel=reserve,source=source,extension_spent=spent,
                 extension_income=income,extension_wasted=wasted,live=live,
                 peak=peak_seen,workspace=workspace,candidates=candidates,
                 mode=mode,record=record,retained=retained)
    for key, expected in dict(status=status,decision=decision,history=history,
                              effects=effects,events=generated_events,
                              account_start=start,final=final).items():
        assert case[key] == jsonable(expected), (case['name'],key)
    whole = F(reference['spent'])+spent+reserve+source+10*(1-first_bit)+wasted
    assert case['whole_account'] == ['56',str(whole)] and whole == 56
    actual_map = (([par['readiness'][2],par['readiness'][0]] if inverted
                   else [par['readiness'][0],par['readiness'][2]]) if width == 2
                  else list(par['readiness']))
    in_family = (width == 3 or par['readiness'][0] == par['readiness'][1])
    if in_family and not par['first_flip']:
        assert actual_map in candidates
    return dict(name=case['name'],prefix_fields=len(expected_prefix),
                extension_events=len(generated_events),status=status,
                decision=decision,retained=retained,source=source,
                final_fuel=str(reserve),actual_relation_in_family=in_family,
                actual_relation_in_candidates=in_family and actual_map in candidates,
                denied_transaction=rejected)


def check_original_account(reference):
    reserve, prior_live, peak = F(36),0,0
    for event in reference['events']:
        kind, new_live, work = event['kind'],event['live'],event['work']
        occupancy = max(prior_live,new_live)+event['workspace']+event['temporary']
        assert event['peak'] == occupancy and event['duration'] == work+1
        extra = (F(6) if kind == 'installation' else
                 F(1,4) if kind in {'target_reset','target_action','endpoint_read','extraction_work'} else
                 F(new_live,64) if kind == 'retention_epoch' else F(0))
        amount = F(work,64)+F(occupancy*(work+1),65536)+F(max(0,new_live-prior_live),64)+extra
        assert amount == F(event['bill']) and reserve >= amount and occupancy <= 256
        reserve -= amount
        assert reserve == F(event['fuel'])
        prior_live, peak = new_live,max(peak,occupancy)
    assert reserve == F(reference['fuel'])
    assert F(36)-reserve == F(reference['spent']) and peak == reference['peak_cells']
    assert prior_live == 15
    return len(reference['events'])


def main():
    results = json.loads((HERE/'results.json').read_text())
    saved = json.loads((PARENT/'results.json').read_text())
    bindings = {}
    for origin,rows in ((PARENT,results['source_hashes']),(PARENT,saved['source_hashes'])):
        for relative,expected in rows.items():
            path = origin/relative
            assert digest(path) == expected, relative
            bindings[str(path.relative_to(PARENT))] = expected
    baseline = saved['cases']
    original_events = sum(check_original_account(baseline[key])
                          for key in ('inverted_sensor','primary_unary'))
    assert len(results['cases']) == 17
    checked = [independent_case(case,baseline) for case in results['cases']]
    by_name = {case['name']:case for case in results['cases']}
    primary,disabled = by_name['failed_use_reappraised'],by_name['consumer_disabled']
    assert primary['prefix'] == disabled['prefix']
    assert primary['history'][0]['after'] == disabled['history'][0]['after'] == [[0,0],[1,0]]
    assert primary['events'][:7] == disabled['events'][:7]
    assert primary['decision'] == ['aa','uncertain_probe'] and disabled['decision'] == ['','legacy_reliance']
    assert by_name['blocked']['effects'] == by_name['phase_dependent_outside_family']['effects']
    # Contradiction is retained, not repaired or counted as a sound model.
    assert by_name['false_first_receipt']['final']['candidates'] == []
    assert by_name['false_first_receipt']['final']['retained']
    phase = by_name['broader_phase_family']
    assert phase['status'] == 'funding:revise_application'
    assert phase['final']['record'] == [1,0] and len(phase['final']['candidates']) == 4
    assert not phase['final']['retained'] and phase['final']['source'] == 0
    phase_alternative = by_name['phase_dependent_broader_family']
    assert phase_alternative['prefix'] == by_name['phase_dependent_outside_family']['prefix']
    assert phase_alternative['decision'] == ['a','uncertain_probe']
    assert phase_alternative['final']['candidates'] == [[0,1,0],[0,1,1]]
    assert phase_alternative['final']['retained'] and phase_alternative['final']['extension_income'] == '10'
    report = dict(status='passed',scope='Independent finite reconstruction from serialized source-bound artifacts; no producer imports or broad legacy rerun',
                  check_source_sha256=digest(Path(__file__)),results_sha256=digest(HERE/'results.json'),
                  source_bindings=bindings,unique_source_bindings=len(bindings),
                  original_account_events=original_events,case_count=len(checked),
                  extension_events=sum(c['extension_events'] for c in checked),cases=checked,
                  reviewer_limitations=['Reviewer advised design before implementation.',
                                       'Source access discipline assessed by inspection; no sandbox or information-flow proof.',
                                       'Finite reconstruction does not validate physical realization or unspecified fault families.'])
    (HERE/'independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','case_count','unique_source_bindings','original_account_events','extension_events')},indent=2))


if __name__ == '__main__':
    main()
