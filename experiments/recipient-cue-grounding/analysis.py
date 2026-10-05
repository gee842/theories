"""Retrospective paired reanalysis of a preserved public HTML table preview.

All source strings, zero counts, ties and focal animals remain visible. This
implements the frozen local protocol; it is not an original-CSV verification,
assignment-exact causal test, or replication of the authors' fitted analyses.
"""
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import io
import json
import math
import random
import re
import statistics
import sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SOURCE = REPO / '_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/experiment4-preview.tsv'
PROTOCOL_SHA256 = '44fe0ae4b4c03741629109110a6ceb22df8d4dcc161bccf1c512487f47e25f2d'
SOURCE_SHA256 = '4a2a9b660cfd9920a8d1bdcc7830507341e6c58ff08b239398dd6daebb82adbd'
FIELDS = ['preview_row', 'ratID', 'treatment', 'pull_f', 'lat_f', 'Pull2', 'Pull3', 'Pull4', 'Pull5', 'Pull6']
TIMINGS = FIELDS[4:]
TREATMENTS = ('neutral', 'cooperating')
BOOTSTRAP_SEED = 20261006
BOOTSTRAP_REPLICATES = 20000


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def source_validation():
    raw = SOURCE.read_bytes()
    freeze_raw = (HERE / 'protocol-freeze.json').read_bytes()
    freeze = json.loads(freeze_raw)
    assert sha((HERE / 'PROTOCOL.md').read_bytes()) == PROTOCOL_SHA256 == freeze['sha256']
    assert sha(raw) == SOURCE_SHA256 == freeze['source_sha256']
    table = list(csv.reader(io.StringIO(raw.decode()), delimiter='\t'))
    assert table[0] == FIELDS
    # The earlier independent DOM receipt applies to the original blank header.
    canonical_table = [r.copy() for r in table]
    canonical_table[0][0] = ''
    canonical = json.dumps(canonical_table, separators=(',', ':'), ensure_ascii=False).encode('ascii')
    fnv = 14695981039346656037
    for byte in canonical:
        fnv = ((fnv ^ byte) * 1099511628211) % (2**64)
    assert len(canonical) == 3119 and f'{fnv:x}' == 'df8ebe2256185e27'
    return table, dict(source_path=str(SOURCE.relative_to(REPO)),
        source_sha256=SOURCE_SHA256, protocol_sha256=PROTOCOL_SHA256,
        protocol_freeze_sha256=sha(freeze_raw), model_sha256=sha(Path(__file__).read_bytes()),
        source_kind='Derived complete displayed HTML preview; original CSV bytes unavailable.',
        original_csv_verified=False, displayed_data_rows=len(table)-1,
        canonical_ascii_length=len(canonical), fnv1a64=f'{fnv:x}',
        header_adaptation='Blank first header renamed preview_row; other cell strings retained.',
        source_url='https://datadryad.org/dataset/doi:10.5061/dryad.h18931zjd',
        protocol_frozen_at_utc=freeze['frozen_at_utc'])


def parse(table):
    errors = []
    raw_rows = []
    parsed = []
    missing = {field: [] for field in FIELDS}
    row_ids = Counter()
    paired = defaultdict(dict)
    duplicates = []
    for line_number, cells in enumerate(table[1:], 2):
        if len(cells) != len(FIELDS):
            errors.append(dict(line=line_number, reason='wrong_cell_count', cells=cells))
            continue
        raw = dict(zip(FIELDS, cells))
        raw_rows.append(raw)
        row = dict(raw)
        for field, cell in raw.items():
            if cell == 'NA':
                missing[field].append(raw['preview_row'])
        for field in ('preview_row','pull_f'):
            if not re.fullmatch(r'[0-9]+', raw[field]):
                errors.append(dict(line=line_number, field=field, raw=raw[field], reason='invalid_required_integer'))
                row[field] = None
            else:
                row[field] = int(raw[field])
        if not raw['ratID'] or raw['ratID']=='NA':
            errors.append(dict(line=line_number, reason='missing_focal_id'))
        if raw['treatment'] not in TREATMENTS:
            errors.append(dict(line=line_number, reason='unexpected_treatment', value=raw['treatment']))
        for field in TIMINGS:
            if raw[field] == 'NA':
                row[field] = None
                continue
            try:
                value = Decimal(raw[field])
                if not value.is_finite() or value < 0:
                    raise InvalidOperation
                row[field] = int(value) if value == value.to_integral_value() else float(value)
            except InvalidOperation:
                row[field] = None
                errors.append(dict(line=line_number, field=field, raw=raw[field], reason='invalid_numeric_timing'))
        row_ids[row['preview_row']] += 1
        if raw['treatment'] in paired[raw['ratID']]:
            duplicates.append(dict(ratID=raw['ratID'], treatment=raw['treatment'], preview_row=raw['preview_row']))
        else:
            paired[raw['ratID']][raw['treatment']] = row
        parsed.append(row)
    duplicate_row_ids = [key for key,count in row_ids.items() if count > 1]
    incomplete = {key: sorted(set(TREATMENTS)-set(rows)) for key,rows in paired.items() if set(rows)!=set(TREATMENTS)}
    if duplicate_row_ids:
        errors.append(dict(reason='duplicate_row_identifiers', values=duplicate_row_ids))
    if duplicates:
        errors.append(dict(reason='duplicate_focal_treatment', values=duplicates))
    if incomplete:
        errors.append(dict(reason='incomplete_pairs', values=incomplete))
    if len(parsed)!=48 or len(paired)!=24 or set(row_ids)!=set(range(1,49)):
        errors.append(dict(reason='unexpected_preview_structure', row_count=len(parsed), focal_count=len(paired)))
    audit = dict(valid=not errors, invalid_fields_or_structure=errors,
        raw_data_rows=len(raw_rows), focal_ids=sorted(paired),
        duplicated_row_identifiers=duplicate_row_ids, duplicated_focal_treatments=duplicates,
        incomplete_pairs=incomplete, missing_cells={k:dict(count=len(v), preview_rows=v) for k,v in missing.items()},
        treatment_row_counts=dict(Counter(r['treatment'] for r in raw_rows)))
    return raw_rows, parsed, paired, audit


