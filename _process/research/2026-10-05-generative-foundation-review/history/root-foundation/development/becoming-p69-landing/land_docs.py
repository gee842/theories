#!/usr/bin/env python3
"""After the checkers, before make_records.py: the totals in the chapter's section 9 and the study's closing
counts, and the reading-catalogue entry (sentence and Lean list), from the receipt.
Usage: python3 -B land_docs.py W"""
import json
import re
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
D = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
receipt = json.loads((W / D / 'becoming-verification.json').read_text())
spine = [m for m in receipt['modules'] if m['spine']]
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_CORE = len(receipt['core_closure'])
N_PKG = len(spine)
print('totals', N_THM, N_DECL, N_CORE, N_PKG)


def sub1(s, pattern, repl):
    s2, n = re.subn(pattern, repl, s)
    assert n == 1, (pattern, n)
    return s2


chapter = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
s = chapter.read_text()
s = sub1(s, r'覆盖 \d+ 项定理、\d+ 项声明审计，源声明的公理报告全部为空；核心闭包共 \d+ 个模块（包 \d+ 个模块',
         f'覆盖 {N_THM} 项定理、{N_DECL} 项声明审计，源声明的公理报告全部为空；核心闭包共 {N_CORE} 个模块（包 {N_PKG} 个模块')
s = sub1(s, r'cover \d+ theorems and \d+ declaration audits, all source declarations with empty axiom reports; the core closure has \d+ modules \(the package \d+',
         f'cover {N_THM} theorems and {N_DECL} declaration audits, all source declarations with empty axiom reports; the core closure has {N_CORE} modules (the package {N_PKG}')
chapter.write_text(s)

study = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
s = study.read_text()
matches = list(re.finditer(r'The package now has \d+ theorems and \d+ declaration audits, over a core closure of \d+ modules and a package of \d+', s))
assert matches
last = matches[-1]
s = s[:last.start()] + f'The package now has {N_THM} theorems and {N_DECL} declaration audits, over a core closure of {N_CORE} modules and a package of {N_PKG}' + s[last.end():]
study.write_text(s)

EN = ("The labelled process and the frame are readings of one unfolding, a world, with no premise: read within the "
      "configuration the move changes no run and is what the law leaves open, and a world's move is its relata's "
      "exchange; every history is a run of the law it shows, the least one, determined exactly where the history is "
      "consistent, the correspondence failing to be an identity through dead ends and splices; a claim is a relatum and "
      "novelty is arising; configurations are alike where a bisimulation relates them, and a description makes sense "
      "exactly where it identifies the alike ones (P69; Ren agreed that law and history are one unfolding read two ways, "
      "“there are no two realities”; the other readings are the AI's, pending Ren). ")
ZH = ("带标签的过程与框架是同一展开即一个世界的读法，不加前提：动作读入配置时运行不变，就是律所留开的；世界的动作是关系项的交换；"
      "每段历史是它所显示之律的运行，最小的律，恰在历史一致处确定，对应经死路与拼接而不是同一；主张是关系项，新实现就是生起；"
      "配置在互模拟联系处相同，有意义的描述恰把相同者等同（P69；Ren 同意律与历史是同一展开的两种读法，“there are no two realities”；"
      "其余读法是 AI 的，待 Ren）。")
AFTER_EN = "(P64–P68; the readings are the AI's, pending Ren). "
AFTER_ZH = "（P64–P68；读法是 AI 的，待 Ren）。"
cat = W / 'theories/becoming/results/data/arguments-m-z.json'
data = json.loads(cat.read_text())
entry = next(d for d in data if d['id'] == 'the-theory-of-becoming')
assert entry['argument_en'].count(AFTER_EN) == 1 and entry['argument_zh'].count(AFTER_ZH) == 1
assert EN not in entry['argument_en']
entry['argument_en'] = entry['argument_en'].replace(AFTER_EN, AFTER_EN + EN)
entry['argument_zh'] = entry['argument_zh'].replace(AFTER_ZH, AFTER_ZH + ZH)
L = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
lean = entry['lean']
assert L + 'Unfolding.lean' not in lean
lean.insert(lean.index(L + 'Mechanism.lean') + 1, L + 'Unfolding.lean')
cat.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('reading entry: sentence and', len(lean), 'Lean files')
