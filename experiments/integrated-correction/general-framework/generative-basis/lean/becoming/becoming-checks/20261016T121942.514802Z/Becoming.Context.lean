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
* **The Mermin–Peres square** (Mermin 1990, Peres 1990). Nine claims in three rows and three columns, each line
  registering three; a row's three values have even parity, as do the first two columns', and
  the third column's odd. Each line's possibilities are local, every cell can show either value
  in both its lines (`Square.unforced`), and no assignment fits all six lines
  (`Square.noGlobal`). Two-qubit observables realize the square, so quantum registrations are
  of this kind: `Becoming.Quantum` (P72q), which imports this module, checks it
  (`line_product`, `shows_support`, `support_shown`, `no_context_free_values`).

* **Laws in context.** A law can also hold in a context: a family gives each context its law
  (`pooledLaw`, `retainedLaw`). Forgetting which context supports a step pools the laws; the pooled
  law runs exactly the courses some single context runs, for an inhabited family, exactly where
  such courses compose (`pooledLaw_exact_iff_joinClosed`). Two contexts, one stepping from `0` to
  `1` and the other from `1` to `2`, pool into a course from `0` to `2` that no context runs
  (`CrossingContexts.pooled_crosses`, `CrossingContexts.not_inOne`). Retaining the context, as the
  indexed frame retains it for claims, runs exactly these courses (`retainedLaw_trace_iff`,
  `retainedLaw_realizes_inOne`). Where contexts and configurations change together
  (`evolvingLaw`), the law with the context forgotten (`erasedLaw`) runs the courses of the
  evolving law from every context exactly where every context can follow each forgotten step,
  which is the foundation's `projection_exact_iff` read along `Prod.snd`
  (`erasedLaw_exact_iff_lifts`); the contexts a course can arrive in are those its last step
  advances from the contexts its earlier part arrives in (`arrives_append`, `arrives_snoc`). A
  context can change within one course, and the course can end (`ChangingContext.joins`,
  `ChangingContext.ends`), and the forgotten law can take a step the given context cannot follow
  (`ChangingContext.erased_not_lifted`).
So a frame of context-free claims is a commitment of the representation: it holds of a world
exactly where its registrations glue, and some worlds' registrations cannot glue at any
configuration. Claims indexed by the context in which they are registered always fit, at the cost
that a claim registered in two contexts is two claims. Readings of this as wave and particle, as
the Kochen–Specker theorem, or as values being relations registered in context belong to the
study, not to this module.

**Classical sources.** Reading a family of registrations in context as gluing to one context-free
reading is the sheaf-theoretic account of contextuality (Abramsky and Brandenburger 2011), and
possibilities that are the parts of no whole are its logical contextuality; the parity form of the
obstruction, its cohomological reading and the magic-square games are credited in
`Becoming.Gluing` (Abramsky, Barbosa, Kishida, Lal and Mansfield 2015; Arkhipov 2012).

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


/-! ## Laws in context -/

section Laws

variable {I : Type u} {S : Type v} {A : Type w}

/-- The pooled law of a family of laws, one for each context: a step some context's law takes,
with the context forgotten. -/
def pooledLaw (family : I → Process S A) : Process S A :=
  ⟨fun s a t => ∃ i, (family i).step s a t⟩

/-- A course some single context's law runs. -/
def InOne (family : I → Process S A) (s : S) (word : List A) (t : S) : Prop :=
  ∃ i, Trace (family i) s word t

/-- Courses of single contexts compose: a course run in one context followed by a course run in
one context is a course run in one context. -/
def JoinClosed (family : I → Process S A) : Prop :=
  ∀ s m t xs ys, InOne family s xs m → InOne family m ys t → InOne family s (xs ++ ys) t

/-- A course of one context is a course of the pooled law. -/
theorem InOne.pooled {family : I → Process S A} {s t : S} {word : List A} :
    InOne family s word t → Trace (pooledLaw family) s word t
  | ⟨i, path⟩ => trace_map (P := family i) (Q := pooledLaw family) (f := fun x => x)
      (fun _ _ _ step => ⟨i, step⟩) path

