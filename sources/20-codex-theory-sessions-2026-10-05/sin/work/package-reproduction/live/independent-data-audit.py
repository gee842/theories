"""Independent raw-data audit. Does not import the study generator or analyzer."""
import collections
import datetime
import hashlib
import itertools
import json
import pathlib
import random
import re

ROOT = pathlib.Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[1]
errors = []
checks = collections.Counter()

def read(path):
    return json.loads(path.read_text())

def check(condition, category, detail):
    checks[category] += 1
    if not condition:
        errors.append({'category': category, 'detail': detail})

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def correct_route(row, rule):
    if rule is None:
        return row[0]
    a, b, av, bv = rule
    return 1 - row[0] if row[a] == av and row[b] == bv else row[0]

def rows_in_prompt(text):
    return [[int(x.strip()) for x in line.split('|')[1:]]
            for line in text.splitlines() if re.match(r'^C\d\d \|', line)]

def displayed_rows(rows, fixture):
    return [[row[j] for j in fixture['order']] for row in rows]

def words(text):
    return len(text.split())

def validate_answers(obj, n, name, maintenance=False):
    expected = {'maintenance_slots', 'packet', 'answers', 'reason'} if maintenance else {'answers'}
    valid = (isinstance(obj, dict) and set(obj) == expected and
             isinstance(obj.get('answers'), list) and len(obj['answers']) == n and
             all(type(x) is int and x in (0, 1) for x in obj['answers']))
    check(valid, 'response_schema', name)
    if maintenance:
        check(type(obj.get('maintenance_slots')) is int and obj['maintenance_slots'] in (0, 1), 'slot_schema', name)
        check(isinstance(obj.get('packet'), str), 'packet_schema', name)
        check(isinstance(obj.get('reason'), str) and words(obj['reason']) <= 40, 'reason_schema', name)
        check((obj['maintenance_slots'] == 0 and obj['packet'] == '') or
              (obj['maintenance_slots'] == 1 and 0 < words(obj['packet']) <= 120), 'allocation_packet_consistency', name)

frozen = read(ROOT / 'FREEZE.json')
for rel, value in frozen['files'].items():
    check(sha(WORKSPACE / rel) == value, 'initial_frozen_hash', rel)
check(sha(ROOT / 'analyze.py') == read(ROOT / 'ANALYSIS-FREEZE.json')['sha256'], 'analysis_frozen_hash', 'analyze.py')
manifest = read(ROOT / 'design-manifest.json')
check(len(manifest) == 32 and len({m['id'] for m in manifest}) == 32, 'manifest_cardinality', '32 lineages')
for entry in manifest:
    base = ROOT / 'lineages' / entry['id']
    check(sha(base / 'private.json') == entry['private_sha256'], 'fixture_frozen_hash', entry['id'])
    check(sha(base / 'baseline-prompt.txt') == entry['prompt_sha256'], 'baseline_prompt_frozen_hash', entry['id'])
sf = read(ROOT / 'SUCCESSOR-FREEZE.json')
check(sha(ROOT / 'successor-assignments.json') == sf['successor_assignments_sha256'], 'successor_assignment_frozen_hash', 'assignment file')
for entry in sf['maintenance_responses']:
    check(sha(ROOT / 'lineages' / entry['id'] / 'maintenance-response.json') == entry['sha256'], 'maintenance_sealed_hash', entry['id'])
S = read(ROOT / 'successor-assignments.json')
check(len(S) == 64 and len({(s['id'], s['replica']) for s in S}) == 64, 'successor_cardinality', '64 seats')
seat_lookup = {(s['id'], s['replica']): s for s in S}
for s in S:
    check(sha(ROOT / 'lineages' / s['id'] / (s['replica'] + '-prompt.txt')) == s['prompt_sha256'], 'successor_prompt_frozen_hash', [s['id'], s['replica']])

