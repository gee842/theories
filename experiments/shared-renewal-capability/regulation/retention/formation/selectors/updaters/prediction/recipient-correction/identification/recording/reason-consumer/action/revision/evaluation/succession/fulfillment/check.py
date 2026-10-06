"""Check PROTOCOL.md predictions P1-P7 against the first producer run.

Reads saved outputs only: results.json.gz, reporting.json and the accepted
study's reporting.json. Writes check.json. A failed prediction is reported,
never repaired.
"""
from fractions import Fraction as Q
from pathlib import Path
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
files = json.loads((HERE / 'result-files.json').read_text())
packed = (HERE / 'results.json.gz').read_bytes()
assert hashlib.sha256(packed).hexdigest() == files['compressed_sha256']
data = json.loads(gzip.decompress(packed))
accepted = json.loads((HERE.parent / 'reporting.json').read_text())['cases']
FROZEN = list(accepted)
ARMS = data['arms']


def paths(case, arm):
    for prod, d in data['cases'][case]['arms'][arm]['producers'].items():
        for i, p in enumerate(d['paths']):
            yield prod, i, p


def paired(case, arm):
    """Yield (shared path, arm path) pairs on identical donor paths."""
    for prod, d in data['cases'][case]['arms']['shared']['producers'].items():
        other = data['cases'][case]['arms'][arm]['producers'][prod]['paths']
        for a, b in zip(d['paths'], other):
            assert a['predecessor_ref'] == b['predecessor_ref']
            yield prod, a, b


results = {}

# P1: regression of the shared arm on frozen cases.
EXCLUDE = {'retained', 'new_spent'}
mismatch = []
for case in FROZEN:
    for arm in accepted[case]:
        for prod, old in accepted[case][arm].items():
            if arm != 'shared':
                continue
            new = data['cases'][case]['arms']['shared']['producers'][prod]['metrics']
            for key, value in old.items():
                if key in EXCLUDE:
                    continue
                if Q(new[key]) != Q(value):
                    mismatch.append([case, prod, key, value, new[key]])
results['P1_shared_regression'] = dict(passed=not mismatch, compared_cases=len(FROZEN), mismatches=mismatch[:20],
                                       mismatch_count=len(mismatch))

# P2: k=1 withholds wherever shared attempts, claim met, n/command equal.
viol = []; n_att = 0; source_diff = []
for case in data['cases']:
    for prod, a, b in paired(case, 'fulfill_k1'):
        ma, mb = a['metrics'], b['metrics']
        if ma['selected_attempted']:
            n_att += 1
            if mb['positive_assessment'] or not mb['claim_met_end_k1'] or ma['n'] != mb['n'] \
                    or ma['supported_child_command'] != mb['supported_child_command']:
                viol.append([case, prod, a['predecessor_ref']])
            if ma['selected_completed']:
                source_diff.append(mb['source'] - ma['source'])
results['P2_k1_withdrawal'] = dict(passed=not viol and n_att > 0, shared_attempts=n_att, violations=viol[:20],
                                   violation_count=len(viol),
                                   source_gain_values=sorted(set(source_diff)))

# P3: evidence sensitivity at k=2 under faithful channels.
viol = []; seen = {'withhold_both_captured': 0, 'deliver_first_missed': 0}
faithful = [c for c in data['cases'] if c in FROZEN and data['cases'][c]['config']['feedback'] == ['faithful'] * 3]
for case in faithful:
    for arm in ('fulfill_k2_deliver', 'fulfill_k2_hold'):
        for prod, a, b in paired(case, arm):
            ma, mb = a['metrics'], b['metrics']
            if not ma['positive_assessment']:
                continue
            both = mb['probe_captures'] == 2
            first_missed = not mb['first_probe_capture']
            if both and mb['positive_assessment']:
                viol.append([case, arm, prod, a['predecessor_ref'], 'delivered after both captured'])
            if both and not mb['positive_assessment']:
                seen['withhold_both_captured'] += 1
            if first_missed and mb['probe_captures'] == 1:
                if not mb['positive_assessment']:
                    viol.append([case, arm, prod, a['predecessor_ref'], 'withheld while first missed'])
                else:
                    seen['deliver_first_missed'] += 1
            if mb['excess_k2']:
                viol.append([case, arm, prod, a['predecessor_ref'], 'excess'])
