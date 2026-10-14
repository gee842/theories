import Lean
import Becoming

/-!
P58 decidability inventory (a periphery tool, not part of the core; run by
`DECIDABILITY-INVENTORY.py`, which writes the page `DECIDABILITY-INVENTORY.md`). For every declaration of the core's
modules: the binders whose type is a decidability family (`Decidable`, `DecidableEq`,
`DecidablePred`, or any definition unfolding to one under binders), a decided proposition
(`p ∨ ¬ p` under binders, such as the core's `Decided`, unfolded at default transparency), or an
excluded middle (the same where `p` depends on a binder ranging over propositions or predicates,
such as `∀ p : Prop, p ∨ ¬ p`); whether the statement depends on the binder; whether
the proof (or definition body) uses it; and which decidability-taking definitions the statement
mentions. Also the declarations whose result is a decidability family (decidedness proved).
Writes tab-separated rows to the path in `P58_OUT`.
-/

open Lean Meta

/-- What a binder type is, under binders: a decidability family, a decided proposition, an
excluded middle (a decided proposition for every proposition or predicate a binder ranges over),
or neither. Unfolds at default transparency, so the core's `Decided p` is read as `p ∨ ¬ p`. -/
def binderKind (t : Expr) : MetaM (Option String) := do
  try
    forallTelescopeReducing t fun xs body => do
      let body ← whnfD body
      if body.isAppOf ``Decidable then return some "decidable"
      if body.isAppOfArity ``Or 2 then
        let a := body.appFn!.appArg!
        let b ← whnfD body.appArg!
        let negOf : Option Expr :=
          if b.isAppOfArity ``Not 1 then some b.appArg!
          else match b with
            | .forallE _ d (.const ``False _) _ => some d
            | _ => none
        if let some d := negOf then
          if ← isDefEq a d then
            for x in xs do
              if a.containsFVar x.fvarId! then
                if ← forallTelescopeReducing (← inferType x) fun _ b => return (← whnfD b).isProp then
                  return some "excluded-middle"
            return some "decided"
      return none
  catch _ => return none

def skipName (n : Name) : Bool :=
  n.isInternal ||
  (match n with
   | .str _ s => s == "eq_def" || s == "eq_unfold" ||
       (s.startsWith "eq_" && (s.toList.drop 3).all Char.isDigit) || s == "inj" || s == "injEq" || s == "sizeOf_spec" ||
       s == "noConfusion" || s == "noConfusionType" || s == "casesOn" || s == "recOn" || s == "rec" ||
       s == "brecOn" || s == "below" || s == "binductionOn" || s == "ibelow" || s == "ctorIdx" ||
       s == "toCtorIdx" || s.startsWith "match_" || s.startsWith "proof_"
   | _ => false)

def clean (s : String) : String :=
  (s.replace "\n" " ").replace "\t" " " |>.splitOn " " |>.filter (· ≠ "") |> " ".intercalate

def ppClean (e : Expr) : MetaM String := do
  return clean (toString (← ppExpr e))

def inCore (m : Name) : Bool :=
  m == `Becoming || (m.getRoot == `Becoming && m != `Becoming.Bridge)

def inventory : MetaM Unit := do
  let env ← getEnv
  let out := (← IO.getEnv "P58_OUT").getD "p58-inventory.tsv"
  -- the declarations of the core
  let mut decls : Array (Name × Name × ConstantInfo) := #[]
  for (n, ci) in env.constants.toList do
    if skipName n then continue
    match ci with
    | .inductInfo _ | .ctorInfo _ | .recInfo _ | .quotInfo _ => continue
    | _ => pure ()
    let some m := env.getModuleIdxFor? n | continue
    let mod := env.header.moduleNames[m.toNat]!
    if inCore mod then decls := decls.push (mod, n, ci)
  -- first pass: definitions taking a decidability family (the primitives)
  let mut prims : NameSet := {}
  let mut rows : Array String := #[]
  for (_, n, ci) in decls do
    if ci matches .thmInfo _ then continue
    let r ← forallTelescope ci.type fun xs _ => do
      let mut found := false
      for x in xs do
        if (← binderKind (← inferType x)).isSome then found := true
      return found
    if r then prims := prims.insert n
  -- second pass: every declaration with such a binder, and every result that is one
  for (mod, n, ci) in decls do
    let kind := match ci with
      | .thmInfo _ => "theorem" | .defnInfo _ => "def" | .opaqueInfo _ => "opaque"
      | .axiomInfo _ => "axiom" | _ => "other"
    let rs ← forallTelescope ci.type fun xs body => do
      let mut acc : Array String := #[]
      -- the decidability-taking definitions the statement mentions
      let stmt ← mkForallFVars xs body
      let mentioned := stmt.getUsedConstants.filter (fun c => prims.contains c && c != n)
      let ment := ",".intercalate (mentioned.toList.map toString).eraseDups
      let val? := ci.value? (allowOpaque := true)
      let applied := val?.map (fun v => v.beta xs)
      -- result: is the declaration itself a decidability family (decidedness proved)?
      if let some k := (← binderKind body) then
        acc := acc.push s!"{mod}\t{kind}\t{n}\tRESULT\t{k}\t{← ppClean body}\t-\t-\t{ment}"
      for i in [0:xs.size] do
        let x := xs[i]!
        let t ← inferType x
        let some k ← binderKind t | continue
        let later ← mkForallFVars (xs.extract (i+1) xs.size) body
        let stmtUses := later.containsFVar x.fvarId!
        let proofUses := match applied with
          | some a => (Lean.collectFVars {} a).fvarSet.contains x.fvarId!
          | none => false
        let bi := (← x.fvarId!.getDecl).binderInfo
        let bk := if bi.isInstImplicit then "inst" else if bi.isImplicit then "implicit" else "explicit"
        acc := acc.push s!"{mod}\t{kind}\t{n}\t{i}/{xs.size}:{bk}\t{k}\t{← ppClean t}\t{stmtUses}\t{proofUses}\t{ment}"
      if acc.isEmpty && !mentioned.isEmpty then
        acc := acc.push s!"{mod}\t{kind}\t{n}\tNONE\t-\t-\t-\t-\t{ment}"
      return acc
    rows := rows ++ rs
  IO.FS.writeFile out ("\n".intercalate rows.toList ++ "\n")
  IO.println s!"{decls.size} declarations, {prims.size} decidability-taking definitions, {rows.size} rows → {out}"

#eval inventory
