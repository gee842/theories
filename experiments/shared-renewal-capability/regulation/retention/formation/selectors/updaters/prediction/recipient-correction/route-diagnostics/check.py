#!/usr/bin/env python3
"""Finite evidence signatures and saved-ancestry audit, not a new experiment.

No route is changed and no funding/observation apparatus is implemented here.
The independent actual receipt and paid before/after reads are explicit premises
of the diagnostic interface, not borrowed from the tested route's audit trace.
"""

from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
LEARNING = BASE / 'successor-learning'
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
DORMANT_ROUTES = ('target', 'closed', 'frozen')


def require(condition, reason):
    if not condition:
        raise AssertionError(reason)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    frozen = {}

    def freeze(path):
        relative = str(path.relative_to(REPO))
        if relative not in frozen:
            frozen[relative] = path.read_bytes()
        return frozen[relative]

    saved = json.loads(freeze(LEARNING / 'results.json'))
    inputs = json.loads(freeze(LEARNING / 'inputs.json'))
    checked = json.loads(freeze(LEARNING / 'independent-check.json'))
    accepted = json.loads(freeze(LEARNING / 'check.json'))
    require(accepted['status'] == 'passed', 'Accepted producer-side check is not passed')
    require(digest(freeze(LEARNING / 'check.py')) == accepted['checker_sha256'],
            'Accepted producer-side checker hash mismatch')
    require(set(accepted['data_sha256']) == {'inputs.json', 'results.json'},
            'Accepted data-hash inventory changed')
    for name, expected in accepted['data_sha256'].items():
        require(digest(freeze(LEARNING / name)) == expected,
                'Accepted checked data bytes differ: ' + name)
    require(checked['status'] == 'passed', 'Accepted independent check is not passed')
    require(saved['source_sha256'] == inputs['source_sha256'], 'Accepted input/result source manifests differ')
    require(accepted['source_sha256'] == saved['source_sha256'], 'Accepted check/result source manifests differ')
    for manifest in (saved['source_sha256'], checked['source_sha256']):
        for relative, expected in manifest.items():
            path = (REPO / relative).resolve()
            require(path.is_relative_to(REPO), 'Manifest path escapes repository')
            require(digest(freeze(path)) == expected, 'Accepted source hash mismatch: ' + relative)
    freeze(LEARNING / 'HANDOFF.md')
    freeze(Path(__file__).resolve())
    learner = load(LEARNING / 'model.py', '_diagnostic_successor_interface')
    route_model = learner.parent

    # True/False below means the actual independently reported receipt. It is
    # not the potentially absent/private-zero signal returned by tested gamma.
    expected_present = dict(target=(False, True), private_zero=(True, True),
                            closed=(False, False), frozen=(False, False))
    expected_absent = dict(target=(False, False), private_zero=(True, True),
                           closed=(False, False), frozen=(False, False))
    signatures = {}
    route_checks = commitment_checks = 0
    for channel in (True, False):
        by_route = {}
        for route in route_model.Route:
            per_code = []
            input_presence = []
            for code in range(4):
                observed = []
                for receipt in (True, False):
                    action = route_model.issue(code, 1)
                    outcome = route_model.route_feedback(route, code, 1, action, receipt, True, channel)
                    ordinary = learner.feedback(route.value, code, action, receipt, channel, 'ordinary')
                    conventional = learner.feedback(route.value, code, action, receipt, channel, 'conventional')
                    require(outcome == ordinary == conventional, 'Route/table feedback mismatch')
                    candidate, label, source_tag = outcome
                    require(0 <= candidate < 4 and candidate % 2 == code % 2,
                            'Recipient update leaves bounded code or alters original-actor bit')
                    observed.append(route_model.issue(candidate, 1) != action)
                    input_presence.append(label is not None)
                    for paid_write in (False, True):
                        # Existing successor write guard commits candidate only
                        # after a completed paid write (model.py:158-160).
                        committed = candidate if paid_write else code
                        flip = route_model.issue(committed, 1) != action
                        require(committed % 2 == code % 2, 'Commitment changed original-actor bit')
                        require(paid_write or not flip, 'Unpaid write changed the physical record')
                        commitment_checks += 1
                    route_checks += 1
                per_code.append(tuple(observed))
            expected = (expected_present if channel else expected_absent)[route.value]
            require(all(sig == expected for sig in per_code), 'Unexpected conditional flip signature')
            by_route[route.value] = dict(flip_after_success=expected[0], flip_after_failure=expected[1],
                acquired_label_present=all(input_presence), all_four_codes_agree=True)
        signatures['channel_present' if channel else 'channel_absent'] = by_route
    require(expected_present['closed'] == expected_present['frozen'], 'Closed/frozen record alias missing')
    require(len(set(expected_present.values())) == 3, 'Paid report+record classifier has wrong classes')

    # Consecutive logical probes under a stable available binary plant. These
    # execute only the pure action/update functions, with all writes completed;
    # they do not construct a paid experiment or assert funds for three probes.
    replays = []
    fixed_points = 0
    for code in range(4):
        initial_bit = route_model.issue(code, 1)
        for world in (0, 1):
            sequences = {}
            for route in route_model.Route:
                current = code
                receipt_word, codes = '', [current]
                for _ in range(3):
                    action = route_model.issue(current, 1)
                    captured = action == world
                    current, _, _ = route_model.route_feedback(route, current, 1, action, captured, True, True)
                    require(current % 2 == code % 2, 'Replay changed original-actor bit')
                    receipt_word += str(int(captured))
                    codes.append(current)
                sequences[route.value] = dict(actual_receipts=receipt_word, codes=codes)
            if world != initial_bit:
                require({r: v['actual_receipts'] for r, v in sequences.items()} ==
                        dict(target='011', private_zero='010', closed='000', frozen='000'),
                        'Wrong-initial-bit receipt words changed')
                require(sequences['target']['actual_receipts'][:2] == sequences['private_zero']['actual_receipts'][:2]
                        and sequences['target']['codes'][1] == sequences['private_zero']['codes'][1]
                        and sequences['target']['codes'][2] != sequences['private_zero']['codes'][2],
                        'Two-outcome alias or second paid-record distinction missing')
            else:
                require({r: v['actual_receipts'] for r, v in sequences.items()} ==
                        dict(target='111', private_zero='101', closed='111', frozen='111'),
                        'Correct-initial-bit receipt words changed')
                for route in DORMANT_ROUTES:
                    require(sequences[route]['codes'] == [code] * 4, 'Correct stable fixed point failed')
                    candidate, _, _ = route_model.route_feedback(route_model.Route(route), code, 1,
                        initial_bit, True, True, True)
                    require(candidate == code, 'One-step stable fixed-point certificate failed')
                    fixed_points += 1
            replays.append(dict(initial_code=code, world=world, sequences=sequences))

    # This is a local evidence-map alias, not equality of complete saved states,
    # histories, payments or source inventories.
    action, code = 0, 1
    target_available_wrong = action == 1 and True
    target_unavailable_right = action == 0 and False
    require(target_available_wrong == target_unavailable_right is False, 'Receipt ambiguity missing')
    wrong_update = route_model.route_feedback(route_model.Route.TARGET, code, 1, action,
                                               target_available_wrong, True, True)
    outage_update = route_model.route_feedback(route_model.Route.TARGET, code, 1, action,
                                                target_unavailable_right, True, True)
    require(wrong_update == outage_update == (3, 1, 'target'), 'Same receipt no longer gives same update')

    # Reanalyse exact actual dormant-capacity ancestry. No preparation, suffix,
    # copying or continuation function is called to regenerate these results.
    ancestry_groups = []
    entry_count = terminal_count = 0
    for producer in PRODUCERS:
        entries = inputs['inputs']['same_law'][producer]
        rows = saved['cases']['same_law_stable']['producers'][producer]['ordinary']['distribution']
        for actor in (8, 15):
            for code in (0, 3):
                route_records, common_input, common_output = {}, None, None
                for gamma in DORMANT_ROUTES:
                    candidates = [entry for entry in entries if entry['kind'] == 'transmission'
                        and entry['route'] == gamma and entry['transmission']['state']['retained']
                        and entry['transmission']['state']['actor'] == actor
                        and entry['transmission']['state']['child'] == [gamma, code]]
                    require(len(candidates) == 1, 'Dormant ancestor is missing or not uniquely matched')
                    entry = candidates[0]
                    entrance = entry['transmission']['state']
                    require(entrance['recipient'] == 20 and entrance['child_fuel'] == 0
                            and entrance['auxiliary_source'] == 0 and entry['target_law'] == code // 2,
                            'Actual stable entrance contract changed')
                    matched = [row for row in rows if row['kind'] == 'continuation'
                        and row['state']['original_actor'] == actor and row['state']['gamma'] == gamma
                        and row['state']['q'] == code and row['state']['grandchild_retained']]
                    require(len(matched) == 1, 'Dormant terminal state missing or ambiguous')
                    row, end = matched[0], matched[0]['state']
                    require(Q(row['probability']) == Q(entry['mass']), 'Saved dormant input/output mass differs')
                    require(end['recipient'] == 25 and end['learner_fuel'] == end['grandchild_fuel'] == 0
                        and end['old_auxiliary_source'] == end['new_source'] == 0
                        and end['grandchild'] == [gamma, code] and end['grandchild_stage'] == 'child_held'
                        and end['grandchild_blank'] == end['grandchild_part'] == 0
                        and end['grandchild_occupied'] == end['grandchild_assembled'] == 1
                        and end['grandchild_latch'] is None, 'Dormant successor handoff changed')
                    input_projection = {k: entrance[k] for k in ('actor', 'recipient', 'child_fuel',
                        'auxiliary_source', 'blank', 'routing_part', 'occupied_blank', 'assembled_part',
                        'latch', 'copied', 'retained', 'child_recipient_action_enabled')}
                    output_projection = dict(end)
                    del output_projection['gamma']
                    output_projection['grandchild'] = [code]
                    if common_input is None:
                        common_input, common_output = input_projection, output_projection
                    require(input_projection == common_input and output_projection == common_output,
                            'Stable capacity contrast changed physical stocks/payload beyond route identity')
                    expected_mass = Q(1, 72 if producer == 'fixed_normal' else 144)
                    require(Q(entry['mass']) == expected_mass, 'Dormant exact state mass changed')
                    route_records[gamma] = dict(unconditional_mass=str(expected_mass),
                        prefix_fuel=entry['predecessor']['state']['fuel'],
                        template_before=[gamma, code], template_after=[gamma, code],
                        terminal_stage=end['grandchild_stage'])
                    entry_count += 1
                    terminal_count += 1
                ancestry_groups.append(dict(producer=producer, original_actor=actor, q=code,
                    route_records=route_records, common_entrance=common_input,
                    common_terminal_projection=common_output))

    hashes = {relative: digest(data) for relative, data in sorted(frozen.items())}
    for relative, expected in hashes.items():
        require(digest((REPO / relative).read_bytes()) == expected,
                'Source changed during diagnostic inspection: ' + relative)
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=hashes, sources_unchanged_during_check=True,
        accepted_data_verification=dict(status=accepted['status'],
            record=str((LEARNING / 'check.json').relative_to(REPO)),
            checker_sha256=accepted['checker_sha256'], data_sha256=accepted['data_sha256']),
        scope=('Conditional finite-function evidence audit and reanalysis of accepted saved histories. '
               'No new physical test, diagnostic apparatus, route revision, selector, funding law or renewal is executed.'),
        counts=dict(route_input_cases=route_checks, paid_unpaid_commitment_cases=commitment_checks,
                    three_probe_replays=len(replays) * 4, stable_one_step_fixed_points=fixed_points,
                    matched_ancestry_groups=len(ancestry_groups), matched_ancestor_rows=entry_count,
                    matched_terminal_rows=terminal_count),
        diagnostic_contract=dict(
            input='Ordinary action equals the currently stored recipient bit; q remains in 0..3.',
            independent_report='Actual recipient success/failure must be acquired independently of the route under test.',
            records='Before/after q observations require explicitly funded access; saved trace fields are not an installed monitor.',
            write='A completed paid write is known; unpaid writes cannot support this classification.',
            route='The same physical route and named recipient address persist across compared observations.',
            coverage='Both actual success and failure are required to observe the complete signature; no funds or occurrence are proved here.',
            excludes='The classifier excludes readable gamma, source/provenance tags, input-presence flags, hidden law and audit scores.'),
        conditional_signatures=signatures,
        classification=dict(channel_present=[['target'], ['private_zero'], ['closed', 'frozen']],
                            channel_absent=[['private_zero'], ['target', 'closed', 'frozen']],
                            unpaid_write=[['target', 'private_zero', 'closed', 'frozen']]),
        unpaid_write_counterexample=dict(route='target', q_before=1, action=0,
            independent_actual_receipt=False, candidate_q=wrong_update[0], paid_write=False,
            committed_q=1, observed_flip=False,
            scope='Conditional commitment guard, not an executed or funded physical inspection.'),
        stable_probe_examples=[row for row in replays if row['initial_code'] == 1],
        fixed_point_interpretation=('For each of the four codes, a correct stable available target leaves '
            'TARGET/CLOSED/FROZEN unchanged with receipt true. Iterating this fixed point preserves their '
            'record/outcome equality for any finite sequence; readable gamma or input presence is a different projection.'),
        receipt_ambiguity=dict(q=1, action=0, actual_receipt=False, next_q=3,
            alternatives=[dict(target_law=1, available=True), dict(target_law=0, available=False)],
            scope='Local action/receipt/update alias; not an assertion that full saved histories, budgets or source inventories match.'),
        actual_dormant_ancestry=ancestry_groups,
        access_boundary=dict(
            physical_template='gamma and q exist on the carrier; a new diagnostic read still needs a paid access contract.',
            paid_target='The existing probe supplies named recipient query 1 after its sensing fee; the low bit still refers to the original actor.',
            route_signal='TARGET/FROZEN can acquire actual receipt when the channel is present; PRIVATE_ZERO supplies private zero; CLOSED supplies none.',
            auxiliary_observations='Readable gamma and independently exposed input presence can separate otherwise aliased routes, but are not included in the signature classifier.',
            balances='Physical balances govern declared payment guards; they are not automatically new controller observations.',
            audit_only='capture/receipt_source/decoder_errors/witness flags, old-code controls and saved traces do not install a persistent diagnostic tape.',
            next_carrier='Admit an actual retained grandchild with a present bounded template and occupied assembled carrier. The older learner active flag does not by itself admit the grandchild.',
            stock='Matched stable endpoints have recipient25, original actor8 or15, both new carriers cash0, zero source and no free grandchild blank/routing part.',
            route_revision='Changing gamma requires a new paid reconfiguration/replacement law and explicit evidence access; these functions only evaluate the existing fixed routes.'))
    (HERE / 'verification.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(dict(status='passed', counts=report['counts'], frozen_files=len(hashes))))


if __name__ == '__main__':
    main()
