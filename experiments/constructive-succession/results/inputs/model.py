"""Paid finite circuit synthesis through actual serialized handoffs.

Truth tables have eight rows. This is computation in a supplied Boolean
language, not noisy empirical learning or invention of an action ontology.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement
import random

MASK = 255
INPUTS = (170, 204, 240)
MAX_GATES = 32
BASE_SERVICE = 16
TARGET_COST = 8
TRIAL_COST = 9  # one construction operation and eight evaluation rows
VERIFY_COST = 8
MAX_EXTRA_ROOTS = 16


class Arena:
    def __init__(self, nodes=None):
        self.nodes = list(nodes) if nodes is not None else [None, None, None]

    def closure(self, roots):
        found = set()
        stack = list(roots)
        while stack:
            i = stack.pop()
            if i in found:
                continue
            found.add(i)
            if i >= 3:
                stack.extend(self.nodes[i])
        return found

    def gates(self, root):
        return len(self.closure([root]) - {0, 1, 2})

    def evaluate(self, root):
        """Independent interpreter, used for billed checks or audit only."""
        cache = dict(enumerate(INPUTS))
        def visit(i):
            if i not in cache:
                a, b = self.nodes[i]
                cache[i] = ~(visit(a) & visit(b)) & MASK
            return cache[i]
        return visit(root)


@dataclass
class State:
    package: dict
    bank: int


def primitive_state(bank=1000):
    return State({'nodes': [None, None, None], 'installed': 0,
                  'evidence': {}, 'extra_roots': []}, bank)


def choose_roots(arena, values, order, installed, target, policy):
    base = arena.closure([installed]) | {0, 1, 2}
    base_values = {values[i] for i in base}
    candidates = [i for i in order if i not in base and values[i] not in base_values]
    if policy == 'solution':
        return []
    if policy == 'closest':
        return sorted(candidates, key=lambda i: ((values[i] ^ target).bit_count(), i))
    if policy == 'recent':
        return list(reversed(candidates))
    if policy in ('diverse', 'diverse_recompute'):
        selected = []
        reference = set(base_values)
        while candidates:
            i = min(candidates, key=lambda j: (
                -min((values[j] ^ v).bit_count() for v in reference), j))
            selected.append(i)
            reference.add(values[i])
            candidates.remove(i)
        return selected
    raise ValueError(policy)


def handoff(arena, values, order, installed, target, bank, policy, archive_price):
    """No next target is accepted by this interface.

    The successful source is always inspectable. Its transitive circuit and
    cached computation cost two units per gate to transfer. Additional source
    costs archive_price per gate plus one per cached table. Extra spending is
    capped at half the work left after the successful source is paid for.
    """
    base = arena.closure([installed]) | {0, 1, 2}
    base_gates = base - {0, 1, 2}
    mandatory = 2 * len(base_gates)
    assert bank >= mandatory
    allowed_extra = (bank - mandatory) // 2
    kept = set(base)
    roots = []
    source_only = policy == 'diverse_recompute'
    for root in choose_roots(arena, values, order, installed, target, policy):
        expanded = kept | arena.closure([root])
        extra_count = len(expanded - base)
        cost = extra_count * (archive_price + (0 if source_only else 1))
        if cost <= allowed_extra:
            kept = expanded
            roots.append(root)
        if len(roots) >= MAX_EXTRA_ROOTS:
            break
    extra_nodes = kept - base
    extra_cost = len(extra_nodes) * (archive_price + (0 if source_only else 1))
    ids = sorted(kept)
    remap = {old: new for new, old in enumerate(ids)}
    nodes = [None if i < 3 else tuple(remap[j] for j in arena.nodes[i]) for i in ids]
    evidence = {remap[i]: values[i] for i in kept if i >= 3
                and (not source_only or i in base)}
    package = {'nodes': nodes, 'installed': remap[installed], 'evidence': evidence,
               'extra_roots': [remap[i] for i in roots]}
    return State(package, bank - mandatory - extra_cost), {
        'solution_transfer': mandatory, 'extra_transfer': extra_cost,
        'extra_roots': len(roots), 'extra_nodes': len(extra_nodes),
        'delivered_nodes': len(ids) - 3,
    }


def episode(state, target, flow, policy, archive_price, reserve_quarters=0):
    assert 0 <= target <= MASK
    arena = Arena(state.package['nodes'])
    installed = state.package['installed']
    values = dict(enumerate(INPUTS))
    # Only actually delivered tables are available to this new learner.
    values.update({int(i): v for i, v in state.package['evidence'].items()})
    opening = state.bank
    bank = opening + flow
    costs = {'service': BASE_SERVICE, 'target': TARGET_COST,
             'recompute': 0, 'search': 0, 'validation': 0, 'installation': 0}
    bank -= BASE_SERVICE + TARGET_COST
    old_transfer = 2 * arena.gates(installed)
    assert bank >= old_transfer
    search_floor = old_transfer + (bank - old_transfer) * reserve_quarters // 4
    # Same recovery route in every arm. Uncached source remains usable.
    for i in range(3, len(arena.nodes)):
        if target in values.values():
            break
        if i not in values and bank - 8 >= search_floor:
            values[i] = arena.evaluate(i)
            bank -= 8
            costs['recompute'] += 8
    by_value = {}
    order = []
    for i in sorted(values):
        if values[i] not in by_value:
            by_value[values[i]] = i
            order.append(i)
    inherited_values = set(by_value)
    inherited_target = target in inherited_values
    inherited_solution_values = {values[i] for i in arena.closure([installed])} | set(INPUTS)
    solution_target = target in inherited_solution_values
    attempts = 0
    new_functions = 0
    found_unaffordable = False
    solved = False
    new_composition = False

    def try_install(root, newly_constructed):
        nonlocal installed, bank, solved, new_composition, found_unaffordable
        gates = arena.gates(root)
        # Physical incumbent may continue unchanged; a changed program must
        # pay independent exhaustive verification, installation, and handoff.
        installation = 0 if root == installed else gates
        validation = 0 if root == installed else VERIFY_COST
        if bank >= validation + installation + 2 * gates:
            if validation:
                assert arena.evaluate(root) == target
            bank -= validation + installation
            costs['validation'] += validation
            costs['installation'] += installation
            installed = root
            solved = True
            new_composition = newly_constructed
        else:
            found_unaffordable = True

    if inherited_target:
        try_install(by_value[target], False)
    pairs = list(combinations_with_replacement(range(len(order)), 2))
    cursor = 0
    while not solved and cursor < len(pairs) and bank >= TRIAL_COST + search_floor:
        a_idx, b_idx = pairs[cursor]
        cursor += 1
        a, b = order[a_idx], order[b_idx]
        # Shape and size are inspectable before evaluating a candidate.
        if len((arena.closure([a, b]) - {0, 1, 2})) + 1 > MAX_GATES:
            continue
        bank -= TRIAL_COST
        costs['search'] += TRIAL_COST
        attempts += 1
        result = ~(values[a] & values[b]) & MASK
        if result in by_value:
            continue
        root = len(arena.nodes)
        arena.nodes.append((a, b))
        values[root] = result
        by_value[result] = root
        index = len(order)
        order.append(root)
        pairs.extend((j, index) for j in range(index + 1))
        new_functions += 1
        if result == target:
            try_install(root, True)
    next_state, transfer = handoff(arena, values, order, installed, target,
                                    bank, policy, archive_price)
    costs['solution_transfer'] = transfer['solution_transfer']
    costs['extra_transfer'] = transfer['extra_transfer']
    assert opening + flow - sum(costs.values()) == next_state.bank
    assert next_state.bank >= 0
    assert not solved or arena.evaluate(installed) == target
    return next_state, {
        'target': target, 'solved': solved, 'new_composition': new_composition,
        'inherited_target': inherited_target, 'solution_target': solution_target,
        'found_unaffordable': found_unaffordable, 'attempts': attempts,
        'new_functions': new_functions, 'opening_bank': opening, 'flow': flow,
        'closing_bank': next_state.bank, 'costs': costs, **transfer,
        'installed_gates': arena.gates(installed),
        'reserve_quarters': reserve_quarters, 'search_floor': search_floor,
    }


def tasks(seed, regime, count=4):
    rng = random.Random(seed)
    target = INPUTS[0] ^ INPUTS[1]
    out = []
    for _ in range(count):
        if regime == 'repeat':
            pass
        elif regime == 'local':
            target ^= 1 << rng.randrange(8)
        elif regime == 'independent':
            target = rng.randrange(256)
        else:
            raise ValueError(regime)
        out.append(target)
    return out


def run(seed, regime, policy, archive_price, flow, count=4, reserve_quarters=0):
    target = INPUTS[0] ^ INPUTS[1]
    state, bootstrap = episode(primitive_state(), target, 0, policy, archive_price)
    assert bootstrap['solved']
    records = []
    # Task sequence is accessed only after each predecessor's package is fixed.
    for target in tasks(seed, regime, count):
        state, record = episode(state, target, flow, policy, archive_price, reserve_quarters)
        records.append(record)
    return {'seed': seed, 'regime': regime, 'policy': policy,
            'archive_price': archive_price, 'flow': flow,
            'reserve_quarters': reserve_quarters,
            'bootstrap': bootstrap, 'episodes': records,
            'final_bank': state.bank, 'final_package': state.package}
