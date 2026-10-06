"""Separate finite replay from the prospective initiation protocol.

Imports only frozen independent ancestral-law helpers, never producer laws.
The checker author participated in design; this is not blind replication.
"""
from copy import deepcopy
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
spec = importlib.util.spec_from_file_location('scope_independent', HERE/'scope_independent_check.py')
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)
I = P.I
EXTRA = ['initiationParts', 'trialA', 'newB', 'candidateA', 'contactPhase', 'binding',
         'pendingCost', 'observedCost', 'formFamily', 'finishFamily', 'newBRecord',
         'initiationSelected', 'initiationPC', 'initiationCommonSpent', 'initiationTotalSpent']
COLS = P.COLS + EXTRA
WORDS = {0: [], 1: ['finishNewB'], 2: ['formTargetA', 'finishNewB'], 3: ['formTargetA']}
TRAINING = ['assemble']*3 + ['armForm', 'formTrialA', 'observe', 'commit', 'armFinish',
    'finishOldB', 'observe', 'commit', 'native:repair', 'native:capture', 'primeTrialA',
    'native:repair', 'native:capture', 'finishTrialA', 'formNewB', 'primeNewB', 'contactNewB']
CASES = {'scarce_faithful': (0, 0, False, 'scarce'),
         'scarce_clamped': (0, 0, True, 'scarce'),
         'scarce_missing_form': (1, 0, False, 'scarce'),
         'scarce_wrong_form': (2, 0, False, 'scarce'),
         'scarce_wrong_finish': (0, 2, False, 'scarce'),
         'ample_faithful': (0, 0, False, 'ample'),
         'ample_intervening_loss': (0, 0, False, 'loss'),
         'B_completed': (0, 0, False, 'complete'),
         'B_dissociated': (0, 0, False, 'dissociate')}
FORM = {'formTrialA': 'trialA', 'formNewB': 'newB', 'formTargetA': 'candidateA'}
LOCAL = {'primeTrialA': ('trialA', 1), 'finishTrialA': ('trialA', 2),
         'primeTargetA': ('candidateA', 1), 'finishTargetA': ('candidateA', 2)}
PHYSICAL = set(FORM) | set(LOCAL) | {'finishOldB', 'primeNewB', 'finishNewB', 'dissociateNewB'}


def pack(s): return [s[k] for k in COLS]
def unpack(v):
    assert len(v) == len(COLS)
    return dict(zip(COLS, v))
def native_view(s):
    t = P.native_view(s)
    t['parts'] += s['initiationParts'] + sum(s[k] in (1, 2, 3) for k in ('trialA', 'newB', 'candidateA'))
    return t

def valid(s):
    P.valid(s)
    assert 0 <= s['initiationParts'] <= 3
    assert all(s[k] in range(5) for k in ('trialA', 'newB', 'candidateA', 'contactPhase'))
    assert s['binding'] in range(3) and s['newBRecord'] in range(6)
    assert all(s[k] in range(8) for k in ('pendingCost', 'observedCost', 'formFamily', 'finishFamily'))
    assert I.population(s) + 2*native_view(s)['parts'] <= 78


def guard(s, event):
    if event.startswith('native:'): return I.native_guard(native_view(s), event[7:])
    if event == 'assemble':
        return s['initiationParts'] < 3 and min(s['freeA'], s['freeH'], s['common']) > 0 and s['trialA'] == 0
    if s['initiationParts'] != 3: return False
    if event in FORM: return s[FORM[event]] == 0 and min(s['freeA'], s['freeH'], s['common']) > 0
    if event == 'finishOldB': return s['activityB'] == 2 and s['common'] > 0
    if event in LOCAL:
        field, phase = LOCAL[event]
        return s[field] == phase and s['local'] == 1
    if event in ('primeNewB', 'finishNewB'):
        return s['newB'] == (1 if event == 'primeNewB' else 2) and s['common'] > 0
    if event == 'dissociateNewB': return s['newB'] in (1, 2) and s['common'] > 0
    if not s['common']: return False
    if event == 'armForm': return s['contactPhase'] in (0, 4) and s['trialA'] == 0
    if event == 'armFinish': return s['contactPhase'] in (0, 4) and s['activityB'] == 2
    if event in ('observe', 'commit'): return s['contactPhase'] == (2 if event == 'observe' else 3)
    return event in ('contactNewB', 'select')


