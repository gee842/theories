"""A commons with gated renewal, in the style of the Harvest game (Perolat et al. 2017).

Apples stand on the cells of patches.  At each step every agent either waits or harvests
one apple from the patch it is assigned to; then each empty cell regrows with a
probability read off the number of apples standing within Euclidean distance 2 of it
(Perolat et al. 2017: 0 with none, 0.01 with one or two, 0.05 with three or four, 0.1 with
more).  A cell with no apple within distance 2 never regrows, so a patch whose cells see no
apple of another patch renews only while at least one of its own apples stands: the gate
of `Flow.joint_excess_ends` with need m = 1.

Departure from Perolat et al. (stated, deliberate): agents do not walk.  An agent's whole
choice is to harvest or wait at its patch, so that tabular learners can be trained on a
CPU.  Tagging is left out.

Accounting is exact: at each step and patch the level after is the level before minus
what was taken plus what was given (`Flow.Balances`), in whole apples.  Every random draw
comes from a stream owned by one patch, so what happens at one patch never reads another
patch's stream.
"""

import random

PEROLAT = (0.0, 0.01, 0.01, 0.05, 0.05, 0.1)  # by neighbour count 0..5; 5 means "more than 4"


def regrow_prob(k, table=PEROLAT):
    return table[min(k, len(table) - 1)]


def block(x0, y0, w=3, h=3):
    return [(x0 + i, y0 + j) for j in range(h) for i in range(w)]


class Commons:
    """Patches of cells on a plane, with radius-2 regrowth across all of them."""

    def __init__(self, patches, seed, table=PEROLAT, radius2=4):
        self.patches = [list(p) for p in patches]
        self.table = table
        cells = [c for p in self.patches for c in p]
        if len(set(cells)) != len(cells):
            raise ValueError("patches overlap")
        self.index = {c: i for i, c in enumerate(cells)}
        self.owner = []
        for pi, p in enumerate(self.patches):
            self.owner += [pi] * len(p)
        self.ncells = len(cells)
        self.nbrs = [
            [self.index[d] for d in cells
             if d != c and (d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2 <= radius2]
            for c in cells
        ]
        self.patch_cells = [[self.index[c] for c in p] for p in self.patches]
        self.seed = seed
        self.rngs = [random.Random(f"{seed}/patch/{i}") for i in range(len(self.patches))]
        self.apple = [1] * self.ncells

    def reset(self, full=True):
        self.apple = [1 if full else 0] * self.ncells

    def level(self, pi):
        a = self.apple
        return sum(a[i] for i in self.patch_cells[pi])

    def levels(self):
        return [self.level(pi) for pi in range(len(self.patches))]

    def crosses(self):
        """Pairs of patches some of whose cells lie within distance 2 of each other."""
        out = set()
        for i, ns in enumerate(self.nbrs):
            for j in ns:
                if self.owner[i] != self.owner[j]:
                    out.add(tuple(sorted((self.owner[i], self.owner[j]))))
        return sorted(out)

    def step(self, requests):
        """requests[pi] = list of agent ids asking to harvest at patch pi this step.

        Returns (taken, given, got): per-patch amounts taken and given, and the set of agents
        whose harvest succeeded.  Harvest comes first, then regrowth on what stands after it.
        """
        a = self.apple
        npatch = len(self.patches)
        taken = [0] * npatch
        got = set()
        for pi in range(npatch):
            req = list(requests[pi]) if pi < len(requests) else []
            if not req:
                continue
            rng = self.rngs[pi]
            rng.shuffle(req)
            standing = [i for i in self.patch_cells[pi] if a[i]]
            for agent in req:
                if not standing:
                    break
                k = rng.randrange(len(standing))
                cell = standing.pop(k)
                a[cell] = 0
                taken[pi] += 1
                got.add(agent)
        given = [0] * npatch
        new = []
        for pi in range(npatch):
            rng = self.rngs[pi]
            for i in self.patch_cells[pi]:
                if a[i]:
                    continue
                k = 0
                for j in self.nbrs[i]:
                    k += a[j]
                p = regrow_prob(k, self.table)
                # one draw per empty cell, always, so the stream's use does not depend on k
                if rng.random() < p:
                    new.append(i)
                    given[pi] += 1
        for i in new:
            a[i] = 1
        return taken, given, got


def isolated_layout(npatch=1, gap=2):
    """Patches of 3x3 cells in a row, `gap` empty columns apart (gap >= 2: no cell of one sees
    a cell of another within distance 2)."""
    return [block(i * (3 + gap), 0) for i in range(npatch)]
