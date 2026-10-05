"""Finite exact checks for the scientific-principles research note.

Standard library only. Fractions make the Bernoulli path probabilities exact.
These are conditional calculations, not sampled experiments or empirical data.
Run with python3 reproduce.py; results are saved next to this script.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def binomial_tail(n, k, p=F(1, 2)):
    return sum((F(comb(n, j)) * p**j * (1-p)**(n-j)
                for j in range(k, n+1)), F(0))


def crossing(nmax, p, reject):
    # Live mass for each count after n observations; rejection is absorbing.
    live = {0: F(1)}
    absorbed = F(0)
    expected_samples = F(0)
    by_time = []
    for n in range(1, nmax+1):
        expected_samples += sum(live.values())
        nxt = {}
        for k, mass in live.items():
            for new_k, probability in [(k, 1-p), (k+1, p)]:
                w = mass * probability
                if reject(n, new_k):
                    absorbed += w
                else:
                    nxt[new_k] = nxt.get(new_k, F(0)) + w
        live = nxt
        assert sum(live.values()) + absorbed == 1
        by_time.append(absorbed)
    return absorbed, expected_samples, by_time


def record(x):
    return {"exact": str(x), "decimal": float(x)}


def main():
    nmax = 100
    alpha = F(1, 20)
    tails = {(n, k): binomial_tail(n, k)
             for n in range(1, nmax+1) for k in range(n+1)}
    rules = {
        "fixed_n_100": lambda n, k: n == nmax and tails[n, k] <= alpha,
        "repeated_fixed_sample_p": lambda n, k: tails[n, k] <= alpha,
        "alpha_spending": lambda n, k: tails[n, k] <= alpha / (n*(n+1)),
        "likelihood_ratio": lambda n, k: F(3, 2)**k * F(1, 2)**(n-k) >= 1/alpha,
    }
    sequential = {}
    for name, rule in rules.items():
        row = {}
        for label, p in [("null_p_half", F(1, 2)), ("alternative_p_three_quarters", F(3, 4))]:
            prob, samples, path = crossing(nmax, p, rule)
            row[label] = {"rejection_probability": record(prob),
                          "expected_samples": record(samples)}
        sequential[name] = row
    assert sequential["repeated_fixed_sample_p"]["null_p_half"]["rejection_probability"]["decimal"] > .05
    for name in ["fixed_n_100", "alpha_spending", "likelihood_ratio"]:
        assert F(sequential[name]["null_p_half"]["rejection_probability"]["exact"]) <= alpha
    # Independent full-path enumeration checks probabilities and sample counts.
    for name, rule in rules.items():
        nsmall = 10
        small_rule = (lambda n, k: n == nsmall and tails[n, k] <= alpha) if name == 'fixed_n_100' else rule
        for p in [F(1,2), F(3,4)]:
            probability, sample_sum = F(0), F(0)
            for code in range(2**nsmall):
                bits = [(code >> j) & 1 for j in range(nsmall)]
                total_k = sum(bits)
                weight = p**total_k * (1-p)**(nsmall-total_k)
                k, stopped, did_reject = 0, nsmall, False
                for n, bit in enumerate(bits, 1):
                    k += bit
                    if small_rule(n, k):
                        stopped, did_reject = n, True
                        break
                probability += weight * did_reject
                sample_sum += weight * stopped
            dp_probability, dp_samples, _ = crossing(nsmall, p, small_rule)
            assert dp_probability == probability
            assert dp_samples == sample_sum

    # Testing two simple coin laws with every finite sequence possible.
    n = 20
    p0, p1 = F(1, 2), F(3, 4)
    probs0 = [F(comb(n, k))*p0**k*(1-p0)**(n-k) for k in range(n+1)]
    probs1 = [F(comb(n, k))*p1**k*(1-p1)**(n-k) for k in range(n+1)]
    tv = sum(abs(a-b) for a,b in zip(probs0, probs1))/2
    optimum = sum(min(a,b) for a,b in zip(probs0, probs1))/2
    assert optimum == (1-tv)/2
    threshold = min(k for k in range(n+1) if binomial_tail(n,k) <= alpha)
    alpha_actual, power = binomial_tail(n,threshold), binomial_tail(n,threshold,p1)
    assert alpha_actual + (1-power) >= 1-tv
    coin = {"n":n,"reject_if_heads_at_least":threshold,
            "actual_size":record(alpha_actual),"power_p_three_quarters":record(power),
            "tv":record(tv),"equal_prior_minimum_error":record(optimum)}

    # Two causal models agree observationally and disagree after do(X=1).
    observed = [{"x":u,"y":u,"probability":.5} for u in [0,1]]
    causal = {"model_A":"X=U, Y=X; U ~ Bernoulli(1/2)",
              "model_B":"X=U, Y=U; U ~ Bernoulli(1/2)",
              "observed_law_both":observed,
              "P_Y1_under_do_X1":{"model_A":1.0,"model_B":.5}}

    # Measurement package Y = physical state XOR sensor inversion.
    rows=[{"state":s,"sensor_inverted":b,"routine":s^b,"known_zero_reference":b}
          for s in [0,1] for b in [0,1]]
    for row in rows:
        assert row["routine"] ^ row["known_zero_reference"] == row["state"]
    for y in [0,1]:
        compatible=[r for r in rows if r["routine"]==y]
        assert {r["state"] for r in compatible} == {0,1}

    # Independent error checking and a latent common-mode miss.
    checks=[]
    for k in [1,2,3,5,10]:
        q,r=F(1,10),F(1,5)
        checks.append({"checks":k,"all_miss_independent":record(r**k),
                       "all_miss_independent_same_marginal":record((q+(1-q)*r)**k),
                       "all_miss_shared_mode":record(q+(1-q)*r**k)})

    out={"status":"exact finite calculations using rational arithmetic",
         "assumptions":"Specified iid Bernoulli laws; frozen rules; hard maximum 100 observations; no empirical data.",
         "sequential":sequential,"coin_n20":coin,"causal_example":causal,
         "measurement_package":rows,"checking_error":checks,
         "twenty_independent_tests_each_size_point05":record(1-F(19,20)**20),
         "checks_passed":["probability mass at every DP step","small-horizon exhaustive path enumeration",
                          "TV optimum identity","error lower bound","sequential null bounds",
                          "auxiliary calibration recovers physical state"]}
    path=Path(__file__).resolve().parent / 'verification-results.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({"coin_n20":coin,"sequential":sequential,"checks_passed":out["checks_passed"]},indent=2))


if __name__ == '__main__':
    main()
