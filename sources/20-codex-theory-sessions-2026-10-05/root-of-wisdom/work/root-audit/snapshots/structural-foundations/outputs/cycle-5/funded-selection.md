# Funded selection among decision rules

This experiment makes the copying and financing of decision rules part of the dynamics. It extends the [fourth-cycle operating process](../cycle-4/adoption-dynamics.md) while explicitly adding population turnover, a treasury, measurement, new-plant construction, and rule transmission.

The principal result is that an early cash-ranking rule can make one program reach 100% of a population while renewal capacity declines until no successor can be funded. Evaluating later cash changes both the selected program and the renewal outcome. A calibrated forecast from the early report gives the same result as later observation: the mechanism depends on how available evidence is used, not simply on waiting longer.

All persistence results remain conditional on the specified outside grant and production inputs. The model does not establish that a population creates all its own support.

## The candidate rules and the common calendar

There are two supplied programs. `S` uses the one-cycle rolling terminal-cash planner; `L` uses the two-cycle planner. Every new organizational instance starts with the same eight-module basic plant, 240 cash, and no auxiliary diagnostic channels. The prior experiment's paid diagnostic, authorization, and execution sequence remains unchanged.

The [checker](verification/check_funded_selection.py) obtains the following profiles by executing the earlier planner and expanding its actual payment steps:

| Program | Cash after first repair cycle | Cash after second cycle | Channels at the end |
|---|---:|---:|---:|
| S | 140 | 100 | 2 |
| L | 128 | 136 | 4 |

Every population epoch lasts **two complete repair cycles**, sixteen original physical slots. Under both evaluation procedures, parents operate for both cycles, offspring are created at the same endpoint, and the same funding arrives on the same schedule. An early evaluator records first-cycle cash; a late evaluator records second-cycle cash. This does not compare a one-cycle reproduction interval with a two-cycle interval.

Every parent then retires. Its remaining cash returns to the common treasury; its basic plant and auxiliary channels are dismantled without resale. This forced two-cycle turnover is a new physical mechanism. It prevents an unacknowledged transfer of installed apparatus and differs from leaving a viable L carrier operating indefinitely. Closure has no additional modeled liability beyond the listed operations and destruction of the assets.

Only a **program** is copied. A newborn receives its own fully financed plant and reserve. One cannot obtain a new functioning organization merely by copying the label S or L.

## Every birth and every measurement are financed

The birth packet costs 260:

| Component | Amount | Accounting role |
|---|---:|---|
| Newborn cash | 240 | A transfer into the child's reserve |
| Construction of the basic eight-module plant | 16 | A payment to the supplied construction process |
| Program copying and installation | 4 | A payment to the transmission process |

Construction and copying have zero additional calendar delay in this supplied model. Auxiliary channels are purchased later by the newborn's actual planner from its 240. The fixed construction price and availability of the builder are explicit assumptions.

The initial two founders, one S and one L, are established with an outside endowment of 520: 480 operating cash, 32 basic-plant construction, and eight copying/installation fees. Initial common treasury is zero. Subsequent outside support is a grant of `G=150` per active parent per two-cycle epoch; no grant arrives for an empty population. Operating production also retains the earlier model's explicit external feedstock.

At the start of an epoch, the grant arrives in the treasury. A flat audit-and-record contract costs `e=2` per parent and is prepaid before the observed outcomes. It covers recording at the declared observation time and retaining the program/report association through the common copying boundary. The early and late contracts have the same price for this controlled comparison. Program/report payload does not alter the bill or grant. An independently priced evaluation-delay model appears in [paid evaluation](paid-evaluation.md).

These treasury funds cannot be redirected to rescue or change the incumbent parent operation. Each parent executes its supplied rule using its own 240. After the second cycle, parents remit their actual remaining cash.

Let current counts be `(N_S,N_L)`, total `N`, and treasury reserve `R`. The pool available for births is

\[
F=R+(G-e)N+100N_S+136N_L.
\]

There are at most `K=4` physical sites. The number of newborns is

\[
M=\min\{K,\lfloor F/260\rfloor\}.
\]

Pay all birth packets. Carry the remainder subject to treasury cap `U=259`, discarding any overflow:

\[
R'=\min\{259,F-260M\}.
\]

Capping occurs **after** the births are funded. The cap is less than the cost of one newborn, so an empty population cannot restart from retained treasury alone. There is no unmodeled immigration or permanent external program donor.

