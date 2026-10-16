"""Reproduce the constructed renewal illustration. Requires numpy/scipy/matplotlib."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent


def dynamics(kappa):
    def f(t, y):
        e, c, x = y
        u = .1 + .4 * x
        return [9*c/(1+c) - e - u*e*c, (u*e-1)*c, (1-kappa)*e*.4*x*(1-x)]
    return f


numerical = {}
for kappa in (.5, 1.5):
    sol = solve_ivp(dynamics(kappa), [0, 200], [2, 3+np.sqrt(7), .99],
                    rtol=1e-10, atol=1e-12, max_step=.1, dense_output=True)
    assert sol.success
    trajectory = sol.sol(np.linspace(0, 200, 20001))
    end = sol.y[:, -1]
    if kappa == .5:
        assert np.max(np.abs(end-np.array([2, 3+np.sqrt(7), 1]))) < 1e-7
    else:
        assert end[0] < 1e-8 and end[1] < 1e-8
        assert 0 < end[2] < .99
        assert 4.63 < trajectory[0].max() < 4.64
    numerical[str(kappa)] = {"endpoint": end.tolist(), "sampled_support_peak": float(trajectory[0].max()), "integration_success": bool(sol.success)}

u = np.linspace(.25001, 1.05, 900)
d = 1/u
c = (8-d+np.sqrt((8-d)**2-4*d))/2
e = 1/u
lo, hi, choice = 7/12, 2/3, 5/8
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(2, 1, figsize=(10, 7.4), sharex=True)
fig.subplots_adjust(left=.115, right=.96, bottom=.16, top=.83, hspace=.27)
fig.suptitle("Renewal can face conflicting requirements", x=.115, y=.975, ha="left", fontsize=19, fontweight="bold")
fig.text(.115, .925, "A constructed model: more effort raises capacity but lowers available support.", ha="left", fontsize=11, color="#4b5563")
for ax, values, floor, label, color in zip(axes, [e, c], [1.5, 6], ["Support at equilibrium", "Capacity at equilibrium"], ["#245f99", "#88542e"]):
    ax.axvspan(lo, hi, color="#c6e8d0", alpha=.75)
    ax.plot(u, values, color=color, lw=2.5)
    ax.axhline(floor, ls="--", color="#a83d3d", lw=1.4)
    ax.axvline(choice, color="#496b55", ls=":", lw=1)
    actual = 1/choice if floor == 1.5 else (16+6*np.sqrt(6))/5
    ax.scatter([choice], [actual], color=color, s=38, zorder=4)
    ax.set_ylabel(label)
    ax.grid(axis="y", color="#e5e7eb", lw=.8)
    ax.set_xlim(.25, 1.05)
    ax.text(1.035, floor, f" required > {floor:g}", ha="right", va="bottom", color="#a83d3d", fontsize=10)
axes[0].set_ylim(.75, 4.15)
axes[1].set_ylim(1.8, 7.1)
axes[0].text(choice, 3.8, "Both requirements satisfied\n7/12 < effort < 2/3", ha="center", fontsize=10, color="#28573a")
axes[1].annotate("effort 5/8", (choice, (16+6*np.sqrt(6))/5), xytext=(.75, 5),
                 arrowprops={"arrowstyle":"-", "color":"#6b7280"}, fontsize=10)
axes[1].set_xlabel("Selected renewal effort u")
axes[1].set_xticks([.25, .5, choice, .75, 1.0])
axes[1].set_xticklabels(["1/4", "1/2", "5/8", "3/4", "1"])
fig.text(.115, .065, "P(C) = 9C/(1+C); loss and conversion parameters equal 1. Upper equilibrium branch shown.\nLocal attraction also requires selection to favor this effort; reaching its basin has a separate cost.", fontsize=9, color="#4b5563", ha="left")
fig.savefig(HERE / "renewal-tradeoff.png", dpi=180, facecolor="white")
fig.savefig(HERE / "renewal-tradeoff.svg", facecolor="white")
plt.close(fig)
(HERE / "NUMERICAL-CHECKS.json").write_text(json.dumps({"scope": "Constructed illustrative integration, not proof or empirical validation; tiny endpoint magnitudes are not certified precision.", "horizon": 200, "rtol": 1e-10, "atol": 1e-12, "max_step": .1, "sampled_times": 20001, "results": numerical}, indent=2)+"\n")
print(json.dumps({"checked_trajectories": len(numerical), "figure": "renewal-tradeoff.png"}))