def subtract(support, channel):
    if channel not in (1, 2, 4): return None
    index = (1, 2, 4).index(channel)
    if support[index] < 1: return None
    out = list(support)
    out[index] -= 1
    return out


def select(s, cfg):
    if s['newBRecord'] != 3: return 3
    if cfg['clamp'] or s['formFamily'] not in (1, 2, 4) or s['finishFamily'] not in (1, 2, 4): return 2
    support = [s['common'], s['local'], s['source']]
    after = subtract(support, s['formFamily'])
    if after is not None and subtract(after, s['finishFamily']) is not None: return 2
    return 1 if subtract(support, s['finishFamily']) is not None else 0


def step(s, cfg, event):
    valid(s)
    effect = event
    if event == 'act':
        assert s['initiationPC'] < len(WORDS[s['initiationSelected']])
        effect = WORDS[s['initiationSelected']][s['initiationPC']]
    assert guard(s, effect), (effect, pack(s))
    t = dict(s)
    if effect.startswith('native:'):
        v = I.native_apply(native_view(s), effect[7:])
        t.update({k: v[k] for k in I.COLUMNS[:7]})
    elif effect in LOCAL:
        field, phase = LOCAL[effect]
        t.update(local=0, intact=0)
        t[field] = phase+1
    else:
        t['common'] -= 1
        if effect == 'assemble' or effect in FORM:
            t['freeA'] -= 1
            t['freeH'] -= 1
            if effect == 'assemble': t['initiationParts'] += 1
            else: t[FORM[effect]] = 1
        elif effect == 'finishOldB': t['activityB'] = 3
        elif effect in ('primeNewB', 'finishNewB'): t['newB'] = 2 if effect == 'primeNewB' else 3
        elif effect == 'dissociateNewB':
            t.update(newB=4)
            t['freeA'] += 1
            t['freeH'] += 1
        elif effect in ('armForm', 'armFinish'):
            t.update(contactPhase=1, binding=1 if effect == 'armForm' else 2, pendingCost=0, observedCost=0)
        elif effect == 'observe':
            mode = cfg['form_mode'] if s['binding'] == 1 else cfg['finish_mode']
            t.update(contactPhase=3, observedCost=s['pendingCost'] if mode == 0 else (0 if mode == 1 else 4))
        elif effect == 'commit':
            field = 'formFamily' if s['binding'] == 1 else 'finishFamily'
            if s['observedCost']: t[field] &= s['observedCost']
            t['contactPhase'] = 4
        elif effect == 'contactNewB': t['newBRecord'] = s['newB']+1
        elif effect == 'select': t.update(initiationSelected=select(t, cfg), initiationPC=0)
    if s['contactPhase'] == 1 and (effect.startswith('native:') or effect in PHYSICAL):
        match = effect == ('formTrialA' if s['binding'] == 1 else 'finishOldB')
        delta = tuple(s[k]-t[k] for k in ('common', 'local', 'source'))
        emission = {(1, 0, 0): 1, (0, 1, 0): 2, (0, 0, 1): 4}.get(delta, 0)
        t.update(contactPhase=2 if match else 0, binding=s['binding'] if match else 0,
                 pendingCost=emission if match else 0)
    if event == 'act': t['initiationPC'] = s['initiationPC']+1
    t['initiationCommonSpent'] += s['common']-t['common']
    t['initiationTotalSpent'] += I.energy(s)-I.energy(t)
    valid(t)
    assert I.energy(s)+s['initiationTotalSpent'] == I.energy(t)+t['initiationTotalSpent']
    assert s['common']+s['initiationCommonSpent'] == t['common']+t['initiationCommonSpent']
    assert t['common'] <= s['common'] and t['source'] <= s['source']
    assert all(t[k] == s[k] for k in P.COLS[7:] if k != 'activityB')
    for field in ('activityA', 'activityB', 'trialA', 'newB', 'candidateA'):
        assert t[field] >= s[field]
        if s[field] == 3: assert t[field] == 3
    return t, effect


