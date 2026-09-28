"""Sketch: join the capture model to the latency inequality (review of 2026-09-28 paper, section 3).

A reform fires when the OBSERVED substrate falls to an alarm level. Observation is delayed by tau
(evaluation plus decision) and can be flattered by capture:
    V_obs(t) = V(t - tau) + mu * (r / r_H) * (K - V(t - tau)),   r_H = b/d the rule support at full capture.
Run: python3 coupled_chain.py
"""
from check_models import BASE, field, rk4

V_ALARM, V_MIN = 0.6, 0.3
LEVERS = {"raise c 0.5 -> 1.5 (liability)": dict(c=1.5), "raise d 1 -> 3 (rule sunset)": dict(d=3.0)}


def sim(lever, tau=0.0, mu=0.0, T=200.0, dt=0.005):
    P = dict(BASE, h=1.5); f = field(P); r_H = P['b'] / P['d']
    y, t, hist, fired, minV, crossed = [0.6, 0.6, 1.0], 0.0, [[0.6, 0.6, 1.0]], None, 1.0, False
    lag = int(round(tau / dt))
    while t < T:
        _, r_d, V_d = hist[max(0, len(hist) - 1 - lag)]
        if fired is None and V_d + mu * (r_d / r_H) * (P['K'] - V_d) <= V_ALARM:
            P.update(lever); f = field(P); fired = t
        y = rk4(f, y, t, dt); t += dt; hist.append(list(y))
        minV = min(minV, y[2]); crossed = crossed or y[2] < V_MIN
    return fired, minV, crossed


def main():
    P = dict(BASE, h=1.5); f = field(P); y, t, ta = [0.6, 0.6, 1.0], 0.0, None
    while y[2] > V_MIN:
        y = rk4(f, y, t, 0.005); t += 0.005
        ta = t if ta is None and y[2] <= V_ALARM else ta
    print(f"Without reform V falls from {V_ALARM} to {V_MIN} in {t - ta:.2f} time units (the model's own T_irreversible).")
    for name, lever in LEVERS.items():
        print(name)
        for tau in (0.0, 0.5, 1.0, 1.5):
            fired, minV, crossed = sim(lever, tau=tau)
            print(f"   delay {tau:<3}: fires t = {fired:.2f}, min V = {minV:.3f}, floor crossed: {'yes' if crossed else 'no'}")
    print("masking by capture, zero delay, liability lever")
    for mu in (0.0, 0.4, 0.6, 0.8):
        fired, minV, crossed = sim(LEVERS["raise c 0.5 -> 1.5 (liability)"], mu=mu)
        print(f"   mu = {mu}: fires t = {fired:.2f}, min V = {minV:.3f}, floor crossed: {'yes' if crossed else 'no'}")


if __name__ == "__main__":
    main()
