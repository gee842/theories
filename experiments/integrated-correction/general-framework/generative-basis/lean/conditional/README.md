# Conditional universality of continued support

AI-assisted development, 6 October 2026. This package advances Ren's request to
state laws shared by any reality satisfying explicit conditions. It contributes
to the [conditional-universality statement](../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md).
It uses the existing [relational core](../README.md), without changing its laws.

## Quantified account

`ResourceContinuation.lean` quantifies over an arbitrary state carrier, event
alphabet, and transition relation. Choose an independently justified reserve
`r(s)`, event demand `d(s,a,t)`, and supplied credit `c(s,a,t)`, all natural
numbers. Its law class requires every permitted event to satisfy

```
r(t) + d(s,a,t) ≤ r(s) + c(s,a,t).
```

The law allows unrecorded loss and zero-demand events. `SupportTrace` retains
actual intermediate states and exact totals for each accounted history. Every
finite core `Trace` has such an account. The main theorem derives

```
total demand + final reserve ≤ initial reserve + total credit.
```

Accounted histories compose through their actual common boundary state, adding
all three totals. An executable closed accounted cycle has an executable history
of any finite number of repetitions, with proportional demand, credit, and
credit-event count. This is an existential admissibility result under the stated
law. A genuinely exhaustible external store cannot be omitted from the state and
then treated as restored by an abstract local cycle.

It also proves this balance on every finite interval of any supplied infinite
execution. Thus unbounded cumulative demand requires unbounded cumulative
credit. The theorem holds for each resource account separately, with no summing
of unlike supports into a universal value. A step-preserving map into a process
with a justified account transfers the bound to the concrete process.

Two stronger results expose their extra premises:

- If **every event demands at least one unit**, every infinite execution has a
  positive-credit event at some index from `start` through
  `start + reserve(states(start))`, for every `start`.
- If credit per event is also bounded above by `K`, then every interval satisfies
  `event count + final reserve ≤ initial reserve + K × positive-credit-event count`.

An infinite execution is conditional input to these necessity statements. No
existence, inevitability, actor control, or favorable direction is inferred.
Nonempty cycles with positive demand must cover that demand with credit.

## Realizations and boundaries

`RenewalExamples.lean` proves:

- A resource-consuming cycle can continue forever with ongoing paid restoration.
  The very same event law permits a terminal branch from the same initial state.
- Positive credit on every permitted event does not ensure continuation: demand
  can exceed provision and deplete every finite initial reserve.
- An infinite zero-demand process requires no credit and satisfies the general
  balance. It falls outside the positive-demand results.
- An arbitrarily large one-time credit can finance an arbitrarily long finite
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

The reserve is a physical or operational accounting quantity to be identified,
not reward, welfare, meaning, or a universal scalar value. At a declared system
boundary credit can mean renewal, conversion of an untracked store, or external
provision. The theorem does not identify which mechanism provides it. Recording
the whole universe as the boundary may make a different account appropriate.

Trivial all-zero accounts satisfy any relation and explain nothing. A useful
application must establish the resource interpretation and demand premise
independently of the desired conclusion. Positive-demand bounds apply to the
specified discrete events; arbitrary subdivision or zero-cost stuttering changes
that premise. Summable real-valued costs and physical duration are not covered by
the natural-number event-count corollaries. No empirical calibration is claimed
here, and no regulator, learning rule, or concern mechanism is derived by these
accounting constraints alone.

## Reproduce and audit

Run in this directory:

```sh
python3 check.py
```

The checker pins Lean `4.29.1`, freezes all source bytes, rebuilds the inherited
core and the new modules in a fresh temporary directory, rejects proof holes and
custom axiom declarations, and audits every newly declared theorem. It accepts
only the standard dependencies `propext` and `Quot.sound`; some declarations have
empty axiom dependencies. This is not an axiom-free foundational claim.

The recorded check passed all four modules: 18 inherited core audits and **60
new theorem audits** (21 accounting, 21 realization/boundary, 18 support).
Of the new audits, 34 have empty axiom dependencies; the remaining 26 depend
only on the allowed standard axioms.

`verification.json` records compiler, source, checker and log hashes, exact audited
declarations, dependency results, and whether sources stayed unchanged during the
check. `verification/` preserves the compiler output. Local compiled caches are
ignored and are not trusted by the checker.
