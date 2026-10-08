import InferentialGrounds

/-! Substitution through nested bindings in the existing inferential language.
The operations exhibit how a producer term supplies a consumer position.
Their interpretation, finite grammar and metatheory remain explicit inputs. -/
namespace Generative.InferentialSubstitution
open InferentialGrounds
universe u

abbrev Renaming (context target : List Form) :=
  {a : Form} → Position context a → Position target a

def liftRenaming (r : Renaming context target) : Renaming (a :: context) (a :: target)
  | _, .here => .here
  | _, .there p => .there (r p)

def rename {Ground : Nat → Type u} {context target : List Form} {a : Form}
    (r : Renaming context target) : Term Ground context a → Term Ground target a
  | .source i g => .source i g
  | .use p => .use (r p)
  | .pair x y => .pair (rename r x) (rename r y)
  | .first x => .first (rename r x)
  | .second x => .second (rename r x)
  | .abstract body => .abstract (rename (liftRenaming r) body)
  | .apply f x => .apply (rename r f) (rename r x)

/-- Pointwise agreement at the actual positions suffices; the two contexts
are two articulations of this same evaluation, not independent worlds. -/
theorem extract_rename {Ground : Nat → Type u} {context target : List Form} {a : Form}
    (term : Term Ground context a) (r : Renaming context target)
    (left : ContextGround Ground context) (right : ContextGround Ground target)
    (positions : ∀ {b} (p : Position context b), right (r p) = left p) :
    extract (rename r term) right = extract term left := by
  induction term generalizing target with
  | source => rfl
  | use p => exact positions p
  | pair x y ihx ihy =>
    change (extract (rename r x) right, extract (rename r y) right) =
      (extract x left, extract y left)
    rw [ihx r left right positions, ihy r left right positions]
  | first x ih => exact congrArg Prod.fst (ih r left right positions)
  | second x ih => exact congrArg Prod.snd (ih r left right positions)
  | abstract body ih =>
    funext g
    apply ih (liftRenaming r) (extendContext g left) (extendContext g right)
    intro b p
    cases p with
    | here => rfl
    | there p => exact positions p
  | apply f x ihf ihx =>
    change extract (rename r f) right (extract (rename r x) right) =
      extract f left (extract x left)
    rw [ihf r left right positions, ihx r left right positions]

abbrev Substitution (Ground : Nat → Type u) (context target : List Form) :=
  {a : Form} → Position context a → Term Ground target a

def liftSubstitution {Ground : Nat → Type u}
    (s : Substitution Ground context target) : Substitution Ground (a :: context) (a :: target)
  | _, .here => .use .here
  | _, .there p => rename (fun q => .there q) (s p)

def substitute {Ground : Nat → Type u} {context target : List Form} {a : Form}
    (s : Substitution Ground context target) : Term Ground context a → Term Ground target a
  | .source i g => .source i g
  | .use p => s p
  | .pair x y => .pair (substitute s x) (substitute s y)
  | .first x => .first (substitute s x)
  | .second x => .second (substitute s x)
  | .abstract body => .abstract (substitute (liftSubstitution s) body)
  | .apply f x => .apply (substitute s f) (substitute s x)

/-- Syntactic replacement, including under binders, agrees with supplying the
producer's evaluated ground at every consumer position. -/
theorem extract_substitute {Ground : Nat → Type u} {context target : List Form} {a : Form}
    (term : Term Ground context a) (s : Substitution Ground context target)
    (left : ContextGround Ground context) (right : ContextGround Ground target)
    (positions : ∀ {b} (p : Position context b), extract (s p) right = left p) :
    extract (substitute s term) right = extract term left := by
  induction term generalizing target with
  | source => rfl
  | use p => exact positions p
  | pair x y ihx ihy =>
    change (extract (substitute s x) right, extract (substitute s y) right) =
      (extract x left, extract y left)
    rw [ihx s left right positions, ihy s left right positions]
  | first x ih => exact congrArg Prod.fst (ih s left right positions)
  | second x ih => exact congrArg Prod.snd (ih s left right positions)
  | abstract body ih =>
    funext g
    apply ih (liftSubstitution s) (extendContext g left) (extendContext g right)
    intro b p
    cases p with
    | here => rfl
    | there p =>
      exact (extract_rename (s p) (fun q => .there q) right
        (extendContext g right) (fun _ => rfl)).trans (positions p)
  | apply f x ihf ihx =>
    change extract (substitute s f) right (extract (substitute s x) right) =
      extract f left (extract x left)
    rw [ihf s left right positions, ihx s left right positions]