A = read(ROOT / 'assignments.json')
blocks = read(ROOT / 'assignment-blocks.json')
fixtures = [read(ROOT / 'lineages' / m['id'] / 'private.json') for m in manifest]
byid = {d['id']: d for d in fixtures}
expected_blocks = [[d['id'] for d in fixtures if d['truth'] and tuple(d['truth'][:2]) == pair]
                   for pair in itertools.combinations(range(1, 5), 2)]
controls = [d['id'] for d in fixtures if d['truth'] is None]
expected_blocks.extend([controls[:4], controls[4:]])
check(blocks == expected_blocks, 'randomization_blocks', 'six pair blocks, two control blocks')
rng_a = random.Random(202610058691)
generated_a = {}
for block in blocks:
    selected = set(rng_a.sample(block, 2))
    generated_a.update({lid: int(lid in selected) for lid in block})
    check(sum(A[lid] for lid in block) == 2, 'A_balance', block)
check(generated_a == A, 'A_seed_reproduction', 'documented seed and two-of-four assignment')
rng_b = random.Random(202610059407)
for d in fixtures:
    b0 = rng_b.randrange(2)
    check(seat_lookup[d['id'], 'r0']['B'] == b0 and seat_lookup[d['id'], 'r1']['B'] == 1 - b0,
          'B_seed_reproduction_and_pairing', d['id'])

all_rules = [None] + [list(pair + vals) for pair in itertools.combinations(range(1, 5), 2)
                      for vals in itertools.product((0, 1), repeat=2)]
check(collections.Counter(tuple(d['truth']) for d in fixtures if d['truth']) ==
      collections.Counter(tuple(rule) for rule in all_rules[1:]), 'truth_coverage', 'all 24 exceptions exactly once')
