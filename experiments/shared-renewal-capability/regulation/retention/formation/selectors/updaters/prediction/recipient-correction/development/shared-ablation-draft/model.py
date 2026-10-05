"""Paid target-specific evidence on actual formed coupling histories."""
from collections import defaultdict
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
PARENT = HERE.parent / 'coupling/model.py'
spec = importlib.util.spec_from_file_location('_recipient_coupling', PARENT)
parent = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = parent
spec.loader.exec_module(parent)
ARMS = ('shared', 'indexed', 'conventional', 'private_only', 'private_as_recipient',
        'frozen', 'shared_cheap')
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
PHASES = ('recipient', 'actor', 'recipient', 'actor')
COUNTS = ('eligible', 'setup_started', 'installed', 'rents', 'senses', 'trials',
          'recipient_trials', 'actor_trials', 'recipient_captures', 'actor_captures',
          'evidence', 'writes', 'missing_evidence', 'decoder_errors', 'unpaid_write',
          'actor_command_changed', 'spent', 'waste')


def cases():
    base = dict(initial_common=30, opposite=True, recipient_availability='1',
                channel=True, identity='correct', write=1, packet=10)
    return dict(primary=base, same_law=dict(base, opposite=False),
                recipient_outage=dict(base, recipient_availability='3/4'),
                missing_channel=dict(base, channel=False),
                target_alias=dict(base, identity='alias'),
                target_swapped=dict(base, identity='swapped'),
                low_reserve=dict(base, initial_common=12),
                expensive_write=dict(base, write=4))


def indexed(arm):
    return arm in ('indexed', 'conventional')


def read(arm, q, target):
    """Only paid target observation and actual installed payload enter policy."""
    if arm == 'conventional':
        return ((0, 0), (1, 0), (0, 1), (1, 1))[q][target]
    if indexed(arm):
        return (q >> target) & 1
    return int(q == 4)


def write(arm, q, target, bit):
    if arm == 'conventional':
        cells = list(((0, 0), (1, 0), (0, 1), (1, 1))[q])
        cells[target] = bit
        return cells[0] + 2*cells[1]
    if indexed(arm):
        return (q & ~(1 << target)) | (bit << target)
    return 4*bit


def eligible(s):
    return bool(s['stage'] == 2 and s['life'] and s['gate_life'] and
                s['coupling_life'] and s['coupling'] == 0 and s['written'] and
                s['q'] in (0, 4))


def reported(case, target):
    truth = int(target == 'recipient')
    return 0 if case['identity'] == 'alias' else truth ^ int(case['identity'] == 'swapped')


def finish(initial, case, arm, state, counts, trace):
    c = dict(counts)
    first, a1, second, a2 = trace
    correction = bool(first['action'] is not None and first['capture'] is False
                      and first['paid_write'] and first['label'] is not None
                      and first['command_after'] != first['action']
                      and second['action'] is not None and second['capture'] is True
                      and second['action'] != first['action'])
    strict = bool(correction and a1['capture'] is True and a2['capture'] is True)
    c.update(recipient_correction=int(correction), strict_witness=int(strict),
             final_actor=state['fuel'], final_recipient=state['recipient'],
             active_memory=int(state['active']))
    assert initial['fuel'] + 4*case['packet'] == sum(c[k] for k in
            ('final_actor', 'final_recipient', 'spent', 'waste'))
    assert state['fuel'] >= 0 and state['recipient'] >= 0
    if indexed(arm) and state['recoded']:
        assert 0 <= state['q'] < 4
    return state, c, trace


