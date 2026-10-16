# Changing the AI Trajectory — V7.3

*5 October 2026. Conditional working paper. AI-assisted development and review are not independent human certification.*

Start with [START-HERE](START-HERE.md). This edition extends preserved [V7.2](../history/v7.2/README.md) from a protected destination toward a feasible transition: a bounded mathematical construction, a worked institutional illustration and a proposed empirical comparison. [RELEASE-REVIEW](RELEASE-REVIEW.md) explains why completed development and review warrant the upgrade, with its limits.

| File | Purpose |
|---|---|
| [THEORY](THEORY.md) | Core argument; §11.6 states the new constructive contribution and implementation boundary. |
| [SUPPLEMENT](SUPPLEMENT.md) | S16 supplies a protected region; S17 develops the finite transition and its explicit assumptions. |
| [DISCUSSION](DISCUSSION.md) | X10 gives the worked procurement transition and retains the wider institutional alternatives. |
| [TESTS](TESTS.md) | Test N and its bounded pilot extension are proposed and unrun. |
| [EVIDENCE](EVIDENCE.md) | Empirical gaps and primary-source lineage, including EV20. |
| [CLAIMS](CLAIMS.md) | §12 records new claims and provenance; earlier records remain preserved. |
| [CHANGELOG](CHANGELOG.md) | Changes from V7.2. |
| [LEDGER](LEDGER.md) | Preservation, checkpoint and verification method. |

The new transition assumes its temporary powers can be exercised and its continuing operating conditions remain in force. It does not prove a real institution can preserve them through all future changes. The contribution is a conditional construction and a testable operational proposal.

## Sources and rebuilding

Edit `src/core/`, `src/supp/`, `src/disc/` and `src/reg/`; root Markdown files are assembled outputs. Run from `v7.3/`:

```sh
python3 src/assemble_v73.py
python3 src/refs_v73.py
python3 xref_v73.py > verification/xref.log 2>&1
python3 checks_v73.py > checks_v73.log 2>&1
python3 verification/audit_v73.py
```

Completed verification: 249 counted checks passed, zero failed, across 46 blocks; assembly, references and baseline preservation passed. The three fresh bounded reviews support the upgrade within its stated scope. The suite retains 45 inherited blocks and adds PT. Use `python3 checks_v73.py PT` for the new transition checks. No institutional experiment, public release or external distribution is implied by passing them.