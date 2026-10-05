"""Exact public game of constructed fallback, operating cash, and strategic interference.

No floating point is used for decisions. Run study.py for the frozen enumeration.
"""

from dataclasses import dataclass, replace
from fractions import Fraction as Q
from functools import lru_cache


@dataclass(frozen=True)
class Model:
    T: int = 2
    b: int = 5
    x: int = 2
    o: int = 4
    o0: int = 0
    ell: int = 2
    m: int = 1
    K: int = 1
    c: Q = Q(1)
    r: Q = Q(4)
    chi: Q = Q(3, 2)
    discount: Q = Q(1)
    handoff_at: tuple = ()  # zero-based periods
    J: int = 0
    successor_at: int = -1
    successor_chi: Q = Q(3, 2)


@dataclass(frozen=True)
class Result:
    vp: Q
    vo: Q
    path: tuple


def choices(p, t, cash, owned):
    """Every bill includes subsistence, due before this period's income."""
    raw = []
    if owned and t in p.handoff_at:
        raw += [("lapse", p.ell, False, False),
                ("transfer_dormant", p.ell + p.J, True, False),
                ("transfer_active", p.ell + p.J + p.m, True, True),
                ("rebuild_dormant", p.ell + p.K, True, False),
                ("rebuild_active", p.ell + p.K + p.m, True, True)]
    else:
        raw.append(("idle", p.ell, owned, False))
        if owned:
            raw.append(("activate", p.ell + p.m, True, True))
        else:
            raw += [("build_dormant", p.ell + p.K, True, False),
                    ("build_active", p.ell + p.K + p.m, True, True)]
    # Lower immediate expenditure breaks participant ties; retain access on exact cost ties.
    return sorted((a for a in raw if a[1] <= cash), key=lambda a: (a[1], not a[2], a[0]))


def operator_moves(p, t, active, reverse_ties=False):
    chi = p.successor_chi if p.successor_at >= 0 and t >= p.successor_at else p.chi
    moves = [("harm", Q(0), False), ("safeguard", p.c, False)]
    if active:
        moves.insert(1, ("block", chi, True))
    if reverse_ties:
        moves.reverse()
    return moves


class Game:
    def __init__(self, p, persistent=False, participant="optimal", reverse_ties=False):
        self.p = p
        self.persistent = persistent
        self.participant = participant
        self.reverse_ties = reverse_ties
        self.solve = lru_cache(None)(self._solve)
        self.visited = 0

    def _solve(self, t, cash, owned=False):
        p = self.p
        self.visited += 1
        if t == p.T:
            return Result(Q(0), Q(0), ())
        available = choices(p, t, cash, owned)
        # With x >= ell every on-path inactive baseline can pay the next period.
        if not available:
            raise ValueError(f"No affordable subsistence at {(t, cash, owned)}")
        if self.participant == "never":
            available = [a for a in available if a[0] in ("idle", "lapse")]
        if self.participant == "always":
            active = [a for a in available if a[3]]
            available = [active[0] if active else available[0]]
        candidates = []
        for action in available:
            name, bill, next_owned, active = action
            alternatives = []
            for op, op_cost, blocked in operator_moves(p, t, active, self.reverse_ties):
                allocations = []
                for participates in (True, False):
                    income = (p.b if op == "safeguard" else p.x) if participates else (p.o if active and not blocked else p.o0)
                    next_cash = cash - bill + income
                    # An allocation that cannot fund the next subsistence bill ends
                    # modeled operation. Under the core parameters it is dominated.
                    if t + 1 < p.T and next_cash < p.ell:
                        # Current model restricts to x>=ell and nonnegative costs; choosing
                        # o0 can voluntarily end operation. Its future receipts are zero,
                        # with no fictional later subsistence consumption.
                        future = Result(Q(0), Q(0), ())
                        terminated = True
                    else:
                        future = self.solve(t + 1, next_cash, next_owned)
                        terminated = False
                    current_p = Q(income - bill)
                    current_o = (p.r if participates else Q(0)) - op_cost
                    vp = current_p + p.discount * future.vp
                    vo = current_o + p.discount * future.vo
                    score = vp if self.participant == "optimal" else current_p
                    row = {
                        "period": t + 1, "cash_before": cash, "owned_before": owned,
                        "participant_action": name, "bill": bill, "active": active,
                        "operator_action": op, "operator_cost": str(op_cost),
                        "participates": participates, "income": income,
                        "cash_after": next_cash, "owned_after": next_owned,
                        "terminated": terminated,
                    }
                    allocations.append((score, Result(vp, vo, (row,) + future.path), current_o, current_p))
                selected = max(allocations, key=lambda z: z[0])
                op_score = selected[1].vo if self.persistent else selected[2]
                alternatives.append((op_score, selected[1], selected[3]))
            selected = max(alternatives, key=lambda z: z[0])
            participant_score = selected[1].vp if self.participant != "myopic" else selected[2]
            candidates.append((participant_score, selected[1]))
        return max(candidates, key=lambda z: z[0])[1]


def trace_summary(result, initial_cash):
    path = result.path
    return {
        "participant_value": str(result.vp), "operator_value": str(result.vo),
        "final_cash": path[-1]["cash_after"] if path else initial_cash,
        "active_periods": sum(z["active"] for z in path),
        "safeguarded_participations": sum(z["participates"] and z["operator_action"] == "safeguard" for z in path),
        "harmful_participations": sum(z["participates"] and z["operator_action"] != "safeguard" for z in path),
        "independent_exits": sum(not z["participates"] for z in path),
        "blockades": sum(z["operator_action"] == "block" for z in path),
        "construction_events": sum(z["participant_action"].startswith(("build", "rebuild")) for z in path),
        "path": list(path),
    }


def static_outcomes(p, active=True):
    """All pure SPNE outcomes in the single-period game, including off-path ties."""
    from itertools import product
    moves = operator_moves(p, 0, active)
    responses = []
    for op, cost, blocked in moves:
        income_in = p.b if op == "safeguard" else p.x
        income_out = p.o if active and not blocked else p.o0
        best = max(income_in, income_out)
        responses.append([(accept, income, (p.r if accept else Q(0)) - cost)
                          for accept, income in [(True, income_in), (False, income_out)] if income == best])
    found = set()
    for profile in product(*responses):
        value = max(response[2] for response in profile)
        for move, response in zip(moves, profile):
            if response[2] == value:
                found.add((move[0], response[0], response[1], str(response[2])))
    return sorted(found)