def suffix(case, arm, initial, actor_law):
    assert arm in ARMS
    state = dict(initial, recipient=0, active=False, installed=False, recoded=False)
    counts = dict.fromkeys(COUNTS, 0)
    counts['eligible'] = int(eligible(initial))
    if eligible(initial) and state['fuel'] >= 2:
        state['fuel'] -= 2; counts['spent'] += 2; counts['setup_started'] = 1
        recode_cost = 0 if arm == 'shared_cheap' else 2
        if state['fuel'] >= recode_cost:
            state['fuel'] -= recode_cost; counts['spent'] += recode_cost
            state['installed'] = state['active'] = True
            counts['installed'] = 1
            if indexed(arm):
                bit = int(initial['q'] == 4)
                state['q'] = bit + 2*bit
                state['recoded'] = True
    paths = [(Q(1), state, counts, [])]
    for target in PHASES:
        nxt = []
        true_law = actor_law ^ int(target == 'recipient' and case['opposite'])
        for mass, old, oldc, oldtrace in paths:
            s, c = dict(old), dict(oldc)
            event = dict(target=target, report=None, action=None, capture=None,
                         label=None, paid_write=False, command_after=None,
                         q_before=s['q'], q_after=s['q'])
            def abort():
                c['waste'] += case['packet']
                nxt.append((mass, s, c, oldtrace + [dict(event)]))
            if not s['active']:
                abort(); continue
            if s['fuel'] < 1:
                s['active'] = False
                abort(); continue
            s['fuel'] -= 1; c['spent'] += 1; c['rents'] += 1
            if s['fuel'] < 1:
                abort(); continue
            s['fuel'] -= 1; c['spent'] += 1; c['senses'] += 1
            obs_target = reported(case, target)
            event['report'] = obs_target
            if s['fuel'] < 3:
                abort(); continue
            action = read(arm, s['q'], obs_target)
            event['action'] = action
            s['fuel'] -= 3; c['spent'] += 3
            c['trials'] += 1; c[target + '_trials'] += 1
            s['last'] = action
            availability = Q(case['recipient_availability']) if target == 'recipient' else Q(1)
            chance = availability if action == true_law else Q(0)
            for capture, chance_out in ((True, chance), (False, 1-chance)):
                if not chance_out:
                    continue
                t, d, ev = dict(s), dict(c), dict(event, capture=capture)
                if capture:
                    t['recipient' if target == 'recipient' else 'fuel'] += case['packet']
                    d[target + '_captures'] += 1
                else:
                    d['waste'] += case['packet']
                if t['fuel'] >= 1:
                    t['fuel'] -= 1; d['spent'] += 1; d['evidence'] += 1
                    available = not (target == 'recipient' and (not case['channel'] or arm == 'private_only'))
                    if available:
                        receipt = bool(capture)
                        if arm == 'private_as_recipient' and target == 'recipient':
                            receipt = False
                        label = action if receipt else 1-action
                        ev['label'] = label
                        d['decoder_errors'] += int(label != true_law)
                    else:
                        label = None; d['missing_evidence'] += 1
                    if t['fuel'] >= case['write']:
                        t['fuel'] -= case['write']; d['spent'] += case['write']; d['writes'] += 1
                        ev['paid_write'] = True
                        old_actor_command = read(arm, t['q'], 0)
                        if label is not None and arm != 'frozen':
                            t['q'] = write(arm, t['q'], obs_target, label)
                        if target == 'recipient':
                            d['actor_command_changed'] += int(old_actor_command != read(arm, t['q'], 0))
                    else:
                        d['unpaid_write'] += 1
                ev['q_after'] = t['q']
                ev['command_after'] = read(arm, t['q'], obs_target)
                assert old['fuel'] + old['recipient'] + case['packet'] == (
                    t['fuel'] + t['recipient'] + d['spent']-oldc['spent'] + d['waste']-oldc['waste'])
                nxt.append((mass*chance_out, t, d, oldtrace + [ev]))
        paths = nxt
        assert sum(p for p, *_ in paths) == 1
    return [(p, *finish(initial, case, arm, s, c, tr)) for p, s, c, tr in paths]


