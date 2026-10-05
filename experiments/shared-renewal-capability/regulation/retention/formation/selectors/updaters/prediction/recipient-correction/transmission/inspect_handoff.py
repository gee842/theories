#!/usr/bin/env python3
"""Reanalyse frozen recipient-correction outputs without executing their producers.

This is a bounded evidence/contract audit, not a transmission implementation,
an independent experiment, or verification of the full stochastic process.
"""

import ast
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
STUDY = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').is_file())
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
COMPARATORS = ('private_only', 'frozen', 'private_as_recipient')
NONALIASED = ('primary', 'same_law', 'recipient_outage', 'missing_channel',
             'target_swapped', 'low_reserve', 'expensive_write')
EXCLUDED = ('q', 'recipient')


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def key(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def distribution(rows, transform):
    out = defaultdict(Fraction)
    for row in rows:
        mass = Fraction(row['probability'])
        require(mass > 0, 'Saved terminal rows must have positive exact mass')
        out[key(transform(row))] += mass
    require(sum(out.values()) == 1, 'Saved distribution is not normalized')
    return dict(out)


def full_row(row):
    return {k: v for k, v in row.items() if k != 'probability'}


def retained_actor(row):
    state = row['state']
    if row['kind'] == 'suffix':
        state = {k: v for k, v in state.items() if k not in EXCLUDED}
    else:
        require(row['kind'] == 'preparation_failure', 'Unexpected terminal class')
    return {'kind': row['kind'], 'state': state}


def serialize_dist(dist):
    return [dict(json.loads(k), probability=str(v)) for k, v in sorted(dist.items())]


def payload_dist(rows):
    out = defaultdict(Fraction)
    for row in rows:
        if row['kind'] == 'suffix':
            s = row['state']
            out[(s['fuel'], s['q'], s['recipient'])] += Fraction(row['probability'])
    return [dict(actor_fuel=f, q=q, recipient=r, unconditional_mass=str(m))
            for (f, q, r), m in sorted(out.items())]


def main():
    # Parse only these frozen bytes. Never import model.py or call a producer.
    frozen = {}

    def freeze(path):
        relative = str(path.relative_to(REPO))
        if relative not in frozen:
            frozen[relative] = path.read_bytes()
        return frozen[relative]

    fixtures = json.loads(freeze(STUDY / 'fixtures.json'))
    results = json.loads(freeze(STUDY / 'results.json'))
    prior_check = json.loads(freeze(STUDY / 'independent-check.json'))
    require(prior_check['status'] == 'passed', 'Saved suffix check is not passed')
    require(fixtures['source_sha256'] == results['source_sha256'],
            'Fixture and result source manifests differ')
    manifests = (fixtures['source_sha256'], prior_check['source_sha256'])
    for manifest in manifests:
        for relative, expected in manifest.items():
            path = (REPO / relative).resolve()
            require(path.is_relative_to(REPO), 'Source manifest escapes repository')
            require(digest(freeze(path)) == expected, f'Source hash mismatch: {relative}')
    source = freeze(STUDY / 'model.py').decode()
    freeze(STUDY / 'HANDOFF.md')
    freeze(Path(__file__).resolve())

    cases = results['cases']
    require(set(cases) == set(NONALIASED) | {'target_alias'}, 'Fixture set changed')
    primary = {}
    projected_checks = []
    full_conventional_checks = 0
    for case_name, case in cases.items():
        require(set(case['producers']) == set(PRODUCERS), 'Producer set changed')
        for producer in PRODUCERS:
            arms = case['producers'][producer]
            baseline = distribution(arms['indexed']['distribution'], retained_actor)
            indexed_full = distribution(arms['indexed']['distribution'], full_row)
            require(indexed_full == distribution(arms['conventional']['distribution'], full_row),
                    f'Conventional full distribution differs: {case_name}/{producer}')
            full_conventional_checks += 1
            for arm in COMPARATORS:
                equal = baseline == distribution(arms[arm]['distribution'], retained_actor)
                expected = case_name != 'target_alias' or arm == 'private_as_recipient'
                require(equal == expected,
                        f'Unexpected actor projection relation: {case_name}/{producer}/{arm}')
                projected_checks.append(dict(case=case_name, producer=producer,
                                             comparator=arm, equal=equal))
            if case_name == 'primary':
                metrics = arms['indexed']['metrics']
                for arm in COMPARATORS:
                    for name in ('spent', 'actor_captures', 'final_actor', 'active_memory'):
                        require(arms[arm]['metrics'][name] == metrics[name],
                                f'Primary private metric differs: {producer}/{arm}/{name}')
                    require(indexed_full != distribution(arms[arm]['distribution'], full_row),
                            f'Primary comparator unexpectedly identical in full: {producer}/{arm}')
                expected_actor = '25/9' if producer == 'fixed_normal' else '25/18'
                expected_recipient = '20/9' if producer == 'fixed_normal' else '10/9'
                require(metrics['final_actor'] == expected_actor, 'Primary actor mean changed')
                require(metrics['final_recipient'] == expected_recipient,
                        'Primary recipient mean changed')
                for arm in COMPARATORS:
                    require(arms[arm]['metrics']['final_recipient'] ==
                            (expected_recipient if arm == 'private_as_recipient' else '0'),
                            f'Primary recipient contrast changed: {producer}/{arm}')
                primary[producer] = dict(
                    actor_projection=serialize_dist(baseline),
                    arm_metrics={arm: {name: arms[arm]['metrics'][name] for name in
                        ('spent', 'actor_captures', 'final_actor', 'final_recipient',
                         'active_memory', 'strict_witness', 'decoder_errors', 'missing_evidence')}
                        for arm in ('indexed',) + COMPARATORS},
                    payload_recipient_projections={arm: payload_dist(arms[arm]['distribution'])
                        for arm in ('indexed',) + COMPARATORS})

    actual = []
    fixture = fixtures['fixtures']['30']
    for producer in PRODUCERS:
        arms = cases['primary']['producers'][producer]
        witness = arms['indexed']['witness']
        preparation, predecessor = witness['preparation'], witness['predecessor']
        require(preparation in fixture['preparations'], 'Witness preparation absent from fixture')
        prefix_rows = fixture['prefix_records'][producer][str(preparation['reserve'])]
        require(predecessor in prefix_rows, 'Witness predecessor absent from actual fixture')
        require(preparation['commissioned'] and preparation['packets'] == 12 and
                preparation['backing_slots'] == 2, 'Witness preparation contract changed')
        require(predecessor['state']['fuel'] == 21 and predecessor['state']['q'] == 4 and
                predecessor['final_regime'] == 1, 'Actual 21-unit witness changed')
        state = witness['state']
        require((state['fuel'], state['recipient'], state['q']) == (9, 10, 1),
                'Actual faithful witness endpoint changed')
        mass = Fraction(preparation['probability']) * Fraction(predecessor['probability'])
        require(mass == Fraction(witness['unconditional_terminal_branch_mass']),
                'Witness mass does not equal saved preparation times predecessor mass')
        expected_mass = Fraction(1, 18 if producer == 'fixed_normal' else 36)
        require(mass == expected_mass, 'Actual witness unconditional mass changed')
        matched = {}
        for arm, q, recipient in (('indexed', 1, 10), ('private_only', 3, 0),
                                   ('frozen', 3, 0), ('private_as_recipient', 3, 10)):
            wanted = dict(state, q=q, recipient=recipient)
            rows = [row for row in arms[arm]['distribution']
                    if row['kind'] == 'suffix' and row['state'] == wanted]
            require(len(rows) == 1, f'Expected endpoint row not unique: {producer}/{arm}')
            row = rows[0]
            require(Fraction(row['probability']) == mass,
                    f'Matched endpoint row has different mass: {producer}/{arm}')
            require(row['metrics']['spent'] == 32 and row['metrics']['actor_captures'] == 2,
                    f'Matched endpoint private account changed: {producer}/{arm}')
            if arm == 'indexed':
                require(row['metrics'] == witness['metrics'], 'Witness metrics absent from distribution')
            matched[arm] = row
        require([e['target'] for e in witness['trace']] == ['recipient', 'actor', 'recipient', 'actor']
                and [e['action'] for e in witness['trace']] == [1, 1, 0, 1]
                and [e['capture'] for e in witness['trace']] == [False, True, True, True],
                'Saved actual witness trace changed')
        actual.append(dict(producer=producer, preparation=preparation, predecessor=predecessor,
                           faithful_trace=witness['trace'], matched_terminal_rows=matched,
                           unconditional_mass=str(mass)))

    functions = {node.name: node for node in ast.parse(source).body
                 if isinstance(node, ast.FunctionDef)}
    argument_facts = {name: [a.arg for a in functions[name].args.args]
                      for name in ('suffix', 'read', 'write')}
    require(all('arm' in args for args in argument_facts.values()),
            'Expected externally parameterized arm interface changed')
    suffix_state_fields = sorted({k for case in cases.values() for arms in case['producers'].values()
        for arm in ('indexed',) + COMPARATORS for row in arms[arm]['distribution']
        if row['kind'] == 'suffix' for k in row['state']})
    require('arm' not in suffix_state_fields, 'Arm now appears in saved physical state')

    hashes = {relative: digest(data) for relative, data in sorted(frozen.items())}
    for relative, expected in hashes.items():
        require(digest((REPO / relative).read_bytes()) == expected,
                f'Input/checker changed during inspection: {relative}')
    report = dict(
        status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        scope=('Reanalysis of the same saved synthetic evidence, not an independent experiment, '
               'producer rerun, full stochastic verification, pathwise proof, or a physical copying law.'),
        checker=str(Path(__file__).resolve().relative_to(REPO)), source_sha256=hashes,
        inputs_and_checker_unchanged_during_inspection=True,
        producer_code_imported_or_executed=False,
        projection=dict(excluded_suffix_state_fields=list(EXCLUDED),
                        retained='Every other saved state field, including inherited auxiliary fields, and every preparation-failure state.',
                        metrics='Audit metrics excluded; probability masses summed exactly without conditioning.',
                        full_comparator='Full indexed/conventional comparison includes all saved metrics.'),
        counts=dict(primary_projected_equalities=9, nonaliased_projected_equalities=63,
                    alias_equalities=3, alias_inequalities=6,
                    conventional_full_distribution_equalities=full_conventional_checks,
                    actual_predecessor_witnesses=len(actual), matched_terminal_rows=4 * len(actual)),
        primary=primary, all_projected_comparisons=projected_checks, actual_witnesses=actual,
        lineage_limit=('Indexed witness explicitly retains its actual predecessor and trace. Alternative-arm '
                       'rows match the saved terminal state projection and mass; their ancestry/trace is not '
                       'stored per row and is not independently reconstructed by this audit.'),
        source_level_observations=dict(
            classification='Source/interface observations, not machine-proved semantic impossibility.',
            function_arguments=argument_facts, saved_suffix_state_fields=suffix_state_fields,
            external_arm='The supplied arm parameter selects read/write/channel behavior; it is absent from saved state.',
            payload='HANDOFF.md describes q as two orientation estimates, with no persistent provenance or recipe template.',
            missing_copy_template=('No heritable encoding or assembly law for the arm is established by these records. '
                                   'Copying q alone would transmit parameters, not the full learning recipe.'),
            resource_limit=('Recipient reserve is a separate scalar stock. No receiver, destination components, '
                            'recipient maintenance surplus, new source, or continued donor lifetime is introduced.')))
    output = HERE / 'handoff-audit.json'
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(dict(status=report['status'], counts=report['counts'],
                          frozen_files=len(hashes), output=str(output.relative_to(REPO)))))


if __name__ == '__main__':
    main()
