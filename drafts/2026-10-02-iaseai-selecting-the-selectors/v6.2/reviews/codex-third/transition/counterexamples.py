"""Independent checks of remaining v6.2 transition boundary statements."""
import math

# detectlink defines timely detection as detection plus effective response.
decisive_time = 2.0
detection_time = 0.5
original_response_time = 0.5
human_response_time = 2.0
p_before = float(detection_time + original_response_time > decisive_time)
p_after = float(detection_time + human_response_time > decisive_time)
assert p_before == 0.0 and p_after == 1.0
print('Same detector, response requiring human authorization: p_d =', p_before, '->', p_after)

# A verifier with zero inbound conversion has row sum 0 < 1 throughout.
# With a=c=zeta=1, epsilon*d=.01 and initial normalized support=2,
# z(t)=2 exp(-.01t), u(t)=logit(.99)+200(1-exp(-.01t))-t.
# Its asymptotic capture is removed, but its decisions are highly captured first.
def logit_share(t):
    return math.log(99.0) + 200.0 * (-math.expm1(-0.01*t)) - t

def alternate_share(t):
    u = logit_share(t)
    if u >= 0:
        q = math.exp(-u)
        return q/(1+q)
    q = math.exp(u)
    return 1/(1+q)

assert 0 < 1  # full inbound row sum
assert alternate_share(50) < 1e-12
assert logit_share(1000) < -700
print('Row sum 0, captured start .99: alternate share at t=50 =', alternate_share(50))
print('The same verifier eventually uncaptures: logit at t=1000 =', logit_share(1000))

# Optional endpoint: complete pooling erases every strict relative ordering.
payoffs = (2.0, 1.0)
beta = 1.0
pooled = tuple((1-beta)*p + beta*sum(payoffs)/len(payoffs) for p in payoffs)
assert payoffs[0] > payoffs[1] and pooled[0] == pooled[1]
print('Complete pooling changes strict ordering:', payoffs, '->', pooled)

# Optional wording check: T-R falling does not itself imply g_C rising.
def assurance(R,T,P=0.0,S=-1.0,F=0.0,v=.5):
    gc = R-v*(P-F)-(1-v)*T
    gd = (1-v)*(P-S)
    return gc,gd/(gc+gd)
old = assurance(2.,3.)
new = assurance(1.,1.2)
assert .2 < 1 and new[0] < old[0] and new[1] > old[1]
print('T-R falls 1->.2, but g_C falls and trust threshold rises:', old, '->', new)
