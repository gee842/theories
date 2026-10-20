"""R36: what the 20 October Chinese edition stated and the English did not.

The ZH audit (mirror mode) found 18 Lean names of the frozen Chinese edition in neither the new Chinese edition
nor the records it links. Two are fragments of longer names (`_listing`, `_by_core`), and `Frame.realized` and
`families_reach_each_other` are in the English chapter; the other fourteen come from seven rows of the old
Chinese module table in section 9, a table the English had moved to its reference edition on 17 October. Their
statements are carried into the English section 9 here, translated, before the list of modules, so nothing the
Chinese edition alone stated is lost from the live chapter. Without --apply, prints the paragraph.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
LIVE = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
B = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/'
BEGIN, END = '<!-- zh-table:begin -->', '<!-- zh-table:end -->'

TEXT = f"""{BEGIN}
**Module statements from the Chinese edition's table.** The 20 October Chinese edition kept a table of the core's modules in this section; seven of its rows state laws the English named nowhere, carried here in translation (the frozen table is in [the Chinese edition of 20 October](../history/THE-THEORY-OF-BECOMING-2026-10-20.zh.md#9-形式脊柱--the-formal-spine)).
- [Becoming.Prelude]({B}becoming/Becoming/Prelude.lean) (L0, no premise, imports only `Init`): the lemmas on numbers, truth values, lists and options the layers use, each stated once: cancellation, subtraction and products of natural numbers (`add_right_cancel`, `Naturals.sub_sub`, `mul_assoc_nat`), what `all`, `any`, `contains`, `filter`, `find?`, `bind` and `map` test (`ListTests.all_true_iff`, `ListTests.find_none_iff`), membership in appended and mapped lists (`mem_append_cases`, `preimage_of_mem_map`), proved by recursion where Lean's own versions use `propext`.
- [Becoming.ClassifiedBeliefProcesses]({B}becoming/Becoming/ClassifiedBeliefProcesses.lean) (no premise): a narrowed belief whose inhabitation is decided is empty or inhabited (`after_empty_or_inhabited`); where every narrowed belief's inhabitation is decided, every belief is classified at every depth, and bounded sufficiency is the implication form (`classified_of_decidable`, `sufficiency_iff_implication_of_decidable`).
- [Becoming.MoveOutcomeProcesses]({B}becoming/Becoming/MoveOutcomeProcesses.lean) (no premise): one process covers another at a configuration exactly where every target the first completes in one step the second also completes in one step (`covers_iff`); covering is a preorder kept along revision (`covers_along`); covering fails exactly where some target is not carried (`not_covers_iff`), and with double-negation elimination as a hypothesis the lost target can be named. Four processes on two configurations witness that more possible outcomes need not cover, that covering can remove a possibility, and that a summary can hide a loss.
- [Becoming.RenewalFlow]({B}becoming/Becoming/RenewalFlow.lean) (no premise): on webs, neither a formation's trace nor the focal formation's own trace decides the class of a run: formations each within renewal consume jointly, upgrading consumes, and the seasonal web neither renews nor consumes (`SupportGatedWebs.formation_does_not_decide` and five more).
- [Becoming.EdgeClosure]({B}becoming/Becoming/EdgeClosure.lean) (no premise): what a single-label process stepping along edges reaches from a seed contains the seed, is closed under the edges and lies within every property kept along them (`Closure.base`, `Closure.step`, `Closure.induction`); the core's closure of a relation is this closure from a seed (`withinClosure_iff_closure`).
- [Becoming.SeedReach]({B}becoming/Becoming/SeedReach.lean) (no premise): reach from a seed is the least invariant holding at the seed; a configuration is separated from the seed by some invariant exactly where it is not reached; "every process reaches every configuration not so separated" is exactly double-negation elimination (`fromSeed_of_not_separated_iff_dne`), so asserting reach needs a path or a decision of reach.
- [LivingOrganizationCorrespondence]({B}universal-ethics/LivingOrganizationCorrespondence.lean) (periphery instance, Lean 4.30.0-rc2, its own checker, standard axioms only): with the recipe entering the pool as the gate (`entryGate`) and the other steps reflecting the pool's presence (`presence_reflected`), `trace_pool_origin` is given by the core's `Gated.origin` without deciding the pool (`trace_pool_origin_by_core`), the pool is present after the entry step (`entry_then_present`), and an empty pool stays empty where every admitted recipe closes (`empty_pool_preserved_by_core`).
{END}
"""


def main():
    text = LIVE.read_text()
    if BEGIN in text:
        new = text[:text.index(BEGIN)] + TEXT.rstrip('\n') + text[text.index(END) + len(END):]
    else:
        anchor = '\n<!-- modules:begin -->'
        assert text.count(anchor) == 1
        new = text.replace(anchor, '\n' + TEXT + anchor)
    if '--apply' in sys.argv:
        LIVE.write_text(new)
        print('applied')
    else:
        print(TEXT)


if __name__ == '__main__':
    main()
