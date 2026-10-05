# A common constraint with different outcomes at different scales

This model connects scale, shared correction capacity, payment chronology, recurring production, and the expense of maintaining an interface. It extends the second cycle's ample-reserve scheduling example. It is a supplied mechanism with exact consequences, not an empirical scaling law or a claim of mathematical novelty.

## The physical assumptions

There are `n ≥ 1` modules and a fixed installed number `1 ≤ k ≤ n` of diagnostic channels. A fault wave affects every module. Every module has a fresh hidden binary condition; all joint assignments are admitted. Guaranteed repair requires its perfect diagnosis, authorization, and indicated execution, in that strict order. Each stage lasts one slot and costs one unit per module. Diagnosis uses one of the `k` channels; the other stages have sufficient independent parallel capacity. There are no substitute routes or informative side channels.

A stage can use another stage's result only in a later slot. Paid diagnosis supplies a free, reliable register **within that episode**. The separate [succession study](paid-memory-and-succession.md) charges for retained evidence; this scheduling model does not.

All production stops until every module has been repaired. Healthy gross production is `y` per module per slot, from explicitly external feedstock. Operating expense is `c ≥ 0` per module per slot, including outage slots. Let `p=y−c` be healthy net production before diagnostic-channel maintenance; `p` can be signed, while `y ≥ 0`. Each installed channel costs `u ≥ 0` to maintain in every slot, healthy or faulty. Installed channels cannot be suspended or liquidated in this comparison.

A fault can occur immediately. Later fault onsets are at least `Δ ≥ 0` slots apart; arbitrarily long quiet intervals are also admitted. Every wave must finish within `H ≥ 1` slots of onset. Faults are initiated only when the system is healthy; if the minimum spacing has already elapsed when repair finishes, the next slot may start another wave. This excludes overlapping waves during an existing outage.

The carried-cash cap is `B` and initial carried cash is `b₀ ≤ B`. A healthy slot receives gross production before paying its expenses, then spills any remainder above `B`. An outage slot receives no production, including the completion slot, and must prepay all that slot's expenses. There is no borrowing or accessible outside cash balance. Failure means a missed payment or a missed repair deadline. Temporary loss of production during an outage is allowed.

The controller chooses every stage allocation from available information. The environment chooses fault timing and fresh hidden causes. The guarantee quantifies over **every admitted environment history**, with no probability distribution or stationary-adversary restriction.

## S3.1 — An exact fixed-design criterion

For a fixed design `(n,k)`, define

\[
T=\left\lceil\frac nk\right\rceil+2,
\qquad
C=3n+(cn+uk)T,
\qquad
q=pn-uk,
\qquad h=\max\{\Delta-T,0\}.
\]

`T` is minimum repair duration. `C` is the total expense of that fastest repair. `q` is the healthy per-slot cash increment before capping. `h` is the smallest number of healthy earning slots between successive fastest repairs.

**There exists a controller that remains solvent and completes every repair forever if and only if**

\[
\boxed{b_0\ge C,\quad B\ge C,\quad T\le H,
\quad q\ge0,\quad hq\ge C.}
\]

The separate cap inequality is redundant when `b₀ ≤ B` and `b₀ ≥ C`, but is retained to distinguish storage capacity from starting cash in design comparisons. Here `C ≥ 3n > 0`, so the replenishment inequality also implies `q>0` and `Δ>T`; these stronger consequences need not be separate premises.

**Duration and episode cost.** Every module must be diagnosed to guarantee its matching action. The last diagnosis cannot finish before slot `ceil(n/k)`; that module then needs two additional slots. A batched pipeline attains the bound. Every successful repair pays `3n` stage fees and at least `T` slots of operating and channel expenses. Since there is no outage income and every expense is nonnegative, initial cash `C` covers every internal payment prefix of that fastest pipeline.

**Necessity of starting support and deadline.** The environment may fault immediately. No schedule costs less than `C` or finishes sooner than `T`. Thus `b₀≥C` and `T≤H` are necessary.

**Necessity of quiet solvency.** If `q<0`, an arbitrarily long quiet interval exhausts any finite carried cash. The controller has no permitted deactivation route to avoid this expense.

