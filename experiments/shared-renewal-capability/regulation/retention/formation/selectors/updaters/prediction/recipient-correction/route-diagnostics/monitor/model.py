"""A finite paid monitor of an actual retained recipient-route grandchild.

The eight cells/head, calibrated contacts and finite lease are supplied recipes.
The monitor reads its own cells, not the plant's outcome/audit variable or gamma.
No route is replaced. Opaque ancestor stocks remain outside its funding account.
"""

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('_monitor_route', BASE / 'transmission/model.py')
route_model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = route_model
spec.loader.exec_module(route_model)

PRICES = dict(assembly=2, rent=1, sense=1, pre_read=1, arm=1, work=3,
              seal=1, acquire=1, write=1, post_read=1, commit=1)
STAGES = ('rent', 'sense', 'pre_read', 'arm', 'work', 'seal', 'acquire', 'write', 'post_read', 'commit')


def cases():
    base = dict(prior_control='ordinary', reverse=True, frames=2, channel=True,
                bus_contact=True, availability=[True, True], receipt_fault='none',
                cells=8, heads=1, source=20, prices=dict(PRICES), stop_before=None,
                known_break=False, implementation='ordinary', monitor=True)
    out = dict(primary=base,
        stable=dict(base, reverse=False), no_monitor=dict(base, monitor=False),
        controlled_proxy_stable=dict(base, prior_control='clamp_learning', reverse=False),
        missing_cells=dict(base, cells=7), missing_head=dict(base, heads=0),
        missing_packet=dict(base, source=0),
        stopped_work=dict(base, stop_before='work'), stopped_seal=dict(base, stop_before='seal'),
        missing_bus=dict(base, channel=False, bus_contact=False),
        unknown_bus=dict(base, bus_contact=None),
        false_bus_contact=dict(base, channel=False, bus_contact=True, frames=1),
        source_outage=dict(base, reverse=False, availability=[False, True]),
        stuck_receipt_one=dict(base, receipt_fault='stuck_one', frames=1),
        stuck_receipt_zero=dict(base, reverse=False, receipt_fault='stuck_zero', frames=1),
        wrong_recipient_contact=dict(base, reverse=False, receipt_fault='wrong_recipient', frames=1),
        known_binding_break=dict(base, known_break=True))
    for stage in PRICES:
        out['expensive_' + stage] = dict(base, prices=dict(PRICES, **{stage: 99}))
    return out


def admitted(entry):
    if entry['parent_kind'] != 'continuation':
        return False
    s = entry['parent_state']
    child = s['grandchild']
    return bool(s['grandchild_retained'] and child is not None and child[0] in
                ('target', 'closed', 'private_zero', 'frozen') and 0 <= child[1] < 4
                and s['grandchild_occupied'] == 1 and s['grandchild_assembled'] == 1
                and s['grandchild_stage'] == 'child_held')


def classify(success, failure, binding):
    """Only the physically backed summary cells and binding bit choose this."""
    if not binding:
        return 'unresolved'
    if 3 in (success, failure):
        return 'conflict'
    signatures = dict(target=(1, 2), private_zero=(2, 2), nonwriter=(1, 1))
    possible = [name for name, (s, f) in signatures.items()
                if success in (0, s) and failure in (0, f)]
    return possible[0] if len(possible) == 1 else ('conflict' if not possible else 'unresolved')


def update_summary(old, flip):
    value = 2 if flip else 1
    return value if old == 0 else old if old == value else 3


def ordinary_update(gamma, q, action, receipt, channel, implementation):
    if implementation == 'ordinary':
        return route_model.route_feedback(route_model.Route(gamma), q, 1, action, receipt, True, channel)[0]
    if gamma == 'closed' or (not channel and gamma != 'private_zero') or gamma == 'frozen':
        return q
    received = False if gamma == 'private_zero' else receipt
    label = action if received else 1 - action
    return q % 2 + 2 * label


