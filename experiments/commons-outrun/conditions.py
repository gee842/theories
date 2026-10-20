"""The frozen conditions of CG2 and the outcome each is predicted to reach (PREDICTIONS-2026-10-20.md).

k: members on one isolated 3x3 patch; s: regrowth scale (Perolat probabilities times s, capped at
1); lam: weight of the reading of the level after the last step; v: weight of the reading of the
level after each step; share: each member is rewarded the step's apples divided by k instead of
its own; joint: one learner chooses how many of the k requests to make (reading the union).

`lock` is the class the exact calibration gives (calibrate.py; the rule is in the predictions
file): "locked" where harvesting at every step is a best response against a rest that does so
(gain < 0.25), "open" where it is not (gain >= 1.0).  The prediction follows from the class:
locked -> depleted, open -> kept.
"""

V_STAR = 0.2134          # calibrate.py: v* in [0.21333, 0.21340] for k = 3, s = 1
V_LO = 0.107             # about v* / 2
V_HI = 0.64              # about 3 v*


def cond(k, s, lam=2.0, v=0.0, share=False, joint=False, lock=None):
    return dict(k=k, s=s, lam=lam, v=v, share=share, joint=joint, lock=lock,
                predicted="depleted" if lock == "locked" else "kept")


CONDITIONS = {
    # the rest outruns the renewal: depletion locked for every weight of the end reading
    "k3s1": cond(3, 1, lock="locked"),             # CG1's D2b c3, replicated
    "k3s1_lam32": cond(3, 1, lam=32.0, lock="locked"),
    "k2s1": cond(2, 1, lock="locked"),
    "k3s8": cond(3, 8, lock="locked"),
    # the rest cannot outrun the renewal, the whole can: open
    "k2s8": cond(2, 8, lock="open"),
    "k3s16": cond(3, 16, lock="open"),
    # a reading before the rest's end, below and above v*
    "k3s1_vlo": cond(3, 1, lam=0.0, v=V_LO, lock="locked"),
    "k3s1_vhi": cond(3, 1, lam=0.0, v=V_HI, lock="open"),
    # reward sharing: restraint seen only through the renewal it lets through
    "k3s1_share": cond(3, 1, lam=0.0, share=True, lock="locked"),
    "k3s8_share": cond(3, 8, lam=0.0, share=True, lock="open"),
    # one selector reading the union of the three couplings
    "k3s1_joint": cond(3, 1, joint=True, lock="open"),
}

LOCKED_BELOW = 0.25
OPEN_FROM = 1.0
