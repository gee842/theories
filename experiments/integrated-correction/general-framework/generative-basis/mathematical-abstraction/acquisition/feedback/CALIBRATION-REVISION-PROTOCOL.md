# Full-load consequences revise diagnostic applicability

Prospective protocol, 6 October 2026. This additive continuation preserves
[remaining_dependency.py](remaining_dependency.py), its saved outcomes, and the
[capacity erratum](REMAINING-DEPENDENCY-ERRATUM.md). It addresses one particular
join: actual full-load consequence → acquired qualification of the inherited
weak prediction → selected, feasible weak recheck. It does not claim the first
general example of applicability learning or a new ultimate undertaking.

## Actual ancestors and independently observable consequence

The main parents are `law_01_learned`, `calibration_break`, and `false_dependence`
from [remaining-dependency-results.json](remaining-dependency-results.json).
Each has retained historical weak report `[0,1]`, selected setting 1, 34 live
cells, fuel `214009/32768`, source 0, and the old productive-use component still
fulfilled. The first parent's load/waste stocks are 10/0; the latter two are
0/10. Their physical weak/full maps are respectively `01/01`, `01/00`, and
`00/00`. The last acquired its old positive weak report through a false contact.
The actual old full operation and final retention have already occurred.

No final receipt survived in the old interface. A newly formed independent
reader now samples the persistent load and waste compartments. Its supplied
contract, restricted to this one-transfer lineage, is: uniquely occupied load
10/waste 0 indicates 1; load 0/waste 10 indicates 0; otherwise indication is
unavailable. This contact changes neither stock. Structural binding uses the
retained `service_issued` control location and selected setting, the original
one-transfer path into these initially empty compartments, and the physical
context returned by the reader. The controller must check the expected context
from its old retained tag. It does not inspect the audit's success field or
resurrect a lost transient receipt. No removal, mixing or unrelated later
deposit occurs before this contact in the declared positive cases.

The new reader can also sample the actual weak-test response after an ordinary
relay command and weak challenge. This is explicitly a **new independent
contact route**, formed using current fuel/capacity; the old defective contact
law is preserved in its history. It is not a newly calibrated full-law probe.
The old weak law is stationary across the old and fresh weak tests in the
primary family. Misbound, absent and false new contacts are adverse controls.

All parent histories are reconstructed and compared to their saved bytes.
Actual source remains 0. No second full transfer, actor replenishment, resource
reset, or external supply appears. The load and waste remain distinct stocks in
the original 145-unit identity. Capacity remains 256; the real earlier peak
114 is preserved, rather than replacing it with the smaller endpoint peak.

## Candidate relation and inquiry rule

There are sixteen candidate physical maps `(W0,W1,F0,F1)`, indexed by
`W0 + 2*W1 + 4*F0 + 8*F1`. `W` is the stationary weak response and `F` the
response at the previous full operation. All sixteen mask bits begin present.
The historical weak report is retained as a prediction, not assumed to be
physical truth, so it does not eliminate candidates. The candidate family and
the interpretation of its coordinates are supplied.

A correctly bound full indication `b` at setting `r` retains precisely the
candidates with `F_r=b`: eight remain. An unknown/misbound indication retains
all sixteen. Compare that observed full outcome with the historical weak
prediction at the same setting. A match supports only that tested prediction;
a mismatch withdraws reliance on that historical prediction for full operation.
Neither result establishes full-map calibration or identifies a unique fault.

The supplied local inquiry policy activates only after this mismatch. Among
weak settings whose predicted outcomes disagree across surviving candidates,
prefer the previously exercised full setting, then the other setting. This is
a concrete discriminating inquiry under the declared family, not an optimality
or necessity claim. Its fixed scan consumes work even when no inquiry is chosen.
An absent full indication yields no mismatch-driven inquiry.

The selected weak recheck actually commands the relay, creates a new response,
acquires it through the new contact, and writes a **separate fresh record**.
Filtering `W_r=a` then leaves four candidates. In the actual failure pair,
fresh weak 1 versus full 0 establishes a same-setting discrepancy; fresh weak
0 versus full 0 contradicts the old weak report under the stationary-law
premise and establishes only current same-setting agreement. Untested `W` and
`F` coordinates remain unresolved. Even learning the entire weak map would not
determine the untested full coordinate in this family. An earlier false report
is not distinguished from every possible physical change outside this family.

