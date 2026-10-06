"""Independent completed-run audit; never imports/runs the experiment producer.

Uses only saved inputs/responses and a reviewer-recorded live-agent snapshot.
No model calls. No changes to the frozen protocol, prompts, checker or scorer.
"""
from pathlib import Path
import copy
from datetime import datetime
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def load(name):
    return json.loads((HERE / name).read_text())


def response_parse(raw):
    """Independent strict implementation of the frozen response schema."""
    def pairs(items):
        names = [k for k, _ in items]
        if len(set(names)) != len(names):
            raise ValueError('duplicate object key')
        return dict(items)
    try:
        obj = json.loads(raw.decode('utf-8'), object_pairs_hook=pairs)
    except (UnicodeDecodeError, ValueError, TypeError):
        return None
    if type(obj) is not dict or list(obj) != ['answers']:
        return None
    entries = obj['answers']
    if type(entries) is not list or len(entries) != 8:
        return None
    for v in entries:
        if type(v) is int and v in [0, 1]:
            continue
        if type(v) is str and v == '?':
            continue
        return None
    return entries


def visible_oracle(prompt):
    """Current conclusions follow from displayed data, not hidden trial state."""
    packet = prompt.split('ARCHIVED PACKET FROM ASTER EPISODE 0\n')[1].split('\nEND ARCHIVED PACKET')[0]
    m = re.search(r'route = (\w+) XOR ([^.]+)\.', packet)
    if m:
        base, expression = m.groups()
        terms = []
        for text in re.sub(r'[\[\]()]', '', expression).split(' AND '):
            part = re.fullmatch(r'(\w+)(?:=([01]))?', text.strip())
            need(part is not None, 'packet exception grammar')
            terms.append((part[1], int(part[2]) if part[2] is not None else 1))
    else:
        m = re.search(r'route equals (\w+), except invert it when (\w+)=([01]) AND (\w+)=([01])\.', packet)
        need(m is not None, 'packet prose grammar')
        base, terms = m[1], [(m[2], int(m[3])), (m[4], int(m[5]))]
    target = re.search(r'The target setting is (\w+), episode (\d+)\.', prompt).groups()
    observation = re.search(r'CURRENT AUDITED ROW\nsetting: (\w+); episode: (\d+)\nfields: (.+)\nvalues: (.+)\nverified route: ([01])', prompt)
    scope = observation[1], observation[2]
    fields = observation[3].split(', ')
    measured = dict(zip(fields, map(int, observation[4].split(', '))))
    rows = []
    for line in prompt.splitlines():
        if re.match(r'T\d\d \|', line):
            parts = line.split(' | ')
            rows.append(dict(zip(fields, map(int, parts[1:]))))
    need(len(rows) == 8, 'eight displayed queries')
    def route(values, correction):
        value = values[base]
        if correction and all(values[name] == bit for name, bit in terms):
            value = 1 - value
        return value
    permitted = [False, True]
    if scope == target:
        permitted = [x for x in permitted if route(measured, x) == int(observation[5])]
    need(permitted, 'compatible candidate family not empty')
    expected = []
    for values in rows:
        values_set = {route(values, hypothesis) for hypothesis in permitted}
        expected.append(values_set.pop() if len(values_set) == 1 else '?')
    return {'expected': expected, 'base': [route(x, False) for x in rows],
            'packet': [route(x, True) for x in rows],
            'candidates': ['P' if v else 'B' for v in permitted]}


