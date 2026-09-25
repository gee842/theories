# R-Dynamics 与社会吸引子

> Status: research note, doctrine-adjacent.  This document uses the current
> `wen-substrate/` line as background, especially the distinction-monism
> carrier `R N δ := Fin N -> δ`, the scope / residual account in
> `r-scope-information-flow.md`, and the historical attractor sketches in
> `wen-algebra.md` / `r8.md`.  It is not a Lean theorem and must not be cited as
> a closure of Claim Z / T0 / T1-T3 / full T5 / GUT-C.

## Abstract

R tower by itself is not a dynamical system.  It is a formal substrate of
distinctions, scopes, projections, direct sums, partial faces, Hom-as-content,
and tower growth.  Attractors appear only after an update law is imposed:

```text
state space X built from R
update law f : X -> X
trajectory x, f x, f^2 x, ...
```

This note proposes a conservative R-dynamics vocabulary for reality-facing
systems and applies it to capitalism.  The central claim is not that
capitalism "is R" in any metaphysical sense.  The claim is narrower:
capitalism can be modelled as a strong attractor regime because it combines
projection, selection, accumulation, recursion, and boundary-stabilisation.
It maps heterogeneous social and ecological distinctions into a price/profit
scope, iterates investment and competition, and repeatedly folds residuals
back into the capital circuit when legal, financial, or technical devices make
them addressable.

The result is a stable but not closed system.  Capitalism generates basins of
accumulation, concentration, commodification, and crisis-cycle behaviour, while
remaining open at the residual boundary: ecology, unpaid care, political force,
meaning, desire, and non-priced obligations are not automatically contained by
the price/profit projection.

## 0. Claim discipline

This document has three layers.

1. **R-kernel facts**.  These are already native to the current doctrine:
   `R N δ := Fin N -> δ`, direct-sum splitting, projection/residual loss,
   `RPattern` partial faces, and finite orbit facts once an endomap is supplied.
2. **R-dynamics schema**.  This is a proposed vocabulary: choose a state space
   built from R, choose an update law, then study fixed points, cycles, basins,
   opening channels, and residual recovery.
3. **Capitalism mapping**.  This is a reality-facing interpretation.  It is
   useful if it clarifies observable mechanisms, but it is not a theorem about
   all economies or all social life.

The safe statement is:

```text
R gives the distinction/scope geometry.
Attractors arise after choosing laws of update.
Capitalism is a candidate real-world update regime with strong attractor form.
```

The unsafe statement is:

```text
Capitalism is formally proved to be an R-attractor.
```

That is not claimed here.

## 1. Minimal R-dynamics vocabulary

### 1.1 State space

At the substrate level:

```text
R N δ := Fin N -> δ
```

For the canonical finite Boolean case:

```text
R N := Fin N -> Bool
```

A reality-facing model does not begin with "the world".  It begins with a
chosen observation:

```text
encode : Phenomenon -> R N
```

or, when the unobserved part matters:

```text
encode : Phenomenon -> R (N + K)
visible  : R (N + K) -> R N
residual : R (N + K) -> R K
```

The residual is not a metaphor.  In the R-scope account, projection from
`R (N + K)` to `R N` forgets a fiber of shape `R K`.  A judgment at the visible
scope is complete only when it descends along that fiber.

### 1.2 Update law

An attractor requires an endodynamic law:

```text
f : X -> X
```

where `X` may be:

```text
R N
R (N + K)
RPattern N
R N x R M
End(R N)
RStream
```

Once `f` is chosen, an orbit is:

```text
x_0, x_1, x_2, ...
x_{t+1} = f x_t
```

In finite `R N`, every orbit eventually enters a cycle.  But a cycle is not
automatically an attractor in the strong sense.  A fixed point or cycle becomes
an attractor when many distinct initial states flow into it.

### 1.3 Attractor, basin, open channel

For finite `X`:

```text
fixed(f)      := { x | f x = x }
periodic_k(f) := { x | f^k x = x and no smaller positive period }
basin(A)      := { x | some iterate of x enters A }
```

Three behavioural classes are enough for this note.

| class | R-dynamics form | reading |
|---|---|---|
| convergent | many states enter a fixed point or small stable set | attractor |
| cyclic | states enter a repeating loop | stable cycle |
| open | new residual coordinates or unbounded stream behaviour remain active | no finite closure without extra law |

### 1.4 The easiest attractor-producing forms

The following structures are the strongest candidates for real-world
attractor maps.

