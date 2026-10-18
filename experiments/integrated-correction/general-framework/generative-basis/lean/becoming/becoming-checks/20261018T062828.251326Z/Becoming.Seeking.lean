import Becoming.Locality
import Becoming.Recurrence

/-!
# Seeking: the boundary condition for 无明

On 10 October 2026 Ren called the fight to be "the biggest that dominates" mammalian: "the
seeking system got locked in, what they are pursuing is illusion (in south asia and Buddhism)",
and asked that the boundary condition for 无明 be found and proved. On 11 October Ren gave the
go: "yes let's do 无明". This module states, with no axiom and no premise beyond what each law
names, where seeking can come to rest at enough and where it cannot.

Seeking is read as activity directed toward a target met at a state, and the target as formed
within the unfolding, not given from outside. That formation is not modelled here: a target is
any condition on the configuration, the seeker's own or the others'.

* **B1. Enough.** A target met at a state the law leaves unchanged is met at every later step,
  at rest (`Law.fixed_rests`). Under a determined law, seeking comes to rest with its target met
  exactly when it reaches such a state (`Law.rests_iff`): the boundary of enough. A target of
  "more than now", a quantity of one's own that rises across each step, is met only by change
  (`more_not_at_rest`, `Law.more_never_rests`). Met at every step it makes every configuration
  new (`more_new`), so no list holds them and it needs an open world (`more_needs_open`, an
  instance of `unlisted_of_new`); counting on meets it (`succ_more`). A target of "above all
  others" is met at a state by at most one seeker (`aboveAll_unique`), so never by two at once
  (`aboveAll_not_two`); under any law, no state left unchanged meets it for two seekers
  (`Law.aboveAll_never_rests`).
* **B2. Expansion or exhaustion.** Where what stands is listed at each step
  (`Web.StandingCensus`), a seeker whose own standing rises at arbitrarily late steps needs, at
  arbitrarily late steps, steps across which what stands does not run down: drawing from beyond
  what it closes over, or exchange that does not dissipate (`Flow.more_needs_unrun`, from
  `Flow.change_recurs_iff`). Where what stands runs down at every step from some step on, its
  rises do not recur: the pursuit ends by exhaustion, not by reaching enough
  (`Flow.more_exhausted`).

**B3 and B4 are theorems already on the spine** and are read here, not restated:
- *B3, feedback.* Losses reach a seeker only through what it registers (识). Through support
  they register only where its cumulative net draw passes the margin
  (`Flow.Balances.supported_iff_within_margin`); below the threshold a difference stays until
  support diverges (`Flow.subthreshold_alike`); before the break, how far off the break is does
  not register (`Web.break_not_bounded`); where the cost falls beyond the registration closure
  (识闭包), no mark ever comes (`Flow.uncoupled_beyond_coupling`).
- *B4, seeing (明).* What support does not mark, measurement marks
  (`Web.observed_raise_couples`), as do a model answerable to what is registered
  (`Flow.excludes_tail_within`) and another formation's registration (`Clearing.pooled`). What
  one's own act does is fixed only where the configuration returns, under a model of what is
  irrelevant (`Run.fixes_on_return`, `Run.generalizes`).

**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D26).** 无明
is the not-seeing that keeps seeking locked onto a target that cannot be met at rest:
"more than now", or "above all others" among two or more. Its boundary is B1: seeking can rest only
where its target is met at a state the unfolding leaves unchanged. B2 is what such seeking does: it
needs a beyond, and where there is none it ends by exhaustion. B3 says why the locked seeking is not
corrected by its own feedback, and B4 what corrects it. Dominance as such is not the target ruled
out: power held within an order that meets its targets, regulated, or taken by one who understands
when order cannot be agreed, serves a target that can be met. Hijacking (B5), the formation and
transmission of such targets, is not stated.

What is not derived: how a target forms or is revised; that a seeker pursues it; which targets
actual formations hold. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

universe u

variable {S : Type u}

/-! ## B1. Enough -/