def ancestor(a):
    original = a['native']
    assert original['initial'] == [0, 0, 0, 0, 0, 360, 230]
    assert original['events'] == I.expected_ancestor() and len(original['steps']) == 94
    s = I.unpack(original['initial'] + [0]*16)
    for event, row in zip(original['events'], original['steps']):
        assert row['event'] == event and row['before'] == I.pack(s)[:7]
        s = I.native_apply(s, event)
        assert row['after'] == I.pack(s)[:7]
    assert original['final'] == I.pack(s)[:7] == [38, 39, 1, 1, 1, 293, 216]
    training = a['criterion_training']
    assert training['config'] == dict(receipt_mode=0, clamp=False, later_repair=False, force_bulk=False)
    assert training['events'] == P.TRAINING and len(training['steps']) == 22
    s = I.unpack(original['final']+[0]*16)
    s['candidates'] = 7
    assert training['initial'] == I.pack(s)
    for event, row in zip(P.TRAINING, training['steps']):
        assert row['event'] == event and row['before'] == I.pack(s)
        s = I.step(s, training['config'], event)
        assert row['after'] == I.pack(s)
    assert training['final'] == I.pack(s)
    scope = a['scope_prefix']
    assert scope['config'] == dict(contact_mode=0, clamp=False)
    events = P.PREFIX + ['native:repair', 'native:capture', 'finishA']
    assert scope['events'] == events and len(scope['steps']) == 13
    s = P.unpack(I.pack(s)+[0]*13)
    assert scope['initial'] == P.pack(s)
    for event, row in zip(events, scope['steps']):
        assert row['event'] == event and row['before'] == P.pack(s)
        s, effect = P.step(s, scope['config'], event)
        assert row['after'] == P.pack(s) and row['effect'] == effect
    assert scope['final'] == P.pack(s)
    assert I.pack(s)[:7] == [24, 25, 1, 0, 0, 264, 214]
    assert s['activityA'] == 3 and s['activityB'] == 2
    s = unpack(P.pack(s)+[0]*15)
    s['formFamily'] = s['finishFamily'] = 7
    return s


def inspect(data):
    assert data['status'] == 'passed' and data['vector_columns'] == COLS
    initial = pack(ancestor(data['ancestry']))
    rows = {c['name']: c for c in data['cases']}
    assert set(rows) == set(CASES) and len(data['cases']) == len(rows)
    count = denied = 0
    for name, case in rows.items():
        fm, cm, clamp, branch = CASES[name]
        cfg = case['config']
        assert cfg == dict(form_mode=fm, finish_mode=cm, clamp=clamp) and case['branch'] == branch
        assert case['initial'] == initial
        word = list(TRAINING)
        if branch in ('complete', 'dissociate'):
            word += ['finishNewB' if branch == 'complete' else 'dissociateNewB', 'contactNewB']
        reached = len(word)
        leaks = 244 if branch in ('complete', 'dissociate') else (245 if branch in ('ample', 'loss') else 246)
        word += ['native:leak_common']*leaks
        decision = len(word)
        word += ['select']
        selected = len(word)
        if branch == 'loss': word += ['native:leak_common']
        before_execution = len(word)
        assert case['events'][:len(word)] == word
        assert all(e == 'act' for e in case['events'][len(word):])
        assert case['events'] == [r['event'] for r in case['steps']]
        s = unpack(initial)
        visited = [initial]
        for row in case['steps']:
            assert row['before'] == pack(s), (name, row['event'], 'before')
            s, effect = step(s, cfg, row['event'])
            assert row['after'] == pack(s) and row['effect'] == effect, (name, row['event'], 'after')
            visited.append(pack(s))
        marks = {'trained': len(TRAINING), 'scope_reached': reached, 'decision': decision,
                 'selected': selected, 'before_execution': before_execution, 'final': len(case['events'])}
        assert set(marks) == set(case['milestones'])
        assert all(case['milestones'][k] == visited[pos] for k, pos in marks.items())
        assert case['final'] == pack(s) and case['selected'] == s['initiationSelected']
        assert case['pending'] == [label for label, field in [('originalA', 'activityA'),
            ('originalB', 'activityB'), ('trialA', 'trialA'), ('newB', 'newB'), ('targetA', 'candidateA')]
            if s[field] in (1, 2)]
        assert case['target_started'] == (s['candidateA'] > 0)
        assert case['newB_product'] == (s['newB'] == 3) and case['newB_dissociated'] == (s['newB'] == 4)
        assert case['retained_products'] == dict(originalA=s['activityA'] == 3,
            originalB=s['activityB'] == 3, trialA=s['trialA'] == 3)
        pending = s['initiationPC'] < len(WORDS[s['initiationSelected']])
        if pending:
            event = WORDS[s['initiationSelected']][s['initiationPC']]
            assert not guard(s, event)
            assert case['denied'] == [dict(event='act', effect=event, state=pack(s))]
        else: assert case['denied'] == []
        assert s['common'] == s['local'] == s['intact'] == 0 and s['source'] == 212
        count += len(case['events'])
        denied += len(case['denied'])
    good, clamp = rows['scarce_faithful'], rows['scarce_clamped']
    assert good['milestones']['decision'] == clamp['milestones']['decision']
    assert good['newB_product'] and not good['target_started']
    for name in ('scarce_clamped', 'scarce_missing_form', 'scarce_wrong_form', 'scarce_wrong_finish', 'ample_intervening_loss'):
        c = rows[name]
        assert c['target_started'] and not c['newB_product'] and len(c['denied']) == 1
    ample = rows['ample_faithful']
    assert ample['newB_product'] and unpack(ample['final'])['candidateA'] == 1
    assert ample['milestones']['decision'] == rows['ample_intervening_loss']['milestones']['decision']
    assert ample['milestones']['selected'] == rows['ample_intervening_loss']['milestones']['selected']
    assert rows['B_completed']['newB_product'] and rows['B_dissociated']['newB_dissociated']
    return dict(cases=len(rows), ancestry_events=129, acquisition_events=len(TRAINING), extension_events=count,
                extension_states=count+len(rows), coordinates=len(COLS), denied_events=denied)