The grant must also cover the audit at its earlier payment time: `R+GN≥eN`. Positive terminal funds would not excuse a missed audit prepayment. All base cases satisfy that guard. The no-grant control supplies four treasury units specifically to pay its first audit.

### The real cash ledger

The 240 transferred to each newborn is not destroyed expenditure. The global check includes incumbent cash, treasury, grants, operating receipts, actual operating expenses, audit bills, plant/copy fees, discarded overflow, and the cash still held by children.

For the initial mixed population, 480 incumbent cash plus the grant 300 plus actual operating receipts 480 gives 1,260. It balances exactly against 724 operating/installation expenses, four audit fees, forty new plant/copy fees, 480 child cash, and twelve remaining treasury units. Both evaluation procedures have this same ledger; only the copied program differs.

## The implemented copying rules

The first comparison copies the program of the highest measured-cash parent into every funded newborn. If several parents tie, parents among the tied group are sampled uniformly. Every copy is paid. This is an explicit score-to-copy rule, not a deduction that cash automatically causes reproductive success.

- Early raw cash is 140 for S versus 128 for L, so an initially mixed population copies S.
- Late cash is 100 for S versus 136 for L, so the same initial population copies L.

Both initially fund two children and retain twelve treasury units. Population size is a consequence of financing, not a normalized constant.

## A program can fix while its population disappears

Under early winner copying:

| Epoch | Original repair cycles elapsed | S count | L count | Treasury | S share |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 | 0 | 1/2 |
| 1 | 2 | 2 | 0 | 12 | 1 |
| 2 | 4 | 1 | 0 | 248 | 1 |
| 22 | 44 | 1 | 0 | 8 | 1 |
| 23 | 46 | 0 | 0 | 256 | Undefined |

The final 256 is real retained treasury, but it cannot pay the next 260-unit birth packet. No parent remains to receive the next per-parent grant. Extinction is not represented as a winning type with a zero denominator.

Under late winner copying, the population becomes all L in the first epoch, remains nonempty, and reaches four sites at epoch eleven. Continuing grants and the declared production mechanism finance its subsequent replacements. The claim is indefinite funded renewal under those assumptions, not independence from outside support.

### Exact renewal-capital proof

Define the bookkeeping potential

\[
\Phi=260N+R.
\]

This is the replacement packet value of the current count plus treasury, **not literal cash inventory** or a conserved substance. If spill is `s≥0`, the transition identity is

