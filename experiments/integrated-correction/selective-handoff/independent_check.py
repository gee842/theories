"""Prospective artifact audit. No participant calls; never runs analyze.main.

Rules are parsed from the displayed historical packet, audited against the
original named-field reports, and applied to the current displayed evidence.
Neither prepare nor analyze is imported. Only analyze.parsed's isolated AST is
executed as the parser under test; no response files or results are created.
"""
from pathlib import Path
import ast
import copy
import hashlib
import itertools
import json
import random
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT / 'sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages'
ORDINARY = 'Assess the supplied materials carefully and answer the current target cases accurately.'
BOUNDARY = ORDINARY + (' Check the setting and episode of evidence before using it; '
                      'retain an inherited correction where supported, revise it when '
                      'defeated, and preserve uncertainty where the evidence does not decide.')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(test, message):
    if not test:
        raise AssertionError(message)


def table(text, prefix):
    out = []
    for line in text.splitlines():
        if re.match(prefix + r'\d\d \|', line):
            parts = [x.strip() for x in line.split('|')]
            out.append((parts[0], [int(x) for x in parts[1:]]))
    return out


def packet_rule(packet):
    """Read the four documented grammar forms; do not read hidden condition IDs."""
    m = re.search(r'route = (\w+) XOR ([^.]+)\.', packet)
    if m:
        base, expression = m.groups()
        expression = re.sub(r'[\[\]()]', '', expression)
        terms = []
        for part in expression.split(' AND '):
            t = re.fullmatch(r'(\w+)(?:=([01]))?', part.strip())
            require(t is not None, 'packet exception syntax')
            terms.append((t[1], int(t[2]) if t[2] else 1))
    else:
        m = re.search(r'route equals (\w+), except invert it when (\w+)=([01]) AND (\w+)=([01])\.', packet)
        require(m is not None, 'packet prose syntax')
        base = m[1]
        terms = [(m[2], int(m[3])), (m[4], int(m[5]))]
    require(len(terms) == 2 and len({x[0] for x in terms}) == 2, 'two distinct exception fields')
    require(base not in dict(terms), 'exception excludes base field')
    return base, dict(terms)


def answer(values, base, terms=None):
    bit = values[base]
    return 1 - bit if terms and all(values[k] == v for k, v in terms.items()) else bit


def prompt_data(text):
    head, instruction = text.split('\nASSESSMENT INSTRUCTION\n')
    target = re.search(r'The target setting is (\w+), episode (\d+)\.', head)
    base = re.search(r'B, route equals (\w+); or P,', head)
    packet = head.split('ARCHIVED PACKET FROM ASTER EPISODE 0\n')[1].split('\nEND ARCHIVED PACKET')[0]
    obs = re.search(r'CURRENT AUDITED ROW\nsetting: (\w+); episode: (\d+)\nfields: (.+)\nvalues: (.+)\nverified route: ([01])\n', head)
    require(target is not None and base is not None and obs is not None, 'complete displayed task fields')
    fields = obs[3].split(', ')
    vals = [int(x) for x in obs[4].split(', ')]
    queries = table(head, 'T')
    header = head.split('TARGET CASES, ALL ASTER EPISODE 1\n')[1].splitlines()[0]
    require(header == 'case | ' + ' | '.join(fields), 'target and observation field order')
    require([x[0] for x in queries] == ['T%02d' % i for i in range(1, 9)], 'eight ordered target IDs')
    require(len(fields) == len(set(fields)) == len(vals) == 5, 'five distinct binary fields')
    require(all(len(row) == 5 and set(row) <= {0, 1} for _, row in queries), 'binary target rows')
    require(set(vals) <= {0, 1}, 'binary calibration row')
    return {'common': head, 'instruction': instruction, 'target': (target[1], int(target[2])),
            'base': base[1], 'packet': packet, 'fields': fields,
            'scope': (obs[1], int(obs[2])), 'observation': vals,
            'outcome': int(obs[5]), 'tests': [row for _, row in queries]}


