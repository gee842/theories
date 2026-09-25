---
name: Lean 4 syntax atoms must avoid «»-bracketed CJK
description: When declaring `notation` / `syntax` for wenyan tokens in Lean 4, use bare CJK chars (e.g., `已`), not «...»-quoted form
type: feedback
originSessionId: c55c7f11-0b44-438a-8520-1b94e91d9763
---
In the SSBX project, the codebase uses `«已»`, `«终»`, etc. as Lean identifiers (via Lean's `«...»` raw-identifier quotation). However, when declaring `notation "«已»" => Shi.ji`, Lean rejects this with "invalid atom" because the parser sees `«已»` as a *raw identifier token*, not a string atom.

**Why:** Lean 4's `«...»` is reserved for identifier quoting. Atoms in `notation` / `syntax` declarations must be string-tokenizable, and `«ident»` is parsed as ident before atom-string check.

**How to apply:** Two distinct contexts with opposite rules:

| Context | Form | Reason |
|---|---|---|
| `notation` / `syntax` atom | bare CJK (`"已"`, `"比爻"`) | Lean's `«…»` is parsed as ident, can't be a string atom |
| `def` / `theorem` name | «»-quoted (`def «判型良»`, `theorem «文核同源»`) | CJK identifiers need raw-ident escaping to be valid Lean names |

- `notation "已" => Shi.ji` ✓ ; `notation "«已»" => Shi.ji` ✗ → "invalid atom"
- `def «判型良» := ...` ✓ ; `def 判型良 := ...` ✗ → "expected token"

The `reservedTokens` in `BaguaWenSpec.lean` are bare CJK content (without «»), consistent with the notation rule.

**Related:** For `sepBy(term, "；")`, the `macro_rules` pattern needs `$[$is]；*` (literal CJK semicolon inside `$[…]…*`), not `$is;*` or `,*`. The separator in the pattern must match exactly.
