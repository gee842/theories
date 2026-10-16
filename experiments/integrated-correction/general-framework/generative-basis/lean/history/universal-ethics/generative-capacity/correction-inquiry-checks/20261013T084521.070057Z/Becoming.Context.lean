import Becoming.Frame

/-!
# Contextual worlds: claims registered in context

A `Frame` fixes whether each claim is realized by the configuration alone: what is registered
of a claim does not depend on what else is registered with it. This module states that as a
commitment of the representation and what follows where it fails, with no premise.

A claim is registered in a context (`Contextual`): `within k c` says that context `k` registers
claim `c`, and `shows s k c` is what `k` registers of `c` at configuration `s`. Nothing is
decided and no choice is made.

* **Gluing is agreement where contexts meet.** The registrations at a configuration glue, one
  context-free reading agreeing with every context (`Contextual.Glues`), exactly where every
  two contexts registering a claim register it alike (`Contextual.glues_iff_agree`, given a
  context registering each claim).
* **Context-free claims are a commitment.** Read with its context, every registration is a claim
  of a frame (`Contextual.indexed`, `Contextual.indexed_fits`). A frame of context-free claims
  fits exactly where the registrations glue at every configuration (`Contextual.fitsFree_iff`).
* **Where the possibilities do not glue, no configuration does.** If what each context can show
  depends only on the claims it registers (`Local`) and no context-free reading lies within every
  context's possibilities (`NoGlobal`), then no configuration respecting them glues
  (`Contextual.not_glues`), and no frame of context-free claims fits a world one of whose
  configurations respects them (`Contextual.no_free_frame`), while the indexed frame does.
