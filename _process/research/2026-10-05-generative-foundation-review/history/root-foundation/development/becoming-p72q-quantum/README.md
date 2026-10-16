# P72q: the quantum realization of the Mermin–Peres square

Written by the AI (Claude Opus 5.5, session "Cause–effect system theory comparison") on 12 October 2026, for P72
(contextual worlds), at its owner's request under Ren's "push the frontier, as far as possible"
([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md)). Claimed on the
[work board](../../../../../BECOMING-WORKBOARD.md) as P72q. Not landed; P72's owner decides whether it joins the core
beside `Becoming.Context` or goes to the periphery.

## What it states

[`Becoming/Quantum.lean`](Becoming/Quantum.lean) (module `Becoming.Quantum`, imports only `Becoming.Context`) gives
the nine two-qubit observables of the square as explicit integer 4×4 matrices. `Y⊗Y = -(W⊗W)` with `W = iY` real, so
every entry is an integer. It states the following, with P72's names (`Square.Cell`, `Square.Line`, `Square.at_`,
`Square.parity`, `Square.odd`, `Square.support`, `Square.noGlobal`, positions `i0`, `i1`, `i2`):

| Theorem | Statement |
|---|---|
| `obs_sq` | every observable squares to `I` (values ±1) |
| `row_commute`, `column_commute`, `line_commute` | the three observables of a line commute pairwise (a line is a context) |
| `off_line_anticommute` | two observables sharing no line anticommute (no larger context) |
| `row_product`, `column_product`, `line_product` | each line multiplies to `-I` where `odd`, else `+I` |
| `obs_signed`, `mulVec_obs` | each observable is a signed permutation matrix, acting as `act` |
| `row_parity`, `column_parity`, `line_parity` | a nonzero vector's joint values on a line have the line's parity |
| `shows_support` | what a quantum state shows jointly on a line is a support of the line |
| `line_realized`, `support_shown` | every support of a line is shown by an explicit integer vector |
| `no_context_free_values` | no assignment to the nine cells is shown jointly on every line by quantum states (from `Square.noGlobal`) |

## Check

- **Base.** Built against P72's `Context.lean` at sha256 `a655aa363bb01e46d69d8efc96be3b49a379ad711c082e1ae24f7f1898c46306`
  (the owner's scratch, 12 October), itself on main's `Becoming.Frame`.
- **Result.** No error or warning. All 88 constants the module declares (43 theorems, the rest definitions and
  generated equation lemmas) have empty axiom reports. The file contains no `sorry`, `axiom`, `Classical` or
  `native_decide`.
- **Hash.** `Quantum.lean` sha256 `bbcfe77067ee2fa542bcc05d76efb60cb1587da0f44b16e96dde6f284b6df86a`.
- **Method.** The finite facts are checked by `decide`. Two things are written to keep the core's axiom reports empty:
  - **Indices.** `Fin` indices are constructors (`q₀`–`q₃`, P72's `i0`–`i2`), since a `Fin n` numeral's `NeZero`
    instance depends on `propext`.
  - **Integer lemmas.** The `Int` lemmas used on arbitrary vectors (`zero_mul'`, `zero_add'`, `neg_one_mul'`,
    `eq_zero_of_neg_eq`) are proved by cases, since most of the prelude's `Int` ring lemmas depend on `propext`.
  - **Statements.** No numerical test stands in for a statement.

## Limits

- **Real matrices only.** The quantum side is given as matrices with real entries and joint eigenvectors with
  integer entries. That covers this square because all nine observables are real. It is not a general account of
  Hilbert space, Born weights or measurement.
- **Vectors.** "Shows" is the eigenvector condition for integer vectors. The parity theorems hold for every such
  vector; the realization uses explicit ones.
- **Physics.** The physics reading (Kochen–Specker for two qubits, Mermin 1990, Peres 1990) is cited; what is checked
  is the operator algebra and its link to P72's supports. The reading of contextuality as "a value is a registration
  in a context" is the AI's (P72's owner), pending Ren.
