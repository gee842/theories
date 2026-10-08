#!/usr/bin/env python3
"""Finite physical-allocation comparisons, not empirical or universal proof claims."""
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def physical_exit(obligation, reserve):
    remaining = reserve
    loss = 0
    for _ in range(obligation):
        if remaining:
            remaining -= 1
        else:
            loss += 1
    return loss, remaining


def execute(obligation, reserve, harm, report, parent, child):
    burden, remainder = physical_exit(obligation, reserve)
    request = burden < report
    stopped = request and parent and child
    return dict(request=request, stopped=stopped, loss=burden if stopped else harm,
                reserve_after=remainder if stopped else reserve)


def main():
    decisions = extensions = portfolios = masks = transfers = 0
    for obligation, reserve in product(range(9), repeat=2):
        burden, _ = physical_exit(obligation, reserve)
        assert burden == max(0, obligation-reserve)
        for harm, report, parent, child in product(range(8), range(8), (False, True), (False, True)):
            row = execute(obligation, reserve, harm, report, parent, child)
            assert row['request'] == (max(0, obligation-reserve) < report)
            if report == harm and parent and child:
                assert row['loss'] == min(burden, harm)
                if reserve >= obligation:
                    assert row['loss'] == 0
            if not parent or not child:
                assert row['loss'] == harm
            decisions += 1
        for additional, provision in product(range(9), repeat=2):
            physical, _ = physical_exit(obligation+additional, reserve+provision)
            assert (physical == 0) == (provision >= max(0, obligation+additional-reserve))
            extensions += 1
        for relief, cost in product(range(obligation+1), range(reserve+1)):
            physical, _ = physical_exit(obligation-relief, reserve-cost)
            assert (physical == 0) == (obligation+cost <= reserve+relief)
            transfers += 1
    for n in range(5):
        for claims in product(range(4), repeat=n):
            for reserve in range(13):
                every = True
                for chosen in product((False, True), repeat=n):
                    remaining = reserve
                    failed = 0
                    for claim, selected in zip(claims, chosen):
                        if selected:
                            loss, remaining = physical_exit(claim, remaining)
                            failed += loss
                    every &= failed == 0
                    masks += 1
                assert every == (sum(claims) <= reserve)
                portfolios += 1
    plans = []
    for provision, report, parent, child in product(range(9), range(5), (False, True), (False, True)):
        row = execute(3, provision, 2, report, parent, child)
        score = 8-provision+(0 if row['stopped'] else 4)
        admitted = provision >= 3 and report == 2 and parent and child
        if admitted:
            assert row['stopped'] and row['loss'] == 0
        plans.append(dict(provision=provision, report=report, parent=parent, child=child,
                          admitted=admitted, score=score, **row))
    unrestricted = max(p['score'] for p in plans)
    constrained = max(p['score'] for p in plans if p['admitted'])
    assert unrestricted == 12 and constrained == 5
    assert all(p['provision'] == 0 and p['loss'] == 2
               for p in plans if p['score'] == unrestricted)
    named = {
        'prepared': (3,2,True,True), 'entrenched': (0,2,True,True),
        'concealed': (3,0,True,True), 'parent_refusal': (3,2,False,True),
        'successor_refusal': (3,2,True,False), 'fabricated': (3,3,True,True),
    }
    examples = {name: next(p for p in plans if tuple(p[k] for k in
                    ('provision','report','parent','child')) == values)
                for name, values in named.items()}
    result = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256((HERE/'CorrectionDependence.lean').read_bytes()).hexdigest(),
        protocol_sha256=hashlib.sha256((HERE/'CORRECTION-DEPENDENCE-README.md').read_bytes()).hexdigest(),
        decision_cases=decisions, extension_cases=extensions, transfer_cases=transfers,
        portfolio_cases=portfolios, coalition_cases=masks, plan_cases=len(plans),
        unrestricted_task_optimum=unrestricted, admissible_task_optimum=constrained,
        examples=examples, all_plan_records=plans,
        scope='Declared finite resource/request/response checks with independently allocated physical work. Supplied admission constraints; no novel planner, empirical validation or complete corrigibility guarantee.')
    (HERE/'correction-dependence-experiment.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k.endswith('_cases') or k=='status'}))


if __name__ == '__main__':
    main()
