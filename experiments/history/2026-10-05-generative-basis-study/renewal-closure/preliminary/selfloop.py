"""Bounded-horizon check: one constraint kind that depends on itself and opens a channel.

Conventions (to be fixed exactly in Phase 0 of RENEWAL-CLOSURE-ROADMAP.md):
- a token is alive for l consecutive ticks, its birth tick included;
- at tick t every live token brings a units of arrival;
- R(t+1) + m * births(t+1) <= R(t) + a * alive(t);
- a birth at t+1 needs a token born earlier and still alive at t+1.
The search explores every strategy with 0..2 births per tick.  Reserve is capped
to keep the search finite; an "ends" verdict is reported as reliable only if the
cap was never reached.  A finite horizon cannot certify endless renewal.
"""

def search(a, l, m, R0, H=60, cap=60):
    frontier = {((0,), R0)}           # ages of live tokens, reserve
    cap_hit = False
    for _ in range(H):
        nxt = set()
        for ages, R in frontier:
            avail = R + a * len(ages)
            older = [x + 1 for x in ages if x + 1 < l]
            if not older:
                continue              # no parent alive at the next tick
            for b in range(3):
                if b * m <= avail:
                    left = avail - b * m
                    cap_hit |= left > cap
                    nxt.add((tuple(sorted(older + [0] * b)), min(cap, left)))
        frontier = nxt
        if not frontier:
            return False, cap_hit
    return True, cap_hit

if __name__ == "__main__":
    for a, l, m in [(1, 3, 5), (1, 3, 4), (1, 3, 3), (1, 3, 2), (2, 3, 7), (2, 3, 6),
                    (1, 1, 1), (1, 1, 2), (3, 2, 7), (3, 2, 6)]:
        rel = '>' if a * l > m else '=' if a * l == m else '<'
        out = {R0: search(a, l, m, R0) for R0 in (0, a, m, 3 * m)}
        print(f"a={a} l={l} m={m}  a*l {rel} m  (persists_within_horizon, cap_hit) by R0: {out}")