check(len(controls) == 8, 'truth_coverage', 'eight unchanged controls')
baseline_snapshot = read(ROOT / 'baseline-snapshot.json')
data = []
generic = 'No lineage-specific packet is available. Use the common orientation and your own best judgment.'
maintenance_common = []
for d in fixtures:
    lid = d['id']; directory = ROOT / 'lineages' / lid
    baseline = read(directory / 'baseline-response.json')
    m = read(directory / 'maintenance-response.json')
    validate_answers(baseline, 8, lid + '/baseline')
    validate_answers(m, 4 - m['maintenance_slots'], lid + '/maintenance', True)
    check(baseline == baseline_snapshot[lid], 'baseline_snapshot_equality', lid)
    check(len(d['baseline']) == 8 and len({tuple(r[1:]) for r in d['baseline']}) == 8 and
          all(sum(r[1:]) % 2 == 0 for r in d['baseline']), 'baseline_even_parity', lid)
    check(len(d['test']) == 16 and len({tuple(r) for r in d['test']}) == 16 and
          all(sum(r[1:]) % 2 == 1 for r in d['test']), 'test_odd_parity', lid)
    check(not ({tuple(r) for r in d['baseline']} & {tuple(r) for r in d['test']}), 'test_report_novelty', lid)
    check(len(d['service']) == 4 and all(row in d['test'] for row in d['service']), 'service_test_overlap', lid)
    target_baseline = [correct_route(r, d['truth']) for r in d['baseline']]
    target_test = [correct_route(r, d['truth']) for r in d['test']]
    signatures = {tuple(correct_route(r, h) for r in d['baseline']) for h in all_rules}
    check(len(signatures) == 25, 'report_identifies_candidate_family', lid)
    matching = [h for h in all_rules if [correct_route(r, h) for r in d['baseline']] == target_baseline]
    check(len(matching) == 1 and matching[0] == d['truth'], 'classical_report_learner', lid)
    learned_correct = sum(correct_route(r, matching[0]) == truth for r, truth in zip(d['test'], target_test))
    check(learned_correct == 16, 'classical_successor_score', lid)

    bp = (directory / 'baseline-prompt.txt').read_text()
    mp = (directory / 'maintenance-prompt.txt').read_text()
    base_orientation = bp.split('\nRoute these eight current cases.')[0]
    check(mp.split('\nYour already-submitted baseline answers were ')[0] == base_orientation, 'common_founder_orientation', lid)
    legacy_name = re.search(r'inherited rule is: route equals field (\w+)\.', bp).group(1)
    check(legacy_name == d['fields'][d['order'].index(0)], 'public_legacy_mapping', lid)
    check(rows_in_prompt(bp) == displayed_rows(d['baseline'], d), 'baseline_public_rows', lid)
    check('verified route' not in bp and 'Your scored answers' not in bp, 'baseline_no_report', lid)
    submitted = re.search(r'already-submitted baseline answers were (\[.*?\])\.', mp).group(1)
    check(json.loads(submitted) == baseline['answers'], 'maintenance_actual_baseline', lid)
    tables = rows_in_prompt(mp)
    if A[lid]:
        expected = [row + [y] for row, y in zip(displayed_rows(d['baseline'], d), target_baseline)]
        expected += displayed_rows(d['service'], d)
        check(tables == expected, 'timely_verified_report_and_service', lid)
        score = sum(x == y for x, y in zip(baseline['answers'], target_baseline))
        check(f'You got {score}/8 correct.' in mp, 'timely_actual_score', lid)
    else:
        check(tables == displayed_rows(d['service'], d) and 'verified route' not in mp and 'You got ' not in mp,
              'delayed_no_labels_or_score', lid)
    maintenance_common.append(mp.split('You now have FOUR work slots.')[1].split('Ordinary cases:')[0])
    M = int(m['maintenance_slots'] == 1 and 0 < words(m['packet']) <= 120)
    outcomes = {}
    normalized_successors = []
    for replica in ('r0', 'r1'):
        s = seat_lookup[lid, replica]
        obj = read(directory / (replica + '-response.json'))
        validate_answers(obj, 16, lid + '/' + replica)
        sp = (directory / (replica + '-prompt.txt')).read_text()
        check(sp.split('\nHandoff material:')[0] == base_orientation, 'common_successor_orientation', [lid, replica])
        prefix, tail = sp.split('Handoff material:\n', 1)
        payload, suffix = tail.split('\n\nYou are a fresh successor.', 1)
        check(payload == (m['packet'] if M and s['B'] else generic), 'exact_assigned_payload', [lid, replica])
        check(s['packet_valid'] == bool(M), 'recorded_packet_validity', [lid, replica])
        check(rows_in_prompt(suffix) == displayed_rows(d['test'], d), 'successor_public_rows', [lid, replica])
        check('verified route' not in suffix, 'no_successor_test_labels', [lid, replica])
        normalized_successors.append(prefix + '<PAYLOAD>' + suffix)
        outcomes[s['B']] = sum(x == y for x, y in zip(obj['answers'], target_test))
    check(normalized_successors[0] == normalized_successors[1], 'paired_context_equal_except_payload', lid)
    current_correct = sum(x == correct_route(row, d['truth']) for x, row in zip(m['answers'], d['service']))
    data.append({'id': lid, 'stratum': d['stratum'], 'A': A[lid], 'M': M,
                 'baseline_correct': sum(x == y for x, y in zip(baseline['answers'], target_baseline)),
                 'packet_words': words(m['packet']), 'reason_words': words(m['reason']),
                 'service_attempts': len(m['answers']), 'service_correct': current_correct,
                 'Y0_count': outcomes[0], 'Y1_count': outcomes[1], 'gain_count': outcomes[1] - outcomes[0],
                 'classical_report_learner_correct': learned_correct})
check(len(set(maintenance_common)) == 1, 'common_maintenance_incentives', 'same task and incentive paragraphs')

rows_by_id = {row['id']: row for row in data}
primary = {}
challenge_ids = [d['id'] for d in fixtures if d['truth'] is not None]
for name, field, scale in [('feedback_to_maintenance', 'M', 1), ('factorial_interaction', 'gain_count', 16)]:
    observed = sum((2 * A[lid] - 1) * rows_by_id[lid][field] for lid in challenge_ids)
    total_y = sum(rows_by_id[lid][field] for lid in challenge_ids)
    total_permutations = extreme = 0
    selections = [list(itertools.combinations(block, 2)) for block in blocks[:6]]
    for selection in itertools.product(*selections):
        treated_sum = sum(rows_by_id[lid][field] for block in selection for lid in block)
        statistic = 2 * treated_sum - total_y
        total_permutations += 1
        extreme += abs(statistic) >= abs(observed)
    primary[name] = {'effect': observed / (12 * scale), 'tail_count': extreme,
                     'permutations': total_permutations, 'p_two_sided': extreme / total_permutations}
