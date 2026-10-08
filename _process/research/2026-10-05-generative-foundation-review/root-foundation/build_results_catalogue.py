#!/usr/bin/env python3
"""Render the bilingual reading index and check documentary coverage, not proofs.

From the repository root:
  python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_results_catalogue.py
  python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_results_catalogue.py --check

Argument prose is edited in the three JSON reading registers. This script owns
results/README.md, THEORY-MAP.md and both ARGUMENTS chapter volumes.
Source hashes identify inspected versions; refresh only after reviewing changes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'theories/shengsheng-buxi-generative-existence/results'
CANON = OUT.parent / 'unified-2026-10-05'
FIELDS = ('id', 'source', 'title_zh', 'title_en', 'category', 'status',
          'argument_zh', 'argument_en', 'significance_zh', 'significance_en',
          'scope_zh', 'scope_en', 'next_zh', 'next_en', 'source_sha256')
CATEGORIES = dict(zip(
    ('alignment application classical classical-comparison classical-ethical comparison empirical empirical-identification ethical-argument ethical-mechanism ethics ethics-development ethics-interface evidence formal-compendium formal-index formal-interface formal-specification foundation governance identification-mathematics learning mathematical-boundary mathematical-model mathematics mechanism mechanism-mathematics mechanism-strategy methodology navigation normative-foundation philosophical-epistemic programme research-programme review roadmap selection synthesis').split(),
    ('对齐 应用 经典思想 经典比较 经典伦理 比较 经验研究 经验识别 伦理论证 伦理机制 伦理 伦理发展 伦理接口 证据 形式汇编 形式索引 形式接口 形式规格 基础 治理 识别数学 学习 数学边界 数学模型 数学 机制 机制数学 机制与策略 方法 导航 规范基础 认识论 研究纲领 研究纲领 审查 路线 选择 综合').split()))


def category(d: dict) -> str:
    code = d['category']
    return f'{CATEGORIES[code]} / {code.replace("-", " ")}' if code in CATEGORIES else code


def rel(path: str) -> str:
    return os.path.relpath(ROOT / path, OUT)


def chapter_link(identifier: str) -> str:
    volume = 'A-L' if identifier[0].upper() <= 'L' else 'M-Z'
    return f'ARGUMENTS-{volume}.md#{identifier}'


def link(label: str, target: str) -> str:
    return f'[{label}](<{target}>)' if ' ' in target else f'[{label}]({target})'


@lru_cache(maxsize=None)
def anchors(path: Path) -> set[str]:
    """Explicit IDs and GitHub-style headings in a Markdown reading document."""
    body = path.read_text()
    found = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)[\"\']', body))
    counts: dict[str, int] = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*\s*$', body, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = re.sub(r'<[^>]*>', '', heading).replace('`','').lower()
        slug = ''.join(c for c in heading if c in '-_' or not unicodedata.category(c).startswith(('P','S'))).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        found.add(slug if not n else f'{slug}-{n}')
    return found


@lru_cache(maxsize=None)
def line_count(path: Path) -> int:
    return len(path.read_text().splitlines())


def branch_volume(branches: list[dict]) -> str:
    lines = ['# 理论分支：中英论证与意义 / Theory branches: arguments and significance', '',
             '2026-10-08 · [返回成果目录](README.md) · [研究路线](ROADMAP.md) · [Lean 索引](LEAN-INDEX.md)', '',
             '覆盖 `theories/*/README.md` 的全部分支，包括一个方法与记忆档案。以下为有出处的中英阅读重构，不是 Ren 原话或新证明。旧分支的版本与证据范围保留；统一理论的最新结果在对应章节中另列。', '',
             'Covers every branch README, including the method and memory archive. These are attributed bilingual reading reconstructions, not quotations from Ren or new proofs. Historical versions retain their scope; current unified results are separately linked.', '',
             '| 理论 / Theory | 当前状态 / Status |', '|---|---|']
    for d in branches:
        lines.append(f"| [{d['title_zh']} / {d['title_en']}](#{d['id']}) | {d['status']} |")
    for d in branches:
        lines.extend(['', f'<a id="{d["id"]}"></a>', f"## {d['title_zh']} / {d['title_en']}", '',
                      f"**编号 / ID:** `{d['id']}` · **类别 / Category:** {d['category']}", '',
                      f"**状态 / Status:** {d['status']}", '',
                      f"**论证：** {d['argument_zh']}", '', f"**Argument:** {d['argument_en']}", '',
                      f"**意义：** {d['significance_zh']}", '', f"**Significance:** {d['significance_en']}", '',
                      f"**后续：** {d['next_zh']}", '', f"**Next:** {d['next_en']}", '',
                      f"**完整论述 / Full account:** {link(d['source'], rel(d['source']))}", '',
                      '**Lean / 形式对应：** 本分支整体没有登记为一个 Lean 定理；可核查的细项见相关章节及 [Lean 索引](LEAN-INDEX.md)。相关章节表示研究联系，不自动证明旧分支的全部主张。 / The branch as a whole is not registered as one Lean theorem. Related chapters identify inspectable components and research connections, not a proof of every historical claim.'])
        if d.get('related_chapters'):
            lines.extend(['', '**相关章节 / Related chapters:** ' + ' · '.join(link(x, chapter_link(x)) for x in d['related_chapters'])])
    return '\n'.join(lines) + '\n'


def chapter_volume(rows: list[dict], volume: str) -> str:
    lines = [f'# 论证目录 {volume} / Argument catalogue {volume}', '',
             f'2026-10-08 · {len(rows)} 个章节 / chapters · [返回成果目录](README.md) · [研究路线](ROADMAP.md) · [Lean 索引](LEAN-INDEX.md)', '',
             '每项是有出处的中英论证阅读版，按原文件名编号；并非 Ren 原话或全部历史原文的逐句翻译。方法、综述、计划与论证分别标记。一个章节不是一个独立定理，审计声明数也不是理论数量。', '',
             'Each entry is an attributed bilingual reading reconstruction, identified by its source filename. These are not quotations from Ren or full translations of every historical text. Methods, syntheses, plans and arguments are distinguished; chapter and audit counts are not theory counts.', '',
             '完成状态限于各条所声明范围。有条件的统一基础已经获评完成；普遍伦理有效、实际遵循、唯一必要性及更强无假设目标分别保留。角色和边界在同一生成展开中解释。此处整理既有结果，不新增证明或编译检查。', '',
             'Completion is scoped. The conditional foundation is accepted; universal validity, compliance, exclusive necessity and assumption-free grounding remain separate questions. Roles and boundaries differentiate within one unfolding. This catalogue adds no proof or compiler run.', '',
             '## 可查看列表 / Contents', '', '| ID | 中文 / English | 类型 / Category | 状态 / Status |', '|---|---|---|---|']
    for d in rows:
        lines.append(f"| [{d['id']}](#{d['id']}) | {d['title_zh']} / {d['title_en']} | {category(d)} | {d['status']} |")
    for d in rows:
        lines.extend(['', f'<a id="{d["id"]}"></a>', f"## {d['title_zh']} / {d['title_en']}", '',
                      f"**编号 / ID:** `{d['id']}` · **类别 / Category:** {category(d)}", '',
                      f"**来源 / Source:** {link(Path(d['source']).name, rel(d['source']))}", '',
                      f"**状态 / Status:** {d['status']}", '',
                      f"**中文论证：** {d['argument_zh']}", '', f"**English argument:** {d['argument_en']}", '',
                      f"**意义：** {d['significance_zh']}", '', f"**Significance:** {d['significance_en']}", '',
                      f"**范围：** {d['scope_zh']}", '', f"**Scope:** {d['scope_en']}", '',
                      f"**后续：** {d['next_zh']}", '', f"**Next:** {d['next_en']}", ''])
        if d.get('lean'):
            lines.extend(['**Lean 对应 / Lean correspondence:** ' + ' · '.join(link(Path(x).name,rel(x)) for x in d['lean']), '',
                          '形式对应只覆盖上面说明的前提与子结论；模块存在不等于当前版本已重新编译。 / Correspondence covers only the stated premises and subclaims; source existence does not establish a fresh check of the current version.'])
        else:
            lines.append('**Lean 对应 / Lean correspondence:** 未登记本条的直接 Lean 证明；按上方说明保留哲学、方法、经验或历史验证范围。 / No direct Lean proof is registered for this entry; retain the philosophical, methodological, empirical or historical validation scope stated above.')
        if d.get('evidence'):
            lines.extend(['', '**既有检查、审读与来源 / Existing checks, reviews and sources:** ' + ' · '.join(link(Path(x.split('#')[0]).name,rel(x)) for x in d['evidence'])])
    return '\n'.join(lines)+'\n'


def index(chapters: list[dict], branches: list[dict]) -> str:
    lines = ['# 理论成果与论证目录 / Results and argument catalogue', '',
             '更新 / Updated: 2026-10-08 · [仓库首页](../../../README.md) · [研究进度与下一步](ROADMAP.md) · [完整研究记录](../../../RESEARCH.md)', '',
             '**从这里查：一个论证说了什么、为什么重要、中文与英文怎样对应、Lean 检查了哪一部分、还有什么需要研究。**', '',
             '**Use this directory to find the argument, its significance, its Chinese and English formulations, its Lean correspondence and its remaining questions.**', '',
             '## 阅读入口 / Reading routes', '',
             '| 文档 / Document | 内容 / Contents |', '|---|---|',
             '| [会话成果与证明复用 / Session outcomes and proof reuse](SESSION-RESULTS.md) | 会话到成果族、规范复用入口、重复证明判别及新增章节。 / Chats mapped to result families, canonical reuse targets, overlap decisions and additional chapters. |',
             f'| [全部理论分支 / Theory map](THEORY-MAP.md) | {len(branches)} 个分支的中英论证、意义、状态和后续；含方法档案。 / Bilingual branch accounts, including the method archive. |',
             '| [统一论证 A–L](ARGUMENTS-A-L.md) · [统一论证 M–Z](ARGUMENTS-M-Z.md) | 逐章中英阅读版：论证、意义、范围、下一问题、原文、Lean 与证据。 / Paired chapter readings with scope, questions, sources and evidence. |',
             '| [Lean 模块](LEAN-INDEX.md) · [定理名称](LEAN-DECLARATIONS.md) | 按模块及声明名称定位源码；区分检查记录与当前源码。 / Find modules and named declarations; distinguish recorded checks from current sources. |',
             '| [研究路线 / Roadmap](ROADMAP.md) | 已有结果、持续方向与建议的下一检验。 / Established results, ongoing directions and proposed tests. |',
             '| [细项主张账本 / Claim register](../unified-2026-10-05/CLAIMS.md) | 原有细项主张、证据类别、反例与研究沿革。 / Existing detailed claims, evidence classes and counterexamples. |', '',
             '## 按问题阅读 / Read by question', '',
             '| 问题 / Question | 推荐起点 / Entry points |', '|---|---|',
             '| 已经建立了怎样的共同基础？ / What foundation has been established? | [生成根据](ARGUMENTS-A-L.md#generative-grounding) · [前提与范围](ARGUMENTS-A-L.md#foundation-premises) · [全篇理论](ARGUMENTS-M-Z.md#theory) |',
             '| 组织怎样形成学习和修正能力？ / How do organization, learning and revision form? | [生成发展](ARGUMENTS-A-L.md#generative-development) · [学习路线修正](ARGUMENTS-A-L.md#learning-route-revision) · [评价接续](ARGUMENTS-A-L.md#evaluative-succession) |',
             '| 生生为何有伦理意义？ / Why does generativity matter ethically? | [统一伦理](ARGUMENTS-M-Z.md#unified-ethical-grounding) · [评价根据](ARGUMENTS-A-L.md#evaluative-grounding) · [良知](ARGUMENTS-A-L.md#liangzhi-evolution) |',
             '| 数学与一般规律推进到哪里？ / How far do mathematical and general results reach? | [Lean 核心](ARGUMENTS-A-L.md#generative-core-lean) · [数学根前沿](ARGUMENTS-M-Z.md#mathematical-root-frontier) · [条件普遍性](ARGUMENTS-A-L.md#conditional-universality) |',
             '| 怎样检验或改变理论？ / How can the theory be tested or revised? | [经验范围](ARGUMENTS-A-L.md#empirical-scope) · [实验接入](ARGUMENTS-A-L.md#experimental-access) · [非二元方法](ARGUMENTS-M-Z.md#nondual-method) |',
             '| 与既有思想、技术和共同生活有什么关系？ / How does it connect to earlier theories and practice? | [理论分支图](THEORY-MAP.md) · [道与生成](ARGUMENTS-A-L.md#dao-and-generativity) · [王阳明](ARGUMENTS-M-Z.md#wang-yangming) |', '',
             '## 覆盖与证据含义 / Coverage and evidence', '',
             f'本阅读版保留 **{len(chapters)} 个顶层 Markdown 章节**及 **{len(branches)} 个理论分支 README** 的已记录核读版本。新增章节、来源变化及会话成果见[当前检查点地图](SESSION-RESULTS.md)；旧摘要与哈希没有因导航更新而自动升级。章节是阅读和维护单元，不是独立理论或定理数。每项提供中英论证与意义，完整原文、历史批评及证明继续保留。', '',
             f'This reading edition retains the recorded source versions of **{len(chapters)} unified chapters** and **{len(branches)} branch READMEs**. Additional chapters, changed source versions and session outcomes appear in the [checkpoint map](SESSION-RESULTS.md). Navigation updates do not certify old summaries or refresh their review hashes. Chapters are reading units, not independent theories or theorems; full arguments, criticism and proofs remain at their original locations.', '',
             '| 标签 / Category | 含义 / Meaning |', '|---|---|',
             '| 有条件的检查结果 / Checked conditional result | Lean 检查指定定义与前提下的形式推论；模型与实际对象的对应、伦理前提的根据另列。 / Formal inference under specified definitions and hypotheses; correspondence and normative warrant remain separate. |',
             '| 哲学或文本论证 / Philosophical or textual argument | 有正面论证、异议与来源；没有直接 Lean 时明确保留。 / Argument, criticism and sources; missing direct formalization stays visible. |',
             '| 历史数学结果 / Historical mathematics | 保持原有手证、计算或历史检查的验证范围；不由后来的关联模块追认。 / Retains its original hand-proof, computation or historical-check scope. |',
             '| 经验或合成证据 / Empirical or synthetic evidence | 真实研究、对应解释、有限模拟各按原有范围阅读。 / Real studies, correspondence and finite simulations keep distinct scopes. |',
             '| 开放研究 / Open research | 目标、猜想和拟议检验；不计作完成结果。 / Targets, conjectures and proposed tests, not completed results. |', '',
             '角色、边界、认识和评价都按[非二元方法](../unified-2026-10-05/NONDUAL-METHOD.md)理解为同一展开中形成的关系。分类只是阅读分工，不把过程分成互不相关的事实、价值或主体与世界。正面成果、实际损失和反例均保留。', '',
             'Under the shared nondual method, roles, boundaries, knowing and evaluation are differentiated relations within one unfolding. The catalogue’s categories organize reading; they do not split reality into independent domains. Positive results, losses and counterexamples remain visible.', '',
             '## 逐项列表 / Complete chapter list', '',
             '编号沿用原文件名，支持页面搜索（中文、英文或文件名）。每项的 Lean 栏只指认具体对应；“有 Lean”不表示整个哲学结论都已获证。', '',
             'Identifiers follow source filenames. Search by Chinese, English or filename. A Lean link identifies a particular correspondence; it does not certify the entire philosophical claim.', '',
             '| 编号 / ID | 中英标题 / Bilingual title | 类别 / Category |', '|---|---|---|']
    for d in sorted(chapters, key=lambda x:x['id']):
        lines.append(f"| [`{d['id']}`]({chapter_link(d['id'])}) | {d['title_zh']} / {d['title_en']} | {category(d)} |")
    lines.extend(['', '## 维护 / Maintenance', '',
                  '条目数据位于 [A–L](data/arguments-a-l.json)、[M–Z](data/arguments-m-z.json)和[分支表](data/theory-map.json)。`source_sha256` 记录阅读对应的源码版本；原文变化后须重读相关条目。以本目录取代复制工作区；原始研究继续在既有理论与研究文件中修订。', '',
                  'The JSON registers hold the paired readings. `source_sha256` records the inspected version; changed sources require a targeted reread. Continue substantive work in the existing study files.', '',
                  '```sh',
                  'python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_results_catalogue.py --check',
                  'python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_lean_catalogue.py --check',
                  '```', '',
                  '这些命令从仓库根目录执行，只核对目录、字段、链接与快照，不编译 Lean，也不增加科学证据。更新时先修订受影响的中英条目和版本标记，再去掉 `--check` 生成相应目录；Lean 的实际复现按各包自己的 README 进行。详见[本轮编辑记录](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RESULTS-CATALOGUE-RECORD.md)。', '',
                  'Run from the repository root. These checks validate documentation, links and snapshots, not Lean proofs. Review affected bilingual entries and version markers before regeneration. Reproduce formal results through each package’s own instructions.'])
    return '\n'.join(lines)+'\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    chapters = []
    for name in ('arguments-a-l.json', 'arguments-m-z.json'):
        chapters += json.loads((OUT/'data'/name).read_text())
    branches = json.loads((OUT/'data/theory-map.json').read_text())
    errors=[]
    for label, rows, expected in (
        ('chapters', chapters, {str(p.relative_to(ROOT)) for p in CANON.glob('*.md')}),
        ('branches', branches, {str(p.relative_to(ROOT)) for p in (ROOT/'theories').glob('*/README.md')})):
        actual={x['source'] for x in rows}
        if actual != expected:
            errors.append(f'{label} missing={sorted(expected-actual)}, extra={sorted(actual-expected)}')
        if len({x['id'] for x in rows}) != len(rows): errors.append(f'Duplicate {label} IDs')
        for d in rows:
            for field in FIELDS:
                if not isinstance(d.get(field), str) or not d[field].strip(): errors.append(f'{d.get("id")}: missing {field}')
            for source in [d['source'], *d.get('lean',[]), *d.get('evidence',[])]:
                if not (ROOT/source.split('#')[0]).exists(): errors.append(f'{d["id"]}: missing path {source}')
            if (ROOT/d['source']).is_file():
                digest=hashlib.sha256((ROOT/d['source']).read_bytes()).hexdigest()
                if d.get('source_sha256') != digest: errors.append(f'{d["id"]}: source changed; reread entry before refreshing its hash')
    outputs={'README.md':index(chapters,branches),'THEORY-MAP.md':branch_volume(branches),
             'ARGUMENTS-A-L.md':chapter_volume([d for d in chapters if d['id'][0].upper()<='L'], 'A–L'),
             'ARGUMENTS-M-Z.md':chapter_volume([d for d in chapters if d['id'][0].upper()>'L'], 'M–Z')}
    if not errors:
        for name,body in outputs.items():
            target=OUT/name
            if args.check:
                if not target.exists() or target.read_text()!=body: errors.append(f'Stale generated file: {target.relative_to(ROOT)}')
            else: target.write_text(body)
    # Validate relative Markdown file targets in this documentary release.
    files=[ROOT/'README.md', *OUT.rglob('*.md')]
    checked_links=0
    checked_fragments=0
    for p in files:
        text=p.read_text()
        for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\n]+?)\)', text):
            target=match.group(1).strip().strip('<>')
            if urlsplit(target).scheme: continue
            pathname, _, fragment=target.partition('#')
            target=unquote(pathname)
            dest=(p.parent/target).resolve() if target else p.resolve()
            checked_links+=1
            if not dest.exists():
                errors.append(f'{p.relative_to(ROOT)}: broken target {target}')
            elif fragment and dest.suffix.lower()=='.md':
                checked_fragments+=1
                if unquote(fragment) not in anchors(dest): errors.append(f'{p.relative_to(ROOT)}: missing anchor {target}#{fragment}')
            elif fragment and dest.suffix.lower()=='.lean':
                checked_fragments+=1
                m=re.fullmatch(r'L(\d+)(?:-L(\d+))?',fragment)
                if m and int(m.group(2) or m.group(1))>line_count(dest): errors.append(f'Line beyond source: {target}#{fragment}')
    print(json.dumps({'chapters':len(chapters),'branches':len(branches),'local_file_links_checked':checked_links,'fragments_checked':checked_fragments,'errors':errors},ensure_ascii=False,indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
