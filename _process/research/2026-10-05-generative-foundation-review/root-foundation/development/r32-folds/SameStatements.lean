import Lean
import Becoming
import Becoming.MoveOutcomeProcesses
import Becoming.ClassifiedBeliefProcesses
import Becoming.ContextArrivalTraces
open Lean

/-!
# Theorems of the run with the same statement (R32, B9)

Run by `samestatements.py` (through the connectivity measure's restore and dump runner) against the
run's compiled modules; it reads the environment and declares nothing. For every theorem of a
tracked module it writes one JSON line: its name `n`, module `m`, kind `k` (`thm`), the hash `h` of
its type with binder names erased (`Expr.hash` does not read binder names) and the universe level
parameters `u`. Theorems with equal hashes are then compared by `samestatements.py` through the
printed key `e`, the type with every binder named alike (so only the bound structure, binder kinds and
constants count).
-/

def toolchainRoots : List Name := [`Init, `Std, `Lean, `Lake]

/-- The type with every binder name replaced by `x`, so two statements differing only in bound
names print alike. -/
partial def anonymize : Expr → Expr
  | .forallE _ d b bi => .forallE `x (anonymize d) (anonymize b) bi
  | .lam _ d b bi => .lam `x (anonymize d) (anonymize b) bi
  | .letE _ t v b nd => .letE `x (anonymize t) (anonymize v) (anonymize b) nd
  | .app f a => .app (anonymize f) (anonymize a)
  | .mdata _ e => anonymize e
  | .proj s i e => .proj s i (anonymize e)
  | e => e

#eval show CoreM Unit from do
  let env ← getEnv
  let some out ← IO.getEnv "THEOREM_CONNECTIVITY_OUT"
    | throwError "THEOREM_CONNECTIVITY_OUT is not set"
  IO.FS.withFile out .write fun h => do
    for i in [0:env.header.moduleNames.size] do
      let m := env.header.moduleNames[i]!
      if toolchainRoots.contains m.getRoot then continue
      for ci in env.header.moduleData[i]!.constants do
        if let .thmInfo v := ci then
          let e := anonymize v.type
          let line := Json.mkObj [("n", toJson ci.name.toString), ("m", toJson m.toString),
            ("k", toJson "thm"), ("t", Json.arr #[]), ("v", Json.arr #[]),
            ("h", toJson (toString e.hash)), ("u", toJson (v.levelParams.map toString)),
            ("e", toJson (toString e))]
          h.putStrLn line.compress
