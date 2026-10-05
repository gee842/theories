"""Exact constructed checks for dynamics-formal.md; no empirical data."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def frac(x):
    return F(str(x))


def geom(r, m):
    return sum((r**j for j in range(m)), F(0))


def fixed_start(r, additive, transmission, m):
    return transmission * additive * geom(r, m) / (1-transmission*r**m)


def iterate_cycle(x, r, additive, transmission, m):
    phases = []
    for _ in range(m):
        phases.append(x)
        x = r*x + additive
    return transmission*x, phases


def score(w, g, z, b=F(2), H=F(10)):
    return z*(b+H*g*w)


def required_reserve(costs, yields):
    prefix = F(0)
    reserve = F(0)
    for cost, renewal in zip(costs, yields):
        reserve = max(reserve, cost-prefix)
        prefix += renewal-cost
    return reserve, prefix


def run_budget(reserve, costs, yields, cycles=1, discard_surplus=False):
    initial = reserve
    for _ in range(cycles):
        for cost, renewal in zip(costs, yields):
            if reserve < cost:
                return False, reserve
            reserve = reserve-cost+renewal
        if discard_surplus:
            reserve = min(reserve, initial)
    return True, reserve


def main():
    recurrence_cases = 0
    for r, additive, transmission, m in product(
        [F(0), F(1, 4), F(7, 10)], [F(0), F(1, 3), F(2)],
        [F(1, 5), F(9, 10), F(1)], [1, 2, 4, 7]
    ):
        star = fixed_start(r, additive, transmission, m)
        end, phases = iterate_cycle(star, r, additive, transmission, m)
        assert end == star
        assert min(phases) == star
        x = F(0)
        for n in range(6):
            assert x == star*(1-(transmission*r**m)**n)
            nxt, observed = iterate_cycle(x, r, additive, transmission, m)
            assert min(observed) == x
            assert nxt >= x
            x = nxt
        recurrence_cases += 1

    action_cases = 0
    for w, g, z, b, H, a in product(
        [F(0), F(1, 2), F(3)], [F(0), F(1, 2), F(1)],
        [F(-1, 2), F(0), F(1, 2), F(1)], [F(0), F(2)],
        [F(1), F(10)], [F(1), F(4), F(8)]
    ):
        repair = a+(1-z)*b+w*g*(1-z)*H
        unprotected = b+w*g*H
        assert (repair < unprotected) == (score(w, g, z, b, H) > a)
        action_cases += 1

    m = 4
    common = [(F(7, 10), F(1, 2)),
              (F(1, 2), F(2, 5)),
              (F(1, 2), F(2, 5))]
    probe_mass, actual_Q, harm_scale = F(1, 10), F(4, 5), F(10)
    probe_harm = probe_mass*(1-actual_Q)*harm_scale
    measurement_cost = F(9, 25)
    probe_intervention_cost = probe_mass*(F(6)+(1-actual_Q)*2)
    audit_fee = F(1)
    assert probe_harm == F(1, 5)
    assert audit_fee >= probe_intervention_cost+measurement_cost
    assert audit_fee == probe_intervention_cost+measurement_cost
    illustrations = []
    for w_transmission in [F(9, 10), F(1, 5)]:
        transmissions = [w_transmission, F(19, 20), F(19, 20)]
        stars = [fixed_start(r, A, t, m)
                 for (r, A), t in zip(common, transmissions)]
        eventual = score(*stars) > 6
        current = [F(0), F(0), F(0)]
        first_durable = None
        late_start_scores = []
        actual_costs = []
        harm_ledger = []
        for generation in range(40):
            if score(*current) > 6 and first_durable is None:
                first_durable = generation
            late_start_scores.append(float(score(*current)))
            for step in range(m):
                protects = score(*current) > 6
                if first_durable is not None:
                    assert protects
                # Q=.8. Maintenance includes paid rehearsal, alignment and audit.
                action_cost = F(6)+F(1,5)*2 if protects else F(2)
                actual_costs.append(F(2)+action_cost+(F(2) if step == m-1 else 0))
                operating_harm = (1-actual_Q)*harm_scale if protects else harm_scale
                harm_ledger.append((operating_harm, probe_harm, operating_harm+probe_harm))
                current = [r*x+A for x, (r, A) in zip(current, common)]
            current = [t*x for x, t in zip(current, transmissions)]
        assert (first_durable is not None) == eventual
        # All-repair envelope pays before renewal and includes succession.
        cycle_costs = [F(42, 5)]*3+[F(52, 5)]
        cycle_yields = [F(9)]*4
        required, net = required_reserve(cycle_costs, cycle_yields)
        assert required == F(43, 5) and net == F(2, 5)
        assert run_budget(required, cycle_costs, cycle_yields, 100, True)[0]
        assert not run_budget(required-F(1, 100), cycle_costs, cycle_yields)[0]
        assert run_budget(required, actual_costs, [F(9)]*len(actual_costs))[0]
        assert harm_ledger[0] == (F(10), F(1, 5), F(51, 5))
        assert all(total == operating+probe for operating, probe, total in harm_ledger)
        if eventual:
            assert all(row == (F(2), F(1, 5), F(11, 5))
                       for row in harm_ledger[first_durable*m:])
        illustrations.append({
            'valence_transmission': str(w_transmission),
            'periodic_start_w_g_z': [str(x) for x in stars],
            'limiting_minimum_protection_score': float(score(*stars)),
            'repair_expenditure': 6,
            'durable_protection_condition': eventual,
            'first_durable_generation_from_zero': first_durable,
            'conservative_reserve': str(required),
            'net_resource_gain_per_generation': str(net),
            'costs_paid_in_bootstrap': True,
            'first_four_start_scores': late_start_scores[:4],
            'validation_cohort_mass_per_interval': str(probe_mass),
            'probe_intervention_resource_cost': str(probe_intervention_cost),
            'probe_measurement_resource_cost': str(measurement_cost),
            'audit_resource_fee': str(audit_fee),
            'probe_harm_per_interval': str(probe_harm),
            'first_generation_harm_ledger': [
                {'operating_harm': str(op), 'probe_harm': str(probe), 'total_harm': str(total)}
                for op, probe, total in harm_ledger[:m]],
            'no_repair_no_probe_reference_harm_per_interval': str(harm_scale),
            'all_repair_total_harm_per_interval': str((1+probe_mass)*(1-actual_Q)*harm_scale),
            '40_generation_cumulative_operating_harm': str(sum(row[0] for row in harm_ledger)),
            '40_generation_cumulative_probe_harm': str(sum(row[1] for row in harm_ledger)),
            '40_generation_cumulative_total_harm': str(sum(row[2] for row in harm_ledger)),
        })

    harm_boundary_cases = 0
    for rho, Q in product([F(1, 20), F(1, 10), F(1), F(5)],
                           [F(0), F(1, 10), F(1, 2), F(4, 5), F(1)]):
        assert ((1+rho)*(1-Q) < 1) == (Q > rho/(1+rho))
        harm_boundary_cases += 1

    budget_cases = 0
    for costs, yields in product(product(range(1, 4), repeat=3),
                                 product(range(0, 4), repeat=3)):
        costs, yields = list(map(F, costs)), list(map(F, yields))
        required, net = required_reserve(costs, yields)
        assert run_budget(required, costs, yields)[0]
        assert not run_budget(required-F(1, 2), costs, yields)[0]
        if net >= 0:
            assert run_budget(required, costs, yields, 15, True)[0]
        else:
            # A sufficient finite number of repeats to exhaust even this reserve.
            repeats = int(required / (-net)) + 3
            assert not run_budget(required, costs, yields, repeats)[0]
        budget_cases += 1

    # Buffer must hold the last yield before surplus is discarded.
    final_yield_prefixes = [F(0), F(0), F(9)]
    assert F(1)+max(final_yield_prefixes) == 10
    assert F(1)+max(final_yield_prefixes[:-1]) == 1  # would underestimate required capacity

    # Harmful repair: recipient metering retracts a favorable mistaken estimate.
    Q, z, gamma = F(-2, 5), F(4, 5), F(1, 2)
    correction_trace = []
    correction_reserve = F(100)
    negative_probe_fee = probe_mass*(6+(1-Q)*2)+measurement_cost
    assert negative_probe_fee == F(31, 25)  # favorable-case fee1 would underpay this protocol
    for k in range(4):
        protects = score(F(5, 3), F(4, 5), z) > 6
        operating_harm = (1-Q)*harm_scale if protects else harm_scale
        current_probe_harm = probe_mass*(1-Q)*harm_scale
        cost = F(1)+negative_probe_fee+(6+(1-Q)*2 if protects else 2)
        assert correction_reserve >= cost
        correction_reserve -= cost
        correction_trace.append({'audits': k, 'estimated_efficacy': str(z),
                                 'repair_chosen': protects,
                                 'operating_harm': str(operating_harm),
                                 'probe_harm': str(current_probe_harm),
                                 'total_harm': str(operating_harm+current_probe_harm),
                                 'paid_probe_fee': str(negative_probe_fee),
                                 'paid_total_cost': str(cost)})
        assert z == Q+(F(4, 5)-Q)*(1-gamma)**k
        z = (1-gamma)*z+gamma*Q
    assert correction_trace[0]['repair_chosen']
    assert not correction_trace[1]['repair_chosen']
    assert all(row['probe_harm'] == '7/5' for row in correction_trace)
    assert score(F(0), F(0), F(1), b=F(0)) == 0  # stopping bound denominator zero: no repair

    # Separate improved policy: exact assay evidence gates deployment AND probes.
    # The original fixed-audit counterexample above is intentionally retained.
    gated_trace = []
    z, has_valid_assay, suspended = F(4, 5), False, False
    gated_probe_harm = F(0)
    gated_probe_expense = F(0)
    pilot_resource_reserve, pilot_harm_allowance = F(2), F(3, 2)
    declared_efficacy_lower_bound = F(-1, 2)
    reserved_probe_cost = probe_mass*(6+(1-declared_efficacy_lower_bound)*2)+measurement_cost
    reserved_probe_harm = probe_mass*(1-declared_efficacy_lower_bound)*harm_scale
    assert pilot_resource_reserve >= reserved_probe_cost
    assert pilot_harm_allowance >= reserved_probe_harm
    assay_count = 0
    for interval in range(4):
        if suspended:
            assert has_valid_assay
            gated_trace.append({'interval': interval, 'assay_run': False,
                                'candidate_deployed': False,
                                'smoothed_estimate': str(z), 'suspended': True,
                                'probe_harm': '0'})
            continue
        deployed_before_result = score(F(5, 3), F(4, 5), z) > 6
        E = F(-2, 5)  # exact metered signal, not a free unobserved parameter
        assert E >= declared_efficacy_lower_bound
        has_valid_assay = True
        assay_count += 1
        harm = probe_mass*(1-E)*harm_scale
        gated_probe_harm += harm
        gated_probe_expense += probe_mass*(6+(1-E)*2)+measurement_cost
        assert gated_probe_expense <= pilot_resource_reserve
        assert gated_probe_harm <= pilot_harm_allowance
        z = (1-gamma)*z+gamma*E
        suspended = E <= 0
        gated_trace.append({'interval': interval, 'assay_run': True,
                            'candidate_deployed': deployed_before_result,
                            'actual_assay_signal': str(E),
                            'smoothed_estimate': str(z), 'suspended': suspended,
                            'probe_harm': str(harm)})
    assert assay_count == 1 and gated_probe_harm == F(7, 5)
    assert gated_probe_expense == F(31, 25)
    assert z == F(1, 5) and z > 0  # exact evidence suspends before smoothing reaches zero
    # Positive stationary assays never activate this additional gate.
    for positive_Q, transmission in product([F(1, 10), F(4, 5), F(1)],
                                            [F(1, 10), F(9, 10), F(1)]):
        estimate = F(0)
        for _ in range(8):
            E = positive_Q
            assert not (E <= 0)
            estimate = transmission*((1-gamma)*estimate+gamma*E)
            assert estimate > 0

    # Observer cue creates a self-confirming false critic despite actual harm.
    H, v, mask_cost, repair_cost = F(10), F(1), F(1), F(4)
    private_cue_relief, recipient_efficacy, private_loss = F(1), F(0), F(6)
    actual_mask_private_cost = mask_cost+(1-private_cue_relief)*private_loss
    actual_mask_harm = (1-recipient_efficacy)*H
    assert actual_mask_private_cost == 1 and actual_mask_harm == 10
    mask_z = F(1)
    for _ in range(20):
        assert mask_cost+v*(1-mask_z)*H < repair_cost
        mask_z = F(1, 2)*mask_z+F(1, 2)*1  # cue relief, not recipient evidence
        assert mask_z == 1
    assert mask_cost+v*H > repair_cost  # separately observed actual harm reverses ranking

    # A productive recipient-capacity bridge: surplus, deficit, and equality.
    loss, restoration, slope, base = F(1, 4), F(2), F(1), F(2)
    capacity_star = restoration/loss
    revenue_star = base+slope*capacity_star
    productive = []
    for generation_cost in [F(9), F(10), F(11)]:
        X = F(0)
        cumulative_net = F(0)
        smallest_prefix = F(0)
        for k in range(80):
            assert X == capacity_star*(1-(1-loss)**k)
            net = base+slope*X-generation_cost
            cumulative_net += net
            smallest_prefix = min(smallest_prefix, cumulative_net)
            X = (1-loss)*X+restoration
        if generation_cost < revenue_star:
            assert net > 0
        elif generation_cost == revenue_star:
            exact_deficit_limit = slope*capacity_star/loss
            assert -cumulative_net < exact_deficit_limit
            assert abs(float(-cumulative_net-exact_deficit_limit)) < 1e-7
        else:
            assert net < -1
        productive.append({'generation_cost': str(generation_cost),
                           'limiting_generation_receipt': str(revenue_star),
                           'net_after_80_generations': float(net),
                           'maximum_cumulative_deficit_in_80_generations': float(-smallest_prefix),
                           'equality_total_deficit_limit': '32' if generation_cost == revenue_star else None})

    output = {
        'status': 'passed',
        'kind': 'constructed exact mathematical checks, not empirical evidence',
        'affine_learning_and_succession_cases': recurrence_cases,
        'partial_efficacy_decision_cases': action_cases,
        'prefix_solvency_schedules': budget_cases,
        'total_harm_probe_boundary_cases': harm_boundary_cases,
        'illustrations': illustrations,
        'negative_efficacy_correction': correction_trace,
        'exact_assay_gate': {
            'trace': gated_trace,
            'total_active_assays': assay_count,
            'total_probe_harm': str(gated_probe_harm),
            'total_probe_resource_cost': str(gated_probe_expense),
            'prefunded_pilot_resource_reserve': str(pilot_resource_reserve),
            'declared_pilot_harm_allowance': str(pilot_harm_allowance),
            'assumed_efficacy_lower_bound_for_pilot': str(declared_efficacy_lower_bound),
            'suspension_record_retained': True,
            'scope': 'Exact known-baseline controlled assay; noisy evidence is not covered.',
        },
        'masking_counterexample': {
            'perceived_mask_burden': 1, 'actual_recipient_harm': 10,
            'world_metered_mask_burden': 11, 'successful_repair_burden': 4,
            'stable_false_observer_critic': True,
        },
        'productive_capacity_bridge': productive,
    }
    path = Path(__file__).with_name('dynamics-checks.json')
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
