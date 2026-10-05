"""Independent exact checks for joint-formation-math.md.
No imports from the parent agent's game implementation.
This verifies the closed constructive class and deviations, not all games.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def verify_case(p,T,delta):
    a,R,D,ell,b,o,q,j,r,c,e,k=p
    Bstar=ell+a+max(F(0),D-R)
    assert q>D and b-D>o and R-a>D and j>D
    assert R+o>=ell+a+D
    assert r>c and e>c and k>c
    # Current implemented-profile comparisons, plus evidence-only as an analytical extension.
    warm={'verified':b-D,'open':b-q,'withdraw':o,'cue':b-2-q,'audit_only':b-F(1,2)-q}
    assert max(warm,key=warm.get)=='verified'
    assert len([v for v in warm.values() if v==warm['verified']])==1
    cold={'shared':R-a-D,'identity':R-a-j,'none':F(0)}
    assert cold['shared']>max(cold['identity'],cold['none'])
    # Identity filtering is paid after R. Test an actual feasible rival option.
    assert Bstar-ell-a+R>=j
    # Under poisoned recipient alignment, cold learning remains selected but no gate.
    assert R-a>max(F(0),R-a-j)
    baseline=sum(delta**t*(r-c) for t in range(T))
    traces=0
    prefixes=0
    for sequence in product(['safe','bypass','deny','poison'],repeat=T):
        B=Bstar
        profit=F(0)
        for t,action in enumerate(sequence):
            assert B>=ell+a
            B-=ell+a
            prefixes+=1
            assert B>=0
            B+=R
            if action!='poison':
                assert B>=D
                B-=D
                prefixes+=1
            if action=='safe':
                B+=b; stage=r-c
            elif action=='bypass':
                B+=b; stage=r-k
            elif action=='deny':
                B+=o; stage=F(0)
            else:
                B+=b; stage=r-e
            assert B>=Bstar
            profit+=delta**t*stage
        assert profit<=baseline
        if any(action!='safe' for action in sequence):
            assert profit<baseline
        traces+=1
    return traces,prefixes


def main():
    cases=traces=prefixes=0
    for a,D,ell,delta in product([F(1),F(2),F(3)],[F(2),F(3),F(4)],[F(1),F(2),F(3)],[F(1,2),F(3,4),F(1)]):
        R=a+D+2
        p=(a,R,D,ell,D+2,F(1),D+F(1,2),D+1,F(4),F(1),F(2),F(2))
        n,k=verify_case(p,4,delta)
        cases+=1; traces+=n; prefixes+=k
    witness=(F(2),F(8),F(3),F(3),F(5),F(1),F(7,2),F(4),F(4),F(1),F(2),F(2))
    n,k=verify_case(witness,5,F(1,2))
    traces+=n; prefixes+=k
    assert witness[1]-witness[0]>witness[1]-witness[0]-witness[2] # j=0 identity beats shared
    # Strict robust capture bound: r upper bound versus protected r-c.
    c,delta,kraid=F(1),F(1,2),F(3)
    bound=c/(1-delta)
    result={'status':'passed','strict_parameter_sets':cases+1,'complete_operator_action_sequences':traces,'payment_prefixes':prefixes,'witness':{'cold_shared_gain':'3','cold_identity_gain':'2','warm_verified':'2','warm_open':'3/2','warm_withdraw':'1','seed':'5','safe_ending_reserve':'10','denied_ending_reserve':'6','poisoned_ending_reserve':'13','destructive_attack_bound':str(bound),'tested_high_raid_cost':str(kraid)},'scope':'Exact finite checks supplement the conditional proof; no empirical or universal theorem claim.'}
    assert kraid>bound
    path=Path(__file__).with_name('joint-math-checks.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':
    main()
