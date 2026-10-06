#!/usr/bin/env python3
"""Exact descriptive reanalysis of archived choices; no experimental intervention."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import csv
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'sources/30-recipient-harm-valuation-2026-10-06'
ORIGINAL = SOURCE / 'original'
PHASES = ('baseline', 'shock1', 'shock2', 'shock3', 'shock_all')
METRICS = ('preferred_offered', 'alternative_offered', 'nonresponse_offered',
           'unknown_offered', 'preferred_completed')
GROUPS = {
    'no_harm_male': list(range(1, 15)),
    'contingent_harm_male': list(range(15, 27)),
    'contingent_harm_female': list(range(27, 39)),
    'random_harm_male': list(range(39, 47)),
    'not_pre_exposed_male': list(range(47, 61)),
    'one_vs_two_pellets': list(range(61, 68)),
    'one_vs_three_pellets': list(range(68, 79)),
}
CONTRASTS = {
    'primary_harm_minus_no_harm': ('contingent_harm_male', 'no_harm_male'),
    'secondary_exposed_minus_not_exposed': ('contingent_harm_male', 'not_pre_exposed_male'),
    'secondary_female_minus_male': ('contingent_harm_female', 'contingent_harm_male'),
    'secondary_two_pellets_minus_one': ('one_vs_two_pellets', 'contingent_harm_male'),
    'secondary_three_pellets_minus_one': ('one_vs_three_pellets', 'contingent_harm_male'),
    'descriptive_random_minus_contingent': ('random_harm_male', 'contingent_harm_male'),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def mean(values):
    known = [F(v) for v in values if v is not None]
    return dict(known=len(known), unknown=len(values)-len(known),
                exact=str(sum(known, F(0))/len(known)) if known else None)


def stats(values):
    counts = Counter(values)
    n = len(values)
    completed = counts[1]+counts[2]
    result = {'offered': n, 'preferred': counts[2], 'alternative': counts[1],
              'nonresponse': counts[0], 'unknown': counts[None], 'completed': completed}
    for name, code in [('preferred', 2), ('alternative', 1), ('nonresponse', 0), ('unknown', None)]:
        result[name+'_offered'] = str(F(counts[code], n))
    result['preferred_completed'] = str(F(counts[2], completed)) if completed else None
    assert sum(counts.values()) == n
    assert sum(F(result[k]) for k in METRICS[:-1]) == 1
    return result


def parse():
    with (ORIGINAL / 'dataMainPaper.csv').open(encoding='utf-8-sig', newline='') as stream:
        summary_rows = [r for r in csv.DictReader(stream) if r['Animal Number'].strip()]
    summaries = {int(r['Animal Number']): r for r in summary_rows}
    assert len(summaries) == len(summary_rows) == 142
    with (ORIGINAL / 'TrialByTrialChoicesMainPaper.csv').open(encoding='utf-8-sig', newline='') as stream:
        raw = list(csv.reader(stream))
    assert len(raw) == 81 and all(len(r) == 88 for r in raw)
    assert raw[0][1:3] == ['Actor Number', 'Group']
    for offset in (3, 23, 43, 63):
        assert raw[1][offset:offset+20] == ['Trial '+str(i) for i in range(1, 21)]
    assert not any(cell.strip() for cell in raw[-1])
    actors = []
    for row in raw[2:-1]:
        actor_id = int(row[1])
        meta = summaries[actor_id]
        assert row[2].strip() == meta['Condition'].strip()
        group = next(g for g, ids in GROUPS.items() if actor_id in ids)
        assert meta['Gender'].strip() == ('Female' if group.endswith('female') else 'Male')
        codes = []
        for cell in row[3:83]:
            assert cell in ('0', '1', '2', ''), (actor_id, cell)
            codes.append(None if cell == '' else int(cell))
        blocks = {name: codes[j*20:(j+1)*20] for j, name in enumerate(PHASES[:4])}
        blocks['shock_all'] = codes[20:]
        phase_stats = {name: stats(block) for name, block in blocks.items()}
        changes = {phase: {metric: None if phase_stats[phase][metric] is None or
                          phase_stats['baseline'][metric] is None else
                          str(F(phase_stats[phase][metric])-F(phase_stats['baseline'][metric]))
                          for metric in METRICS} for phase in PHASES[1:]}
        actors.append(dict(actor=actor_id, group=group, source_group=row[2],
            metadata={k: meta[k] for k in ['SBL#', 'Rat Number', 'Condition', 'Group', 'Gender']},
            codes=codes, phases=phase_stats, changes=changes,
            supplied_nonperformance=row[83:88]))
    assert [a['actor'] for a in actors] == list(range(1, 79))
    unknown = [(a['actor'], i) for a in actors for i, c in enumerate(a['codes']) if c is None]
    assert unknown == [(70, 70)], unknown
    return actors, summaries


def group_stats(actors):
    return dict(actors=[a['actor'] for a in actors], n=len(actors),
        sbl_labels=dict(sorted(Counter(a['metadata']['SBL#'] for a in actors).items())),
        totals={p: {key: sum(a['phases'][p][key] for a in actors)
                    for key in ('offered', 'preferred', 'alternative', 'nonresponse', 'unknown', 'completed')}
                for p in PHASES},
        means={p: {m: mean([a['phases'][p][m] for a in actors]) for m in METRICS} for p in PHASES},
        changes={p: {m: mean([a['changes'][p][m] for a in actors]) for m in METRICS} for p in PHASES[1:]})


def contrast(left, right):
    a, b = group_stats(left), group_stats(right)
    return dict(left_actors=a['actors'], right_actors=b['actors'],
        phase_differences={p: {m: None if a['means'][p][m]['exact'] is None or b['means'][p][m]['exact'] is None
            else str(F(a['means'][p][m]['exact'])-F(b['means'][p][m]['exact'])) for m in METRICS} for p in PHASES},
        change_differences={p: {m: None if a['changes'][p][m]['exact'] is None or b['changes'][p][m]['exact'] is None
            else str(F(a['changes'][p][m]['exact'])-F(b['changes'][p][m]['exact'])) for m in METRICS} for p in PHASES[1:]})


def audit_summaries(actors, summaries):
    comparisons, discrepancies = [], []
    for actor in actors:
        i = actor['actor']
        meta = summaries[i]
        for phase, field in [('baseline', 'Baseline'), ('shock1', 'Shock 1'), ('shock2', 'Shock 2'), ('shock3', 'Shock 3')]:
            actual = actor['phases'][phase]['preferred_completed']
            expected = None if actual is None else F(actual)*100
            given = None if not meta[field].strip() else F(meta[field])
            delta = None if expected is None or given is None else abs(given-expected)
            row = dict(actor=i, field=field, given=meta[field], computed=None if expected is None else str(expected),
                absolute_difference=None if delta is None else str(delta),
                agree=(given is None and expected is None) or (delta is not None and delta <= F(11, 1000)))
            comparisons.append(row)
            if not row['agree']: discrepancies.append(row)
        values = [actor['phases'][p]['preferred_completed'] for p in PHASES[1:4]]
        expected = None if any(v is None for v in values) else sum(F(v)*100 for v in values)/3
        given = None if not meta['AverageShock'].strip() else F(meta['AverageShock'])
        delta = None if expected is None or given is None else abs(given-expected)
        row = dict(actor=i, field='AverageShock', given=meta['AverageShock'],
            computed=None if expected is None else str(expected), absolute_difference=None if delta is None else str(delta),
            agree=(given is None and expected is None) or (delta is not None and delta <= F(11, 1000)))
        comparisons.append(row)
        if not row['agree']: discrepancies.append(row)
        calculated = [actor['phases'][p]['nonresponse'] for p in PHASES[:4]]
        calculated.append(sum(calculated))
        for phase, given, expected in zip((*PHASES[:4], 'total'), actor['supplied_nonperformance'], calculated):
            row = dict(actor=i, field='nonperformance_'+phase, given=given, computed=expected,
                agree=bool(given.strip()) and F(given) == expected)
            comparisons.append(row)
            if not row['agree']: discrepancies.append(row)
    return dict(comparisons=comparisons, discrepancies=discrepancies,
                tolerance_percentage_points='11/1000')


def main():
    freeze = read(HERE / 'protocol-freeze.json')
    assert sha(HERE / 'PROTOCOL.md') == freeze['protocol_sha256']
    for path, digest in freeze['source_sha256'].items(): assert sha(ROOT / path) == digest
    clarification = read(HERE / 'schema-clarification-freeze.json')
    for name, digest in clarification['files'].items(): assert sha(HERE / name) == digest
    actors, summaries = parse()
    by_group = {g: [a for a in actors if a['group'] == g] for g in GROUPS}
    comparisons = {name: contrast(by_group[l], by_group[r]) for name, (l, r) in CONTRASTS.items()}
    left, right = (by_group[g] for g in CONTRASTS['primary_harm_minus_no_harm'])
    omissions = {str(a['actor']): contrast([x for x in left if x['actor'] != a['actor']],
                    [x for x in right if x['actor'] != a['actor']]) for a in left+right}
    sbls = sorted({a['metadata']['SBL#'] for a in left+right})
    label_omissions = {label: contrast([a for a in left if a['metadata']['SBL#'] != label],
                         [a for a in right if a['metadata']['SBL#'] != label]) for label in sbls}
    actor70 = next(a for a in actors if a['actor'] == 70)
    completions = {}
    for replacement in (0, 1, 2):
        values = actor70['codes'].copy(); values[70] = replacement
        completed = {p: stats(values[j*20:(j+1)*20]) for j, p in enumerate(PHASES[:4])}
        completed['shock_all'] = stats(values[20:])
        completions[str(replacement)] = completed
    result = dict(schema_version=1, status='computed_pending_independent_check',
        protocol_sha256=freeze['protocol_sha256'], clarification_sha256=sha(HERE / 'SCHEMA-CLARIFICATION.md'),
        analysis_sha256=sha(Path(__file__)), source_sha256=freeze['source_sha256'],
        actors=actors, groups={g: group_stats(a) for g, a in by_group.items()}, contrasts=comparisons,
        primary_leave_one_actor_out=omissions, primary_leave_one_sbl_label_out=label_omissions,
        actor70_unknown_completion_sensitivity=completions, source_summary_audit=audit_summaries(actors, summaries),
        source_coverage=dict(trial_actors=78, summary_actors=142, primary_actors=26,
            offered_trial_slots=78*80, unknown_trial_slots=1,
            summary_only_actor_ids=sorted(set(summaries)-set(range(1, 79))),
            summary_only_conditions=dict(sorted(Counter(r['Condition'] for i, r in summaries.items() if i>78).items()))),
        interpretation='Exact descriptive archived-cohort comparisons. Equal offered food is not equal private experience or realized food. Nonperformance and unknown remain separate. No population causal estimate or latent/normative value identified.',
        new_animal_experiments=0)
    path = HERE / 'results.json'
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    receipt = dict(status='computed', code_sha256=sha(Path(__file__)), results_sha256=sha(path),
        protocol_sha256=freeze['protocol_sha256'], clarification_sha256=result['clarification_sha256'],
        actors=78, primary_actors=26, trial_slots=6240,
        source_discrepancies=len(result['source_summary_audit']['discrepancies']))
    (HERE / 'analysis-receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))
    print(json.dumps({name: obj['change_differences']['shock_all'] for name, obj in comparisons.items()}, indent=2))


if __name__ == '__main__':
    main()