def reconstruct(trials, payloads):
    rows, baselines, oracles = [], [], []
    for t in trials:
        oracle = visible_oracle((HERE / t['prompt']).read_text())
        need(oracle['expected'] == t['expected'], 'trial oracle agrees with displayed evidence')
        raw = payloads.get(t['id'])
        answer = response_parse(raw) if raw is not None else None
        successes = [int(a == b) for a, b in zip(answer, oracle['expected'])] if answer is not None else [0] * 8
        different = [x != y for x, y in zip(oracle['base'], oracle['packet'])]
        rows.append({'id': t['id'], 'fixture': t['fixture'], 'arm': t['arm'], 'state': t['state'],
                     'present': raw is not None, 'valid': answer is not None, 'answers': answer,
                     'response_sha256': sha(raw) if raw is not None else None,
                     'entry_correct': sum(successes), 'complete_correct': int(all(successes)),
                     'distinguishing_correct': sum(x for x, flag in zip(successes, different) if flag),
                     'common_correct': sum(x for x, flag in zip(successes, different) if not flag)})
        for name, predictions in [('finite_candidates', oracle['expected']), ('packet_copy', oracle['packet']),
                                  ('base_copy', oracle['base']), ('abstain_all', ['?'] * 8)]:
            hits = sum(x == y for x, y in zip(predictions, oracle['expected']))
            baselines.append({'id': t['id'], 'state': t['state'], 'comparator': name,
                              'entry_correct': hits, 'complete_correct': int(hits == 8)})
        oracles.append({'id': t['id'], **oracle})
    summaries = []
    for arm in ['ordinary', 'boundary']:
        for state in ['confirm', 'defeat', 'foreign']:
            group = [r for r in rows if (r['arm'], r['state']) == (arm, state)]
            summaries.append({'arm': arm, 'state': state, 'planned_contexts': len(group),
                              'present': sum(x['present'] for x in group), 'valid': sum(x['valid'] for x in group),
                              'complete_correct': sum(x['complete_correct'] for x in group),
                              'entries_correct': sum(x['entry_correct'] for x in group), 'planned_entries': len(group) * 8})
    joint = {}
    for arm in ['ordinary', 'boundary']:
        successes = 0
        for fixture in sorted({r['fixture'] for r in rows}):
            group = [r for r in rows if r['arm'] == arm and r['fixture'] == fixture]
            need(len(group) == 3 and {r['state'] for r in group} == {'confirm', 'defeat', 'foreign'}, 'complete donor/state cohort')
            successes += int(all(r['complete_correct'] for r in group))
        joint[arm] = successes
    result = {'status': 'complete' if all(x['present'] for x in rows) else 'incomplete',
              'contexts': len(rows), 'present': sum(x['present'] for x in rows),
              'summaries': summaries, 'fixtures_passing_all_three': joint,
              'rows': rows, 'deterministic_comparators': baselines}
    return result, oracles


def compare(actual, expected):
    """Count every exact scalar/list/dict comparison, rejecting extras as well."""
    count = 1
    need(type(actual) is type(expected), 'result value types')
    if isinstance(expected, dict):
        need(set(actual) == set(expected), 'result dictionary fields')
        for k in expected:
            count += compare(actual[k], expected[k])
    elif isinstance(expected, list):
        need(len(actual) == len(expected), 'result list length')
        for a, b in zip(actual, expected):
            count += compare(a, b)
    else:
        need(actual == expected, 'result scalar equality')
    return count


