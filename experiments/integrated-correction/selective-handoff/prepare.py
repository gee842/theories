"""Prepare a fixed, small selective reuse probe. Never calls a model."""
from pathlib import Path
import hashlib
import itertools
import json
import random

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / 'sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dump(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def label(row, rule):
    a, b, av, bv = rule
    return row[0] ^ int(row[a] == av and row[b] == bv)

def main():
    assert not list((HERE / 'responses').glob('*.txt')), 'Do not overwrite a run after responses'
    selected = []
    for d in sorted(SOURCE.iterdir()):
        p = d / 'maintenance-response.json'
        if p.is_file() and json.loads(p.read_text()).get('packet'):
            selected.append(d)
    selected = selected[:4]
    assert [d.name for d in selected] == ['L02', 'L06', 'L08', 'L12']
    fixtures, trials = [], []
    ordinary = 'Assess the supplied materials carefully and answer the current target cases accurately.'
    boundary = ('Assess the supplied materials carefully and answer the current target cases accurately. '
                'Check the setting and episode of evidence before using it; retain an inherited correction '
                'where supported, revise it when defeated, and preserve uncertainty where the evidence does not decide.')
    for d in selected:
        private = json.loads((d / 'private.json').read_text())
        packet = json.loads((d / 'maintenance-response.json').read_text())['packet']
        rule, order, fields = private['truth'], private['order'], private['fields']
        universe = list(itertools.product([0, 1], repeat=5))
        used = {tuple(r) for r in private['baseline']}
        exception = [r for r in universe if label(r, rule) != r[0] and r not in used]
        regular = [r for r in universe if label(r, rule) == r[0] and r not in used]
        calibration = next(r for r in universe if label(r, rule) != r[0] and r in used)
        test = [r for group in [exception, regular] for bit in [0, 1]
                for r in [r for r in group if r[0] == bit][:2]]
        assert len(test) == len(set(test)) == 8
        assert calibration not in test
        rng = random.Random('selective-handoff-20261006-' + d.name)
        rng.shuffle(test)
        def shown(row):
            return [row[k] for k in order]
        base = fields[order.index(0)]
        fixture = {'id': d.name, 'fields': fields, 'base_field': base,
                   'corrected_exception': [{'field': fields[order.index(rule[0])], 'value': rule[2]},
                                           {'field': fields[order.index(rule[1])], 'value': rule[3]}],
                   'source_files': {str((d / n).relative_to(ROOT)): digest(d / n) for n in
                                    ['private.json', 'baseline-prompt.txt', 'maintenance-prompt.txt', 'maintenance-response.json']},
                   'packet': packet, 'packet_utf8_sha256': hashlib.sha256(packet.encode()).hexdigest(),
                   'calibration': shown(calibration), 'tests': [shown(r) for r in test],
                   'base_labels': [r[0] for r in test], 'packet_labels': [label(r, rule) for r in test]}
        fixtures.append(fixture)
        for state in ['confirm', 'defeat', 'foreign']:
            setting = 'Aster' if state != 'foreign' else 'Birch'
            outcome = label(calibration, rule) if state == 'confirm' else calibration[0]
            expected = (fixture['packet_labels'] if state == 'confirm' else fixture['base_labels'] if state == 'defeat' else
                        [a if a == b else '?' for a, b in zip(fixture['packet_labels'], fixture['base_labels'])])
            table = 'case | ' + ' | '.join(fields) + '\n'
            table += '\n'.join('T%02d | ' % (i + 1) + ' | '.join(map(str, shown(r))) for i, r in enumerate(test))
            common = f'''This is a benign synthetic routing assessment. Work only from this message. Do not use tools, inspect files, browse, contact agents, or write files. Return your final answer directly. Do not discuss the study design.

TASK
All five fields are binary. The target setting is Aster, episode 1. Throughout each setting and episode there is one deterministic rule. Different settings and different episodes may have different rules; there is no presumption of persistence or change.
Exactly two rules are allowed in the current target: B, route equals {base}; or P, the corrected rule described in the archived packet below. These are the entire candidate family. The packet was correct for Aster, episode 0. Its statements about future cases were written in that historical episode and are not a guarantee about episode 1. The following audited row is exact for its labeled setting and episode. No other current observations or cross-setting equivalence are supplied.

ARCHIVED PACKET FROM ASTER EPISODE 0
{packet}
END ARCHIVED PACKET

CURRENT AUDITED ROW
setting: {setting}; episode: 1
fields: {', '.join(fields)}
values: {', '.join(map(str, shown(calibration)))}
verified route: {outcome}

TARGET CASES, ALL ASTER EPISODE 1
{table}

OUTPUT CONTRACT
For each target case, return 0 or 1 only if every current target rule consistent with the supplied information gives that route. Otherwise return "?". This is a warranted-output task: guessing a hidden true rule is not requested. Return only JSON in this shape: {{"answers":[eight entries, each 0, 1, or "?"]}}.

ASSESSMENT INSTRUCTION
'''
            for arm, instruction in [('ordinary', ordinary), ('boundary', boundary)]:
                tid = d.name + '-' + state + '-' + arm
                prompt = common + instruction + '\n'
                path = HERE / 'prompts' / (tid + '.txt')
                path.write_text(prompt)
                trials.append({'id': tid, 'fixture': d.name, 'state': state, 'arm': arm,
                               'prompt': str(path.relative_to(HERE)), 'prompt_sha256': digest(path), 'expected': expected})
    random.Random(20261006).shuffle(trials)
    for i, trial in enumerate(trials):
        trial['dispatch_position'] = i + 1
    dump('fixtures.json', fixtures)
    dump('trials.json', trials)
    print(json.dumps({'contexts': len(trials), 'decisions_per_context': 8, 'selected_donors': [d.name for d in selected]}))

if __name__ == '__main__':
    main()
