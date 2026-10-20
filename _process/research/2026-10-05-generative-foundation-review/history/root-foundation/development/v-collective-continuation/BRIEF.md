# V: what a collective's continuation needs (brief for V1–V5)

Item V, claimed on the work board 19 October 2026. Origin: Ren pasted an eight-constraint account
of social viability (material reproduction; local gain rewarded against the whole; true information
flow; cooperation among strangers; bounded conflict; feedback on power; stability with
adaptability; forming the next generation; and, unifying them, keeping the capacity to correct) and
asked whether the theory covers it. The answer (this session) found constraints 1–3, 6 and the
correction point covered by spine laws, constraints 4, 5, 7 and 8 partial or missing, and five
pushbacks. Ren: "please, spawn a swarm of subagents, think hard, let's fully complete this", then
"I agree with your push back, let's think about how to resolve them elegantly".

This brief fixes the five new core modules. Each states laws of one unfolding in the core's
vocabulary, no social word in a Lean name, and no premise beyond what each law names.

## Rules for every module (non-negotiable)

- **Pure core.** The module lives in the Lean package `Becoming`
  (`experiments/integrated-correction/general-framework/generative-basis/lean/becoming/`). It imports
  only `Becoming.*` modules (and through them `GenerativeCore`). No Mathlib, no `Std`, no `Lean`.
- **Empty axiom report for every declaration.** No `propext`, `Quot.sound`, `Classical.choice`.
  So: no `simp` / `simp_all` / `omega` / `decide` on Props built with `↔`-rewriting / `by_cases` on an
  undecided Prop / `funext` / `Classical`. `rfl`, `match`, `cases`, `induction`, `exact`, `refine`,
  `intro`, `constructor`, `Nat.*` lemmas whose own axiom report is empty are fine. Several `Nat`
  library lemmas use `propext` (for example `Nat.add_sub_of_le`, `Nat.le_of_add_le_add_right`):
  prefer the core's own versions (`grep -rn "theorem add_sub_of_le" Becoming/`) or prove the fact by
  induction. Never compare Prop-valued functions by `=`; state pointwise `↔` instead.
- **Build and audit** with the shared-cache scratch builder, always with an ABSOLUTE tree path:
  `cd <package> && python3 -B scratch_build.py <ABSOLUTE tree dir>` . It compiles the module against
  the checkout and prints each declaration's axioms. Done means: compiles with no error and no
  warning, and every declaration's axiom report is empty. `LEAN_TIMEOUT=3600` if the machine is busy.
- **Write only inside your own tree dir** (given below). Do not edit any file of the checkout, the
  board, records, chapters or studies. Do not commit. Do not run the checker (`check_becoming.py`).
- **Base family.** The connectivity measure counts a theorem as "apart" unless it is stated on the
  base (a `Process`/`Run`/`Law.orbit` course, or `World`/`Flow`/`Web`). State every main law on a
  course of a law of change (`Law.orbit next s n`, a `Run P`, or `Viability`/`Keeping` notions) or on a
  `Web`/`Flow`. A helper lemma about lists or numbers is fine, but each main law must be about a
  course or a web.
