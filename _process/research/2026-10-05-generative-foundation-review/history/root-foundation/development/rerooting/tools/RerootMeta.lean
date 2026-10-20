import Lean
import RerootImports
open Lean

def kindOf : ConstantInfo → String
  | .axiomInfo _ => "axiom" | .defnInfo _ => "def" | .thmInfo _ => "theorem"
  | .opaqueInfo _ => "opaque" | .quotInfo _ => "quot" | .inductInfo _ => "inductive"
  | .ctorInfo _ => "ctor" | .recInfo _ => "rec"

def valueOf : ConstantInfo → Option Expr
  | .defnInfo d => some d.value | .thmInfo t => some t.value | .opaqueInfo o => some o.value
  | _ => none

#eval show CoreM Unit from do
  let env ← getEnv
  let names := env.header.moduleNames
  let modOf (n : Name) : String :=
    match env.getModuleIdxFor? n with
    | some i => toString (names[i.toNat]!)
    | none => "?"
  let src ← IO.FS.readFile "RerootModules.txt"
  let wanted : List String := (src.splitOn "\n").filter (· ≠ "")
  let mut rows : Array Json := #[]
  let mut seen : Std.HashMap Name String := {}
  for (n, ci) in env.constants.map₁.toList do
    let m := modOf n
    if wanted.contains m then
      let ty := ci.type.getUsedConstants
      let va := (valueOf ci).map (·.getUsedConstants) |>.getD #[]
      for c in ty ++ va do
        unless seen.contains c do seen := seen.insert c (modOf c)
      rows := rows.push (Json.mkObj [("name", toJson n.toString), ("module", toJson m),
        ("kind", toJson (kindOf ci)), ("internal", toJson (n.isInternal)), ("type", toJson (ty.map Name.toString)),
        ("value", toJson (va.map Name.toString))])
  let mods := Json.mkObj (seen.toList.map fun (c, m) => (c.toString, toJson m))
  IO.FS.writeFile "reroot-meta.json" (Json.mkObj [("decls", Json.arr rows), ("modules", mods)]).compress
  IO.println s!"{rows.size} constants"
