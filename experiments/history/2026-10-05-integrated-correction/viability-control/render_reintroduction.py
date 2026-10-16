"""Render the declared exploratory perturbation from saved trajectories."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "results"
data = np.load(OUT / "trajectories.npz")
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), layout="constrained")
curves = [
    ("changing_targets", "equilibrium_rule", "#4267AE", "--", "Rule toward target / 6, no perturbation"),
    ("exploratory_reintroduction", "equilibrium_rule", "#B24B42", "-", "Same rule, 1% alternative reintroduced"),
    ("exploratory_reintroduction", "filtered", "#247B64", "-", "Constraint filter, same reintroduction"),
    ("exploratory_reintroduction", "cap_0.7", "#BB8B2F", "-", "Fixed cap .7, same reintroduction"),
]
for case, policy, color, ls, label in curves:
    key = f"{case}_{policy}"
    t, state = data[key + "_t"], data[key + "_state"]
    for ax, idx in zip(axes, (3, 1)):
        ax.plot(t, state[idx], color=color, ls=ls, lw=1.9, label=label)
for ax in axes:
    ax.axvspan(450, 600, color="grey", alpha=.08)
    ax.axvline(450, color="black", ls=":", lw=1)
    ax.set(xlim=(420, 750), xlabel="Time")
axes[0].set(ylabel="Verification G", title="A. Apparent target success can be vulnerable")
axes[0].legend(frameon=False, fontsize=8, loc="center right")
axes[1].set(ylabel="Genuine maintenance share h", title="B. A represented alternative can regain ground", ylim=(-.02, 1.03))
axes[1].axhline(.9, color="black", ls=":", lw=.8)
axes[1].text(455, .15, "Target 6", color="#666666")
axes[1].text(645, .15, "Target 4", color="#666666")
fig.suptitle("Testing persistence after a one percent practice reintroduction", fontsize=15)
fig.supxlabel("Exploratory model intervention at time 450 · shaded phase requests G = 6 · finite horizon", fontsize=10)
fig.savefig(OUT / "reintroduction.png", dpi=180)
fig.savefig(OUT / "reintroduction.svg")
plt.close(fig)