gains = [row['gain_count'] for row in data if row['stratum'] == 'challenge' and row['A'] == 1]
observed = sum(gains)
all_sums = [sum(sign * gain for sign, gain in zip(signs, gains)) for signs in itertools.product((-1, 1), repeat=len(gains))]
extreme = sum(abs(s) >= abs(observed) for s in all_sums)
primary['access_after_feedback'] = {'effect': observed / (len(gains) * 16), 'tail_count': extreme,
                                    'permutations': len(all_sums), 'p_two_sided': extreme / len(all_sums)}
for stat in primary.values():
    stat['bonferroni_adjusted_p'] = min(1.0, 3 * stat['p_two_sided'])
    stat['passes_registered_criterion'] = stat['effect'] > 0 and stat['p_two_sided'] < 0.05 / 3

arm_summary = []
for stratum, a in itertools.product(('challenge', 'adequate'), (0, 1)):
    selected = [row for row in data if row['stratum'] == stratum and row['A'] == a]
    n = len(selected)
    arm_summary.append({'stratum': stratum, 'A': a, 'n': n, 'packets': sum(r['M'] for r in selected),
                        'baseline_correct': sum(r['baseline_correct'] for r in selected), 'baseline_cases': 8*n,
                        'service_attempted': sum(r['service_attempts'] for r in selected),
                        'service_correct': sum(r['service_correct'] for r in selected),
                        'Y0_correct': sum(r['Y0_count'] for r in selected),
                        'Y1_correct': sum(r['Y1_count'] for r in selected), 'successor_cases_per_B': 16*n})

results = read(ROOT / 'results.json')
for name, value in primary.items():
    for key in ('effect', 'tail_count', 'permutations', 'p_two_sided'):
        check(abs(results['primary'][name][key] - value[key]) < 1e-14, 'reported_primary_agreement', [name, key])
for previous in results['lineages']:
    for key in ('A', 'M', 'baseline_correct', 'packet_words', 'service_attempts', 'service_correct', 'Y0_count', 'Y1_count', 'gain_count'):
        check(previous[key] == rows_by_id[previous['id']][key], 'reported_lineage_agreement', [previous['id'], key])

def stamp(path):
    return path.stat().st_mtime
def iso(epoch):
    return datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).isoformat()
baseline_paths = list(ROOT.glob('lineages/*/baseline-response.json'))
maintenance_paths = list(ROOT.glob('lineages/*/maintenance-response.json'))
successor_paths = list(ROOT.glob('lineages/*/r*-response.json'))
check(len(baseline_paths) == 32 and len(maintenance_paths) == 32 and len(successor_paths) == 64, 'raw_response_count', '128 JSON responses')
check(max(map(stamp, baseline_paths)) < stamp(ROOT / 'assignments.json') < min(map(stamp, maintenance_paths)), 'local_timing_A', 'all baselines before A and maintenance')
check(max(map(stamp, maintenance_paths)) < stamp(ROOT / 'successor-assignments.json') < min(map(stamp, successor_paths)), 'local_timing_B', 'all maintenance before B and successor')
check(stamp(ROOT / 'FREEZE.json') < min(map(stamp, baseline_paths)), 'local_timing_initial_freeze', 'before first baseline')
check(stamp(ROOT / 'ANALYSIS-FREEZE.json') < min(map(stamp, maintenance_paths)), 'local_timing_analysis_freeze', 'before maintenance outcomes')
check(stamp(ROOT / 'SUCCESSOR-FREEZE.json') < min(map(stamp, successor_paths)), 'local_timing_successor_freeze', 'before successor outcomes')
for directory in sorted((ROOT / 'lineages').iterdir()):
    for stage in ('baseline', 'maintenance', 'r0', 'r1'):
        check(stamp(directory / (stage + '-prompt.txt')) < stamp(directory / (stage + '-response.json')), 'local_prompt_before_response', [directory.name, stage])

