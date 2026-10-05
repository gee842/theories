#!/usr/bin/env python3
"""Exact paired-component replacement check; Python standard library only.

The small plant is deterministic conditional on a hidden fixed binary fault.
Controllers have perfect recall. No operating output replenishes repair cash.
Run from any directory; writes modular-replacement-results.json beside this file.
"""
from dataclasses import asdict, dataclass, replace
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


PROVIDERS = ('original', 'recoded', 'redacted')
ACTIONS = ('inspect', 'fresh', 'authorize', 'apply0', 'apply1', 'wait')


@dataclass(frozen=True, order=True)
class State:
    theta: int
    time: int
    cash: int
    permit: bool = False
    source: str = 'none'
    record: int = -1
    mode: str = 'old'


def initial(theta, cash, horizon):
    return State(theta, 0, cash, mode='old' if horizon > 0 else 'failed')


def costs(cheap=1, fresh=2, permission=1, execution=1):
    return dict(inspect=cheap, fresh=fresh, authorize=permission,
                apply0=execution, apply1=execution, wait=0, hold=0)


def output(s):
    # One service unit is supplied from a separate admitted feedstock.
    return int(s.mode != 'failed')


def observe(s, provider):
    record = s.record
    if provider == 'redacted' and s.source == 'cheap':
        record = 'redacted'
    return (s.time, s.cash, s.permit, s.source, record, s.mode, output(s))


def abstract_observation(obs, provider):
    if provider != 'recoded':
        return obs
    z = list(obs)
    if z[4] in (0, 1):
        z[4] = 1 - z[4]
    return tuple(z)


def action_adapter(action, provider):
    if provider == 'recoded' and action in ('apply0', 'apply1'):
        return 'apply' + str(1 - int(action[-1]))
    return action


def abstract_state(s, provider):
    if provider == 'recoded' and s.record >= 0:
        return replace(s, record=1 - s.record)
    return s


def step(s, action, provider, horizon, price, authorized=True):
    if s.time >= horizon:
        return None
    if s.mode != 'old':
        return replace(s, time=s.time + 1) if action == 'hold' else None
    if action == 'hold' or s.cash < price[action]:
        return None
    if authorized and action.startswith('apply') and not s.permit:
        return None
    new = replace(s, time=s.time + 1, cash=s.cash - price[action])
    if action in ('inspect', 'fresh'):
        raw = 1 - s.theta if provider == 'recoded' else s.theta
        new = replace(new, source='cheap' if action == 'inspect' else 'fresh', record=raw)
    elif action == 'authorize':
        new = replace(new, permit=True)
    elif action.startswith('apply'):
        effect = int(action[-1])
        if provider == 'recoded':
            effect = 1 - effect
        new = replace(new, mode='renewed' if effect == s.theta else 'failed')
    if new.time == horizon and new.mode == 'old':
        new = replace(new, mode='failed')
    return new


def legal_actions(s):
    return ('hold',) if s.mode != 'old' else ACTIONS


def key(states):
    return tuple(sorted(set(states)))


def make_solver(provider, horizon, price, authorized=True):
    @lru_cache(None)
    def solve(belief):
        if all(s.mode == 'renewed' for s in belief):
            return True
        if any(s.mode == 'failed' or s.time >= horizon for s in belief):
            return False
        for a in ACTIONS:
            successors = [step(s, a, provider, horizon, price, authorized) for s in belief]
            if any(s is None or s.mode == 'failed' for s in successors):
                continue
            branches = {}
            for s in successors:
                branches.setdefault(observe(s, provider), []).append(s)
            if all(solve(key(ss)) for ss in branches.values()):
                return True
        return False

    def witness(belief):
        if all(s.mode == 'renewed' for s in belief):
            return {'goal': True}
        if not solve(belief):
            return None
        for a in ACTIONS:
            successors = [step(s, a, provider, horizon, price, authorized) for s in belief]
            if any(s is None or s.mode == 'failed' for s in successors):
                continue
            branches = {}
            for s in successors:
                branches.setdefault(observe(s, provider), []).append(s)
            if all(solve(key(ss)) for ss in branches.values()):
                return {'action': a, 'branches': [
                    {'observation': obs, 'then': witness(key(ss))}
                    for obs, ss in branches.items()]}
        raise AssertionError('No witness for winning state')
    return solve, witness


