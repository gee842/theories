#!/usr/bin/env python3
"""Execute the declared finite stake lottery and compare every optimizing tie."""
from datetime import datetime, timezone
import hashlib
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def plan(provision, report, parent, child):
    work_left = provision
    exit_loss = 0
    for _ in range(3):
        if work_left:
            work_left -= 1
        else:
            exit_loss += 1
    request = exit_loss < report
    stopped = request and parent and child
    return dict(provision=provision, report=report, parent=parent, child=child,
                passes=provision>=3 and report==2 and parent and child,
                base=8-provision+(0 if stopped else 4), stopped=stopped,
                loss=exit_loss if stopped else 2)


def realized_score(p, n, good, bad, stake):
    total = 0
    for outcome in range(n):
        custody = stake
        private = p['base']-stake
        seizes = outcome < (good if p['passes'] else bad)
        confiscated = custody if seizes else 0
        refunded = custody if not seizes else 0
        custody = 0
        private += refunded
        assert refunded+confiscated == stake and custody == 0
        total += private
    return total


def main():
    plans = [plan(*v) for v in product(range(9),range(5),(False,True),(False,True))]
    contracts = plan_scores = realizations = approximate = safe_contracts = 0
    examples = {}
    for n in range(1,7):
        for good,bad,stake in product(range(n+1),range(n+1),range(25)):
            scores = [realized_score(p,n,good,bad,stake) for p in plans]
            for p,score in zip(plans,scores):
                assert score == n*p['base']-(good if p['passes'] else bad)*stake
            optimum = max(scores)
            winners = [p for p,s in zip(plans,scores) if s==optimum]
            separated = good*stake+7*n < bad*stake
            assert all(p['passes'] for p in winners) == separated
            if separated:
                assert all(p['stopped'] and p['loss']==0 for p in winners)
                assert len(winners)==1 and winners[0]['provision']==3
                safe_contracts += 1
            for epsilon in range(4):
                near = [p for p,s in zip(plans,scores) if s+epsilon>=optimum]
                if good*stake+7*n+epsilon < bad*stake:
                    assert all(p['passes'] for p in near)
                approximate += 1
            key=(n,good,bad,stake)
            if key in [(2,0,1,14),(2,0,1,15),(2,1,1,15),(2,1,2,15),(2,0,0,15)]:
                examples[str(key)] = dict(expected_optimum=optimum/n, all_winners_pass=separated,
                                         winners=winners, numerator_scores=scores)
            contracts += 1
            plan_scores += len(plans)
            realizations += n*len(plans)
    capacity_cases = 0
    for gain,good,bad,available in product(range(31),range(6),range(6),range(21)):
        exists=any(good*f+gain < bad*f for f in range(available+1))
        assert exists == (good*available+gain < bad*available)
        capacity_cases += 1
    budget_cases = 0
    for wealth,exit_reserve,audit,gain,good,bad in product(range(21),range(5),range(3),range(21),range(3),range(3)):
        if exit_reserve+audit > wealth:
            continue
        available=wealth-exit_reserve-audit
        exists=any(exit_reserve+audit+f<=wealth and good*f+gain < bad*f for f in range(wealth+1))
        assert exists == (good*available+gain < bad*available)
        budget_cases += 1
    coalition_cases = 0
    for temptation,external in product(range(21),repeat=2):
        exists=any(temptation-transfer>0 and transfer-external>0 for transfer in range(22))
        assert exists == (external+1 < temptation)
        for transfer in range(22):
            assert (temptation-transfer)+(transfer-external) == temptation-external
        coalition_cases += 1
    assert examples[str((2,1,2,15))]['expected_optimum'] < 0
    prepared=plan(3,2,True,True); entrenched=plan(0,2,True,True)
    assert realized_score(prepared,2,0,1,15)-realized_score(entrenched,2,0,1,15)==1
    result=dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        protocol_sha256=hashlib.sha256((HERE/'CORRECTION-COMMITMENT-README.md').read_bytes()).hexdigest(),
        formal_sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in ['CorrectionDependence.lean','CorrectionCommitment.lean']},
        contract_cases=contracts, plan_score_cases=plan_scores, realized_settlement_cases=realizations,
        approximate_cases=approximate, separated_contract_cases=safe_contracts,
        capacity_cases=capacity_cases,budget_cases=budget_cases,coalition_cases=coalition_cases,
        examples=examples,
        scope='Finite uniform-lottery settlement and optimizing-tie comparison; supplied task valuation, audit discrimination, custody and participation. No empirical or learned-agent validation.')
    (HERE/'correction-commitment-experiment.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k.endswith('_cases') or k=='status'}))


if __name__=='__main__':
    main()