audit = {'audit_method': 'Independent standard-library scorer and exhaustive assignment enumeration; neither run.py nor analyze.py imported or executed.',
         'audit_time_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'all_automated_checks_pass': not errors, 'errors': errors, 'checks_by_category': dict(checks),
         'raw_response_counts': {'founder_baselines': len(baseline_paths), 'founder_maintenance': len(maintenance_paths), 'successors': len(successor_paths)},
         'successor_prompt_files': 64, 'distinct_successor_prompt_byte_strings': len({s['prompt_sha256'] for s in S}),
         'primary': primary, 'arm_summary': arm_summary, 'lineages': data,
         'timing': {'last_baseline': iso(max(map(stamp, baseline_paths))), 'A_file': iso(stamp(ROOT/'assignments.json')),
                    'first_maintenance': iso(min(map(stamp, maintenance_paths))), 'last_maintenance': iso(max(map(stamp, maintenance_paths))),
                    'B_file': iso(stamp(ROOT/'successor-assignments.json')), 'first_successor': iso(min(map(stamp, successor_paths))),
                    'last_successor': iso(max(map(stamp, successor_paths)))},
         'limits': ['Local timestamps and self-generated hashes support integrity but are not external notarization.',
                    'Prompt-file hashes do not by themselves prove invocation identity, fresh context, or full tool-trace compliance.',
                    'Filesystem restrictions were instructional, not a security sandbox.',
                    'All successor contexts are novel relative to the verified baseline, but four test cases also appeared as maintenance-stage ordinary cases.',
                    'The opportunity cost is one foregone case, not necessarily one lost correct point.',
                    'The conventional candidate-elimination learner matches 16/16 with the complete report in every fixture.',
                    'Exact probabilities test sharp finite-assignment nulls and do not establish weak-average interaction inference or population generalization.']}
invocation_path = ROOT / 'orchestrator-invocations.json'
if invocation_path.exists():
    invocation = read(invocation_path)
    participants = invocation['participants']
    check(len(participants) == 96 and len({p['participant_task'] for p in participants}) == 96,
          'orchestrator_record_cardinality', '96 distinct declared participant identities')
    expected_response_files = set()
    actual_response_files = set()
    for fixture in fixtures:
        relative = 'work/live/lineages/' + fixture['id'] + '/'
        expected_response_files.update(relative + s + '-response.json' for s in ('baseline', 'maintenance', 'r0', 'r1'))
    for participant in participants:
        check(participant['context_creation'] == 'collaboration.spawn_agent with fork_turns none',
              'orchestrator_declared_fresh_start', participant['participant_task'])
        if 'baseline_response' in participant:
            check(participant['maintenance_context'] == 'same founder via collaboration.followup_task',
                  'orchestrator_declared_founder_continuation', participant['participant_task'])
            actual_response_files.update([participant['baseline_response'], participant['maintenance_response']])
        else:
            actual_response_files.add(participant['response'])
    check(expected_response_files == actual_response_files, 'orchestrator_record_response_coverage', 'all 128 saved response files')
    audit['orchestrator_record'] = {'provenance': invocation['provenance'], 'distinct_declared_participants': len(participants),
                                  'declared_fresh_founder_contexts': sum('baseline_response' in p for p in participants),
                                  'declared_fresh_successor_contexts': sum('response' in p for p in participants),
                                  'independent_platform_attestation': False, 'complete_tool_trace_audit': False,
                                  'actual_model_identifier': 'not recorded by exposed collaboration responses'}
    audit['checks_by_category'] = dict(checks)
    audit['all_automated_checks_pass'] = not errors
(ROOT / 'data-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
print(json.dumps({k: audit[k] for k in ('all_automated_checks_pass', 'errors', 'raw_response_counts', 'distinct_successor_prompt_byte_strings', 'primary', 'arm_summary', 'timing')}, indent=2))