results['P3_k2_evidence_sensitivity'] = dict(passed=not viol and all(seen.values()), counts=seen,
                                             violations=viol[:20], violation_count=len(viol))

# P4: unknown status under a missing first channel.
viol = []; counts = dict(unknown=0, deliver_excess=0, hold_unmet=0)
for case in ('first_feedback_missing_changed', 'first_feedback_missing_stable'):
    for arm in ('fulfill_k2_deliver', 'fulfill_k2_hold'):
        for prod, a, b in paired(case, arm):
            ma, mb = a['metrics'], b['metrics']
            if not ma['positive_assessment']:
                continue
            if not mb['status_unknown']:
                viol.append([case, arm, prod, a['predecessor_ref'], 'status not unknown'])
                continue
            counts['unknown'] += 1
            first = mb['first_probe_capture']
            if arm.endswith('deliver'):
                if bool(mb['excess_k2']) != bool(first and mb['selected_capture']):
                    viol.append([case, arm, prod, a['predecessor_ref'], 'excess mismatch'])
                counts['deliver_excess'] += mb['excess_k2']
            else:
                if bool(mb['withheld_while_unmet_k2']) != (not first):
                    viol.append([case, arm, prod, a['predecessor_ref'], 'unmet mismatch'])
                counts['hold_unmet'] += mb['withheld_while_unmet_k2']
results['P4_unknown_status'] = dict(passed=not viol and counts['deliver_excess'] > 0 and counts['hold_unmet'] > 0,
                                    counts=counts, violations=viol[:20], violation_count=len(viol))

# P5: forged register record misleads.
cnt = 0; viol = []
for arm in ('fulfill_k2_deliver', 'fulfill_k2_hold'):
    for prod, a, b in paired('register_receipt_forged', arm):
        ma, mb = a['metrics'], b['metrics']
        if ma['positive_assessment'] and not mb['first_probe_capture']:
            if not mb['positive_assessment'] and mb['withheld_while_unmet_k2']:
                cnt += 1
            else:
                viol.append([arm, prod, a['predecessor_ref']])
results['P5_forged_record'] = dict(passed=cnt > 0 and not viol, misled_histories=cnt, violations=viol[:20])

# P6: k=3 matches shared choices.
viol = []
for case in data['cases']:
    for prod, a, b in paired(case, 'fulfill_k3'):
        if a['metrics']['positive_assessment'] != b['metrics']['positive_assessment']:
            viol.append([case, prod, a['predecessor_ref']])
results['P6_k3_matches_shared'] = dict(passed=not viol, violations=viol[:20], violation_count=len(viol))

# P7: unprovisioned register.
viol = []
for prod, a, b in paired('register_unprovisioned', 'fulfill_k2_deliver'):
    if a['metrics']['positive_assessment'] != b['metrics']['positive_assessment']:
        viol.append(['deliver', prod, a['predecessor_ref']])
for prod, a, b in paired('register_unprovisioned', 'fulfill_k2_hold'):
    if a['metrics']['positive_assessment'] and b['metrics']['positive_assessment']:
        viol.append(['hold', prod, a['predecessor_ref']])
results['P7_unprovisioned'] = dict(passed=not viol, violations=viol[:20], violation_count=len(viol))

# Mixture summary for the main contrast (variable producer).
summary = {}
for case in ('changed', 'stable', 'first_feedback_missing_changed', 'first_feedback_missing_stable',
             'register_receipt_forged', 'late_efficacy_change'):
    summary[case] = {arm: {k: data['cases'][case]['arms'][arm]['producers']['variable']['metrics'][k]
                           for k in ('positive_assessment', 'selected_capture', 'recipient_gain', 'source',
                                     'claim_met_end_k1', 'claim_met_end_k2', 'excess_k1', 'excess_k2',
                                     'withheld_while_unmet_k2', 'status_fulfilled', 'status_pending',
                                     'status_unknown')}
                     for arm in ARMS}

out = dict(results_sha256=files['compressed_sha256'], counts=files['counts'],
           passed=all(r['passed'] for r in results.values()), predictions=results, variable_summary=summary)
(HERE / 'check.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k: v['passed'] for k, v in results.items()}, indent=1), out['passed'])