def runtime_check(freeze):
    """Inspect only the 24 specified source lines; never decrypt protected text."""
    metadata = load('runtime-dispatch-metadata.json')
    records = metadata['records']
    need(len(records) == 24, '24 runtime projection records')
    requested = {r['source_line']: r for r in records}
    need(len(requested) == 24, 'distinct selected runtime source lines')
    read_records = {}
    with open(metadata['source_path'], 'rb') as stream:
        for lineno, raw in enumerate(stream, 1):
            if lineno in requested:
                r = requested[lineno]
                need(sha(raw) == r['source_line_sha256'], 'exact selected runtime line hash')
                event = json.loads(raw)
                payload = event['payload']
                need(event['type'] == 'response_item' and payload['type'] == 'function_call', 'actual recorded function call')
                need(payload['namespace'] == 'collaboration' and payload['name'] == 'spawn_agent', 'actual recorded spawn function')
                arguments = json.loads(payload['arguments'])
                projection = {'source_line': lineno, 'source_line_sha256': sha(raw),
                              'timestamp': event['timestamp'], 'ordinal': event['ordinal'],
                              'call_id': payload['call_id'], 'task_name': arguments['task_name'],
                              'fork_turns': arguments['fork_turns'], 'model_override': arguments.get('model'),
                              'reasoning_effort_override': arguments.get('reasoning_effort'),
                              'logged_message_is_protected': arguments['message'].startswith('gAAAA'),
                              'logged_message_sha256': sha(arguments['message'].encode('utf-8'))}
                need(projection == r, 'runtime metadata projection matches source line')
                need(set(arguments) == {'task_name', 'fork_turns', 'message'}, 'runtime argument fields omit overrides')
                need(datetime.fromisoformat(event['timestamp']) >= datetime.fromisoformat(freeze['frozen_at_utc']), 'actual runtime event after local freeze')
                read_records[lineno] = projection
            if lineno >= max(requested):
                break
    need(set(read_records) == set(requested), 'all selected runtime lines found')
    ordered = [read_records[n] for n in sorted(read_records)]
    need(ordered == records, 'projection order is source event order')
    need([r['task_name'] for r in ordered] == ['reuse%02d' % i for i in range(1, 25)], 'runtime neutral name/order mapping')
    need(all(r['fork_turns'] == 'none' and r['logged_message_is_protected'] for r in ordered), 'fork-none and protected-message metadata')
    return {'source_lines_verified': 24, 'first_event_timestamp': ordered[0]['timestamp'],
            'last_event_timestamp': ordered[-1]['timestamp'], 'decryption_attempted': False,
            'scope': 'Selected local runtime spawn metadata only. Prompt plaintext and responses are not authenticated by these protected fields. No unrelated session contents were parsed or copied; absence of extra calls outside the selected lines was not independently audited.'}


