#!/usr/bin/env python3
"""Independent TSV arithmetic and meet-in-the-middle reference audit.

Does not import the analysis implementation. The sign distribution is counted
by half-word enumeration and binary searches, independently of its integer DP.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
from itertools import product
from bisect import bisect_left, bisect_right
import csv
import hashlib
import json
import math
import random
import statistics

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/experiment4-preview.tsv'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def signflip(xs):
    middle = len(xs) // 2
    left = [sum(s*x for s, x in zip(word, xs[:middle]))
            for word in product((-1, 1), repeat=middle)]
    right = sorted(sum(s*x for s, x in zip(word, xs[middle:]))
                   for word in product((-1, 1), repeat=len(xs)-middle))
    threshold = abs(sum(xs))
    denominator = 2**len(xs)
    if threshold == 0:
        numerator = denominator
    else:
        numerator = sum(bisect_right(right, -threshold-a) + len(right)
                        - bisect_left(right, threshold-a) for a in left)
    return {'numerator': numerator, 'denominator': denominator,
            'probability': numerator/denominator}


def summarize(xs):
    signs = [sum(x > 0 for x in xs), sum(x < 0 for x in xs), sum(x == 0 for x in xs)]
    m = sum(signs[:2])
    numerator = min(2**m, 2*sum(math.comb(m, k) for k in range(min(signs[:2])+1)))
    return {'n': len(xs), 'sum': sum(xs), 'mean': float(Fraction(sum(xs), len(xs))),
            'median': statistics.median(xs), 'stdev': statistics.stdev(xs),
            'positive_negative_zero': signs, 'signflip': signflip(xs),
            'sign': {'numerator': numerator, 'denominator': 2**m,
                     'probability': numerator/(2**m)}}


def bootstrap(xs):
    rng = random.Random(20261006)
    # Integer sums sorted before division give the declared interpolated mean
    # quantiles, without borrowing the primary implementation's quantile helper.
    totals = sorted(sum(xs[rng.randrange(len(xs))] for _ in xs) for _ in range(20000))
    bounds = []
    for p in (Fraction(1, 40), Fraction(39, 40)):
        place = 19999*p
        lower = place.numerator // place.denominator
        residual = place-lower
        value = (1-residual)*totals[lower] + residual*totals[min(lower+1, 19999)]
        bounds.append(float(value/len(xs)))
    return bounds


def compare_results(expected, body, header):
    result = json.loads((HERE/'results.json').read_text())
    assert result['provenance']['source_sha256'] == sha(SOURCE)
    assert result['provenance']['protocol_sha256'] == sha(HERE/'PROTOCOL.md')
    assert result['provenance']['model_sha256'] == sha(HERE/'analysis.py')
    assert result['provenance']['protocol_freeze_sha256'] == sha(HERE/'protocol-freeze.json')
    assert result['validation']['valid'] and not result['validation']['invalid_fields_or_structure']
    assert result['source_cell_strings'] == [dict(zip(header, r)) for r in body]
    for raw, parsed in zip(result['source_cell_strings'], result['parsed_rows'], strict=True):
        for key in header:
            if key in ('ratID', 'treatment'):
                assert parsed[key] == raw[key]
            elif raw[key] == 'NA':
                assert parsed[key] is None
            else:
                assert parsed[key] == float(raw[key])
    assert [p['ratID'] for p in result['pairs']] == expected['ids']
    for pair in result['pairs']:
        e = expected['paired_counts'][pair['ratID']]
        assert pair['neutral'] == e['neutral'] and pair['cooperating'] == e['cooperating']
        assert pair['difference'] == e['cooperating']-e['neutral']

    def compare_summary(e, desc, flip, sign):
        for a, b in [('n', 'n'), ('sum', 'difference_sum'), ('mean', 'mean_difference'),
                     ('median', 'median_difference'), ('stdev', 'sample_sd_difference')]:
            assert math.isclose(e[a], desc[b], rel_tol=1e-13, abs_tol=1e-13)
        assert e['positive_negative_zero'] == [desc[k] for k in
            ('positive_differences', 'negative_differences', 'zero_differences')]
        for name, actual in [('signflip', flip), ('sign', sign)]:
            assert all(e[name][k] == actual[k] for k in ('numerator', 'denominator', 'probability'))

    compare_summary(expected['primary'], result['descriptive'], result['sign_flip'], result['binomial_sign'])
    assert result['descriptive']['treatment_totals'] == expected['totals']
    assert result['bootstrap']['seed'] == 20261006 and result['bootstrap']['replicates'] == 20000
    assert result['bootstrap']['interval'] == expected['primary']['bootstrap_95_percentile']
    seen = set()
    for case in result['single_animal_omissions']['omissions']:
        key = case['omitted_ratID']
        assert key not in seen
        seen.add(key)
        compare_summary(expected['all_single_omissions'][key], case['descriptive'],
                        case['sign_flip'], case['binomial_sign'])
    assert seen == set(expected['ids'])
    latency = result['latency_audit']
    assert latency['zero_count_rows'] == expected['latency_coding']['zero_pull_rows']
    assert latency['zero_count_with_420'] == expected['latency_coding']['zero_pull_rows_at_420']
    assert not latency['timing_outside_session']
    assert {k: len(v) for k, v in latency['missing_timing_cells'].items() if v} == expected['latency_coding']['missing_cells']
    return {'status': 'pass', 'raw_rows_and_parsed_rows_checked': 48, 'paired_animals_checked': 24,
            'complete_single_omissions_checked': 24, 'exact_reference_calculations_checked': 50,
            'bootstrap_replay': '20,000 complete-animal draws and declared percentile interval agree',
            'analysis_sha256': sha(HERE/'analysis.py'), 'results_sha256': sha(HERE/'results.json')}


def main():
    freeze = json.loads((HERE/'protocol-freeze.json').read_text())
    assert sha(HERE/'PROTOCOL.md') == freeze['sha256']
    assert sha(SOURCE) == freeze['source_sha256']
    with SOURCE.open(newline='') as stream:
        cells = list(csv.reader(stream, delimiter='\t'))
    assert len(cells) == 49 and set(map(len, cells)) == {10}
    header, *body = cells
    assert header == ['preview_row', 'ratID', 'treatment', 'pull_f', 'lat_f',
                      'Pull2', 'Pull3', 'Pull4', 'Pull5', 'Pull6']
    canonical = [['']+header[1:]]+body
    raw = json.dumps(canonical, separators=(',', ':'), ensure_ascii=True).encode('ascii')
    h = 0xcbf29ce484222325
    for b in raw:
        h = ((h ^ b)*0x100000001b3) & ((1 << 64)-1)
    assert len(raw) == 3119 and f'{h:016x}' == 'df8ebe2256185e27'
    assert [int(r[0]) for r in body] == list(range(1, 49))
    pairs = {}
    missing = Counter()
    zeros = horizon_zeros = 0
    for row in body:
        r = dict(zip(header, row))
        key = r['ratID']
        group = pairs.setdefault(key, {})
        assert r['treatment'] in ('neutral', 'cooperating') and r['treatment'] not in group
        count = int(r['pull_f'])
        assert str(count) == r['pull_f'] and count >= 0
        group[r['treatment']] = count
        for col in header[4:]:
            if r[col] == 'NA': missing[col] += 1
            else: assert 0 <= float(r[col]) <= 420
        if count == 0:
            zeros += 1
            horizon_zeros += r['lat_f'] == '420'
    assert len(pairs) == 24 and all(set(v) == {'neutral', 'cooperating'} for v in pairs.values())
    ids = sorted(pairs)
    differences = [pairs[k]['cooperating']-pairs[k]['neutral'] for k in ids]
    primary = summarize(differences)
    primary['bootstrap_95_percentile'] = bootstrap(differences)
    omissions = {k: summarize(differences[:i]+differences[i+1:]) for i, k in enumerate(ids)}
    out = {'status': 'pass: independent arithmetic and primary-output comparison agree',
           'protocol_sha256': sha(HERE/'PROTOCOL.md'), 'source_sha256': sha(SOURCE),
           'checker_sha256': sha(Path(__file__)), 'source_cells_fnv1a64': f'{h:016x}',
           'method': 'Independent CSV parsing, rational descriptives, meet-in-the-middle exact sign enumeration, binomial coefficient counting and separately coded bootstrap replay.',
           'primary': primary, 'paired_counts': pairs, 'ids': ids, 'differences': differences,
           'totals': {t: sum(pairs[k][t] for k in ids) for t in ('neutral', 'cooperating')},
           'latency_coding': {'zero_pull_rows': zeros, 'zero_pull_rows_at_420': horizon_zeros,
                              'missing_cells': dict(missing)},
           'all_single_omissions': omissions,
           'scope': 'Arithmetic audit of a derived public preview; no original-CSV verification or validation of sampling, assignment or cognitive interpretation assumptions.'}
    out['results_comparison'] = compare_results(out, body, header)
    (HERE/'independent-verification.json').write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'n': primary['n'], 'mean': primary['mean'], 'bootstrap': primary['bootstrap_95_percentile'],
                      'signflip': primary['signflip'], 'sign': primary['sign'], 'omissions': len(omissions)}))


if __name__ == '__main__':
    main()