def count_pairs(paired):
    return [dict(ratID=focal,
                 neutral=pair['neutral']['pull_f'], cooperating=pair['cooperating']['pull_f'],
                 difference=pair['cooperating']['pull_f']-pair['neutral']['pull_f'],
                 source_rows={t:pair[t]['preview_row'] for t in TREATMENTS})
            for focal,pair in sorted(paired.items())]


def descriptive(pairs):
    values = [r['difference'] for r in pairs]
    n = len(values)
    totals = {t:sum(p[t] for p in pairs) for t in TREATMENTS}
    return dict(n=n, units='Pulls per focal rat per seven-minute session; cooperating minus neutral.',
        treatment_totals=totals, treatment_means={t:totals[t]/n for t in TREATMENTS},
        treatment_means_exact={t:str(Fraction(totals[t],n)) for t in TREATMENTS},
        difference_sum=sum(values), mean_difference=sum(values)/n,
        mean_difference_exact=str(Fraction(sum(values),n)),
        median_difference=statistics.median(values), sample_sd_difference=statistics.stdev(values),
        positive_differences=sum(v>0 for v in values), negative_differences=sum(v<0 for v in values),
        zero_differences=sum(v==0 for v in values),
        zero_count_sessions={t:sum(p[t]==0 for p in pairs) for t in TREATMENTS})


def sign_flip(values):
    distribution = Counter({0:1})
    for value in values:
        next_distribution = Counter()
        for total, weight in distribution.items():
            next_distribution[total+value] += weight
            next_distribution[total-value] += weight
        distribution = next_distribution
    denominator = 2**len(values)
    assert sum(distribution.values()) == denominator
    observed = abs(sum(values))
    numerator = sum(weight for total,weight in distribution.items() if abs(total)>=observed)
    return dict(observed_absolute_sum=observed, numerator=numerator, denominator=denominator,
        probability=numerator/denominator, exact_fraction=str(Fraction(numerator,denominator)),
        reference='Equiprobable independent paired signs; equality included; zero-pair multiplicities retained.',
        assignment_exact=False)


def binomial_sign(values):
    positive = sum(v>0 for v in values)
    negative = sum(v<0 for v in values)
    m = positive+negative
    denominator = 2**m
    numerator = min(denominator, 2*sum(math.comb(m,k) for k in range(min(positive,negative)+1)))
    return dict(nonzero_pairs=m, positive=positive, negative=negative, ties=len(values)-m,
        numerator=numerator, denominator=denominator, probability=numerator/denominator,
        exact_fraction=str(Fraction(numerator,denominator)),
        reference='Conditional independent equiprobable signs among nonties; not assumption-free causal inference.')


def quantile(sorted_values, p):
    index = (len(sorted_values)-1)*p
    low = math.floor(index)
    high = math.ceil(index)
    weight = index-low
    return sorted_values[low]*(1-weight)+sorted_values[high]*weight


def bootstrap(values):
    n = len(values)
    rng = random.Random(BOOTSTRAP_SEED)
    means = [sum(values[rng.randrange(n)] for _ in range(n))/n for _ in range(BOOTSTRAP_REPLICATES)]
    ordered = sorted(means)
    return dict(unit='Complete focal-animal pair', seed=BOOTSTRAP_SEED, replicates=BOOTSTRAP_REPLICATES,
        sorting='Focal identifiers lexicographic before sampling.',
        sampling='random.Random(seed); n randrange(n) draws with replacement per resample.',
        interval_kind='Exploratory animal-paired percentile interval; unadjusted.',
        quantile_rule='Linear interpolation at index (B-1)*p.',
        probabilities=[0.025,0.975], interval=[quantile(ordered,0.025),quantile(ordered,0.975)],
        mean_sequence_sha256=sha(json.dumps(means,separators=(',',':')).encode()),
        assumption='Focal animals approximate independent comparable sampling units; donor reuse/common influences unknown.')