def world_paths(theta, cash, provider, horizon, price):
    """Enumerate complete legal plant action words without belief recursion."""
    first = initial(theta, cash, horizon)
    paths = []
    def visit(s, history, actions, decisions):
        if s.time == horizon:
            paths.append((actions, decisions, s.mode == 'renewed'))
            return
        for a in legal_actions(s):
            ns = step(s, a, provider, horizon, price)
            if ns is None:
                continue
            next_history = history + ((a, observe(ns, provider)),)
            visit(ns, next_history, actions + (a,), decisions + ((history, a),))
    visit(first, (('initial', observe(first, provider)),), (), ())
    return paths


def exhaustive_policy_pairs(cash, provider, horizon, price):
    """Alternative exact test: pair all world action words and impose causality.

    If the two words share an observation/action history, their next actions
    must agree. This directly enforces nonanticipation on policy pairs rather
    than recursing on information sets. It shares the plant step function.
    """
    paths = [world_paths(theta, cash, provider, horizon, price) for theta in (0, 1)]
    checked = feasible = winning_pairs = 0
    best_fair_prior = 0.0
    for p0, p1 in product(*paths):
        checked += 1
        actions = dict(p0[1])
        if any(hist in actions and actions[hist] != a for hist, a in p1[1]):
            continue
        feasible += 1
        score = (int(p0[2]) + int(p1[2])) / 2
        best_fair_prior = max(best_fair_prior, score)
        winning_pairs += int(p0[2] and p1[2])
    return dict(world_path_counts=list(map(len, paths)), pairs_checked=checked,
                causal_pairs=feasible, winning_pairs=winning_pairs,
                robust=winning_pairs > 0, best_fair_prior=best_fair_prior)


def batch_without_feedback(cash, horizon, price):
    """A temporal coarse control: commit all commands before any test result."""
    paths = [world_paths(theta, cash, 'original', horizon, price) for theta in (0, 1)]
    by_actions = [{p[0]: p[2] for p in pp} for pp in paths]
    common = set(by_actions[0]) & set(by_actions[1])
    robust = any(by_actions[0][word] and by_actions[1][word] for word in common)
    fair = max((int(by_actions[0][word]) + int(by_actions[1][word])) / 2 for word in common)
    return dict(common_command_words=len(common), robust=robust, best_fair_prior=fair)


def reachable(provider, cash, horizon, price, authorized=True):
    states = {initial(theta, cash, horizon) for theta in (0, 1)}
    pending = list(states)
    edges = []
    while pending:
        s = pending.pop()
        for a in legal_actions(s):
            ns = step(s, a, provider, horizon, price, authorized)
            if ns is None:
                continue
            assert ns.cash == s.cash - price[a]
            assert ns.cash >= 0
            edges.append((s, a, ns))
            if ns not in states:
                states.add(ns)
                pending.append(ns)
    return states, edges


