"""Bounded-horizon check: kinds P and Q that depend on each other (P -> Q, Q -> P).

Only Q opens a channel (arrival aQ per live Q-token per tick); P brings nothing.
Same conventions as selfloop.py; 0..2 births per kind per tick.  The target
theorem predicts: renewal iff aQ*lQ > mQ (excess channel reachable from the
cycle).  aQ*lQ = mQ is not enough here, because P is on the cycle and is not
balanced.  A finite horizon cannot certify endless renewal.
"""

def search(aQ, lP, mP, lQ, mQ, R0, H=70, cap=80):
    frontier = {((0,), (0,), R0)}
    cap_hit = False
    for _ in range(H):
        nxt = set()
        for P, Q, R in frontier:
            avail = R + aQ * len(Q)
            P1 = [x + 1 for x in P if x + 1 < lP]
            Q1 = [x + 1 for x in Q if x + 1 < lQ]
            for bp in range(3):
                for bq in range(3):
                    if bp and not Q1:
                        continue      # a P birth needs a live, older Q
                    if bq and not P1:
                        continue      # a Q birth needs a live, older P
                    d = bp * mP + bq * mQ
                    if d <= avail:
                        nP = tuple(sorted(P1 + [0] * bp))
                        nQ = tuple(sorted(Q1 + [0] * bq))
                        if nP or nQ:
                            cap_hit |= avail - d > cap
                            nxt.add((nP, nQ, min(cap, avail - d)))
        frontier = nxt
        if not frontier:
            return False, cap_hit
    return True, cap_hit

if __name__ == "__main__":
    for c in [(1, 3, 1, 3, 2), (1, 3, 1, 3, 3), (1, 3, 1, 3, 4), (2, 3, 1, 3, 5),
              (2, 3, 1, 3, 6), (1, 2, 1, 4, 3), (1, 2, 1, 4, 4)]:
        aQ, lP, mP, lQ, mQ = c
        rel = '>' if aQ * lQ > mQ else '=' if aQ * lQ == mQ else '<'
        print(c, f"aQ*lQ {rel} mQ", {R0: search(*c, R0) for R0 in (0, 5, 20)}, flush=True)
    # The balanced-but-insufficient cases need a longer horizon before they end.
    for c in [(1, 3, 1, 3, 3), (2, 3, 1, 3, 6)]:
        print(c, "R0=20, H=180:", search(*c, 20, H=180, cap=40), flush=True)
