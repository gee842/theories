# Changing the AI Trajectory — V7.2

*4 October 2026. Conditional working paper. Originally drafted by Claude from Ren's direction; revised by Codex at Ren's request. The text is AI-drafted or drawn from the author's corpus. Model review and numerical checks are not independent human certification.*

Start with [START-HERE](START-HERE.md). V7.2 integrates the requirement that shared viability and effective correction persist through changes in capability, successors and institutions. It preserves [V7.1](../v7.1/README.md) and its release record.

The central discussion is **THEORY §10.4**. The aim is to preserve corrective functions while institutions and rules remain open to legitimate challenge and replacement. A correcting policy's existence does not establish that people can obtain the evidence, authorize it and execute it in time.

**SUPPLEMENT S16** proves one reduced joint certificate linking rule capture, effective liability, selection of load and host viability. It is a conditional composition of existing models, with explicit initial-state and continuing bounds. It does not derive durable funding or authority, compute the full correctable kernel, or validate the present-path diagnosis. **TESTS, Test N** specifies an institutional experiment that can reject the proposed mechanism; it has not been run.

## Reading the edition

| File | Purpose |
|---|---|
| [THEORY](THEORY.md) | Abstract, Chinese guide and core argument; §10.4 contains the constructive target. |
| [SUPPLEMENT](SUPPLEMENT.md) | Proofs and model boundaries; S13 maps open interfaces, S15 maps numerical checks, S16 develops the new target and reduced certificate. |
| [DISCUSSION](DISCUSSION.md) | Intellectual lineage, alternative paths and institutional design. |
| [CLAIMS](CLAIMS.md) | Claim status and dependencies; §11 records this integration and its provenance. |
| [EVIDENCE](EVIDENCE.md) | Sources and empirical gaps; EV19 distinguishes theoretical predecessors from evidence of implementation. |
| [TESTS](TESTS.md) | Cruxes and proposed studies; Test N and §6.5 specify correction through institutional change. |
| [CHANGELOG](CHANGELOG.md) | What changed from V7.1. |
| [LEDGER](LEDGER.md) | Preservation, provenance and verification. |
| [RELEASE-REVIEW](RELEASE-REVIEW.md) | Bounded review findings, resolutions and remaining limits. |

For a formal read, follow §§2–6 with S2–S6, then §§8–11 with S13 and S16. For alignment, read §6.6 with §10.4. For the institutional test, read C4, Test N, protocol §6.5 and Study 3 together. The constructive target and the empirical diagnosis have separate burdens of proof.

## Sources and rebuilding

Edit `src/core/`, `src/supp/`, `src/disc/` and `src/reg/`; root Markdown files are assembled outputs. Stable result declarations and references are resolved by the assembler. The 128 declaration identities inherited from V7.1 are preserved; `jointcorrection` is the one new declaration, in S16.

Run from `v7.2/`:

```sh
python3 src/assemble_v72.py
python3 src/refs_v72.py
python3 xref_v72.py
python3 checks_v72.py > checks_v72.log 2>&1
python3 verification/audit_v72.py
```

The reference generator reads the assembled documents; the cross-reference check assembles again. The numerical suite retains the inherited blocks and adds **RC**, four groups testing the reduced joint certificate and limits of local diagnostics. There are 45 default blocks; `python3 checks_v72.py RC` selects the addition. A counted group can contain several assertions. Passing these checks does not establish a real institution's performance.

See [verification/summary.json](verification/summary.json), [checks_v72.log](checks_v72.log) and the review record for the completed verification and its limits. No publication or external distribution is part of this revision.