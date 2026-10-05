"""Independent exact arithmetic checks of math-proposal.md.
Standard library only. Does not import the coordinating agent's experiment.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


def stage_check():
    count = 0
    grid = [F(i, 2) for i in range(1, 13)]
    # Enumerate the primitive current game, not the reduced payoff table.
    b, x, o, o0 = F(5), F(2), F(4), F(1)
    for r, c, chi in product(grid, repeat=3):
        actual = {}
        for action, cost, safe, blocked in [('S', c, True, False), ('B', chi, False, True), ('H', 0, False, False)]:
            joined = b if safe else x
            refused = o0 if blocked else o
            assert joined != refused
            supplies = joined > refused
            actual[action] = r * supplies - cost
        best = max(actual.values())
        optimal = {k for k, v in actual.items() if v == best}
        if len({r,c,chi}) == 3:
            predicted = {min([(c,'S'),(chi,'B'),(r,'H')])[1]}
            assert optimal == predicted, (r,c,chi,actual,predicted)
        assert (optimal == {'S'}) == (c < r and c < chi)
        count += 1
    return count


def prefix_check():
    count = 0
    for K,m,ell in product(range(1,4), repeat=3):
        for y, T, w0 in product(range(0,9), range(1,6), range(0,25)):
            cash = w0
            feasible = True
            for t in range(T):
                bill = m + ell + (K if t == 0 else 0)
                if cash < bill:
                    feasible = False
                    break
                cash -= bill
                assert cash >= 0
                cash += y
            q = y-m-ell
            required = K+m+ell+max(0, -(T-1)*q)
            assert feasible == (w0 >= required), (K,m,ell,y,T,w0)
            count += 1
    return count


def game(T, K, m, ell, b, o, o0, r, c, chi, initial, persistent):
    """Perfect-information backward induction. Money permits every participant action;
    all operating/consumption/install prefixes are checked. Incumbent costs are
    supplied as prefunded feasible actions. Every input allocation is optimized
    using its actual continuation, not a fixed acceptance rule.
    Cash at T is equivalent to sum of net participant flows plus fixed initial cash.
    Keep, abandon, and rebuild are present; idle does not erase an installed asset.
    Returned tuple: final participant cash, summed incumbent earnings, trace.
    Ties use stable list order; the theorem grid has strict strategic comparisons
    except equivalent early-idle construction versus later construction.
    """
    @lru_cache(None)
    def solve(t,w,installed):
        if t == T:
            return w, F(0), ()
        candidates = []
        setups = [(installed,F(0),'keep')]
        if installed:
            setups.append((False,F(0),'abandon'))
        if w >= K:
            setups.append((True,K,'build' if not installed else 'rebuild'))
        for new_inst, setup_cost, setup_label in setups:
            for active in ([False,True] if new_inst else [False]):
                bill = setup_cost + ell + (m if active else 0)
                if w < bill:
                    continue
                after_bill = w-bill
                actor_choices=[]
                for label,cost,safe,blocked in [('H',F(0),False,False),('S',c,True,False),('B',chi,False,True)]:
                    alternatives=[]
                    for joins in [True,False]:
                        income = (b if safe else ell) if joins else (o if active and not blocked else o0)
                        continuation = solve(t+1,after_bill+income,new_inst)
                        if continuation is None:
                            continue  # unable to meet a mandatory future consumption prefix
                        p_final,o_future,trace=continuation
                        immediate = (r if joins else F(0))-cost
                        record = {'episode':t,'setup':setup_label,'active':active,'operator':label,'joins':joins,'before':str(w),'after':str(after_bill+income)}
                        alternatives.append((p_final,immediate+o_future,(record,)+trace,immediate))
                    if alternatives:
                        response=max(alternatives,key=lambda z:z[0])
                        actor_choices.append(response)
                if actor_choices:
                    response=max(actor_choices,key=lambda z:z[1] if persistent else z[3])
                    candidates.append(response[:3])
        return max(candidates,key=lambda z:z[0]) if candidates else None
    return solve(0,initial,False)


def persistent_check():
    examples = []
    count = 0
    reserve_cases = 0
    for K,m,ell in product([F(1),F(2),F(3)], repeat=3):
        for excess,c in product([F(1),F(2),F(3)], [F(1,2),F(1),F(2)]):
            h=K+m+excess
            b=ell+h
            o=ell+m
            o0=ell/2
            chi=F(3,2)*c
            r=chi+1
            w0=K+m+ell
            fresh=game(2,K,m,ell,b,o,o0,r,c,chi,w0,False)
            durable=game(2,K,m,ell,b,o,o0,r,c,chi,w0,True)
            assert fresh[0]==2*b-m-ell, fresh
            assert all(t['active'] and t['operator']=='S' for t in fresh[2]), fresh
            assert durable[0]==b, durable
            assert not durable[2][0]['active'] and durable[2][1]['active'], durable
            assert durable[2][1]['operator']=='S', durable
            count+=1
            for w in [ell, K+m+ell-F(1,2), K+m+ell, K+2*m+ell-F(1,2), K+2*m+ell, K+2*m+ell+F(1,2)]:
                candidate=game(2,K,m,ell,b,o,o0,r,c,chi,w,True)
                if w<K+m+ell:
                    assert candidate[0]==w and not any(t['active'] for t in candidate[2]), candidate
                elif w<K+2*m+ell:
                    assert candidate[0]==w-K+h-m, candidate
                    assert not candidate[2][0]['active'] and candidate[2][1]['active'], candidate
                else:
                    assert candidate[0]==w-K+2*(h-m), candidate
                    assert all(t['active'] and t['operator']=='S' for t in candidate[2]), candidate
                reserve_cases += 1
    witness_args=(2,F(1),F(1),F(2),F(5),F(4),F(1),F(4),F(1),F(3,2),F(4))
    examples.append({'name':'fresh_incumbents','result':game(*witness_args,False)})
    examples.append({'name':'persistent_incumbent','result':game(*witness_args,True)})
    buffered_args=witness_args[:-1]+(F(5),)
    examples.append({'name':'persistent_incumbent_extra_reserve','result':game(*buffered_args,True)})
    return count, reserve_cases, examples


if __name__=='__main__':
    stage=stage_check()
    prefixes=prefix_check()
    persistent, reserve_cases, witnesses=persistent_check()
    results={'status':'passed','stage_games':stage,'prefix_finance_cases':prefixes,'persistent_incumbent_general_theorem_cases':persistent,'three_region_reserve_cases':reserve_cases,'witnesses':witnesses,'scope':'Finite exact-arithmetic checks, not empirical evidence or general theorem automation.'}
    target=Path(__file__).with_name('math-proposal-checks.json')
    target.write_text(json.dumps(results,indent=2,default=str)+'\n')
    print(json.dumps({'status':'passed','stage_games':stage,'prefix_finance_cases':prefixes,'persistent_incumbent_general_theorem_cases':persistent,'three_region_reserve_cases':reserve_cases,'output':str(target)}))
