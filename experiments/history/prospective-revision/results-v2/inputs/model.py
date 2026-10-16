"""Exact finite workflow risks. See PROTOCOL.md for information and cost scope."""
from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import product
from math import comb

import numpy as np
from scipy.optimize import linprog
from scipy.stats import binom


@dataclass(frozen=True)
class World:
    name: str
    q: float
    p: float  # future switch rate when d>0; d<0 has .5-p


WORLDS = (World("E", 1/3, .25), World("P", 1., .45),
          World("T", 1., .25), World("U", 1/3, .45))
TAU_MIN = 69/512
K2_PROB = 27/128


@dataclass(frozen=True)
class Params:
    validation_size: int = 1024
    deployment_size: int = 500
    audit_fee: float = .02
    validation_fee: float = .002
    running_fee: float = .002
    response_cost: float = .3
    audit_alpha: float = .05
    validation_alpha: float = .05
    max_audits: int = 128
    expense_cap: float = 6.
    question_probability: float = .5

    @property
    def threshold(self):
        return self.response_cost + self.running_fee / TAU_MIN


def eligibility(q):
    return (120+54*q)/1024


def atoms(world):
    """Full joint enumeration of switch word, endpoint, next need, mass."""
    for b in product((0, 1), repeat=4):
        k = sum(b)
        pk = comb(4, k)*(.25**k)*(.75**(4-k))
        cluster = b in ((0, 0, 1, 1), (1, 1, 0, 0))
        cond = (world.q/2 if cluster else (1-world.q)/4) if k == 2 else 1/comb(4, k)
        d = sum(b[2:])-sum(b[:2])
        rate = world.p if d > 0 else .5-world.p if d < 0 else .25
        for z, y in product((0, 1), repeat=2):
            py = rate if z == 0 else 1-rate
            yield b, z, y, pk*cond*.5*(py if y else 1-py)


@lru_cache(None)
def critical_values(max_n, null_p, alpha):
    """Smallest accepted upper-tail count; n+1 means never reject."""
    result = np.arange(max_n+1, dtype=int)+1
    if null_p >= 1 or alpha <= 0:
        return tuple(result)
    for n in range(1, max_n+1):
        counts = np.arange(n+1)
        hits = counts[binom.sf(counts-1, n, null_p) <= alpha]
        if len(hits):
            result[n] = hits[0]
    return tuple(result)


def mixed_binomial_test(size, eligibility_probability, success_probability, null_p, alpha):
    n = np.arange(size+1)
    critical = np.asarray(critical_values(size, null_p, alpha))
    return float(np.dot(binom.pmf(n, size, eligibility_probability),
                        binom.sf(critical-1, n, success_probability)))


@lru_cache(None)
def audit_power(m, q, alpha=.05):
    return mixed_binomial_test(m, K2_PROB, q, 1/3, alpha)


@lru_cache(None)
def validation_power(world, params):
    return mixed_binomial_test(params.validation_size, eligibility(world.q), world.p,
                               params.threshold, params.validation_alpha)


def branch_expense(m, eta, params):
    # Conservative maximum. m=0, eta=0 can never open validation.
    if m == 0 and eta == 0:
        return 0.
    return m*params.audit_fee + params.validation_size*params.validation_fee + params.deployment_size*params.running_fee


def workflow_risk(world, m, eta, params):
    a = audit_power(m, world.q, params.audit_alpha)
    r = a+(1-a)*eta
    v = validation_power(world, params)
    adopt = r*v
    lam = params.question_probability
    gross = eligibility(world.q)*(world.p-params.response_cost)
    archive = m*params.audit_fee
    validate = lam*r*params.validation_size*params.validation_fee
    running = lam*adopt*params.deployment_size*params.running_fee
    operating_improvement = lam*adopt*params.deployment_size*gross
    return {"audit_probability": a, "validation_open_probability_given_question": r,
            "validation_accept_probability_given_open": v,
            "adopt_probability_given_question": adopt,
            "archive_expense": archive, "validation_expense": validate,
            "running_expense": running, "operating_improvement": operating_improvement,
            "incremental_loss": archive+validate+running-operating_improvement,
            "total_loss_continuation_deployment_plus_expense":
                lam*params.deployment_size*.275+archive+validate+running-operating_improvement,
            "branch_expense_bound": branch_expense(m, eta, params)}


def workflows(params):
    candidates = [("none", 0, 0.)]
    candidates += [(f"audit-{m}", m, 0.) for m in range(1, params.max_audits+1)]
    candidates += [("direct", 0, 1.)]
    return [{"name": name, "m": m, "eta": eta,
             "worlds": {w.name: workflow_risk(w, m, eta, params) for w in WORLDS}}
            for name, m, eta in candidates
            if branch_expense(m, eta, params) <= params.expense_cap+1e-12]


def loss_matrix(rows):
    return np.array([[row["worlds"][w.name]["incremental_loss"] for w in WORLDS]
                     for row in rows])


def prior_grid(denominator):
    for e in range(denominator+1):
        for p in range(denominator-e+1):
            for t in range(denominator-e-p+1):
                u = denominator-e-p-t
                yield np.array([e, p, t, u], dtype=float)/denominator


def minimax_regret(rows):
    c = loss_matrix(rows)
    best = c.min(axis=0)
    regrets = c-best
    count = len(rows)
    objective = np.r_[np.zeros(count), 1.]
    a_ub = np.column_stack((regrets.T, -np.ones(len(WORLDS))))
    a_eq = np.array([np.r_[np.ones(count), 0.]])
    fit = linprog(objective, A_ub=a_ub, b_ub=np.zeros(len(WORLDS)),
                  A_eq=a_eq, b_eq=[1.], bounds=[(0, None)]*(count+1), method="highs")
    if not fit.success:
        raise RuntimeError(fit.message)
    weights = fit.x[:-1]
    state_regrets = weights@regrets
    dual_value = float(fit.eqlin.marginals[0])
    dual_slack = objective-a_ub.T@fit.ineqlin.marginals-a_eq.T@fit.eqlin.marginals
    pure = int(np.argmin(regrets.max(axis=1)))
    return {"worst_regret": float(fit.fun), "dual_value": dual_value,
            "duality_gap": abs(float(fit.fun)-dual_value),
            "max_primal_violation": float(max(0., (a_ub@fit.x).max(), abs(weights.sum()-1))),
            "max_dual_violation": float(max(0., -dual_slack.min())),
            "world_best_loss": dict(zip([w.name for w in WORLDS], best.tolist())),
            "world_regrets": dict(zip([w.name for w in WORLDS], state_regrets.tolist())),
            "mixture": [{"workflow": rows[i]["name"], "probability": float(v)}
                        for i, v in enumerate(weights) if v > 1e-10],
            "best_pure": {"workflow": rows[pure]["name"],
                          "worst_regret": float(regrets[pure].max())}}
