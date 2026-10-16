"""Read-only record, preservation and integration checks; no scientific rerun."""
from pathlib import Path
from fractions import Fraction as Q
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
BASE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition'
OUTPUT = HERE / 'APPLICABILITY-REVALUATION-CHECKS.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchor(text):
    text = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def links(path, content):
    found = []
    for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        raw = raw.strip('<>')
        if urlsplit(raw).scheme:
            continue
        name, _, fragment = raw.partition('#')
        target = (path.parent / unquote(name)).resolve() if name else path
        exists = target.exists() or target == OUTPUT
        valid = True
        if exists and fragment and target.suffix == '.md':
            valid = unquote(fragment) in {
                anchor(h) for h in re.findall(r'^#{1,6} (.+)$', target.read_text(), re.M)
            }
        found.append({'document': str(path.relative_to(ROOT)), 'target': raw,
                      'exists': exists, 'fragment_ok': valid})
    return found


acquisition = json.loads((BASE / 'results.json').read_text())
access = json.loads((BASE / 'access/results.json').read_text())
bindings = []
for directory, data in [(BASE, acquisition), (BASE / 'access', access)]:
    for name, expected in data['source_hashes'].items():
        path = directory / name
        bindings.append({'file': str(path.relative_to(ROOT)), 'matches': digest(path) == expected})

ordinary = acquisition['cases']['primary_unary']
inverted = acquisition['cases']['inverted_sensor']
target = acquisition['primary_target']
checks = {}
checks['same_cycle_initial_and_transitions'] = (
    target['initial'] == inverted['model']['initial'] == 0
    and target['transitions'] == inverted['model']['transitions'] == [[1], [2], [0]])
checks['all_three_sensor_outputs_complement_raw'] = (
    inverted['model']['outputs'] == [x ^ 1 for x in target['outputs']])
checks['old_raw_target_audit_preserved'] = (
    inverted['analyst_model_exact'] is False and inverted['analyst_distinguishing_word'] == '')
checks['use_words_and_outcomes'] = (
    ordinary['use']['word'] == 'aaaaa' and ordinary['use']['success'] is True
    and inverted['use']['word'] == 'aaaaaa' and inverted['use']['success'] is False)
for name, record in [('ordinary', ordinary), ('inverted', inverted)]:
    use = record['use']
    checks[name + '_whole_resource_identity'] = (
        Q(record['spent']) + Q(use['fuel_after_return']) + use['source'] + use['wasted'] == 56)
    checks[name + '_retained_sensor_certificate'] = record['certified'] and record['retained']

first, second = [access['fixtures'][name] for name in ['primary_sensor_flip', 'readiness_change']]
checks['same_native_sensor_prefix'] = first['native_trace'][:-1] == second['native_trace'][:-1]
checks['opposite_final_probe'] = (
    first['native_trace'][-1] == {'command': 'probe', 'observation': 1}
    and second['native_trace'][-1] == {'command': 'probe', 'observation': 0})
for name in ['primary_sensor_flip', 'readiness_change', 'sensor_only_ambiguity']:
    record = access['fixtures'][name]
    checks[name + '_whole_resource_identity'] = (
        Q(record['starting_fuel']) + 10 == Q(record['spent']) + Q(record['fuel'])
        + record['source_remaining'] + record['wasted'])

edits = json.loads((HERE / 'APPLICABILITY-REVALUATION-EDITS.json').read_text())
insertions, local_links = [], []
for item in edits['changes']:
    path = ROOT / item['file']
    insertions.append({'file': item['file'], 'present': item['addition'] in path.read_text()})
    local_links.extend(links(path, item['addition']))
notes = sorted(HERE.glob('APPLICABILITY-REVALUATION-*.md'))
for path in notes:
    local_links.extend(links(path, path.read_text()))
passed = (all(x['matches'] for x in bindings) and all(checks.values())
          and all(x['present'] for x in insertions)
          and all(x['exists'] and x['fragment_ok'] for x in local_links))
report = {'status': 'passed' if passed else 'failed',
          'scope': 'Stored table correspondence, recorded accounts, original producer bindings, additive entries and local links. No learner import, experiment rerun, independent statistical reconstruction or universal ethical certification.',
          'source_bindings': bindings, 'record_checks': checks, 'insertions': insertions,
          'local_links': local_links, 'note_sha256': {p.name: digest(p) for p in notes},
          'results_sha256': {'acquisition': digest(BASE / 'results.json'),
                             'access': digest(BASE / 'access/results.json')},
          'checker_sha256': digest(Path(__file__))}
OUTPUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'status': report['status'], 'source_bindings': len(bindings),
                  'record_checks': len(checks), 'additions': len(insertions), 'links': len(local_links)}))
if not passed:
    raise SystemExit(1)
