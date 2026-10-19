import Becoming.Withholding
import Becoming.FaultEnvelopes
import Becoming.Labelled

/-!
# Tolerance: thresholds of waiting and the laws that restore giving

`Becoming.Withholding` compares two laws under which a formation's giving waits on all it waits
on, and shows that restoring giving needs another law (`Withholding.Ring.givesFirst_restores`).
This module states the general family: laws of giving where a formation may go without some of
what it waits on, the start every restoration has to overcome, the formations that restoring
needs, and what a set of formations that keeps giving needs, with no premise beyond the
hypotheses each statement names. Every main law is stated on a run `Law.run next s` of the spine.

A formation `a` waits on the formations listed in `ups a` (a list, so that a number of them can be
counted) and spares `tol a` of them: under the *tolerating law* `tolerating tol ups` it gives at
the next step where all but at most `tol a` of what it waits on gave (`AllBut`). A formation that
waits on `m` and spares `m - k` gives where at least `k` of what it waits on gave.

* **All but `f`.** `AllBut s f l` holds where at most `f` members of `l` fail `s`. With `f = 0` it
  is "every member" (`AllBut.zero_iff`), with `f` at least the length of `l` it always holds
  (`AllBut.of_length_le`), it grows with `s` and with `f` (`AllBut.mono_set`,
  `AllBut.mono_count`), and it holds of the configuration where nothing gives exactly where
  `l` is at most `f` long (`AllBut.withheld_iff`).
* **Tolerance zero is waiting on all.** The tolerating law with every tolerance `0` has the course
  of `Withholding.answers` on the listed waits, at every step (`tolerating_zero`).
* **Every law that keeps inclusion** (`KeepsInclusion`: more giving now gives at least as much
  giving at the next step) keeps it along its courses (`KeepsInclusion.course`). The four laws
  `waitsAll`, `answers`, `givesFirst` and `tolerating` keep inclusion
  (`waitsAll_keeps`, `answers_keeps`, `givesFirst_keeps`, `tolerating_keeps`). For every such law:
  - **The worst start is total withholding** (headline). A formation gives at step `n` from every
    start exactly where it gives at `n` from the start at which nothing gives (`worst_start`).
  - **From total withholding giving only grows**: what gives at `n` gives at `n + 1`
    (`rises_from_withheld`), so restoring by step `n` is restoring at every later step from every
    start (`restored_stays`).
  - **Restoring needs a formation that gives after total withholding**: where none gives at the
    step after it, no formation gives at any step from it (`withheld_kept`).
* **The tolerating law.**
  - **Restoring needs a formation sparing all it waits on.** From total withholding, a formation
    giving at any step finds a formation that waits on at most as many as it spares
    (`gives_needs_sparing`); such a formation gives at every step after the start, whatever the
    start (`sparing_gives`); and where no formation spares all it waits on, total withholding at
    one step is total withholding at every later step (`total_stays`).
  - **A set that keeps giving.** A set of formations giving at the start, each waiting on at most
    its tolerance outside the set, gives at every step, whatever the other formations do
    (`kept_set`). With tolerance `0` the set takes in all it waits on.
  - **A thin withholding passes out in one step.** Where the start gives outside a set and every
    formation waits on at most its tolerance inside the set, every formation gives at every step
    from step 1 on (`thin_absorbed`).
* **Restoring under `givesFirst`, exactly.** A *clear chain* is a chain of waits none of whose
  formations after the first gives first (`Clear`). Under `Withholding.givesFirst`:
  - a clear chain of `n` waits into `a` makes `a` withhold at step `n` from total withholding
    (`clear_withholds`);
  - with the sources decided (`∀ a, src a ∨ ¬ src a`), `a` gives at step `n` from every start
    exactly where no clear chain of `n` waits leads into it (`restores_iff`, headline), and where
    no clear chain of `L` waits exists every formation gives at every step from `L` on, whatever the
    start (`restores_from`);
  - a loop of waits clear of sources withholds at each of its formations at every step from total
    withholding, so no step restores it from every start (`clear_loop_withholds`);
  - without memory, restoring by step `n` is exactly no chain of `n` waits into the formation
    (`answers_restores_iff`), so giving first never restores later than waiting on all
    (`givesFirst_restores_of_answers`), and with memory no step restores giving
    (`waitsAll_never_restores`).
  The ring of `Becoming.Withholding` has no clear chain of three waits (`Ring.no_clear_three`), so
  `Withholding.Ring.givesFirst_restores` is an instance (`Ring.restores_from_three`).
