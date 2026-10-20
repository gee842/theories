"""Test bed A: yeast growing cooperatively in sucrose under daily serial dilution (an Allee system).

A stochastic simulation of the two-phase growth model of Dai, Vorselen, Korolev and Gore (Science
2012): slow exponential growth below a density N_c, faster logistic growth above it, for T = 23.5 h
a day, then dilution by a factor DF into fresh medium. The parameters are NOT the paper's table S1
(not available here); they were chosen in this study so that the model reproduces the facts the
paper's main text reports: bistability for dilution factors 500 to 1600 and none at 250, a fold
just above 1600, a per-capita growth rate about 40% higher at intermediate than at low density,
and stable densities of order 1e5 cells/ul. Noise: Poisson sampling of the cells transferred into
a 200 ul culture (volume assumed), and a mean-one lognormal factor on each day's growth (sigma
calibrated so that the stationary coefficient of variation at DF 750 is near the paper's ~0.05).

Units: the level x is the density at the end of a day's growth (cells/ul), as measured in the
paper. A harvester (the part) removes H cells/ul from the grown culture before transfer. So, with
s(y) = G(y / DF) - y the renewal surplus of a culture left at y,

    x_{t+1} = (x_t - H) + s(x_t - H).

The need u is the unstable fixed point (s(u) = 0, s < 0 below it): below u renewal under the
standing dilution fails even once the harvester stops. The margin is m = x - u.

Standard library only.
"""

import math
import random

T = 23.5                      # hours of growth a day
K = 2.0e5                     # carrying capacity, cells/ul
GAMMA_LOW = math.log(350) / T # per hour, below N_C (a day's growth factor 350 at low density)
GAMMA_HIGH = 1.4 * GAMMA_LOW  # per hour, above N_C ("~40% higher")
N_C = 100.0                   # cells/ul
VOLUME = 200.0                # ul per culture (assumed)
SIGMA = 0.05                  # lognormal sd of a day's growth factor (calibrated, see calibrate_yeast)


def grow(n, hours=T, gl=GAMMA_LOW, gh=GAMMA_HIGH, nc=N_C, k=K):
    """Deterministic two-phase growth of an inoculum n (cells/ul) over `hours`."""
    if n <= 0.0:
        return 0.0
    t = hours
    if n < nc:
        tau = math.log(nc / n) / gl
        if tau >= t:
            return n * math.exp(gl * t)
        n, t = nc, t - tau
    return k / (1.0 + (k / n - 1.0) * math.exp(-gh * t))


def surplus(y, df):
    """Renewal surplus of a culture left at y after harvest: next level minus y."""
    return grow(y / df) - y


def fixed_points(df, lo=1.0, hi=4.0e5, steps=20000):
    """Roots of s(y) = 0 on a log grid, refined by bisection: [u, x*] or [] past the fold."""
    roots = []
    a = math.log(lo)
    b = math.log(hi)
    prev_y = lo
    prev = surplus(lo, df)
    for i in range(1, steps + 1):
        y = math.exp(a + (b - a) * i / steps)
        cur = surplus(y, df)
        if prev == 0.0 or prev * cur < 0.0:
            l, r = prev_y, y
            for _ in range(80):
                mid = 0.5 * (l + r)
                if surplus(l, df) * surplus(mid, df) <= 0.0:
                    r = mid
                else:
                    l = mid
            roots.append(0.5 * (l + r))
        prev_y, prev = y, cur
    return roots


def max_surplus(df, lo, hi, steps=4000):
    """Largest renewal surplus over [lo, hi] (the deterministic largest sustained harvest)."""
    best = (-1e18, lo)
    for i in range(steps + 1):
        y = lo + (hi - lo) * i / steps
        s = surplus(y, df)
        if s > best[0]:
            best = (s, y)
    return best


def poisson(rng, mean):
    if mean <= 0.0:
        return 0
    if mean < 30.0:
        limit = math.exp(-mean)
        k, p = 0, 1.0
        while True:
            p *= rng.random()
            if p <= limit:
                return k
            k += 1
    return max(0, int(round(rng.gauss(mean, math.sqrt(mean)))))


