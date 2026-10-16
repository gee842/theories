<a id="外围-mathlib-版本固定--pin-of-the-peripherys-mathlib"></a>
# 外围 Mathlib 版本固定

> **中文版（2026-10-17）。** 正典文本是[英文版](README.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

外围中用 Mathlib 的检查器（例如 [`check_correction_inquiry.py`](../universal-ethics/generative-capacity/check_correction_inquiry.py)）不在本仓库内构建 Mathlib，而是用仓库外的一个 Lake 项目：环境变量 `SYSTEMS_MATHLIB_PROJECT`，默认 `~/repos/生生不息`，工具链 `leanprover/lean4:v4.30.0-rc2`。核心与桥（[`../becoming/`](../becoming/README.md)）不依赖它：它们只用 Lean 4.29.1 的序言与 `Std`。

这里保存该项目的两个小文件，原字节不变，只为在仓库内固定 Mathlib 的修订；该项目的其他内容均未复制。

| 文件 | sha256 | 来源 |
|---|---|---|
| [`sources/lakefile.lean`](sources/lakefile.lean) | `738411c8fa58a1a15e4c01c20fb07cf56574abcf4d0f3158523c2ca41f96bc58` | `~/repos/生生不息/lakefile.lean` (modified 2026-05-18 20:20) |
| [`sources/lake-manifest.json`](sources/lake-manifest.json) | `740eef1aae725322b99872aba59cc5c902378b992bfe9122737a454f3076321b` | `~/repos/生生不息/lake-manifest.json` (modified 2026-05-09 15:51) |

复制于 2026-10-16（I5，检查器加固与可复现构建）。该项目的 `lean-toolchain` 未复制，其内容为 `leanprover/lean4:v4.30.0-rc2`（sha256 `ce4c4e3d87434b9663f46de25ce34b48a0cf0d392e0a320a0787b4674a2d7b61`）。Mathlib 修订为 `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`，与 `check_correction_inquiry.py` 的 `MATHLIB_REVISION` 相同；清单还固定 plausible、LeanSearchClient、importGraph、proofwidgets、aesop、Qq、batteries 与 Cli 的修订。

外人复现外围：建一个 Lake 项目，用上面的工具链与 `lakefile.lean` 中的 `require mathlib … @ "ea11ccc0…"`（项目自己的 `lean_lib` 与 `lean_exe` 条目可以省去），放入 `lake-manifest.json`，运行 `lake exe cache get` 与 `lake build Mathlib`，再把 `SYSTEMS_MATHLIB_PROJECT` 指向它。这里的文件放在 `sources/` 下，所以 Becoming 检查器的模块索引与 Lean 目录都不把 `lakefile.lean` 当作模块读。
