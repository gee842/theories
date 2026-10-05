"""Exact finite accounting for a supplied, maintained participant-recourse protocol.

No external packages; money/usable-work Q is stored in ninths. This is a
constructed finite mechanism, not an empirical or universal ethical model.
"""
from dataclasses import dataclass, asdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

SCALE = 9

@dataclass(frozen=True)
class State:
    E: int = 3
    B: int = 6
    Q: int = 27
    mode: str = "X"  # X, F, or D<number of further X rounds>
    carrier: bool = True

@dataclass(frozen=True)
class Config:
    capacity: int = 27
    funding: int = 11
    threshold: int = 4
    delay: int = 2
    access: bool = True
    authority: bool = True
    external_fair: bool = False


def advance(s, cfg=Config()):
    """Old stock pays Q upkeep/fee; end-of-round funding cannot pay those fees.

    B pays a filing fee before this round's distribution. A new claim leaves
    X in force for exactly cfg.delay rounds, counting the filing round. An
    operative gate then enforces F until B reaches 6 and releases. Outside
    that constraint the return-comparison mechanism selects X.
    """
    active = s.E >= 2
    upkeep_paid = s.carrier and s.Q >= SCALE
    carrier = upkeep_paid
    q = s.Q - SCALE if carrier else 0
    mode = s.mode if carrier and cfg.authority else "X"
    if cfg.external_fair:
        mode = "F"
    b = s.B
    filed = (active and carrier and cfg.access and cfg.authority and not cfg.external_fair
             and mode == "X" and 1 <= b <= cfg.threshold and q >= 2*SCALE)
    if filed:
        q -= 2*SCALE
        b -= 1
        mode = "F" if cfg.delay == 0 else f"D{cfg.delay}"
    rule = "F" if mode == "F" else "X"
    p = (3 if rule == "F" else 1) if active else 0
    available_b = b + p
    draw = min(2, available_b)
    raw_b = available_b - draw
    overflow_b = max(0, raw_b-6)
    b = min(6, raw_b)
    unmet_b = 2-draw
    if mode.startswith("D"):
        delay = int(mode[1:])
        mode = "F" if delay == 1 else f"D{delay-1}"
    elif mode == "F" and b == 6 and not cfg.external_fair:
        mode = "X"
    income_q = cfg.funding if active else 0
    discarded_q = 0
    if carrier:
        raw_q = q + income_q
        discarded_q = max(0, raw_q-cfg.capacity)
        q = min(cfg.capacity, raw_q)
    else:
        # The carrier cannot spontaneously reappear; unserviceable earmarked
        # receipts are discarded rather than turned into free authority.
        discarded_q = income_q + (s.Q if not upkeep_paid else 0)
        q = 0
    e = s.E if active else 0
    ns = State(e, b, q, mode, carrier)
    gross = 90 if active else 0
    common = 18 if active else 0
    common_wear = 9*(s.E+common//9-e)
    participant = 9*p
    incumbent = gross-common-income_q-participant
    assert min(gross,common,participant,incumbent,income_q)>=0
    assert gross == common+income_q+participant+incumbent
    assert 9*s.E+common == 9*e+common_wear
    # Independently audit participant and Q material accounts, in ninths.
    assert 9*s.B+participant == 9*b+9*draw+9*overflow_b+9*int(filed)
    if carrier:
        assert s.Q+income_q == q+9+18*int(filed)+discarded_q
    else:
        assert s.Q+income_q == discarded_q
    ledger = dict(rule=rule,filed=filed,gross=gross,common=common,common_wear=common_wear,
                  participant=participant,incumbent=incumbent,
                  correction_receipt=income_q,correction_upkeep=9*int(carrier),
                  correction_fee=18*int(filed),participant_fee=9*int(filed),
                  correction_discarded=discarded_q,participant_draw=9*draw,
                  participant_discarded=9*overflow_b,unmet_participant_draw=9*unmet_b,
                  carrier_lost=s.carrier and not carrier)
    return ns, ledger


def safe(s):
    return s.E >= 2 and s.B >= 1 and s.carrier


def orbit(s, cfg=Config()):
    seen = {}
    states=[]
    ledgers=[]
    while s not in seen:
        seen[s]=len(states)
        states.append(s)
        s, ledger = advance(s,cfg)
        ledgers.append(ledger)
    start=seen[s]
    return states,ledgers,start


def packed_orbit(s, cfg=Config()):
    states,ledger,start=orbit(s,cfg)
    bad=[i for i,x in enumerate(states) if not safe(x)]
    cycle_ledger=ledger[start:]
    return dict(initial=asdict(s),config=asdict(cfg),transient_length=start,
                period=len(states)-start,min_B=min(x.B for x in states),
                first_protected_condition_failure=bad[0] if bad else None,
                all_states_safe=not bad,
                trace=[dict(tick=i,**asdict(x),**ledger[i]) for i,x in enumerate(states)],
                cycle_totals={k:sum(l[k] for l in cycle_ledger)
                              for k in cycle_ledger[0] if isinstance(cycle_ledger[0][k],int)})


def enumerate_states(cfg=Config()):
    modes = ["X","F"] + [f"D{i}" for i in range(1,cfg.delay)]
    for e,b in product(range(4),range(7)):
        yield State(e,b,0,"X",False)
        for q,mode in product(range(cfg.capacity+1),modes):
            yield State(e,b,q,mode,True)


def main():
    baseline=Config()
    good=packed_orbit(State(),baseline)
    assert good["all_states_safe"] and good["period"]==9 and good["min_B"]==1
    totals=good["cycle_totals"]
    assert totals["gross"]==810
    assert totals["common"]==162
    assert totals["participant"]==171
    assert totals["incumbent"]==378
    assert totals["correction_receipt"]==99
    assert totals["correction_upkeep"]==81
    assert totals["correction_fee"]==18
    assert totals["participant_fee"]==9
    assert totals["filed"]==1
    recovery_state=State()
    for _ in range(9):
        recovery_state,_=advance(recovery_state)
    assert recovery_state == State(B=6,Q=23)
    withdrawals={
        "earmark_cut_after_first_recovery":packed_orbit(recovery_state,Config(funding=9)),
        "authority_lost_after_first_recovery":packed_orbit(recovery_state,Config(authority=False)),
        "signal_access_lost_after_first_recovery":packed_orbit(recovery_state,Config(access=False)),
    }
    for v in withdrawals.values():
        assert not v["all_states_safe"]
    all_states=list(enumerate_states())
    all_states_set=set(all_states)
    initially_safe=0
    indefinitely_safe=0
    cycles=set()
    protected_cycles=set()
    for s in all_states:
        states,ledgers,start=orbit(s)
        for x,l in zip(states,ledgers):
            ns,_=advance(x)
            assert ns in all_states_set
        cyc=states[start:]
        # Rotation-invariant representation of every exact attractor.
        key=tuple(sorted((x.E,x.B,x.Q,x.mode,x.carrier) for x in cyc))
        cycles.add(key)
        if all(safe(x) for x in cyc):
            protected_cycles.add(key)
        if safe(s):
            initially_safe+=1
            indefinitely_safe+=all(safe(x) for x in states)
    funding_sweep=[]
    for income in range(9,19):
        z=packed_orbit(State(),Config(funding=income))
        assert z["all_states_safe"] == (income>=11)
        funding_sweep.append(dict(funding_ninths=income,safe=z["all_states_safe"],
                                 first_failure=z["first_protected_condition_failure"]))
    capacity_sweep=[]
    for capacity in range(9,46):
        z=packed_orbit(State(Q=capacity),Config(capacity=capacity))
        assert z["all_states_safe"] == (capacity>=27)
        capacity_sweep.append(dict(capacity_ninths=capacity,safe=z["all_states_safe"]))
    initialization=[]
    for q in range(28):
        z=packed_orbit(State(Q=q))
        assert z["all_states_safe"] == (q>=23)
        initialization.append(dict(Q_ninths=q,safe=z["all_states_safe"]))
    # At generous funding/capacity, independently predicted delay bound governs.
    timing=[]
    for threshold,delay in product(range(1,7),range(1,6)):
        cfg=Config(capacity=90,funding=27,threshold=threshold,delay=delay)
        z=packed_orbit(State(Q=90),cfg)
        expected=threshold-1-delay>=1
        assert z["all_states_safe"] == expected, (threshold,delay,z["min_B"],z["first_protected_condition_failure"])
        if expected:
            assert z["period"] == 2*(6-threshold)+1+2*delay
        timing.append(dict(threshold=threshold,delay=delay,safe=z["all_states_safe"],
                           predicted_safe=expected,period=z["period"]))
    results=dict(status="all_exact_checks_passed",units="all ledger amounts and Q are ninths",
                 principal=good,
                 comparisons={
                     "controller_only":packed_orbit(State(),Config(access=False)),
                     "externally_locked_fair":packed_orbit(State(),Config(external_fair=True)),
                     "no_surplus_funding":packed_orbit(State(),Config(funding=9)),
                     "insufficient_reserve_capacity":packed_orbit(State(Q=26),Config(capacity=26)),
                     "one_extra_delay_tick":packed_orbit(State(),Config(delay=3)),
                     "carrier_initially_absent":packed_orbit(State(Q=0,carrier=False)),
                 },
                 exact_finite_graph=dict(states=len(all_states),initially_safe=initially_safe,
                    indefinitely_safe=indefinitely_safe,attractors=len(cycles),
                    protected_attractors=len(protected_cycles),all_successors_enumerated=True),
                 interventions_after_first_recovery=withdrawals,
                 funding_sweep=funding_sweep,capacity_sweep=capacity_sweep,
                 initialization_sweep=initialization,timing_sweep=timing,
                 scope=["supplied protocol and allocation candidates, not institutional emergence",
                        "finite exhaustive accounting, not physical experiment",
                        "controller-only comparison uses private current-return replacement",
                        "funding threshold conditional on fixed recovery/release protocol",
                        "fixed fair comparison is explicitly externally enforced"])
    out=Path(__file__).with_name("model-checks.json")
    out.write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps({"status":results["status"],"graph":results["exact_finite_graph"],
                      "cycle_period":good["period"],"cycle_B_min":good["min_B"],
                      "funding_threshold":"11/9","capacity_threshold":3,
                      "initial_Q_threshold":"23/9"},indent=2))


if __name__ == "__main__":
    main()
