"""Classify the polymorphic ethics modules against the Becoming spine (plan P3).

Recomputes the census criterion of BECOMING-UNIFICATION-PLAN.md §1, requires the
table below to classify exactly the modules it selects, and checks each row's
claim mechanically: a bridged interface names declarations of a checked spine
module and is imported by the spine; a core module imports GenerativeCore; a
Mathlib leaf imports Mathlib; every other module stays on the Std toolchain.
Writes BECOMING-INSTANCE-CHECKS.json and BECOMING-INSTANCE-CLASSIFICATION.md.
No Lean is compiled here; the spine receipt supplies the kernel check.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean"
ETHICS = LEAN / "universal-ethics"
SPINE_DIR = LEAN / "becoming"
spec = importlib.util.spec_from_file_location("check_becoming", SPINE_DIR / "check_becoming.py")
becoming = importlib.util.module_from_spec(spec)
spec.loader.exec_module(becoming)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
rel = lambda p: p.relative_to(ROOT).as_posix()

CATEGORIES = {
    "bridge": ("接口实例或等价定理", "Interface instantiated or proved equal",
               "模块自建的接口或组合子，脊柱给出具名实例，或证明它就是脊柱上的同一概念。"),
    "core": ("已在核心上", "Already on the core",
             "定理陈述在核心 `Process`／`Trace` 上；框架的 `P` 直接代入，无需桥接。"),
    "history": ("对历史类型多态", "Polymorphic over histories",
                "定理对历史（完整相关延续）类型及外给关系多态；取历史为框架的配置即直接适用，前提仍由使用者提供。"
                "用到 `Robust`、`Better`、`Inventory` 处，经第一类的桥接定理与脊柱概念等同。"),
    "renewal": ("运行上的更新界（P3b）", "Renewal bounds on runs (P3b)",
                "定理对状态序列 `Nat → S` 多态，运行的 `state` 直接代入；其自然数秩的更新或完成界是 "
                "`falls_finitely` 的情形。`ContinuationRenewal` 的良基形式比自然数秩更一般，不由该原则导出。"),
    "mathlib": ("Mathlib 叶子（P5）", "Mathlib leaves (P5)",
                "依赖 Mathlib，与 Std 工具链分开；不进入脊柱回执。"),
    "model": ("具体模型", "Concrete models",
              "具体反例、可执行规划器或证据模型。多态引理服务于这些模型（列表、过滤、可执行计算），不是需要在脊柱上实例化的接口；"
              "两个探究模块是探究层的确定、可计算特例。"),
}

# module -> (category, spine declarations or "", note)
TABLE = {
    "WholeGroundCoverage": ("bridge", ["Becoming.reached_iff_closure"], "`Reached` 即沿边的可达闭包"),
    "CutCoverageAudit": ("bridge", ["Becoming.cutReach_iff_closure"], "`Reach` 与 WholeGroundCoverage 的 `Reached` 逐字同构"),
    "EvaluatorGrounding": ("bridge", ["Becoming.chain_iff_reach"], "`Chain` 即边过程上的可达；路线本身见 MetaethicalCore §9"),
    "JointContinuationClassification": ("bridge", ["Becoming.Frame.continuations", "Becoming.Frame.map_preserves_bundles",
                                                   "Becoming.Frame.lift_reflects_bundles"],
                                        "可达配置即延续空间；忠实变换来自核心 `trace_map`／`trace_lift`"),
    "PracticalJudgment": ("bridge", ["Becoming.commonResponse_is_robust", "Becoming.robust_iff_commonResponse",
                                     "Becoming.BetterAt"],
                          "`Robust` 即共同回应，反之每个稳健回应都是某过程的共同回应；`Better` 在配置上即 `BetterAt`"),
    "PracticalReach": ("bridge", ["Becoming.guarantees_iff_completes"], "`Guarantees` 即一步完成"),
    "StandardsBridge": ("bridge", ["Becoming.revise_is_after"], "按观察过滤规则表即纯观察上的 `After`"),
    "CorrectionInfrastructure": ("bridge", ["Becoming.liveStep_iff_enabled"], "`LiveStep` 即 `Enabled`"),
    "GenerativeComparison": ("bridge", ["Becoming.Frame.inventory", "Becoming.g0_iff", "Becoming.extension_iff",
                                        "Becoming.comparison_iff", "Becoming.comparison_lifts",
                                        "Becoming.articulation_iff_lifted", "Becoming.lifted_comparison_supplies_reason",
                                        "Becoming.lift_coherent_selection_survives",
                                        "Becoming.lift_continual_improvement_has_no_survivor"],
                             "G0、生成扩展与 C 在定义上即核心的；函数式情境恰为提升规则 L 下的确定情形；比较、理由、存活与持续改进推广到每个框架"),
    "PositiveGroundUncertainty": ("bridge", ["Becoming.universal_reason"], "可靠探究的范围给出 `SecuresPositiveGround` 的实例"),
    "PositionedPositiveReason": ("bridge", ["Becoming.securesPositiveGround_iff", "Becoming.positionedArticulation_iff",
                                             "Becoming.positioned_articulation_of_articulates", "Becoming.universal_reason"],
                                 "确保的正面根据与 D 在定义上即核心的；路线理由由表述前提 A 给出"),
    "LivingOrganization": ("core", [], "生命组织的轨迹与可行动作"),
    "LivingAllocation": ("core", [], ""),
    "LivingExpansion": ("core", [], ""),
    "LivingRealization": ("core", [], ""),
    "LivingRecovery": ("core", [], ""),
    "SituatedRenewal": ("core", [], "也用到 ContinuationRenewal，见 P3b"),
    "SituatedContinuation": ("core", [], "也用到 ContinuationRenewal，见 P3b"),
    "SustainedJudgment": ("core", [], "同时用到 `PracticalJudgment`，经其桥接"),
    "ContinuationRenewal": ("renewal", ["Becoming.falls_finitely", "Becoming.Run.renewal_recurs"],
                            "无更新尾部与任意晚的更新"),
    "OpenFutureRevision": ("renewal", ["Becoming.falls_finitely"], "交接的剩余步数证书；完成界来自 ContinuationRenewal"),
    "WholePracticalRestriction": ("history", [], "`Family Whole Index`：整体取配置，指标取立场"),
    "GenerativeLossComparison": ("history", [], "外给的 `Le` 可取 `BetterAt`"),
    "GenerativeTradeoff": ("history", [], "`Problem Circumstance Response History`"),
    "ClassificationRevision": ("history", [], "记录与目标在历史上"),
    "ClassificationRobustJudgment": ("history", [], "经 `PracticalJudgment`"),
    "ConcernExtension": ("history", [], "经 `PracticalJudgment`"),
    "EvaluativeExtension": ("history", [], "经 `PracticalJudgment`"),
    "RelationalOrganization": ("history", [], "经 `PracticalJudgment`"),
    "AlignmentDirection": ("history", [], "唯一的多态定理是忠实修订保持要求；其余为具体 AI 服务例"),
    "SelectorReviewCoverage": ("history", [], "`live`／`menu` 与 `Robust` 同形，世界取范围内的配置"),
    "RelationalGrounding": ("model", [], "关于边际描述的具体反例"),
    "UnequalBasicLosses": ("model", [], "两层损失诊断；多态引理是报告去重"),
    "AggregationContext": ("model", [], ""),
    "AlignmentInquiry": ("model", [], "可执行的一次探测规划器，是探究层的确定、可计算特例"),
    "FormativeAssessment": ("model", [], "确定性评估序列，是探究层的特例"),
    "EvidenceQualifiedCorrection": ("model", [], "候选模型池与保守证书"),
    "FallibleInspection": ("model", [], ""),
    "ReformEvidence": ("model", [], ""),
    "WisdomGoalGrounds": ("model", [], ""),
    "CorrectionBoundary": ("mathlib", [], ""),
    "CorrectionParent": ("mathlib", [], ""),
    "CorrectionRelations": ("mathlib", [], ""),
    "ObservationRepair": ("mathlib", [], ""),
    "ObservationChange": ("mathlib", [], ""),
}

THEOREM = re.compile(r"^(?:theorem|lemma)\s+\S+(.*?):=", re.M | re.S)
POLY = re.compile(r"[\{\(]\s*[A-Za-z]\w*(\s+[A-Za-z]\w*)*\s*:\s*Type")
TYPE_VARIABLE = re.compile(r"^variable\s*[\{\(][^\n]*:\s*Type", re.M)


def census():
    """The plan's §1 criterion: a theorem with an explicit type binder, or a type variable."""
    rows = {}
    for directory in (ETHICS, ETHICS / "generative-capacity", ETHICS / "evolution-connectionism"):
        for path in sorted(directory.glob("*.lean")):
            text = path.read_text()
            theorems = THEOREM.findall(text)
            polymorphic = sum(1 for signature in theorems if POLY.search(signature))
            if polymorphic or TYPE_VARIABLE.search(text):
                rows[path.stem] = {"path": rel(path), "lines": text.count("\n"),
                                   "theorems": len(theorems), "polymorphic_theorems": polymorphic}
    return rows