class Culture:
    """One replicate population. `memory` adds a lag phase that grows with the number of
    consecutive days the culture has spent near saturation (a hidden state the level does not
    show): lag = LAG_PER_DAY hours per such day, at most LAG_DAYS days counted."""

    LAG_PER_DAY = 1.0
    LAG_DAYS = 4
    SATURATED = 0.7

    def __init__(self, df, x, rng, sigma=SIGMA, memory=False, saturated_days=0):
        self.df = df
        self.x = x
        self.rng = rng
        self.sigma = sigma
        self.memory = memory
        self.saturated_days = saturated_days

    def day(self, harvest=0.0):
        """One cycle: harvest H from the grown culture, transfer 1/DF of it, grow a day.
        Returns the amount actually taken."""
        taken = min(harvest, self.x)
        left = self.x - taken
        cells = poisson(self.rng, VOLUME * left / self.df)
        n = cells / VOLUME
        hours = T
        if self.memory:
            hours = T - self.LAG_PER_DAY * min(self.saturated_days, self.LAG_DAYS)
        g = grow(n, hours)
        if self.sigma > 0.0 and g > 0.0:
            g *= math.exp(self.rng.gauss(0.0, self.sigma) - 0.5 * self.sigma ** 2)
        if self.memory:
            self.saturated_days = self.saturated_days + 1 if g > self.SATURATED * K else 0
        self.x = g
        return taken

    @property
    def extinct(self):
        return self.x <= 0.0


# ---------------------------------------------------------------- interventions (measurement)

def survives(df, x0, seed, harvest_first=0.0, harvest_after=0.0, days=20, memory=False,
             saturated_days=0, need=None):
    """One replicate: an optional one-shot harvest, then `days` cycles of harvest_after.
    Survival means not extinct at the end and, if `need` is given, end level above it."""
    rng = random.Random(seed)
    c = Culture(df, x0, rng, memory=memory, saturated_days=saturated_days)
    c.day(harvest_first)
    for _ in range(days):
        if c.extinct:
            return False
        c.day(harvest_after)
    return (not c.extinct) and (need is None or c.x > need)


def survival_fraction(df, x0, seed0, reps, **kw):
    return sum(survives(df, x0, seed0 + i, **kw) for i in range(reps)) / reps


def pulse_margin(df, x0, seed0, reps=200, tol=0.002, days=20, **kw):
    """The margin by intervention: the largest one-shot harvest from a culture at x0 after which,
    with no further harvest, at least half of the replicates survive `days` cycles (the salt-shock
    experiment of Dai et al., with removal instead of salt). Bisection on H in [0, x0]."""
    lo, hi = 0.0, x0
    if survival_fraction(df, x0, seed0, reps, harvest_first=0.0, days=days, **kw) < 0.5:
        return 0.0
    while hi - lo > tol * x0:
        mid = 0.5 * (lo + hi)
        if survival_fraction(df, x0, seed0, reps, harvest_first=mid, days=days, **kw) >= 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def sustained_yield(df, x0, seed0, reps=200, days=60, tol=0.002, **kw):
    """The largest sustained harvest by intervention: the largest constant H under which, from
    x0, at least half of the replicates survive `days` cycles. Bisection on H in [0, x0]."""
    lo, hi = 0.0, x0
    while hi - lo > tol * x0:
        mid = 0.5 * (lo + hi)
        if survival_fraction(df, x0, seed0, reps, harvest_after=mid, days=days, **kw) >= 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def stationary(df, seed, days=40, burn=10, sigma=SIGMA):
    """Mean and coefficient of variation of the level at the stable state (one replicate per
    seed, ensemble over seeds is the caller's)."""
    roots = fixed_points(df)
    rng = random.Random(seed)
    c = Culture(df, roots[-1], rng, sigma=sigma)
    xs = []
    for t in range(days):
        c.day()
        if t >= burn:
            xs.append(c.x)
    return xs


def break_day(df, x0, harvest, need, seed, days=200, memory=False, saturated_days=0):
    """Days of constant harvest until the harvest first takes the culture below the measured
    need (x_t - H < need), the operational break; None if it never does within `days`."""
    rng = random.Random(seed)
    c = Culture(df, x0, rng, memory=memory, saturated_days=saturated_days)
    for t in range(days):
        if c.x - harvest < need:
            return t
        c.day(harvest)
    return None


def prepare(df, x0, history, seed, memory):
    """A culture brought to level x0 by one of three histories; returns (x0, saturated_days).
    h_long: 10 days at the stable state, then a one-shot removal down to x0.
    h_short: 1 day at the stable state, then the removal.
    h_below: grown up from a low inoculum (never saturated), stopped at x0 by removal on the
    day it first exceeds x0.
    In the scalar model only x0 is carried; with memory the saturated-day count is carried."""
    rng = random.Random(seed)
    roots = fixed_points(df)
    if history in ("h_long", "h_short"):
        c = Culture(df, roots[-1], rng, sigma=SIGMA, memory=memory, saturated_days=0)
        for _ in range(10 if history == "h_long" else 1):
            c.day()
        return x0, c.saturated_days
    c = Culture(df, 1.5 * roots[0], rng, sigma=SIGMA, memory=memory, saturated_days=0)
    for _ in range(60):
        if c.x >= x0 or c.extinct:
            break
        c.day()
    return x0, c.saturated_days
