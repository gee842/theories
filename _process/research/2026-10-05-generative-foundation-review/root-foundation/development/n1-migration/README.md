# N1 migration package (prepared, not applied)

18 October 2026. AI-authored. This folder prepares the renaming that the [naming study](../../REGISTRATION-VOCABULARY-STUDY.md) adopted in its section 7, so that it can be reviewed before anything changes. Nothing here has been applied. Ren's instruction for N1 and N2 was "still no renames"; his later "please continue" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md#rens-go-to-continue-18-october-2026)) is read as a go for additive work, not as lifting that instruction.

- [migration_dry_run.py](migration_dry_run.py) reads the canonical Lean files (not the check receipts), the result records and the chapter. It writes the two files below and changes nothing else.
- [MIGRATION-DRY-RUN.md](MIGRATION-DRY-RUN.md) is the table to review: 30 definitions with their adopted names, and 126 theorem names with a name proposed by substitution. The same data, with the files and records each name appears in, is in `MIGRATION-DRY-RUN.json`.

As of this run: no proposed name clashes with an existing one; every definition in the table was found; 89 Lean files and 30 records name at least one entry.

## How the names were made

- **Definitions** are renamed by an explicit table, each name chosen from study section 7. Examples: `Web.Registers` → `Web.CoupledInto`, `Web.RegistersAlike` → `Web.AlikeThrough`, `Web.Belief` → `Web.ClassThrough`, `Web.Refutes` → `Web.Excludes`, `Learning.record` → `Learning.prefix`, `Learning.Refuted` → `Learning.Misses`, `Learning.Holds` → `Learning.Accords`, `Learning.learner` → `Learning.byElimination`, `Parting.worldLearner` → `Parting.fromProcess`, `Learnable.withWorld` → `Learnable.fromLaw`, `Likeness.Registers` → `RespectsClaims`.
- **Theorem names** are proposed by substitution, with the sense depending on the module family:
  - in the web modules (Testing, Selection, Response, Runaway, Feedback, …), "registers" becomes "couples", "refutes" becomes "excludes" and "belief" becomes "class";
  - in the learning modules (Learning, Learnable, Identification, Parting and their run instances), "record" becomes "prefix", "refuted" becomes "missed", "holds" becomes "accords" and "learner" becomes "byElimination".
- The logical sense of "unrefuted" and "refutable" (a double negation, P58b; `Horizon.Refutable`) is kept. Modules outside the two families are not touched; for example, Experiment's "record" keeps its sense.

## Decisions needed before applying

1. **Argument order of `Web.CoupledInto`.** `Web.Registers obs g c` means that c couples into g.
   - (A) Keep the argument order and name it `Web.CoupledInto obs g c`, read "g has c coupled into it". This keeps every call site's arguments.
   - (B) Reorder to `Web.CouplesInto obs c g`, which reads in English order but touches every call site's arguments.
   - The AI recommends (A).
2. **Scope.**
   - (i) Rename the 30 definitions and the 126 theorem names.
   - (ii) Rename the definitions and the theorem families named after them (`Web.RegistersAlike.refl` and the like), and leave the other theorem names for a later pass.
   - The AI recommends (ii) first: it is smaller and every change is mechanical.
3. **Old names.** Keep each old name for one cycle as a deprecated alias (`@[deprecated]`, statement unchanged), so that records and other sessions' work keep resolving, then remove the aliases in a later pass.
4. **Order and owner.** Apply on one branch, by one session, after the queue is empty; no other session may be renaming the same files. Then:
   - rebind the records naming a renamed declaration, with a history note;
   - explain the retired words once in the chapter's glossary, as for G0 and Part I/II;
   - land through the queue with one checker run.

## What is not in this package

- Docstring and record wording. Most of the vocabulary lives in prose (about 2,000 occurrences of `regist…` in the Lean), and that is changed by reading, not by substitution.
- The adjacent words of study section 6.4 (`Admits`, "model", `Reads`).