def import_closure(index, name):
    seen, external, stack = set(), set(), [name]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        paths = index.get(current, [])
        if len(paths) != 1:
            external.add(current)
            continue
        stack.extend(becoming.imports_of(paths[0].read_bytes()))
    return seen - external, external


def declared(name, sources):
    *prefix, last = name.removeprefix("Becoming.").split(".")
    pattern = (r"^\s*(?:theorem|lemma|def|abbrev|structure)\s+" + re.escape(".".join(prefix + [last]))
               + r"(?=\s|\{|\(|:)")
    return [module for module, text in sources.items() if re.search(pattern, text, re.M)]


def main():
    errors = []
    rows = census()
    missing, extra = sorted(set(rows) - set(TABLE)), sorted(set(TABLE) - set(rows))
    if missing or extra:
        errors.append({"census_mismatch": {"unclassified": missing, "not_in_census": extra}})

    receipt_path = SPINE_DIR / "becoming-verification.json"
    receipt = json.loads(receipt_path.read_text())
    spine_sources = {name: (SPINE_DIR / f"{name}.lean").read_text() for name in receipt["spine_modules"]}
    if receipt["status"] != "passed":
        errors.append({"spine_receipt": "not passed"})
    for name, text in spine_sources.items():
        if hashlib.sha256(text.encode()).hexdigest() != receipt["source_sha256"][name]:
            errors.append({"spine_receipt_stale": name})

    index = becoming.module_index()
    spine_closure = set()
    for name in receipt["spine_modules"]:
        spine_closure |= import_closure(index, name)[0]

    for module, (category, connections, note) in TABLE.items():
        if module not in rows:
            continue
        local, external = import_closure(index, module)
        mathlib = sorted(e for e in external if e.startswith("Mathlib"))
        row = rows[module]
        row.update(category=category, connections=[], note=note,
                   imports_core="GenerativeCore" in local, imports_mathlib=bool(mathlib))
        for name in connections:
            found = declared(name, spine_sources)
            row["connections"].append({"declaration": name, "spine_modules": found})
            if not found:
                errors.append({"undeclared_connection": [module, name]})
        if category == "bridge" and module not in spine_closure:
            errors.append({"bridge_not_imported_by_spine": module})
        if category == "core" and not row["imports_core"]:
            errors.append({"core_without_GenerativeCore": module})
        if (category == "mathlib") != row["imports_mathlib"]:
            errors.append({"toolchain_mismatch": [module, category, mathlib]})
        if category == "history" and not row["polymorphic_theorems"]:
            errors.append({"history_without_polymorphic_theorem": module})

    totals = {category: {"modules": sum(1 for r in rows.values() if r.get("category") == category),
                         "lines": sum(r["lines"] for r in rows.values() if r.get("category") == category),
                         "theorems": sum(r["theorems"] for r in rows.values() if r.get("category") == category)}
              for category in CATEGORIES}
    result = {
        "status": "passed" if not errors else "failed",
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "criterion": "A module in universal-ethics, generative-capacity or evolution-connectionism with a theorem "
                     "whose signature has an explicit type binder, or with a type variable (plan §1).",
        "census": {"modules": len(rows), "lines": sum(r["lines"] for r in rows.values()),
                   "theorems": sum(r["theorems"] for r in rows.values())},
        "totals": totals,
        "spine_receipt": {"path": rel(receipt_path), "sha256": sha(receipt_path), "utc": receipt["utc"]},
        "checker_sha256": sha(Path(__file__)),
        "scope": "Classification and mechanical checks of its rows only. Kernel checking of every named "
                 "declaration is supplied by the spine receipt; the inherited modules are not recompiled.",
        "modules": rows,
        "errors": errors,
    }
    (HERE / "BECOMING-INSTANCE-CHECKS.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    (HERE / "BECOMING-INSTANCE-CLASSIFICATION.md").write_text(page(result))
    print(json.dumps({"status": result["status"], "census": result["census"],
                      "totals": {k: v["modules"] for k, v in totals.items()}, "errors": errors}, ensure_ascii=False))
    return 0 if not errors else 1


def page(result):
    spine = "../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming"
    lines = [
        "# 既有伦理模块在 Becoming 脊柱上的位置 / Ethics modules on the Becoming spine",
        "",
        "由 [BECOMING-INSTANCE-CHECK.py](BECOMING-INSTANCE-CHECK.py) 生成，勿手改；检查结果见 "
        "[BECOMING-INSTANCE-CHECKS.json](BECOMING-INSTANCE-CHECKS.json)。这是"
        "[统一计划](BECOMING-UNIFICATION-PLAN.md) P3 的分类表。",
        "",
        f"按计划第 1 节的判据，伦理族中含类型多态定理的模块共 {result['census']['modules']} 个"
        f"（{result['census']['lines']:,} 行、{result['census']['theorems']} 条定理）。"
        "通用模块对小接口多态，因此不复制、不改写：脊柱给出接口的实例，或证明模块自建的组合子就是脊柱上的同一概念，"
        f"它们的定理便直接作用于同一展开。具名声明在 [BecomingInstances.lean]({spine}/BecomingInstances.lean)、"
        f"[BecomingRenewal.lean]({spine}/BecomingRenewal.lean) 或 [MetaethicalCore.lean]({spine}/MetaethicalCore.lean) 中，"
        "由脊柱回执逐条检查，公理报告为空。",
        "",
        "Generated; do not edit. The polymorphic ethics modules are not copied: the spine instantiates their "
        "interfaces or proves their combinators equal to its own, so their theorems apply to one unfolding. "
        "Each named declaration is kernel-checked with an empty axiom report by the spine receipt.",
        "",
        "**方向约定。** `GenerativeComparison` 中 `Better first second` 表示后者更好；`PracticalJudgment` 与 "
        "`LiftBetter` 中 `better x y` 表示前者更好。桥接定理保留各自的约定。",
        "",
        "**提升规则 L 是实质承诺。** 一个回应若有一好一坏两个结果，保守规则在两个方向上都不作比较"
        "（`LiftModel.some_outcome_does_not_lift`）；经无结果的中间回应，传递性失败（`LiftModel.lift_needs_live_middle`）。",
        "",
        "| 类别 / Category | 模块 | 行 | 定理 |",
        "|---|---:|---:|---:|",
    ]
    for key, (zh, en, _) in CATEGORIES.items():
        t = result["totals"][key]
        lines.append(f"| {zh} / {en} | {t['modules']} | {t['lines']:,} | {t['theorems']} |")
    for key, (zh, en, explanation) in CATEGORIES.items():
        lines += ["", f"## {zh} / {en}", "", explanation, "", "| 模块 | 定理（多态） | 脊柱声明 | 说明 |", "|---|---:|---|---|"]
        for module, row in result["modules"].items():
            if row.get("category") != key:
                continue
            declarations = "，".join(f"`{c['declaration'].removeprefix('Becoming.')}`" for c in row["connections"])
            lines.append(f"| [{module}](../../../../{row['path']}) | {row['theorems']}（{row['polymorphic_theorems']}） "
                         f"| {declarations or '—'} | {row['note'] or '—'} |")
    lines += ["", "## 范围 / Scope", "",
              "分类与逐行机械检查。被继承模块不在此重新编译；具名声明的内核检查由脊柱回执提供。"
              "第三类定理的前提（历史类型的含义、外给关系的规范根据）仍由使用者提供，取配置为历史并不证明这些前提。"
              "第五、六类未桥接是有意的：Mathlib 叶子留待 P5；具体模型没有需要实例化的接口。", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