def run(entry, case):
    """Execute at most two fixed frames, stopping at the first failed guard.

    Entry comes from an accepted terminal row. Its separately recovered base_law
    enters only work. A stage's fund+spend pair is guarded; no interrupted
    transfer-only histories are asserted. All unused source stays in the bank.
    """
    if case['frames'] not in (1, 2) or any(v < 0 for v in case['prices'].values()):
        raise ValueError('Finite nonnegative-price episode required')
    if min(case['cells'], case['heads'], case['source']) < 0:
        raise ValueError('Negative monitor provision')
    ok = admitted(entry)
    old = entry['parent_state']
    physical = entry['parent_kind'] == 'continuation'
    child = old['grandchild'] if physical else None
    recipient = old['recipient'] if physical else 0
    cash = old['grandchild_fuel'] if physical else 0
    s = dict(original_actor=old['original_actor'] if physical else None,
             older_learner_cash=old['learner_fuel'] if physical else None,
             recipient=recipient, child_cash=cash,
             untouched_energy=entry['inherited_energy'] - recipient - cash,
             gamma=child[0] if child else None, q=child[1] if child else None,
             carrier_active=ok, monitor_installed=False,
             free_cells=case['cells'], bound_cells=0, free_heads=case['heads'], bound_heads=0,
             new_source=case['source'], spent=0, lost=0, transferred=0,
             pre=0, receipt=0, post=0, success_summary=0, failure_summary=0, binding=False,
             armed=False, work_done=False, sealed=False, bus_valid=None, write_done=False,
             pre_read_done=False, post_read_done=False, target_report=None,
             issued=None, candidate=None, route_receipt=False,
             frame=-1, stage='initial', diagnosis='unresolved')
    metrics = dict(admitted=int(ok), assembled=0, frames_started=0, work_events=0,
                   captures=0, commits=0, publications=0, payment_prefix_checks=0)
    trace = []
    initial_total = entry['inherited_energy'] + case['source']
    qlow = child[1] % 2 if child else None

    def audit():
        assert s['untouched_energy'] + s['recipient'] + s['child_cash'] + s['new_source'] + s['spent'] + s['lost'] == initial_total
        assert s['recipient'] >= min(recipient, 1)
        assert min(s[k] for k in ('recipient', 'child_cash', 'new_source', 'spent', 'lost')) >= 0
        assert s['free_cells'] + s['bound_cells'] == case['cells']
        assert s['free_heads'] + s['bound_heads'] == case['heads']
        assert s['bound_cells'] == 8 * int(s['monitor_installed'])
        assert s['bound_heads'] == int(s['monitor_installed'])
        if s['q'] is not None:
            assert 0 <= s['q'] < 4 and s['q'] % 2 == qlow
        assert all(s[k] in (0, 1) for k in ('pre', 'receipt', 'post'))
        assert s['success_summary'] in range(4) and s['failure_summary'] in range(4)

    def snapshot(stage):
        s['stage'] = stage
        audit()
        trace.append(deepcopy(s))

    def finish(stage):
        snapshot(stage)
        final = dict(metrics, spent=s['spent'], lost=s['lost'], transferred=s['transferred'],
                     source_remaining=s['new_source'], final_recipient=s['recipient'],
                     final_child=s['child_cash'], diagnosis=s['diagnosis'])
        return dict(state=s, trace=trace, metrics=final)

    def pay(stage):
        fee = case['prices'][stage]
        missing = max(0, fee - s['child_cash'])
        if s['recipient'] < 1 + missing:
            return False
        s['recipient'] -= missing
        s['child_cash'] += missing
        s['transferred'] += missing
        audit()
        metrics['payment_prefix_checks'] += 1
        s['child_cash'] -= fee
        s['spent'] += fee
        audit()
        metrics['payment_prefix_checks'] += 1
        return True

    def recipient_credit(amount):
        # This single physical transition effects the actual credit and both
        # ordinary-bus/independent-contact pulses. No later capture audit is read.
        s['recipient'] += amount
        s['route_receipt'] = True
        if s['armed'] and s['binding'] and case['receipt_fault'] not in ('stuck_zero', 'wrong_recipient'):
            s['receipt'] = 1
        metrics['captures'] += 1

    snapshot('initial')
    if not ok:
        return finish('unadmitted')
    if entry['base_law'] not in (0, 1):
        raise ValueError('Admitted plant requires its recovered inherited target law')
    if case['monitor']:
        if s['free_cells'] < 8 or s['free_heads'] < 1:
            return finish('blocked_assembly_parts')
        if not pay('assembly'):
            return finish('blocked_assembly_funds')
        s.update(free_cells=s['free_cells'] - 8, bound_cells=8,
                 free_heads=s['free_heads'] - 1, bound_heads=1,
                 monitor_installed=True, binding=True)
        metrics['assembled'] = 1
        snapshot('assembled')
    world = entry['base_law'] ^ int(case['reverse'])
    for frame in range(case['frames']):
        s.update(frame=frame, armed=False, work_done=False, sealed=False, bus_valid=None,
                 write_done=False, pre_read_done=False, post_read_done=False,
                 target_report=None, issued=None, candidate=None, route_receipt=False)
        metrics['frames_started'] += 1
        snapshot('frame_started')
        program = STAGES if case['monitor'] else ('rent', 'sense', 'work', 'acquire', 'write')
        for stage in program:
            if case['stop_before'] == stage:
                return finish('stopped_before_' + stage)
            if stage == 'work' and s['new_source'] < 10:
                return finish('blocked_work_packet')
            if stage == 'commit' and not (s['binding'] and s['sealed'] and s['write_done']
                                         and s['post_read_done'] and s['bus_valid'] is True):
                return finish('blocked_commit_evidence')
            if not pay(stage):
                if stage == 'rent':
                    s['carrier_active'] = False
                return finish('blocked_' + stage + '_funds')
            if stage == 'sense':
                s['target_report'] = 1
            elif stage == 'pre_read':
                s['pre'] = route_model.issue(s['q'], s['target_report'])
                s['pre_read_done'] = True
            elif stage == 'arm':
                s['receipt'] = int(case['receipt_fault'] == 'stuck_one')
                s['armed'] = True
            elif stage == 'work':
                action = ((0, 0, 1, 1)[s['q']] if case['implementation'] == 'conventional'
                          else route_model.issue(s['q'], s['target_report']))
                s['issued'] = action
                s['new_source'] -= 10
                if action == world and case['availability'][frame]:
                    recipient_credit(10)
                else:
                    s['lost'] += 10
                s['work_done'] = True
                metrics['work_events'] += 1
            elif stage == 'seal':
                assert s['armed'] and s['work_done']
                s.update(armed=False, sealed=True, bus_valid=case['bus_contact'])
            elif stage == 'acquire':
                s['candidate'] = ordinary_update(s['gamma'], s['q'], s['issued'],
                    s['route_receipt'], case['channel'], case['implementation'])
            elif stage == 'write':
                s['q'] = s['candidate']
                s['write_done'] = True
            elif stage == 'post_read':
                s['post'] = route_model.issue(s['q'], s['target_report'])
                s['post_read_done'] = True
            elif stage == 'commit':
                field = 'success_summary' if s['receipt'] else 'failure_summary'
                s[field] = update_summary(s[field], s['post'] != s['pre'])
                s['diagnosis'] = classify(s['success_summary'], s['failure_summary'], s['binding'])
                metrics['commits'] += 1
                metrics['publications'] += int(s['diagnosis'] in ('target', 'private_zero', 'nonwriter'))
            snapshot(stage)
        if case['known_break'] and frame == 0:
            s.update(binding=False, success_summary=0, failure_summary=0, diagnosis='unresolved', armed=False)
            return finish('known_binding_break')
    return finish('episode_complete')
