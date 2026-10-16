"""m6: smaller items.
(1) Lemma 3.3(3): 'both compliance and evasion are stable' needs s(0) > c > s(1); a falling sanction that stays above c
    gives global compliance, one that starts below c gives global evasion.
(2) Prop 5.4: a single p_d for 'a deviation'. If different deviations carry different (g, p_d), the max-g deviation
    need not be the binding one.
(3) Remark S2.1: the per-period multiplier with diffusion is 1 + (d_K + delta_f)(Gamma - 1), not 1 + d_K(Gamma - 1).
(4) Theorem 5.12: (variety grows) is not used in the proof: a bound that uses only (coverage lags) and (residual floor).
(5) Prop 5.4(5): 'each breaks out with probability q' with 'neither with 1-2q' needs q <= 1/2 and excludes simultaneous breakouts.
"""
import math

def replicator(p, pi, dt=0.01, T=3000.0):
    for _ in range(int(T/dt)):
        f = pi(p); pb = sum(a*b for a, b in zip(p, f))
        p = [a + dt*a*(b-pb) for a, b in zip(p, f)]; s = sum(p); p = [a/s for a in p]
    return p

print("(1) Lemma 3.3(3): compliers pay c=0.3; evaders face s(x) = q0 (1 - x) F, falling with the evader share x")
for q0, F in [(0.8, 0.6), (2.0, 0.6), (0.4, 0.6)]:
    outs = []
    for x0 in (0.05, 0.5, 0.95):
        p = replicator([1-x0, x0], lambda p: [-0.3, -q0*p[0]*F])
        outs.append(f"x0={x0}: x_T={p[1]:.3f}")
    print(f"   q0 F = {q0*F:.2f} (s(0)) vs c=0.3: " + "; ".join(outs) + ("  -> bistable, tipping share %.3f" % (1-0.3/(q0*F)) if q0*F > 0.3 else "  -> evasion is globally stable (s(0) < c)"))
print("   with q0 F = 1.2 the sanction falls with x but stays above c until x = 0.75; still bistable. A sanction that stays above c for ALL x")
p = replicator([0.05, 0.95], lambda p: [-0.3, -(0.5 + 0.5*p[0])])
print(f"   (s(x) = 0.5 + 0.5(1-x) >= 0.5 > 0.3): from x0=0.95 the evader share goes to {p[1]:.3f}: compliance globally stable, no tipping share.")
print("   -> the lemma's 'both stable' clause needs the premise s(0) > c > s(1).")

print("(2) Prop 5.4 with two deviations: A has (g=1.0, p_d=0.1), B has (g=0.2, p_d=0.6); C=3, D=6, v=1, delta=0.9")
def ok(g, pd, C=3.0, D=6.0, v=1.0, dl=0.9): return (1-dl)*g + dl*pd*(D-C) <= dl*(1-pd)*(C-v)
print(f"   deviation A (max g): condition holds = {ok(1.0, 0.1)}; deviation B (smaller g, larger p_d): holds = {ok(0.2, 0.6)}")
print("   -> the statement must quantify over deviations (each with its own p_d), or assume p_d common to all deviations.")

print("(3) Remark S2.1 multiplier with diffusion: single channel, Gamma = (1-beta) r omega dK/(dK+df)")
for (dK, df, Gamma) in [(0.2, 0.0, 1.5), (0.2, 0.1, 1.5), (0.05, 0.05, 3.0)]:
    lam_true = 1 + (dK+df)*(Gamma-1); lam_text = 1 + dK*(Gamma-1)
    T_true = math.log(50)/math.log(lam_true); T_text = math.log(50)/math.log(lam_text)
    print(f"   dK={dK}, df={df}, Gamma={Gamma}: eigenvalue 1+(dK+df)(Gamma-1)={lam_true:.3f} (text 1+dK(Gamma-1)={lam_text:.3f}); periods 1%->50%: {T_true:.0f} vs text {T_text:.0f}")

print("(4) Theorem 5.12: with coverage U_t/Y_t -> 0 and a residual floor h(1-U/Y)+, survival <= prod(1 - h(1-eps)) after T_eps;")
print("    whether Y grows is irrelevant to that bound (take Y constant and U_t decreasing: the bound holds). The premise (variety grows) is idle in the proof.")

print("(5) Prop 5.4(5): v = [(1-d)P + d q (D+U)]/(1-d+2dq); with q=0.6 the 'neither' probability 1-2q is negative")
P, D, U, dl = 0.0, 3.0, -2.0, 0.9
for q in (0.3, 0.5, 0.6):
    print(f"   q={q}: 1-2q = {1-2*q:+.2f}; v = {((1-dl)*P + dl*q*(D+U))/(1-dl+2*dl*q):.4f}")