* **Two ways the parts fail a whole.** What a whole of possibilities allows within each context
  (`restrict`) is local (`restrict_local`), and the whole lies within what these glue to
  (`glued_of_whole`). The parts can fail it in two ways: they may not give it back
  (`PartsDetermine` fails; a relation held by the whole and by no part, as `Becoming.Description`
  shows for parity on Specker's pairs), or they may allow what no whole has: possibilities
  with no context-free reading, where some context allows something, are the parts of no whole
  (`no_whole`; `Specker.no_whole`, `Square.no_whole`).
* **Specker's three boxes** (1960): any two boxes may be opened together, and exactly one of the
  two opened holds the gem. Each opening's possibilities are local, every box can show either
  way in every opening it belongs to (`Specker.unforced`), no placement fits them all
  (`Specker.noGlobal`), and a world showing a gem in each opening exists (`Specker.respects`).
* **The Mermin–Peres square.** Nine claims in three rows and three columns, each line
  registering three; a row's three values have even parity, as do the first two columns', and
  the third column's odd. Each line's possibilities are local, every cell can show either value
  in both its lines (`Square.unforced`), and no assignment fits all six lines
  (`Square.noGlobal`). Two-qubit observables realize the square, so quantum registrations are
  of this kind: `Becoming.Quantum` (P72q), which imports this module, checks it
  (`line_product`, `shows_support`, `support_shown`, `no_context_free_values`).

So a frame of context-free claims is a commitment of the representation: it holds of a world
exactly where its registrations glue, and some worlds' registrations cannot glue at any
configuration. Claims indexed by the context in which they are registered always fit, at the cost
that a claim registered in two contexts is two claims. Readings of this as wave and particle, as
the Kochen–Specker theorem, or as values being relations registered in context belong to the
study, not to this module.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w u' u''

/-- Claims registered in contexts: which claims each context registers, and what it registers of
each at each configuration. -/
structure Contextual (S : Type u) (K : Type v) (C : Type w) (V : Type u') where
  within : K → C → Prop
  shows : S → K → C → V

/-- What each context can show depends only on the claims it registers. -/
def Local {K : Type v} {C : Type w} {V : Type u'} (within : K → C → Prop)
    (support : K → (C → V) → Prop) : Prop :=
  ∀ k v v', (∀ c, within k c → v c = v' c) → support k v → support k v'

/-- No context-free reading lies within every context's possibilities. -/
def NoGlobal {K : Type v} {C : Type w} {V : Type u'} (support : K → (C → V) → Prop) : Prop :=
  ¬ ∃ v : C → V, ∀ k, support k v

/-- No context forces a claim: every claim can show every value in every context registering
it. -/
def Unforced {K : Type v} {C : Type w} {V : Type u'} (within : K → C → Prop)
    (support : K → (C → V) → Prop) : Prop :=
  ∀ k c b, within k c → ∃ v, support k v ∧ v c = b

namespace Contextual

variable {S : Type u} {K : Type v} {C : Type w} {V : Type u'} (X : Contextual S K C V)

/-! ## Gluing -/

/-- At `s` the registrations glue: one context-free reading agrees with every context on every
claim it registers. -/
def Glues (s : S) : Prop :=
  ∃ v : C → V, ∀ k c, X.within k c → X.shows s k c = v c

/-- At `s` every two contexts registering a claim register it alike. -/
def Agree (s : S) : Prop :=
  ∀ k k' c, X.within k c → X.within k' c → X.shows s k c = X.shows s k' c

theorem Glues.agree {X : Contextual S K C V} {s : S} (glues : X.Glues s) : X.Agree s :=
  match glues with
  | ⟨_, hv⟩ => fun k k' c w w' => (hv k c w).trans (hv k' c w').symm

/-- **The registrations glue exactly where contexts agree where they meet.** -/
theorem glues_iff_agree (home : C → K) (covers : ∀ c, X.within (home c) c) (s : S) :
    X.Glues s ↔ X.Agree s :=
  ⟨Glues.agree, fun agree =>
    ⟨fun c => X.shows s (home c) c, fun k c w => agree k (home c) c w (covers c)⟩⟩

/-! ## Frames -/

/-- Read with its context, every registration is a claim: a context, a claim and a value. -/
def indexed {A : Type u''} (P : Process S A) : Frame S A (K × C × V) :=
  ⟨P, fun s q => X.within q.1 q.2.1 ∧ X.shows s q.1 q.2.1 = q.2.2⟩

/-- The indexed frame fits every registration. -/
theorem indexed_fits {A : Type u''} (P : Process S A) (s : S) (k : K) (c : C) (b : V) :
    (X.indexed P).realized s (k, c, b) ↔ X.within k c ∧ X.shows s k c = b :=
  Iff.rfl

/-- A frame of context-free claims, a claim with a value, fits when it agrees with every context
on every claim the context registers. -/
def FitsFree {A : Type u''} (F : Frame S A (C × V)) : Prop :=
  ∀ s k c b, X.within k c → (X.shows s k c = b ↔ F.realized s (c, b))

/-- **A frame of context-free claims fits exactly where the registrations glue at every
configuration.** -/
theorem fitsFree_iff {A : Type u''} (P : Process S A) (home : C → K)
    (covers : ∀ c, X.within (home c) c) :
    (∃ F : Frame S A (C × V), F.P = P ∧ X.FitsFree F) ↔ ∀ s, X.Glues s :=
  ⟨fun ⟨_, _, fits⟩ s =>
    ⟨fun c => X.shows s (home c) c, fun k c w =>
      ((fits s (home c) c (X.shows s k c) (covers c)).mpr
        ((fits s k c (X.shows s k c) w).mp rfl)).symm⟩,
   fun glues =>
    ⟨⟨P, fun s q => X.shows s (home q.1) q.1 = q.2⟩, rfl, fun s k c _ w =>
      match glues s with
      | ⟨_, hv⟩ =>
        have same : X.shows s k c = X.shows s (home c) c := (hv k c w).trans (hv (home c) c (covers c)).symm
        ⟨fun e => same.symm.trans e, fun e => same.trans e⟩⟩⟩

/-! ## Where the possibilities do not glue -/

/-- What every context shows at `s` lies within its possibilities. -/
def Respects (support : K → (C → V) → Prop) (s : S) : Prop := ∀ k, support k (X.shows s k)

/-- **Where the possibilities allow no context-free reading, no configuration respecting them
glues.** -/
theorem not_glues {support : K → (C → V) → Prop} (loc : Local X.within support)
    (none : NoGlobal support) {s : S} (respects : X.Respects support s) : ¬ X.Glues s :=
  fun ⟨v, hv⟩ => none ⟨v, fun k => loc k (X.shows s k) v (fun c w => hv k c w) (respects k)⟩

/-- So no frame of context-free claims fits a world one of whose configurations respects them,
since such a frame glues at every configuration; the indexed frame fits it (`indexed_fits`). -/
theorem no_free_frame {A : Type u''} {support : K → (C → V) → Prop} (loc : Local X.within support)
    (none : NoGlobal support) {s₀ : S} (respects : X.Respects support s₀) (P : Process S A)
    (home : C → K) (covers : ∀ c, X.within (home c) c) :
    ¬ ∃ F : Frame S A (C × V), F.P = P ∧ X.FitsFree F :=
  fun fits => X.not_glues loc none respects ((X.fitsFree_iff P home covers).mp fits s₀)

end Contextual

/-! ## A whole and the readings of its parts -/

section Wholes

variable {K : Type v} {C : Type w} {V : Type u'}

/-- What a whole of possibilities allows within a context: the readings some possibility agrees
with on every claim the context registers. -/
def restrict (within : K → C → Prop) (W : (C → V) → Prop) (k : K) (u : C → V) : Prop :=
  ∃ v, W v ∧ ∀ c, within k c → v c = u c

/-- A reading every context allows: what the descriptions of the parts glue to. -/
def Glued (support : K → (C → V) → Prop) (v : C → V) : Prop := ∀ k, support k v

/-- The parts of a whole give it back: every reading that every context allows is possible. -/
def PartsDetermine (within : K → C → Prop) (W : (C → V) → Prop) : Prop :=
  ∀ v, Glued (restrict within W) v → W v

/-- A whole lies within what its parts glue to. -/
theorem glued_of_whole {within : K → C → Prop} {W : (C → V) → Prop} {v : C → V} (h : W v) :
    Glued (restrict within W) v :=
  fun _ => ⟨v, h, fun _ _ => rfl⟩

/-- What a whole allows within a context depends only on the claims the context registers. -/
theorem restrict_local (within : K → C → Prop) (W : (C → V) → Prop) :
    Local within (restrict within W) :=
  fun _ _ _ same ⟨v, hv, agree⟩ => ⟨v, hv, fun c w => (agree c w).trans (same c w)⟩

/-- **Possibilities with no context-free reading, where some context allows something, are the
parts of no whole**, whatever each context registers: locality is not used. Where nothing is
allowed anywhere, the empty whole has these parts. -/
theorem no_whole {within : K → C → Prop} {support : K → (C → V) → Prop}
    (none : NoGlobal support) (some : ∃ k u, support k u) :
    ¬ ∃ W : (C → V) → Prop, ∀ k u, support k u ↔ restrict within W k u :=
  fun ⟨_, parts⟩ => match some with
    | ⟨k, u, h⟩ => match (parts k u).mp h with
      | ⟨v, hv, _⟩ => none ⟨v, fun k' => (parts k' v).mpr ⟨v, hv, fun _ _ => rfl⟩⟩

end Wholes

/-! ## Specker's three boxes -/

namespace Specker

/-- Three boxes. -/
inductive Box where
  | a
  | b
  | c

/-- The three ways to open two of them. -/
inductive Opening where
  | ab
  | bc
  | ca

def first : Opening → Box
  | .ab => .a
  | .bc => .b
  | .ca => .c

def second : Opening → Box
  | .ab => .b
  | .bc => .c
  | .ca => .a

/-- An opening registers its two boxes. -/
def within (k : Opening) (x : Box) : Prop := x = first k ∨ x = second k

/-- Exactly one of the two opened holds the gem. -/
def support (k : Opening) (v : Box → Bool) : Prop := v (first k) ≠ v (second k)

theorem local_ : Local within support :=
  fun _ _ _ same h e => h ((same _ (.inl rfl)).trans (e.trans (same _ (.inr rfl)).symm))

theorem three_do_not : ∀ x y z : Bool, ¬ (x ≠ y ∧ y ≠ z ∧ z ≠ x) := by decide

/-- **No placement of gems fits every opening.** -/
theorem noGlobal : NoGlobal support :=
  fun ⟨v, hv⟩ => three_do_not (v .a) (v .b) (v .c) ⟨hv .ab, hv .bc, hv .ca⟩

/-- `marks x y`: `y` is `x`. -/
def marks : Box → Box → Bool
  | .a, .a => true
  | .b, .b => true
  | .c, .c => true
  | .a, .b => false
  | .a, .c => false
  | .b, .a => false
  | .b, .c => false
  | .c, .a => false
  | .c, .b => false

theorem marks_self : ∀ x, marks x x = true
  | .a => rfl
  | .b => rfl
  | .c => rfl

theorem marks_other : ∀ k, marks (first k) (second k) = false ∧ marks (second k) (first k) = false
  | .ab => ⟨rfl, rfl⟩
  | .bc => ⟨rfl, rfl⟩
  | .ca => ⟨rfl, rfl⟩

theorem flip_ne : ∀ b : Bool, b ≠ !b
  | true => fun h => nomatch h
  | false => fun h => nomatch h

/-- **No opening forces a box**: every box can show either way in every opening it belongs to,
so whatever a box shows in one opening it can show in the other. -/
theorem unforced : Unforced within support :=
  fun k x b w => match w with
    | .inl e => ⟨fun y => cond (marks (first k) y) b (!b),
        by
          show cond (marks (first k) (first k)) b (!b) ≠ cond (marks (first k) (second k)) b (!b)
          rw [marks_self, (marks_other k).1]
          exact flip_ne b,
        by
          subst e
          show cond (marks (first k) (first k)) b (!b) = b
          rw [marks_self]
          rfl⟩
    | .inr e => ⟨fun y => cond (marks (second k) y) b (!b),
        by
          show cond (marks (second k) (first k)) b (!b) ≠ cond (marks (second k) (second k)) b (!b)
          rw [marks_self, (marks_other k).2]
          exact fun h => flip_ne b h.symm,
        by
          subst e
          show cond (marks (second k) (second k)) b (!b) = b
          rw [marks_self]
          rfl⟩

/-- A world with one configuration: each opening shows the gem in its first box. -/
def world : Contextual Unit Opening Box Bool := ⟨within, fun _ k y => marks (first k) y⟩

/-- It respects every opening's possibilities, so it glues nowhere. -/
theorem respects : world.Respects support () :=
  fun k => by
    show marks (first k) (first k) ≠ marks (first k) (second k)
    rw [marks_self, (marks_other k).1]
    exact fun h => nomatch h

theorem not_glues : ¬ world.Glues () :=
  world.not_glues local_ noGlobal respects

/-- **The openings' possibilities are the parts of no whole.** -/
theorem no_whole : ¬ ∃ W : (Box → Bool) → Prop, ∀ k u, support k u ↔ restrict within W k u :=
  Becoming.no_whole noGlobal (match unforced .ab .a true (.inl rfl) with
    | ⟨v, h, _⟩ => ⟨.ab, v, h⟩)

end Specker

/-! ## The Mermin–Peres square -/

namespace Square

/-- A cell: its row and its column. -/
abbrev Cell := Fin 3 × Fin 3

/-- The three positions, named without numerals: a numeral of `Fin 3` goes through an instance
whose proof uses `propext`. -/
def i0 : Fin 3 := ⟨0, by decide⟩
def i1 : Fin 3 := ⟨1, by decide⟩
def i2 : Fin 3 := ⟨2, by decide⟩

/-- A line registers three cells. -/
inductive Line where
  | row (i : Fin 3)
  | column (j : Fin 3)

def within : Line → Cell → Prop
  | .row i, p => p.1 = i
  | .column j, p => p.2 = j

/-- The cell at position `q` of a line. -/
def at_ : Line → Fin 3 → Cell
  | .row i, q => (i, q)
  | .column j, q => (q, j)

theorem within_at : ∀ (l : Line) (q : Fin 3), within l (at_ l q)
  | .row _, _ => rfl
  | .column _, _ => rfl

/-- The parity of three values. -/
def parity (x y z : Bool) : Bool := x ^^ (y ^^ z)

/-- Odd parity: only the third column (`true` is the outcome −1). -/
def odd : Line → Bool
  | .row _ => false
  | .column j => Nat.beq j.val 2

/-- A line's three values have the parity the line requires. -/
def support (l : Line) (v : Cell → Bool) : Prop :=
  parity (v (at_ l i0)) (v (at_ l i1)) (v (at_ l i2)) = odd l

theorem local_ : Local within support :=
  fun l v v' same h =>
    (congrArg (fun z => parity z (v' (at_ l i1)) (v' (at_ l i2))) (same _ (within_at l i0))).symm.trans
      ((congrArg (fun z => parity (v (at_ l i0)) z (v' (at_ l i2))) (same _ (within_at l i1))).symm.trans
        ((congrArg (fun z => parity (v (at_ l i0)) (v (at_ l i1)) z) (same _ (within_at l i2))).symm.trans h))

theorem nine : ∀ a b c d e f g h i : Bool,
    ¬ (parity a b c = false ∧ parity d e f = false ∧ parity g h i = false ∧
       parity a d g = false ∧ parity b e h = false ∧ parity c f i = true) := by decide

/-- **No assignment fits all six lines.** -/
theorem noGlobal : NoGlobal support :=
  fun ⟨v, hv⟩ => nine (v (i0, i0)) (v (i0, i1)) (v (i0, i2)) (v (i1, i0)) (v (i1, i1)) (v (i1, i2))
    (v (i2, i0)) (v (i2, i1)) (v (i2, i2))
    ⟨hv (.row i0), hv (.row i1), hv (.row i2), hv (.column i0), hv (.column i1), hv (.column i2)⟩

/-- The position of a cell within a line. -/
def pos : Line → Cell → Fin 3
  | .row _, p => p.2
  | .column _, p => p.1

theorem pos_at : ∀ (l : Line) (q : Fin 3), pos l (at_ l q) = q
  | .row _, _ => rfl
  | .column _, _ => rfl

theorem at_pos : ∀ (l : Line) (p : Cell), within l p → at_ l (pos l p) = p
  | .row _, (_, _), w => by cases w; rfl
  | .column _, (_, _), w => by cases w; rfl

/-- Values by position: `b` at position `q`, `t` at the next, `b` at the third. -/
def fill (q : Fin 3) (b t : Bool) (r : Fin 3) : Bool :=
  cond (Nat.beq r.val q.val) b (cond (Nat.beq r.val ((q.val + 1) % 3)) t b)

theorem fill_parity : ∀ (q : Fin 3) (b t : Bool), parity (fill q b t i0) (fill q b t i1) (fill q b t i2) = t ∧ fill q b t q = b := by
  decide

/-- **No line forces a cell**: every cell can show either value in both its lines. -/
theorem unforced : Unforced within support :=
  fun l p b w =>
    ⟨fun y => fill (pos l p) b (odd l) (pos l y),
     by
       show parity (fill (pos l p) b (odd l) (pos l (at_ l i0))) (fill (pos l p) b (odd l) (pos l (at_ l i1)))
         (fill (pos l p) b (odd l) (pos l (at_ l i2))) = odd l
       rw [pos_at, pos_at, pos_at]
       exact (fill_parity (pos l p) b (odd l)).1,
     (fill_parity (pos l p) b (odd l)).2⟩

/-- **The lines' possibilities are the parts of no whole.** -/
theorem no_whole : ¬ ∃ W : (Cell → Bool) → Prop, ∀ l u, support l u ↔ restrict within W l u :=
  Becoming.no_whole noGlobal (match unforced (.row i0) (i0, i0) true rfl with
    | ⟨v, h, _⟩ => ⟨.row i0, v, h⟩)

end Square

end Becoming
