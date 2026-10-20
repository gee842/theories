#!/usr/bin/env python3
"""A2: apply the generativity-chain change Ren took on 18 October 2026 (D43, review item 51).

`Selection` enters the wisdom entry M15; `Observation` and `Parting` enter the learning entry
M26. Each sentence states its theorem in the naming study's coupling vocabulary (section 7:
couples into, the map, prefix, extrapolation, alternatives) and its record's exact scope. The
script only appends: no existing text, link or fingerprint of the chain is changed, and it
refuses to run twice. Fingerprints of the new link targets are recorded separately, after reading
them, by record_reading.py.

Usage: python3 -B apply_chain_links.py  (from the repository root)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
DATA = ROOT / "theories/becoming/results/data/generativity-chain.json"
LEAN = "experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/"
RECORDS = "theories/becoming/results/records/"
D43 = ("_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md"
       "#d43-其余的待决读法--the-other-pending-readings")
SOURCE = "sources/15-codex-theory-conversations/2026-10-16-selection-through-a-model.md"

M15 = {
    "claim_zh": (
        "选择经选择者的模型，不经记录（Ren 2026-10-16：“it is about the cognitive model, not just record”）："
        "模型是备择的映射，两个备择被每个经它的选择选得相同，恰当它使二者并列（`Relabel.selected_alike_iff`）；"
        "模型是一个归并，经它的选择对要紧者正确，只在要紧者跨这一归并同去之处；模型归并了要紧者所分开的两个备择时，"
        "经它的选择都不正确，要分开它们需要更细的模型（`Learning.selects_right_through`、`Learning.selects_not_right_of_parted`）。"
        "记得更多并不提供哪个模型正确。"),
    "claim_en": (
        "Selection works through the selector's model, not the record (Ren, 16 October 2026: “it is about the cognitive "
        "model, not just record”): with the model a map of the alternatives, two alternatives are selected alike by every "
        "selection through it exactly when it ties them (`Relabel.selected_alike_iff`). The model is a lumping, and a "
        "selection through it is right about what matters only where what matters goes alike across the lumping; where "
        "the model lumps two alternatives that what matters separates, no selection through it is right, and separating "
        "them takes a finer model (`Learning.selects_right_through`, `Learning.selects_not_right_of_parted`). Remembering "
        "more does not supply which model is right."),
    "scope_zh": (
        "选择（`Becoming.Selection` 与 `Becoming.Learning`，沿运行为 `Becoming.SelectionRuns`；记录 "
        "selection-through-a-model-of-the-options）：无公理；备择的相等已定，选择经模型是假设，要紧者是给定的；"
        "哪个模型正确、何者要紧都不推出，更细的模型从哪里来属于学习。“记得更多并不提供哪个模型正确”是 AI 对 Ren "
        "这一更正的读法，写在 Ren 2026-10-16 认可的重构中（“go ahead with the reframing”）；这一环节由 Ren 2026-10-18 取（D43）。"),
    "scope_en": (
        "Selection (`Becoming.Selection` and `Becoming.Learning`, along runs `Becoming.SelectionRuns`; record "
        "selection-through-a-model-of-the-options): no axiom; the alternatives' equality is decided, that a selection "
        "goes through the model is a hypothesis, and what matters is given. Which model is right, and what matters, are "
        "not shown; where a finer model comes from belongs to learning. That remembering more does not supply the right "
        "model is the AI's reading of Ren's correction, stated in the reframing Ren approved on 16 October 2026 (“go ahead "
        "with the reframing”); Ren took this link on 18 October 2026 (D43)."),
    "connection_zh": (
        "经选择者模型的选择→智慧候选中记录与规律之别：选择在何处正确，由模型对要紧者的拟合决定，不由更多记录决定；"
        "观察与分开给出的学习之限见学习一项（M26）。"),
    "connection_en": (
        "Selection through the selector's model feeds the wisdom candidate's distinction of record and law: where a "
        "selection is right is decided by its model's fit to what matters, not by more record; the limits that "
        "observation and parting set on learning are in the learning entry (M26)."),
    "links": [
        {"label_zh": "经选择者模型的选择：结果与范围", "label_en": "Selection through the selector's model: result and scope",
         "path": RECORDS + "selection-through-a-model-of-the-options.md"},
        {"label_zh": "经模型的选择（Relabel）", "label_en": "Selection through the model (Relabel)",
         "path": LEAN + "Selection.lean"},
        {"label_zh": "模型即归并：对要紧者是否正确", "label_en": "The model as a lumping: right about what matters",
         "path": LEAN + "Learning.lean"},
        {"label_zh": "Ren：认知模型，不只是记录", "label_en": "Ren: the cognitive model, not just record",
         "path": SOURCE},
        {"label_zh": "Ren 所取的这一环节（D43）", "label_en": "The link Ren took (D43)", "path": D43},
    ],
}

M26 = {
    "claim_zh": (
        "观察在下游之内：对每个读入每个条件一个所列水平之时程的律，同样形成在场、部分动作相同、其余遵从律而"
        "起始只在一个储量上不同的两个平衡进程，在每一步、在按到那一步形成的所读路线不在储量下游的每个条件上都相同"
        "（`apart_only_downstream`）；所以一个形成的交换只经它所读、位于储量下游的水平回应储量之差"
        "（`exchange_alike_off_downstream`），直接观察是长度为零的路线。"
        "运行分开之处，前段与律都不固定其去向：两个运行在一步分开，指它们经映射的历程在此步之前相同、在此步不同；"
        "此前的前段是同一个，所以没有外推，无论被给予什么（律在内），在两个运行上都对（`Parting.not_right_on_both`）；"
        "移动与配置列出、步已定时，依过程所建之外推在一步于每个运行上都对，恰当那一步没有两个运行分开"
        "（`Parting.world_right_iff`）。从一个配置出发没有两个运行分开、值已定、运行被 N 个配置的列表所持时，按最小界的外推"
        "不被给予什么，从 2N − 1 起都对（`Parting.leastBound_right`），同于确定的律，后者处处不分开（`Parting.unparted_of_determined`）。"),
    "claim_en": (
        "Observing lies within the downstream: under every law reading into each condition a schedule of "
        "listed levels, two balanced courses with the same formations present, the part acting alike and the rest "
        "following the law, apart at the start only in a stock, stand alike at each step at every condition not "
        "downstream of the stock by the readings formed by then (`apart_only_downstream`). So a formation's exchange "
        "responds to the stock's difference only through a level it reads that lies downstream "
        "of the stock (`exchange_alike_off_downstream`), direct observation being the route of length zero. Where "
        "runs part, neither the prefix nor the law fixes the way: "
        "two runs part at a step where their courses through the map are alike before it and differ at it; the "
        "prefixes before it are one, so no extrapolation, whatever it is given, the law included, is right on both "
        "(`Parting.not_right_on_both`). With moves and configurations listed and steps decided, the extrapolation "
        "built from the process is right at a step on every run exactly where no two runs part there "
        "(`Parting.world_right_iff`). Where no two runs from a configuration part, with the values decided and the run "
        "held by a list of N configurations, the extrapolation by the least bound, given nothing, is right from 2N − 1 "
        "on (`Parting.leastBound_right`), as for determined laws, which part nowhere (`Parting.unparted_of_determined`)."),
    "scope_zh": (
        "观察（`Becoming.Observation`，记录 observation-is-a-route）：无公理，不判定条件，也不需条件有限；律所读的"
        "时程是给定的；在下游者是否不同、带误差的量度、律读哪个时程都不推出。读法减弱为 `apart_only_downstream` "
        "所表明的，由 Ren 2026-10-18 取（D43）；“观察不是依赖之外的第二种关系”是猜想，不在这一环节之内。"
        "分开（`Becoming.Parting`，记录 identification-where-runs-part）：无公理；逆命题需要列出的移动与配置、"
        "已定的步与已定的值；运行分开之处，配置之界不界定任何历程（`Parting.free_unbounded`）；无穷或不可判定的"
        "过程中依过程所建之外推不推出。两个环节由 Ren 2026-10-18 取（D43）。"),
    "scope_en": (
        "Observation (`Becoming.Observation`, record observation-is-a-route): no axiom, no decision on conditions and "
        "no finiteness of conditions; the schedule a law reads is given; that what lies downstream differs, measurement "
        "with error and which schedule a law reads are not shown. The reading is weakened to what "
        "`apart_only_downstream` shows, as Ren took it on 18 October 2026 (D43); that observation is no second relation "
        "beside dependence is a conjecture and is not part of this link. Parting (`Becoming.Parting`, record "
        "identification-where-runs-part): no axiom; the converse needs listed moves and configurations, decided steps "
        "and decided values; where runs part, a bound on configurations bounds no course (`Parting.free_unbounded`), "
        "and the extrapolation built from the process is not shown for infinite or undecided processes. Ren took both "
        "links on 18 October 2026 (D43)."),
    "links": [
        {"label_zh": "观察在下游之内：结果与范围", "label_en": "Observing lies within the downstream: result and scope",
         "path": RECORDS + "observation-is-a-route.md"},
        {"label_zh": "观察源码", "label_en": "Observation source", "path": LEAN + "Observation.lean"},
        {"label_zh": "运行分开之处的辨识：结果与范围", "label_en": "Identification where runs part: result and scope",
         "path": RECORDS + "identification-where-runs-part.md"},
        {"label_zh": "分开源码", "label_en": "Parting source", "path": LEAN + "Parting.lean"},
        {"label_zh": "Ren 所取的读法与环节（D43）", "label_en": "The readings and links Ren took (D43)", "path": D43},
    ],
}


def append(entry, change):
    for field in ("claim_zh", "claim_en", "scope_zh", "scope_en", "connection_zh", "connection_en"):
        if field in change:
            if change[field] in entry.get(field, ""):
                raise SystemExit(f"{entry['id']}.{field} already holds the A2 text")
            entry[field] = (entry[field].rstrip() + " " + change[field]) if entry.get(field) else change[field]
    known = {link["path"] for link in entry["links"]}
    for link in change["links"]:
        if link["path"] in known:
            raise SystemExit(f"{entry['id']} already links {link['path']}")
        entry["links"].append(link)


def main():
    data = json.loads(DATA.read_text())
    entries = {e["id"]: e for s in data["sections"] for e in s["entries"]}
    append(entries["M15"], M15)
    append(entries["M26"], M26)
    data["updated"] = "2026-10-18"
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("M15 +", len(M15["links"]), "links; M26 +", len(M26["links"]), "links; updated 2026-10-18")


if __name__ == "__main__":
    main()
