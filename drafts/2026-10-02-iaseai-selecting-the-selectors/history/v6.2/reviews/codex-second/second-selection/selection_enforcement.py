"""Independent second review: exact clock counterexample and local algebra.

Standard library only. Does not import the manuscript's check implementation.
"""
from fractions import Fraction as F
from math import exp


def delayed_detection():
    # t=0 deviation yields C+g. Pending dates yield C. With probability
    # 1-p it is detected/answered at t=9; otherwise decisive at t=10.
    # Eventual absorbing per-period payoffs are v and D, respectively.
    C, D, v, g, delta, p = F(1), F(3, 2), F(0), F(3, 10), F(9, 10), F(16, 25)
    printed = (1-delta)*g + delta*(p*(D-C)+(1-p)*(v-C))
    actual = (1-delta)*g + p*delta**10*(D-C) + (1-p)*delta**9*(v-C)
    printed_bound = ((C-v)-(1-delta)*g/delta)/(D-v)
    actual_bound = (delta**9*(C-v)-(1-delta)*g)/(delta**10*(D-C)+delta**9*(C-v))
    assert printed == F(-3, 500)
    assert actual == F(263215599, 125000000000)
    assert actual_bound < p < printed_bound
    print('delayed_detection', dict(printed=float(printed), actual=float(actual),
        printed_bound=float(printed_bound), actual_bound=float(actual_bound)))


def old_floor_counterexample_is_now_in_repaired_branch():
    # V6.1 falling-floor counterexample: alpha_cor=.05 > alpha_f=.01.
    # The revised floor branch predicts cultivation ends, correctly.
    rows = []
    for t in (0., .25, .5, 1., 10., 100.):
        d = 2*exp(.05*t)
        q = max(0., .5*exp(-.05*t)-.49*exp(-.01*t))*exp(.2*t)
        rows.append(q/d)
    assert all(0 <= x < 1 for x in rows)
    assert rows[-3:] == [0., 0., 0.]
    print('repaired_falling_floor', rows)


def cheap_talk_ideal_gap():
    # Direct quadratic derivative solutions, including common third-party slope.
    for n in (2, 3, 4, 6):
        for theta in (F(-1), F(0), F(1, 2), F(n-1)):
            if n-1+theta <= 0:
                continue
            b, L = F(1, 20), F(7, 3)
            sender = (2*b*(n-1)+theta*L)/(2*(n-1+theta))
            receiver = (2*theta*b+theta*L)/(2*(n-1+theta))
            assert sender-receiver == b*(n-1-theta)/(n-1+theta)
    print('cheap_talk_ideal_gap', 'exact identity confirmed')


if __name__ == '__main__':
    delayed_detection()
    old_floor_counterexample_is_now_in_repaired_branch()
    cheap_talk_ideal_gap()
