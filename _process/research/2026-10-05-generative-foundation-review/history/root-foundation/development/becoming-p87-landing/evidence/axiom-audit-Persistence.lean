import Lean
import Becoming.Persistence
open Lean Elab Command
#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? `Becoming.Persistence | throwError "no module"
  let mut count := 0
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      let axioms ← liftCoreM <| Lean.collectAxioms n
      if axioms.size > 0 then logInfo m!"AXIOMS {n} {axioms.toList}"
  logInfo m!"CONSTANTS {count}"
