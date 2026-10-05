"""Independent reconstruction of actual architecture endpoints for learning.

Reuses the already independent preparation/coupling and architecture event
interpreters, explicitly; does not call either production transition function.
The new learning suffix is outside this helper's reference implementation.
"""
from collections import defaultdict
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
_REFERENCES = {}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def parent_references(architecture):
    key = id(architecture)
    if key not in _REFERENCES:
        handoff = load_module('_learning_parent_handoff_'+str(key),
                              HERE.parent/'handoff_check.py')
        old = {name: sys.modules.get(name) for name in ('model','handoff_check')}
        sys.modules['model'], sys.modules['handoff_check'] = architecture, handoff
        try:
            reference = load_module('_learning_parent_reference_'+str(key),
                                    HERE.parent/'independent_check.py')
        finally:
            for name, value in old.items():
                if value is None:
                    del sys.modules[name]
                else:
                    sys.modules[name] = value
        _REFERENCES[key] = handoff, reference
    return _REFERENCES[key]


def independent_parent(architecture, law, formation_arm='live', prefix_arm='variable'):
    """Return original preparation rows, full endpoint rows and work counts.

    Each endpoint retains its actual coupling parent, architecture state,
    initial/current regimes, exact unconditional mass, preparation record and
    conditional-mean prefix marks. Distinct parent histories are not silently
    identified merely because a later scalar balance agrees.
    """
    handoff, reference = parent_references(architecture)
    coupling = architecture.upstream
    old_law = law.upstream_law()
    preps, visited = handoff.independent_preparation(old_law)
    rows, prefix_cache = [], {}
    prefix_evaluations = reference_calls = microbranches = 0
    initial_total = law.initial_common+law.initial_source+law.patient_initial
    full_mass, full_account = Q(0), Q(0)
    for prep in preps:
        prep_mass = Q(prep['probability'])
        if not prep['commissioned']:
            full_mass += prep_mass
            full_account += prep_mass*(prep['preparation_spent']+
                                      prep['remaining_energy']+law.patient_initial)
            continue
        if prep['reserve'] not in prefix_cache:
            table, counts = handoff.independent_prefix(coupling, old_law,
                prefix_arm, prep['reserve'], law.prefix_steps)
            prefix_cache[prep['reserve']] = table
            prefix_evaluations += sum(row['incoming_states'] for row in counts)
        prefix = prefix_cache[prep['reserve']]
        remaining = prep['remainder']+(prep['packets']-law.prefix_steps)*law.packet
        assert remaining == 2*law.rounds*law.packet
        for (z, donor), (mass, marks) in sorted(prefix.items(),
                key=lambda item: (item[0][0],tuple(asdict(item[0][1]).values()))):
            regime = z ^ (sum(t < law.prefix_steps for t in old_law.reversals) % 2)
            branches = reference.reference(law, donor, regime, formation_arm)
            reference_calls += 1
            microbranches += len(branches)
            distribution = defaultdict(Q)
            for branch in branches:
                distribution[branch.state] += branch.probability
            assert sum(distribution.values()) == 1
            for state, conditional in sorted(distribution.items(),
                    key=lambda item: str(asdict(item[0]))):
                probability = prep_mass*mass*conditional
                full_mass += probability
                assert state.source == 0
                parent_suffix_total = sum(getattr(state, field) for field in
                    ('fuel','patient','source','spent','patient_used','damage','waste'))
                assert parent_suffix_total == donor.fuel+law.patient_initial+remaining
                historic = (prep['preparation_spent']+old_law.adapter
                    +marks[coupling.MARKS.index('spent')]/mass
                    +marks[coupling.MARKS.index('waste')]/mass)
                assert parent_suffix_total+historic == initial_total
                full_account += probability*(parent_suffix_total+historic)
                rows.append(dict(preparation=prep, initial_regime=z, regime=regime,
                    coupling_state=donor, state=state, probability=probability,
                    conditional_prefix_mass=mass, conditional_architecture_mass=conditional,
                    prefix_marks={name:value/mass for name,value in zip(coupling.MARKS,marks)},
                    historic_energy=historic))
    assert full_mass == 1 and full_account == initial_total
    counts = dict(preparation_states=visited, preparation_terminals=len(preps),
                  prefix_states_evaluated=prefix_evaluations,
                  architecture_reference_calls=reference_calls,
                  architecture_microbranches=microbranches,
                  architecture_terminal_rows=len(rows), total_mass=str(full_mass),
                  full_parent_energy=str(full_account))
    return preps, rows, counts