/-- Where courses of single contexts compose, every pooled course is run in one context. -/
theorem JoinClosed.inOne {family : I → Process S A} (joins : JoinClosed family) (seed : I) :
    ∀ {s t : S} {word : List A}, Trace (pooledLaw family) s word t → InOne family s word t
  | _, _, _, .nil s => ⟨seed, .nil s⟩
  | _, _, _, .cons ⟨i, step⟩ path =>
    joins _ _ _ [_] _ ⟨i, .cons step (.nil _)⟩ (JoinClosed.inOne joins seed path)

/-- **Pooling keeps exactly the courses of single contexts where they compose.** For an
inhabited family, the pooled law runs exactly the courses some single context runs, exactly
where such courses are closed under joining. -/
theorem pooledLaw_exact_iff_joinClosed {family : I → Process S A} (seed : I) :
    (∀ s word t, Trace (pooledLaw family) s word t ↔ InOne family s word t) ↔
      JoinClosed family :=
  ⟨fun exact s _ t xs ys first second =>
     (exact s (xs ++ ys) t).mp (trace_append_iff.mpr ⟨_, first.pooled, second.pooled⟩),
   fun joins _ _ _ => ⟨joins.inOne seed, InOne.pooled⟩⟩

/-- The law that retains the context: a configuration carries its context, and a step keeps the
context and takes a step of that context's law. -/
def retainedLaw (family : I → Process S A) : Process (I × S) A :=
  ⟨fun p a q => p.1 = q.1 ∧ (family p.1).step p.2 a q.2⟩

theorem retainedLaw_trace {family : I → Process S A} :
    ∀ {p q : I × S} {word : List A}, Trace (retainedLaw family) p word q →
      p.1 = q.1 ∧ Trace (family p.1) p.2 word q.2
  | _, _, _, .nil p => ⟨rfl, .nil p.2⟩
  | _, _, _, .cons ⟨same, step⟩ path =>
    match retainedLaw_trace path with
    | ⟨same', rest⟩ =>
      ⟨same.trans same', .cons step
        (Eq.subst (motive := fun i => Trace (family i) _ _ _) same.symm rest)⟩

/-- **Retaining the context runs exactly the courses of that context.** -/
theorem retainedLaw_trace_iff {family : I → Process S A} {i j : I} {s t : S} {word : List A} :
    Trace (retainedLaw family) (i, s) word (j, t) ↔ i = j ∧ Trace (family i) s word t :=
  ⟨retainedLaw_trace, fun ⟨same, path⟩ =>
    Eq.subst (motive := fun k => Trace (retainedLaw family) (i, s) word (k, t)) same
      (trace_map (P := family i) (Q := retainedLaw family) (f := fun x => (i, x))
        (fun _ _ _ step => ⟨rfl, step⟩) path)⟩

/-- **The retained law realizes exactly the courses of single contexts.** -/
theorem retainedLaw_realizes_inOne {family : I → Process S A} {s t : S} {word : List A} :
    (∃ i j, Trace (retainedLaw family) (i, s) word (j, t)) ↔ InOne family s word t :=
  ⟨fun ⟨i, _, path⟩ => ⟨i, (retainedLaw_trace_iff.mp path).2⟩,
   fun ⟨i, path⟩ => ⟨i, i, retainedLaw_trace_iff.mpr ⟨rfl, path⟩⟩⟩

/-- Contexts and configurations changing together: `R i s a j t` says that from configuration `s`
in context `i` the move `a` leads to `t` in context `j`. -/
def evolvingLaw (R : I → S → A → I → S → Prop) : Process (I × S) A :=
  ⟨fun p a q => R p.1 p.2 a q.1 q.2⟩

/-- The same law with the context forgotten. -/
def erasedLaw (R : I → S → A → I → S → Prop) : Process S A :=
  ⟨fun s a t => ∃ i j, R i s a j t⟩

