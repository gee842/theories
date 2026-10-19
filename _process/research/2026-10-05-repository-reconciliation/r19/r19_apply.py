"""R19: state living significance as the Lean shows (docs only). Run from the repository root."""
import sys

EDITS = {
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md': [
        ("Normatively, living significance says that living and further generation within the whole have basic positive normative significance; at the level of claims, every living claim has significance from every standpoint (`Valuation.Significant`).",
         "Normatively, living significance says that every living claim has significance from every standpoint (`Valuation.Significant`). It gives significance, not a positive valence, and the `living` readings do not include further generation: the direction of 生生 is read separately, by widening what can form (D1)."),
        ("| Living and further generation within the whole have basic positive significance; at the level of claims, every living claim has significance from every standpoint | `G0`, `Valuation.Significant` |",
         "| At the level of claims, every living claim has significance from every standpoint; on a frame, realized living content falls under the relevance read from significance. It gives significance, not a positive valence, and does not reach further generation (row D, readings of `living`) | `G0`, `Valuation.Significant` |"),
        ("Positive relevance is read from significance: it is the significance of realized living content (`Frame.relevance`), and every use of living significance is discharged through it (section 6.12). |",
         "Relevance is read from significance: it is the significance of realized living content (`Frame.relevance`), and every use of living significance is discharged through it (section 6.12). The `positive` of `G0` is a parameter, not a valence: read from significance under the condition, it holds of exactly the realized living content (`relevance_least`). |"),
        ("| Self-significance | A standpoint's own living, further-generating content has positive significance for it |",
         "| Self-significance | A standpoint's own living claims have significance from it (significance, not a positive valence) |"),
        ("Living significance says that realized living content is positively relevant (`G0`, [Becoming.Metaethics](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean)).",
         "Living significance says that realized living content falls under a relevance (`G0`, [Becoming.Metaethics](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean)); read from significance, that relevance is the significance of realized living content, with no valence (`Frame.relevance`, `relevance_least`)."),
        ("| living significance | Realized living content is positively relevant; at the level of claims, every living claim has significance from every standpoint. Not an axiom:",
         "| living significance | At the level of claims, every living claim has significance from every standpoint; on a frame, realized living content falls under the relevance read from significance. It gives significance, not a positive valence, and the `living` readings do not include further generation. Not an axiom:"),
        ("| G0 | living significance: every living claim has significance from every standpoint (realized living content is positively relevant) |",
         "| G0 | living significance: every living claim has significance from every standpoint (on a frame, realized living content falls under the relevance read from significance) |"),
    ],
    'theories/becoming/OPENING.md': [
        ("the work derives living significance (that living and further generation within the whole have basic positive significance), together with",
         "the work derives living significance (that every living claim has significance from every standpoint; this is significance, not a positive valence, and it does not reach further generation, whose direction the theory reads separately), together with"),
    ],
    '_process/navigation/README-LEAD.md': [
        ("Living significance, that living and further generation within the whole have basic positive significance, is a theorem under one condition",
         "Living significance, that every living claim has significance from every standpoint, is a theorem under one condition"),
    ],
}

texts = {p: open(p, encoding='utf-8').read() for p in EDITS}
for path, pairs in EDITS.items():
    for old, new in pairs:
        n = texts[path].count(old)
        if n != 1:
            sys.exit(f'{path}: expected 1 occurrence, found {n}: {old[:80]}')
        texts[path] = texts[path].replace(old, new)
for path, text in texts.items():
    open(path, 'w', encoding='utf-8').write(text)
print('applied', sum(len(v) for v in EDITS.values()), 'edits')
