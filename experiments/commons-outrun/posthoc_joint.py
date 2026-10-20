"""Post hoc, after the frozen runs (not a prediction): why the joint learner (k3s1_joint) failed.

Two diagnostics, both run after VERDICTS.json was written:
1. Control: CG1's single coupled learner (k = 1, s = 1, own apples + 2 x last level) trained by this
   experiment's code, 3 seeds; CG1 round 2 kept the patch in 20/20 seeds.  Kept here too means the joint
   failure is not a fault of the shared code.
2. The joint learner's greedy actions and Q-values at a few steps left, seed diag/joint/0, against the
   exact optimum from calibrate.value (the values a converged learner would hold are near the exact ones).

    python3 posthoc_joint.py > results/posthoc-joint.txt
"""
from multiprocessing import Pool

import learners
from conditions import cond

SPEC = dict(H=100, alpha=0.1, eps_end=0.02, eps_frac=0.8, episodes=30000, eval_episodes=50, probe=20)


def control(s):
    r = learners.train_eval(dict(SPEC, cond=cond(1, 1, lock="open"), seed=f"diag/c1/{s}"))
    return s, sum(1 for x in r["eval"]["alive_probe"] if x >= 1) / 50


def joint_table():
    store = []
    base = learners.Q

    class Kept(base):
        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            store.append(self)

    learners.Q = Kept
    try:
        learners.train_eval(dict(SPEC, cond=cond(3, 1, joint=True, lock="open"), seed="diag/joint/0"))
    finally:
        learners.Q = base
    ag = store[0]
    rows = []
    for tau in (100, 60, 30, 10, 3, 1):
        cells = []
        for x in range(10):
            i = ag.idx(x, tau)
            q = ag.q[i:i + 4]
            cells.append(f"{q.index(max(q))}:" + "/".join(f"{v:.0f}" for v in q))
        rows.append(f"steps left {tau:3d}  " + " ".join(cells))
    return rows


if __name__ == "__main__":
    with Pool(3) as p:
        res = p.map(control, range(3))
    print("control k=1 coupled (share of evaluation episodes alive at H-20):", res)
    print("joint learner, level 0..9: greedy action (requests): Q(0)/Q(1)/Q(2)/Q(3)")
    for r in joint_table():
        print(r)