| structure | formal form | attractor behaviour |
|---|---|---|
| projection | `R (N + K) -> R N` | collapses distinct states into the same visible scope |
| idempotent | `p^2 = p` | one-step convergence to image of `p` |
| nilpotent / dissipative | `A^m = 0` or rank drops under iteration | convergence to zero or a low-dimensional subspace |
| closure / normalisation | `cl(cl x) = cl x`, `x <= cl x` where order exists | convergence to closed form |
| compatible merge | `RPattern.merge` | support increases until stable face or conflict |
| finite non-invertible endomap | `f : R N -> R N` not injective | basins form because histories collapse |

By contrast, invertible maps, automorphisms, toggles, and involutions tend to
produce cycles rather than basins.  They are stable as symmetries, not
attractive as dissipative laws.

## 2. How reality maps into R

To map a real system into R, one should not first ask "what is the true N?"
The practical procedure is:

1. Choose distinctions that matter for the question.
2. Encode those distinctions as a finite or stream R-state.
3. Specify the scope of observation.
4. Record the residual.
5. Identify update laws.
6. Ask which laws are reversible, which are projective, which are recursive,
   and which close under iteration.

For a social system, the axes may include ownership, debt, labour time,
production capacity, legal status, price visibility, ecological cost,
administrative legibility, risk transfer, enforcement capacity, and symbolic
legitimacy.  These are not kernel names.  They are interpretation-layer axes.

The decisive question is not whether every axis is binary in ordinary
language.  The R move is to ask whether the system makes operative
distinctions:

```text
owned / not owned
priced / not priced
paid / unpaid
enforceable / unenforceable
liquid / illiquid
profitable / unprofitable
insured / uninsured
visible to accounting / residual
```

Real-valued magnitudes can be represented by many finite distinctions or by a
non-Boolean δ-realisation.  The Boolean presentation is the finite canonical
cross-section, not the only possible semantic realisation.

## 3. Capitalism as attractor regime

Capitalism is not one map.  It is a family of mutually reinforcing maps.  Its
attractor force comes from their composition:

```text
projection -> selection -> accumulation -> reinvestment -> expansion
```

More explicitly:

```text
heterogeneous life-process
  -> price / property / contract / accounting scope
  -> profit comparison
  -> capital allocation
  -> production and market expansion
  -> new heterogeneous life-process under altered constraints
```

This is why capitalism is a good candidate for R-dynamics analysis: it is not
merely a belief system, and not merely an exchange mechanism.  It is an
iterated institutional update law.

### 3.1 Price as projection

The price system acts like a projection:

```text
π_price : R (N + K) -> R N
```

The visible part contains what can be priced, exchanged, owned, collateralised,
taxed, insured, or capitalised.  The residual contains what the current
price/property/accounting scope does not fully see:

```text
ecological depletion
unpaid care
social trust
long-term health
local attachment
meaning
future fragility
political coercion
```

Projection is powerful because it makes comparison possible.  It is dangerous
because visible equality is not full equality.  Two processes with the same
price can differ radically in residual cost.

In R-scope terms:

```text
visible equality != full equality
unless residual rank is zero
or a law determines the residual
```

Capitalism repeatedly tries to create such residual-determining laws:
insurance, carbon credits, risk models, labour contracts, property rights,
intellectual property, futures markets, derivatives, ESG metrics, and state
regulation.  Some of these recover real residual information; others only
rename the loss.

### 3.2 Profit as selection

Profit comparison is a selection law:

```text
select_profit : population_of_firms -> surviving_population
```

Firms, techniques, products, and institutions that fail profitability tests
are removed, acquired, downsized, disciplined, or made dependent.  This is
non-invertible.  Once a firm fails, a factory closes, a neighbourhood changes,
or a skill ecology disappears, the previous state is not recovered simply by
running the update backwards.

This non-invertibility is crucial.  Pure exchange can be reversible in an
idealised model.  Capitalist competition is not.  It kills branches of the
state tree.

### 3.3 Capital as recursion

The capital circuit has recursive form:

```text
M -> C -> P -> C' -> M'
```

where money capital buys commodities and labour-power, enters production, and
returns as expanded money capital when successful.  In R-dynamics terms:

```text
capital_{t+1} = f(capital_t, labour_t, technology_t, law_t, demand_t, residual_t)
```

The key attractor is not money as object.  It is accumulation as a recursive
law:

```text
profit -> reinvestment -> larger capacity -> stronger market position -> profit
```

When this recursion is reinforced by credit, scale economies, network effects,
or monopoly power, it creates basins where many local variations flow toward
concentration.

### 3.4 Property and contract as boundary stabilisers

Property stabilises state boundaries:

```text
who controls what
who may exclude whom
who bears which loss
who may claim which future income
```

In R terms, property and contract pin coordinates.  They turn fluid social
relations into addressable, enforceable, transferable patterns.  That is close
to `RPattern` refinement:

```text
unspecified relation -> specified claim -> enforceable claim
```

