"""Pareto frontier of talk configurations for "No Safe Way to Win".

Each optional slide has a time cost (seconds, from the script's timing cues) and two
value scores, both the assistant's judgment (0-10):
  F  fidelity: how much of Ren's argument the slide carries (recording + theory documents)
  R  reception: how much it helps a mixed international room understand and accept the
     argument, net of the risk of being misread (as allegiance, essentialism, naivety, fate)
Required slides are always in. Constraints encode coherence. Values are additive except
for a diminishing-returns factor inside each part of the talk (the second and later slides
of a part count 0.85, then 0.7 ...), so a talk that covers every part beats one that piles
slides into one part.
"""
import itertools, json

REQUIRED = {  # id: seconds
    'cover': 20, 'loop': 50, 'hinge': 40, 'nosafe': 30, 'order': 45, 'close': 50}
OPTIONAL = {  # id: (seconds, F, R, part)
    'film':       (105, 5, 8, 'open'),
    'agenda':     (35, 1, 3, 'open'),
    'minds':      (55, 9, 6, 'game'),
    'boundary':   (50, 9, 7, 'game'),
    'kernel':     (45, 8, 7, 'game'),
    'endgames':   (50, 6, 6, 'game'),
    'training':   (45, 7, 8, 'hinge'),
    'scales':     (55, 8, 9, 'hinge'),
    'brakes':     (40, 7, 7, 'hinge'),
    'frame':      (45, 7, 6, 'frame'),
    'mirror':     (45, 7, 9, 'frame'),
    'dilemma':    (50, 8, 8, 'frame'),
    'relational': (40, 8, 6, 'see'),
    'regulator':  (50, 6, 4, 'see'),
    'direction':  (40, 7, 7, 'see'),
    'trust':      (50, 7, 9, 'follows'),
}
BASE_T = sum(REQUIRED.values())

def ok(s):
    if 'regulator' in s and 'relational' not in s: return False      # builds on it
    if not ({'frame', 'mirror', 'dilemma'} & s): return False        # the mixed room needs part 3
    if not ({'relational', 'direction'} & s): return False           # the affirmative alternative
    if not ({'minds', 'boundary', 'kernel'} & s): return False       # the mechanism needs its core
    return True

def value(s, k):
    idx = 1 if k == 'F' else 2
    by_part = {}
    for x in s:
        by_part.setdefault(OPTIONAL[x][3], []).append(OPTIONAL[x][idx])
    tot = 0.0
    for vals in by_part.values():
        for i, v in enumerate(sorted(vals, reverse=True)):
            tot += v * (0.85 ** i)
    return tot

configs = []
ids = list(OPTIONAL)
for r in range(len(ids) + 1):
    for combo in itertools.combinations(ids, r):
        s = set(combo)
        if not ok(s): continue
        T = BASE_T + sum(OPTIONAL[x][0] for x in s)
        configs.append((T, round(value(s, 'F'), 2), round(value(s, 'R'), 2), tuple(sorted(s, key=ids.index))))

# Pareto: minimise T, maximise F and R
configs.sort()
front = []
for c in configs:
    T, F, R, s = c
    dominated = any(T2 <= T and F2 >= F and R2 >= R and (T2, F2, R2) != (T, F, R) for T2, F2, R2, _ in front)
    if not dominated:
        front = [f for f in front if not (T <= f[0] and F >= f[1] and R >= f[2] and (T, F, R) != f[:3])]
        front.append(c)
print(f'{len(configs)} coherent configurations; {len(front)} on the Pareto frontier (min time, max F, max R)')

# For each time budget, the best configuration by a single score that weights the two values
# (W_R for a mixed international room), among frontier points that fit the budget.
W_F, W_R = 0.45, 0.55
def score(c): return W_F * c[1] + W_R * c[2]
rows = []
for minutes in [8, 10, 12, 14, 15, 16, 17, 18, 20]:
    fit = [c for c in front if c[0] <= minutes * 60]
    if not fit: continue
    best = max(fit, key=score)
    rows.append((minutes, best))
fmax = max(c[1] for c in front); rmax = max(c[2] for c in front)
for minutes, (T, F, R, s) in rows:
    cut = [x for x in ids if x not in s]
    print(f'<= {minutes:>2} min | uses {T/60:4.1f} min | F {F:5.1f} ({F/fmax:4.0%}) | R {R:5.1f} ({R/rmax:4.0%}) | cut: {", ".join(cut) or "none"}')

# marginal value per minute of each optional slide, from the full configuration
full = set(ids)
print('\nmarginal value per minute, removing one slide from the full talk:')
for x in ids:
    s = full - {x}
    if not ok(s): print(f'  {x:<11} (required by a constraint once others are in)'); continue
    dF = value(full, 'F') - value(s, 'F'); dR = value(full, 'R') - value(s, 'R')
    m = OPTIONAL[x][0] / 60
    print(f'  {x:<11} {OPTIONAL[x][0]:>4}s  dF/min {dF/m:5.2f}  dR/min {dR/m:5.2f}  weighted/min {(W_F*dF+W_R*dR)/m:5.2f}')


# ---- With the film fixed in (Ren chose a short excerpt), and a robustness check ----
import random
def best_for(budget_s, scores, wR, force=('film',)):
    best=None
    for T,F,R,s in configs:
        if any(f not in s for f in force): continue
        if T > budget_s: continue
        sv={x:scores[x] for x in s}
        def val(k):
            by={}
            for x in s: by.setdefault(OPTIONAL[x][3],[]).append(sv[x][0 if k=='F' else 1])
            return sum(v*(0.85**i) for vals in by.values() for i,v in enumerate(sorted(vals,reverse=True)))
        sc=(1-wR)*val('F')+wR*val('R')
        if best is None or sc>best[0]: best=(sc,T,s)
    return best
base={x:(OPTIONAL[x][1],OPTIONAL[x][2]) for x in ids}
print('\nWith the film fixed in, at the base scores (W_R = 0.55):')
for m in [12,14,15,16,17,18]:
    sc,T,s=best_for(m*60, base, W_R)
    print(f'  <= {m} min | uses {T/60:4.1f} | cut: {", ".join(x for x in ids if x not in s) or "none"}')
rng=random.Random(20261004)
N=300
for m in [15,16,17]:
    counts={x:0 for x in ids}
    for _ in range(N):
        sc_={x:(max(0,min(10,base[x][0]+rng.uniform(-1.5,1.5))), max(0,min(10,base[x][1]+rng.uniform(-1.5,1.5)))) for x in ids}
        wR=rng.uniform(0.4,0.7)
        _,T,s=best_for(m*60, sc_, wR)
        for x in s: counts[x]+=1
    print(f'\nRobustness at <= {m} min (film fixed; scores ±1.5, W_R 0.40–0.70; {N} draws): share of draws that keep each slide')
    print('  ' + '  '.join(f'{x} {counts[x]/N:.0%}' for x in ids if x!='film'))
