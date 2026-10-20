#!/usr/bin/env python3
"""Numerical checks of board item RG's statements, run before the proofs (evidence, not proof; the Lean module
Becoming.Regulation proves each statement). usage: python3 -B simulate.py   (prints one line per check, exit 1 on
a failure)

1. Two-sided regulation: random balanced exchanges, opposing on both sides and within the gap to m, bring the level to
   m within its gap and keep it there; within the gap alone, the level never crosses m.
2. Without the bound: the witness (take two at two, give two at nothing, m = 1) alternates for ever.
3. Late reading: under the late return, a course stays within (l + 1) d of its start for random rests moving the level
   by at most d a step; two rests that agree before T and differ over the l + 1 steps after (+d against -d) leave the
   two courses 2 (l + 1) d apart for every rule, here several rules reading l late.
4. The late relay (step M, band [a, b], reading l late, no drift): from every start held below a, the run settles in
   the band exactly where its entry carried l M further is within b, and otherwise leaves both ends without end; the
   start held at a - 1 leaves exactly where b + 2 <= a + (l + 1) M."""
import random
import sys

fails = []


def check(name, ok):
    print(('ok  ' if ok else 'FAIL') + ' ' + name)
    if not ok:
        fails.append(name)


# 1. Two-sided regulation.
rng = random.Random(20261019)
ok_settle = ok_between = True
for _ in range(2000):
    m, x = rng.randint(0, 30), rng.randint(0, 60)
    gap0, xs = abs(x - m), [x]
    for t in range(80):
        g = abs(x - m)
        if x > m:
            net = -rng.randint(1, g)      # takes more than it gives, by at most the excess
        elif x < m:
            net = rng.randint(1, g)       # gives more than it takes, by at most the deficit
        else:
            net = 0
        x += net
        xs.append(x)
    ok_settle &= all(v == m for v in xs[gap0:])
    # within the gap alone (not necessarily opposing): never crosses m
    x = rng.randint(0, 60)
    side = (x > m) - (x < m)
    for t in range(80):
        g = abs(x - m)
        lo, hi = (-g, 0) if x >= m else (0, g)
        x += rng.randint(lo, hi)   # within the gap: net in [-(x - m), 0] above m, [0, m - x] below
        s = (x > m) - (x < m)
        ok_between &= s == 0 or s == side
        if s == 0:
            side = 0
check('two-sided regulation settles at m within the gap', ok_settle)
check('within the gap the level never crosses m', ok_between)

# 2. The overshoot witness.
x, seq = 2, []
for t in range(40):
    seq.append(x)
    x = x - 2 if x == 2 else x + 2
check('the overshoot witness alternates above and below m = 1, never at it',
      all((v > 1) if i % 2 == 0 else (v < 1) for i, v in enumerate(seq)))


# 3. Late reading.
def late_return(l, rec, t):
    if t > l:
        g, k = rec[t - (l + 1)]
        return (k - g if k > g else 0, g - k if g > k else 0)
    return (0, 0)


def course(rule, rec, x0, n):
    xs = [x0]
    for t in range(n):
        give, take = rule(rec, t)
        xs.append(xs[-1] + give + rec[t][0] - take - rec[t][1])
    return xs


ok_keep = True
for _ in range(500):
    l, d = rng.randint(0, 5), rng.randint(1, 4)
    rec = [(rng.randint(0, d), 0) if rng.random() < 0.5 else (0, rng.randint(0, d)) for _ in range(200)]
    xs = course(lambda r, t: late_return(l, r, t), rec, 1000, 200)
    ok_keep &= all(abs(v - 1000) <= (l + 1) * d for v in xs)
check('the late return keeps every course within (l + 1) d of its start', ok_keep)

ok_spread = True
rules = [lambda l: (lambda r, t: late_return(l, r, t)),
         lambda l: (lambda r, t: (2, 0) if t > l and r[t - l - 1][1] > 0 else (0, 0)),
         lambda l: (lambda r, t: (t % 3, (t + l) % 2))]
for mk in rules:
    for l in range(0, 5):
        for d in range(1, 4):
            for T in range(0, 6):
                base = [(rng.randint(0, d), rng.randint(0, d)) for _ in range(T)]
                up = base + [(d, 0)] * (l + 1)
                down = base + [(0, d)] * (l + 1)
                a = course(mk(l), up, 500, T + l + 1)[-1]
                b = course(mk(l), down, 500, T + l + 1)[-1]
                ok_spread &= a - b == 2 * (l + 1) * d
check('two rests agreeing before T leave courses 2 (l + 1) d apart under every rule reading l late', ok_spread)


# 4. The late relay.
def relay_run(x0, a, b, M, l, steps=600):
    xs = [x0] * (l + 1)
    for t in range(steps):
        r = xs[-1 - l]
        xs.append(xs[-1] + (M if r < a else (-M if r > b else 0)))
    return xs


def classify(xs, a, b, tail=300):
    t = xs[-tail:]
    lo, hi = any(v < a for v in t), any(v > b for v in t)
    if lo and hi:
        return 'both'
    if not lo and not hi and len(set(t)) == 1:
        return 'settled'
    return 'other'


ok_relay = ok_threshold = True
for l in range(0, 5):
    for M in range(1, 6):
        for w in range(0, (l + 2) * M + 2):
            a = 10 * (l + 2) * M + 20
            b = a + w
            for x0 in range(a - 3 * M, a):
                k = next(k for k in range(1, 10 * M + 10) if x0 + k * M >= a)
                entry = x0 + k * M
                want = 'settled' if entry + l * M <= b else 'both'
                ok_relay &= classify(relay_run(x0, a, b, M, l), a, b) == want
            leaves = classify(relay_run(a - 1, a, b, M, l), a, b) == 'both'
            ok_threshold &= leaves == (b + 2 <= a + (l + 1) * M)
check('the late relay settles exactly where its entry carried l M further is within b, else leaves both ends', ok_relay)
check('the start held at a - 1 leaves exactly where b + 2 <= a + (l + 1) M', ok_threshold)
sys.exit(1 if fails else 0)
