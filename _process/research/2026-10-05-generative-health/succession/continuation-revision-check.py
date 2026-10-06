"""Extract accepted histories for a continuation corollary; run no model dynamics."""
from pathlib import Path
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
REL = Path('experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/inquiry-revision')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    folder = ROOT / REL
    receipt = json.loads((folder / 'independent-check.json').read_text())
    assert receipt['status'] == 'accepted_independent_finite_replay'
    bindings = {name: digest(ROOT / name) == expected
                for name, expected in receipt['source_sha256'].items()}
    assert all(bindings.values()), 'Accepted receipt no longer binds current artifacts'
    data = json.loads(gzip.decompress((folder / 'results.json.gz').read_bytes()))
    extracted = {}
    for name in ['faithful', 'one_history', 'zero_history', 'sham', 'opposed', 'mixed']:
        history = data['histories'][name]
        suffix = history['trace'][history['entry_index']:]
        rows = [dict(event=row['event'], stock=row['state']['core']['recipient'],
                     fuel=row['state']['core']['fuel'],
                     count=row['state']['native']['count'],
                     limit=row['state']['controls']['training_limit'],
                     port=row['state']['port']['mode'],
                     acquisition_phase=row['state']['native']['phase'],
                     physical_phase=row['state']['physical']['core_phase'],
                     occupied=sum(link is not None for link in row['state']['links']))
                for row in suffix]
        extracted[name] = dict(entry_index=history['entry_index'], suffix=rows,
                               earlier_prefix_minimum_stock=min(row['state']['core']['recipient'] for row in history['trace'][:history['entry_index'] + 1]),
                               minimum_stock=min(row['stock'] for row in rows),
                               result=history['result'])
    positive = extracted['faithful']
    assert positive['suffix'][0]['stock'] == 36
    assert positive['minimum_stock'] == 36 and positive['result']['affected'] == 46
    assert positive['result']['limit'] == 4 and positive['result']['service']
    assert positive['result']['fuel'] == 1 and positive['result']['material'] == 68
    assert all(row['count'] == 4 for row in positive['suffix'])
    one = extracted['one_history']
    assert one['suffix'][0]['stock'] == 38 and one['suffix'][0]['occupied'] == 1
    assert one['earlier_prefix_minimum_stock'] == 36
    assert one['suffix'][0]['physical_phase'] == one['suffix'][0]['acquisition_phase'] == 'ready'
    assert one['suffix'][0]['port'] == 'idle'
    entry = data['histories']['one_history']['trace'][one['entry_index']]['state']
    assert entry['controls']['assessment_implementation'] == 'graph'
    assert not entry['controls']['recipient_filter']
    transmitted = entry['native']['n'] * sum(link['sign'] for link in entry['links'] if link is not None)
    assert 10 * transmitted == 40 and not 10 * transmitted > 64
    one['inherited_assessment_arithmetic'] = dict(transmission=transmitted, favors_response=False,
                                                 scope='Evaluation of the unchanged formula if admitted; no counterfactual history executed.')
    assert one['result']['limit'] == 6 and not one['result']['service']
    assert any(row['event'] == 'inquiry.commit.blocked' for row in one['suffix'])
    for name in ['opposed', 'mixed']:
        assert extracted[name]['result']['limit'] == 4
        assert not extracted[name]['result']['service']
    assert extracted['sham']['result']['limit'] == 6
    old = json.loads((HERE / 'continuity-correction-checks.json').read_text())
    old_bindings = {name: digest(ROOT / name) == expected
                    for name, expected in old['source_versions_sha256'].items()}
    assert all(old_bindings.values())
    result = dict(date='2026-10-06',
                  scope='Accepted saved-history extraction and artifact binding; no transition execution, empirical test or Lean certification.',
                  input_hashes={str((REL / name)): digest(folder / name)
                                for name in ['results.json.gz', 'independent-check.json', 'model.py']},
                  accepted_receipt_bindings=bindings, original_proof_source_bindings=old_bindings,
                  cases=extracted,
                  corollary_scope='The recorded new witness preserves every stock floor f <= 36. The old universal first-debit claim and its b >= 2 generalization are source-level arguments in the companion prose, not proved by finite extraction.',
                  passed=True)
    (HERE / 'continuation-revision-checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=True, saved_histories=len(extracted),
                          accepted_bindings=len(bindings), original_bindings=len(old_bindings),
                          primary_minimum_stock=positive['minimum_stock'],
                          primary_final_stock=positive['result']['affected'],
                          one_occupied_commit='blocked', model_executed=False)))


if __name__ == '__main__':
    main()