/-- **Forgetting the context is exact from every context exactly where every context can follow
each forgotten step.** This is the foundation's `projection_exact_iff`, read along `Prod.snd`. -/
theorem erasedLaw_exact_iff_lifts (R : I → S → A → I → S → Prop) :
    (∀ i s a t, (∃ j k, R j s a k t) → ∃ k, R i s a k t) ↔
      ∀ i s word t, Trace (erasedLaw R) s word t ↔ ∃ j, Trace (evolvingLaw R) (i, s) word (j, t) :=
  Iff.trans
    ⟨fun lifts => ⟨fun p _ q step => ⟨p.1, q.1, step⟩,
       fun p a t ⟨_, _, step⟩ => match lifts p.1 p.2 a t ⟨_, _, step⟩ with
         | ⟨k, next⟩ => ⟨(k, t), next, rfl⟩⟩,
     fun ⟨_, lift⟩ i s a t forgotten => match lift (i, s) a t forgotten with
       | ⟨q, next, same⟩ =>
         ⟨q.1, Eq.subst (motive := fun x => R i s a q.1 x) same next⟩⟩
    (Iff.trans (projection_exact_iff (P := evolvingLaw R) (Q := erasedLaw R) (q := fun p => p.2))
      ⟨fun exact i s word t => (exact (i, s) word t).trans
          ⟨fun ⟨q, path, same⟩ =>
             ⟨q.1, Eq.subst (motive := fun x => Trace (evolvingLaw R) (i, s) word (q.1, x))
               same path⟩,
           fun ⟨j, path⟩ => ⟨(j, t), path, rfl⟩⟩,
       fun exact p word t => (exact p.1 p.2 word t).trans
          ⟨fun ⟨j, path⟩ => ⟨(j, t), path, rfl⟩,
           fun ⟨q, path, same⟩ =>
             ⟨q.1, Eq.subst (motive := fun x => Trace (evolvingLaw R) p word (q.1, x)) same path⟩⟩⟩)

/-- The contexts a course can arrive in: from a context in `initial`, the evolving law runs the
course from `s` to `t`, arriving in context `j`. -/
def Arrives (R : I → S → A → I → S → Prop) (initial : I → Prop) (s : S) (word : List A) (t : S)
    (j : I) : Prop :=
  ∃ i, initial i ∧ Trace (evolvingLaw R) (i, s) word (j, t)

/-- The contexts one step advances to from the contexts in `possible`. -/
def Advance (R : I → S → A → I → S → Prop) (possible : I → Prop) (s : S) (a : A) (t : S)
    (j : I) : Prop :=
  ∃ i, possible i ∧ R i s a j t

/-- **Arrival along a joined course is arrival along its second part from where the first
arrives.** -/
theorem arrives_append {R : I → S → A → I → S → Prop} {initial : I → Prop} {s t : S}
    {xs ys : List A} {k : I} :
    Arrives R initial s (xs ++ ys) t k ↔ ∃ m, Arrives R (Arrives R initial s xs m) m ys t k :=
  ⟨fun ⟨i, start, path⟩ => match trace_append_iff.mp path with
    | ⟨mid, first, second⟩ => ⟨mid.2, mid.1, ⟨i, start, first⟩, second⟩,
   fun ⟨_, j, ⟨i, start, first⟩, second⟩ =>
    ⟨i, start, trace_append_iff.mpr ⟨(j, _), first, second⟩⟩⟩

theorem arrives_singleton {R : I → S → A → I → S → Prop} {possible : I → Prop} {s t : S} {a : A}
    {j : I} : Arrives R possible s [a] t j ↔ Advance R possible s a t j :=
  ⟨fun ⟨i, start, path⟩ => ⟨i, start, trace_singleton_iff.mp path⟩,
   fun ⟨i, start, step⟩ => ⟨i, start, trace_singleton_iff.mpr step⟩⟩

/-- **The contexts a course arrives in are those its last step advances to from the contexts its
earlier part arrives in.** Support is carried by the one course, not chosen afresh per step. -/
theorem arrives_snoc {R : I → S → A → I → S → Prop} {initial : I → Prop} {s t : S}
    {word : List A} {a : A} {j : I} :
    Arrives R initial s (word ++ [a]) t j ↔ ∃ m, Advance R (Arrives R initial s word m) m a t j :=
  arrives_append.trans
    ⟨fun ⟨m, arrives⟩ => ⟨m, arrives_singleton.mp arrives⟩,
     fun ⟨m, advance⟩ => ⟨m, arrives_singleton.mpr advance⟩⟩