def infer(data):
    base, terms = packet_rule(data['packet'])
    require(data['base'] == base, 'displayed candidate base matches packet')
    observation = dict(zip(data['fields'], data['observation']))
    hypotheses = [('B', None), ('P', terms)]
    if data['scope'] == data['target']:
        hypotheses = [(name, rule) for name, rule in hypotheses
                      if answer(observation, base, rule) == data['outcome']]
    require(hypotheses, 'nonempty compatible candidate set')
    outputs = []
    for row in data['tests']:
        possibilities = {answer(dict(zip(data['fields'], row)), base, rule) for _, rule in hypotheses}
        outputs.append(next(iter(possibilities)) if len(possibilities) == 1 else '?')
    return [name for name, _ in hypotheses], outputs


def audit(fixtures, trials, prompts, archived, source_bytes):
    checks = 0
    def ck(condition, message):
        nonlocal checks
        checks += 1
        require(condition, message)

    ck([f['id'] for f in fixtures] == ['L02', 'L06', 'L08', 'L12'], 'four selected fixture identities')
    ck(len(trials) == 24 and len({t['id'] for t in trials}) == 24, '24 unique trials')
    f_by_id = {f['id']: f for f in fixtures}
    archive_details = []
    for f in fixtures:
        a = archived[f['id']]
        private = a['private']
        packet = a['response']['packet']
        ck(f['packet'] == packet, 'exact decoded historical packet')
        ck(f['packet_utf8_sha256'] == sha(packet.encode('utf-8')), 'extracted packet digest')
        base, terms = packet_rule(packet)
        fields = private['fields']
        ck(f['fields'] == fields and f['base_field'] == base, 'fixture named field definitions')
        ck({e['field']: e['value'] for e in f['corrected_exception']} == terms, 'explicit comparator exception')
        ck(len(f['corrected_exception']) == 2, 'exception field count')
        for name, digest in f['source_files'].items():
            ck(name in source_bytes and sha(source_bytes[name]) == digest, 'original source digest')
        expected_sources = {str((ARCHIVE / f['id'] / name).relative_to(ROOT)) for name in
                            ['private.json', 'baseline-prompt.txt', 'maintenance-prompt.txt', 'maintenance-response.json']}
        ck(set(f['source_files']) == expected_sources, 'four declared archive files')

        baseline = table(a['baseline_prompt'], 'C')
        report_text = a['maintenance_prompt'].split('Here is the complete verified report:\n')[1].split('Your scored answers were')[0]
        report = table(report_text, 'C')
        ck(len(baseline) == len(report) == 8, 'original baseline and verified report size')
        ck([x[1] for x in baseline] == [x[1][:-1] for x in report], 'verified report repeats original baseline')
        for _, row in report:
            ck(answer(dict(zip(fields, row[:-1])), base, terms) == row[-1], 'packet rule fits original verified label')
        permitted = [None] + [dict(zip(pair, bits))
                             for pair in itertools.combinations([k for k in fields if k != base], 2)
                             for bits in itertools.product([0, 1], repeat=2)]
        fits = [rule for rule in permitted if all(answer(dict(zip(fields, row[:-1])), base, rule) == row[-1]
                                                for _, row in report)]
        ck(fits == [terms], 'original full report uniquely identifies decoded packet within historical family')
        order = private['order']
        ck(sorted(order) == list(range(5)), 'archive display permutation')
        shown_baseline = [tuple(row[k] for k in order) for row in private['baseline']]
        ck(shown_baseline == [tuple(x[1]) for x in baseline], 'private/public baseline join')
        all_internal = [tuple(int(x) for x in format(i, '05b')) for i in range(32)]
        rule_i, rule_j, bit_i, bit_j = private['truth']
        for row in all_internal:
            values = dict(zip(fields, [row[k] for k in order]))
            expected = 1 - row[0] if row[rule_i] == bit_i and row[rule_j] == bit_j else row[0]
            ck(answer(values, base, terms) == expected, 'named packet and internal truth agree over full domain')
        tests = [tuple(row) for row in f['tests']]
        ck(len(tests) == len(set(tests)) == 8, 'unique target tuples')
        ck(not set(tests).intersection(shown_baseline), 'targets exclude historical baseline')
        ck(tuple(f['calibration']) not in tests, 'targets exclude current calibration')
        ck(tuple(f['calibration']) in shown_baseline, 'current calibration sourced from historical baseline tuple')
        bv = [answer(dict(zip(fields, row)), base) for row in tests]
        pv = [answer(dict(zip(fields, row)), base, terms) for row in tests]
        ck(bv == f['base_labels'] and pv == f['packet_labels'], 'reconstructed displayed target labels')
        for distinguish in [False, True]:
            selected_bits = [b for b, p in zip(bv, pv) if (b != p) == distinguish]
            ck(sorted(selected_bits) == [0, 0, 1, 1], 'balanced common/distinguishing targets')
        pools = {(diff, bit): [] for diff in [True, False] for bit in [0, 1]}
        baseline_internal = {tuple(x) for x in private['baseline']}
        for row in all_internal:
            if row in baseline_internal:
                continue
            values = dict(zip(fields, [row[k] for k in order]))
            different = answer(values, base, terms) != answer(values, base)
            pools[(different, row[0])].append(row)
        canonical_test = [row for diff in [True, False] for bit in [0, 1] for row in pools[(diff, bit)][:2]]
        random.Random('selective-handoff-20261006-' + f['id']).shuffle(canonical_test)
        ck([[row[k] for k in order] for row in canonical_test] == f['tests'], 'prespecified balanced tuple selection and order')
        calibration_options = [row for row in all_internal if row in baseline_internal and
                               answer(dict(zip(fields, [row[k] for k in order])), base, terms) != row[0]]
        ck(f['calibration'] == [calibration_options[0][k] for k in order], 'prespecified diagnostic tuple')
        overlap = {}
        for name in ['service', 'test']:
            old = {tuple(row[k] for k in order) for row in private[name]}
            overlap[name] = len(set(tests) & old)
        archive_details.append({'fixture': f['id'], 'packet_rule': {'base': base, 'exception': terms},
                                'historical_candidates': len(permitted), 'compatible_candidates': len(fits),
                                'baseline_overlap': 0, 'prior_service_overlap': overlap['service'],
                                'prior_successor_test_overlap': overlap['test']})

    rows = []
    by_group = {}
    for position, t in enumerate(trials, 1):
        ck(t['dispatch_position'] == position, 'sequential dispatch positions')
        ck(t['fixture'] in f_by_id and t['arm'] in ['ordinary', 'boundary'] and t['state'] in ['confirm', 'defeat', 'foreign'], 'trial factor levels')
        ck(t['id'] == '-'.join([t['fixture'], t['state'], t['arm']]), 'trial identity')
        ck(t['prompt'] == 'prompts/' + t['id'] + '.txt', 'prompt identity')
        text = prompts[t['id']]
        ck(sha(text.encode('utf-8')) == t['prompt_sha256'], 'prompt digest')
        d = prompt_data(text)
        f = f_by_id[t['fixture']]
        ck(d['instruction'] == {'ordinary': ORDINARY, 'boundary': BOUNDARY}[t['arm']] + '\n', 'exact assigned instruction')
        ck(d['packet'] == f['packet'], 'prompt packet unchanged')
        ck(d['fields'] == f['fields'] and d['tests'] == f['tests'] and d['observation'] == f['calibration'], 'displayed observation and queries match fixture')
        ck(d['target'] == ('Aster', 1), 'target episode')
        ck('no presumption of persistence or change' in text and 'not a guarantee about episode 1' in text, 'common nonpersistence premises')
        ck('every current target rule consistent with the supplied information' in text, 'common warranted-output criterion')
        ck('Do not use tools, inspect files, browse, contact agents, or write files.' in text, 'participant access instruction')
        ck(t['id'] not in text and t['fixture'] not in text, 'no researcher identity in prompt')
        candidates, expected = infer(d)
        ck(expected == t['expected'], 'answer vector inferred only from visible evidence')
        state = {'P': 'confirm', 'B': 'defeat', 'BP': 'foreign'}[''.join(candidates)]
        ck(state == t['state'], 'researcher state matches independently inferred candidate set')
        ck(expected.count('?') == (4 if len(candidates) == 2 else 0), 'selective uncertainty count')
        by_group.setdefault((t['fixture'], t['state']), {})[t['arm']] = d
        rows.append({'id': t['id'], 'dispatch_position': position, 'compatible_candidates': candidates,
                     'independent_expected': expected, 'prompt_sha256': t['prompt_sha256']})
    ck(len(by_group) == 12, '12 matched prompt pairs')
    for arms in by_group.values():
        ck(set(arms) == {'ordinary', 'boundary'}, 'complete paired arms')
        ck(arms['ordinary']['common'] == arms['boundary']['common'], 'prompt pair differs only in final instruction')
    for fixture in f_by_id:
        c = by_group[(fixture, 'confirm')]['ordinary']
        d = by_group[(fixture, 'defeat')]['ordinary']
        u = by_group[(fixture, 'foreign')]['ordinary']
        ck(c['common'].replace('verified route: ' + str(c['outcome']), 'verified route: X') ==
           d['common'].replace('verified route: ' + str(d['outcome']), 'verified route: X'), 'confirm/defeat changes observation label alone')
        ck(d['common'].replace('setting: Aster;', 'setting: PLACE;') ==
           u['common'].replace('setting: Birch;', 'setting: PLACE;'), 'defeat/foreign changes observation scope alone')
    planned = ['-'.join([f['id'], state, arm]) for f in fixtures
               for state in ['confirm', 'defeat', 'foreign'] for arm in ['ordinary', 'boundary']]
    random.Random(20261006).shuffle(planned)
    ck(planned == [t['id'] for t in trials], 'frozen-seed dispatch shuffle')
    return {'assertions': checks, 'archive_details': archive_details, 'rows': rows}