def hash_paths(paths):
    return {str(p.relative_to(REPO)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def source_hashes():
    paths = [Path(__file__), HERE/'PROTOCOL.md', PARENT,
             PARENT.parent/'PROTOCOL.md', parent.PARENT, parent.parent.PARENT,
             parent.parent.upstream.OLD_PATH, parent.parent.upstream.old.ARITHMETIC]
    return hash_paths(paths)


def fixtures():
    data = {}
    for reserve in sorted({c['initial_common'] for c in cases().values()}):
        original = parent.Law(initial_common=reserve, horizon=12)
        prefix = parent.Law(initial_common=reserve, horizon=8)
        preps, visited = parent.prepare(original)
        rows = {}
        for producer in PRODUCERS:
            rows[producer] = {}
            for prep in preps:
                if prep['commissioned']:
                    rows[producer][str(prep['reserve'])] = parent.terminal_records(prefix, producer, prep['reserve'])
        data[str(reserve)] = dict(original_law=original.record(), prefix_law=prefix.record(),
                                 preparations=preps, preparation_states=visited, prefix_records=rows)
    return data


def compare(case, arm, producer, fixture, verify=None):
    metrics = defaultdict(Q)
    distribution = defaultdict(Q)
    witness = None
    for prep in fixture['preparations']:
        pp = Q(prep['probability'])
        metrics['preparation_spent'] += pp*prep['preparation_spent']
        if not prep['commissioned']:
            metrics['uncommissioned_energy'] += pp*prep['remaining_energy']
            key = json.dumps(dict(kind='preparation_failure', state=prep['state']), sort_keys=True)
            distribution[key] += pp
            continue
        metrics['p_commissioned'] += pp
        metrics['adapter_spent'] += pp*fixture['original_law']['adapter']
        assert prep['packets'] == 12 and prep['remainder'] == 0
        for row in fixture['prefix_records'][producer][str(prep['reserve'])]:
            p = pp*Q(row['probability'])
            marks = row['conditional_mean_marks']
            assert prep['reserve'] + 80 == row['state']['fuel'] + Q(marks['spent']) + Q(marks['waste'])
            metrics['prefix_spent'] += p*Q(marks['spent'])
            metrics['prefix_waste'] += p*Q(marks['waste'])
            out = suffix(case, arm, row['state'], row['final_regime'])
            if verify is not None:
                verify(case, arm, row['state'], row['final_regime'], out)
            for pr, state, counts, trace in out:
                for key, value in counts.items():
                    metrics[key] += p*pr*value
                key = json.dumps(dict(kind='suffix', state=state, metrics=counts), sort_keys=True)
                distribution[key] += p*pr
                if counts['strict_witness'] and witness is None:
                    witness = dict(preparation=prep, predecessor=row, state=state, metrics=counts, trace=trace,
                                   unconditional_terminal_branch_mass=str(p*pr))
    keys = ('preparation_spent', 'adapter_spent', 'uncommissioned_energy',
            'prefix_spent', 'prefix_waste', 'spent', 'waste', 'final_actor', 'final_recipient')
    for key in COUNTS + ('recipient_correction', 'strict_witness', 'final_actor', 'final_recipient', 'active_memory'):
        metrics.setdefault(key, Q(0))
    assert sum(metrics[k] for k in keys) == case['initial_common'] + 121
    assert sum(distribution.values()) == 1
    return dict(metrics={k: str(v) for k, v in sorted(metrics.items())},
                distribution=[dict(probability=str(p), **json.loads(k)) for k, p in sorted(distribution.items())],
                witness=witness)


def main():
    before = source_hashes()
    fs = fixtures()
    result = {}
    for name, case in cases().items():
        result[name] = dict(law=case, producers={})
        for producer in PRODUCERS:
            result[name]['producers'][producer] = {
                arm: compare(case, arm, producer, fs[str(case['initial_common'])]) for arm in ARMS}
            a = result[name]['producers'][producer]
            assert a['indexed'] == a['conventional']
        assert result[name]['producers']['variable'] == result[name]['producers']['conventional']
        print(name, {a: result[name]['producers']['variable'][a]['metrics']['strict_witness'] for a in ARMS}, flush=True)
    assert source_hashes() == before, 'Source changed during run; rerun.'
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before, fixtures=fs), indent=2)+'\n')
    (HERE/'results.json').write_text(json.dumps(dict(source_sha256=before, cases=result), indent=2)+'\n')


if __name__ == '__main__':
    main()