def main():
    price = costs()
    rows = []
    for provider, horizon in product(PROVIDERS, range(5)):
        solver, _ = make_solver(provider, horizon, price)
        for cash in range(7):
            belief = key(initial(theta, cash, horizon) for theta in (0, 1))
            result = solver(belief)
            threshold = 4 if provider == 'redacted' else 3
            assert result == (horizon >= 3 and cash >= threshold)
            full_info = all(solver((s,)) for s in belief)
            assert full_info == (horizon >= 2 and cash >= 2)
            physical_solver, _ = make_solver(provider, horizon, price, False)
            physical = all(physical_solver((s,)) for s in belief)
            assert physical == (horizon >= 1 and cash >= 1)
            rows.append(dict(provider=provider, horizon=horizon, cash=cash,
                             robust=result, full_information_authorized=full_info,
                             full_information_physical=physical))

    pair_checks = []
    for provider, cash in product(PROVIDERS, range(6)):
        enumeration = exhaustive_policy_pairs(cash, provider, 3, price)
        solver, _ = make_solver(provider, 3, price)
        belief = key(initial(theta, cash, 3) for theta in (0, 1))
        assert enumeration['robust'] == solver(belief)
        if provider == 'redacted' and cash == 3:
            assert enumeration['best_fair_prior'] == 0.5
        pair_checks.append(dict(provider=provider, cash=cash, **enumeration))

    graph_checks = []
    for cash, horizon, authorized in product(range(7), range(5), (False, True)):
        original_states, original_edges = reachable('original', cash, horizon, price, authorized)
        redacted_states, redacted_edges = reachable('redacted', cash, horizon, price, authorized)
        assert original_states == redacted_states
        assert set(original_edges) == set(redacted_edges)
        recoded_states, recoded_edges = reachable('recoded', cash, horizon, price, authorized)
        assert {abstract_state(s, 'recoded') for s in recoded_states} == original_states
        for s, a, ns in recoded_edges:
            abs_s, abs_ns = abstract_state(s, 'recoded'), abstract_state(ns, 'recoded')
            abs_a = action_adapter(a, 'recoded')  # This codec is involutive.
            assert step(abs_s, abs_a, 'original', horizon, price, authorized) == abs_ns
            assert observe(abs_s, 'original') == abstract_observation(observe(s, 'recoded'), 'recoded')
            assert output(s) == output(abs_s)
        mapped_edges = {(abstract_state(s, 'recoded'), action_adapter(a, 'recoded'),
                         abstract_state(ns, 'recoded')) for s, a, ns in recoded_edges}
        assert mapped_edges == set(original_edges)
        graph_checks.append(dict(cash=cash, horizon=horizon, authorized=authorized,
                                 states=len(original_states), edges=len(original_edges)))

    price_controls = []
    for cheap, fresh, perm, execution in product((1, 2), (1, 2, 3), (1, 2), (1, 2)):
        cp = costs(cheap, fresh, perm, execution)
        for provider in PROVIDERS:
            solver, _ = make_solver(provider, 3, cp)
            target = (fresh if provider == 'redacted' else min(cheap, fresh)) + perm + execution
            for cash in range(target + 2):
                belief = key(initial(theta, cash, 3) for theta in (0, 1))
                assert solver(belief) == (cash >= target)
            price_controls.append(dict(provider=provider, cheap=cheap, fresh=fresh,
                                       permission=perm, execution=execution, minimum_cash=target))

    # Integer unit rescaling: same affordability and policy structure if every
    # price and initial cash are multiplied by the same strictly positive k.
    scaling_cases = 0
    for scale, provider, cash in product((1, 2, 5), PROVIDERS, range(7)):
        scaled_price = {a: c * scale for a, c in price.items()}
        base_solver, _ = make_solver(provider, 3, price)
        scaled_solver, _ = make_solver(provider, 3, scaled_price)
        base_b = key(initial(theta, cash, 3) for theta in (0, 1))
        scaled_b = key(initial(theta, scale * cash, 3) for theta in (0, 1))
        assert base_solver(base_b) == scaled_solver(scaled_b)
        scaling_cases += 1

    witnesses = {}
    for provider, cash in (('original', 3), ('recoded', 3), ('redacted', 3), ('redacted', 4)):
        _, get_witness = make_solver(provider, 3, price)
        witnesses[f'{provider}_{cash}'] = get_witness(key(initial(theta, cash, 3) for theta in (0, 1)))
    batching = batch_without_feedback(3, 3, price)
    assert not batching['robust'] and batching['best_fair_prior'] == 0.5
    report = dict(
        status='all assertions passed',
        semantics=dict(hidden_fault='fixed binary; robust over both initial states',
                       memory='perfect recall, unpriced in this milestone',
                       installed_comparison='equal post-installation cash and same deadline',
                       operating_output='separate service signal; never credited to revision cash',
                       target='renewed, safely absorbing; failure irreversible',
                       costs=price),
        analytic_thresholds=dict(original=3, recoded=3, redacted=4,
                                 full_information_authorized=2, full_information_physical=1,
                                 robust_minimum_horizon=3),
        capacity_cases=rows,
        exhaustive_policy_pair_checks=pair_checks,
        identical_or_isomorphic_graph_checks=graph_checks,
        price_controls=price_controls,
        integer_cash_unit_rescalings_checked=scaling_cases,
        temporal_batch_without_feedback=batching,
        witnesses=witnesses,
        limits=['Finite supplied grammar and perfect diagnostics',
                'Identical plant graph omits the differing observer interface',
                'No empirical cross-domain or cross-scale validation',
                'Exhaustive pair check shares the plant step function; proof is independent',
                'Perfect-recall memory is not paid recurrent inheritance'])
    path = Path(__file__).with_name('modular-replacement-results.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(status=report['status'], capacity_cases=len(rows),
                          policy_pair_cases=len(pair_checks),
                          policy_pairs_examined=sum(r['pairs_checked'] for r in pair_checks),
                          graph_cases=len(graph_checks), price_cases=len(price_controls),
                          unit_rescaling_cases=scaling_cases, results=str(path)), indent=2))


if __name__ == '__main__':
    main()