def main():
    trials, plan, records = load('trials.json'), load('dispatch-plan.json'), load('dispatch-record.json')
    freeze, preflight = load('FREEZE.json'), load('preflight.json')
    need(freeze['status'] == 'pre_dispatch' and freeze['participant_contexts_created'] == 0, 'local freeze claim')
    for name, expected_hash in freeze['files'].items():
        need(sha((ROOT / name).read_bytes()) == expected_hash, 'unchanged frozen input: ' + name)
    for name, expected_hash in preflight['files_sha256'].items():
        need(sha((HERE / name).read_bytes()) == expected_hash, 'unchanged preflight input: ' + name)
    for name, expected_hash in preflight['source_sha256'].items():
        need(sha((ROOT / name).read_bytes()) == expected_hash, 'unchanged archival source: ' + name)
    need(len(trials) == len(plan) == len(records) == 24, '24 trial/plan/dispatch joins')
    need(len({t['id'] for t in trials}) == 24, 'unique trials')
    need({p.stem for p in (HERE / 'responses').glob('*.txt')} == {t['id'] for t in trials}, 'exact response file set')
    preflight_rows = {r['id']: r for r in preflight['rows']}
    for i, (trial, dispatch, record) in enumerate(zip(trials, plan, records), 1):
        need(trial['dispatch_position'] == record['position'] == i, 'dispatch position join')
        need(trial['id'] == dispatch['trial_id'] == record['trial_id'], 'dispatch trial join')
        prompt = (HERE / trial['prompt']).read_bytes()
        need(sha(prompt) == trial['prompt_sha256'] == preflight_rows[trial['id']]['prompt_sha256'], 'unchanged prompt bytes')
        need(dispatch['arguments'] == {'task_name': 'reuse%02d' % i, 'fork_turns': 'none', 'message': prompt.decode('utf-8')}, 'exact declared dispatch arguments')
        need(record['returned_task_name'] == '/root/reuse%02d' % i, 'transcribed canonical agent identity')
        need(record['arguments_source'] == 'dispatch-plan.json', 'declared argument source')
        need(datetime.fromisoformat(record['recorded_at_utc']) >= datetime.fromisoformat(freeze['frozen_at_utc']), 'record time follows local freeze')
    payloads = {t['id']: (HERE / 'responses' / (t['id'] + '.txt')).read_bytes() for t in trials}
    expected, oracles = reconstruct(trials, payloads)
    comparisons = compare(load('results.json'), expected)
    for row in oracles:
        need(row['expected'] == preflight_rows[row['id']]['independent_expected'], 'post-run independent oracle agrees with pre-dispatch audit')

    snapshot = load('reviewer-agent-snapshot.json')
    matched_tool_finals = []
    for agent, final in snapshot['final_texts'].items():
        record = next(r for r in records if r['returned_task_name'] == agent)
        need(payloads[record['trial_id']] == final.encode('utf-8'), 'independently visible final exact bytes')
        matched_tool_finals.append({'agent': agent, 'trial_id': record['trial_id'], 'sha256': sha(final.encode('utf-8'))})

    rejected = []
    mutations = [
        ('wrong row accuracy', lambda x: x['rows'][0].__setitem__('entry_correct', 7)),
        ('wrong group total', lambda x: x['summaries'][0].__setitem__('complete_correct', 3)),
        ('wrong joint success', lambda x: x['fixtures_passing_all_three'].__setitem__('ordinary', 3)),
        ('wrong comparator score', lambda x: x['deterministic_comparators'][0].__setitem__('entry_correct', 7)),
        ('omitted response row', lambda x: x['rows'].pop()),
        ('false response identity', lambda x: x['rows'][0].__setitem__('response_sha256', '0' * 64)),
    ]
    for name, change in mutations:
        altered = copy.deepcopy(expected)
        change(altered)
        try:
            compare(altered, expected)
        except AssertionError:
            rejected.append(name)
        else:
            raise AssertionError('mutation accepted: ' + name)
    paired = []
    by_id = {r['id']: r for r in expected['rows']}
    for fixture in sorted({t['fixture'] for t in trials}):
        for state in ['confirm', 'defeat', 'foreign']:
            a = by_id[fixture + '-' + state + '-ordinary']
            b = by_id[fixture + '-' + state + '-boundary']
            paired.append({'fixture': fixture, 'state': state,
                           'boundary_minus_ordinary_complete': b['complete_correct'] - a['complete_correct'],
                           'boundary_minus_ordinary_entries': b['entry_correct'] - a['entry_correct']})
    runtime = runtime_check(freeze)
    bind = ['verify_results.py', 'reviewer-agent-snapshot.json', 'runtime-dispatch-metadata.json', 'FREEZE.json', 'preflight.json',
            'dispatch-record.json', 'RUN-NOTES.md', 'results.json'] + ['responses/' + t['id'] + '.txt' for t in trials]
    receipt = {'status': 'passed_independent_saved_run_audit', 'model_calls_by_reviewer': 0,
               'producer_imported_or_executed': False, 'frozen_files_verified': len(freeze['files']),
               'preflight_inputs_verified': len(preflight['files_sha256']),
               'archival_source_hashes_verified': len(preflight['source_sha256']),
               'exact_result_comparisons': comparisons, 'deliberate_corruptions_rejected': rejected,
               'contexts': 24, 'present': expected['present'], 'valid': sum(r['valid'] for r in expected['rows']),
               'complete_correct': sum(r['complete_correct'] for r in expected['rows']),
               'correct_entries': sum(r['entry_correct'] for r in expected['rows']), 'planned_entries': 192,
               'definite_entries': sum(type(v) is int for r in expected['rows'] for v in (r['answers'] or [])),
               'uncertainty_entries': sum(v == '?' for r in expected['rows'] for v in (r['answers'] or [])),
               'summaries': expected['summaries'], 'joint_success': expected['fixtures_passing_all_three'],
               'paired_differences': paired, 'independent_oracles': oracles,
               'direct_tool_final_matches': matched_tool_finals,
               'runtime_dispatch_metadata_check': runtime,
               'provenance_limit': snapshot['limitation'],
               'additional_limits': 'Freeze and dispatch history are local orchestrator records, not authenticated platform exports. No complete child tool traces, backend model revision or security isolation certification. Ceiling on selected finite cases shows no observed instruction benefit; not statistical equivalence or value acquisition.',
               'files_sha256': {name: sha((HERE / name).read_bytes()) for name in bind}}
    (HERE / 'results-review.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ['status', 'frozen_files_verified', 'exact_result_comparisons', 'contexts', 'valid', 'complete_correct', 'correct_entries', 'direct_tool_final_matches']}))


if __name__ == '__main__':
    main()
