"""Independent exact arithmetic reconstruction from individual citizen records."""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import math

from scipy.stats import t

ROOT = Path(__file__).resolve().parent


def verify(number, treatment):
    source = ROOT/'data'/f'Experiment_{number}.tab'
    with source.open() as h:
        rows = list(csv.DictReader(h, delimiter='\t'))
    citizen_groups = defaultdict(list)
    authorities = {}
    for r in rows:
        key = (r['session'], int(r['period']), int(r['group']))
        if int(r['z_isenforcer']):
            assert key not in authorities
            authorities[key] = r
        else:
            citizen_groups[key].append(r)
    assert set(citizen_groups) == set(authorities)
    scores = defaultdict(list)
    audit_groups = {}
    for key, citizens in citizen_groups.items():
        assert len(citizens) == 4
        a = authorities[key]
        total = sum(int(r['p_contributedtopg']) for r in citizens)
        assert total == int(a['g_totcontributedtopg'])
        z = int(a['g_accuracy'])-int(a['e_biginvestment']) if number == 1 else int(a['g_authoritypaidfrompg'])
        assert z in (0, 1)
        score = Fraction((2*z-1)*(total-2), 2)
        scores[key[0]].append(score)
        audit_groups[key] = (z, Fraction(total, 4))
    estimates = {s: sum(v)/len(v) for s, v in scores.items()}
    avg = sum(estimates.values())/len(estimates)
    n = len(estimates)
    # Independent variance-of-session-mean calculation, using rational deviations.
    variance_of_mean = sum((x-avg)**2 for x in estimates.values()) / (n*(n-1))
    se = math.sqrt(float(variance_of_mean))
    interval = [float(avg)-t.ppf(.975,n-1)*se, float(avg)+t.ppf(.975,n-1)*se]
    result = json.loads((ROOT/'results'/'analysis.json').read_text())['results'][treatment]
    discrepancies = [abs(float(avg)-result['equal_session_estimate']),
                     abs(se-result['session_standard_error'])]
    discrepancies += [abs(x-y) for x, y in zip(interval, result['approximate_t95_interval'])]
    for r in result['sessions']:
        discrepancies.append(abs(float(estimates[r['session']])-r['estimate']))
    with (ROOT/'results'/f'groups_{number}.csv').open() as h:
        prepared = list(csv.DictReader(h))
    assert len(prepared) == len(audit_groups)
    for r in prepared:
        key = (r['session'], int(r['period']), int(r['group']))
        z, y = audit_groups[key]
        field = 'higher_accuracy' if number == 1 else 'authority_benefits'
        assert int(r[field]) == z and Fraction(r['outcome']) == y
    assert max(discrepancies) < 1e-14
    return {'experiment': number, 'group_periods': len(audit_groups), 'sessions': n,
            'exact_primary_fraction': str(avg), 'estimate': float(avg),
            'exact_session_fractions': {k: str(v) for k, v in estimates.items()},
            'interval': interval, 'max_difference_from_production': max(discrepancies),
            'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}


def main():
    provenance = json.loads((ROOT/'data'/'provenance.json').read_text())
    for row in provenance['files']:
        assert hashlib.sha256((ROOT/'data'/row['file']).read_bytes()).hexdigest() == row['sha256']
    assert hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest() == provenance['protocol_sha256']
    out = {'data_and_protocol_hashes_match': True,
           'results': [verify(1, 'primary_information'), verify(2, 'boundary_authority_beneficiary')],
           'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'limitations': 'Numerical verification; does not verify unobserved assignment execution or few-session interval coverage.'}
    (ROOT/'results'/'independent_verification.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
