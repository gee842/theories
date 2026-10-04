"""m10  The scissors in reduced form, and Test G (Section 5.5; Remark S5.1; keys `zonesillus`, `enforce`, `standprice`).

Claims under test (memo item 13):
  (A) Reduced form (binary faithful-AI game of Prop 6.1, n=4, b=1, c=.3, d=.2, eps=1, delta=.9, D=C in objective units,
      actors acting on theta from the standing price; RIVALS NOT RESPONDING): the largest enforceable discounted loop gain
      is .92 at p_d=0 and .39 at p_d=.9; none exists above p_d ~ .95 (theta0=0) and ~ .98 (theta0=.4), not .99.
      Computed by direct valuation of cooperation and deviation paths and bisection on Gd (no threshold formula).
  (B) With a common return (prize growing with capacity), the narrowing arm weakens: the same computation with
      theta from (1+theta)/(n-1-theta) = (1+theta0)/(n-1-theta0) (1-Grel_d)/(1-Gcom_d).
  (C) Test G: the restraint gap between wider and narrower objectives rises with p_d when a decisive position is worth
      no more than cooperation (D=C); when it is worth more (D>C) the gap is hump-shaped and closes as p_d -> 1.
Standard library only.
"""
n, b, c, dd, eps, delta = 4, 1.0, 0.3, 0.2, 1.0, 0.9
A = eps * (b - dd) - c; B = eps * (b / (n - 1) + dd); K = c + n * eps * dd

def sustained(theta, pd, D=0.0):
    # objective units: cooperation 0 per period; deviation: stage gain A - theta B, then w.p. pd a decisive position worth
    # D per period, else reversion to all racing worth -K(1+theta) per period (direct valuation of the two paths)
    coop = 0.0
    dev = (A - theta * B) + delta * (pd * D + (1 - pd) * (-K * (1 + theta))) / (1 - delta)
    return dev <= coop + 1e-12

def theta_of(theta0, Grel, Gcom=0.0):
    rho = (1 + theta0) / (n - 1 - theta0) * (1 - Grel) / (1 - Gcom)
    return (rho * (n - 1) - 1) / (1 + rho)

def largest_G(theta0, pd, Gcom=0.0):
    if not sustained(theta_of(theta0, 0.0, Gcom), pd): return None
    lo, hi = 0.0, 0.999999
    if sustained(theta_of(theta0, hi, Gcom), pd): return hi
    for _ in range(80):
        mid = (lo + hi) / 2
        if sustained(theta_of(theta0, mid, Gcom), pd): lo = mid
        else: hi = mid
    return lo

def check_A_B():
    print("(A) largest enforceable discounted relative loop gain, by p_d (D=C)")
    for th0 in (0.0, 0.4):
        row = []
        for pd in (0.0, 0.5, 0.9, 0.94, 0.95, 0.97, 0.98, 0.99):
            G = largest_G(th0, pd)
            row.append(f"p_d={pd}: {'none' if G is None else f'{G:.3f}'}")
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if largest_G(th0, mid) is not None: lo = mid
            else: hi = mid
        print(f"   theta0={th0}: " + "; ".join(row) + f"  | none above p_d = {lo:.4f}")
    print("(B) with a common return Gcom_d (prize growing with capacity), theta0=0")
    for Gc in (0.0, 0.3, 0.6):
        row = []
        for pd in (0.0, 0.5, 0.9):
            G = largest_G(0.0, pd, Gc)
            row.append(f"p_d={pd}: {'none' if G is None else ('any' if G > 0.9999 else f'{G:.3f}')}")
        print(f"   Gcom_d={Gc}: " + "; ".join(row))

def check_C():
    print("(C) Test G: share of theta ~ U[-1,3] sustaining restraint; wider (theta>1) minus narrower (theta<1)")
    for D in (0.0, 0.5):
        row = []
        for pd in (0.0, 0.5, 0.8, 0.9, 0.95, 0.99, 1.0):
            thetas = [-1 + 4 * (k + 0.5) / 4000 for k in range(4000)]
            wide = [t for t in thetas if t > 1]; narrow = [t for t in thetas if t < 1]
            fw = sum(sustained(t, pd, D) for t in wide) / len(wide); fn = sum(sustained(t, pd, D) for t in narrow) / len(narrow)
            row.append(f"{pd}: {fw-fn:+.2f}")
        print(f"   D-C={D}: gap by p_d  " + "; ".join(row))
    print("   D=C: the gap rises with p_d; D>C: it rises, then closes as p_d -> 1 (no objective with theta<=n-1 sustains restraint),")
    print("   where this theory and structural realism agree: the test discriminates at intermediate p_d")

if __name__ == '__main__':
    print(__doc__.split('\n')[0]); print()
    check_A_B(); print(); check_C()
