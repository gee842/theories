# Conditional universality of continued support

AI-assisted development, 6 October 2026. This package advances Ren's request to
state laws shared by any reality satisfying explicit conditions. It contributes
to the [conditional-universality statement](../../../../../../theories/becoming/chapters/CONDITIONAL-UNIVERSALITY.md).
It uses the existing [relational core](../README.md), without changing its laws.

## Quantified law

`ResourceContinuation.lean` quantifies over an arbitrary state carrier, event
alphabet, and transition relation. Choose, with independent justification,
what each state holds available for further activity, `held(s)`, what each
event enacts, `enacted(s,a,t)`, and what arrives during it, `arrived(s,a,t)`,
all natural numbers. The law class `SustainLaw` (U1) requires every permitted
event to satisfy

```
held(t) + enacted(s,a,t) ≤ held(s) + arrived(s,a,t).
```

No event enacts more than was held plus what arrived; nothing appears from
nowhere. The law allows unrecorded loss and events that enact nothing.
`SupportTrace` retains actual intermediate states and exact totals for each
supported history. Every finite core `Trace` has such totals. The main theorem
derives

```
total enacted + final held ≤ initial held + total arrived.
```

Supported histories compose through their actual common boundary state, adding
all three totals. An executable closed supported cycle has an executable history
of any finite number of repetitions, with proportional enacted and arrived
totals and arrival-event count. This is an existential admissibility result
under the stated law. A genuinely exhaustible external store cannot be omitted
from the state and then treated as restored by an abstract local cycle.

It also proves this bound on every finite interval of any supplied infinite
execution. Thus unbounded cumulative enactment requires unbounded cumulative
arrival. The theorem holds for each supporting quantity separately, with no
summing of unlike supports into a universal value. A step-preserving map into a
process with a justified law transfers the bound to the concrete process.

Two stronger results expose their extra premises:

- If **every event enacts at least one unit**, every infinite execution has an
  event in which something arrives at some index from `start` through
  `start + held(states(start))`, for every `start`.
- If what arrives in one event is also bounded above by `K`, then every interval
  satisfies `event count + final held ≤ initial held + K × arrival-event count`.

An infinite execution is conditional input to these necessity statements. No
existence, inevitability, actor control, or favorable direction is inferred.
Around a nonempty cycle whose events enact something, what arrives must cover
what was enacted.

Vocabulary renamed on 6 October 2026 at [Ren's direction](../../../../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md),
replacing an exchange picture (account, reserve, demand, credit). Statements
and proofs are unchanged; the [rename record](../verification-history/2026-10-06-before-vocabulary-rename/README.md)
lists every old and new name and checks that only names changed.

## Realizations and boundaries

`RenewalExamples.lean` proves:

- A cycle that draws on what is held can continue forever with ongoing restoration.
  The very same event law permits a terminal branch from the same initial state.
- Something arriving on every permitted event does not ensure continuation:
  what is enacted can exceed what arrives and deplete every finite initial hold.
- An infinite process that enacts nothing needs no arrival and satisfies the
  general law. It falls outside the positive-enactment results.
- An arbitrarily large single arrival can sustain an arbitrarily long finite
  run. A uniform lower frequency bound cannot silently assume a bounded delivery.

`SupportNecessity.lean` supplies the complementary lifetime and dependency
constraints. Each positive-time birth has an earlier still-functioning parent.
With episode lifetime at most `L` and a type rank in `Fin n` that strictly rises
along every allowed parent relation, every live episode is at time `t ≤ n × L`.
Expiry is inclusive; the theorem rules out functioning strictly after the
deadline. An unequal-lifetime version uses a local deadline potential.

The rank is a supplied certificate: this package does not prove that every
finite acyclic graph has such a certificate. An infinite acyclic type chain
can function at every time, a permitted cyclic type relation can remain unused,
and later arrivals without internal parents violate the parent premise. All
three boundaries have checked examples. Episode carriers, support relations,
expiry conditions and type structure remain explicit inputs, rather than claims
that every enduring system has the same dependency architecture.

## What is supplied

What is held is a physical or operational quantity to be identified, not
reward, welfare, meaning, or a universal scalar value. At a declared system
boundary, what arrives can be renewal, conversion of an untracked store, or
external provision. The theorem does not identify which mechanism provides it.
Taking the whole universe as the boundary may make a different choice of
quantities appropriate.

Trivial all-zero quantities satisfy any relation and explain nothing. A useful
application must establish the interpretation and the enactment premise
independently of the desired conclusion. Positive-enactment bounds apply to the
specified discrete events; arbitrary subdivision or stuttering that enacts
nothing changes that premise. Summable real-valued enactments and physical duration are not covered by
the natural-number event-count corollaries. No empirical calibration is claimed
here, and no regulator, learning rule, or concern mechanism is derived by these
constraints alone.

## Reproduce and audit

Run in this directory:

```sh
python3 check.py
```

The checker pins Lean `4.29.1`, freezes all source bytes, rebuilds the inherited
core and the new modules in a fresh temporary directory, rejects proof holes and
custom axiom declarations, and audits every newly declared theorem. Every audit
must be empty: no Lean axiom, including `propext` and `Quot.sound`, is accepted.
Lean's own logic remains a framework presupposition.

The recorded check passed all four modules: 18 inherited core audits and **63
new theorem audits** (24 sustaining-law, 21 realization/boundary, 18 support),
all empty. Until 6 October 2026, 26 of them depended on `propext` and
`Quot.sound`, introduced by `omega` and `simp`. Following Ren's rule of no
assumptions and no axioms, those proofs were rewritten with explicit
constructive arithmetic; three helper lemmas (`le_cancel_left`, `step_then_rest`,
`rest_then_step`) were added. No statement changed. `cycleStates` and
`cycleActions` now read parity from a recursive `even` instead of `% 2`.

`verification.json` records compiler, source, checker and log hashes, exact audited
declarations, dependency results, and whether sources stayed unchanged during the
check. `verification/` preserves the compiler output. Local compiled caches are
ignored and are not trusted by the checker.

## Later package: renewal and closure

[`renewal/`](renewal/README.md) builds on `SupportNecessity`, the core `Depletion` theorems and the U1 law (6 October 2026, 32 audits).
- It proves the cycle extraction this package did not claim: late activity descends from a realized closure of kinds, and acyclic support has a deadline without a supplied rank.
- It shows that constraints which bring in less than their formation demands cannot renew forever, whatever their closure.
