import Lean
import Becoming
open Lean

#eval show CoreM Unit from do
  let src ← IO.FS.readFile "names.txt"
  let mut out := ""
  for s in (src.splitOn "\n").filter (· ≠ "") do
    let n := s.toName
    match ← findDeclarationRanges? n with
    | some r => out := out ++ s!"{s}\t{r.range.pos.line}\t{r.range.pos.column}\t{r.range.endPos.line}\t{r.range.endPos.column}\n"
    | none => out := out ++ s!"{s}\tNONE\n"
  IO.FS.writeFile "ranges.tsv" out