def normalized_parent_rows(rows):
    return {(row['initial_regime'],tuple(asdict(row['coupling_state']).items()),
             tuple(asdict(row['state']).items())): row['probability'] for row in rows}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes():
    root = HERE.parents[10]
    paths = {Path(__file__).resolve(), HERE/'PROTOCOL.md',
        HERE.parent/'PROTOCOL.md', HERE.parent/'independent_check.py',
        HERE.parent/'handoff_check.py', HERE.parent.parent/'check.py',
        HERE.parent.parent/'PROTOCOL.md'}
    for module in tuple(sys.modules.values()):
        name = getattr(module, '__file__', None)
        if name:
            path = Path(name).resolve()
            if path.suffix == '.py' and path.is_relative_to(root):
                paths.add(path)
    return {str(path.relative_to(root)): digest(path) for path in sorted(paths)}


def serialize(value):
    if is_dataclass(value):
        return serialize(asdict(value))
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key:serialize(item) for key,item in value.items()}
    if isinstance(value,(tuple,list)):
        return [serialize(item) for item in value]
    return value


def saved_key(z,donor,entry):
    return (z,tuple(donor.items()),tuple((k,tuple(v) if isinstance(v,list) else v)
                                      for k,v in entry.items()))


def audit_saved_results(producer,reports):
    path=HERE/'results.json'
    frozen_hash=digest(path)
    saved=json.loads(path.read_text())
    root=HERE.parents[10]
    assert all(digest(root/name)==sha for name,sha in saved['source_sha256'].items())
    comparisons=terminal_count=0
    for case,law in producer.cases().items():
        report=reports[case]; result=saved['cases'][case]; old=law.architecture_law()
        expected={saved_key(row['initial_regime'],asdict(row['coupling_state']),
                           asdict(row['state'])):row for row in report['branches']}
        failures=[dict(preparation=p,probability=p['probability'],bank=law.initial_bank,
            patient=old.patient_initial,raw_r=old.receptor_parts,raw_d=old.comparator_parts,
            raw_w=old.connector_parts,raw_t=old.template_parts) for p in report['failed_preparations']]
        assert result['failed_preparations']==failures
        assert result['initial_total_energy_including_recipient']==report['extended_initial_energy']
        failed=report['failed_preparation_mass']
        prior_account=sum(row['probability']*(row['historic_energy']+
            sum(getattr(row['state'],field) for field in ('spent','patient_used','damage','waste','source')))
            for row in report['branches'])
        for arm,output in result['arms'].items():
            observed=defaultdict(Q); totals=defaultdict(Q)
            for row in output['terminal_rows']:
                key=saved_key(row['initial_regime'],row['coupling_state'],row['entry'])
                reference=expected[key]; probability=Q(row['probability'])
                observed[key]+=probability
                assert row['regime']==reference['regime']
                end=row['state']; entry=row['entry']; parent=end['parent']
                for field in entry:
                    if field not in ('fuel','patient','active','q','last','raw_w','retained'):
                        assert parent[field]==entry[field]
                assert not parent['active'] or entry['active']
                assert all(not now or before for now,before in zip(parent['retained'],entry['retained']))
                assert parent['raw_w']+int(end['wire'])==entry['raw_w']
                assert parent['raw_w']+sum(mask.bit_count() for mask in parent['graph'])+int(end['wire'])==old.connector_parts
                if end['indexed']:
                    assert end['wire'] and 0<=parent['q']<4 and parent['last'] in (0,1)
                assert end['escrow']==0 and end['bank']==0
                terminal_total=parent['fuel']+parent['patient']+end['bank']+sum(end[field] for field in ('spent','waste','patient_used','damage'))
                assert terminal_total==entry['fuel']+entry['patient']+law.initial_bank
                for field in ('fuel','patient','raw_w'):
                    totals[field]+=probability*parent[field]
                for field in ('bank','spent','waste','patient_used','damage'):
                    totals[field]+=probability*end[field]
                terminal_count+=1
            assert dict(observed)=={key:row['probability'] for key,row in expected.items()}
            assert sum(observed.values())+failed==1
            metrics={key:Q(value) for key,value in output['metrics'].items()}
            for field,stock in (('patient',old.patient_initial),('bank',law.initial_bank),('raw_w',old.connector_parts)):
                assert metrics[field]==totals[field]+failed*stock
            for field in ('fuel','spent','waste','patient_used','damage'):
                assert metrics[field]==totals[field]
            assert metrics['historical_energy']==prior_account
            assert metrics['uncommissioned_energy']==sum(Q(p['probability'])*p['remaining_energy'] for p in report['failed_preparations'])
            assert metrics['failed_preparation_spent']==sum(Q(p['probability'])*p['preparation_spent'] for p in report['failed_preparations'])
            account=('fuel','patient','bank','spent','waste','patient_used','damage',
                     'historical_energy','uncommissioned_energy','failed_preparation_spent')
            assert sum(metrics[field] for field in account)==report['extended_initial_energy']
            comparisons+=1
    assert digest(path)==frozen_hash,'Saved output changed during audit.'
    return dict(case_arm_comparisons=comparisons,terminal_rows_checked=terminal_count,
        all_parent_masses_preserved=True,failed_preparation_bank_and_parts_preserved=True,
        original_depleted_source_preserved=True,guide_graph_and_material_histories_preserved=True,
        connector_wire_conservation=True,indexed_output_format_checked=True,
        outgoing_format='When indexed=true: q=2*actor_bit+recipient_bit; last=qualification. These bytes require the indexed decoder, not the old architecture command semantics.',
        production_results_sha256=frozen_hash)