end Laws

/-! ### Two contexts that pool into a crossing no context runs -/

namespace CrossingContexts

/-- Context `false` steps from `0` to `1`; context `true` steps from `1` to `2`. -/
def family (b : Bool) : Process Nat Unit :=
  ⟨fun s _ t => (b = false ∧ s = 0 ∧ t = 1) ∨ (b = true ∧ s = 1 ∧ t = 2)⟩

theorem pooled_crosses : Trace (pooledLaw family) 0 [(), ()] 2 :=
  .cons ⟨false, Or.inl ⟨rfl, rfl, rfl⟩⟩ (.cons ⟨true, Or.inr ⟨rfl, rfl, rfl⟩⟩ (.nil 2))

/-- **No single context runs the crossing.** -/
theorem not_inOne : ¬ InOne family 0 [(), ()] 2 :=
  fun ⟨_, path⟩ => match trace_cons_iff.mp path with
    | ⟨_, first, rest⟩ => match trace_cons_iff.mp rest with
      | ⟨_, second, _⟩ => match first, second with
        | .inl ⟨_, _, one⟩, .inl ⟨_, zero, _⟩ => Nat.noConfusion (one.symm.trans zero)
        | .inl ⟨off, _, _⟩, .inr ⟨on, _, _⟩ => Bool.noConfusion (off.symm.trans on)
        | .inr ⟨_, start, _⟩, _ => Nat.noConfusion start

theorem not_joinClosed : ¬ JoinClosed family :=
  fun joins => not_inOne (((pooledLaw_exact_iff_joinClosed false).mpr joins 0 [(), ()] 2).mp
    pooled_crosses)

theorem retained_excludes : ¬ ∃ i j, Trace (retainedLaw family) (i, 0) [(), ()] (j, 2) :=
  fun crossing => not_inOne (retainedLaw_realizes_inOne.mp crossing)

end CrossingContexts

/-! ### A context that changes within one course -/

namespace ChangingContext

/-- From `0` in context `false` to `1` in context `true`, then from `1` to `2` in context `true`. -/
def relation (i : Bool) (s : Nat) (_ : Unit) (j : Bool) (t : Nat) : Prop :=
  (i = false ∧ s = 0 ∧ j = true ∧ t = 1) ∨ (i = true ∧ s = 1 ∧ j = true ∧ t = 2)

theorem joins : Trace (evolvingLaw relation) (false, 0) [(), ()] (true, 2) :=
  .cons (m := (true, 1)) (Or.inl ⟨rfl, rfl, rfl, rfl⟩)
    (.cons (Or.inr ⟨rfl, rfl, rfl, rfl⟩) (.nil (true, 2)))

theorem arrives : Arrives relation (fun i => i = false) 0 [(), ()] 2 true :=
  ⟨false, rfl, joins⟩

/-- **The course ends at `2`.** -/
theorem ends (j : Bool) (t : Nat) : ¬ relation true 2 () j t
  | .inl ⟨on, _, _, _⟩ => Bool.noConfusion on
  | .inr ⟨_, two, _, _⟩ => Nat.noConfusion two fun one => Nat.noConfusion one

/-- **The forgotten law can take a step the given context cannot follow.** -/
theorem erased_not_lifted :
    Trace (erasedLaw relation) 0 [()] 1 ∧
      ¬ ∃ j, Trace (evolvingLaw relation) (true, 0) [()] (j, 1) :=
  ⟨trace_singleton_iff.mpr ⟨false, true, Or.inl ⟨rfl, rfl, rfl, rfl⟩⟩,
   fun ⟨_, path⟩ => match trace_singleton_iff.mp path with
     | .inl ⟨on, _, _, _⟩ => Bool.noConfusion on
     | .inr ⟨_, start, _, _⟩ => Nat.noConfusion start⟩

end ChangingContext

end Becoming
