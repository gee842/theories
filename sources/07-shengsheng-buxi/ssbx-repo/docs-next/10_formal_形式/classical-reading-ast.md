# Classical Reading AST

> Status: active AST compiler boundary, 2026-05-21.  This is a reading compiler
> boundary, not a claim that Wen automatically understands all classical
> Chinese.

## Purpose

The active Wen frontend now distinguishes raw classical text from executable
R.Code.  A line like:

```text
文「道可道，非常道。」
```

is preserved and inspected as text.  It does not become a theorem or a Bool
judgment.  A later selected reading records how a human/commentarial reading
cuts and roles the text:

```text
讀 一 為 道 可 道，非 常 道
訓 一.1 道 為名 道體
訓 一.2 可 為助 可說
訓 一.3 道 為謂 道出
```

If an annotation target resolves through the typed binding context, the
annotated atom also becomes an R.Code name.  For example:

```text
名 #oooo 道體
文「道。」
讀 一 為 道
訓 一.1 道 為名 道體
判 一.1 等 道體
```

Here `訓 一.1 ... 道體` is first checked against selected reading `一`; only
then it emits `def 一.1 := 道體`, so the later `判` reaches the R core.  If the
target is not bound, the annotation remains reading evidence and reports that
no R.Code command was emitted.

## Architecture

```text
raw classical text
-> Wen.Text source spans and lex tokens
-> Wen.Reading candidate segmentations / reading forest
-> Wen.Classical.Module / Item / Annotation
-> selected reading + role annotations
-> R.Code commands
-> R.Awareness reports
```

The important point is that segmentation is not semantics.  Raw text such as
`道可道非常道` first generates a reading forest with candidates like
`道/可/道/非/常/道`, `道/可道/非常/道`, and `道可道/非常道`.  Candidate nodes now
also carry a first broad structural shape: `曰` tags a quote clause, `者` tags a
topic-comment clause, `若/苟 ... 則 ...` tags a conditional, `而/且/與/及` tags a
parallel clause, and `之` marks relation/genitive shape.  These are clause-kind
tags only; the current compiler does not yet split quote speaker/body,
topic/comment fields, or premise/conclusion fields.  The selected reading then
records atom roles: first `道` as topic/nominal object, `可` as modal, second
`道` as predicate/action, `非` as negation, `常` as attribute, final `道` as
nominal.

## Boundary

- `Foundation/R` remains language-independent.
- Chinese roles and commentary live in `Foundation/Wen`, not in R core.
- Raw text without selected reading reports `unknown` / needs-reading style
  diagnostics, never true or false.
- `Wen.Classical` is the active source compiler boundary.  The older
  `Wen.SourceModule` shape remains as a compatibility shim for the current
  R.Code elaborator, but it no longer owns parsing authority.
- The line-oriented command language remains useful for executable claims and
  migration fixtures; real classical prose enters through `文/讀/訓` items in
  the Classical AST.

## Implemented Compiler Boundary

The current Lean modules are:

```text
formal/SSBX/Foundation/Wen/Classical/AST.lean
formal/SSBX/Foundation/Wen/Classical/Parser.lean
formal/SSBX/Foundation/Wen/Classical/Lower.lean
formal/SSBX/Foundation/Wen/Classical.lean
```

`Parser` produces `Classical.Module` / `Classical.Item` values.  `Lower` bridges
those items into the existing `SourceModule.SourceCommand` compatibility shape.
`ElabToRCode` then emits `R.Code.Command`; all truth, scope, loss, operator, and
dynamic semantics remain in the R core.

Raw text items such as `文「道可道，非常道。」` only emit reading forests.
Selected reading items such as `讀 一 為 道 可 道，非 常 道` record an annotated
reading candidate.  Annotation items such as `訓 一.1 道 為名 道體` check the
selected atom and lower only when the target is a typed term/predicate binding.

## Smoke File

The first corpus-style fixture is:

```text
formal/SSBX/Foundation/Wen/samples/classical-reading-demo.wen
```

Run it with:

```bash
lake exe wen --inspect-file formal/SSBX/Foundation/Wen/samples/classical-reading-demo.wen
```

Expected behavior: raw `文` lines are tokenized without spaces, `讀` lines are
recorded as selected reading evidence, and `訓` references are checked against
selected reading atoms.  A `訓` line only emits R.Code when its target has an
explicit typed binding; otherwise it stays text-facing evidence.

Current implemented behavior:

- `讀 <label> 為 <reading>` builds a structured selected reading with source
  span and atom roles, and records whether it matches an earlier raw-text
  forest candidate.
- Reading candidates and selected readings preserve broad clause-kind tags such
  as quote, topic-comment, conditional, parallel, and relation.  They do not yet
  split quote speaker/body, topic/comment, or premise/conclusion fields; this is
  still reading evidence, not semantic proof.
- `訓 <label>.<index> <surface> <role-marker> <target>` attaches a typed role
  annotation to that atom and checks that the referenced surface matches.
- Term-like roles (`為題`, `為名`, `為狀`, `為關`) lower to an R.Code term
  definition when `<target>` resolves as `#word`, `@word`, or a declared term
  binding.  Predicate roles (`為謂`) lower to an R.Code predicate definition
  when `<target>` resolves as a declared predicate binding.
- Invalid references such as `訓 一.9 ...`, duplicate reading labels, invalid
  role markers, and surface mismatches are reported as elaboration errors.
- Reading evidence enriches `R.Awareness` diagnostics.  R.Code lowering only
  records the selected atom-to-core binding; a later `判` can prove that
  definition, but truth of the raw text or reading still requires an explicit
  law / finite executable request beyond the reading evidence itself.
- `SourceModule` delegates parsing to `Classical.Parser`; it is now a
  compatibility layer, not the active AST.

Additional fixture:

```text
formal/SSBX/Foundation/Wen/samples/daodejing-01-reading.wen
```

This file preserves the first chapter as text + selected readings + annotation
evidence.  It contains only small bound-atom smoke checks and does not claim a
complete theorem-backed interpretation of the chapter.
