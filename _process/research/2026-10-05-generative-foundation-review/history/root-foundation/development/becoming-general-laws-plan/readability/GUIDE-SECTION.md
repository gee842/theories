# Proposed section for _process/RESULT-WORKFLOW.md (draft, not applied)

## 怎样写一条记录 / Writing a record

先说成果做了什么，再说它的确切条件；只写定理或论证实际承担的边界。轮次、回执、会话与“未新增”的说明属于沿革和证据，不属于主张。

Say what the result does, then its exact conditions. Write only the boundaries the theorem or argument actually carries. Rounds, receipts, sessions and "nothing new was added" belong to history and evidence, not to the claim.

| Field | What goes in it | Limit (en / zh chars) |
|---|---|---|
| `title` | A name, not the statement. | 100 / 40 |
| `statement` | What the result does, or what the target asks, in one or two positive sentences. No Lean names, P-numbers, sections, dates or receipts. | 300 / 150 |
| `claim` | The exact statement with its conditions written in, when `statement` is not already exact. A family of laws goes to `laws`, one item per law with its declarations. | 1500 / 700 |
| `laws` | Optional. One law per item, paired zh/en, with the declarations that prove it (checked against `references`). | 420 / 190 each |
| `hypotheses` | Premises the result uses: logical commitments, supplied laws, normative commitments, correspondence assumptions. | 420 / 190 each |
| `does_not_show` | Substantive non-implications only: a converse that fails, a stronger reading not reached, a correspondence not supplied. One sentence each; name a `witness` declaration where one exists. | 8 items, 240 / 110 each |
| `counterexamples` | Witnessed cases with their source. | — |
| `standard_boundaries` | Keys for boundaries shared by many records (discrete steps, decidability, formal law vs actual systems, omission is not refutation …), defined once in `standard-boundaries.json`. Do not write them out. | — |
| `not_required` | Targets: what the target does not ask. | 6 items, 200 / 90 each |
| `progress` | Targets, assessments, arguments: one line per completed connection with its boundary and the study anchor. | 16 items, 240 / 110 each |
| `validation_scope` | The current evidence in one paragraph: kind of evidence and where its receipts are. | 600 / 260 |
| `next_delta` | The next substantive step, stated positively. | 400 / 180 |
| `history` | Everything about rounds: who asked, when, which P-number or section, which receipt, what was reused or not recounted. | — |
| `text_versions` | Hash-bound snapshots of earlier record bytes, written by the migration. | — |

Do not write in the public fields (title, statement, claim, laws, does_not_show, not_required, progress, counterexamples, next_delta, overview):

- the status in other words ("remains open", "is unproved": the status field says it);
- "no new theorem / Lean run / experiment / independent review" (that is `validation_scope`);
- round numbers, section numbers, receipt timestamps, session ids, "this round", "has landed";
- another record's status or scope (link it as a dependency or related result);
- instructions to later sessions ("do not reopen") — those go on the work board.

**Replace, do not append.** When a round adds a boundary, re-read the existing items and fold the new one into the item it refines, or replace an item it supersedes; record the change in `history`. The migration snapshot and git keep every earlier wording.

**Checks.** `research.py check` runs the readability lint. For schema 2 its rules are errors; for schema 1 they are warnings. A changed schema-1 record may not lengthen `limitations`, `validation_scope` or `correspondence`: migrate it to schema 2 first. The lint judges form only; whether a boundary is substantive is the author's reading.