**Necessity of replacement.** Choose faults as early as permitted after each completion. A repair of duration `t≥T` costs `C(t)=3n+(cn+uk)t` and leaves at most `max(Δ−t,0)` healthy earning slots. When `q≥0`, its uncapped cycle increment

\[
D(t)=\max(\Delta-t,0)q-C(t)
\]

is nonincreasing in `t`. If `D(T)<0`, every admitted schedule loses at least the same positive amount on each such cycle. A finite reserve cannot finance infinitely many cycles. Capping cash can only discard surplus, not cure this deficit. The argument permits a different schedule every cycle; it is not restricted to a stationary scheduler.

**Sufficiency.** Use the fastest pipeline after every fault. If fault-onset cash is at least `C`, all payments and the deadline are met. After the next minimum quiet interval, onset cash is at least

\[
\min\{B,\ b-C+hq\}\ge C.
\]

Longer quiet intervals do not harm solvency when `q≥0`. Induction gives the guarantee for every allowed fault sequence. If faults eventually stop, quiet solvency remains safe.

## S3.2 — Too little and too much fixed infrastructure can both fail

Take `n=8`, `c=1`, `p=4`, `u=2`, `Δ=8`, and `H=6`. For the table, choose ample storage and starting cash so only deadline and repeatability remain at issue.

| Channels `k` | Repair slots `T` | Repair expense `C` | Healthy increment `q` | Minimum replenishment `hq` | Can sustain every allowed sequence? |
|---:|---:|---:|---:|---:|---|
| 1 | 10 | 124 | 30 | 0 | No: deadline and replacement |
| 2 | 6 | 96 | 28 | 56 | No: replacement |
| 3 | 5 | 94 | 26 | 78 | No: replacement |
| 4 | 4 | 88 | 24 | 96 | Yes, with `b₀,B ≥ 88` |
| 5 | 4 | 96 | 22 | 88 | No: replacement |
| 6 | 4 | 104 | 20 | 80 | No: replacement |
| 7 | 4 | 112 | 18 | 72 | No: replacement |
| 8 | 3 | 96 | 16 | 80 | No: replacement |

Only four channels sustain this regime. A fifth channel incurs unavoidable upkeep without reducing the four-slot repair time. Eight channels finish faster but consume too much recurring support. No larger finite initial reserve changes those deficit conclusions.

This does not contradict the fact that adding optional costless actions cannot reduce feasibility. An installed channel here has an unavoidable maintenance expense. If unused channels can be shut down for free, or partially repaired modules resume production, this is a different physical model and the table must be recomputed. The result predicts neither that centralization is generally good nor that four is a universal optimal size.

## S3.3 — The invariant relation and the changing scale parameters

Put `r=k/n`, the number of channels per module. Dividing all balances by `n` gives

\[
T=\lceil1/r\rceil+2,
\quad C/n=3+(c+ur)T,
\quad q/n=p-ur.
\]

The condition takes the same form at every integer size. Exact proportional replication `(n,k,B,b₀) → (an,ak,aB,ab₀)` for a positive integer `a` preserves `r`, repair duration, and feasibility. Expenses and cash flows scale by `a`. This is a physical replication result under the stated independence and shared-interface assumptions, not just a relabeling of units.

Increasing `n` while holding `k` fixed changes `r` and eventually violates a fixed deadline. More generally, any sequence with `k(n)/n → 0` eventually fails every fixed finite deadline, because `ceil(n/k(n))+2` diverges. This includes positive sublinear channel growth. The exact timing requirement is

\[
H\ge3,\qquad k\ge\left\lceil\frac{n}{H-2}\right\rceil.
\]

Infrastructure that grows proportionally can preserve timing, but it must still meet the maintenance and replenishment constraints. Scaling the count of channels by itself does not scale the outside feedstock, rights of access, memory, or other unmodeled inputs.

For a fixed batch count `m=ceil(1/r)`, let `T=m+2`. When `u>0` and `Δ>T`, replenishment is equivalent to

\[
r\le \frac{p(\Delta-T)-cT-3}{u\Delta}.
\]