A contract is not merely a description.  It is a partial pattern with an
enforcement path.  Compatible contracts compose; conflicting contracts require
adjudication, hierarchy, or crisis.

### 3.5 Debt and interest as temporal attractor

Debt adds a future constraint to the current state:

```text
present liquidity -> future payment obligation
```

Interest adds growth pressure:

```text
obligation_{t+1} = obligation_t + interest_t
```

This produces a temporal attractor: agents must act now in ways that keep the
future payment path viable.  Debt therefore projects future states backward
into present action.

In ordinary economic language, this is discipline.  In R-dynamics language, it
is a cross-time constraint that narrows the basin of viable trajectories.

### 3.6 Commodification as domain expansion

Capitalism does not merely optimise inside a fixed market.  It expands the
market-readable domain:

```text
not-yet-priced -> priced
not-yet-owned -> owned
not-yet-financialised -> financialised
not-yet-managed -> managed
```

This is not simple convergence.  It is attractor-plus-opening.  The system
stabilises more and more phenomena under the price/profit scope while opening
new residual boundaries at each expansion.

Examples:

```text
land -> real estate asset
attention -> advertising inventory
personal data -> behavioural prediction asset
education -> credential market
care -> service industry
future revenue -> securitised instrument
carbon absorption -> tradable credit
```

Each move increases the visible scope of capital while also creating new
residuals: exclusion, surveillance, fragility, moral injury, ecological
overshoot, or political backlash.

## 4. The capitalism attractor map

A schematic R-model can be written:

```text
X_t := R (P + L + E + S + K)

P = priced / property / profit-visible coordinates
L = labour and reproduction coordinates
E = ecological coordinates
S = state / legal / enforcement coordinates
K = residual and unpriced coordinates
```

Capitalist observation uses a visible scope:

```text
π_cap : X_t -> R P
```

The update law is a composite:

```text
F_cap =
  expand_scope
  ∘ allocate_by_profit
  ∘ enforce_property
  ∘ price_projection
  ∘ produce_and_exchange
```

This gives a trajectory:

```text
X_0, F_cap X_0, F_cap^2 X_0, ...
```

The main attractors are:

| attractor | mechanism | R-dynamics shape |
|---|---|---|
| accumulation | profit recursion | positive feedback under iteration |
| concentration | scale, credit, network effects | many-to-one competitive selection |
| commodification | expansion of price/property scope | residual coordinates become visible coordinates |
| proletarianisation / dependency | loss of independent access to means of life | state-space narrowing |
| crisis cycle | leverage, overproduction, residual return | periodic or recurrent basin switching |
| abstraction of value | heterogeneous value becomes exchange value | projection to common comparison axis |

The strongest single formula is:

```text
diverse value -> price -> profit -> accumulation -> power over future production
```

This is a projection-selection-recursion loop.

## 5. Why capitalism is stable but not closed

Capitalism is stable because the same law applies across many domains:

```text
Can it be owned?
Can it be priced?
Can it be exchanged?
Can it produce return?
Can the return be reinvested?
Can the risk be transferred?
Can the residual be legally or financially encoded?
```

When the answer becomes yes, the phenomenon enters the capital basin.

But capitalism is not closed because the price/profit scope does not exhaust
the full state.  Its residuals are structurally real:

```text
ecological limit
bodily exhaustion
care work
social trust
political legitimacy
meaning
non-market obligation
future uncertainty
```

If a residual remains outside the update law, it can return as:

```text
strike
illness
burnout
ecological disaster
financial crisis
political revolt
regulatory intervention
war
withdrawal
refusal
```

Thus capitalism is not a completed self-contained attractor.  It is a strong
partial attractor with open residual boundary.

## 6. Capitalism compared with other social attractors

Capitalism is not the only attractor-producing social form.  It is distinctive
because it composes several attractor mechanisms at once.

| regime | projection | selection | recursion | attractor |
|---|---|---|---|---|
| bureaucracy | case -> file / category | procedural admissibility | rule application | administrative legibility |
| law | conflict -> claim / precedent | admissible evidence | judgment / appeal | legally decidable form |
| social media | expression -> engagement metrics | algorithmic ranking | feedback optimisation | attention capture |
| academic system | inquiry -> paper / citation / grant | peer and metric selection | career reproduction | publishable research shape |
| military command | situation -> target / order | threat prioritisation | command loop | operational objective |
| capitalism | life-process -> price / profit / asset | competition and return | accumulation | capital expansion |

The capitalist case is unusually strong because its projection is portable.
Money, price, credit, and ownership allow very different phenomena to enter a
common comparison space.  That makes capitalism a high-mobility attractor.

## 7. Fixed points, cycles, and crises

A naive model would expect capitalism to converge to equilibrium.  The
R-dynamics view is more cautious.