/-- The quantity `q` rises across the step from `n` along `g`: a target of "more than now" is
met there. -/
def MoreThanNow (q : S → Nat) (g : Nat → S) (n : Nat) : Prop :=
  q (g n) < q (g (n + 1))

/-- `g` rests across the step from `n`: the configuration does not change. -/
def RestsAt (g : Nat → S) (n : Nat) : Prop :=
  g (n + 1) = g n

/-- **More than now is met only by change.** -/
theorem more_not_at_rest {q : S → Nat} {g : Nat → S} {n : Nat} (more : MoreThanNow q g n) :
    ¬ RestsAt g n :=
  fun rests => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le more (Nat.le_of_eq (congrArg q rests)))

/-- Met at every step from `N`, more than now raises the quantity between any two later steps. -/
theorem more_rises {q : S → Nat} {g : Nat → S} {N : Nat} (more : ∀ n, N ≤ n → MoreThanNow q g n) :
    ∀ {i : Nat} (d : Nat), N ≤ i → q (g i) < q (g (i + (d + 1)))
  | _, 0, le => more _ le
  | _, d + 1, le => Nat.lt_trans (more_rises more d le) (more _ (Nat.le_trans le (Nat.le_add_right _ _)))

/-- **Met at every step, more than now makes every configuration new.** -/
theorem more_new {q : S → Nat} {g : Nat → S} (more : ∀ n, MoreThanNow q g n) :
    ∀ i j, i < j → g i ≠ g j :=
  fun i _ lt same =>
    match gap_of_lt lt with
    | ⟨d, at_j⟩ => Nat.lt_irrefl (q (g i)) (Nat.lt_of_lt_of_le
        (more_rises (N := 0) (fun n _ => more n) d (Nat.zero_le i))
        (Nat.le_of_eq (congrArg q ((congrArg g at_j).symm.trans same.symm))))

/-- **More than now, met at every step, needs an open world**: no list holds the configurations
it passes through. An instance of `unlisted_of_new`. -/
theorem more_needs_open {q : S → Nat} {g : Nat → S} (more : ∀ n, MoreThanNow q g n) :
    ¬ ∃ l : List S, ∀ n, g n ∈ l :=
  unlisted_of_new (more_new more)

/-- Counting on meets more than now at every step, in an open world. -/
theorem succ_more (s : Nat) : ∀ n, MoreThanNow id (Law.orbit Nat.succ s) n :=
  fun n => Law.succ_open.2.2.2 s n

/-- Seeker `i` stands above all others at `s`: every other seeker's quantity is below its own. -/
def AboveAll {I : Type} (q : I → S → Nat) (i : I) (s : S) : Prop :=
  ∀ j, j ≠ i → q j s < q i s

