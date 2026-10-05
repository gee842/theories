#!/usr/bin/env python3
"""Descriptive reanalysis of preserved logs. No model, tool, or embedded-code execution."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'sources/28-agentdojo-evidence-2026-10-06'
PIPELINES = {'baseline': 'gpt-4o-2024-05-13',
             'repeat': 'gpt-4o-2024-05-13-repeat_user_prompt'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':')).encode()).hexdigest()


def fraction(numerator, denominator):
    return str(Fraction(numerator, denominator)) if denominator else None


def boolean(value):
    return value if type(value) is bool else None


def binomial_counts(values):
    counts = Counter('true' if value is True else 'false' if value is False else 'unknown'
                     for value in values)
    return {'true': counts['true'], 'false': counts['false'], 'unknown': counts['unknown'],
            'known_denominator': counts['true'] + counts['false'],
            'true_fraction_among_known': fraction(counts['true'], counts['true'] + counts['false'])}


def parse_file(pipeline, user, injection):
    part = 'none/none' if injection is None else f'important_instructions/injection_task_{injection}'
    relative = f'runs/{PIPELINES[pipeline]}/banking/user_task_{user}/{part}.json'
    path = SOURCE / 'original' / relative
    raw = json.loads(path.read_text())
    assert raw['suite_name'] == 'banking'
    assert raw['pipeline_name'] == PIPELINES[pipeline]
    assert raw['user_task_id'] == f'user_task_{user}'
    assert raw['injection_task_id'] == (None if injection is None else f'injection_task_{injection}')
    assert raw['attack_type'] == (None if injection is None else 'important_instructions')
    messages = raw['messages']
    requests = [message.get('content') for message in messages if message['role'] == 'user']
    assert requests and isinstance(requests[0], str)
    calls = [call for message in messages for call in (message.get('tool_calls') or [])]
    tools = [message for message in messages if message['role'] == 'tool']
    validity_fields = {key: raw[key] for key in ('attack_is_valid', 'attack_validity', 'valid_attack') if key in raw}
    # No record field can be silently guessed from its absence or a current source comment.
    assert not validity_fields, ('Unexpected validity schema: review explicitly', relative)
    utility = boolean(raw.get('utility'))
    attack = boolean(raw.get('security')) if injection is not None else None
    return {
        'pipeline': pipeline, 'task': user, 'injection': injection,
        'case_key': f'u{user:02d}/' + ('clean' if injection is None else f'i{injection}'),
        'source': str(path.relative_to(ROOT)), 'source_sha256': sha(path),
        'request_sha256': digest(requests[0]), 'injections_sha256': digest(raw['injections']),
        'system_messages_sha256': digest([message.get('content') for message in messages if message['role'] == 'system']),
        'utility': utility, 'reported_attacker_success': attack,
        'reported_joint_task_success': None if injection is None or utility is None or attack is None else utility and not attack,
        'error_present': raw.get('error') is not None, 'error': raw.get('error'),
        'attack_validity': None, 'validity_status': 'not_recorded',
        'recorded_message_count': len(messages), 'recorded_user_messages': len(requests),
        'recorded_assistant_messages': sum(message['role'] == 'assistant' for message in messages),
        'recorded_tool_call_count': len(calls), 'recorded_tool_result_count': len(tools),
        'recorded_tool_error_count': sum(message.get('error') is not None for message in tools),
        'recorded_call_names': dict(sorted(Counter(call['function'] for call in calls).items())),
        'recorded_duration': raw.get('duration'),
    }


def summarize(rows, attacked):
    out = {'row_count': len(rows), 'recorded_errors': sum(row['error_present'] for row in rows),
        'utility': binomial_counts([row['utility'] for row in rows]),
        'recorded_tool_calls': sum(row['recorded_tool_call_count'] for row in rows),
        'recorded_tool_results': sum(row['recorded_tool_result_count'] for row in rows),
        'recorded_tool_errors': sum(row['recorded_tool_error_count'] for row in rows)}
    if attacked:
        joint = Counter('unknown' if row['utility'] is None or row['reported_attacker_success'] is None
            else f"u{int(row['utility'])}_a{int(row['reported_attacker_success'])}" for row in rows)
        out.update(reported_attacker_success=binomial_counts([row['reported_attacker_success'] for row in rows]),
            reported_joint_task_success=binomial_counts([row['reported_joint_task_success'] for row in rows]),
            joint={key: joint[key] for key in ('u0_a0', 'u0_a1', 'u1_a0', 'u1_a1', 'unknown')},
            attack_validity=binomial_counts([row['attack_validity'] for row in rows]))
    return out


def pair_summaries(pairs):
    out = {'pair_count': len(pairs)}
    for field in ('utility', 'reported_attacker_success', 'reported_joint_task_success'):
        available = [pair for pair in pairs if pair['baseline'][field] is not None and pair['repeat'][field] is not None]
        changes = Counter(f"{int(pair['baseline'][field])}->{int(pair['repeat'][field])}" for pair in available)
        total = sum(int(pair['repeat'][field]) - int(pair['baseline'][field]) for pair in available)
        out[field] = {'known_pairs': len(available), 'unknown_pairs': len(pairs) - len(available),
            'changes': {key: changes[key] for key in ('0->0', '0->1', '1->0', '1->1')},
            'repeat_minus_baseline_sum': total, 'repeat_minus_baseline_mean': fraction(total, len(available))}
    return out


def main():
    freeze = json.loads((HERE / 'protocol-freeze.json').read_text())
    assert sha(HERE / 'PROTOCOL.md') == freeze['sha256']
    manifest = json.loads((SOURCE / 'manifest.json').read_text())
    assert manifest['trajectory_files'] == 320
    for entry in manifest['files'] + manifest['metadata']:
        path = SOURCE / entry['path']
        assert path.stat().st_size == entry['bytes'] and sha(path) == entry['sha256'], path
    rows = [parse_file(pipeline, user, injection)
            for pipeline in PIPELINES for user in range(16) for injection in [None, *range(9)]]
    assert len(rows) == 320
    indexed = {(row['pipeline'], row['case_key']): row for row in rows}
    pairs = []
    for baseline in (row for row in rows if row['pipeline'] == 'baseline'):
        repeat = indexed['repeat', baseline['case_key']]
        pairs.append({'case_key': baseline['case_key'], 'task': baseline['task'], 'injection': baseline['injection'],
            'same_recorded_request': baseline['request_sha256'] == repeat['request_sha256'],
            'same_injection_payload': baseline['injections_sha256'] == repeat['injections_sha256'],
            'same_recorded_system_messages': baseline['system_messages_sha256'] == repeat['system_messages_sha256'],
            'both_without_recorded_error': not baseline['error_present'] and not repeat['error_present'],
            'baseline': {field: baseline[field] for field in ('utility', 'reported_attacker_success', 'reported_joint_task_success')},
            'repeat': {field: repeat[field] for field in ('utility', 'reported_attacker_success', 'reported_joint_task_success')}})
    attacked_pairs = [pair for pair in pairs if pair['injection'] is not None]
    clean_pairs = [pair for pair in pairs if pair['injection'] is None]
    summaries = {}
    for pipeline in PIPELINES:
        clean = [row for row in rows if row['pipeline'] == pipeline and row['injection'] is None]
        attacked = [row for row in rows if row['pipeline'] == pipeline and row['injection'] is not None]
        summaries[pipeline] = {'clean': summarize(clean, False), 'attacked_all_recorded_labels': summarize(attacked, True),
            'attacked_without_recorded_error': summarize([row for row in attacked if not row['error_present']], True),
            'attacked_recorded_valid_only': summarize([row for row in attacked if row['attack_validity'] is True], True)}
    matching = {'paired_cases': len(pairs), 'paired_attacked_cases': len(attacked_pairs),
        'request_mismatches': [pair['case_key'] for pair in pairs if not pair['same_recorded_request']],
        'payload_mismatches': [pair['case_key'] for pair in attacked_pairs if not pair['same_injection_payload']],
        'recorded_system_mismatches': [pair['case_key'] for pair in pairs if not pair['same_recorded_system_messages']],
        'common_recorded_valid_pairs': 0,
        'initial_environment_per_run_verified': False, 'paired_random_seeds_verified': False,
        'transient_model_input_completeness_verified': False}
    out = {'status': 'descriptive analysis of preserved labels; independent checking and effect replay separate',
        'commit': manifest['commit'], 'protocol_sha256': freeze['sha256'],
        'manifest_sha256': sha(SOURCE / 'manifest.json'), 'analysis_sha256': sha(Path(__file__)),
        'rows': rows, 'summaries': summaries, 'matching': matching,
        'paired_clean': pair_summaries(clean_pairs), 'paired_attacked': pair_summaries(attacked_pairs),
        'paired_same_recorded_input': pair_summaries([pair for pair in attacked_pairs
            if pair['same_recorded_request'] and pair['same_injection_payload']]),
        'paired_without_recorded_error': pair_summaries([pair for pair in attacked_pairs if pair['both_without_recorded_error']]),
        'task_level': {str(task): pair_summaries([pair for pair in attacked_pairs if pair['task'] == task]) for task in range(16)},
        'injection_level': {str(task): pair_summaries([pair for pair in attacked_pairs if pair['injection'] == task]) for task in range(9)},
        'leave_one_task_out': {str(task): pair_summaries([pair for pair in attacked_pairs if pair['task'] != task]) for task in range(16)},
        'leave_one_injection_out': {str(task): pair_summaries([pair for pair in attacked_pairs if pair['injection'] != task]) for task in range(9)},
        'validity_scope': 'No per-record validity result is saved. Valid-only estimates are unavailable, not zero attack success.',
        'interpretation': 'Security=true is the archived attacker-goal label, not automatically a verified unauthorized effect. Clean security placeholders are excluded. Descriptive paired task conditions are not randomized replicates or evidence of ethical concern.',
        'new_model_calls': 0, 'real_tool_actions': 0}
    (HERE / 'results.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'summaries': summaries, 'matching': matching, 'paired_attacked': out['paired_attacked']}, indent=2))


if __name__ == '__main__':
    main()