def audit(producer):
    parent_references(producer.architecture)
    before = source_hashes()
    cache, reports = {}, {}
    for case, law in producer.cases().items():
        parent_law = law.architecture_law()
        key = (repr(parent_law.record()),law.formation_arm)
        if key not in cache:
            cache[key] = independent_parent(producer.architecture,parent_law,law.formation_arm)
        expected_preps, expected_rows, counts = cache[key]
        actual_preps, actual_rows, actual_counts = producer.parent_distribution(law)
        assert actual_preps == expected_preps
        assert normalized_parent_rows(actual_rows) == normalized_parent_rows(expected_rows)
        assert actual_counts['preparation_states'] == counts['preparation_states']
        assert actual_counts['parent_suffix_calls'] == counts['architecture_reference_calls']
        assert actual_counts['parent_microbranches'] == counts['architecture_microbranches']
        expected_map = {key:row for key,row in zip(
            normalized_parent_rows(expected_rows),expected_rows)}
        entered_rows = []
        for row in actual_rows:
            row_key = (row['initial_regime'],tuple(asdict(row['coupling_state']).items()),
                       tuple(asdict(row['state']).items()))
            reference = expected_map[row_key]
            assert row['regime'] == reference['regime']
            assert row['prep'] == reference['preparation']
            assert row['prefixmarks'] == reference['prefix_marks']
            assert row['historic_energy'] == reference['historic_energy']
            entered = producer.entrance(law,row['state'])
            assert entered.parent == row['state']
            assert entered.bank == law.initial_bank == 4*law.packet
            assert not entered.wire and not entered.indexed and entered.escrow == 0
            for field,value in asdict(entered).items():
                if field not in ('parent','bank'):
                    assert value == 0 or value is False
            entered_rows.append(dict(**reference,entrance=entered))
        failed = [row for row in expected_preps if not row['commissioned']]
        failed_mass = sum(Q(row['probability']) for row in failed)
        terminal_mass = sum(row['probability'] for row in expected_rows)
        assert failed_mass+terminal_mass == 1
        initial = parent_law.initial_common+parent_law.initial_source+parent_law.patient_initial
        assert Q(counts['full_parent_energy']) == initial
        reports[case] = dict(formation_arm=law.formation_arm,parent_counts=counts,
            parent_mass=terminal_mass,failed_preparation_mass=failed_mass,
            initial_parent_energy=initial,initial_auxiliary_bank=law.initial_bank,
            extended_initial_energy=initial+law.initial_bank,
            auxiliary_bank_mass_on_parent_endpoints=terminal_mass*law.initial_bank,
            auxiliary_bank_mass_on_failed_preparation=failed_mass*law.initial_bank,
            failed_preparations=failed,branches=entered_rows)
    saved_checks=audit_saved_results(producer,reports)
    assert source_hashes() == before, 'Dependency changed during parent-handoff audit.'
    return dict(status='pass',scope='Independent original preparation, coupling prefix, architecture terminal law, learning entrance and saved branch/account preservation; new learning event semantics checked separately.',
        reused_references=['architecture/handoff_check.py::independent_preparation',
            'coupling/check.py::independent_events','architecture/independent_check.py::reference'],
        compared_cases=len(reports),unique_parent_laws=len(cache),
        rows=reports,saved_result_checks=saved_checks,source_sha256=before)


if __name__ == '__main__':
    producer=load_module('_learning_handoff_producer',HERE/'model.py')
    result=audit(producer)
    (HERE/'handoff-check.json').write_text(json.dumps(serialize(result),indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','compared_cases','unique_parent_laws')}))
