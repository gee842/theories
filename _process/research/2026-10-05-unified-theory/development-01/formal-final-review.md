# Final proof review of formation mathematics

5 October 2026. Independent review of `theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FORMATION-MATH.md`.

Final reviewed SHA-256: `c65410ed0daf160c49c477efc16c7ed7bf0d1adf41983b77a9f852751ecf7ecf`.

**Verdict: ACCEPT. Both requested wording corrections have been applied and verified. No theorem blocker or mathematical counterexample was found.** The result is a conditional two-period game and exact accounting of prescribed paths; it is not an empirical law or an all-horizon institutional theorem.

## A15 and A16

The parameter class inherits K,m>0 and has ell>0, because 0<=o0<ell. The assumptions h>K+m and ell+m<=o<b imply that both safe participation and unblocked refusal preserve enough cash for last-period activation after an initially affordable build. A first blockade at the minimum construction cash instead leaves only ell. At that state the actor can pay baseline subsistence, but cannot activate, even if abandoning and rebuilding remain available.

The first-period allocation responses in the proof remain optimal when full continuation is considered. After S, b exceeds o and both possible receipts fund the same profitable last-period operation. After H, o exceeds ell and funds last-period operation while harmful participation cannot do better. After B, ell exceeds o0 and preserves at least the inactive continuation; refusal cannot create a more favorable future capability. This checks the dynamic best-response step that a static one-period comparison alone would not establish.

Consequently the persistent operator's comparisons are valid: repeated safeguarding gives 2(r−c), unblocked exit followed by safeguarding gives r−c, and a capacity-depleting first blockade gives 2r−chi. The strict inequalities chi<2c and r>chi make the last uniquely preferable. At the participant's initial choice, early activation is inferior to inactivity, while delayed activation yields positive gain h−K−m. Early dormant construction and late construction have the same final value. Thus the theorem correctly identifies the date of **activation**, not a unique physical construction date.

For arbitrary real reserves, write d=w−(K+m+ell). In the middle region, 0<=d<m; blockade leaves ell+d, which is still below the activation prefix ell+m. In the upper region d>=m, blockade leaves at least ell+m and therefore loses its special continuation benefit. Every first-period operator action then has continuation value r−c; the strict current cost comparison selects S. Immediate operation adds h−m>0 relative to postponement. This reasoning covers continuous reserves, not merely the discrete enumerated grid.

Below the initial activation threshold, paying for dormant construction cannot help: if it is affordable, it lowers cash by K but does not raise inactive receipts, which exactly replace subsistence. The later activation bill therefore remains unaffordable. The region should not be described as forbidding all physical construction; it forbids completing a path to funded operation under these choices.

The exact boundary inclusions in A16 are correct. At W_aff activation first becomes affordable, but its blockade continuation is still unfunded. At W_res the blockade continuation becomes funded, changing the operator's strict choice. Those financing equalities do not themselves create an operator payoff tie, because c<chi<r remains strict.

## Prefix and handoff proofs

A9 is necessary and sufficient for the **specified** path of immediate installation and T>=1 consecutive active episodes. After setting aside K, opening balances are w0−K+tq; requiring every such balance to cover m+ell yields the minimum at an endpoint. Nonnegative receipts then ensure no uncounted post-payment deficit. This does not prove that the prescribed path is privately optimal or that no other feasible policy exists below its threshold.

A13 is correct for a **mandatory, regular, stationary** handoff fee J>=0 every L>=1 active episodes, starting at a handoff. A nonnegative block drift Lq−J implies q>=0, so the largest required prefix is the first bill J+m+ell. Negative block drift eventually exhausts every finite starting reserve. Optional idle intervals, cheaper rebuilding, changed opponents, or changed receipts are different policies; the following paragraph appropriately preserves those choices rather than promoting A13 to their universal feasibility condition.

The stationary profitability comparison A6 and its earliest-feasible-date argument are sound under the stated executable stationary continuation. They do not supply liquidity or a no-credit financing instrument.

## Completed wording corrections

1. Section 1 now restricts zero-payoff refusal to H followed by refusal and explicitly retains already-paid S/B costs if the participant refuses. The protocol and solver already implemented this correctly, and the proved parameter class gives participation after S/B, so the correction does not change A3/A15/A16.
2. A11 now describes the earliest **combined installation-and-activation** date under continued inactivity. Dormant construction may be affordable earlier at K+ell. A15/A16 distinguish activation from dormant construction correctly.

## Independent supplemental checks

The separate [rational-case checker](formal_adversarial_check.py) uses the previously independently implemented decision tree, without invoking the coordinating implementation. It tested 150 rational parameter families satisfying A15, each with seven initial-cash locations and both operator horizons: 2,100 cases. Locations include both exact reserve boundaries, fractional points inside the middle region, and lower/upper controls. Every selected activation pattern, participant value, and protected active-period outcome matched A15/A16. [Results](formal-adversarial-checks.json) retain the deterministic seed and counts.

These finite tests supplement the proof audit. The acceptance concerns the explicit mechanism and assumptions; it does not establish empirical adequacy, originality of game-theoretic ingredients, or protection against an enlarged interference repertoire.

## Companion report check

I also inspected `FORMATION.md`, the experiment `README.md`, and the recorded `results/summary.json`. Reported totals agree: 1,152 parameter cases, 9,216 policy runs, 2,304 operator-tie sensitivity runs, 97 tie-sensitive environments, and participant value lower/equal under persistence in 85/1,067 grid cases. The reports appropriately avoid generalizing those counts to a universal effect of patience. The heuristic policies, fresh-operator receipt totals, zero-continuation cessation convention, absence of empirical validation, and distinction between delayed operation and physical construction are explicit. No additional overclaim requiring correction was found in this focused read.