* **The certificate law of `Becoming.FaultEnvelopes`.** A domain gives at the next step where the
  certificate over its roster, under its envelope, accepts the giving of the step before
  (`certified`). A set of domains giving at the start, each with a separated envelope admitting a
  fault set that holds all of its roster outside the set, gives at every step (`certified_kept`,
  from `FaultEnvelopes.certificate_available`); a domain gives at step 1 from every start
  withholding exactly within one of its admitted fault sets exactly where its envelope is separated
  (`certified_available_iff`, from `FaultEnvelopes.availability_iff_separated`); and without
  separation a withholding held within an admitted fault set stops the domain at once
  (`certified_blocked`, from `FaultEnvelopes.correlated_three_blocks`).
* **Witness: three formations each waiting on the other two** (`Triad`). From one withholding,
  with tolerance `0` every formation withholds at every step from step 2 on and at step 1 `first`
  still gives (`Triad.spreads`); with tolerance `1` every formation gives at every step from step 1
  on (`Triad.absorbed`); and with tolerance `1` total withholding is kept at every step
  (`Triad.total_kept`): tolerance absorbs a thin withholding and restores nothing.

**Relations to other laws.** `worst_start` reads restoration off one course, the course from total
withholding; it is the monotone counterpart of `Withholding.withholding_absorbs` (with memory, the
course from total withholding is total withholding at every step). `clear_withholds` refines
`Withholding.withholding_spreads`: withholding spreads along a chain unless a formation on it gives
first. `kept_set` is the tolerating form of a set closed under what it waits on, and
`thin_absorbed` is the tolerating form of `Withholding.gives_without_chain`: a withholding passes
out in one step where every formation spares what the withholding touches. The tolerating law and
the certificate law are two readings of fault tolerance in giving: the first counts what may be
missing, the second lists which sets may fail together.

What is not derived: which formations wait on which, their tolerances and sources, and how a law
that tolerates or gives first forms. No ethical predicate, ranking or axiom occurs. The readings
belong to the chapter.
-/

namespace Becoming
namespace Tolerance

open Withholding

universe u

variable {α : Type u}

/-! ## All but `f` -/

/-- All but at most `f` members of `l` hold `s`: each member that does not is spared, at most `f`
times. -/
inductive AllBut (s : α → Prop) : Nat → List α → Prop
  | nil (f : Nat) : AllBut s f []
  | holds {f : Nat} {b : α} {l : List α} : s b → AllBut s f l → AllBut s f (b :: l)
  | spare {f : Nat} (b : α) {l : List α} : AllBut s f l → AllBut s (f + 1) (b :: l)

namespace AllBut

