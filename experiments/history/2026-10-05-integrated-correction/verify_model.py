"""Reproducible numerical audit of a conditional funded-correction model.

Run with Python, numpy, scipy, and matplotlib. No empirical data are used.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from pathlib import Path
import hashlib
import json
import platform

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import expit, logit


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


@dataclass(frozen=True)
class Parameters:
    y0: float = 1.0
    B: float = 0.8
    chi: float = 1.0
    eta: float = 10.0
    mu: float = 1.0
    K: float = 1.0
    kappa: float = 1.0
    tau: float = 1.0 / 6.0

    @property
    def A(self):
        return self.chi * self.B


def probability(c, p, mode="ordinary"):
    channel = np.asarray(c) / (p.K + np.asarray(c))
    return channel * channel if mode not in ("no_evidence", "no_execution") else channel * 0.0


def receipt(c, p, mode="ordinary"):
    return p.y0 + p.A * probability(c, p, mode)


def advantage(c, p, mode="ordinary"):
    r = receipt(c, p, mode)
    return -p.tau * r if mode == "free_access" else (1.0 - p.tau) * r - p.y0


def physical_rhs(x, c, p, mode="ordinary"):
    return np.array([
        p.kappa * x * (1.0 - x) * advantage(c, p, mode),
        p.eta * p.tau * x * receipt(c, p, mode) - p.mu * c,
    ])


def trajectory(initial, p, horizon=300.0, mode="ordinary", samples=1601):
    x0, c0 = initial
    assert 0.0 < x0 < 1.0 and c0 >= 0.0

    def rhs(_t, state):
        z, c = state
        dc = p.eta * p.tau * expit(z) * receipt(c, p, mode) - p.mu * c
        if mode == "external_capacity":
            dc = 0.0
        return [p.kappa * advantage(c, p, mode), dc]

    sol = solve_ivp(rhs, (0.0, horizon), [logit(x0), c0], method="DOP853",
                    rtol=2e-10, atol=2e-12, dense_output=True)
    assert sol.success, sol.message
    time = np.linspace(0.0, horizon, samples)
    states = sol.sol(time)
    assert states[1].min() > -1e-8
    return {"t": time, "x": expit(states[0]), "C": states[1], "log_odds": states[0]}


def full_capacity(p):
    upper = p.eta * p.tau * (p.y0 + p.A) / p.mu
    return brentq(lambda c: p.eta * p.tau * receipt(c, p) - p.mu * c,
                  0.0, upper * 1.01 + 1e-12, xtol=1e-13)


def threshold(p):
    if p.A == 0:
        return None
    z2 = p.tau * p.y0 / ((1.0 - p.tau) * p.A)
    if not 0.0 < z2 < 1.0:
        return None
    z = np.sqrt(z2)
    return {"z": float(z), "C_s": float(p.K * z / (1.0 - z)),
            "x_s": float(p.mu * p.K / (p.eta * p.A * z * (1.0 - z)))}


def fee_window(p):
    if p.eta * p.A <= 4.0 * p.mu * p.K:
        return None
    delta = np.sqrt(1.0 - 4.0 * p.mu * p.K / (p.eta * p.A))
    zz = np.array([(1.0 - delta) / 2.0, (1.0 + delta) / 2.0])
    return p.A * zz**2 / (p.y0 + p.A * zz**2)


def jacobian(x, c, p):
    rp = p.A * 2.0 * c * p.K / (p.K + c)**3
    return np.array([
        [p.kappa * (1.0 - 2.0 * x) * advantage(c, p),
         p.kappa * x * (1.0 - x) * (1.0 - p.tau) * rp],
        [p.eta * p.tau * receipt(c, p), p.eta * p.tau * x * rp - p.mu],
    ])


def summarize(tr):
    return {"x_final": float(tr["x"][-1]), "C_final": float(tr["C"][-1]),
            "x_min": float(tr["x"].min()), "C_min": float(tr["C"].min()),
            "horizon": float(tr["t"][-1])}


def task_enumeration(c, p, alpha=.9, evidence=True, execution=True):
    """Enumerate latent context, probe, implementation, and noisy signal.

    Independent uninformed guesses and fail-to-enact fallback are fair coins.
    Output b+Delta*correct; the witness uses b=0, Delta=2.
    """
    e = c / (p.K + c) if evidence else 0.0
    a = c / (p.K + c) if execution else 0.0
    proposed_correct = 0.0
    actual_correct = 0.0
    for context in (0, 1):
        for probe, pe in ((0, 1.0-e), (1, e)):
            for proposal in (0, 1):
                pp = (alpha if proposal == context else 1.0-alpha) if probe else .5
                weight = .5 * pe * pp
                proposed_correct += weight * (proposal == context)
                for enacted, pa in ((0, 1.0-a), (1, a)):
                    for fallback in (0, 1):
                        action = proposal if enacted else fallback
                        actual_correct += weight * pa * .5 * (action == context)
    return {"proposal_accuracy": proposed_correct, "enactment_probability": a,
            "actual_accuracy": actual_correct, "gross_output": 2.0*actual_correct}


def run():
    OUT.mkdir(exist_ok=True)
    p = Parameters()
    th = threshold(p)
    window = fee_window(p)
    cr = full_capacity(p)
    assert np.isclose(th["C_s"], 1.0) and np.isclose(th["x_s"], .5)
    assert np.linalg.norm(physical_rhs(th["x_s"], th["C_s"], p)) < 1e-12
    saddle_eigenvalues = np.linalg.eigvals(jacobian(th["x_s"], th["C_s"], p))
    high_eigenvalues = np.linalg.eigvals(jacobian(1.0, cr, p))
    assert np.prod(saddle_eigenvalues) < 0 and np.max(high_eigenvalues.real) < 0

    rng = np.random.default_rng(20261005)
    # Vary scales, capacities, costs, appropriation, and admissible task benefits.
    cases = []
    for _ in range(600):
        y0 = np.exp(rng.uniform(-1.5, 1.5))
        pp = Parameters(y0=y0, B=y0*rng.uniform(.05, 1.0), chi=rng.uniform(.03, 1.0),
                        eta=np.exp(rng.uniform(-1.0, 4.0)), mu=np.exp(rng.uniform(-1, 1)),
                        K=np.exp(rng.uniform(-1, 1)), tau=rng.uniform(.002, .95))
        ww = fee_window(pp)
        expected = ww is not None and ww[0] < pp.tau < ww[1]
        cc = full_capacity(pp)
        margin = float(advantage(cc, pp))
        assert expected == (margin > 0.0)
        stable = np.max(np.linalg.eigvals(jacobian(1.0, cc, pp)).real) < 0.0
        assert stable == expected
        # Exact fee/output accounting, including distributed common spillovers.
        x, c = rng.uniform(.01, .99), rng.uniform(.001, 8.0)*pp.K
        q = probability(c, pp)
        shared = x * (1.0-pp.chi) * pp.B * q
        fees = pp.tau*x*receipt(c, pp)
        retained = x*((1.0-pp.tau)*receipt(c, pp)+shared)+(1.0-x)*(pp.y0+shared)
        total_output = pp.y0 + x*pp.B*q
        assert abs(retained+fees-total_output) < 1e-10
        cases.append({"parameters": asdict(pp), "capacity_at_full_adoption": cc,
                      "selection_margin": margin, "inside_fee_window": bool(expected)})

    chain = {}
    for label, e, a in (("Both channels", True, True), ("Evidence only", True, False),
                        ("Execution only", False, True), ("Neither", False, False)):
        row = task_enumeration(1.0, p, evidence=e, execution=a)
        expected_output = p.y0 + p.B*(.25 if e and a else 0.0)
        assert abs(row["gross_output"]-expected_output) < 1e-12
        chain[label] = row
    assert chain["Evidence only"]["proposal_accuracy"] > chain["Neither"]["proposal_accuracy"]
    assert chain["Evidence only"]["gross_output"] == chain["Neither"]["gross_output"]
    assert abs(task_enumeration(1.0, p, alpha=.5)["gross_output"]-p.y0) < 1e-12

    trajectories = {
        "healthy": trajectory((.6, 1.2), p),
        "depleted": trajectory((.2, .4), p),
        "no_evidence": trajectory((.6, 1.2), p, mode="no_evidence"),
        "no_execution": trajectory((.6, 1.2), p, mode="no_execution"),
        "free_access": trajectory((.6, 1.2), p, mode="free_access"),
        "all_benefits_public": trajectory((.6, 1.2), replace(p, chi=0.0)),
        "uninformative_signal": trajectory((.6, 1.2), replace(p, B=0.0)),
        "insufficient_private_capture": trajectory((.6, 1.2), replace(p, chi=.25), horizon=1200),
        "fee_too_low": trajectory((.6, 1.2), replace(p, tau=.008), horizon=4000),
        "fee_too_high": trajectory((.6, 1.2), replace(p, tau=.42), horizon=1200),
        "external_capacity": trajectory((.6, 1.2), replace(p, tau=.008), mode="external_capacity"),
    }
    assert trajectories["healthy"]["x"].min() >= .6 - 1e-8
    assert trajectories["healthy"]["C"].min() >= th["C_s"] - 1e-8
    assert abs(trajectories["healthy"]["C"][-1] - cr) < 1e-7
    assert trajectories["depleted"]["x"].max() <= .25 + 1e-8
    assert trajectories["depleted"]["C"].max() <= .5 + 1e-8
    for name in ("depleted", "no_evidence", "no_execution", "free_access",
                 "all_benefits_public", "uninformative_signal",
                 "insufficient_private_capture", "fee_too_low", "fee_too_high"):
        assert trajectories[name]["x"][-1] < 1e-7, (name, summarize(trajectories[name]))
        assert abs(trajectories[name]["C"][-1]) < 1e-7
    assert trajectories["external_capacity"]["x"][-1] > 1.0-1e-7
    for name in ("no_execution", "all_benefits_public", "uninformative_signal"):
        # These interventions have identical adoption/funding equations here,
        # although useful public output need not be identical across them.
        for key in ("x", "C"):
            assert np.allclose(trajectories[name][key], trajectories["no_evidence"][key],
                               rtol=1e-8, atol=1e-10)

    # A conservative, finite capacity-only grant; membership is never overwritten.
    x0, c0 = .2, .4
    c1, xt = 10.0, .6
    time_bound = (logit(xt)-logit(x0))/(p.kappa*advantage(c1, p))
    seed_capacity = c1*np.exp(p.mu*time_bound)
    seed_cost = (seed_capacity-c0)/p.eta
    seeded = trajectory((x0, seed_capacity), p)
    early = trajectory((x0, seed_capacity), p, horizon=time_bound)
    assert early["C"].min() >= c1 - 1e-7
    assert early["x"][-1] >= xt - 1e-7
    assert seeded["x"][-1] > 1.0-1e-7 and abs(seeded["C"][-1]-cr) < 1e-7
    trajectories["capacity_seed"] = seeded

    # Exploratory extension after the original checks: equal current gross output
    # can hide different reproduction of the service. This is not preregistered.
    matched = {}
    for label, c in (("many_funders", .6), ("few_funders", 3.0)):
        x = .125/probability(c, p)
        gross = p.y0+x*p.B*probability(c, p)
        fee_flow = p.tau*x*receipt(c, p)
        run = trajectory((x, c), p)
        trajectories[f"matched_{label}"] = run
        persistent_entry = np.flatnonzero((run["x"] >= th["x_s"]) & (run["C"] >= th["C_s"]))
        depleted_entry = np.flatnonzero((run["x"] <= .25) & (run["C"] <= .5))
        matched[label] = {"initial": [float(x), c], "gross_output": float(gross),
                          "upkeep_flow": float(fee_flow), "retained_output": float(gross-fee_flow),
                          "first_sample_in_persistent_region": float(run["t"][persistent_entry[0]]) if len(persistent_entry) else None,
                          "first_sample_in_depleted_region": float(run["t"][depleted_entry[0]]) if len(depleted_entry) else None,
                          "result": summarize(run)}
    assert matched["many_funders"]["gross_output"] == matched["few_funders"]["gross_output"]
    assert matched["many_funders"]["first_sample_in_persistent_region"] is not None
    assert matched["few_funders"]["first_sample_in_depleted_region"] is not None

    # Include a nontrivial public spillover witness, separate from pure private capture.
    spillover_p = replace(p, chi=.75)
    spillover_th = threshold(spillover_p)
    spillover_initial = ((1.0+spillover_th["x_s"])/2.0, 1.2*spillover_th["C_s"])
    spillover = trajectory(spillover_initial, spillover_p)
    assert spillover_th["x_s"] < 1 and spillover["x"][-1] > 1-1e-7

    # Integration sensitivity for the difficult seed trajectory.
    def seed_rhs(_t, state):
        z, c = state
        return [p.kappa*advantage(c, p), p.eta*p.tau*expit(z)*receipt(c, p)-p.mu*c]
    refined = solve_ivp(seed_rhs, (0, 300), [logit(x0), seed_capacity], method="Radau",
                        rtol=2e-11, atol=2e-13, dense_output=True)
    assert refined.success
    reference = refined.sol(seeded["t"])
    integration_difference = float(max(np.max(np.abs(expit(reference[0])-seeded["x"])),
                                       np.max(np.abs(reference[1]-seeded["C"]))))
    assert integration_difference < 1e-5

    result = {
        "status": "All specified mathematical/numerical checks passed; no empirical validation.",
        "parameters": asdict(p), "threshold": th, "fee_window": window.tolist(),
        "full_adoption_capacity": cr, "full_adoption_selection_margin": float(advantage(cr, p)),
        "saddle_eigenvalues": saddle_eigenvalues.tolist(), "high_eigenvalues": high_eigenvalues.tolist(),
        "parameter_cases_checked": len(cases), "task_chain": chain,
        "trajectories": {key: summarize(val) for key, val in trajectories.items()},
        "finite_seed": {"original_state": [x0, c0], "C1": c1, "target_x": xt,
                        "time_bound": float(time_bound), "seed_capacity": float(seed_capacity),
                        "cost_bound": float(seed_cost), "state_at_time_bound": summarize(early),
                        "meaning": "Sufficient external one-time grant, not optimal or spontaneous recovery."},
        "exploratory_equal_current_output": matched,
        "public_spillover_witness": {"parameters": asdict(spillover_p), "threshold": spillover_th,
                                    "initial": list(spillover_initial), "result": summarize(spillover)},
        "independent_integrator_max_difference": integration_difference,
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (OUT / "verification.json").write_text(json.dumps(result, indent=2)+"\n")
    (OUT / "parameter-checks.json").write_text(json.dumps(cases, indent=2)+"\n")
    np.savez_compressed(OUT / "trajectories.npz",
                        **{f"{name}_{key}": arr for name, tr in trajectories.items() for key, arr in tr.items()})
    make_plot(p, th, window, cr, trajectories, chain)
    print(json.dumps(result, indent=2))


def make_plot(p, th, window, cr, tr, chain):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(12, 8.7), layout="constrained")
    green, red, blue = "#247B64", "#B24B42", "#4267AE"
    ax = axes[0, 0]
    ax.axvspan(0, 1, color="white")
    ax.fill_between([.5, 1], 1, 3, color=green, alpha=.1, label="Certified persistent region")
    ax.fill_between([0, .25], 0, .5, color=red, alpha=.14, label="Certified depleted region")
    xx, cc = np.meshgrid(np.linspace(.035, .965, 19), np.linspace(.06, 2.94, 19))
    dx, dc = physical_rhs(xx, cc, p)
    size = np.sqrt(dx*dx+(dc/3)**2)+1e-12
    ax.quiver(xx, cc, dx/size, dc/size, color="#777777", alpha=.45, width=.002)
    for initial in ((.1, 1.7), (.3, 1.4), (.4, .6), (.65, .6), (.8, .3), (.4, 2.5)):
        extra = trajectory(initial, p, horizon=180, samples=1201)
        color = green if extra["x"][-1] > .5 else red
        ax.plot(extra["x"], extra["C"], color=color, alpha=.45, lw=1)
    for name, color in (("healthy", green), ("depleted", red)):
        ax.plot(tr[name]["x"], tr[name]["C"], color=color, lw=2.5)
        ax.scatter(tr[name]["x"][0], tr[name]["C"][0], color=color, s=25)
    ax.scatter([.5], [1], marker="X", s=65, color="#252525", zorder=5)
    ax.scatter([1], [cr], s=55, color=green, zorder=5)
    ax.annotate("Saddle", (.5, 1), xytext=(.55, .91))
    ax.set(xlim=(0, 1.03), ylim=(0, 3), xlabel="Participation x", ylabel="Correction capacity C",
           title="A. Same rules, different starting conditions")
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    ax = axes[0, 1]
    fees = np.linspace(.0001, .5, 301)
    margins = [advantage(full_capacity(replace(p, tau=float(t))), replace(p, tau=float(t))) for t in fees]
    ax.axhline(0, color="#888888", lw=1)
    ax.axvspan(*window, color=green, alpha=.13)
    ax.plot(fees, margins, color=blue, lw=2.2)
    ax.scatter(window, [0, 0], color=green, zorder=5)
    ax.set(xlabel="Fraction of direct receipts spent on upkeep", ylabel="Advantage of participation at full adoption",
           title="B. Financing has a feasible interval")
    ax.text(.065, .021, "Selected and funded", color=green)
    ax.text(.39, -.09, "Too costly", color=red)
    ax.annotate("Underfunded", (window[0]/2, -.003), xytext=(.02, -.10),
                arrowprops={"arrowstyle": "-", "color": red}, color=red)

    ax = axes[1, 0]
    for name, color, label in (("healthy", green, "Healthy start"),
                              ("depleted", red, "Depleted start"),
                              ("capacity_seed", blue, "Depleted + one-time capacity grant")):
        ax.plot(tr[name]["t"], tr[name]["x"], label=label, color=color, lw=2)
    ax.axhline(.5, color="#888888", ls="--", lw=.8)
    ax.set(xlim=(0, 80), ylim=(0, 1.04), xlabel="Time (capacity decay rate = 1)",
           ylabel="Participation x", title="C. Upkeep and initiation are different problems")
    ax.legend(fontsize=8, frameon=False, loc="center right")

    ax = axes[1, 1]
    labels = list(chain)
    positions = np.arange(len(labels))
    accuracy = [chain[k]["proposal_accuracy"] for k in labels]
    increase = [(chain[k]["gross_output"]-p.y0)/p.B for k in labels]
    ax.bar(positions-.17, accuracy, .34, color=blue, label="Proposal accuracy")
    ax.bar(positions+.17, increase, .34, color=green, label="Fraction of potential output gain")
    ax.axhline(.5, color="#888888", lw=.8, ls="--")
    ax.set(xticks=positions, xticklabels=["Both", "Evidence\nonly", "Execution\nonly", "Neither"],
           ylim=(0, 1.0), title="D. Information needs a route into action")
    ax.set_ylabel("Probability / fraction (capacity C = 1)")
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    fig.suptitle("A correction practice must reproduce its own operating conditions", fontsize=16)
    fig.supxlabel("Illustrative mathematical model · fixed task, collection and access rules · no empirical fitting", fontsize=10)
    fig.savefig(OUT / "integrated-correction.png", dpi=180)
    fig.savefig(OUT / "integrated-correction.svg")
    plt.close(fig)


if __name__ == "__main__":
    run()
