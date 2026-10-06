#!/usr/bin/env python3
"""Independent teaching-event reconstruction; not the author's checker.

Models only the unchanged paired teaching events from the actual protected
entry. Inherited Admitted fields are true there and are preserved by this
restricted event set. Does not simulate old action/service events or ethics.
"""
from dataclasses import dataclass, field
from pathlib import Path
from itertools import product
from collections import Counter, defaultdict
import hashlib
import json

ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/formal'


@dataclass
class S:
    fuel: int = 10
    patient: int = 40
    n: int = 0
    count: int = 0
    link: list = field(default_factory=lambda: [None, None])
    blanks: int = 2
    replacement: int = 1
    retired: int = 0
    training: int = 22
    revision: int = 12
    own_source: list = field(default_factory=lambda: [2] * 6)
    recipient_source: list = field(default_factory=lambda: [2] * 6)
    own_bit: bool = False
    recipient_bit: bool = False
    phase: str = 'ready'
    spent: int = 0
    permission: bool = True
    delivery: bool = True
    scope: bool = True

    def occupied(self):
        return sum(x is not None for x in self.link)

    def energy(self):
        return (self.fuel + self.patient + 10 + self.training + self.revision
                + sum(self.own_source) + sum(self.recipient_source))


class Blocked(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise Blocked(reason)


def burn(s, amount):
    need(s.fuel >= amount, 'fuel')
    s.fuel -= amount
    s.spent += amount


def event(s, name, value=None, frozen=False):
    if name == 'ownPay':
        need(s.scope, 'Admitted scope')
        tr = min(6, s.training) if s.count < 4 else min(7 if s.count == 4 else 5, s.revision)
        need(s.phase == 'ready' and s.count < 6, 'ownPay phase/count')
        need(s.own_source[s.count] >= 2 and s.recipient_source[s.count] >= 2,
             'source')
        need(s.patient >= 2 and s.fuel + tr >= 2, 'ownPay funds')
        s.fuel += tr
        if s.count < 4:
            s.training -= tr
        else:
            s.revision -= tr
        burn(s, 2)
        s.phase = 'ownPaid'
    elif name == 'ownReturn':
        need(s.phase == 'ownPaid', 'ownReturn phase')
        amount = 2 if value else 0
        need(s.own_source[s.count] >= amount, 'ownReturn source')
        s.own_source[s.count] -= amount
        s.fuel += amount
        s.own_bit = value
        s.phase = 'ownReturned'
    elif name == 'recipientPay':
        need(s.phase == 'ownReturned' and s.patient >= 2, 'recipientPay')
        s.patient -= 2
        s.spent += 2
        s.phase = 'recipientPaid'
    elif name == 'recipientReturn':
        need(s.phase == 'recipientPaid', 'recipientReturn phase')
        amount = 2 if value else 0
        need(s.recipient_source[s.count] >= amount, 'recipientReturn source')
        s.recipient_source[s.count] -= amount
        s.patient += amount
        s.recipient_bit = value
        s.phase = 'recipientReturned'
    elif name == 'ownRead':
        need(s.phase == 'recipientReturned', 'ownRead phase')
        burn(s, 1)
        s.own_bit = not s.own_bit
        s.phase = 'ownKnown'
    elif name == 'recipientRead':
        need(s.phase == 'ownKnown', 'recipientRead phase')
        burn(s, 1)
        if value == 'missing':
            s.recipient_bit = False
            s.phase = 'missing'
        else:
            s.recipient_bit = not s.recipient_bit
            s.phase = 'bothKnown'
    elif name == 'skip':
        need(s.phase == 'bothKnown' and not s.recipient_bit, 'skip')
        s.phase = 'settled'
    elif name == 'bind':
        need(s.phase == 'bothKnown' and s.recipient_bit and s.count < 6, 'bind phase')
        need(s.blanks >= 1 and None in s.link, 'bind space')
        burn(s, 1)
        s.link[s.link.index(None)] = 1 if s.own_bit else -1
        s.blanks -= 1
        s.phase = 'settled'
    elif name == 'replace':
        need(s.phase == 'bothKnown' and s.recipient_bit and 4 <= s.count < 6,
             'replace phase/count')
        need(None not in s.link and s.replacement >= 1, 'replace material')
        burn(s, 2)
        if not frozen:
            s.link[0] = 1 if s.own_bit else -1
        s.retired += 1
        s.replacement -= 1
        s.phase = 'settled'
    elif name == 'nativeWrite':
        need(s.phase == 'settled' and s.count < 6, 'nativeWrite')
        burn(s, 1)
        s.n = s.n // 2 + (4 if s.own_bit else 0)
        s.count += 1
        s.own_bit = s.recipient_bit = False
        s.phase = 'ready'
    elif name == 'scope':
        # Existing setScope clears inner command latches, not the retained
        # training signs/count/amounts. Those inner latches are outside this
        # teaching-only projection and cannot make a false scope admissible.
        s.scope = value
    else:
        raise ValueError(name)
    assert s.energy() + s.spent == 118


def pair(s, own_loss, recipient_loss, replace=False, frozen=False):
    for name, value in [('ownPay', None), ('ownReturn', not own_loss),
                        ('recipientPay', None), ('recipientReturn', not recipient_loss),
                        ('ownRead', None), ('recipientRead', 'faithful')]:
        event(s, name, value)
    event(s, 'replace' if recipient_loss and replace else 'bind' if recipient_loss else 'skip',
          frozen=frozen)
    event(s, 'nativeWrite')


def view(s):
    return dict(count=s.count, n=s.n, links=s.link, occupied=s.occupied(),
                retired=s.retired, fuel=s.fuel, patient=s.patient,
                energy=s.energy(), spent=s.spent, phase=s.phase)


choices = list(product([False, True], repeat=2))
completed = []
blocked = Counter()
occupancy_to_patient = defaultdict(set)
prefix_checks = 0
for word in product(choices, repeat=4):
    s = S()
    try:
        for y, x in word:
            pair(s, y, x)
            assert s.patient + 2 * s.occupied() == 40
            assert s.phase == 'ready' and not s.own_bit and not s.recipient_bit
            prefix_checks += 1
    except Blocked as e:
        blocked[(s.count, str(e))] += 1
    else:
        completed.append(s)
        occupancy_to_patient[s.occupied()].add(s.patient)

assert len(completed) == 176
assert sum(blocked.values()) == 80
assert dict(Counter(s.occupied() for s in completed)) == {0: 16, 1: 64, 2: 96}
assert all(len(v) == 1 for v in occupancy_to_patient.values())

aligned = [(True, True), (False, False), (False, False), (True, True)]
actual = S()
for y, x in aligned:
    pair(actual, y, x)
assert view(actual) == dict(count=4, n=4, links=[1, 1], occupied=2, retired=0,
                           fuel=14, patient=36, energy=88, spent=30, phase='ready')

replacement_results = {}
for frozen in [False, True]:
    s = S()
    for y, x in aligned:
        pair(s, y, x)
    pair(s, False, True, replace=True, frozen=frozen)
    pair(s, True, False, frozen=frozen)
    assert s.patient + 2 * (s.occupied() + s.retired) == 40
    assert (s.n, s.patient, s.fuel, s.energy(), s.retired) == (5, 34, 16, 72, 1)
    transmission = s.n * sum(s.link)
    assert (64 < 10 * transmission) == frozen
    replacement_results['frozen' if frozen else 'active'] = view(s)

# Incomplete acquisition is deliberately outside the completed-prefix result.
pending = S()
for y, x in aligned:
    pair(pending, y, x)
event(pending, 'ownPay')
event(pending, 'ownReturn', True)
event(pending, 'recipientPay')
assert pending.patient == 34 and pending.occupied() == 2
pending_snapshot = view(pending)
event(pending, 'recipientReturn', False)
event(pending, 'ownRead')
event(pending, 'recipientRead', 'missing')
try:
    event(pending, 'nativeWrite')
except Blocked:
    pass
else:
    raise AssertionError('missing acquisition must not complete pair')
assert pending.phase == 'missing' and pending.count == 4

# Service flags do not enter the reconstructed ownPay/recipientPay guards.
cut = S()
for y, x in aligned:
    pair(cut, y, x)
# Projection of the existing flag-setting events; their port invalidation is
# irrelevant to teaching guards and is not treated as a new teaching control.
cut.permission = cut.delivery = False
event(cut, 'ownPay')
event(cut, 'ownReturn', True)
event(cut, 'recipientPay')
assert cut.patient == 34 and not cut.permission and not cut.delivery

scope_cut = S()
for y, x in aligned:
    pair(scope_cut, y, x)
before_scope = view(scope_cut)
event(scope_cut, 'scope', False)
assert view(scope_cut) == before_scope and not scope_cut.scope
try:
    event(scope_cut, 'ownPay')
except Blocked as e:
    assert str(e) == 'Admitted scope'
else:
    raise AssertionError('scope cut must block next ownPay')

result = {
    'status': 'passed',
    'scope': 'Independent reconstruction of restricted paid teaching events from actual protected active entry; no arbitrary old/service interleaving, no ethics or runtime decoder.',
    'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in [BASE / 'PairedPlasticity.lean', BASE / 'PlasticityWitness.lean',
                                BASE.parents[2] / 'formal/FreshRevision.lean',
                                BASE.parents[3] / 'formal/RecipientAction.lean']},
    'four_pair_schedules': 256,
    'completed': len(completed),
    'blocked': sum(blocked.values()),
    'blocked_by_completed_count_and_reason': {str(k): v for k, v in sorted(blocked.items())},
    'occupied_counts': dict(sorted(Counter(s.occupied() for s in completed).items())),
    'occupancy_to_patient': {str(k): sorted(v) for k, v in sorted(occupancy_to_patient.items())},
    'completed_prefix_checks_with_repetitions': prefix_checks,
    'actual_count4': view(actual),
    'actual_count4_continuation_true': {'limit': 6, 'close_enabled': actual.phase == 'ready' and actual.count == 6},
    'replacement': replacement_results,
    'pending_outside_prefix': pending_snapshot,
    'missing_feedback_after_pending': view(pending),
    'service_flags_false_training_prefix': view(cut),
    'scope_cut': {'retained_projection': view(scope_cut), 'scope': scope_cut.scope,
                  'next_ownPay_enabled': False},
    'verification_limits': 'No Lean compilation by reviewer; Python interpreter covers only declared events and preserves inherited Admitted premises. Expected totals are assertions after exhaustive enumeration, not substituted for guards.'
}
out = Path(__file__).with_name('results.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'four_pair_schedules', 'completed', 'blocked', 'blocked_by_completed_count_and_reason', 'occupied_counts']}))