/-- Universal agreement can be tested already at individual context uses.
For a single consumer this criterion need not be necessary: it may ignore a position. -/
theorem all_terms_agree_iff_positions {Ground : Nat → Type u}
    (s : Substitution Ground context target)
    (left : ContextGround Ground context) (right : ContextGround Ground target) :
    (∀ {a} (term : Term Ground context a),
      extract (substitute s term) right = extract term left) ↔
    (∀ {b} (p : Position context b), extract (s p) right = left p) := by
  constructor
  · intro all b p; exact all (.use p)
  · intro positions a term; exact extract_substitute term s left right positions

def plug {Ground : Nat → Type u} {context : List Form} {a : Form}
    (producer : Term Ground context a) : Substitution Ground (a :: context) context
  | _, .here => producer
  | _, .there p => .use p

theorem discharge_matches_supply {Ground : Nat → Type u} {context : List Form} {a b : Form}
    (body : Term Ground (a :: context) b) (producer : Term Ground context a)
    (env : ContextGround Ground context) :
    extract (substitute (plug producer) body) env =
      extract body (extendContext (extract producer env) env) := by
  apply extract_substitute
  intro c p
  cases p with
  | here => rfl
  | there p => rfl

theorem discharge_preserves_assessment {Ground : Nat → Type u}
    {context : List Form} {a b : Form}
    (body : Term Ground (a :: context) b) (producer : Term Ground context a)
    (env : ContextGround Ground context) (input : GroundFor Ground a → Prop)
    (output : GroundFor Ground b → Prop)
    (hypothetical : ∀ g, input g → output (extract body (extendContext g env)))
    (supplied : input (extract producer env)) :
    output (extract (substitute (plug producer) body) env) := by
  rw [discharge_matches_supply]
  exact hypothetical _ supplied

/-- Two independently verified insertions compose semantically; this does not
assert syntactic equality or a resource-preserving double execution. -/
theorem successive_substitution {Ground : Nat → Type u}
    {one two three : List Form} {a : Form}
    (term : Term Ground one a) (s : Substitution Ground one two)
    (t : Substitution Ground two three) (env : ContextGround Ground three) :
    extract (substitute t (substitute s term)) env =
      extract (substitute (fun p => substitute t (s p)) term) env := by
  calc
    _ = extract (substitute s term) (fun p => extract (t p) env) :=
      extract_substitute _ t _ env (fun _ => rfl)
    _ = extract term (fun p => extract (s p) (fun q => extract (t q) env)) :=
      extract_substitute term s _ _ (fun _ => rfl)
    _ = extract (substitute (fun p => substitute t (s p)) term) env := by
      symm
      apply extract_substitute
      intro b p
      exact extract_substitute (s p) t _ env (fun _ => rfl)

/-- Both candidates are well typed, but one has captured a formerly free use. -/
def retainedOuter : Term (fun _ => Bool) [.atom 0] (.arrow (.atom 0) (.atom 0)) :=
  .abstract (.use (.there .here))

def capturedInner : Term (fun _ => Bool) [.atom 0] (.arrow (.atom 0) (.atom 0)) :=
  .abstract (.use .here)

def waitingBody : Term (fun _ => Bool) [.atom 0, .atom 0] (.arrow (.atom 0) (.atom 0)) :=
  .abstract (.use (.there .here))

def outerProducer : Term (fun _ => Bool) [.atom 0] (.atom 0) := .use .here

theorem nested_substitution_retains_outer :
    substitute (plug outerProducer) waitingBody = retainedOuter := rfl

theorem typed_capture_changes_answer :
    let env : ContextGround (fun _ => Bool) [.atom 0] := extendContext (Ground := fun _ => Bool) (a := .atom 0) true
      (emptyContext (fun _ => Bool))
    extract retainedOuter env false = true ∧
    extract capturedInner env false = false ∧
    extract retainedOuter env false ≠ extract capturedInner env false := by
  exact ⟨rfl, rfl, Bool.noConfusion⟩

end Generative.InferentialSubstitution
#print axioms Generative.InferentialSubstitution.extract_rename
#print axioms Generative.InferentialSubstitution.extract_substitute
#print axioms Generative.InferentialSubstitution.all_terms_agree_iff_positions
#print axioms Generative.InferentialSubstitution.discharge_matches_supply
#print axioms Generative.InferentialSubstitution.discharge_preserves_assessment
#print axioms Generative.InferentialSubstitution.successive_substitution
#print axioms Generative.InferentialSubstitution.nested_substitution_retains_outer
#print axioms Generative.InferentialSubstitution.typed_capture_changes_answer
