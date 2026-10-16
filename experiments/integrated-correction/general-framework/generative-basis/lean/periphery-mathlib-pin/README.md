<a id="外围-mathlib-版本固定--pin-of-the-peripherys-mathlib"></a>
# Pin of the periphery's Mathlib

The periphery checkers that use Mathlib (for example [`check_correction_inquiry.py`](../universal-ethics/generative-capacity/check_correction_inquiry.py)) do not build Mathlib inside this repository; they use a Lake project outside it: the environment variable `SYSTEMS_MATHLIB_PROJECT`, by default `~/repos/生生不息`, with toolchain `leanprover/lean4:v4.30.0-rc2`. The core and the bridge ([`../becoming/`](../becoming/README.md)) do not depend on it: they use only Lean 4.29.1's prelude and `Std`.

This folder keeps two small files of that project, byte for byte, only so that the Mathlib revision is pinned in the repository; nothing else of that project is copied.

| File | sha256 | Source |
|---|---|---|
| [`sources/lakefile.lean`](sources/lakefile.lean) | `738411c8fa58a1a15e4c01c20fb07cf56574abcf4d0f3158523c2ca41f96bc58` | `~/repos/生生不息/lakefile.lean` (modified 2026-05-18 20:20) |
| [`sources/lake-manifest.json`](sources/lake-manifest.json) | `740eef1aae725322b99872aba59cc5c902378b992bfe9122737a454f3076321b` | `~/repos/生生不息/lake-manifest.json` (modified 2026-05-09 15:51) |

Copied on 16 October 2026 (I5, checker hardening and a reproducible build). The project's `lean-toolchain` is not copied; it reads `leanprover/lean4:v4.30.0-rc2` (sha256 `ce4c4e3d87434b9663f46de25ce34b48a0cf0d392e0a320a0787b4674a2d7b61`). The Mathlib revision is `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`, the same as `MATHLIB_REVISION` in `check_correction_inquiry.py`; the manifest also pins the revisions of plausible, LeanSearchClient, importGraph, proofwidgets, aesop, Qq, batteries and Cli.

To reproduce the periphery elsewhere: make a Lake project with the toolchain above and the `require mathlib … @ "ea11ccc0…"` line of `lakefile.lean` (the project's own `lean_lib` and `lean_exe` entries can be left out), put `lake-manifest.json` in it, run `lake exe cache get` and `lake build Mathlib`, and point `SYSTEMS_MATHLIB_PROJECT` at it. The files sit under `sources/`, so neither the Becoming checker's module index nor the Lean catalogue reads `lakefile.lean` as a module.
