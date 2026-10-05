"""Finite purpose-adoption ballot; normative concerns and constitution are supplied.

Inputs are delayed observable summaries and paid exploratory pilot records.
No world/phase labels or true risks are accepted. This is a fallible governance
choice, not a statistical guarantee or final acceptance of the candidate rule.
"""
from dataclasses import asdict, dataclass
from typing import Mapping


@dataclass(frozen=True)
class Ballot:
    actor: str
    yes: bool
    observed_utility_change: float
    reason: str


def petition_eligibility(service: Mapping[str, Mapping[str, float]]) -> bool:
    a, b = service['A'], service['B']
    return (a['n'] >= 16 and b['n'] >= 16
            and b['error'] >= .25
            and b['error'] - a['error'] >= .125)


def hearing_decision(*, service, pilot, extra_round_cost, cash_after_hearing,
                     next_required_payment, reserve_floor, usable_checker,
                     current_mandate='A_ONLY'):
    """Paid pilot completed. Return a prospective mandate decision plus audit data.

    pilot={'incumbent':{'A':rate,'B':rate}, 'edited':{'A':rate,'B':rate}}.
    The cost is the entire institution's incremental cost per two-group round.
    Each constituency values half of that cost; steward values total cost.
    Cooldown/pending-petition control and actual payments belong to the caller.
    """
    if extra_round_cost < 0 or next_required_payment < 0 or reserve_floor < 0:
        raise ValueError('This expansion hearing requires nonnegative prices')
    for arm in ('incumbent', 'edited'):
        for group in ('A', 'B'):
            if not 0 <= pilot[arm][group] <= 1:
                raise ValueError('Pilot errors must be rates')
    eligible = petition_eligibility(service)
    d = {g: pilot['incumbent'][g]-pilot['edited'][g] for g in ('A', 'B')}
    delta_a = d['A'] - .5*extra_round_cost
    delta_b = d['B'] - .5*extra_round_cost
    delta_s = (max(pilot['incumbent'].values())
               - max(pilot['edited'].values()) - extra_round_cost)
    liquid = cash_after_hearing >= next_required_payment+reserve_floor
    a_guard = d['A'] >= 0  # Empirical pilot guard, not proven noninferiority.
    operational = bool(usable_checker and liquid)
    votes = [
        Ballot('A delegate', delta_a > 0, delta_a,
               'own error reduction less half of institutional extra cost'),
        Ballot('B delegate', eligible and delta_b > .125, delta_b,
               'eligible grievance and own benefit exceeds fixed .125 threshold'),
        Ballot('steward', delta_s > 0 and a_guard and operational, delta_s,
               'lower worst group error after expense, empirical A guard, liquidity'),
    ]
    adopt = (current_mandate == 'A_ONLY' and eligible and operational
             and sum(v.yes for v in votes) >= 2)
    return {
        'eligible': eligible, 'liquid': liquid, 'usable_checker': usable_checker,
        'empirical_a_guard': a_guard, 'votes': [asdict(v) for v in votes],
        'adopt': adopt,
        'mandate_after': 'INCLUDE_B' if adopt else current_mandate,
        'gain_under_old_mandate': d['A']-extra_round_cost,
        'gain_under_inclusive_mandate': .5*(d['A']+d['B'])-extra_round_cost,
        'scope': 'fallible pilot-based mandate adoption; separate fresh rule check required',
    }
