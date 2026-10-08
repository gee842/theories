import Std

/-!
# Construction of grounds for a small inferential language

This companion tests a constructive route to justifying inference, rather than
declaring every product of a rule to be true. Atomic grounds are supplied as
types. Terms can retain them, pair them, project them, abstract over a possible
ground and apply a constructed function. Interpretation returns an actual
ground in the supplied type family. Closed atomic terms exist exactly when
the corresponding supplied atomic ground is inhabited.

This is a standard typed-term interpretation, not new proof-theoretic semantics
or an assumption-free justification of Lean. Atomic adequacy, the grammar and
metatheory remain explicit. A copied proof does not execute a physical event
twice or establish joint feasibility of incompatible activities.
-/

namespace Generative.InferentialGrounds

inductive Form where
  | atom : Nat → Form
  | both : Form → Form → Form
  | arrow : Form → Form → Form

inductive Position : List Form → Form → Type where
  | here : Position (a :: context) a
  | there : Position context a → Position (b :: context) a

universe u

inductive Term (Ground : Nat → Type u) : List Form → Form → Type u where
  | source (a : Nat) : Ground a → Term Ground context (.atom a)
  | use : Position context a → Term Ground context a
  | pair : Term Ground context a → Term Ground context b →
      Term Ground context (.both a b)
  | first : Term Ground context (.both a b) → Term Ground context a
  | second : Term Ground context (.both a b) → Term Ground context b
  | abstract : Term Ground (a :: context) b → Term Ground context (.arrow a b)
  | apply : Term Ground context (.arrow a b) → Term Ground context a →
      Term Ground context b

def GroundFor (Ground : Nat → Type u) : Form → Type u
  | .atom a => Ground a
  | .both a b => GroundFor Ground a × GroundFor Ground b
  | .arrow a b => GroundFor Ground a → GroundFor Ground b

def ContextGround (Ground : Nat → Type u) (context : List Form) :=
  {a : Form} → Position context a → GroundFor Ground a

def emptyContext (Ground : Nat → Type u) : ContextGround Ground [] :=
  fun p => nomatch p

def extendContext {Ground : Nat → Type u} {context : List Form} {a : Form}
    (g : GroundFor Ground a) (env : ContextGround Ground context) :
    ContextGround Ground (a :: context)
  | _, .here => g
  | _, .there p => env p

/-- Evaluation constructs a ground from the supplied source and context grounds.
No premise says that a produced sentence is true just because it was produced. -/
def extract {Ground : Nat → Type u} {context : List Form} {a : Form}
    (term : Term Ground context a) (env : ContextGround Ground context) :
    GroundFor Ground a :=
  match term with
  | .source _ g => g
  | .use p => env p
  | .pair x y => (extract x env, extract y env)
  | .first x => (extract x env).1
  | .second x => (extract x env).2
  | .abstract body => fun g => extract body (extendContext g env)
  | .apply f x => extract f env (extract x env)

variable {Ground : Nat → Type u} {context : List Form} {a b : Form}

theorem first_after_pair (x : Term Ground context a) (y : Term Ground context b)
    (env : ContextGround Ground context) :
    extract (.first (.pair x y)) env = extract x env := rfl

theorem second_after_pair (x : Term Ground context a) (y : Term Ground context b)
    (env : ContextGround Ground context) :
    extract (.second (.pair x y)) env = extract y env := rfl

theorem application_after_abstraction (body : Term Ground (a :: context) b)
    (x : Term Ground context a) (env : ContextGround Ground context) :
    extract (.apply (.abstract body) x) env =
      extract body (extendContext (extract x env) env) := rfl

theorem atomic_conservativity (Ground : Nat → Type u) (a : Nat) :
    Nonempty (Term Ground [] (.atom a)) ↔ Nonempty (Ground a) := by
  constructor
  · rintro ⟨term⟩
    exact ⟨extract term (emptyContext Ground)⟩
  · rintro ⟨ground⟩
    exact ⟨.source a ground⟩

theorem no_ground_no_closed_atom (Ground : Nat → Type u) (a : Nat)
    (absent : Ground a → False) : ¬ Nonempty (Term Ground [] (.atom a)) := by
  rintro ⟨term⟩
  exact absent (extract term (emptyContext Ground))

/-- Application to actuality still needs a source-to-claim correspondence. -/
theorem adequate_sources_give_atomic_claim (Ground : Nat → Type u)
    (Claim : Nat → Prop) (adequate : ∀ a, Ground a → Claim a)
    (a : Nat) (term : Term Ground [] (.atom a)) : Claim a :=
  adequate a (extract term (emptyContext Ground))

/-- Prior's two-rule pattern would transform any A-ground into a B-ground.
This is impossible in the displayed inhabited/empty instance, whatever the
intermediate representation C is. It rejects that pattern's uniform adequacy. -/
theorem unsupported_unpacking_impossible (C : Type u) :
    ¬ Nonempty ((Unit → C) × (C → Empty)) := by
  rintro ⟨pack, unpack⟩
  exact Empty.elim (unpack (pack ()))

/-- Evidence can be reused by this syntax; the interpretation exposes its exact
meaning as two references to the same supplied ground, not two physical acts. -/
def duplicate (Ground : Nat → Type u) (a : Form) :
    Term Ground [] (.arrow a (.both a a)) :=
  .abstract (.pair (.use .here) (.use .here))

theorem duplication_is_ground_reuse (Ground : Nat → Type u) (a : Form)
    (g : GroundFor Ground a) :
    extract (duplicate Ground a) (emptyContext Ground) g = (g, g) := rfl

end Generative.InferentialGrounds

#print axioms Generative.InferentialGrounds.extract
#print axioms Generative.InferentialGrounds.first_after_pair
#print axioms Generative.InferentialGrounds.second_after_pair
#print axioms Generative.InferentialGrounds.application_after_abstraction
#print axioms Generative.InferentialGrounds.atomic_conservativity
#print axioms Generative.InferentialGrounds.no_ground_no_closed_atom
#print axioms Generative.InferentialGrounds.adequate_sources_give_atomic_claim
#print axioms Generative.InferentialGrounds.unsupported_unpacking_impossible
#print axioms Generative.InferentialGrounds.duplicate
#print axioms Generative.InferentialGrounds.duplication_is_ground_reuse
