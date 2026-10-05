"""Exact matched-spending guard for a proposed capacity-feedback comparator.

This is a new two-period analytic certificate, not an integrated experiment.
All randomness used to select a calendar occurs before the public signal.
"""
from fractions import Fraction as F
import json

p_signal=F(1,2)
p_need_given_signal=F(1,5)
loss=F(10)
repair=F(4)
test=F(1)
upkeep=F(1,10)

# Feedback keeps readiness iff S=1; tests iff S=1, then treats iff positive.
feedback_spend=p_signal*(upkeep+test)
feedback_operating=p_signal*p_need_given_signal*repair

# For an ex ante calendar with readiness probability q, let u=q*a, where
# a is the diagnostic probability conditional on readiness and S=1.
# Spend=.1*q+.5*u >= .6*u; operating=1-.6*u.
# At a .55 expected inquiry cap, the best u is 11/12, attained q=u, a=1.
q=feedback_spend/(upkeep+p_signal*test)
calendar_spend=q*(upkeep+p_signal*test)
calendar_operating=(p_signal*p_need_given_signal*loss
                    -q*p_signal*p_need_given_signal*(loss-repair))
assert calendar_spend == feedback_spend == F(11,20)
assert feedback_operating==F(2,5)
assert calendar_operating==F(9,20)
assert q==F(11,12)

# Merely replaying the feedback schedule marginal uses q=.5, but does not
# match the recipient's actual inquiry spending (diagnosis remains adaptive).
naive_replay_spend=p_signal*(upkeep+p_signal*test)
assert naive_replay_spend==F(3,10)
assert naive_replay_spend != feedback_spend

print(json.dumps({
    'kind':'exact finite prospective-comparison certificate',
    'horizon':2,
    'initial_cash_each_arm':6,
    'max_pathwise_cost':str(upkeep+test+repair),
    'feedback':{'inquiry_spend':str(feedback_spend),
                'operating_loss':str(feedback_operating),
                'total':str(feedback_spend+feedback_operating)},
    'best_ex_ante_calendar_lottery':{
        'probability_keep':str(q),'inquiry_spend':str(calendar_spend),
        'operating_loss':str(calendar_operating),
        'total':str(calendar_spend+calendar_operating)},
    'naive_independent_replay':{'probability_keep':'1/2',
                              'inquiry_spend':str(naive_replay_spend)},
    'operating_loss_gap':str(calendar_operating-feedback_operating),
    'scope':'fixed known model, common objective, no recurrent production, no institution-selection claim'
},indent=2))
