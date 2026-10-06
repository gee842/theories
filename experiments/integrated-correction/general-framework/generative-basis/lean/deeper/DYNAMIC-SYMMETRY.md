# Symmetry does not select between static and toggle dynamics

6 October 2026. AI-authored extension of [DynamicUnderdetermination.lean](DynamicUnderdetermination.lean), responding to [Ren's exact directive](../../../../../../sources/15-codex-theory-conversations/2026-10-06-no-assumptions-directive.md): “there shall be no assumptions in generative model”. This is a finite proof audit of one proposed route to selecting dynamics, not a completion of that foundational task. Explicit or justified assumptions are not silently exempted from the stronger requirement.

**Result:** the existing static and toggle processes on the same `Bool` states and `Unit` actions both have exactly one successor and predecessor at every state, permit reversal of each step using the same action, and preserve their entire step relation under every bijective Boolean renaming. They remain different: static permits a self-loop and toggle forbids every self-loop. No state map can identify their full step relations.

[DynamicSymmetry.lean](DynamicSymmetry.lean) proves this with explicit property definitions. It also proves that every injective Boolean map is pointwise identity or negation, and that both maps satisfy the explicit bijection predicate. Thus the arbitrary-renaming result does not inspect a selected subset of renamings or rely on an empty quantified class.

The final theorem, `symmetric_dynamics_remain_underdetermined`, is a closed existence statement about these two defined models. It shows that the conjunction of totality, determinism, same-label step symmetry, unique predecessors and all Boolean renaming symmetries does not uniquely determine the law. It does not classify all laws satisfying those properties, exclude derivation from richer independently justified grounds, identify actual physical dynamics or derive the existence of change.

## Verification

The final fresh build passed with **Lean 4.29.1**, commit `f72c35b3f637c8c6571d353742168ab66cc22c00`. It rebuilt the unchanged `GenerativeCore` and `DynamicUnderdetermination` sources before compiling the new module, with `LEAN_PATH` pointing only to a fresh temporary directory for local imports. The installed standard library belongs to the pinned compiler.

All **20 new theorem audits** and **27 inherited audits** reported no axiom dependencies; all three compiler commands exited zero without warnings. Source checks rejected proof holes, unchecked computation shortcuts and custom axiom/constant declarations. Every new theorem has an explicit dependency audit, and all three source hashes remained unchanged during the build.

The [receipt](dynamic-symmetry-verification.json) records source, compiler, toolchain and output SHA-256 hashes, exact compiler commands, module exit codes and audited declarations. [Compiler output](verification/DynamicSymmetry.txt) contains the complete three-module output. The existing `check.py`, its frozen receipt and earlier verification files were not altered by this check.

Empty dependency reports concern Lean's named axiom dependencies. They do not remove its type theory, inference rules, definitions, or the explicitly chosen finite models. The useful advance is narrower and positive: this stronger set of proposed structural requirements is now ruled out as a sufficient discriminator between the two laws.

## Reproduce the exact compilation

Run this from the directory containing this note. It rebuilds the local imports and prints the audits without overwriting the saved receipt:

```sh
python3 - <<'PY'
from pathlib import Path
import os, subprocess, tempfile

root = Path.cwd()
toolchain = (root / 'lean-toolchain').read_text().strip()
assert toolchain == 'leanprover/lean4:v4.29.1'
version = subprocess.check_output(['lean', '+' + toolchain, '--version'], text=True)
assert 'version 4.29.1,' in version
print(version.strip())
prefix = subprocess.check_output(['lean', '+' + toolchain, '--print-prefix'], text=True)
compiler = Path(prefix.strip()) / 'bin' / 'lean'
sources = {
    'GenerativeCore': root.parent / 'GenerativeCore.lean',
    'DynamicUnderdetermination': root / 'DynamicUnderdetermination.lean',
    'DynamicSymmetry': root / 'DynamicSymmetry.lean',
}
with tempfile.TemporaryDirectory(prefix='dynamic-symmetry-recheck-') as temporary:
    build = Path(temporary)
    for name, source in sources.items():
        (build / (name + '.lean')).write_bytes(source.read_bytes())
    env = dict(os.environ, LEAN_PATH=str(build))
    for name in sources:
        subprocess.run([str(compiler), '-o', name + '.olean', name + '.lean'],
                       cwd=build, env=env, check=True, timeout=180)
PY
```

## Connection to further work

The named connection is **a proposed structural basis → determination of admissible dynamics**. The two models retain the same carrier and all tested properties while differing on state change. A next candidate discriminator must identify additional content and justify it, or show that the intended explanatory target admits both laws. Defining change as required selects against static only by putting that requirement into the basis; this proof does not judge whether such a requirement can independently be justified.

This extends the existing underdetermination result without reopening the accepted conditional foundation. It supplies no new ethical ground, empirical result or reason to abandon the stronger necessary-foundation investigation.
