# P88 integration package / 接续包

This supplements the preserved [README](README.md), which records the draft's state at preservation. The original [module](lean/Becoming/OrderNormal.lean), [task](evidence/TASK.md), evidence and [provenance](provenance.json) are unchanged. The added files prepare this exact draft for integration; they do not certify a check or add proofs. P78 `Becoming.Order` must land first.

## Prepared delta / 已准备的增量

- [Study, Chinese](docs/study/p88_zh.md) and [English](docs/study/p88_en.md): exact hypotheses, producer/consumer connection, retained boundaries and review scope. `{S}` and receipt/count placeholders are filled by the shared kit.
- [Configuration](config.py): root/checker/Lean README registration, bilingual plan/chapter/reading entry and two records. The distinct new records are [normal form](docs/records/normal-forms-need-decided-apartness.json) and [least footprint](docs/records/least-footprint-where-idleness-decided.json).
- [Record delta](record_delta.py): the census construction advances `exchanges-commute-unless-joined`; its existing counterexamples remain. Both P78 records link the distinct additions and narrow their old open items. This also repairs the stale P78 hypothesis which called its already-proved P78b converse unproved.

## Usage / 用法

Use [the shared landing kit](../becoming-landing-kit/README.md). With its directory as `KIT`, this package as `RUN`, the landing checkout as `W`, the pre-landing commit as `BASE`, and the assigned study number as `S`:

```text
python3 -B KIT/land_lean.py RUN W
[serialized actual core and periphery checks, inventory review]
python3 -B KIT/land_docs.py RUN W S BASE
python3 -B KIT/make_records.py RUN W REVIEWED_AT_UTC S
python3 -B KIT/repoint.py RUN W BASE
[the kit's catalogue, render, map and consistency checks]
```

`config.py` is also importable into a combined P86–P88 run, provided the integrator preserves each package key and prefix and adjusts the starting section passed to this package's `record_delta.py`. For a combined run starting at section `S`, pass this delta its actual P88 section, not the first package's number. Its registration follows `Order`; its chapter open-item replacements target the P77–P85 landing text. Re-read any anchor failure; do not silently skip edits. The reading entry must be reconciled against `BASE`, as required by the kit.

## Reviewed scope / 审读范围

Task coverage has been assessed against the source statements without adding proofs. The relation-only reachability theorem requires symmetric joining and finite arrangements but no decision. Normal-form construction requires Boolean **apartness** decisions for different named exchanges on a finite stretch. The necessity result concerns Nat-valued invariants compared on that stretch, not arbitrary codomains. Census existence carries forward under any commutation and both ways when sides split; all `Reorders` have that split requirement. The least footprint uses a global idleness decision; its existence converse additionally needs decidable equality of relata. The Lean source's informal disjunction “takes part or is moved” is not promoted into a stronger constructive result: the exact predicate used here is **not idle**, `¬ (¬ present ∧ Unmoved)`.

There is no unnamed, Foata-layer or unbounded normal form, no construction of a least Boolean footprint without idleness decided, no concrete undecidable-idleness world, and no actual continuous-time correspondence. `Reorders` retains supplied sides. No ethical conclusion follows.

Preparation validation: Python syntax, JSON syntax, configured declarations/section headings against the preserved source, and every preservation hash were checked. No Lean checker, canonical record mutation, work-board edit or commit was performed by the package preparer. The historical logs remain insufficient to accept the integrated bytes. The integrating session must record actual consolidated verification and any additional review.
