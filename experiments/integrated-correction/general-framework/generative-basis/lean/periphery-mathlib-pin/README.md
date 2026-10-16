# 外围 Mathlib 版本固定 / Pin of the periphery's Mathlib

外围中用 Mathlib 的检查器（例如 [`check_correction_inquiry.py`](../universal-ethics/generative-capacity/check_correction_inquiry.py)）不在本仓库内构建 Mathlib，而是用仓库外的一个 Lake 项目：环境变量 `SYSTEMS_MATHLIB_PROJECT`，默认 `~/repos/生生不息`，工具链 `leanprover/lean4:v4.30.0-rc2`。核心与桥（[`../becoming/`](../becoming/README.md)）不依赖它：它们只用 Lean 4.29.1 的序言与 `Std`。

The periphery checkers that use Mathlib (for example [`check_correction_inquiry.py`](../universal-ethics/generative-capacity/check_correction_inquiry.py)) do not build Mathlib inside this repository; they use a Lake project outside it: the environment variable `SYSTEMS_MATHLIB_PROJECT`, by default `~/repos/生生不息`, with toolchain `leanprover/lean4:v4.30.0-rc2`. The core and the bridge ([`../becoming/`](../becoming/README.md)) do not depend on it: they use only Lean 4.29.1's prelude and `Std`.

这里保存该项目的两个小文件，原字节不变，只为在仓库内固定 Mathlib 的修订；该项目的其他内容均未复制。 / This folder keeps two small files of that project, byte for byte, only so that the Mathlib revision is pinned in the repository; nothing else of that project is copied.

| 文件 / File | sha256 | 来源 / Source |
|---|---|---|
| [`sources/lakefile.lean`](sources/lakefile.lean) | `738411c8fa58a1a15e4c01c20fb07cf56574abcf4d0f3158523c2ca41f96bc58` | `~/repos/生生不息/lakefile.lean` (modified 2026-05-18 20:20) |
| [`sources/lake-manifest.json`](sources/lake-manifest.json) | `740eef1aae725322b99872aba59cc5c902378b992bfe9122737a454f3076321b` | `~/repos/生生不息/lake-manifest.json` (modified 2026-05-09 15:51) |

复制于 2026-10-16（I5，检查器加固与可复现构建）。该项目的 `lean-toolchain` 未复制，其内容为 `leanprover/lean4:v4.30.0-rc2`（sha256 `ce4c4e3d87434b9663f46de25ce34b48a0cf0d392e0a320a0787b4674a2d7b61`）。Mathlib 修订为 `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`，与 `check_correction_inquiry.py` 的 `MATHLIB_REVISION` 相同；清单还固定 plausible、LeanSearchClient、importGraph、proofwidgets、aesop、Qq、batteries 与 Cli 的修订。

Copied on 16 October 2026 (I5, checker hardening and a reproducible build). The project's `lean-toolchain` is not copied; it reads `leanprover/lean4:v4.30.0-rc2` (sha256 `ce4c4e3d87434b9663f46de25ce34b48a0cf0d392e0a320a0787b4674a2d7b61`). The Mathlib revision is `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`, the same as `MATHLIB_REVISION` in `check_correction_inquiry.py`; the manifest also pins the revisions of plausible, LeanSearchClient, importGraph, proofwidgets, aesop, Qq, batteries and Cli.

外人复现外围：建一个 Lake 项目，用上面的工具链与 `lakefile.lean` 中的 `require mathlib … @ "ea11ccc0…"`（项目自己的 `lean_lib` 与 `lean_exe` 条目可以省去），放入 `lake-manifest.json`，运行 `lake exe cache get` 与 `lake build Mathlib`，再把 `SYSTEMS_MATHLIB_PROJECT` 指向它。这里的文件放在 `sources/` 下，所以 Becoming 检查器的模块索引与 Lean 目录都不把 `lakefile.lean` 当作模块读。

To reproduce the periphery elsewhere: make a Lake project with the toolchain above and the `require mathlib … @ "ea11ccc0…"` line of `lakefile.lean` (the project's own `lean_lib` and `lean_exe` entries can be left out), put `lake-manifest.json` in it, run `lake exe cache get` and `lake build Mathlib`, and point `SYSTEMS_MATHLIB_PROJECT` at it. The files sit under `sources/`, so neither the Becoming checker's module index nor the Lean catalogue reads `lakefile.lean` as a module.
