import Lean
import Becoming.Testing
open Lean Elab Command

/-- Audit every constant declared in `Becoming.Testing` (including generated auxiliaries). -/
elab "#audit_module " m:ident : command => do
  let env ← getEnv
  let some idx := env.getModuleIdx? m.getId | throwError "no module"
  let mut total := 0
  let mut bad : Array (Name × Array Name) := #[]
  for (n, _) in env.constants.toList do
    if env.getModuleIdxFor? n == some idx then
      total := total + 1
      let axs ← liftCoreM (Lean.collectAxioms n)
      if axs.size > 0 then bad := bad.push (n, axs)
  logInfo m!"{m.getId}: {total} constants, {bad.size} with axioms: {bad.toList}"

#audit_module Becoming.Testing
