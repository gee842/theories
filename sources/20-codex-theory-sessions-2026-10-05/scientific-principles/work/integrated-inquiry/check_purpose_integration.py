"""Independent development-only authority/cash trace checks; no held-out run."""
from pathlib import Path
import hashlib
import json

import integrated_model as model


def event(run, kind, predicate=lambda row: True):
    return next(row for row in run['events'] if row['kind'] == kind and predicate(row))


def audit():
    source = Path(model.__file__)
    before_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    full = model.run(1103, 'emerging', 'full', trace_ledger=True)
    fixed = model.run(1103, 'emerging', 'fixed_mandate', trace_ledger=True)
    hearing = event(full, 'purpose_hearing')
    control_hearing = event(fixed, 'purpose_hearing')
    assert hearing['ballot'] == control_hearing['ballot']
    assert hearing['round'] == control_hearing['round']
    assert hearing['cash'] == control_hearing['cash']
    assert [v['yes'] for v in hearing['ballot']['votes']] == [False, True, True]
    assert hearing['before'] == control_hearing['before'] == 'A_ONLY'
    assert hearing['after'] == 'INCLUDE_B'
    assert control_hearing['after'] == 'A_ONLY'

    unfinished = event(full, 'review_unfunded_check')
    assert unfinished['round'] == hearing['round']
    assert unfinished['mandate'] == 'INCLUDE_B'
    assert unfinished['cash'] < unfinished['required']
    assert not any(e['kind'] == 'review_finished' and e['review'] == unfinished['review']
                   for e in full['events'])
    accepted = event(full, 'review_finished', lambda row: row['rule_changed'])
    assert accepted['round'] > unfinished['round']
    assert accepted['mandate'] == 'INCLUDE_B'
    assert accepted['result']['diagnostic_gain_A_only'] < 0
    assert accepted['result']['diagnostic_gain_inclusive'] > 0
    assert accepted['result']['lower'] > 0
    assert accepted['compiled_fields'] == [[0], [0, 1]]
    assert not accepted['prefix_after']
    assert fixed['rule_changes'] == fixed['mandate_changes'] == 0
    assert full['counts']['A']['errors'] == fixed['counts']['A']['errors'] == 0
    assert full['counts']['B']['errors'] < fixed['counts']['B']['errors']
    post = [row for row in full['timeline'] if row['round'] > accepted['round']]
    assert post and all(row['mandate'] == 'INCLUDE_B' and not row['prefix'] for row in post)
    assert len({row['errors_B'] for row in post}) == 1

    ledger_results = []
    for run in (full, fixed):
        cash = run['initial_cash']
        transactions = run['chronological_ledger']['transactions']
        for tx in transactions:
            assert tx['before'] == cash
            cash += tx['amount'] if tx['direction'] == 'credit' else -tx['amount']
            assert cash == tx['after'] and cash >= 0
        assert cash == run['final_cash']
        assert cash == run['initial_cash'] + run['receipts'] - sum(run['expenses'].values())
        ledger_results.append({'arm': run['arm'], 'transactions_checked': len(transactions),
                               'final_cash': cash, 'errors_B': run['counts']['B']['errors']})
    assert before_hash == hashlib.sha256(source.read_bytes()).hexdigest()
    return {
        'status': 'passed', 'seed': 1103, 'scenario': 'emerging',
        'source_sha256': before_hash, 'paired_case_price': model.paired_case_price(model.Config()),
        'initial_hearing_round': hearing['round'], 'initial_hearing_cash': hearing['cash'],
        'initial_unaffordable_check_required': unfinished['required'],
        'later_acceptance_round': accepted['round'], 'fresh_result': accepted['result'],
        'cash_traces': ledger_results,
        'scope': 'Development trace, represented fixed stakeholder concerns; no independent-agent or ethical-legitimacy claim.'
    }


if __name__ == '__main__':
    result = audit()
    Path(__file__).with_name('purpose-integration-checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