The `clamped` consumer acquires the same full evidence, filters the same mask,
updates the same application status and computes the same inquiry proposal,
with the same charges. Its commit only withholds activation of that proposal.
The `conventional` consumer implements the same mask filtering and policy by
an independently expressed finite lookup/scan and must match the full trace.
No candidate count is treated as welfare or as a benefit that offsets resource
consumption; inquiry can reduce retained capability.

## Concrete storage and charges

The old 34-cell interface stays retained. Installation forms 24 additional
bounded registers: sixteen candidate-mask bits and eight registers for full
record, fresh weak record, transient contact, application/diagnosis status,
proposed setting, activated setting, scan cursor, and assembly/control phase.
Record and status registers have explicitly finite product alphabets; they are
not single binary bits. Python projection fields do not imply additional free
registers. The immutable sixteen-map recipe is supplied program structure;
each scan's work and temporary storage are charged.

Reuse the exact inherited `diagnosis.Account` tariff, with zero workspace:
work and rewrite/growth `1/64`, rent `peak*(work+1)/65536`, interface/contact
extra `1/4`, installation extra 1, retention extra `live/64`. Capacity is checked
before fuel; denied charges change nothing. The following envelopes are fixed
before execution:

| Event | Work | Temporary | Extra | Rewrites / live |
| --- | ---: | ---: | ---: | --- |
| `calibration_installation` | 24 | 8 | 1 | live 34 → 58 |
| `full_stock_contact` | 0 | 2 | 1/4 | none |
| `full_record_write` | 1 | 2 | 0 | 2 rewrites |
| `filter_full` | 16 | 2 | 0 | 16 rewrites |
| `revise_application` | 2 | 2 | 0 | 1 rewrite |
| `choose_diagnostic` | 32 | 3 | 0 | 1 rewrite |
| `commit_diagnostic` | 1 | 2 | 0 | 1 rewrite |
| `diagnostic_relay_command` | 1 | 2 | 1/4 | none |
| `diagnostic_weak_challenge` | 1 | 2 | 1/4 | native pending datum |
| `fresh_weak_contact` | 0 | 2 | 1/4 | none |
| `fresh_record_write` | 1 | 2 | 0 | 2 rewrites |
| `filter_weak` | 16 | 2 | 0 | 16 rewrites |
| `revise_diagnosis` | 2 | 2 | 0 | 1 rewrite |
| `calibration_retention` | 1 | 0 | live/64 | none |

A successfully charged contact exposes its datum; a denied contact does not.
Weak contact consumes the native pending datum on success, including a missing
or corrupt report. Record writes are charged even for missing/misbound input,
which becomes unknown, not zero. Unknown records leave the mask unchanged but
still incur the declared scan. Retention is attempted after any later failure
if installation succeeded; otherwise the inherited interface is preserved.
Before installation the entrance requires retained old interface, source 0,
and control location `service_issued` with a selected setting. A source-denied
old operation is not reclassified as an observed full failure.

## Fixed cases and observations

Run all three main parents with learned, clamped and conventional consumers
(nine cases). Add learned continuations from actual `law_10_learned`,
`law_11_learned`, and `false_positive_first` parents. On `calibration_break`,
test new full contact missing, flipped, wrong-context and wrong-setting;
new weak contact missing, flipped, wrong-context and wrong-setting; plus
the actual old `context_change` parent and `source_exhausted` parent. Finally
incur explicit waiting consumption of 1, 2 and 3 units at the primary mismatch
entrance, rather than replacing its fuel. Total: 25 prescribed cases.

Contact faults transform only the returned datum. A context fault reports 2;
a setting fault reports the opposite bit; a flip changes only the response;
missing returns no datum. The actual old changed-context parent already has
physical context 2, and cannot provide bound full evidence for old context 1.
The source-exhausted parent is denied by its original control location before
new installation. The fixed wait consumes its extra plus the normal rent term.

Save every charged event, denial and full state; preserve the entire old
endpoint and its exact source-linked ancestor. Check component completion/H/
old weak record invariance, no new source or load/waste change, all 145 units,
mask nonexpansion, true-map retention under faithful contacts, and complete
conventional equivalence. Check learned/clamped identity through proposal and
commit apart from activation. Report actual failures without tuning charges.

The proposed result is a source-bound revision of diagnostic applicability and
selection of one attainable inquiry. It does not provide another full-service
opportunity, prove a globally correct replacement map, learn ethical grounds,
or implement the separate common-support/source-location dependency branch.