\[
\boxed{\Phi'=\Phi-12N_S+24N_L-s.}
\]

For an all-S population, every nonempty epoch decreases this finite potential by at least twelve. It must therefore become empty in finitely many epochs. This proves the conclusion beyond the displayed trajectory.

For all L, each parent contributes `136+150−2=284` to the pool, exceeding the 260 needed for one funded replacement. Therefore `M≥N` whenever `1≤N≤K`, and nonemptiness is invariant. At treasury cap 259, surplus can accumulate enough to fund additional sites until the site limit is reached. With treasury cap zero, the same population instead persists at its original count and spills its surplus; persistence and population growth are different claims.

Under this exact retirement and birth mechanism, the per-parent grant thresholds are

\[
G_{\min,L}=260+2-136=126,
\qquad
G_{\min,S}=260+2-100=162.
\]

The base grant 150 lies between them. Raising it to 162 makes pure S replacement financially sustainable. Lowering it to 125 makes even pure L exhaust finite support. These are renewal thresholds for the declared packet, audit, and cohort lifespan, not the earlier operating-viability thresholds of a continuing individual.

With no continuing grant and an initial treasury of four to prepay observation, the first epoch returns only 236, insufficient for a single new packet. Both selection procedures then produce no successor. A better score-to-copy rule cannot manufacture the missing construction and reserve resources.

## Correct interpretation can use early information

The early numerical report distinguishes the two supplied program profiles. With the known model, an evaluator can map early cash 140 to predicted two-cycle return 100, and early cash 128 to predicted return 136. Ranking that predicted return selects L while still observing at the early time.

This calibrated early procedure has exactly the same copying kernel as late observation at every one of the 3,900 population/treasury states in the finite domain. The grant, audit contract, retirement, birth time, and financing remain unchanged. The counterexample therefore concerns **raw immediate-cash evaluation versus a continuation-sensitive use of evidence**. It does not prove that later observation is inherently necessary or that short observation windows inevitably fail.

The calibration is supplied model knowledge. Learning it, verifying that it remains valid, or acting when two programs have indistinguishable early reports are different tasks. The paid-evaluator companion studies those distinctions with explicit interfaces and timing expenses.

## Softer copying and exact survival probabilities

Winner copying is not essential to the contrast. A second mechanism samples each newborn's parent independently, with probability proportional to the parent's measured cash. With `w_S,w_L` as the relevant scores,

\[
p_S=\frac{N_Sw_S}{N_Sw_S+N_Lw_L},
\qquad N'_S\sim\operatorname{Binomial}(M,p_S),
\qquad N'_L=M-N'_S.
\]

The birth count `M` is already fixed by real financing; the score assigns program labels to those funded births. Scores do not create cash. This independence is a substantive joint-copying assumption, not a consequence of knowing the marginal probability of each label.

With faithful copying, a pure L population is a persistent class, and pure S is doomed by the finite-potential argument. After any finite number of epochs, current pure-L probability is therefore a lower bound on eventual survival. Adding the still-mixed probability gives an upper bound. Exact rational propagation for 24 epochs yields:

| Evaluation rule | Certified interval for eventual nonextinction probability |
|---|---:|
| Raw early cash | 0.4553133970 to 0.4553135483 |
| Late cash | 0.6490735099 to 0.6490735989 |
| Calibrated early forecast | Identical to late cash |

The remaining interval width is unresolved mixed-population probability, not Monte Carlo error. These are eventual-survival bounds derived from absorbing classes, not merely the probability of being alive after 24 epochs. Even late evaluation has a positive chance of losing L through finite-population copying and then depleting.

The results also report expected population, expected S share conditional on nonemptiness, and the ratio of expected S count to expected total. The latter two quantities need not agree. Neither should replace the absolute funded counts.

## Variation can improve a finite horizon while changing the infinite result

Now let every paid copy independently switch its program label with probability `μ`. The child S probability is

`p'_S=μ+(1−2μ)p_S`.

This is symmetric variation between the two supplied rules. It can restore L after S fixation as well as introduce S into a pure-L population.

Under late weighted copying, the exact probability of extinction by epoch thirty is lower at `μ=0.01` than at `μ=0`; the [results](verification/funded-selection-results.json) retain both finite distributions. This does not establish an infinite-horizon advantage.

For the base financing and any fixed `0<μ<1`, **eventual extinction has probability one** in this bounded model. To see why, put `m=min(μ,1−μ)>0`. Every copied child has conditional probability at least `m` of being S. There are at most four children per epoch, so an all-S batch has conditional probability at least `m^4` whenever reproduction occurs. The potential is bounded by `260·4+259=1299`. One all-S batch followed by at most 109 all-S epochs forces extinction through the negative potential increments. Hence each block of 110 epochs has, conditional on prior survival, a uniformly positive extinction probability at least `m^440`. Repeated blocks give a survival probability tending to zero.

This conservative bound can be extraordinarily small; it is not a useful forecast of how soon extinction occurs. The conclusion depends on finite storage/sites, recurring independent variation, the absence of a guaranteed rescue channel, and the specified depleting S regime. Different joint copying, protected backups, immigration, or financing change the argument. The faithful-copy boundary `μ=0` has the positive survival probabilities above.

## Verification and scope

The [exact checker](verification/check_funded_selection.py), [full results](verification/funded-selection-results.json), and [population trajectories](verification/population-trajectories.csv) preserve the parent payment traces, population ledgers, and selection outcomes. Checks include 11,700 cash-ledger states and kernel rows, 3,900 late/calibrated-early equivalences, and 1,040 pure-L persistence and 1,040 pure-S decline states. Weighted copying is propagated by exact rational arithmetic. The infinite claims use the proofs, not extrapolation from a finite trace.

The checker reads the fourth-cycle plant implementation as a dependency without changing it. Its independent slot-level implementation and fixed-point verification remain in that earlier record. The current experiment adds actual variable population renewal rather than repeatedly normalizing contribution weights to a fixed population size.

What remains supplied is consequential: the two programs, score-to-copy rule, fixed two-cycle retirement, continuing per-parent grant, construction price, site and treasury limits, and available external feedstock. This is an explicit selection mechanism under a declared boundary. It neither establishes empirical institutional behavior nor derives ethical worth from persistence, growth, or popularity.
