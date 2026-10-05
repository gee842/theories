"""Development v1: a bounded integrated inquiry institution.

Decisions use observable summaries, paid records, contracts, cash, and checker
status. Hidden scenario laws are confined to World.sample()/quotes(). All cash
is integer thousandths. This module does not run held-out seeds on import.
"""
from collections import deque
from dataclasses import asdict, dataclass
from itertools import product, combinations
from math import ceil, log, sqrt
from pathlib import Path
import hashlib
import json
import purpose_policy

ROWS = tuple(product((0, 1), repeat=3))
SINGLES = tuple(combinations(range(3), 1))
PAIRS = tuple(combinations(range(3), 2))
GROUPS = ('A', 'B')
DEVELOPMENT_SEEDS = (1103, 2207, 3301, 4409)
ARMS = ('full', 'fixed_mandate', 'fixed_rule', 'no_renewal', 'incumbent_only_opening')
SCENARIOS = ('emerging', 'simple', 'noise', 'transient', 'material_stress', 'poor_income')

@dataclass(frozen=True)
class Config:
    rounds: int = 700
    initial_cash: int = 20000
    maintenance: int = 50
    rebuild: int = 8000
    fee_per_group: int = 400
    refund_per_error: int = 50
    base_prediction: int = 10
    field_read: int = 5
    expanded_retainer: int = 140
    acquired_label: int = 10
    linked_record: int = 5
    fit_price: int = 10
    hearing_price: int = 250
    probe_opening: int = 1000
    reserve_floor: int = 5000
    window: int = 32
    cooldown: int = 64
    curiosity_age: int = 128
    pilot_per_group: int = 32
    target_precision: float = .075
    min_check: int = 64
    max_check: int = 512
    lifetime_alpha: float = .05

@dataclass(frozen=True)
class Model:
    fields: tuple
    predictions: tuple
    score: float

@dataclass(frozen=True)
class Package:
    require_prefix: bool
    models: tuple

def random_word(seed, *key):
    # Exogenous named streams are keyed without arm identity.
    raw = '|'.join(map(str, (seed,) + key)).encode()
    return int.from_bytes(hashlib.blake2b(raw, digest_size=8).digest(), 'big')

class World:
    def __init__(self, scenario, seed):
        self.scenario, self.seed = scenario, seed

    def sample(self, t, group, stage, review, index, forced_row=None):
        value = random_word(self.seed, self.scenario, t, group, stage, review, index)
        row_index = (value & 7) if forced_row is None else forced_row
        c, d, e = ROWS[row_index]
        if group == 'A':
            outcome = c
        elif self.scenario == 'simple' or t < 80:
            outcome = c
        elif self.scenario == 'noise':
            outcome = (value >> 8) & 1
        elif self.scenario == 'transient' and t >= 150:
            outcome = c
        elif self.scenario == 'material_stress' and t >= 400:
            outcome = c
        else:
            outcome = c ^ d
        return row_index, outcome

    def context(self, t, group, stage, review, index):
        return random_word(self.seed, self.scenario, t, group, stage, review, index) & 7

    def quotes(self, t, cfg):
        # These invoices/contract terms are observable before accepting service.
        maintenance = 20000 if self.scenario == 'material_stress' and 200 <= t < 210 else cfg.maintenance
        fee = 10 if self.scenario == 'poor_income' and t >= 40 else cfg.fee_per_group
        return {'maintenance': maintenance, 'fee': fee, 'refund': cfg.refund_per_error}

def fit(fields, labels):
    table = {}
    for key in product((0, 1), repeat=len(fields)):
        ys = [y for row, y in zip(ROWS, labels) if tuple(row[j] for j in fields) == key]
        table[key] = int(2 * sum(ys) > len(ys))
    predictions = tuple(table[tuple(row[j] for j in fields)] for row in ROWS)
    error = sum(y != p for y, p in zip(labels, predictions)) / 8
    return Model(fields, predictions, error + (2 ** len(fields) - 1) / 32)