def parser_checks():
    """Only the exact parser function is executed; analyze.main is never called."""
    tree = ast.parse((HERE / 'analyze.py').read_text())
    nodes = [x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == 'parsed']
    require(len(nodes) == 1, 'one parser under test')
    env = {'json': json}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), '<isolated parser under test>', 'exec'), env)
    parse = env['parsed']
    valid = [0, 1, '?', 1, 0, '?', 0, 1]
    cases = [('valid', json.dumps({'answers': valid}), valid),
             ('whitespace', '\n\t ' + json.dumps({'answers': valid}) + ' \r\n', valid)]
    for name, value in [('boolean', True), ('float', 1.0), ('numeric string', '1'), ('null', None),
                        ('out of range', 2), ('negative', -1), ('unknown string', 'unknown'), ('nested', [0])]:
        cases.append((name, json.dumps({'answers': [value] + valid[1:]}), None))
    payload = json.dumps({'answers': valid})
    cases += [('empty', '', None), ('fence', '```json\n' + payload + '\n```', None),
              ('extra text', payload + ' done', None), ('second JSON', payload + payload, None),
              ('extra key', json.dumps({'answers': valid, 'reason': 'x'}), None),
              ('missing key', '{}', None), ('top list', json.dumps(valid), None),
              ('short', json.dumps({'answers': valid[:-1]}), None),
              ('long', json.dumps({'answers': valid + [0]}), None),
              ('duplicate key', '{"answers":' + json.dumps(valid) + ',"answers":' + json.dumps(valid) + '}', None),
              ('escaped duplicate key', '{"answers":' + json.dumps(valid) + ',"\\u0061nswers":' + json.dumps(valid) + '}', None),
              ('NaN', '{"answers":[NaN,1,0,1,0,1,0,1]}', None)]
    for name, text, expected in cases:
        require(parse(text) == expected, 'strict parser case: ' + name)
    return {'tested_isolated_function': 'analyze.py:parsed', 'cases': [x[0] for x in cases],
            'analyze_main_executed': False}