Capitalism has local fixed-point tendencies:

```text
stable property titles
standardised commodities
repeatable labour contracts
routine profitability
institutionalised accounting categories
```

It also has cycles:

```text
boom / bust
credit expansion / deleveraging
innovation / commoditisation
competition / concentration / antitrust or breakdown
globalisation / protectionist recoil
```

And it has open dynamics:

```text
new technology
new frontier
new asset class
new legal form
new residual crisis
```

So the expected behaviour is not one global fixed point.  It is a moving
landscape of basins:

```text
local convergence + recurrent cycles + residual-driven opening
```

This matches the intuition that capitalism is both stabilising and
destabilising.  It stabilises the form of accumulation while destabilising the
contents that pass through it.

## 8. Toward a formal programme

To formalise this in the repository without overclaiming, the clean path would
be a general R-dynamics layer first, and social examples second.

### 8.1 R-dynamics layer

Candidate definitions:

```lean
def FixedPoints {X : Type} (f : X -> X) := {x : X // f x = x}
def Orbit {X : Type} (f : X -> X) (x : X) : Nat -> X
def EventuallyPeriodic {X : Type} (f : X -> X) (x : X) : Prop
def Basin {X : Type} (f : X -> X) (A : Set X) : Set X
def IsIdempotent {X : Type} (p : X -> X) : Prop := p ∘ p = p
```

For finite `R N`, one can prove:

```text
every orbit is eventually periodic
idempotent maps converge in one step to image
nilpotent linear maps converge to zero
non-injective finite maps create basin collapse
```

### 8.2 Scope-aware dynamics

The next layer should combine update with observation:

```text
q : X -> Y
f : X -> X
g : Y -> Y
q ∘ f = g ∘ q
```

If the square commutes, the visible dynamics is a lawful quotient of the full
dynamics.  If it does not commute, the visible model hides residual forces.

For capitalism, this is the central test:

```text
Does the price/profit dynamics commute with the full social/ecological update?
```

Usually no.  That non-commutation is the formal shape of externality.

### 8.3 Reality-facing model discipline

A capitalism model should state:

1. What the axes are.
2. Which axes are visible to price/profit.
3. Which axes are residual.
4. Which law claims to recover residuals.
5. Which update maps are reversible.
6. Which update maps collapse histories.
7. Which attractors are empirically predicted.
8. Which events would falsify the model.

Without these, "capitalism is an attractor" remains only a metaphor.

## 9. Falsification handles

The model becomes useful only if it can fail.  Several failure routes are
clear.

| claim | falsifier |
|---|---|
| price acts as projection | show that the relevant system preserves all residual distinctions needed for the judgment |
| profit acts as selection | show that survival/allocation is not materially affected by return, competition, or capital access |
| accumulation acts recursively | show that profit does not systematically feed future control over production |
| residuals return as crisis | show that ignored residuals remain permanently inert under the modelled scope |
| commodification expands scope | show that non-market domains are not drawn into price/property/accounting forms under iteration |
| capitalism forms attractor basins | show that trajectories do not cluster toward accumulation, concentration, commodification, or crisis cycles |

These are empirical and historical questions, not Lean obligations by
themselves.  The formal role of R is to make the map explicit enough that the
questions are well-posed.

## 10. Thesis

Capitalism is best read as a strong, partial, reality-facing attractor regime:

```text
projection: heterogeneous life becomes price-visible
selection: profitability filters survival
recursion: profit reinvests into future capacity
boundary: property and contract stabilise claims
expansion: residual domains are pulled into market form
crisis: unrecovered residuals return as discontinuities
```

Its stability comes from the repeated composition of these maps.  Its
instability comes from the fact that its primary projection is not the full
state.  Capitalism therefore does not close reality.  It organises a powerful
basin inside reality by making more and more distinctions legible as capital,
while continually producing residuals that exceed that legibility.

In R language:

```text
capitalism = projection-selection-recursion over a non-closed residual field
```

That is why it attracts, why it expands, why it stabilises, and why it breaks.

## 11. Open obligations

This note leaves several obligations open.

1. Define a small, doctrine-compatible `R/Dynamics.lean` layer for finite
   endomaps, fixed points, cycles, basins, and idempotent convergence.
2. Connect `R.Scope` with dynamics through commuting observation squares.
3. Give a precise externality predicate as failure of visible dynamics to
   commute with full dynamics.
4. Build toy examples: projection attractor, debt recursion, profit selection,
   and residual crisis.
5. Keep all social, economic, and Chinese semantic labels outside
   `Foundation/R/`; they belong in docs, examples, or Atlas-style overlays.

Until then, the capitalism analysis is a disciplined model proposal, not a
formal theorem.
