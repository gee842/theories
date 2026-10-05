"""Post-run deductive certificate. Does not change the frozen experiment/predictions.

Evaluate the already audited finite software law with exact rational weights.
A nonzero 2x2 determinant rules out every finance-only p times authority-only q,
not merely the particular local standardization used in the registered test.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import queue_model
import service

def encode(x): return dict(fraction=str(x),decimal=float(x))

def run():
    results=[]
    for regime in service.REGIMES:
        arrival=F(13,20) if regime['name']=='urgent_fifo' else F(7,20)
        R=[F(0) for _ in range(4)]; P=[F(0),F(0)]; mass=F(0)
        for ib,backlog in enumerate((0,1,3)):
            for bursts in product((False,True),repeat=5):
                k=sum(bursts)
                arrival_weight=arrival**k*(1-arrival)**(5-k)
                for id,duration in enumerate((1,2,4)):
                    for length in (2,4):
                        w=(F(1,4),F(1,2),F(1,4))[ib]*arrival_weight*(F(1,4),F(1,2),F(1,4))[id]*F(1,2)
                        mass+=w
                        for f in (0,1):
                            gate=queue_model.predict_path(regime,backlog,bursts,duration,length,f,0,mode='diag')['gate']
                            if gate: P[f]+=w*F(17,20)
                            for a in (0,1):
                                recovered=queue_model.predict_path(regime,backlog,bursts,duration,length,f,a)['recovered']
                                if recovered: R[2*f+a]+=w*F(17,20)*F(19,20)
        assert mass==1
        determinant=R[0]*R[3]-R[1]*R[2]
        if regime['name']=='reserved_control': assert determinant==0
        else: assert determinant!=0
        results.append(dict(regime=regime['name'],recovery=[encode(x) for x in R],
                            p=[encode(x) for x in P],conditional_q=[encode(R[2*f+a]/P[f]) for f in (0,1) for a in (0,1)],
                            determinant=encode(determinant),interaction=encode(R[3]-R[2]-R[1]+R[0])))
    result=dict(status='exact rational certificate',registered=False,
                explanation='Post-run deduction from the predeclared oracle law, not a new held-out prediction or modified acceptance rule. The identity det(p outer q)=0 follows algebraically.',
                regimes=results)
    Path(__file__).with_name('rank-certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    lines=['# Post-run exact rank certificate','',
           'This is a post-run deductive analysis of the predeclared finite-law oracle. It is not a new prediction, additional target trial, or change to the original decision rules. The original experiment remains unchanged.','',
           'For every two-gate product R[f,a] = p[f] q[a], the 2×2 determinant R00 R11 − R01 R10 is exactly zero. Exact rational enumeration of the audited software yields:','',
           '| Regime | Exact determinant | Decimal |','|---|---|---:|']
    for row in results: lines.append(f"| {row['regime']} | {row['determinant']['fraction']} | {row['determinant']['decimal']:.12f} |")
    lines+=['','Both shared-worker cases therefore rule out **every** scalar finance-only p times authority-only q as an exact representation of these four integrated probabilities. This conclusion does not depend on our chosen q standardization or its sampling error. Conditional repair efficacy depends on finance through job timing/backlog. The source theorem remains valid under its invariant-efficacy assumptions; those assumptions fail in these constructed target regimes.','',
            'In urgent_fifo, true R00 = R01 = 0.040826064453125, whereas R10 = 0.05612755859375 and R11 = 0.15775900390625. Authority has exactly no recovery effect for the late-finance arm but a positive effect for the early-finance arm; no common authority-only multiplier reproduces both nonzero rows.','',
            'This exact structural failure coexists with practical agreement at the registered ±7.5 percentage-point tolerance. The held-out cell-rate experiment passed that tolerance in all regimes, and that result must not be relabeled as a failed practical test. Urgent FIFO has a sampled interaction discrepancy; the reserved control also showed a smaller nominal false-positive interaction discrepancy even though its exact factorization holds. The oracle is what separates these structural and sampling effects.','',
            'Exact fractions, gate probabilities and finance-specific conditional repair probabilities are in rank-certificate.json. Reproduce with `python rank_certificate.py`.']
    Path(__file__).with_name('POSTRUN-RANK.md').write_text('\n'.join(lines)+'\n')
    print('Exact rational rank certificates saved.')

if __name__=='__main__': run()
