"""The frozen conditions of CG3 (PREDICTIONS-2026-10-20.md) and what each account predicts.

One selector on CG2's gated 3x3 patch: m = most requests per step, s = regrowth scale, w =
weight of the level after the last step, v = weight of the level after each step (0 here), q0 =
initial action value (0 as in CG2; 100 for optimistic initial values, above every exact value).

`cov` is the account under test (the selector's own exploratory draw against the renewal):
the exact expected number of steps, of 100, that the patch stands from a full patch when the
requests are drawn uniformly from 0..m at every step (the behaviour at the start of training).
Kept where cov >= COV_KEEP, depleted where cov <= COV_DEPLETE; between, only an order is
predicted.  The other accounts' predictions are listed for the contrasts (PREDICTIONS file).
"""

COV_KEEP = 20.0      # anchors: CG2's control (m = 1, s = 1) cov 23.7, kept 3/3 post hoc
COV_DEPLETE = 7.0    # CG2's k3s1_joint (m = 3, s = 1) cov 6.0, depleted 0/20
Q0_OPT = 100.0


def cond(m, s, w=6.0, v=0.0, q0=0.0, predicted=None):
    return dict(m=m, s=s, w=w, v=v, q0=q0, predicted=predicted)


CONDITIONS = {
    "J3": cond(3, 1, predicted="depleted"),            # CG2's k3s1_joint, new seeds
    "J2": cond(2, 1, predicted="between"),
    "J1": cond(1, 1, predicted="kept"),
    "J1w0": cond(1, 1, w=0.0, predicted="kept"),
    "J3w0": cond(3, 1, w=0.0, predicted="depleted"),
    "J3w48": cond(3, 1, w=48.0, predicted="depleted"),
    "J3s8": cond(3, 8, predicted="kept"),
    "J3s16": cond(3, 16, predicted="kept"),
    "J3opt": cond(3, 1, q0=Q0_OPT, predicted="kept"),
}