- **Reuse, do not rebuild.** Read the modules named for your item first and build on their
  definitions (`Law.orbit`, `Law.lost_stays`, `Identification.StatesBelow`, `prefix_short_twice`,
  `bounded_agree`, `Viability.Kernel`, `Keeping.KeptFor`, `Web.Whole`, `Web.Brief`, `Covered.*`,
  `Loops`, `Frequency`, `Capture`'s `Law.perturbation_reabsorbed`, `Labelled.class_belongs_to_the_run`).
  Where an existing law already says something, cite it in the docstring and state the relation
  (an instance theorem), never reprove it.
- **Style.** Match a recent module (`Becoming/Rejoining.lean`, `Becoming/Cuts.lean`): a module
  docstring `/-! # Name: one line … -/` with bullets naming each law and its declaration in
  backticks, then sections, each theorem with a `/-- **Bold one-line law.** explanation -/`
  docstring. English only. Vocabulary: formation, condition, step, course, run, law (of change),
  configuration, gives, takes, couples into, loop, return. No "trust", "society", "conflict",
  "power", "agent", "interest", "rights", "good", "bad", "should" in Lean names or docstrings; the
  chapter carries the readings. Names state the structure exactly.
- **Exactness.** Where a bound is claimed exact, prove both sides (a witness for the other side).
  Every witness is a small concrete inductive type with explicit cases.
- **Report back**: the tree path, the module name, theorem count, the list of main theorems with
  their exact statements (one line each, Lean), the scratch_build tail showing the empty axiom
  reports, and anything in the brief that turned out false or had to be changed, with why.

## V1 `Becoming.Withholding` — giving that waits on giving (constraint 4)

Tree: `development/v-collective-continuation/v1/Becoming/Withholding.lean`.
Read first: `Recurrence.lean` (`Law.orbit`, `lost_stays`), `Loops.lean` (module docstring),
`Capture.lean` (`Law.perturbation_reabsorbed`).

Setting: formations `α`; `up : α → α → Prop`, `up b a` read "a's giving waits on b's". A
configuration is `α → Prop` (who gives at a step). Two laws of change on configurations:
- `waitsAll up s a := s a ∧ ∀ b, up b a → s b` (keeps giving while it and all it waits on gave);
- `answers up s a := ∀ b, up b a → s b` (gives exactly where all it waits on gave at the step before).
Chains: `Chain up : Nat → α → α → Prop` (exactly `k` waits from `b` to `a`; length 0 is `b = a`),
`Within up k b a := ∃ j, j ≤ k ∧ Chain up j b a`.

Laws (the courses are `Law.orbit (waitsAll up) s n`, `Law.orbit (answers up) s n`):
1. closed form, with memory: gives at `n` ↔ every `b` within `n` of `a` gave at the start;
2. withholding stays: with memory, a formation withholding at `n` withholds at every later step;
   giving at `n + 1` implies giving at `n` (no course of this law regains giving);
3. withholding spreads downstream: `¬ s b`, `Chain up k b a`, `k ≤ n` ⇒ `a` withholds at `n`;
4. one withholding ends all giving in a family reached from it: `∀ a, Within up d b a`, `¬ s b` ⇒
   every formation withholds at every step from `d` on;
5. closed form, without memory: gives at `n` ↔ every `b` with a chain of exactly `n` to `a` gave at
   the start;
6. where no loop, withholding passes out: if there is no chain of length `L` (hence none longer),
   then without memory every formation gives at every step from `L` on, whatever the start;
7. on a loop, withholding returns: `Chain up p b b`, `0 < p`, `¬ s b` ⇒ without memory `b` withholds
   at every step `k * p`;
8. more waiting, less giving: `up ⊆ up'` ⇒ giving under `up'` implies giving under `up` at every
   step, for both laws (each added wait on another's giving is one more way withholding arrives);
9. restoring needs another law: a witness `Ring` (three formations, each waiting on the one before)
   where from one withholding at the start: with memory all withhold from step 2 on, for good;
   without memory the withholding circulates, returning to each formation every 3 steps; and under
   the law in which one formation gives at every step whatever it waits on (`givesFirst`), all give
   at every step from step 2 (or the exact step) on.
State law 4 and 7 as the module's headline: the absorbing course and the returning one.

## V2 `Becoming.Widening` — whether a loop closes, keeps or widens a difference (constraint 5; answers chapter §7.7 "which law closes rather than widens a difference")

Tree: `development/v-collective-continuation/v2/Becoming/Widening.lean`.
Read first: `Recurrence.lean` (`Law.orbit`), `Loops.lean` and `Frequency.lean` docstrings
(`runaway_of_returns`, `Frequency.Sparse.polynomial`), `Rejoining.lean` docstring.

Setting: a return map `f : Nat → Nat` (the difference that comes back after one turn around a
loop, for the difference sent); a loop of links `links : List (Nat → Nat)` has the composed return
map `returnMap links`. Course: `Law.orbit f d n`, the difference after `n` turns.
Laws:
1. answering in kind keeps a difference: `∀ x, f x = x` ⇒ the difference is `d` at every turn;
2. **closing needs a link that gives back less than it received**: if every link `g` of the loop
   has `∀ x, x ≤ g x`, the difference after every turn is at least `d`; so a loop that closes a
   positive difference has some link and some `x` with `g x < x`;
3. a return map below what it receives closes within `d` turns: `f 0 = 0`, `∀ x, 0 < x → f x < x`
   ⇒ `Law.orbit f d d = 0`, and `0` from then on;
4. compensation closes: `f x = x - c` gives `d - n * c` after `n` turns (closes once `n * c ≥ d`);
5. a cut closes at once: a link returning nothing makes the difference `0` from the first turn,
   whatever the other links;
6. monotone return maps settle or rise: `f` monotone, `f d ≤ d` ⇒ the course never rises and
   settles within `d` turns at a value `v` with `f v = v`; `f` monotone, `d ≤ f d` ⇒ it never falls;
7. doubling links run away: every link with `∀ x, x + x ≤ g x` ⇒ after `n` turns at least
   `2 ^ n * d` (state the relation to `Frequency`'s `runaway_of_returns` in the docstring);
8. **whole-number strengths have nothing between**: links `x ↦ a_i * x`; with product `P` of the
   strengths: `P = 0` closes at the first turn, `P = 1` keeps `d` at every turn, `P ≥ 2` exceeds
   every bound (for `d > 0`). So with whole-number strengths a loop that closes gradually needs a
   link that is not a multiplication (law 4). Exact: give the three cases as one theorem.

## V3 `Becoming.Pace` — how fast a rule may change (constraint 7)

Tree: `development/v-collective-continuation/v3/Becoming/Pace.lean`.
Read first: `Recurrence.lean` (`lost_stays`, `merged_stays`, `Merges.loses`), `Identification.lean`
(`StatesBelow`, `bounded_agree`, `prefix_fixes`, `prefix_short_twice`, `bounded_agree_exact`),
`Capture.lean` (`Law.perturbation_reabsorbed`).

Setting: a two-level course: a fast configuration `x : S` and a rule `g : R`; the fast level steps
by the rule, `x (t+1) = f (x t) (g t)`; the rule changes only at reading steps,
`g (t+1) = if reads t then h (x t) (g t) else g t` (`reads : Nat → Bool`). Define the course
recursively (`paced f h reads (x0, g0) t`), and show it is a `Law.orbit` of a law on `S × R × Nat`
(or state it as a `Run` of a process), so it sits on the base.
Laws:
1. **rigid**: under one law, a configuration lost stays lost (cite `lost_stays`), and a rule that
   never reads (`reads t = false` for all `t`) keeps one rule for good, so two courses whose fast
   configurations differ have the same rule at every step: nothing the fast level meets reaches
   the rule;
2. a fast difference reaches the rule only at a reading step: two courses with the same rule at
   the start and the same `reads` have the same rule at every step up to and including the first
   reading step;
3. **regaining needs a change of rule**: a witness on `Bool` where each of two fixed laws loses a
   configuration for good, and the course that changes rule regains it;
4. **dissolving**: a rule held for a stretch shorter than `2N − 1` does not fix the course it
   generates: for every `N ≥ 2` two fast courses, each with at most `N` states, agree over a stretch
   of `2N − 2` steps and differ after it (instance of `prefix_short_twice`, read as two rules each
   held over the stretch);
5. **held long enough, it is fixed**: two fast courses each with at most `N` states that agree over
   a stretch of `2N − 1` steps agree at every step (instance of `bounded_agree`); so a rule held for
   at least `2N − 1` steps between reading steps is fixed, within its stretch, by the first
   `2N − 1` steps — exact by law 4;
6. the pace law as one theorem: for courses with at most `N` states, a stretch of length `L` fixes
   the course it is in, for every pair, exactly when `L ≥ 2N − 1`.
Headline: a rule that never changes loses what it merges; a rule that changes faster than `2N − 1`
steps cannot be fixed from its own stretch; between them, a slow level that reads the fast one at
stretches of at least `2N − 1`.

## V4 `Becoming.Passing` — a pattern across brief carriers (constraint 8)

Tree: `development/v-collective-continuation/v4/Becoming/Passing.lean`.
Read first: `Wholes.lean` (`Web.Whole`, `Web.Covered`, `Web.Brief`, `Covered.arises_within`,
`Covered.needs_arising`, `Whole.covered`), `Transmission.lean` and `Evolution.lean` docstrings,
`Descent.lean` docstring.

Setting on a `Web` (or `World`): `carries : Nat → α → Prop` with `carries t a → active t a`; the
pattern is present at `t` where some formation carries it. `passes : Nat → α → α → Prop`
(`passes t b a`: at step `t`, `b` gives the pattern to `a`). The passing premise (`ByPassing`): a
formation carrying at `t + 1` carried at `t` or was passed it at `t` by a carrier at `t`.
Laws:
1. a lasting pattern of brief carriers needs new carriers: carriers brief for `d` (none carries at
   two steps `d` apart) and the pattern present at every step from `T` ⇒ a carrier begins within
   every `d` consecutive steps (relate to `Covered.arises_within` by an instance on the web whose
   activity is carrying);
2. **under the passing premise, the pattern lasts only through passing**: present at every step from
   `T`, carriers brief for `d` ⇒ within every `d` consecutive steps some carrier passes it;
3. **one empty step ends it**: under the passing premise, if no formation carries at `t`, none
   carries at any later step;
4. **if passing stops, it ends within one span**: under the passing premise, carriers brief for `d`,
   nothing passed from step `T` on ⇒ no formation carries at any step from `T + d` on;
5. witness `Relay`: carriers each carrying for two steps, a new carrier passed the pattern at every
   step: the pattern is present at every step and no carrier lasts; the same with passing stopped
   at `T`: present at `T + 1`, absent from `T + 2` on (exact for law 4 with `d = 2`).
Docstring note: passing carries whatever pattern it carries; nothing here says which patterns are
worth passing.

## V5 `Becoming.JointKeeping` — conditions kept together, and keeping a part (pushbacks 1 and 3)

Tree: `development/v-collective-continuation/v5/Becoming/JointKeeping.lean`.
Read first: `Viability.lean` (`Kernel`, `Certificate`, `Kernel.mono`), `Keeping.lean` docstring,
`Labelled.lean` around `class_belongs_to_the_run` (the `Renewable` example) and `Renewal.lean`
docstring.

Laws:
1. **every course: conditions decompose exactly**: `Kernel P (fun s => g₁ s ∧ g₂ s) s ↔ Kernel P g₁ s ∧
   Kernel P g₂ s`, and for a list of guards;
2. **some course: they do not**: `Keepable P g s := ∃ r : Run P, r.state 0 = s ∧ ∀ n, g (r.state n)`.
   Jointly keepable ⇒ each keepable; witness `Fork`: a configuration from which `g₁` is keepable and
   `g₂` is keepable but not both together;
3. **no rule on the separate answers decides the joint one**: for every `F : Bool → Bool → Bool`,
   and decisions `k₁ k₂ kj : S → Bool` of keepability of `g₁`, `g₂`, and both, on the witness
   process, `¬ ∀ s, kj s = F (k₁ s) (k₂ s)` (two configurations with both conditions keepable, only
   one jointly keepable). So a product, or any function, of separate viabilities does not decide
   joint viability where continuation goes through choices; "any factor zero ⇒ zero" is law 2's
   first half and is all that holds in general;
4. **keeping a part is not renewal**: in `Labelled`'s renewable process, from one configuration,
   the focal formation's activity lies in the kernel of the guard "focal active" (no course leaves
   it), while one run from that configuration is renewing and another consumes the condition of the
   sustaining formation, which ends (from `class_belongs_to_the_run`). Read: a formation's
   continuation, kept under every course, decides neither renewal nor what it does to others;
5. (optional, if natural) finite-horizon form with `Keeping.KeptFor`: kept jointly for `n` steps ⇒
   each kept for `n` steps, and the witness shows the converse fails at `n = 1` or `2`.
