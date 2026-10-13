#!/bin/zsh
# usage: mk.sh WORK_DIR Module.Name   (e.g. mk.sh /path/attraction Becoming.Attraction)
# Compiles WORK_DIR/<Module/Path>.lean against main's core in ztree/, then audits axioms
# of every constant the module declares. WORK_DIR may hold several new modules; build them
# in import order. Nothing outside WORK_DIR is written.
Z=/private/tmp/claude-501/-Users-ren-theories/e2a8824b-beaa-4b8e-9f70-f9716e01002c/scratchpad/p69/ztree
D=$1; M=$2; P=${M//./\/}
LEAN=$HOME/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean
cd $D || exit 1
export LEAN_PATH=$D
$LEAN -o $P.olean $P.lean 2>&1 | head -${LINES_MAX:-120}
[ -f $P.olean ] && [ $P.olean -nt $P.lean ] || { echo "BUILD FAILED"; exit 1; }
cat > .ax_${M//./_}.lean <<LEANEOF
import Lean
import $M
open Lean Elab Command
#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? \`$M | throwError "no module"
  let mut count := 0
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      let axioms ← liftCoreM <| Lean.collectAxioms n
      if axioms.size > 0 then logInfo m!"AXIOMS {n} {axioms.toList}"
  logInfo m!"CONSTANTS {count}"
LEANEOF
$LEAN .ax_${M//./_}.lean 2>&1 | grep -v "injEq" | head -40
grep -nE "sorry|^axiom|Classical|import Mathlib|native_decide|decide :=" $P.lean && echo "CHECK TOKENS ABOVE" || echo "no forbidden tokens"