This upper bound must be intersected with the batch interval `1/m ≤ r < 1/(m−1)` for `m≥2` (or `r=1` for `m=1`), the deadline, storage, and initial-cash constraints. The lower timing bound and upper expense bound can conflict or leave a band of viable ratios.

In the preceding parameter regime, the complete viable ratio band, before cash constraints, is

\[
\boxed{\tfrac12\le k/n\le\tfrac9{16}.}
\]

To check completeness: batches `m≥5` miss the deadline; `m=4` has negative available replacement margin; `m=3` requires `r≤1/4` despite `r≥1/3`; `m=1` requires `r≤7/8` despite `r=1`; `m=2` gives the displayed band. Integer channel counts matter: one module has no viable design in this supplied regime; two modules can share one channel; eight require four; sixteen admit eight or nine. These outcomes follow from the same relation.

The low-size failure does not mean an isolated module is impossible in nature. It means this combination of indivisible apparatus, fees, wave spacing, all-system shutdown, and feedstock has no viable isolated implementation.

## S3.4 — Installation changes which viable design is affordable

Suppose each channel costs an additional `F≥0` to install before the first fault, installation takes zero modeled time, and total initial liquid endowment is `W`. Existing production modules are supplied assets; their construction is outside this comparison. After buying the channels, carried cash is `min(B,W−Fk)`; inaccessible overflow is lost, not held in an external bank.

For a recurrently viable design with `B≥C`, minimum endowment is

\[
W_{\min}(n,k)=Fk+C(n,k).
\]

The least-cost feasible fixed design minimizes this expression over the viable integer `k`. This optimizes a supplied financial objective; it does not explain how a real selector discovers or chooses the design.

For `n=8`, retain `c=1,p=4,Δ=8,H=6` but lower maintenance to `u=1`. With ample storage, viable `k` are three through eight. An installation price `F=1` makes four channels least expensive, requiring `W=76`. At `F=10`, three channels are least expensive, requiring `W=109`. Faster recovery is not the only determinant of the chosen financial optimum. Changing the objective to downtime loss, tail risk, or equitable access can select a different design.

## S3.5 — Feasibility does not determine the implemented selection

Use the same eight-module process and allow a design selector to choose the fixed channel count before operation. Give it sufficient starting endowment and storage for any candidate first repair; keep the protection test and fault class unchanged. Two explicit rules give different realized regimes:

- A rule minimizing repair duration chooses `k=8`. Every repair is individually quick, but the earliest recurring waves remove at least sixteen cash units per cycle (`C−hq=96−80`). Any finite reserve eventually fails under that admitted environment.
- A rule choosing a recurrently viable design chooses `k=4`, the only viable choice here. With at least 88 carried units it meets every admitted wave indefinitely.

Both are supplied selection mechanisms on the same design menu. Their different outcomes follow from their objectives interacting with the same physical constraints. The second rule assumes access to correct model parameters and computation; it does not explain how a real system learns or adopts that rule. A fastest-repair rule can also succeed in another parameter regime. Its failure here is a concrete counterexample to equating a favorable local performance measure with a continuing global guarantee.

## Verification and limits

The [standard-library checker](verification/check_integrated_scale.py) computes the greatest safety fixed point for 24 small games, covering 30,536 enumerated states. It allows all stage allocations, including idle slots, and every permitted quiet/fault choice. It compares the exact minimum initial cash with the analytic criterion, including insufficient storage, signed quiet return, onset spacing, and deadline boundaries. It also checks 2,080 scale/design rows and 108 exact proportional replications. [All assertions passed](verification/integrated-scale-results.json); the [frontier data](verification/integrated-scale-frontier.csv) retain all rows.

The game uses symmetry of identical modules and supplies concrete correct execution through the paid diagnostic registers. It does not infer hidden faults from the analyst's state. The finite game checks are a computational cross-check of the proof within this model; they are neither empirical validation nor a machine proof for all parameter values.

The assumptions carrying the strongest empirical burden are synchronized fault waves, all-system production shutdown, externally supplied feedstock, fixed non-suspendable infrastructure, perfect diagnosis, and the strict repair workflow. Relaxing them is a legitimate next model, not an exception to the accounting constraints. A proposed real-world application must measure those mechanisms independently before importing the frontier.