def rank(model):
    return model.score, model.fields, model.predictions

def construct(require_prefix, labels, charge=None):
    if charge is not None:
        charge(4)  # Coarse and singleton computation is paid before it occurs.
    coarse = fit((), labels)
    singles = [fit(fs, labels) for fs in SINGLES]
    best_single = min(singles, key=rank)
    fit_count = 4  # One coarse and three singleton fitted tables.
    if require_prefix and best_single.score >= coarse.score:
        return coarse, None, fit_count
    pairs = [fs for fs in PAIRS if best_single.fields[0] in fs] if require_prefix else PAIRS
    if charge is not None:
        charge(len(pairs))
    fitted = [fit(fs, labels) for fs in pairs]
    fit_count += len(pairs)
    best = min([coarse] + singles + fitted, key=rank)
    return coarse, (best if best.score < coarse.score else None), fit_count

def operating_cost(package, cfg):
    return (2 * cfg.base_prediction + cfg.field_read * sum(len(m.fields) for m in package.models)
            + (0 if package.require_prefix else cfg.expanded_retainer))

def weights(mandate):
    return (1., 0.) if mandate == 'A_ONLY' else (.5, .5)

def paired_case_price(cfg):
    return cfg.expanded_retainer + 4 * cfg.base_prediction + 2 * (3 * cfg.field_read + cfg.acquired_label + cfg.linked_record)

def opening_stage_reserve(cfg):
    # Covers only opening, candidate construction, inner validation, pilot, and
    # a possible hearing. Actual holdout size/pricing is decided afterwards.
    record_price = 3 * cfg.field_read + cfg.acquired_label + cfg.linked_record
    return (cfg.probe_opening + 32 * record_price + 14 * cfg.fit_price
            + 16 * cfg.base_prediction + cfg.pilot_per_group * paired_case_price(cfg)
            + cfg.hearing_price + cfg.reserve_floor)

def summary(history):
    return {g: {'n': len(history[g]), 'error': sum(history[g]) / len(history[g]) if history[g] else None}
            for g in GROUPS}

