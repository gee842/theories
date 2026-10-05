#!/usr/bin/env python3
"""Execute prespecified all-history preparation and updater comparisons."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from model import ARMS, cases, prepare, evolve, readouts, OLD_PATH, old

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[6]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    files = [ROOT/n for n in ('model.py', 'check.py', 'PROTOCOL.md')]+[OLD_PATH, old.ARITHMETIC]
    hashes = {str(p.relative_to(REPO)): sha(p) for p in files}
    runs = {}
    for name, law in cases().items():
        ends, prep_states = prepare(law)
        mass = sum((Q(x['probability']) for x in ends if x['commissioned']), Q(0))
        assert mass == Q(2, 9)
        expected_prep_spend = sum(Q(x['probability'])*x['preparation_spent'] for x in ends)
        failed_energy = sum(Q(x['probability'])*x['remaining_energy'] for x in ends if not x['commissioned'])
        arms = {}
        reference = {}
        for arm in ARMS:
            unconditional = None
            entry_records = []
            retained_remainder = Q(0)
            for entrance in ends:
                if not entrance['commissioned']:
                    continue
                weight = Q(entrance['probability'])
                table, sizes = evolve(law, arm, entrance['reserve'])
                if arm == 'variable': reference[tuple(entrance['state'])] = table
                if arm == 'hierarchical': assert table == reference[tuple(entrance['state'])]
                values = readouts(law, table, entrance['reserve'])
                if unconditional is None: unconditional = dict.fromkeys(values, Q(0))
                for k, v in values.items(): unconditional[k] += weight*v
                retained_remainder += weight*(entrance['remainder']+
                                                law.packet*(entrance['packets']-law.horizon))
                entry_records.append({'reserve': entrance['reserve'], 'probability': str(weight),
                                      'state_counts': sizes,
                                      'conditional_exact': {k: str(v) for k, v in values.items()}})
            whole_spent = expected_prep_spend+mass*law.adapter+unconditional['post_spent']
            assert (unconditional['reserve']+unconditional['post_spill']+retained_remainder
                    +failed_energy+whole_spent == law.initial_common+law.initial_source)
            arms[arm] = {'unconditional_exact': {k: str(v) for k, v in unconditional.items()},
                         'unconditional_decimal': {k: float(v) for k, v in unconditional.items()},
                         'whole_expected_spent': str(whole_spent),
                         'retained_failed_energy': str(failed_energy),
                         'retained_source_remainder': str(retained_remainder),
                         'entrances': entry_records}
            print(name, arm, 'capture=',float(unconditional['captures']),
                  'updater_witness=',float(unconditional['p_updater_revision']),
                  'inherited=',float(unconditional['inherited_selector_renewals']), flush=True)
        runs[name] = {'law': law.record(), 'preparation': ends,
                      'preparation_state_count': prep_states,
                      'commissioned_probability': str(mass), 'arms': arms}
    # The old low-stock fixture is a preserved obstruction, not reset to F=14.
    from dataclasses import replace
    from model import Law
    low = replace(Law(), initial_common=4, horizon=0, reversals=())
    low_ends, _ = prepare(low)
    assert all(not e['commissioned'] for e in low_ends)
    assert all(sha(p)==hashes[str(p.relative_to(REPO))] for p in files)
    result = {'status':'passed', 'arithmetic':'exact fractions', 'source_sha256':hashes,
              'cases':runs, 'old_depleted_fixture':{'law':low.record(),'outcomes':low_ends},
              'scope':'supplied assembly/conversion law; no empirical or historical-priority claim'}
    (ROOT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Passed',len(runs)*len(ARMS),'all-preparation comparison arms.')


if __name__ == '__main__': main()