variable {s s' : α → Prop}

/-- **More holding, all but as many.** -/
theorem mono_set (sub : ∀ b, s b → s' b) {f : Nat} {l : List α} :
    AllBut s f l → AllBut s' f l
  | nil f => nil f
  | holds h rest => holds (sub _ h) (mono_set sub rest)
  | spare b rest => spare b (mono_set sub rest)

/-- **More spared, still all but as many.** -/
theorem mono_count : ∀ {f g : Nat} {l : List α}, f ≤ g → AllBut s f l → AllBut s g l
  | _, g, _, _, nil _ => nil g
  | _, _, _, le, holds h rest => holds h (mono_count le rest)
  | _, 0, _, le, spare _ _ => absurd le (Nat.not_succ_le_zero _)
  | _, _ + 1, _, le, spare b rest => spare b (mono_count (Nat.le_of_succ_le_succ le) rest)

/-- **Sparing every member.** -/
theorem of_length (l : List α) : AllBut s l.length l :=
  match l with
  | [] => nil 0
  | b :: l => spare b (of_length l)

/-- **Sparing at least as many as the list holds, all but `f` always holds.** -/
theorem of_length_le {f : Nat} {l : List α} (le : l.length ≤ f) : AllBut s f l :=
  mono_count le (of_length l)

/-- **With nothing spared, every member holds.** -/
theorem zero_all : ∀ {l : List α}, AllBut s 0 l → ∀ b, b ∈ l → s b
  | _ :: _, holds h _, _, .head _ => h
  | _ :: _, holds _ rest, b, .tail _ m => zero_all rest b m

/-- **All but none is every member.** -/
theorem zero_iff {l : List α} : AllBut s 0 l ↔ ∀ b, b ∈ l → s b :=
  ⟨zero_all, fun all => match l with
    | [] => nil 0
    | c :: l => holds (all c (.head l)) (zero_iff.mpr fun b m => all b (.tail c m))⟩

/-- **All but `f` finds a member that holds, or the list is at most `f` long.** -/
theorem found {f : Nat} {l : List α} :
    AllBut s f l → (∃ b, b ∈ l ∧ s b) ∨ l.length ≤ f
  | nil f => .inr (Nat.zero_le f)
  | holds h _ => .inl ⟨_, .head _, h⟩
  | spare _ rest => match found rest with
    | .inl ⟨c, m, h⟩ => .inl ⟨c, .tail _ m, h⟩
    | .inr le => .inr (Nat.succ_le_succ le)

/-- **Where nothing holds, all but `f` holds exactly of lists at most `f` long.** -/
theorem withheld_iff {f : Nat} {l : List α} :
    AllBut (fun _ => False) f l ↔ l.length ≤ f :=
  ⟨fun all => match found all with
    | .inl ⟨_, _, empty⟩ => empty.elim
    | .inr le => le,
   of_length_le⟩

end AllBut

/-! ## The tolerating law -/

/-- The tolerating law: a formation gives at the next step where all but at most `tol a` of what
it waits on gave. -/
def tolerating (tol : α → Nat) (ups : α → List α) (s : α → Prop) (a : α) : Prop :=
  AllBut s (tol a) (ups a)

/-- The listed waits as a relation: `b` is listed among what `a` waits on. -/
def Listed (ups : α → List α) (b a : α) : Prop :=
  b ∈ ups a

/-- **Tolerance zero is waiting on all.** With every tolerance `0`, the tolerating law has the
course of `Withholding.answers` on the listed waits, at every step and formation. -/
theorem tolerating_zero (ups : α → List α) (s : α → Prop) : ∀ (n : Nat) (a : α),
    (Law.run (tolerating (fun _ => 0) ups) s).state n a ↔
      (Law.run (answers (Listed ups)) s).state n a
  | 0, _ => Iff.rfl
  | n + 1, _ =>
    ⟨fun gives b m => (tolerating_zero ups s n b).mp (AllBut.zero_all gives b m),
     fun all => AllBut.zero_iff.mpr fun b m => (tolerating_zero ups s n b).mpr (all b m)⟩

/-! ## Laws that keep inclusion -/

/-- The start at which no formation gives. -/
def allWithheld : α → Prop := fun _ => False

/-- A law of change on configurations keeps inclusion: more giving now gives at least as much
giving at the next step. -/
def KeepsInclusion (next : (α → Prop) → α → Prop) : Prop :=
  ∀ s s' : α → Prop, (∀ a, s a → s' a) → ∀ a, next s a → next s' a

section Keeps

variable {next : (α → Prop) → α → Prop}

/-- **A law keeping inclusion keeps it along its courses**: a start within another gives a course
within the other's, at every step. -/
theorem KeepsInclusion.course (keeps : KeepsInclusion next) {s s' : α → Prop}
    (sub : ∀ a, s a → s' a) : ∀ n a, (Law.run next s).state n a → (Law.run next s').state n a
  | 0 => sub
  | n + 1 => keeps _ _ (KeepsInclusion.course keeps sub n)

/-- **The worst start is total withholding.** Under a law keeping inclusion, a formation gives at
step `n` from every start exactly where it gives at `n` from the start at which nothing gives. -/
theorem worst_start (keeps : KeepsInclusion next) (n : Nat) (a : α) :
    (∀ s, (Law.run next s).state n a) ↔ (Law.run next allWithheld).state n a :=
  ⟨fun all => all allWithheld,
   fun gives _ => keeps.course (fun _ empty => (empty : False).elim) n a gives⟩

/-- **From total withholding giving only grows**: under a law keeping inclusion, a formation
giving at step `n` from total withholding gives at `n + 1`. -/
theorem rises_from_withheld (keeps : KeepsInclusion next) :
    ∀ n a, (Law.run next allWithheld).state n a → (Law.run next allWithheld).state (n + 1) a
  | 0 => fun _ empty => (empty : False).elim
  | n + 1 => keeps _ _ (rises_from_withheld keeps n)

theorem rises_le (keeps : KeepsInclusion next) {n : Nat} {a : α}
    (gives : (Law.run next allWithheld).state n a) :
    ∀ d, (Law.run next allWithheld).state (n + d) a
  | 0 => gives
  | d + 1 => rises_from_withheld keeps (n + d) a (rises_le keeps gives d)

/-- **Restoring stays.** Under a law keeping inclusion, a formation giving at step `n` from every
start gives at every step from `n` on, from every start. -/
theorem restored_stays (keeps : KeepsInclusion next) {n : Nat} {a : α}
    (restored : ∀ s, (Law.run next s).state n a) :
    ∀ m, n ≤ m → ∀ s, (Law.run next s).state m a := by
  intro m le
  let ⟨d, same⟩ := gap_of_le le
  subst same
  exact (worst_start keeps (n + d) a).mpr
    (rises_le keeps ((worst_start keeps n a).mp restored) d)

/-- **Restoring needs a formation that gives after total withholding.** Under a law keeping
inclusion, where no formation gives at the step after total withholding, no formation gives at any
step of the course from it. -/
theorem withheld_kept (keeps : KeepsInclusion next) (empty : ∀ a, ¬ next allWithheld a) :
    ∀ n a, ¬ (Law.run next allWithheld).state n a
  | 0 => fun _ out => out
  | n + 1 => fun a gives =>
    empty a (keeps _ _ (fun b g => (withheld_kept keeps empty n b g).elim) a gives)

end Keeps

/-- `waitsAll` keeps inclusion. -/
theorem waitsAll_keeps (up : α → α → Prop) : KeepsInclusion (waitsAll up) :=
  fun _ _ sub a gives => ⟨sub a gives.1, fun b link => sub b (gives.2 b link)⟩

/-- `answers` keeps inclusion. -/
theorem answers_keeps (up : α → α → Prop) : KeepsInclusion (answers up) :=
  fun _ _ sub _ gives b link => sub b (gives b link)

/-- `givesFirst` keeps inclusion. -/
theorem givesFirst_keeps (src : α → Prop) (up : α → α → Prop) :
    KeepsInclusion (givesFirst src up) :=
  fun _ _ sub _ gives => gives.elim Or.inl fun all => Or.inr fun b link => sub b (all b link)

/-- The tolerating law keeps inclusion. -/
theorem tolerating_keeps (tol : α → Nat) (ups : α → List α) :
    KeepsInclusion (tolerating tol ups) :=
  fun _ _ sub _ gives => AllBut.mono_set sub gives

/-! ## Restoring under the tolerating law -/

section Tolerating

variable {tol : α → Nat} {ups : α → List α}

/-- **Restoring needs a formation sparing all it waits on.** From total withholding, a formation
giving at any step under the tolerating law finds a formation that waits on at most as many as it
spares. -/
theorem gives_needs_sparing : ∀ (n : Nat) (a : α),
    (Law.run (tolerating tol ups) allWithheld).state n a → ∃ b, (ups b).length ≤ tol b
  | 0, _, empty => (empty : False).elim
  | n + 1, a, gives => match AllBut.found gives with
    | .inl ⟨b, _, earlier⟩ => gives_needs_sparing n b earlier
    | .inr le => ⟨a, le⟩

/-- **A formation sparing all it waits on gives at every step after the start, whatever the
start.** -/
theorem sparing_gives {a : α} (spares : (ups a).length ≤ tol a) (s : α → Prop) (n : Nat) :
    (Law.run (tolerating tol ups) s).state (n + 1) a :=
  AllBut.of_length_le spares

/-- **Where no formation spares all it waits on, total withholding stays.** Under the tolerating
law, no formation giving at step `m` makes no formation give at any later step. -/
theorem total_stays {s : α → Prop} (spares_none : ∀ a, ¬ (ups a).length ≤ tol a) {m : Nat}
    (empty : ∀ a, ¬ (Law.run (tolerating tol ups) s).state m a) :
    ∀ k a, ¬ (Law.run (tolerating tol ups) s).state (m + k) a
  | 0 => empty
  | k + 1 => fun a gives => match AllBut.found gives with
    | .inl ⟨b, _, earlier⟩ => total_stays spares_none empty k b earlier
    | .inr le => spares_none a le

/-- **A set that keeps giving.** A set of formations giving at the start, each of which waits on
at most its tolerance outside the set, gives at every step under the tolerating law, whatever the
other formations do. -/
theorem kept_set {G s : α → Prop} (start : ∀ a, G a → s a)
    (inside : ∀ a, G a → AllBut G (tol a) (ups a)) :
    ∀ n a, G a → (Law.run (tolerating tol ups) s).state n a
  | 0 => start
  | n + 1 => fun a member => AllBut.mono_set (kept_set start inside n) (inside a member)

/-- **A thin withholding passes out in one step.** Where the start gives outside a set `W` and
every formation waits on at most its tolerance inside `W`, every formation gives at every step from
step 1 on under the tolerating law. -/
theorem thin_absorbed {W s : α → Prop} (start : ∀ a, ¬ W a → s a)
    (thin : ∀ a, AllBut (fun b => ¬ W b) (tol a) (ups a)) :
    ∀ n a, (Law.run (tolerating tol ups) s).state (n + 1) a
  | 0 => fun a => AllBut.mono_set start (thin a)
  | n + 1 => fun a => AllBut.mono_set (fun b _ => thin_absorbed start thin n b) (thin a)

end Tolerating

/-! ## Restoring under `givesFirst`, exactly -/

/-- A clear chain of exactly `k` waits from `b` to `a`: a chain of waits none of whose formations
after the first is a source. -/
inductive Clear (src : α → Prop) (up : α → α → Prop) : Nat → α → α → Prop
  | here (a : α) : Clear src up 0 a a
  | step {k : Nat} {b c a : α} : Clear src up k b c → up c a → ¬ src a → Clear src up (k + 1) b a

section GivesFirst

variable {src : α → Prop} {up : α → α → Prop}

/-- A clear chain of `n = k + 1` waits ends with one link, into a formation that is not a source,
after a clear chain of `k`. -/
theorem Clear.last_of_eq {n : Nat} {b a : α} :
    Clear src up n b a → ∀ k, n = k + 1 → ∃ c, Clear src up k b c ∧ up c a ∧ ¬ src a
  | .here _, _, same => Nat.noConfusion same
  | .step ch link out, _, same => (Nat.succ.inj same) ▸ ⟨_, ch, link, out⟩

/-- A clear chain of `k + 1` waits ends with one link after a clear chain of `k`. -/
theorem Clear.last {k : Nat} {b a : α} (ch : Clear src up (k + 1) b a) :
    ∃ c, Clear src up k b c ∧ up c a ∧ ¬ src a :=
  ch.last_of_eq k rfl

/-- A clear chain is a chain of waits. -/
theorem Clear.chain {k : Nat} {b a : α} : Clear src up k b a → Chain up k b a
  | .here a => Chain.here a
  | .step rest link _ => Chain.step (Clear.chain rest) link

/-- Clear chains join end to end. -/
theorem Clear.append {i : Nat} {x y : α} (first : Clear src up i x y) :
    ∀ {j : Nat} {z : α}, Clear src up j y z → Clear src up (i + j) x z
  | _, _, .here _ => first
  | _, _, .step rest link out => Clear.step (Clear.append first rest) link out

/-- A clear loop repeated `k` times is a clear loop. -/
theorem Clear.iterate {p : Nat} {b : α} (loop : Clear src up p b b) :
    ∀ k, Clear src up (p * k) b b
  | 0 => Clear.here b
  | k + 1 => Clear.append (Clear.iterate loop k) loop

/-- **A clear chain carries withholding.** A clear chain of `n` waits into `a` makes `a` withhold
at step `n` under `givesFirst` from total withholding. -/
theorem clear_withholds : ∀ {n : Nat} {b a : α}, Clear src up n b a →
    ¬ (Law.run (givesFirst src up) allWithheld).state n a
  | _, _, _, .here _ => fun empty => empty
  | _, _, _, .step rest link out => fun gives =>
    gives.elim out fun all => clear_withholds rest (all _ link)

/-- With the sources decided, a formation into which no clear chain of `n` waits leads gives at
step `n` from total withholding. -/
theorem gives_of_no_clear (decided : ∀ a, src a ∨ ¬ src a) : ∀ (n : Nat) (a : α),
    (∀ b, ¬ Clear src up n b a) → (Law.run (givesFirst src up) allWithheld).state n a
  | 0, a, empty => (empty a (Clear.here a)).elim
  | n + 1, a, empty => match decided a with
    | .inl source => Or.inl source
    | .inr out => Or.inr fun c link =>
      gives_of_no_clear decided n c fun b ch => empty b (Clear.step ch link out)

/-- **Restoring under `givesFirst` is exactly no clear chain.** With the sources decided, a
formation gives at step `n` from every start exactly where no clear chain of `n` waits leads into
it. -/
theorem restores_iff (decided : ∀ a, src a ∨ ¬ src a) (n : Nat) (a : α) :
    (∀ s, (Law.run (givesFirst src up) s).state n a) ↔ ∀ b, ¬ Clear src up n b a :=
  ⟨fun all _ ch => clear_withholds ch (all allWithheld),
   fun empty => (worst_start (givesFirst_keeps src up) n a).mpr
     (gives_of_no_clear decided n a empty)⟩

/-- **Where no clear chain is `L` waits long, giving is restored from step `L` on.** With the
sources decided, every formation gives at every step from `L` on under `givesFirst`, whatever the
start. -/
theorem restores_from (decided : ∀ a, src a ∨ ¬ src a) {L : Nat}
    (empty : ∀ b a, ¬ Clear src up L b a) :
    ∀ n, L ≤ n → ∀ s a, (Law.run (givesFirst src up) s).state n a :=
  fun n le s a =>
    restored_stays (givesFirst_keeps src up) ((restores_iff decided L a).mpr (empty · a)) n le s

/-- **Waiting on all restores exactly where no chain is that long.** Without memory, a formation
gives at step `n` from every start exactly where no chain of `n` waits leads into it. -/
theorem answers_restores_iff (n : Nat) (a : α) :
    (∀ s, (Law.run (answers up) s).state n a) ↔ ∀ b, ¬ Chain up n b a :=
  ⟨fun all b ch =>
    (answers_closed up allWithheld n a).mp ((worst_start (answers_keeps up) n a).mp all) b ch,
   fun empty s => (answers_closed up s n a).mpr fun b ch => (empty b ch).elim⟩

/-- **Giving first never restores later.** With the sources decided, where waiting on all
restores a formation by step `n`, so does `givesFirst`: a clear chain is a chain. -/
theorem givesFirst_restores_of_answers (decided : ∀ a, src a ∨ ¬ src a) {n : Nat} {a : α}
    (restored : ∀ s, (Law.run (answers up) s).state n a) :
    ∀ s, (Law.run (givesFirst src up) s).state n a :=
  (restores_iff decided n a).mpr fun b ch => (answers_restores_iff n a).mp restored b ch.chain

/-- **With memory no step restores giving.** Under `waitsAll`, no formation gives at any step from
every start: from total withholding nothing gives. -/
theorem waitsAll_never_restores (n : Nat) (a : α) :
    ¬ ∀ s, (Law.run (waitsAll up) s).state n a :=
  fun all => withheld_kept (waitsAll_keeps up) (fun _ gives => gives.1) n a (all allWithheld)

/-- **A loop clear of sources is never restored.** A clear loop of `p + 1` waits from `b` back to
`b` makes `b` withhold at every step from total withholding under `givesFirst`, so no step gives
at `b` from every start. -/
theorem clear_loop_withholds {p : Nat} {b : α} (loop : Clear src up (p + 1) b b) :
    ∀ n, ¬ (Law.run (givesFirst src up) allWithheld).state n b :=
  fun n gives =>
    clear_withholds (loop.iterate n)
      (((Nat.add_comm n (n * p)).trans (Nat.mul_comm n (p + 1))) ▸
        rises_le (givesFirst_keeps src up) gives (n * p))

end GivesFirst

/-! ## The ring of `Becoming.Withholding` -/

namespace Ring

open Withholding.Ring

/-- **The ring has no clear chain of three waits**: one of any three consecutive formations of the
ring is `first`, the source. -/
theorem no_clear_three : ∀ b a, ¬ Clear isFirst Waits 3 b a := by
  intro b a ch
  let ⟨_, ch, l3, n3⟩ := ch.last
  let ⟨_, ch, l2, n2⟩ := ch.last
  let ⟨_, _, l1, n1⟩ := ch.last
  cases l1 <;> cases l2 <;> cases l3 <;>
    first | exact n1 trivial | exact n2 trivial | exact n3 trivial

/-- Which formation of the ring is the source is decided. -/
theorem isFirst_decided : ∀ a : Withholding.Ring, isFirst a ∨ ¬ isFirst a
  | .first => .inl trivial
  | .second => .inr fun out => out
  | .third => .inr fun out => out

/-- **`Withholding.Ring.givesFirst_restores` is an instance of `restores_from`**: every formation
of the ring gives at every step from step 3 on under `givesFirst`, whatever the start. -/
theorem restores_from_three :
    ∀ n, 3 ≤ n → ∀ s a, (Law.run (givesFirst isFirst Waits) s).state n a :=
  restores_from isFirst_decided no_clear_three

end Ring

/-! ## The certificate law of `Becoming.FaultEnvelopes` -/

section Certified

open FaultEnvelopes

/-- The certificate law: a domain gives at the next step where the certificate over its roster,
under its envelope, accepts the giving of the step before. -/
def certified (roster : Domain → List Domain) (faults : Domain → Envelope) (s : Domain → Bool)
    (a : Domain) : Bool :=
  certificate (roster a) (faults a) s

variable {roster : Domain → List Domain} {faults : Domain → Envelope}

/-- **A set that keeps giving under the certificate law.** A set of domains giving at the start,
each with a separated envelope admitting a fault set that holds all of its roster outside the set,
gives at every step. -/
theorem certified_kept {G : Domain → Prop} {s : Domain → Bool}
    (start : ∀ a, G a → s a = true)
    (apart : ∀ a, G a → separated (roster a) (faults a))
    (covered : ∀ a, G a → ∃ bad, bad ∈ faults a ∧ ∀ d, d ∈ roster a → d ∈ bad ∨ G d) :
    ∀ n a, G a → (Law.run (certified roster faults) s).state n a = true
  | 0 => start
  | n + 1 => fun a member =>
    match covered a member with
    | ⟨bad, admitted, cover⟩ =>
      certificate_available (roster a) (faults a) bad admitted (apart a member) _
        fun d m outside => match cover d m with
          | .inl inside => absurd inside outside
          | .inr kept => certified_kept start apart covered n d kept

/-- **Availability under the certificate law is separation.** A domain gives at step 1 from every
start that withholds exactly within one of its admitted fault sets exactly where its envelope is
separated. -/
theorem certified_available_iff (a : Domain) :
    (∀ actual, actual ∈ faults a →
      (Law.run (certified roster faults) (fun d => !(actual.contains d))).state 1 a = true) ↔
      separated (roster a) (faults a) :=
  availability_iff_separated (roster a) (faults a)

/-- **Without separation, a withholding within an admitted fault set stops a domain.** With roster
`0, 1, 2` and the envelope admitting `0, 1` together or `2` alone, from the start at which only `2`
gives (the withholding within the admitted set `0, 1`), every domain withholds at step 1. -/
theorem certified_blocked (a : Domain) :
    (Law.run (certified (fun _ => roster3) (fun _ => correlated3)) (fun d => d == 2)).state 1 a =
      false :=
  correlated_three_blocks

end Certified

/-! ## Witness: three formations each waiting on the other two -/

/-- Three formations. -/
inductive Triad where
  | first
  | second
  | third

namespace Triad

/-- Each formation waits on the other two. -/
def ups : Triad → List Triad
  | first => [second, third]
  | second => [first, third]
  | third => [first, second]

/-- At the start `first` withholds and the other two give. -/
def oneWithheld : Triad → Prop
  | first => False
  | second => True
  | third => True

/-- The set holding `first` alone. -/
def firstOnly : Triad → Prop
  | first => True
  | second => False
  | third => False

/-- Tolerance `0` everywhere. -/
def tol0 : Triad → Nat := fun _ => 0

/-- Tolerance `1` everywhere. -/
def tol1 : Triad → Nat := fun _ => 1

theorem step_first {s : Triad → Prop} : tolerating tol0 ups s first → s second ∧ s third :=
  fun gives => ⟨AllBut.zero_all gives second (.head _),
    AllBut.zero_all gives third (.tail _ (.head _))⟩

theorem step_second {s : Triad → Prop} : tolerating tol0 ups s second → s first ∧ s third :=
  fun gives => ⟨AllBut.zero_all gives first (.head _),
    AllBut.zero_all gives third (.tail _ (.head _))⟩

theorem step_third {s : Triad → Prop} : tolerating tol0 ups s third → s first ∧ s second :=
  fun gives => ⟨AllBut.zero_all gives first (.head _),
    AllBut.zero_all gives second (.tail _ (.head _))⟩

/-- No formation of the triad spares both of its waits under tolerance `1`. -/
theorem tol1_spares_none : ∀ a, ¬ (ups a).length ≤ tol1 a
  | first => Nat.not_succ_le_self 1
  | second => Nat.not_succ_le_self 1
  | third => Nat.not_succ_le_self 1

theorem tol0_spares_none : ∀ a, ¬ (ups a).length ≤ tol0 a
  | first => Nat.not_succ_le_zero 1
  | second => Nat.not_succ_le_zero 1
  | third => Nat.not_succ_le_zero 1

/-- From one withholding, tolerance `0` withholds everywhere at step 2. -/
theorem total_at_two : ∀ a, ¬ (Law.run (tolerating tol0 ups) oneWithheld).state 2 a
  | first => fun gives => (step_second (step_first gives).1).1
  | second => fun gives => (step_third (step_second gives).2).1
  | third => fun gives => (step_second (step_third gives).2).1

/-- **With tolerance `0` one withholding spreads to all, exactly from step 2.** Every formation
withholds at every step from step 2 on, and at step 1 `first` still gives. -/
theorem spreads :
    (∀ n, 2 ≤ n → ∀ a, ¬ (Law.run (tolerating tol0 ups) oneWithheld).state n a) ∧
      (Law.run (tolerating tol0 ups) oneWithheld).state 1 first := by
  refine ⟨fun n le => ?_, AllBut.holds trivial (AllBut.holds trivial (AllBut.nil 0))⟩
  let ⟨d, same⟩ := gap_of_le le
  subst same
  exact total_stays tol0_spares_none total_at_two d

/-- **With tolerance `1` one withholding passes out in one step**: every formation gives at every
step from step 1 on. An instance of `thin_absorbed`. -/
theorem absorbed : ∀ n a, (Law.run (tolerating tol1 ups) oneWithheld).state (n + 1) a :=
  thin_absorbed (W := firstOnly)
    (fun a outside => match a with
      | first => (outside trivial).elim
      | second => trivial
      | third => trivial)
    (fun a => match a with
      | first => AllBut.holds (fun out => out) (AllBut.holds (fun out => out) (AllBut.nil 1))
      | second => AllBut.spare first (AllBut.holds (fun out => out) (AllBut.nil 0))
      | third => AllBut.spare first (AllBut.holds (fun out => out) (AllBut.nil 0)))

/-- **Tolerance `1` restores nothing**: from total withholding, no formation gives at any step.
An instance of `withheld_kept`. -/
theorem total_kept : ∀ n a, ¬ (Law.run (tolerating tol1 ups) allWithheld).state n a :=
  withheld_kept (tolerating_keeps tol1 ups)
    fun a gives => tol1_spares_none a (AllBut.withheld_iff.mp gives)

end Triad

end Tolerance
end Becoming