def latency_audit(rows):
    zero = [r for r in rows if r['pull_f']==0]
    positive = [r for r in rows if r['pull_f']>0]
    ranges = {}
    for label, values in [('zero_count',[r['lat_f'] for r in zero if r['lat_f'] is not None]),
                          ('positive_count',[r['lat_f'] for r in positive if r['lat_f'] is not None])]:
        ranges[label] = dict(n_numeric=len(values), minimum=min(values) if values else None,
                             maximum=max(values) if values else None)
    return dict(scope='Coding audit only; no latency treatment estimate or survival-model fit.',
        zero_count_rows=len(zero), zero_count_with_420=sum(r['lat_f']==420 for r in zero),
        zero_count_not_420=[r['preview_row'] for r in zero if r['lat_f']!=420],
        positive_count_with_420=[r['preview_row'] for r in positive if r['lat_f']==420],
        first_timing_ranges=ranges,
        missing_timing_cells={f:[r['preview_row'] for r in rows if r[f] is None] for f in TIMINGS},
        later_420_cell_counts={f:sum(r[f]==420 for r in rows) for f in TIMINGS[1:]},
        timing_outside_session=[dict(preview_row=r['preview_row'],field=f,value=r[f])
            for r in rows for f in TIMINGS if r[f] is not None and r[f]>420],
        warning='420 on a no-pull row is not treated as an observed first event; later timing meaning not inferred without raw Readme.',
        published_discrepancy='Main article: latency Wilcoxon p=.003; supplement Table S6: Cox p=.048; unresolved.')


def omission_family(pairs):
    results = []
    for omitted in pairs:
        retained = [p for p in pairs if p['ratID']!=omitted['ratID']]
        values = [p['difference'] for p in retained]
        results.append(dict(omitted_ratID=omitted['ratID'], descriptive=descriptive(retained),
                            sign_flip=sign_flip(values), binomial_sign=binomial_sign(values)))
    ranges = {}
    for name,group,field in [('mean_difference','descriptive','mean_difference'),
                             ('sign_flip_probability','sign_flip','probability'),
                             ('binomial_sign_probability','binomial_sign','probability')]:
        values = [r[group][field] for r in results]
        ranges[name] = dict(minimum=min(values), maximum=max(values))
    return dict(scope='All single-focal omissions; none selected to reconstruct unexplained author exclusion.',
                omissions=results, ranges=ranges)


def main():
    table, provenance = source_validation()
    raw, parsed, paired, audit = parse(table)
    result = dict(status='pending', scope='Retrospective paired reanalysis of complete visible experiment-4 preview.',
        provenance=provenance, python_version=sys.version, validation=audit,
        source_cell_strings=raw, parsed_rows=parsed)
    if not audit['valid']:
        result['status']='invalid_input_requires_documented_protocol_amendment'
        (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
        raise SystemExit('Invalid input structure: no numerical acceptance; inspect results.json.')
    pairs = count_pairs(paired)
    values = [p['difference'] for p in pairs]
    result.update(status='computed_pending_independent_review', pairs=pairs,
        descriptive=descriptive(pairs), bootstrap=bootstrap(values),
        sign_flip=sign_flip(values), binomial_sign=binomial_sign(values),
        single_animal_omissions=omission_family(pairs), latency_audit=latency_audit(parsed),
        limitations=[
            'Published results and prior preview descriptives were known before the local computational freeze.',
            'The original CSV was not downloaded or byte-verified; all displayed cells were independently checked.',
            'Published analysis n=23 versus available complete pairs n=24 is unexplained; all pairs retained.',
            'No donor/recipient IDs, session dates or treatment sequence: additional clustering/carryover unresolved.',
            'The count contrast concerns the assigned donor situation, bundling cooperation, access, activity and other changes.',
            'Contemporaneous remote cue influences recipient-directed action; no retained recipient-specific cognition identified.',
            'No measurement of ingestion, welfare, metabolic cost, normative grounds, governance or AI alignment.',
            'Experiment-3 preview incomplete: no numerical experiment-3 analysis.'])
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], descriptive=result['descriptive'],
        bootstrap_interval=result['bootstrap']['interval'], sign_flip=result['sign_flip'],
        binomial_sign=result['binomial_sign'], omission_ranges=result['single_animal_omissions']['ranges'],
        source_sha256=SOURCE_SHA256, protocol_sha256=PROTOCOL_SHA256),indent=2))


if __name__=='__main__':
    main()