/-- **Above all others is met by at most one seeker at a state.** -/
theorem aboveAll_unique {I : Type} {q : I → S → Nat} {i j : I} {s : S} (other : i ≠ j)
    (above : AboveAll q i s) (above' : AboveAll q j s) : False :=
  Nat.lt_irrefl _ (Nat.lt_trans (above j fun same => other same.symm) (above' i other))

/-- So two seekers never both stand above all others. -/
theorem aboveAll_not_two {I : Type} {q : I → S → Nat} {i j : I} (other : i ≠ j) (s : S) :
    ¬ (AboveAll q i s ∧ AboveAll q j s) :=
  fun ⟨above, above'⟩ => aboveAll_unique other above above'

namespace Law

/-- **A target met at a fixed state is met at rest.** Where the law leaves `s` unchanged and `s`
meets the target, the orbit from `s` stays at `s` and meets it at every step. -/
theorem fixed_rests {next : S → S} {s : S} (fixed : next s = s) {target : S → Prop}
    (meets : target s) : ∀ n, orbit next s n = s ∧ target (orbit next s n)
  | 0 => ⟨rfl, meets⟩
  | n + 1 =>
    have stays : orbit next s (n + 1) = s := (congrArg next (fixed_rests fixed meets n).1).trans fixed
    ⟨stays, (congrArg target stays).mpr meets⟩

/-- **The boundary of enough.** Under a determined law, the orbit from `s` comes to rest with its
target met from some step on exactly when it reaches a state the law leaves unchanged that meets
the target. -/
theorem rests_iff {next : S → S} {s : S} {target : S → Prop} :
    (∃ T, ∀ n, T ≤ n → orbit next s (n + 1) = orbit next s n ∧ target (orbit next s n)) ↔
      ∃ T, next (orbit next s T) = orbit next s T ∧ target (orbit next s T) :=
  ⟨fun ⟨T, rests⟩ => ⟨T, (rests T (Nat.le_refl T)).1, (rests T (Nat.le_refl T)).2⟩,
   fun ⟨T, fixed, meets⟩ => ⟨T, fun _ le =>
     match gap_of_le le with
     | ⟨d, at_n⟩ =>
       have stay : ∀ k, orbit next s (T + k) = orbit next s T ∧ target (orbit next s (T + k)) :=
         fun k => match fixed_rests fixed meets k with
           | ⟨same, holds⟩ => ⟨(orbit_add next s T k).trans same,
               (congrArg target (orbit_add next s T k)).mpr holds⟩
       have here := stay d
       have next' := stay (d + 1)
       ⟨(congrArg (orbit next s) (congrArg (· + 1) at_n)).trans (next'.1.trans
          (here.1.symm.trans (congrArg (orbit next s) at_n.symm))),
        (congrArg (fun m => target (orbit next s m)) at_n).mpr here.2⟩⟩⟩

/-- **More than now never rests.** Under any law, no step at which the orbit rests meets a target
of more than now. -/
theorem more_never_rests {next : S → S} {s : S} {q : S → Nat} (n : Nat) :
    ¬ (orbit next s (n + 1) = orbit next s n ∧ MoreThanNow q (orbit next s) n) :=
  fun ⟨rests, more⟩ => more_not_at_rest more rests

/-- **Two seekers above all others never rest together.** Under any law, no state left unchanged
meets the target of standing above all others for every seeker of a family holding two. -/
theorem aboveAll_never_rests {I : Type} {q : I → S → Nat} {i j : I} (other : i ≠ j)
    (next : S → S) : ¬ ∃ s, next s = s ∧ ∀ k, AboveAll q k s :=
  fun ⟨_, _, all⟩ => aboveAll_unique other (all i) (all j)

end Law

/-! ## B2. Expansion or exhaustion -/

namespace Flow

variable {F C : Type} {L : Flow F C} {W : Web F C} {stand : Nat → List C}

/-- **More than now needs a beyond.** Where what stands is listed at each step, a condition
rising at arbitrarily late steps needs, at arbitrarily late steps, steps across which what stands
does not run down. -/
theorem more_needs_unrun (census : W.StandingCensus stand) {c : C}
    (more : ∀ N, ∃ t, N ≤ t ∧ W.Rises t c) : ∀ N, ∃ t, N ≤ t ∧ ¬ L.RunsDown W t :=
  fun N => match (change_recurs_iff (L := L) census).mp
      (fun N => match more N with
        | ⟨t, le, rises⟩ => ⟨t, le, c, .inl rises⟩) N with
    | ⟨t, le, unrun, _⟩ => ⟨t, le, unrun⟩

/-- **Enclosed, more than now is exhausted.** Where what stands is listed at each step and runs
down at every step from `T` on, no condition rises at arbitrarily late steps. -/
theorem more_exhausted (census : W.StandingCensus stand) {T : Nat}
    (runs : ∀ t, T ≤ t → L.RunsDown W t) {c : C} : ¬ ∀ N, ∃ t, N ≤ t ∧ W.Rises t c :=
  fun more => match more_needs_unrun (L := L) census more T with
    | ⟨t, le, unrun⟩ => unrun (runs t le)

end Flow

end Becoming
