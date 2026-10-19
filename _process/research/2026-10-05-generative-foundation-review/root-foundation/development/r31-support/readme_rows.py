#!/usr/bin/env python3
"""R31 (one-shot): the README rows that cite a declaration R31 moved name the module now holding it
(rowcheck.py lists them), and the rows and chapter sentences that described what moved say where it
is. Each replacement occurs exactly once. usage: python3 -B readme_rows.py (from anywhere)"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CH = ROOT / 'theories/becoming/chapters'

EDITS = {
    PKG / 'README.md': [
        # Regions
        ("not with it (`Clearing.loses_beyond`): a part",
         "not with it (`Clearing.loses_beyond`, in `Becoming.Clearing`): a part"),
        ("undermine another (`Clearing.renewing_over_resource`), and",
         "undermine another (`Clearing.renewing_over_resource`, in `Becoming.Clearing`), and"),
        # Interdependence
        ("need not return (`Clearing.closure_supported`); significance bounded by the whole is the condition "
         "(`bounded_whole`); where the losses lie within a region, the verdict bounded by it is the condition's "
         "(`Web.retains_bounded_iff_retains`), so always where the feeding closure is the whole "
         "(`Flow.within_closure_iff_retains`), while in the clearer's web the two part "
         "(`Clearing.within_closure_yet_loses`); the condition enters only as a hypothesis of the comparisons; "
         "the reading is the AI's |",
         "need not return (`Clearing.closure_supported`); the continuation condition does not enter: where "
         "significance bounded by a region meets it (bounded by the whole it is the condition, `bounded_whole`; "
         "within a region holding the losses the bounded verdict is the condition's, "
         "`Web.retains_bounded_iff_retains`, so where the feeding closure is the whole, "
         "`Flow.within_closure_iff_retains`; in the clearer's web the two part, "
         "`Clearing.within_closure_yet_loses`) is `Becoming.BoundedSignificance`; the reading is the AI's |"),
        # Dependence
        ("stepwise readings of events and their relations; the arithmetic on natural numbers the layers share |",
         "stepwise readings of events and their relations |"),
        # Significance
        ("exceeds the margin (`Flow.Balances.loses_iff_beyond_margin`); a drawer",
         "exceeds the margin (`Flow.Balances.loses_iff_beyond_margin`, in `Becoming.Retaining`); a drawer"),
        ("license the free rider and disagree (`Clearing.centers_disagree`);",
         "license the free rider and disagree (`Clearing.centers_disagree`, in `Becoming.Clearing`);"),
        ("with no axiom, the exact boundary of the generative space with balance only where it is used "
         "(`Flow.widens_iff_within_margin_at`),",
         "with no axiom, the exact boundary of the generative space with balance only where it is used "
         "(`Flow.widens_iff_within_margin_at`, in `Becoming.Retaining`),"),
        ("; the stepwise classes and loss: an undermining event",
         "; in `Becoming.Retaining`, with no condition, the stepwise classes and loss: an undermining event"),
        # ValuationFrames
        ("and `universal_reason`, comparison and extension, the models",
         "and `universal_reason`, the models"),
        # Feedback
        ("within what their difference reaches (`Flow.Balances.comparison_within_difference`); the condition "
         "enters only as a hypothesis of three witnesses;",
         "within what their difference reaches (`Flow.Balances.comparison_within_difference`); the condition "
         "does not enter, and the three witnesses taking it as a hypothesis are in `Becoming.BoundedSignificance`;"),
    ],
    PKG / 'README.zh.md': [
        ("有时不被接纳（`Clearing.loses_beyond`）：", "有时不被接纳（`Clearing.loses_beyond`，在 `Becoming.Clearing`）："),
        ("却仍可损害他者（`Clearing.renewing_over_resource`），", "却仍可损害他者（`Clearing.renewing_over_resource`，在 `Becoming.Clearing`），"),
        ("闭包之外的不必返回（`Clearing.closure_supported`）；以整体为界的意义就是公理（`bounded_whole`）；损失都在区域之内时，"
         "以区域为界的判断就是公理的判断（`Web.retains_bounded_iff_retains`），所以供给闭包是整体时总是"
         "（`Flow.within_closure_iff_retains`），而在清除者的网中两者分开（`Clearing.within_closure_yet_loses`）；"
         "公理只作为比较的假设出现；",
         "闭包之外的不必返回（`Clearing.closure_supported`）；延续条件不出现：以区域为界的意义与它相遇之处（以整体为界即该条件，"
         "`bounded_whole`；损失都在区域之内时以区域为界的判断即该条件的判断，`Web.retains_bounded_iff_retains`，所以供给闭包是整体时总是，"
         "`Flow.within_closure_iff_retains`；在清除者的网中两者分开，`Clearing.within_closure_yet_loses`）在 "
         "`Becoming.BoundedSignificance`；"),
        ("事件与关系的逐步读法；各层共用的自然数算术 |", "事件与关系的逐步读法 |"),
        ("失去有意义的延续（`Flow.Balances.loses_iff_beyond_margin`）；",
         "失去有意义的延续（`Flow.Balances.loses_iff_beyond_margin`，在 `Becoming.Retaining`）；"),
        ("并彼此分歧（`Clearing.centers_disagree`）；", "并彼此分歧（`Clearing.centers_disagree`，在 `Becoming.Clearing`）；"),
        ("平衡只在所用之处（`Flow.widens_iff_within_margin_at`）；",
         "平衡只在所用之处（`Flow.widens_iff_within_margin_at`，在 `Becoming.Retaining`）；"),
        ("（`Flow.Balances.comparison_within_difference`）；公理只作为三个见证的假设出现；",
         "（`Flow.Balances.comparison_within_difference`）；公理不出现，以它为假设的三个见证在 `Becoming.BoundedSignificance`；"),
    ],
    CH / 'THE-THEORY-OF-BECOMING.md': [
        ("The condition enters only as a hypothesis of three witnesses.",
         "The condition enters only as a hypothesis of three witnesses, stated since R31 in "
         "[Becoming.BoundedSignificance](../../../experiments/integrated-correction/general-framework/generative-basis/"
         "lean/becoming/Becoming/BoundedSignificance.lean)."),
    ],
    CH / 'THE-THEORY-OF-BECOMING.zh.md': [
        ("与 `universal_reason`、比较与扩展（`Comparison.outgrows`）、表明每个假设都需要的模型",
         "与 `universal_reason`、表明每个假设都需要的模型"),
        ("条件只作为三个见证的假设出现。",
         "条件只作为三个见证的假设出现，自 R31 起陈述在 "
         "[Becoming.BoundedSignificance](../../../experiments/integrated-correction/general-framework/generative-basis/"
         "lean/becoming/Becoming/BoundedSignificance.lean)。"),
    ],
}

for path, pairs in EDITS.items():
    text = path.read_text()
    for old, new in pairs:
        if old not in text and new in text:
            continue
        assert text.count(old) == 1, (path.name, old[:80], text.count(old))
        text = text.replace(old, new)
    path.write_text(text)
    print(path.name, len(pairs))
