"""Frozen deterministic scoring; observed model replies are separate input files."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent

def parsed(text):
    try:
        def unique_pairs(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError('duplicate key')
                result[key] = value
            return result
        value = json.loads(text, object_pairs_hook=unique_pairs)
        assert isinstance(value, dict) and set(value) == {'answers'}
        answers = value['answers']
        assert isinstance(answers, list) and len(answers) == 8
        assert all((type(x) is int and x in (0, 1)) or (type(x) is str and x == '?') for x in answers)
        return answers
    except (ValueError, AssertionError, TypeError):
        return None

def main():
    trials = json.loads((HERE / 'trials.json').read_text())
    fixtures = {f['id']: f for f in json.loads((HERE / 'fixtures.json').read_text())}
    rows, baseline = [], []
    for t in trials:
        p = HERE / 'responses' / (t['id'] + '.txt')
        present = p.is_file()
        answer = parsed(p.read_text()) if present else None
        f = fixtures[t['fixture']]
        mask = [a != b for a, b in zip(f['base_labels'], f['packet_labels'])]
        correct = [int(a == b) for a, b in zip(answer, t['expected'])] if answer is not None else [0] * 8
        rows.append({'id': t['id'], 'fixture': t['fixture'], 'arm': t['arm'], 'state': t['state'],
                     'present': present, 'valid': answer is not None, 'answers': answer,
                     'response_sha256': hashlib.sha256(p.read_bytes()).hexdigest() if present else None,
                     'entry_correct': sum(correct), 'complete_correct': int(sum(correct) == 8),
                     'distinguishing_correct': sum(c for c, m in zip(correct, mask) if m),
                     'common_correct': sum(c for c, m in zip(correct, mask) if not m)})
        # Finite candidate elimination uses setting/episode identity before labels.
        prompt = (HERE / t['prompt']).read_text()
        match = re.search(r'CURRENT AUDITED ROW\nsetting: (\w+); episode: (\d+)\nfields: (.+)\nvalues: (.+)\nverified route: ([01])', prompt)
        setting, episode, fields, values, observed = match.groups()
        observation = dict(zip(fields.split(', '), map(int, values.split(', '))))
        b = observation[f['base_field']]
        p = b ^ int(all(observation[e['field']] == e['value'] for e in f['corrected_exception']))
        candidates = [f['base_labels'], f['packet_labels']]
        if setting == 'Aster' and episode == '1':
            candidates = [labels for labels, predicted in zip(candidates, [b, p]) if predicted == int(observed)]
        assert candidates
        conventional = [v[0] if all(x == v[0] for x in v) else '?' for v in zip(*candidates)]
        assert conventional == t['expected']
        for name, predictions in [('finite_candidates', conventional), ('packet_copy', f['packet_labels']),
                                  ('base_copy', f['base_labels']), ('abstain_all', ['?'] * 8)]:
            n = sum(a == b for a, b in zip(predictions, t['expected']))
            baseline.append({'id': t['id'], 'state': t['state'], 'comparator': name,
                             'entry_correct': n, 'complete_correct': int(n == 8)})
    summaries = []
    for arm in ['ordinary', 'boundary']:
        for state in ['confirm', 'defeat', 'foreign']:
            r = [x for x in rows if x['arm'] == arm and x['state'] == state]
            summaries.append({'arm': arm, 'state': state, 'planned_contexts': len(r),
                              'present': sum(x['present'] for x in r), 'valid': sum(x['valid'] for x in r),
                              'complete_correct': sum(x['complete_correct'] for x in r),
                              'entries_correct': sum(x['entry_correct'] for x in r), 'planned_entries': 8 * len(r)})
    joint = {arm: sum(all(x['complete_correct'] for x in rows if x['fixture'] == f and x['arm'] == arm)
                     for f in fixtures) for arm in ['ordinary', 'boundary']}
    result = {'status': 'complete' if all(x['present'] for x in rows) else 'incomplete',
              'contexts': len(rows), 'present': sum(x['present'] for x in rows),
              'summaries': summaries, 'fixtures_passing_all_three': joint,
              'rows': rows, 'deterministic_comparators': baseline}
    (HERE / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['rows', 'deterministic_comparators']}))

if __name__ == '__main__':
    main()