class Institution:
    def __init__(self, cfg, arm, trace_ledger=False):
        self.cfg, self.arm = cfg, arm
        self.cash = cfg.initial_cash
        self.receipts = 0
        self.expenses = {}
        self.checker = True
        self.mandate = 'A_ONLY'
        self.package = None
        self.history = {g: deque(maxlen=cfg.window) for g in GROUPS}
        self.counts = {g: {'requested': 0, 'served': 0, 'correct': 0, 'errors': 0, 'unserved': 0} for g in GROUPS}
        self.last_attempt = 0
        self.last_paid_review = 0
        self.review_index = 0
        self.events = []
        self.timeline = []
        self.stage_observations = {}
        self.losses = self.rebuilds = self.petitions = self.rule_changes = self.mandate_changes = 0
        self.ledger_hash = hashlib.sha256()
        self.ledger_rounds = {}
        self.ledger_transactions = [] if trace_ledger else None
        self.transaction_count = 0
        self.failed_payments = 0

    def record_transaction(self, t, direction, category, amount, before):
        self.transaction_count += 1
        row = {'sequence': self.transaction_count, 'round': t, 'direction': direction,
               'category': category, 'amount': amount, 'before': before, 'after': self.cash}
        self.ledger_hash.update(json.dumps(row, sort_keys=True, separators=(',', ':')).encode())
        s = self.ledger_rounds.setdefault(t, {'round': t, 'cash_before': before, 'credited': 0,
            'paid': 0, 'minimum_interim_cash': before, 'transactions': 0})
        s['credited' if direction == 'credit' else 'paid'] += amount
        s['cash_after'] = self.cash
        s['minimum_interim_cash'] = min(s['minimum_interim_cash'], self.cash)
        s['transactions'] += 1
        if self.ledger_transactions is not None:
            self.ledger_transactions.append(row)

    def pay(self, amount, category, t):
        if amount < 0:
            raise ValueError('Negative expense')
        if self.cash < amount:
            self.failed_payments += 1
            return False
        before = self.cash
        self.cash -= amount
        self.expenses[category] = self.expenses.get(category, 0) + amount
        self.record_transaction(t, 'pay', category, amount, before)
        return True

    def require_payment(self, amount, category, t):
        if not self.pay(amount, category, t):
            raise RuntimeError(f'Unfunded required payment: {category}')

    def credit(self, amount, t):
        before = self.cash
        self.cash += amount
        self.receipts += amount
        self.record_transaction(t, 'credit', 'settled_service_fee', amount, before)

    def event(self, t, kind, **data):
        self.events.append({'round': t, 'kind': kind, 'cash': self.cash, **data})

    def take(self, world, t, group, stage, index, forced_row=None, price=None):
        if not self.checker:
            raise RuntimeError('Linked prospective observation requires usable checker')
        if price is None:
            price = 3 * self.cfg.field_read + self.cfg.acquired_label + self.cfg.linked_record
        if not self.pay(price, 'evidence_' + stage, t):
            raise RuntimeError('Acquisition was not financed before observation')
        self.stage_observations[stage] = self.stage_observations.get(stage, 0) + 1
        return world.sample(t, group, stage, self.review_index, index, forced_row)

    def fit_packages(self, world, t, rules):
        # One paid linked training/validation record can be reused by both passive
        # algorithms. Prediction and evaluation still precede the new outcome.
        labels = []
        for g in GROUPS:
            labels.append(tuple(self.take(world, t, g, 'training', i, i)[1] for i in range(8)))
        constructed = []
        for rule in rules:
            pair = []
            for ys in labels:
                coarse, candidate, fits = construct(rule, ys,
                    lambda n: self.require_payment(n * self.cfg.fit_price, 'model_fitting', t))
                pair.append((coarse, candidate))
            constructed.append((rule, pair))
        fresh = []
        for g in GROUPS:
            ys = []
            for i in range(8):
                self.require_payment(len(constructed) * self.cfg.base_prediction, 'inner_validation_compute', t)
                ys.append(self.take(world, t, g, 'inner_validation', i, i)[1])
            fresh.append(tuple(ys))
        packages = []
        for rule, pair in constructed:
            models = []
            for i, (coarse, candidate) in enumerate(pair):
                accepted = (candidate is not None and sum(y == p for y, p in zip(fresh[i], candidate.predictions)) >= 7)
                models.append(candidate if accepted else coarse)
            packages.append(Package(rule, tuple(models)))
        return packages

    def bootstrap(self, world):
        # Endowed capital and intact checker, but initial compiled predictors are
        # constructed from paid data with the same generic mechanism.
        self.package = self.fit_packages(world, 0, (True,))[0]
        self.event(0, 'bootstrap', prefix=self.package.require_prefix,
                   fields=[list(m.fields) for m in self.package.models])

    def pressure(self, t):
        s = summary(self.history)
        sufficient = all(s[g]['n'] >= 16 for g in GROUPS)
        if not sufficient:
            return []
        reasons = []
        w = weights(self.mandate)
        if sum(w[i] * s[g]['error'] for i, g in enumerate(GROUPS)) >= .20:
            reasons.append('mandated_error')
        if self.arm == 'incumbent_only_opening':
            return reasons
        if purpose_policy.petition_eligibility(s):
            reasons.append('B_grievance')
        if t - self.last_paid_review >= self.cfg.curiosity_age:
            reasons.append('unexamined_method')
        return reasons

    def renew(self, quotes, reasons, t):
        if self.checker:
            if self.arm == 'no_renewal' or not self.pay(quotes['maintenance'], 'checker_upkeep', t):
                self.checker = False
                self.losses += 1
                self.event(t, 'checker_lost', cause='withheld_upkeep' if self.arm == 'no_renewal' else 'unaffordable_upkeep')
        elif self.arm != 'no_renewal' and reasons:
            need = self.cfg.rebuild + quotes['maintenance'] + self.cfg.reserve_floor + operating_cost(self.package, self.cfg) + 2 * quotes['refund']
            if self.cash >= need:
                self.require_payment(self.cfg.rebuild, 'checker_rebuild', t)
                self.require_payment(quotes['maintenance'], 'checker_upkeep', t)
                self.checker = True
                self.rebuilds += 1
                self.event(t, 'checker_rebuilt')

    def serve(self, world, quotes, t):
        for g in GROUPS:
            self.counts[g]['requested'] += 1
        cost = operating_cost(self.package, self.cfg)
        # A service contract is a two-group bundle. Prefund the full possible
        # rebate; settled fees are credited only after outcomes are observed.
        if self.cash < cost + 2 * quotes['refund']:
            for g in GROUPS:
                self.counts[g]['unserved'] += 1
            return
        self.require_payment(cost, 'ordinary_operation', t)
        for i, g in enumerate(GROUPS):
            # The entire predictor vector was committed before settlement.
            # Context arrives first; outcome/contract settle synchronously later
            # in this atomic service operation. No future receipt is spendable.
            row = world.context(t, g, 'ordinary', 0, 0)
            pred = self.package.models[i].predictions[row]
            settled_row, y = world.sample(t, g, 'ordinary', 0, 0)
            if settled_row != row:
                raise RuntimeError('Settlement refers to the wrong service case')
            wrong = int(pred != y)
            self.credit(quotes['fee'], t)
            if wrong:
                self.require_payment(quotes['refund'], 'contract_refunds', t)
            count = self.counts[g]
            count['served'] += 1
            count['errors'] += wrong
            count['correct'] += 1 - wrong
            self.history[g].append(wrong)
            # Full contexts and linked labels are discarded here. The retained
            # service record is group-level error/fee history, not a replay log.

    def paired_pilot(self, world, t, incumbent, candidate):
        errors = {'incumbent': {g: 0 for g in GROUPS}, 'edited': {g: 0 for g in GROUPS}}
        for k in range(self.cfg.pilot_per_group):
            self.require_payment(self.cfg.expanded_retainer + 4 * self.cfg.base_prediction, 'pilot_shadow_compute', t)
            for i, g in enumerate(GROUPS):
                row, y = self.take(world, t, g, 'purpose_pilot', k)
                errors['incumbent'][g] += incumbent.models[i].predictions[row] != y
                errors['edited'][g] += candidate.models[i].predictions[row] != y
        return {arm: {g: n / self.cfg.pilot_per_group for g, n in v.items()} for arm, v in errors.items()}

    def review(self, world, t, reasons):
        self.last_attempt = t
        opening_reserve = opening_stage_reserve(self.cfg)
        if not self.checker or self.cash < opening_reserve:
            self.event(t, 'review_blocked', reasons=reasons, usable_checker=self.checker,
                       required_opening_reserve=opening_reserve)
            return
        self.last_paid_review = t
        self.review_index += 1  # Every paid attempt spends its own alpha index.
        alpha = self.cfg.lifetime_alpha / (self.review_index * (self.review_index + 1))
        start_cash = self.cash
        self.event(t, 'review_started', reasons=reasons, review=self.review_index, alpha=alpha,
                   mandate=self.mandate, prefix=self.package.require_prefix)
        self.require_payment(self.cfg.probe_opening, 'review_opening', t)
        incumbent = self.package  # Actual installed forecasts remain unchanged.
        candidate = self.fit_packages(world, t, (not incumbent.require_prefix,))[0]
        delta = (operating_cost(candidate, self.cfg) - operating_cost(incumbent, self.cfg)) / 1000
        pilot = self.paired_pilot(world, t, incumbent, candidate)
        service = summary(self.history)
        if self.mandate == 'A_ONLY' and purpose_policy.petition_eligibility(service) and delta >= 0:
            self.petitions += 1
            self.require_payment(self.cfg.hearing_price, 'purpose_hearing', t)
            ballot = purpose_policy.hearing_decision(
                service=service, pilot=pilot, extra_round_cost=delta,
                cash_after_hearing=self.cash / 1000, next_required_payment=paired_case_price(self.cfg) / 1000,
                reserve_floor=self.cfg.reserve_floor / 1000, usable_checker=self.checker,
                current_mandate=self.mandate)
            before = self.mandate
            if ballot['adopt'] and self.arm != 'fixed_mandate':
                self.mandate = ballot['mandate_after']
                self.mandate_changes += 1
            self.event(t, 'purpose_hearing', ballot=ballot, before=before, after=self.mandate,
                       authority_clamped=self.arm == 'fixed_mandate')
        w = weights(self.mandate)
        pilot_gain = sum(w[i] * (pilot['incumbent'][g] - pilot['edited'][g]) for i, g in enumerate(GROUPS)) - delta
        self.event(t, 'candidate_frozen', review=self.review_index,
                   incumbent=asdict(incumbent), candidate=asdict(candidate),
                   mandate=self.mandate, weights=w, delta=delta, pilot=pilot,
                   pilot_gain_under_enacted_mandate=pilot_gain,
                   provenance={'round': t, 'review': self.review_index,
                       'training_stage': 'training', 'inner_stage': 'inner_validation',
                       'pilot_stage': 'purpose_pilot', 'fresh_stage': 'final_check'})
        if pilot_gain <= 0:
            self.event(t, 'review_failed_pilot', review=self.review_index,
                       mandate=self.mandate, pilot_gain=pilot_gain,
                       priced_expense=start_cash - self.cash)
            return
        disagreement = tuple(incumbent.models[i].predictions != candidate.models[i].predictions for i in range(2))
        W = sum(w[i] for i in range(2) if disagreement[i])
        # If neither weighted forecast can differ, objective gain is known from
        # declared operating prices, without consulting hidden outcomes.
        if W == 0:
            passed = -delta > 0
            result = {'n': 0, 'W': W, 'delta': delta, 'gain': -delta, 'lower': -delta,
                      'method': 'identical_weighted_forecasts_known_cost_difference', 'pass': passed}
        else:
            n = min(self.cfg.max_check, max(self.cfg.min_check,
                    ceil((2 * W) ** 2 * log(1 / alpha) / (2 * self.cfg.target_precision ** 2))))
            radius = 2 * W * sqrt(log(1 / alpha) / (2 * n))
            # Every paired check logs one paid outcome per group and computes
            # both passive forecasts, charging the shared engine once.
            per_round_price = paired_case_price(self.cfg)
            if self.cash < n * per_round_price + self.cfg.reserve_floor:
                self.event(t, 'review_unfunded_check', review=self.review_index, planned_n=n,
                           required=n * per_round_price + self.cfg.reserve_floor, mandate=self.mandate,
                           paid_so_far=start_cash - self.cash)
                return
            self.event(t, 'fresh_check_planned', review=self.review_index, n=n, W=W,
                       alpha=alpha, radius=radius, mandate=self.mandate,
                       per_round_price=per_round_price, required=n * per_round_price + self.cfg.reserve_floor)
            group_differences = [0, 0]
            errors = {'incumbent': [0, 0], 'edited': [0, 0]}
            for k in range(n):
                self.require_payment(self.cfg.expanded_retainer + 4 * self.cfg.base_prediction, 'checking_compute', t)
                for i, g in enumerate(GROUPS):
                    # Predictor vectors were frozen before requesting this fresh outcome.
                    row, y = self.take(world, t, g, 'final_check', k)
                    e0 = int(incumbent.models[i].predictions[row] != y)
                    e1 = int(candidate.models[i].predictions[row] != y)
                    group_differences[i] += e0 - e1
                    errors['incumbent'][i] += e0
                    errors['edited'][i] += e1
            dg = [x / n for x in group_differences]
            gain = sum(w[i] * dg[i] for i in range(2)) - delta
            result = {'n': n, 'W': W, 'delta': delta, 'gain': gain, 'lower': gain - radius,
                      'radius': radius, 'pass': gain - radius > 0,
                      'method': 'fixed_fresh_paired_Hoeffding', 'group_error_reductions': dg,
                      'group_errors': errors,
                      'diagnostic_gain_A_only': dg[0] - delta,
                      'diagnostic_gain_inclusive': .5 * sum(dg) - delta}
        changed = result['pass'] and self.arm != 'fixed_rule'
        if changed:
            self.package = candidate
            self.rule_changes += 1
        self.event(t, 'review_finished', review=self.review_index, mandate=self.mandate,
                   result=result, rule_changed=changed, prefix_after=self.package.require_prefix,
                   compiled_fields=[list(m.fields) for m in self.package.models],
                   deployment_clamped=self.arm == 'fixed_rule', priced_expense=start_cash - self.cash)

    def run(self, world):
        self.bootstrap(world)
        for t in range(1, self.cfg.rounds + 1):
            quotes = world.quotes(t, self.cfg)
            reasons = self.pressure(t)
            self.renew(quotes, reasons, t)
            self.serve(world, quotes, t)
            reasons = self.pressure(t)
            if reasons and t - self.last_attempt >= self.cfg.cooldown:
                self.review(world, t, reasons)
            assert self.cash == self.cfg.initial_cash + self.receipts - sum(self.expenses.values())
            assert self.cash >= 0
            if t % 10 == 0:
                self.timeline.append({'round': t, 'cash': self.cash, 'checker': self.checker,
                    'mandate': self.mandate, 'prefix': self.package.require_prefix,
                    'errors_A': self.counts['A']['errors'], 'errors_B': self.counts['B']['errors'],
                    'served_A': self.counts['A']['served'], 'served_B': self.counts['B']['served']})
        return {'scenario': world.scenario, 'seed': world.seed, 'arm': self.arm,
                'config': asdict(self.cfg), 'final_cash': self.cash,
                'initial_cash': self.cfg.initial_cash, 'receipts': self.receipts,
                'expenses': self.expenses, 'cash_identity': self.cash == self.cfg.initial_cash + self.receipts - sum(self.expenses.values()),
                'counts': self.counts, 'reviews': self.review_index, 'rule_changes': self.rule_changes,
                'mandate_changes': self.mandate_changes, 'checker_losses': self.losses, 'checker_rebuilds': self.rebuilds,
                'paid_observations_by_stage': self.stage_observations,
                'final_mandate': self.mandate, 'final_prefix': self.package.require_prefix,
                'events': self.events, 'timeline': self.timeline,
                'chronological_ledger': {'transaction_count': self.transaction_count,
                    'sha256': self.ledger_hash.hexdigest(), 'failed_payments': self.failed_payments,
                    'rounds': list(self.ledger_rounds.values()), 'transactions': self.ledger_transactions},
                'inference_scope': 'Each check concerns a frozen rule-plus-compiled-predictor package under the atomic review distribution; no future or cross-task algorithm superiority follows.'}

def run(seed, scenario, arm='full', cfg=Config(), trace_ledger=False):
    return Institution(cfg, arm, trace_ledger).run(World(scenario, seed))

def main():
    output = []
    for scenario in SCENARIOS:
        for arm in ARMS:
            result = run(DEVELOPMENT_SEEDS[0], scenario, arm)
            output.append(result)
            print(scenario, arm, 'errorsB', result['counts']['B']['errors'],
                  'served', result['counts']['B']['served'], 'cash', result['final_cash'] / 1000,
                  'mandate', result['mandate_changes'], 'rules', result['rule_changes'],
                  'reviews', result['reviews'], 'lost/rebuilt', result['checker_losses'], result['checker_rebuilds'])
    Path(__file__).with_name('development-v3-seed1103.json').write_text(json.dumps(output, indent=2) + '\n')

if __name__ == '__main__':
    main()
