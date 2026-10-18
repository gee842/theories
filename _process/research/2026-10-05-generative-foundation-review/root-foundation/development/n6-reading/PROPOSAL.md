# N6: the reading pass the N1 renaming left open (proposal to Ren)

Board item N6, claimed in 77733b06b. Branch `n6-reading`, in its own worktree, rebased on main at
9b9e7951b (after L1, S1, G1, G2, A1, F1, G3, L2, C1 and U2c landed). **Nothing here is landed; it waits for Ren's yes.**

N5 (b84e722ea) renamed 175 Lean declarations to the vocabulary adopted in section 7 of the
[naming study](../../REGISTRATION-VOCABULARY-STUDY.md) and left the prose for a reading pass. This
pass reads each sentence that still used a retired word and rewrites it in the adopted words where
the sentence meant that sense. It was not done by substitution: every row of
[PROPOSAL-FULL.md](PROPOSAL-FULL.md) was written after reading its sentence, and the senses that
are not the retired one stay.

## What changed

| Where | Files | Edits |
|---|---|---|
| Lean docstrings and comments of the Becoming package | 64 modules | 960 |
| The chapter, English and Chinese editions, glossary included | 2 | 492 |
| Live fields of the result records (title, statement, claim, laws, hypotheses, scope, dependencies, related, correspondence, next step) | 58 records | 1,151 |

Every edit is a block in [`edits/`](edits/), with its sense, applied to the base by
[`reading_pass.py apply`](reading_pass.py), so the pass can be rerun and every block's count is
checked. Record edits are written from [`specs/records/`](specs/records/) (one file per record or
small group, each with its reasons in its docstring). [PROPOSAL-FULL.md](PROPOSAL-FULL.md) lists
every block: current wording, proposed wording, sense.

## On the rebase

The readings were written against 77733b06b; the edits are reapplied to main's text, and every block's
count is checked again. Where main had rewritten a sentence since, the block was read again:

- The L1 landing split the chapter's bullet "Learnable exactly where a reading of the future" and
  added the D40 reading after it. The bullet's block now stops where main's bullet stops, and the
  D40 reading is reworded the same way, its meaning kept ("a learnable feature", "an extrapolation
  given nothing", "what `fromLaw` is built from").
- The G1 and G2 landings stated the gap for one's own act and the general form of favouring what
  reaches beyond, and removed the sentences calling them open (in the chapter's §8.2 row and in
  selection-through-registration's scope and next step). Those four blocks are dropped; main's new
  sentences already use the adopted words.
- The L2 landing reworded the §8.2 "Learning" row itself ("feature", "extrapolation"); the two
  blocks for it are dropped. A1 added a second use of the where-a-level-couples reading in §8.4,
  which the reading's block now covers (count 2), and a third "不观察" in the zh open-readings list.
  G3 reworded the §8.2 "Selection, causes and experiment" row; the block for `Becoming.Testing`'s
  couplings follows its new punctuation.
- [`left_on_head.py`](left_on_head.py) lists every sentence main added since 77733b06b that still
  holds a retired word after the pass: 156 on 9b9e7951b. Most are kept senses (an experiment's
  record of what a run took in `Becoming.LawAlongRun`, the seeking target in `Becoming.LastChange`,
  Lean hypotheses, links to records, logical refutation, Ren's quoted words, the periphery's
  classified beliefs). The ones in a retired sense are read in
  [`edits/zz-head-9b9e.txt`](edits/zz-head-9b9e.txt) and
  [`specs/records/r36_head.py`](specs/records/r36_head.py): A1's §7 opening ("Where §3 says that a
  formation registers a condition", now that §3 itself says couples into) and its §3 reference,
  in both editions; C1's "a comparison of courses ... does not register it" → "does not show it",
  in the chapter and in what-taking-all-excludes; G3's "`Becoming.Testing`'s registration as the
  projection" → couplings, in `Becoming.LawAlongRun` and a-law-through-a-projection-along-one-run;
  L2's "a record read through a map" → a prefix, in `Becoming.Labels`.

## By sense (study section 7)

| Sense | Retired → adopted | Blocks |
|---|---|---|
| S2 | registers / is registered (a level reaching a formation) → **couples into** (by threshold, by level); "observes" → coupled by level; what a coupling passes → **shows**, **passes**; feedback **carries** | 878 |
| S1 | registration as a function of configurations → **map**; registered course/future → course/future **through the map**; the relation a map draws → **lumping** (归并) | 465 |
| S7 | registrations in context → what a context **shows**, a claim **lies within** a context; a registration within what it registers → **a family of readings** within what it reads, which **says** a reading | 280 |
| L-prefix | the record of a course → its **prefix** (前段) | 235 |
| L-extrap | learner → **extrapolation** (外推), which **proposes** (提出) or **stays silent** (默) | 208 |
| S3 | registers alike → **alike through g's couplings** (经 g 的耦合无别) | 155 |
| L-elim | hypotheses → **candidates** (候选); learning by refutation → **extrapolation by elimination** (逐除外推) | 133 |
| S5 | refutes (a web, a model, a confound) → **excludes** (排除); belief → **the class alike through g** | 115 |
| S4 | registration closure → **coupling closure** (耦合闭包) | 100 |
| L-miss | refuted (a proposal) → **misses** / **accords** (不合 / 相合) | 102 |
| L-feature | target → **feature** (特征) | 73 |
| ALT | options; a model of the options → **alternatives** (备择); a **map** of them | 70 |
| N5 | a retired Lean name left in live prose → its current name (RENAME-TABLE.json) | 57 |
| TEXT | wording around a changed word | 46 |
| L-built | learner given the world → extrapolation **built from the process / the law** | 43 |
| S6 | claims registering → claims that **tell apart**; an equivalence **respecting** the claims | 38 |
| L-fix, ZH, ZH-keep | the Gold sense of identifying → fixing; Chinese wording | 8 |

## What stays, on reading

- **Logical refutation.** "Refutable", "unrefuted", "cannot be refuted", 不能被否证, Kelly's
  refutation from finite data, Markov's principle: double negation and the topology of runs, not
  the register sense.
- **Physical records and registers.** The record of an experiment (what a run has taken, in
  `Becoming.Experiment` and `Becoming.Mechanism`), the measurement's record in
  `Becoming.Observation`, Entropy's record in the conserved amount, a qubit register, evidence
  records, 登记名册 and the 成果登记表.
- **Human learners and epistemic belief** in the periphery's empirical records (a child learning
  words, an archive case, "reasonable belief"), and the periphery's `MachineInstances` learner.
- **Inquiry's belief and target, and the seeking target**: those are the modules' own senses.
- **识** only for a formation's course through the lumping its own couplings make (option (b)),
  and in Ren's quoted and historical uses. Where a delegated reading said "识 itself stays Ren's",
  it now says "the word 识 itself stays Ren's".
- **Ren's words**, quoted verbatim, including "belief", "registration" in quotations, and the
  chapter's table of retired Lean names (kept by design).
- **Record ids and anchors**, history, `text_versions`, references, proof bindings and declaration
  lists: frozen by the tool; only live fields change.

## Statements unchanged

- Lean: `apply` refuses any edit that reaches code (`code_of` of every changed module equals the
  base's). The core checker passed in the tree on the changed files (receipt
  `becoming-checks/20261018T171240.509140Z`), and `check_fallible_inquiry.py` passed for
  `Becoming.FallibleInquiry` (receipt `fallible-inquiry-checks/20261018T174801.206046Z`); records
  whose proofs sit in a changed file are rebound to the receipt covering it, after reading the
  change.
- Records: the JSON round-trips; only the live fields listed above change, and each changed
  record gets a history note saying its claim is unchanged.
  Eleven English statements were shortened to the render's limit of 300 characters; the
  shortened sentences say the same.
- `make research-render` and `research-check` pass on the branch (the 82 reading-drift entries are
  the base's; the argument pages and reading registers are unchanged). On 9b9e7951b
  `research-links` reports no broken link, and `research-test` passes (171 tests, one skipped).
  The receipts of the earlier runs on the branch (core 20261018T094652.463397Z and
  20261018T101831.943492Z, FallibleInquiry 20261018T095146.390681Z and 20261018T102455.825667Z)
  were for pre-rebase bytes and now bind nothing; they stay on the
  branch, and the integrator decides whether they land.
  Generated pages whose content depends on untracked files (the Lean inventory, file counts,
  the manifest) are left to be rendered in the main checkout at landing.

## Readings touched (meaning kept)

Readings are reworded only where they used a retired word, with the meaning kept:

- Taken by Ren or agreed: the-split-that-makes-sense, contextual-registration and
  gluing-under-parity ("a value is a registration in context" → "what a context shows"),
  what-a-finite-history-refutes ("a finite record" → "a finite prefix"),
  loops-within-what-a-law-reads and how-loops-form ("the blindness of Runaway" → "the distance
  not coupling in"; "what registers it" → "what carries it"), determinacy-up-to-likeness
  (direction agreed: "what nothing registers" → "what no claim tells apart").
- Delegated (DELEGATED-CHOICES): D37 sensitivity ("registration is sensitivity" → "coupling is
  sensitivity"), D39 coupling strength ("how strongly a formation registers" → "how strongly a
  level couples into a formation"), the counterfactual readings, 明 in seeking-boundary
  ("registration reaching what support does not mark" → "coupling that lets in what support does
  not mark"), where-a-move-is-formed.
- identification-where-runs-part, related/1, restated the withdrawn reading "settled only when
  taken"; it is reworded and the withdrawal noted.
- Historical narratives of how 识 was chosen (subthreshold-registration, testing-within-registration)
  are kept as history, with a note on the 18 October decision; quoted earlier readings such as
  "a model answerable to registration" stay quoted as the AI's earlier reading.

## Notes on Ren's wording

Ren's words are provenance, not warrant; these are the places where the pass judged them.

- **"Registration" as dualist (17 October).** The pass agrees for the core sense, a formation said
  to register its world, which reads a writer and a register into a relation that the theory
  states as coupling. It does not extend the judgment to the physical senses (an experiment's
  record, a machine register, a measurement), which are relations inside the unfolding and stay.
- **Ren's approved title "Selection through a model of the options" (16 October).** The study's
  row 15 offered "a map of the alternatives"; the pass applies it to the record's statement and
  laws, where "map" says exactly what the Lean states, and changes the title. The correspondence
  keeps "model", because its reading answers Ren's "cognitive model" and a map is the formal part
  of it, not all of it. Ren may prefer to keep the 16 October title; the id is unchanged either
  way.
- **识.** Keeping 识 for a formation's course through its own lumping (option (b)) keeps Ren's word
  where it means what the theory states; elsewhere the formal words are more exact.

## Left for Ren

1. **Yes or no to the pass**, and any rows to change ([PROPOSAL-FULL.md](PROPOSAL-FULL.md)).
2. **Names** ([NAMES.md](NAMES.md)): declarations that still carry a retired sense
   (`Order.order_registers`, the ReferencePlan theorem names, `Contacts.Blind`, the `Registration`
   namespace of `Becoming.Revision`, TypicalRuns' record names, and others found). Proposed only;
   each would be an N5-style migration.
3. **The selection title** above.

## Follow-ups noticed, not done here

- DELEGATED-CHOICES (en and zh) uses the retired senses throughout its dated decisions (D26, D37,
  D39, D44 and others, for example "admission does not register it"). It is a register of dated
  decisions, each original kept above its revisions, and was outside this pass's scope; reading it
  would be its own item, with the revisions dated rather than rewritten.

- wisdom-root-part-one, related/1, still uses the retired labels "the one axiom … G0".
- Some docstring lines now exceed 100 characters (most in LevelCoupling, 21 → 34); the base has
  many such lines and no check enforces a width.
- Record titles changed, so generated anchors in the record pages change; research-links checks
  every link.
