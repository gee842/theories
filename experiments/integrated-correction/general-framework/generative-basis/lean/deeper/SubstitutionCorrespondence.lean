import Becoming.Readout
import InferentialSubstitution

/-!
# Binding-preserving substitution, an instance of `Becoming.Readout`

In `InferentialSubstitution` a substitution replaces every use of a position of one context by a
producer term of another, under nested binders; its exact position criterion states when every
consumer evaluates alike before and after the replacement. This periphery module reads that
criterion on the core's law of readings through parts.

* An assignment of grounds to a context is a configuration whose parts are its positions
  (`part`); a consumer, a term with its form, reads an assignment by evaluating it (`read`).
  Evaluation reads only through the positions (`through`, with function extensionality), and the
  direct use of a position reads that position (`direct`): the premises of
  `Readout.agree_iff_parts`.
* The periphery's substitution lemma (`extract_substitute`) says that each consumer's reading
  after replacement is its reading of the assignment the producers supply (`supplied`,
  `supplies`). So, by `Readout.supplied_agree_iff_parts`, every consumer evaluates alike before
  and after the replacement exactly where each producer supplies the ground at its position
  (`all_terms_agree_iff_positions_by_core`).

The substitution lemma, the language and the interpretation of binding keep the periphery's scope;
the core supplies the criterion, not the lemma. The core does not import this module.
-/

namespace Becoming.SubstitutionCorrespondence

open Generative.InferentialGrounds Generative.InferentialSubstitution Becoming.Readout

universe u

variable {Ground : Nat → Type u} {context target : List Form}

/-- A position of a context with its form. -/
abbrev Place (context : List Form) := (b : Form) × Position context b

/-- A consumer of a context: a term with its form. -/
abbrev Consumer (Ground : Nat → Type u) (context : List Form) := (a : Form) × Term Ground context a

/-- The ground an assignment gives at a position. -/
def part (env : ContextGround Ground context) (p : Place context) : GroundFor Ground p.1 :=
  env p.2

/-- A consumer reads an assignment by evaluating it. -/
def read (c : Consumer Ground context) (env : ContextGround Ground context) :
    GroundFor Ground c.1 :=
  extract c.2 env

/-- The direct use of a position. -/
def use (p : Place context) : Consumer Ground context := ⟨p.1, .use p.2⟩

/-- **Evaluation reads only through the positions.** -/
theorem through : ThroughParts (part (Ground := Ground) (context := context)) read := by
  intro c env env' agree
  have same : @env = @env' := by
    funext b p
    exact agree ⟨b, p⟩
  exact congrArg (fun e : ContextGround Ground context => read c e) same

/-- **The direct use of a position reads that position.** -/
theorem direct :
    ReadsDirectly (part (Ground := Ground) (context := context)) read use :=
  fun _ _ _ same => same

/-- The assignment the producers of a substitution supply from an assignment of the target. -/
def supplied (s : Substitution Ground context target) (right : ContextGround Ground target) :
    ContextGround Ground context :=
  fun p => extract (s p) right

/-- **A consumer's reading after replacement is its reading of the supplied assignment**
(`extract_substitute`). -/
theorem supplies (s : Substitution Ground context target) (c : Consumer Ground context)
    (right : ContextGround Ground target) :
    extract (substitute s c.2) right = read c (supplied s right) :=
  extract_substitute c.2 s (supplied s right) right fun _ => rfl

/-- **Every consumer evaluates alike before and after replacement exactly where each producer
supplies the ground at its position** (`Readout.supplied_agree_iff_parts`). -/
theorem all_terms_agree_iff_positions_by_core (s : Substitution Ground context target)
    (left : ContextGround Ground context) (right : ContextGround Ground target) :
    (∀ {a} (term : Term Ground context a), extract (substitute s term) right = extract term left) ↔
      (∀ {b} (p : Position context b), extract (s p) right = left p) :=
  have core := supplied_agree_iff_parts (through (Ground := Ground) (context := context)) direct
    (replaced := fun c t => extract (substitute s c.2) t) (supply := supplied s)
    (supplies s) (t := right) (s := left)
  ⟨fun all {b} p => core.mp (fun c => all c.2) ⟨b, p⟩,
   fun positions {a} term => core.mpr (fun p => positions p.2) ⟨a, term⟩⟩

end Becoming.SubstitutionCorrespondence