def main():
    path = HERE/'initiation-results.json'
    raw = path.read_bytes()
    data = json.loads(raw)
    hashes = {p: I.sha(ROOT/p) for p in data['source_hashes']}
    assert hashes == data['source_hashes']
    I.check_ancestor_definitions(hashes)
    old = json.loads((HERE/'scope-results.json').read_text())
    original = next(c for c in old['cases'] if c['name'] == 'completion_faithful')
    assert data['ancestry']['native'] == old['ancestry']
    assert data['ancestry']['criterion_training'] == old['criterion_training']
    assert data['ancestry']['scope_prefix']['steps'] == original['steps'][:13]
    assert data['ancestry']['scope_prefix']['final'] == original['milestones']['actual_branch']
    result = inspect(data)
    mutations = []
    for kind in ('material', 'inherited_product', 'contact_binding', 'false_family',
                 'hidden_denial', 'false_new_product', 'erased_intervening_loss', 'reset_ancestry'):
        altered = deepcopy(data)
        rows = {c['name']: c for c in altered['cases']}
        c = rows['scarce_faithful']
        if kind == 'material': c['steps'][0]['after'][0] += 1
        elif kind == 'inherited_product': c['steps'][0]['after'][COLS.index('activityA')] = 0
        elif kind == 'contact_binding':
            next(r for r in c['steps'] if r['event'] == 'formTrialA')['after'][COLS.index('binding')] = 2
        elif kind == 'false_family':
            next(r for r in rows['scarce_wrong_form']['steps'] if r['event'] == 'commit')['after'][COLS.index('formFamily')] = 1
        elif kind == 'hidden_denial': rows['scarce_clamped']['denied'] = []
        elif kind == 'false_new_product': rows['ample_faithful']['final'][COLS.index('candidateA')] = 3
        elif kind == 'erased_intervening_loss':
            c = rows['ample_intervening_loss']
            c['milestones']['before_execution'] = c['milestones']['selected']
        elif kind == 'reset_ancestry': altered['ancestry']['scope_prefix']['final'][5] += 1
        try: inspect(altered)
        except AssertionError: mutations.append(kind)
        else: raise AssertionError(('undetected corruption', kind))
    assert path.read_bytes() == raw and hashes == {p: I.sha(ROOT/p) for p in hashes}
    receipt = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(), **result,
        detected_mutations=mutations, producer_result_sha256=I.sha(path), checker_sha256=I.sha(Path(__file__)),
        helper_hashes={str((HERE/p).relative_to(ROOT)): I.sha(HERE/p)
            for p in ('scope_independent_check.py', 'criterion_independent_check.py')},
        source_hashes=hashes, no_producer_transition_import=True,
        scope='Finite separate replay including complete ancestry; fixed unit channel family, transfer recipes, '
              'bounded protect-B policy and schedule remain supplied. No lived-concern or universal authority proof.')
    (HERE/'initiation-independent-check.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k: v for k, v in receipt.items() if k not in ('source_hashes', 'helper_hashes')}, indent=2))


if __name__ == '__main__': main()
