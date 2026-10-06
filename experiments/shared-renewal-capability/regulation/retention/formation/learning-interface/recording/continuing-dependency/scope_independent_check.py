"""Independent finite replay; no producer transition implementation is imported.

The earlier independent checker supplies the frozen ancestral laws. New scope
laws are reconstructed here from the prospective protocol. This checker author
participated in study design: separate implementation, not blind replication.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
spec = importlib.util.spec_from_file_location('prior_independent', HERE / 'criterion_independent_check.py')
I = importlib.util.module_from_spec(spec)
spec.loader.exec_module(I)
EXTRA = ['scopeReaders', 'activityA', 'activityB', 'recordA', 'recordB',
         'snapshotA', 'snapshotB', 'lastTarget', 'lastPayload', 'scopeSelected',
         'programCounter', 'scopeCommonSpent', 'scopeTotalSpent']
COLS = I.COLUMNS + EXTRA
WORDS = {0: [], 1: ['native:repair', 'native:capture', 'finishA'],
         2: ['native:capture', 'finishA'], 3: ['finishA'], 4: ['finishB']}
TRAINING = ['assemble'] * 9 + ['native:leak_local', 'admit', 'native:wear_a',
    'native:bulk_a', 'judge', 'native:damage', 'probeCapture', 'armRepair',
    'native:repair', 'observe', 'commit', 'probeCapture', 'compileCriterion']
PREFIX = ['assemble'] * 3 + ['contactA', 'formA', 'primeA', 'contactA',
                            'formB', 'primeB', 'contactB']
CASES = {'completion_faithful': (0, False, 'complete'),
         'completion_stale': (2, False, 'complete'),
         'completion_missing': (1, False, 'complete'),
         'completion_clamped': (0, True, 'complete'),
         'dissociation_faithful': (0, False, 'dissociate'),
         'dissociation_stale': (2, False, 'dissociate'),
         'unfinished_faithful': (0, False, 'unfinished'),
         'unfinished_false_absent': (3, False, 'unfinished'),
         'source_empty_faithful': (0, False, 'source_empty')}


def pack(s): return [s[k] for k in COLS]
def unpack(v):
    assert len(v) == len(COLS)
    return dict(zip(COLS, v))
def held(s): return sum(s[k] in (1, 2, 3) for k in ('activityA', 'activityB'))
def valid(s):
    I.valid(s)
    assert 0 <= s['scopeReaders'] <= 3
    assert all(s[k] in range(5) for k in ('activityA', 'activityB'))
    assert all(s[k] in range(6) for k in ('recordA', 'recordB', 'snapshotA', 'snapshotB'))
    assert I.population(s) + 2*(s['parts'] + s['scopeReaders'] + held(s)) <= 78


def native_view(s):
    t = {k: s[k] for k in I.COLUMNS}
    t['parts'] += s['scopeReaders'] + held(s)
    return t


def guard(s, event):
    if event.startswith('native:'):
        return I.native_guard(native_view(s), event[7:])
    if event == 'assemble':
        return (s['scopeReaders'] < 3 and s['freeA'] > 0 and s['freeH'] > 0
                and s['common'] > 0 and s['activityA'] == s['activityB'] == 0)
    if s['scopeReaders'] != 3: return False
    if event in ('formA', 'formB'):
        return s['activity'+event[-1]] == 0 and min(s['freeA'], s['freeH'], s['common']) > 0
    if event in ('primeA', 'finishA'):
        return s['activityA'] == (1 if event == 'primeA' else 2) and s['local'] == 1
    if event in ('primeB', 'finishB'):
        return s['activityB'] == (1 if event == 'primeB' else 2) and s['common'] > 0
    if event in ('dissociateA', 'dissociateB'):
        return s['activity'+event[-1]] in (1, 2) and s['common'] > 0
    return event in ('contactA', 'contactB', 'refreshA', 'select') and s['common'] > 0


def select(s, cfg):
    a, b = (s['snapshotA'], s['snapshotB']) if cfg['clamp'] else (s['recordA'], s['recordB'])
    if a == 3 and s['candidates'] == 1:
        if s['local']: return 3
        if s['source'] and s['intact']: return 2
        if s['source'] and s['resident'] == 1 and s['common']: return 1
    return 4 if b == 3 and s['common'] else 0


def step(s, cfg, event):
    valid(s)
    effective = event
    if event == 'act':
        assert s['programCounter'] < len(WORDS[s['scopeSelected']])
        effective = WORDS[s['scopeSelected']][s['programCounter']]
    assert guard(s, effective), (effective, pack(s))
    t = dict(s)
    if effective.startswith('native:'):
        # Reuse only the previously independent plant law, extracting its seven
        # physical coordinates. Old criterion records/ledgers are frozen here.
        v = I.native_apply(native_view(s), effective[7:])
        t.update({k: v[k] for k in I.COLUMNS[:7]})
    elif effective in ('primeA', 'finishA'):
        t.update(local=0, intact=0, activityA=2 if effective == 'primeA' else 3)
    else:
        t['common'] -= 1
        if effective in ('assemble', 'formA', 'formB'):
            t['freeA'] -= 1
            t['freeH'] -= 1
            if effective == 'assemble': t['scopeReaders'] += 1
            else: t['activity'+effective[-1]] = 1
        elif effective in ('primeB', 'finishB'):
            t['activityB'] = 2 if effective == 'primeB' else 3
        elif effective.startswith('dissociate'):
            t['activity'+effective[-1]] = 4
            t['freeA'] += 1
            t['freeH'] += 1
        elif effective in ('contactA', 'contactB', 'refreshA'):
            target = 'B' if effective == 'contactB' else 'A'
            payload = s['activity'+target] + 1
            if effective == 'refreshA':
                payload = {0: payload, 1: 0, 2: s['snapshotA'], 3: 1}[cfg['contact_mode']]
            t['lastTarget'], t['lastPayload'] = (1 if target == 'A' else 2), payload
            if payload:
                t['record'+target] = payload
                if payload == 3 and not s['snapshot'+target]: t['snapshot'+target] = 3
        elif effective == 'select':
            t['scopeSelected'], t['programCounter'] = select(t, cfg), 0
    t['scopeCommonSpent'] += s['common'] - t['common']
    t['scopeTotalSpent'] += I.energy(s) - I.energy(t)
    if event == 'act': t['programCounter'] = s['programCounter'] + 1
    valid(t)
    assert I.energy(s) + s['scopeTotalSpent'] == I.energy(t) + t['scopeTotalSpent']
    assert s['common'] + s['scopeCommonSpent'] == t['common'] + t['scopeCommonSpent']
    assert t['common'] <= s['common'] and t['source'] <= s['source']
    assert all(t[k] == s[k] for k in I.COLUMNS[7:])
    for k in ('activityA', 'activityB'):
        assert t[k] >= s[k]
        if s[k] == 3: assert t[k] == 3
    return t, effective


def inspect(data):
    assert data['status'] == 'passed' and data['vector_columns'] == COLS
    a = data['ancestry']
    assert a['initial'] == [0, 0, 0, 0, 0, 360, 230]
    assert a['events'] == I.expected_ancestor() and len(a['steps']) == 94
    s = I.unpack(a['initial'] + [0]*16)
    for event, row in zip(a['events'], a['steps']):
        assert row['event'] == event and row['before'] == I.pack(s)[:7]
        s = I.native_apply(s, event)
        assert row['after'] == I.pack(s)[:7]
    assert a['final'] == I.pack(s)[:7] == [38, 39, 1, 1, 1, 293, 216]
    training = data['criterion_training']
    assert training['config'] == dict(receipt_mode=0, clamp=False, later_repair=False, force_bulk=False)
    assert training['events'] == TRAINING and len(training['steps']) == len(TRAINING)
    s = I.unpack(a['final'] + [0]*16)
    s['candidates'] = 7
    assert training['initial'] == I.pack(s)
    for event, row in zip(TRAINING, training['steps']):
        assert row['event'] == event and row['before'] == I.pack(s)
        s = I.step(s, training['config'], event)
        assert row['after'] == I.pack(s)
    assert training['final'] == I.pack(s)
    assert s['common'] == 274 and s['candidates'] == 1 and s['criterionActive'] == 0
    initial = I.pack(s) + [0]*len(EXTRA)
    rows = {c['name']: c for c in data['cases']}
    assert set(rows) == set(CASES) and len(rows) == len(data['cases'])
    count = denied = 0
    for name, case in rows.items():
        mode, clamp, branch = CASES[name]
        cfg = case['config']
        assert cfg == dict(contact_mode=mode, clamp=clamp) and case['branch'] == branch
        assert case['initial'] == initial
        word = list(PREFIX)
        if branch == 'complete': word += ['native:repair', 'native:capture', 'finishA']
        if branch == 'dissociate': word += ['dissociateA']
        if branch == 'source_empty':
            word += ['native:repair'] + ['native:capture', 'native:leak_local']*215 + ['native:damage']
        branch_end = len(word)
        word += ['refreshA'] + ['native:leak_common']*(262 if branch == 'unfinished' else 261) + ['select']
        assert case['events'][:len(word)] == word
        assert all(e == 'act' for e in case['events'][len(word):])
        assert case['events'] == [r['event'] for r in case['steps']]
        s = unpack(initial)
        visited = [pack(s)]
        for row in case['steps']:
            assert row['before'] == pack(s), (name, row['event'], 'before')
            s, effect = step(s, cfg, row['event'])
            assert row['after'] == pack(s) and row['effect'] == effect, (name, row['event'], 'after')
            visited.append(pack(s))
        marks = case['milestones']
        positions = {'empty_acquired':4, 'scope_A':7, 'scope_AB':10,
            'actual_branch':branch_end, 'acquired_revision':branch_end+1,
            'decision':len(word)-1, 'selected':len(word), 'final':len(case['events'])}
        assert set(marks) == set(positions)
        assert all(marks[k] == visited[i] for k, i in positions.items())
        assert case['final'] == pack(s) and case['selected'] == s['scopeSelected']
        assert case['product_A'] == (s['activityA'] == 3) and case['product_B'] == (s['activityB'] == 3)
        assert case['damage_remaining'] == (s['intact'] == 0)
        assert case['actual_pending'] == [k for k in ('A', 'B') if s['activity'+k] in (1,2)]
        prefix = 'snapshot' if clamp else 'record'
        assert case['acquired_pending'] == [k for k in ('A', 'B') if s[prefix+k] in (2,3)]
        remaining = s['programCounter'] < len(WORDS[s['scopeSelected']])
        if remaining:
            next_event = WORDS[s['scopeSelected']][s['programCounter']]
            assert not guard(s, next_event)
            assert case['denied'] == [dict(event='act', effect=next_event, state=pack(s))]
        else: assert case['denied'] == []
        count += len(case['steps'])
        denied += len(case['denied'])
    f, c = rows['completion_faithful'], rows['completion_clamped']
    assert f['milestones']['decision'] == c['milestones']['decision']
    assert f['product_B'] and not c['product_B'] and f['product_A'] == c['product_A'] == True
    assert rows['dissociation_faithful']['product_B'] and not rows['dissociation_faithful']['product_A']
    assert rows['unfinished_faithful']['product_A'] and not rows['unfinished_faithful']['product_B']
    assert not rows['unfinished_false_absent']['product_A'] and rows['unfinished_false_absent']['product_B']
    assert rows['source_empty_faithful']['actual_pending'] == ['A']
    assert rows['source_empty_faithful']['acquired_pending'] == ['A','B']
    return dict(cases=len(rows), extension_events=count, extension_states=count+len(rows),
                coordinates=36, denied_events=denied, ancestry_events=94, training_events=22)


def main():
    path = HERE/'scope-results.json'
    raw = path.read_bytes()
    data = json.loads(raw)
    hashes = {p: I.sha(ROOT/p) for p in data['source_hashes']}
    assert hashes == data['source_hashes']
    I.check_ancestor_definitions(hashes)
    result = inspect(data)
    detected = []
    for kind in ('material', 'historical', 'missing_contact', 'other_activity', 'hidden_denial', 'claimed_product'):
        altered = deepcopy(data)
        rows = {c['name']: c for c in altered['cases']}
        if kind == 'material': rows['completion_faithful']['steps'][0]['after'][0] += 1
        elif kind == 'historical': rows['completion_faithful']['steps'][0]['after'][10] = 0
        elif kind == 'missing_contact':
            row = next(r for r in rows['completion_missing']['steps'] if r['event'] == 'refreshA')
            row['after'][COLS.index('recordA')] = 4
        elif kind == 'other_activity': rows['completion_faithful']['milestones']['actual_branch'][COLS.index('activityB')] = 3
        elif kind == 'hidden_denial': rows['completion_stale']['denied'] = []
        elif kind == 'claimed_product': rows['dissociation_faithful']['product_A'] = True
        try: inspect(altered)
        except AssertionError: detected.append(kind)
        else: raise AssertionError(('undetected corruption', kind))
    assert path.read_bytes() == raw
    assert hashes == {p: I.sha(ROOT/p) for p in hashes}
    receipt = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(), **result,
        detected_mutations=detected, producer_result_sha256=I.sha(path),
        checker_sha256=I.sha(Path(__file__)), helper_sha256=I.sha(HERE/'criterion_independent_check.py'),
        source_hashes=hashes, no_producer_transition_import=True,
        scope='Separate finite replay, including the original ancestor and earlier training. '
              'New recipes, contact semantics, priority and schedule are supplied. '
              'This does not certify lived concern, normative authority or universal grounding.')
    (HERE/'scope-independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k != 'source_hashes'}, indent=2))


if __name__ == '__main__': main()
