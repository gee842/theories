"""Paid one-sided recipient identification on actual formed predecessor states."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
PARENT = HERE.parent / 'model.py'
spec = importlib.util.spec_from_file_location('_identification_recipient', PARENT)
recipient = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = recipient
spec.loader.exec_module(recipient)
parent = recipient.parent
ARMS = ('positive', 'conventional', 'failure_label', 'no_exploration')
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
PHASES = ('recipient', 'actor', 'recipient', 'actor', 'recipient')
COUNTS = ('eligible', 'installed', 'trials', 'recipient_trials', 'actor_trials',
          'recipient_captures', 'actor_captures', 'acquisitions', 'writes',
          'missing_evidence', 'qualifications', 'false_qualification_writes',
          'qualified_recipient_trials', 'false_qualified_commands',
          'qualified_recipient_captures', 'unaffordable', 'spent', 'waste')


def cases():
    base = dict(initial_common=30, opposite=True, recipient_availability='3/4',
                channel=True, write=2, packet=10, target_flip=False)
    return dict(primary=base, noiseless=dict(base, recipient_availability='1'),
                same_law=dict(base, opposite=False),
                no_opportunity=dict(base, recipient_availability='0'),
                missing_channel=dict(base, channel=False),
                target_change=dict(base, target_flip=True),
                low_reserve=dict(base, initial_common=12),
                higher_reserve=dict(base, initial_common=36),
                expensive_write=dict(base, write=4))


def read(q, target):
    return (q >> int(target == 'recipient')) & 1


def update(arm, q, flag, target, receipt):
    """Controller inputs exclude truth, stocks outside own account and clocks."""
    if target == 'actor' or receipt is None:
        return q, flag
    actor, candidate = q & 1, q >> 1
    if arm == 'conventional':
        # Explicit table: index 2*flag+receipt, value (toggle, new flag).
        toggle, new_flag = ((1, 0), (0, 1), (0, 1), (0, 1))[2*flag+int(receipt)]
        return actor + 2*(candidate ^ toggle), new_flag
    if arm == 'failure_label':
        return actor + 2*(candidate if receipt else 1-candidate), 1
    if flag:
        return q, flag
    if receipt:
        return q, 1
    if arm == 'positive':
        return actor + 2*(1-candidate), 0
    assert arm == 'no_exploration'
    return q, 0


def suffix(case, arm, initial, actor_law):
    assert arm in ARMS
    state = dict(initial, recipient=0, source=5*case['packet'], active=False,
                 installed=False, recoded=False, escrow=0)
    counts = dict.fromkeys(COUNTS, 0)
    counts['eligible'] = int(recipient.eligible(initial))
    if counts['eligible'] and state['fuel'] >= 4:
        state['fuel'] -= 4; counts['spent'] += 4
        bit = int(initial['q'] == 4)
        state.update(q=bit+2*bit, last=0, installed=True, active=True, recoded=True)
        counts['installed'] = 1
    paths = [(Q(1), state, counts, [])]
    for phase, target in enumerate(PHASES):
        nxt = []
        true_law = actor_law ^ int(target == 'recipient' and case['opposite'])
        if target == 'recipient' and case['target_flip'] and phase == 4:
            true_law ^= 1
        for mass, old, oldc, oldtrace in paths:
            s, c = dict(old), dict(oldc)
            event = dict(target=target, report=None, action=None, capture=None,
                         receipt=None, paid_write=False, status=None,
                         q_before=s['q'], flag_before=s['last'],
                         q_after=s['q'], flag_after=s['last'], true_law=true_law,
                         before=dict(s), microstates=[])
            s['source'] -= case['packet']
            assert s['source'] >= 0
            bill = 6+case['write']
            if not s['active'] or s['fuel'] < bill:
                if s['active']:
                    c['unaffordable'] += 1
                    s['active'] = False
                    event['status'] = 'unaffordable'
                else:
                    event['status'] = 'inactive'
                c['waste'] += case['packet']
                event['after'] = dict(s)
                nxt.append((mass, s, c, oldtrace+[event]))
                continue
            event['status'] = 'completed'
            event['report'] = target
            action = read(s['q'], target)
            event['action'] = action
            if target == 'recipient' and s['last']:
                c['qualified_recipient_trials'] += 1
                c['false_qualified_commands'] += int(action != true_law)
            s['fuel'] -= 1; c['spent'] += 1
            event['microstates'].append(dict(phase='rent', fuel=s['fuel'], escrow=0))
            s['fuel'] -= 1; c['spent'] += 1
            event['microstates'].append(dict(phase='target_observation', fuel=s['fuel'], escrow=0))
            s['fuel'] -= 1+case['write']; s['escrow'] = 1+case['write']
            event['microstates'].append(dict(phase='reserve_feedback', fuel=s['fuel'], escrow=s['escrow']))
            s['fuel'] -= 3; c['spent'] += 3
            event['microstates'].append(dict(phase='work', fuel=s['fuel'], escrow=s['escrow']))
            assert s['fuel'] >= 0
            c['trials'] += 1; c[target+'_trials'] += 1
            availability = Q(case['recipient_availability']) if target == 'recipient' else Q(1)
            chance = availability if action == true_law else Q(0)
            for capture, chance_out in ((True, chance), (False, 1-chance)):
                if not chance_out:
                    continue
                t, d, ev = dict(s), dict(c), dict(event)
                ev['microstates'] = list(event['microstates'])
                ev['capture'] = capture
                if capture:
                    t['recipient' if target == 'recipient' else 'fuel'] += case['packet']
                    d[target+'_captures'] += 1
                    if target == 'recipient' and old['last']:
                        d['qualified_recipient_captures'] += 1
                else:
                    d['waste'] += case['packet']
                ev['microstates'].append(dict(phase='receipt', fuel=t['fuel'],
                                              recipient=t['recipient'], escrow=t['escrow']))
                receipt = bool(capture) if target == 'actor' or case['channel'] else None
                ev['receipt'] = receipt
                t['escrow'] -= 1; d['spent'] += 1; d['acquisitions'] += 1
                d['missing_evidence'] += int(receipt is None)
                ev['microstates'].append(dict(phase='acquire', fuel=t['fuel'], escrow=t['escrow']))
                before_q, before_flag = t['q'], t['last']
                t['q'], t['last'] = update(arm, t['q'], t['last'], target, receipt)
                if target == 'recipient' and receipt is not None:
                    d['qualifications'] += int(not before_flag and t['last'])
                    d['false_qualification_writes'] += int(t['last'] and read(t['q'], target) != true_law)
                t['escrow'] -= case['write']; d['spent'] += case['write']; d['writes'] += 1
                assert t['escrow'] == 0 and (t['q'] & 1) == (before_q & 1)
                ev.update(paid_write=True, q_after=t['q'], flag_after=t['last'])
                ev['microstates'].append(dict(phase='commit', fuel=t['fuel'], escrow=0,
                                              q=t['q'], flag=t['last']))
                ev['after'] = dict(t)
                assert old['fuel']+old['recipient']+old['source'] == (
                    t['fuel']+t['recipient']+t['source']+d['spent']-oldc['spent']+d['waste']-oldc['waste'])
                nxt.append((mass*chance_out, t, d, oldtrace+[ev]))
        paths = nxt
        assert sum(p for p, *_ in paths) == 1
    out = []
    for p, s, c, tr in paths:
        c = dict(c)
        r1, a1, r2, a2, r3 = tr
        c['strict_witness'] = int(bool(r1['capture'] is False and r1['flag_after'] == 0
            and r1['q_after'] != r1['q_before'] and r2['capture'] is True
            and r2['flag_after'] == 1 and r3['flag_before'] == 1
            and r3['capture'] is True and a1['capture'] is True and a2['capture'] is True))
        c.update(final_actor=s['fuel'], final_recipient=s['recipient'],
                 final_source=s['source'], final_qualified=int(s['recoded'] and bool(s['last'])),
                 active_memory=int(s['active']))
        c['final_false_qualified'] = int(bool(c['final_qualified']) and
            read(s['q'], 'recipient') != (actor_law ^ int(case['opposite']) ^ int(case['target_flip'])))
        assert initial['fuel']+5*case['packet'] == sum(c[k] for k in
            ('final_actor','final_recipient','final_source','spent','waste'))
        assert s['fuel'] >= 0 and s['recipient'] >= 0 and s['escrow'] == 0
        out.append((p, s, c, tr))
    return out


def source_hashes():
    paths = [Path(__file__), HERE/'PROTOCOL.md', PARENT, PARENT.parent/'PROTOCOL.md',
             recipient.PARENT, recipient.PARENT.parent/'PROTOCOL.md', parent.PARENT,
             parent.parent.PARENT, parent.parent.upstream.OLD_PATH,
             parent.parent.upstream.old.ARITHMETIC]
    return {str(p.relative_to(REPO)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def fixtures():
    data = {}
    for reserve in sorted({c['initial_common'] for c in cases().values()}):
        original = parent.Law(initial_common=reserve, horizon=13)
        prefix = parent.Law(initial_common=reserve, horizon=8)
        preps, visited = parent.prepare(original)
        rows = {producer: {str(prep['reserve']): parent.terminal_records(prefix, producer, prep['reserve'])
                          for prep in preps if prep['commissioned']} for producer in PRODUCERS}
        data[str(reserve)] = dict(original_law=original.record(), prefix_law=prefix.record(),
            preparations=preps, preparation_states=visited, prefix_records=rows)
    return data


def compare(case, arm, producer, fixture):
    metrics, distribution, paths = defaultdict(Q), defaultdict(Q), []
    witness = None
    for prep_id, prep in enumerate(fixture['preparations']):
        pp = Q(prep['probability'])
        metrics['preparation_spent'] += pp*prep['preparation_spent']
        if not prep['commissioned']:
            metrics['uncommissioned_energy'] += pp*prep['remaining_energy']
            key = json.dumps(dict(kind='preparation_failure', state=prep['state']), sort_keys=True)
            distribution[key] += pp
            continue
        metrics['p_commissioned'] += pp
        metrics['adapter_spent'] += pp*fixture['original_law']['adapter']
        assert prep['packets'] == 13 and prep['remainder'] == 0
        for row_id, row in enumerate(fixture['prefix_records'][producer][str(prep['reserve'])]):
            p = pp*Q(row['probability'])
            marks = row['conditional_mean_marks']
            assert prep['reserve']+80 == row['state']['fuel']+Q(marks['spent'])+Q(marks['waste'])
            metrics['prefix_spent'] += p*Q(marks['spent'])
            metrics['prefix_waste'] += p*Q(marks['waste'])
            for pr, s, c, tr in suffix(case, arm, row['state'], row['final_regime']):
                for key, value in c.items():
                    metrics[key] += p*pr*value
                key = json.dumps(dict(kind='suffix', state=s, metrics=c), sort_keys=True)
                distribution[key] += p*pr
                record = dict(preparation_id=prep_id, predecessor_id=row_id,
                    conditional_probability=str(pr), probability=str(p*pr), state=s, metrics=c, trace=tr)
                paths.append(record)
                if c['strict_witness'] and witness is None:
                    witness = dict(preparation=prep, predecessor=row, **record)
    keys = ('preparation_spent','adapter_spent','uncommissioned_energy',
            'prefix_spent','prefix_waste','spent','waste','final_actor','final_recipient','final_source')
    for key in COUNTS+('strict_witness','final_actor','final_recipient','final_source',
                       'final_qualified','final_false_qualified','active_memory'):
        metrics.setdefault(key, Q(0))
    assert sum(metrics[k] for k in keys) == case['initial_common']+131
    assert sum(distribution.values()) == 1
    return dict(metrics={k:str(v) for k,v in sorted(metrics.items())},
                distribution=[dict(probability=str(p), **json.loads(k)) for k,p in sorted(distribution.items())],
                paths=paths, witness=witness)


def main():
    before = source_hashes()
    fs, result = fixtures(), {}
    for name, case in cases().items():
        result[name] = dict(law=case, producers={})
        for producer in PRODUCERS:
            result[name]['producers'][producer] = {
                arm: compare(case, arm, producer, fs[str(case['initial_common'])]) for arm in ARMS}
            rows = result[name]['producers'][producer]
            assert rows['positive'] == rows['conventional']
        assert result[name]['producers']['variable'] == result[name]['producers']['conventional']
        print(name, {a:result[name]['producers']['variable'][a]['metrics']['strict_witness'] for a in ARMS}, flush=True)
    assert source_hashes() == before, 'Sources changed during run; rerun.'
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,fixtures=fs),indent=2)+'\n')
    (HERE/'results.json').write_text(json.dumps(dict(source_sha256=before,cases=result),indent=2)+'\n')


if __name__ == '__main__':
    main()
