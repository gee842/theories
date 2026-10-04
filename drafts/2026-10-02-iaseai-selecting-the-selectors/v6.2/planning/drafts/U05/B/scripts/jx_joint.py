"""JX (draft, unit U05/B): the scissors in one reduced joint model, and the detect link.

Setup (D1-opus section 2.3): one ratio channel (capacity) with stakes Omega_t = Omega_0 e^{g_Om t} growing
exogenously and provision k_0(t) = k_0 e^{g_k t}; quasi-static capacity, rivals not responding.
  won share       omega(t) = (kappa Omega_t/n) / (kappa Omega_t/n + k_0(t))
  structural gain Gamma(t) = (1-beta) r omega d_K/(d_K+delta_f)            (eq. (2))
  discounted gain Gamma_d(t) = (1-beta) r omega delta d_K/(1-delta(1-d_K-delta_f))  (Prop 2.2(3))
  gap multiplier  Lambda*(t) = 1+(d_K+delta_f)(Gamma-1)                      (Remark S2.1)
  T_dec(t) = ln(Delta_bar/eps_0)/ln Lambda*  when Lambda*>1, else infinite
  detection-and-response as a Poisson clock of mean tau_det:  upsilon(T) = 1-exp(-T/tau_det),
  so p_d(t) = 1-upsilon(T_dec) = exp(-T_dec/tau_det)                           (detectlink)
  working objective theta(t) = theta_Gamma(theta_0, Gamma_d(t)), eq. (9) with zero common return
  stage game of Remark S5.1 at D=C: restraint sustainable iff theta >= theta_rep(p_d), i.e.
  p_d <= pbar(theta) = 1-(1-delta)(A-theta B)/(delta K (1+theta)), A=eps(b-d)-c, B=eps(b/(n-1)+d), K=c+n eps d.
Variant (a): stage payoffs fixed (the objective arm alone). Variant (b): b,d scale with Omega_t/Omega_0, c fixed.
Pure Python, standard library.
"""
import math

def theta_gamma(theta0, Gd, n):
    return (n*theta0-(n-1)*(1+theta0)*Gd)/(n-(1+theta0)*Gd)

def pbar(theta, b, c, d, eps, n, delta):
    A = eps*(b-d)-c; B = eps*(b/(n-1)+d); K = c+n*eps*d
    return 1-(1-delta)*(A-theta*B)/(delta*K*(1+theta))

def theta_rep(pd, b, c, d, eps, n, delta):
    A = eps*(b-d)-c; B = eps*(b/(n-1)+d); K = c+n*eps*d
    Lp = delta*(1-pd)/(1-delta)
    return (A-Lp*K)/(B+Lp*K)

def run(n=4, r=1.5, beta=0.0, kappa=1.0, dK=0.5, df=0.0, delta=0.8, Omega0=1.0, k0=1.0,
        g_Om=0.05, g_k=0.0, eps0=0.01, Dbar=0.5, tau_det=12.0, theta0=0.0,
        b=1.0, c=0.3, d=0.2, eps=1.0, scale_stage=False, T=200, every=20, label=''):
    print(f'--- {label}: n={n} r={r} beta={beta} d_K={dK} delta_f={df} delta={delta} Omega0={Omega0} k0={k0} '
          f'g_Om={g_Om} g_k={g_k} eps0={eps0} Dbar={Dbar} tau_det={tau_det} theta0={theta0} '
          f'stage b={b} c={c} d={d} eps={eps} scale_stage={scale_stage}')
    print('   t   omega  Gamma  Gamma_d  Lambda*   T_dec     p_d   theta   pbar_d  gap')
    tstar = None; prev = None
    for t in range(T+1):
        Om = Omega0*math.exp(g_Om*t); k = k0*math.exp(g_k*t)
        w = (kappa*Om/n)/(kappa*Om/n+k)
        G = (1-beta)*r*w*dK/(dK+df)
        Gd = (1-beta)*r*w*delta*dK/(1-delta*(1-dK-df))
        Lam = 1+(dK+df)*(G-1)
        Tdec = math.log(Dbar/eps0)/math.log(Lam) if Lam > 1 else float('inf')
        pd = math.exp(-Tdec/tau_det) if Tdec < float('inf') else 0.0
        th = theta_gamma(theta0, Gd, n) if Gd < 1 else float('nan')
        s = Om/Omega0 if scale_stage else 1.0
        pb = pbar(th, b*s, c, d*s, eps, n, delta) if Gd < 1 else float('nan')
        gap = pb-pd
        if prev is not None and prev > 0 and gap <= 0 and tstar is None:
            tstar = t
        prev = gap
        if t % every == 0 or (tstar == t):
            print(f'{t:4d}  {w:6.3f} {G:6.3f} {Gd:7.3f} {Lam:7.4f} {Tdec:8.2f} {pd:7.4f} {th:7.3f} {pb:8.4f} {gap:+.3f}'
                  + ('   <- blades meet' if tstar == t else ''))
    if tstar is None:
        print('   blades do not meet within the horizon')
    else:
        print(f'   first t with p_d >= pbar_d: t* = {tstar}')
    return tstar

print('JX (draft U05/B)  The scissors in one reduced joint model.')
print('(A) stakes outgrow provision (g_Om > g_k): omega rises, Gamma and p_d rise, theta narrows and pbar_d falls')
tA = run(label='A: stage fixed')
print()
print('(A2) same, stage payoffs b,d scaling with the stakes (D=C), c fixed')
tA2 = run(label='A2: stage scales', scale_stage=True)
print()
print('(B) provision grows with the stakes (g_k = g_Om): neither blade moves')
run(label='B: g_k = g_Om', g_k=0.05, T=100, every=25)
print()
print('(C) detection twice as fast (tau_det = 6): the crossing is later')
tC = run(label='C: tau_det=6', tau_det=6.0, T=300, every=50)
print()
print('(D) a wider held self-model (theta_0 = 0.4): the crossing is later')
tD = run(label='D: theta0=0.4', theta0=0.4, T=300, every=50)
print()
print('(E) detect link: (14) with p_d = 1 - upsilon reads upsilon >= 1 - pbar_d; and the one-shot threshold of Prop 8.10')
for (g, C, D, v, delta) in [(2.0, 1.0, 4.0, 0.0, 0.9), (1.0, 3.0, 6.0, 1.0, 0.9), (0.5, 1.0, 0.9, 0.0, 0.9)]:
    pb = 1-((1-delta)*g+delta*(D-C))/(delta*(D-v))
    # one-shot payoffs: R = C; T = normalized value of an undetected deviation; P-F = of a detected one
    R = C; Tt = (1-delta)*(C+g)+delta*D; PF = (1-delta)*(C+g)+delta*v
    ups_810 = (Tt-R)/(Tt-PF)
    print(f'   g={g} C={C} D={D} v={v} delta={delta}: 1-pbar_d = {1-pb:.4f}; (T-R)/(T-(P-F)) = {ups_810:.4f}; '
          f'T<R (cooperation without verification) = {Tt < R}; pbar_d>=1 (R4 exception) = {pb >= 1}')