def main():
    require(not list((HERE / 'responses').glob('*.txt')), 'preflight is before participant responses')
    require(not (HERE / 'results.json').exists(), 'no empirical results before preflight')
    fixtures = json.loads((HERE / 'fixtures.json').read_text())
    trials = json.loads((HERE / 'trials.json').read_text())
    prompts = {t['id']: (HERE / t['prompt']).read_text() for t in trials}
    archived, source_bytes = {}, {}
    selected = []
    for path in sorted(ARCHIVE.glob('L*/maintenance-response.json')):
        source_bytes[str(path.relative_to(ROOT))] = path.read_bytes()
        if json.loads(path.read_text()).get('packet'):
            selected.append(path.parent.name)
    require(selected[:4] == [f['id'] for f in fixtures], 'first four lexical nonempty archival packets')
    for f in fixtures:
        folder = ARCHIVE / f['id']
        for name in ['private.json', 'baseline-prompt.txt', 'maintenance-prompt.txt', 'maintenance-response.json']:
            source_bytes[str((folder / name).relative_to(ROOT))] = (folder / name).read_bytes()
        archived[f['id']] = {'private': json.loads((folder / 'private.json').read_text()),
                             'response': json.loads((folder / 'maintenance-response.json').read_text()),
                             'baseline_prompt': (folder / 'baseline-prompt.txt').read_text(),
                             'maintenance_prompt': (folder / 'maintenance-prompt.txt').read_text()}
    result = audit(fixtures, trials, prompts, archived, source_bytes)
    rejected = []
    def mutation(name, change):
        fs, ts, ps = copy.deepcopy(fixtures), copy.deepcopy(trials), copy.deepcopy(prompts)
        change(fs, ts, ps)
        try:
            audit(fs, ts, ps, archived, source_bytes)
        except (AssertionError, ValueError, KeyError):
            rejected.append(name)
        else:
            raise AssertionError('checker accepted mutation: ' + name)
    mutation('missing trial', lambda f, t, p: t.pop())
    mutation('wrong expected vector', lambda f, t, p: t[0]['expected'].__setitem__(0, '?'))
    mutation('changed inherited packet', lambda f, t, p: f[0].__setitem__('packet', f[0]['packet'] + ' altered'))
    mutation('wrong exception field value', lambda f, t, p: f[0]['corrected_exception'][0].__setitem__('value', 1 - f[0]['corrected_exception'][0]['value']))
    mutation('target leaks calibration', lambda f, t, p: f[0]['tests'].__setitem__(0, f[0]['calibration']))
    mutation('changed source digest', lambda f, t, p: f[0]['source_files'].__setitem__(next(iter(f[0]['source_files'])), '0' * 64))
    def change_scope(fs, ts, ps):
        t = next(t for t in ts if t['state'] == 'foreign')
        ps[t['id']] = ps[t['id']].replace('setting: Birch;', 'setting: Aster;')
        t['prompt_sha256'] = sha(ps[t['id']].encode())
    mutation('scope corrupted with recomputed hash', change_scope)
    def change_arm(fs, ts, ps):
        t = next(t for t in ts if t['arm'] == 'ordinary')
        ps[t['id']] = ps[t['id']].replace(ORDINARY, BOUNDARY)
        t['prompt_sha256'] = sha(ps[t['id']].encode())
    mutation('arm changed with recomputed hash', change_arm)
    mutation('dispatch position changed', lambda f, t, p: t[0].__setitem__('dispatch_position', 2))
    dispatch = json.loads((HERE / 'dispatch-plan.json').read_text())
    require(len(dispatch) == 24, '24 exact dispatch records')
    for position, (record, trial) in enumerate(zip(dispatch, trials), 1):
        require(set(record) == {'trial_id', 'arguments'}, 'dispatch record fields')
        require(record['trial_id'] == trial['id'], 'dispatch order joins trial identity')
        require(record['arguments'] == {'task_name': 'reuse%02d' % position,
                                       'fork_turns': 'none', 'message': prompts[trial['id']]},
                'exact inline prompt, neutral unique name, no history/model overrides')
    paths = ['PROTOCOL.md', 'prepare.py', 'analyze.py', 'fixtures.json', 'trials.json',
             'dispatch-plan.json', 'independent_check.py', 'development/PREPARATION.md'] + [t['prompt'] for t in trials]
    result.update({'status': 'passed_pre_dispatch_core_audit', 'participant_calls': 0,
                   'participant_outputs_examined': 0, 'contexts': len(trials), 'answer_slots': 8 * len(trials),
                   'paired_prompts': 12, 'donor_blocks': 4, 'faults_rejected': rejected,
                   'dispatch_plan': {'records': 24, 'neutral_names': 'reuse01 through reuse24',
                                     'exact_arguments_verified': True, 'dispatch_performed': False},
                   'parser_checks': parser_checks(),
                   'method': 'Independent displayed-prompt and named-packet reconstruction; no prepare/analyze import or analyze.main execution.',
                   'files_sha256': {name: sha((HERE / name).read_bytes()) for name in paths},
                   'source_sha256': {name: sha(data) for name, data in sorted(source_bytes.items())},
                   'scope': 'Prospective fixture/parser validation. No empirical success estimate or platform isolation certification.'})
    (HERE / 'preflight.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'assertions', 'contexts', 'answer_slots', 'paired_prompts', 'donor_blocks', 'faults_rejected']}))


if __name__ == '__main__':
    main()
