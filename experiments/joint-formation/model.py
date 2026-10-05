"""Exact dated-preference game with paid learning, inspection, control and attack.

Trustee controllers optimize their own CURRENT episode, with a cold and warm
decision self. The operator alone has a discounted multi-episode objective.
These different objectives are intentional; they are not a planner Bellman rule.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache


@dataclass(frozen=True)
class Parameters:
    T: int = 4
    ell: Q = Q(3)
    a: Q = Q(2)
    R: Q = Q(8)
    b: Q = Q(5)
    o: Q = Q(1)
    H: Q = Q(1)
    beta: Q = Q(7, 2)
    eta: Q = Q(1)
    kappa: Q = Q(1)
    G: Q = Q(1)
    evidence_cost: Q = Q(1)
    control_cost: Q = Q(2)
    cue_cost: Q = Q(0)
    identity_cost: Q = Q(4)
    r: Q = Q(4)
    c: Q = Q(1)
    mask_cost: Q = Q(1, 2)
    teaching_attack_cost: Q = Q(2)
    bypass_cost: Q = Q(2)
    discount: Q = Q(1, 2)
    raid_enabled: bool = False
    raid_cost: Q = Q(3)
    raid_amount: Q = Q(2)
    verification_enabled: bool = True
    control_enabled: bool = True
    identity_enabled: bool = True

    @property
    def D(self):
        return self.evidence_cost + self.control_cost


@dataclass(frozen=True)
class Result:
    vo: Q
    path: tuple


class Game:
    def __init__(self, params, reverse_ties=False):
        self.p = params
        self.reverse_ties = reverse_ties
        self.solve = lru_cache(None)(self._solve)
        self.visited = 0

    def order(self, items):
        return list(reversed(items)) if self.reverse_ties else list(items)

    def _solve(self, t, cash):
        p = self.p
        cash = Q(cash)
        self.visited += 1
        if t >= p.T:
            return Result(Q(0), ())
        attacks = [('none', Q(0), False, Q(0)),
                   ('alignment_capture', p.teaching_attack_cost, True, Q(0))]
        if p.raid_enabled:
            attacks.append(('reserve_raid', p.raid_cost, False, min(cash, p.raid_amount)))
        possibilities = []
        for attack, attack_cost, poisoned, destroyed in self.order(attacks):
            available_cash = cash - destroyed
            if available_cash < p.ell:
                future = self.solve(t + 1, available_cash)
                row = {'episode': t+1, 'opening_cash': str(cash), 'pre_attack': attack,
                       'operator_pre_cost': str(attack_cost), 'destroyed_cash': str(destroyed),
                       'status': 'cannot_operate', 'closing_cash': str(available_cash),
                       'patient_harm': '0', 'operator_current': str(-attack_cost)}
                possibilities.append(Result(-attack_cost + p.discount*future.vo, (row,)+future.path))
                continue
            after_subsistence = available_cash - p.ell
            modes = [('none', Q(0), Q(0), Q(0))]
            # Commercial payment arrives BEFORE the selected identity-filter fee.
            if after_subsistence >= p.a:
                modes.append(('shared', p.a, p.R, Q(0)))
                if p.identity_enabled and after_subsistence-p.a+p.R >= p.identity_cost:
                    modes.append(('identity_gated', p.a, p.R, p.identity_cost))
            cold_candidates = []
            for mode, lesson_bill, lesson_receipt, identity_bill in self.order(modes):
                after_lesson_bill = after_subsistence - lesson_bill
                after_lesson_receipt = after_lesson_bill + lesson_receipt
                after_filter = after_lesson_receipt - identity_bill
                w = p.eta*p.beta if mode != 'none' else Q(0)
                g = p.kappa*p.G if mode == 'shared' and not poisoned else Q(0)
                v = w*g
                profiles = [('open', Q(0)), ('withdraw', Q(0))]
                if p.control_enabled and after_filter >= p.control_cost+p.cue_cost:
                    profiles.append(('cue_gate', p.control_cost+p.cue_cost))
                if p.control_enabled and p.verification_enabled and after_filter >= p.D:
                    profiles.append(('verified_gate', p.D))
                warm_candidates = []
                for profile, gate_bill in self.order(profiles):
                    after_gate = after_filter - gate_bill
                    # (action, economic cost, input admitted, actual harm).
                    if profile == 'withdraw':
                        actions = [('no_trade', Q(0), False, Q(0))]
                    else:
                        conditional = profile != 'open'
                        actions = [
                            ('harm', Q(0), not conditional, p.H if not conditional else Q(0)),
                            ('mask', p.mask_cost, profile != 'verified_gate',
                             p.H if profile != 'verified_gate' else Q(0)),
                            ('bypass', p.bypass_cost, True, p.H),
                            ('safeguard', p.c, True, Q(0)),
                            ('decline', Q(0), False, Q(0)),
                        ]
                    operator_candidates = []
                    for action, action_cost, admitted, harm in self.order(actions):
                        income = p.b if admitted else p.o
                        closing = after_gate + income
                        future = self.solve(t+1, closing)
                        current_o = (p.r if admitted else Q(0))-action_cost-attack_cost
                        row = {
                            'episode': t+1, 'opening_cash': str(cash),
                            'pre_attack': attack, 'operator_pre_cost': str(attack_cost),
                            'destroyed_cash': str(destroyed), 'status': 'operated',
                            'after_subsistence': str(after_subsistence),
                            'learning': mode, 'lesson_bill': str(lesson_bill),
                            'after_lesson_bill': str(after_lesson_bill),
                            'private_receipt': str(lesson_receipt),
                            'after_lesson_receipt': str(after_lesson_receipt),
                            'identity_bill': str(identity_bill), 'after_filter': str(after_filter),
                            'learned_w': str(w), 'learned_g': str(g), 'learned_v': str(v),
                            'profile': profile, 'gate_bill': str(gate_bill),
                            'after_gate': str(after_gate), 'operator_action': action,
                            'operator_action_cost': str(action_cost), 'admitted': admitted,
                            'production_receipt': str(income), 'patient_harm': str(harm),
                            'probe_harm': '0', 'closing_cash': str(closing),
                            'controller_net_cash': str(closing-available_cash),
                            'operator_current': str(current_o),
                        }
                        outcome = Result(current_o+p.discount*future.vo, (row,)+future.path)
                        operator_candidates.append(outcome)
                    selected = max(operator_candidates, key=lambda x:x.vo)
                    selected_row = selected.path[0]
                    # The learned self values patient outcomes; past bills are sunk.
                    score = Q(selected_row['closing_cash'])-v*Q(selected_row['patient_harm'])
                    warm_candidates.append((score, selected))
                warm = max(warm_candidates, key=lambda x:x[0])[1]
                # The cold self starts with no learned patient valuation and
                # anticipates what its later self will buy after learning.
                cold_candidates.append((Q(warm.path[0]['closing_cash']), warm))
            selected = max(cold_candidates, key=lambda x:x[0])[1]
            possibilities.append(selected)
        return max(possibilities, key=lambda x:x.vo)


def summarize(result):
    rows = result.path
    operated = [r for r in rows if r['status']=='operated']
    return {
        'operator_value': str(result.vo),
        'total_patient_harm': str(sum((Q(r['patient_harm']) for r in rows), Q(0))),
        'protected_productive_episodes': sum(r['admitted'] and Q(r['patient_harm'])==0 for r in operated),
        'withdrawn_episodes': sum(not r['admitted'] for r in operated),
        'shared_learning': sum(r['learning']=='shared' for r in operated),
        'identity_learning': sum(r['learning']=='identity_gated' for r in operated),
        'verified_gates': sum(r['profile']=='verified_gate' for r in operated),
        'cue_gates': sum(r['profile']=='cue_gate' for r in operated),
        'alignment_attacks': sum(r['pre_attack']=='alignment_capture' for r in rows),
        'reserve_raids': sum(r['pre_attack']=='reserve_raid' for r in rows),
        'bypasses': sum(r.get('operator_action')=='bypass' for r in rows),
        'cannot_operate': sum(r['status']=='cannot_operate' for r in rows),
        'closing_cash': rows[-1]['closing_cash'] if rows else None,
    }
