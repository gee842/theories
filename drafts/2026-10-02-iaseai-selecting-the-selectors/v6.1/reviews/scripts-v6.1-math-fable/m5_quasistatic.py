"""m5 (repaired integrator): attack 3, the quasi-static assumption of Assumption 4.2.

Joint dynamics, one dominant carrier (p=1, chi=1, Yhat=1, f=0), captured source domain feeding evaluation:
  capacity under selection with multiplicative variance:  dq/dt = s_q q^2 dDeltaPi/dq,  dDeltaPi/dq = 1/d(t) - gam(t) q^eta
  rule support in evaluation:                              dz/dt = eps (A + aB q - d(t) z)     [exact exponential update]
  share of evaluation following the practice:              d logit x/dt = zeta (a z - c)         [exact in logit]
  gam = e^{-g t}, d = d0 e^{alpha t}. Quasi-static q*(t) = (1/(gam d))^(1/eta); certificate G_qs = (A + aB q*)/(c d).
The actual growth condition of x is a z > c, reported as 'actual certificate fails' when it first holds.
Rate law: alpha >= g/(1+eta) keeps the certificate iff it holds at t=0; alpha < g/(1+eta) fails after a finite time.
"""
import math

def run(alpha, s_q, eta=1.0, g=0.2, d0=2.0, A=0.3, aB=1.0, c=1.0, eps=1.0, zeta=1.0, a=1.0, x0=0.01, T=250.0, dt=0.01):
    q = (1/(1.0*d0))**(1/eta)            # start at the quasi-static level at t=0
    z = A/d0; ux = math.log(x0/(1-x0)); t = 0.0
    fail_qs = None; fail_act = None; tcap = None; minratio = 1e9; maxratio = 0.0
    while t < T:
        gam = math.exp(-g*t); d = d0*math.exp(alpha*t)
        qs = (1/(gam*d))**(1/eta)
        if fail_qs is None and (A + aB*qs)/(c*d) > 1: fail_qs = t
        if fail_act is None and a*z > c: fail_act = t
        if tcap is None and ux > 0: tcap = t
        r = q/qs; minratio = min(minratio, r); maxratio = max(maxratio, r)
        # q: adaptive substeps in log space, rate scale k = s_q*eta*q*/d (linearized relaxation rate at q*)
        k = s_q*eta*qs/d
        nsub = max(1, int(k*dt/0.05) + 1)
        if nsub > 2000:   # fully relaxed within the step
            q = qs
        else:
            h = dt/nsub
            for _ in range(nsub):
                u = math.log(q)
                du = s_q*q*(1/d - gam*q**eta)      # d ln q / dt
                u += h*du
                q = math.exp(min(u, 700.0))
        # z exact for constant inputs over the step
        E = math.exp(-eps*d*dt)
        z = z*E + (A + aB*q)/d*(1-E)
        ux += dt*zeta*(a*z - c)
        t += dt
    return fail_qs, fail_act, tcap, minratio, maxratio

if __name__ == '__main__':
    fmt = lambda v: ('%.1f' % v) if v is not None else 'never (T=250)'
    for eta in (1.0, 2.0):
        thr = 0.2/(1+eta)
        print(f"eta={eta}: rate-law threshold alpha_cor = g/(1+eta) = {thr:.4f}")
        for alpha in (thr-0.01, thr+0.01):
            print(f"  alpha_cor={alpha:.4f} ({'below' if alpha < thr else 'above'} threshold)")
            for s_q in (100.0, 1.0, 0.1, 0.01):
                fq, fa, tc, mn, mx = run(alpha, s_q, eta=eta)
                print(f"     selection speed s_q={s_q:>6}: quasi-static certificate fails at t={fmt(fq)}; actual (a z > c) at t={fmt(fa)}; "
                      f"evaluation captured (x>1/2) at t={fmt(tc)}; q/q* in [{mn:.3f}, {mx:.3f}]")
    print("Reading: with fast selection on capacity the joint dynamics reproduce the rate law: the certificate fails when the quasi-static")
    print("one does, and the seeded evaluation domain is captured shortly after; above the threshold nothing is captured. With slow")
    print("selection q lags q*, the failure is delayed and within the horizon may not occur, although the rate law says it does. The")
    print("threshold rate is not moved, but the failure TIME and so the finite-horizon necessity of R3a depend on how fast selection")
    print("tracks q*. Quasi-static capacity is the worst case for the certificate when q starts at or below q*.")
