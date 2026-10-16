#!/usr/bin/env python3
"""After the checkers: the reading-catalogue entry (sentence and Lean list) and the totals in the chapter's
section 9 and the study's English summary, from the receipt. Usage: python3 -B land_docs.py W"""
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

EN = ("Selection, response, mechanism and attraction need no axiom: a selection through a selector's registration "
      "selects two histories alike exactly when the selector registers them alike, so with the rest fixed it is blind "
      "beyond the registration closure; where the rest responds through its registration, a supplied premise, the "
      "comparison is decided within the part's responsive reach; a projection carries a determined law exactly where "
      "configurations alike under it go alike, what the step does not depend on is re-absorbed in one step, and the "
      "standard causal model x′ = F(x, u, ε) is a determined process whose move is the input and the noise; for every "
      "determined law a configuration is drawn into an absorbing region exactly where it does not return (P64–P68; the "
      "readings are the AI's, pending Ren). ")
ZH = ("选择、回应、机制与吸引不用公理：经选择者之识的选择恰在选择者把两段历史识得相同时把它们选得相同，所以其余固定时在识闭包之外不见；"
      "其余经识回应时（给出的前提），比较在部分的回应所及之内决定；投影恰在经它相同的配置同去之处承载确定的规律，步骤所不依者一步之内被重新吸收，"
      "标准因果模型 x′ = F(x, u, ε) 是动作为输入与噪声的确定过程；对每个确定的律，配置恰在不返回之处被某个吸收区域吸入"
      "（P64–P68；读法是 AI 的，待 Ren）。")
cat = W / 'theories/becoming/results/data/arguments-m-z.json'
data = json.loads(cat.read_text())
entry = next(d for d in data if d['id'] == 'the-theory-of-becoming')
after_en = "equivalent step by step to the representation as it is; adoption is Ren's. "
after_zh = "与原表示逐步等价，是否采用由 Ren 定。"
assert entry['argument_en'].count(after_en) == 1 and entry['argument_zh'].count(after_zh) == 1
assert EN not in entry['argument_en']
entry['argument_en'] = entry['argument_en'].replace(after_en, after_en + EN)
entry['argument_zh'] = entry['argument_zh'].replace(after_zh, after_zh + ZH)
L = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
lean = entry['lean']
for anchor, new in (('Experiment.lean', ['Mechanism.lean', 'Attraction.lean']), ('Runaway.lean', ['Response.lean', 'Selection.lean'])):
    i = lean.index(L + anchor)
    for k, name in enumerate(new):
        assert L + name not in lean
        lean.insert(i + 1 + k, L + name)
cat.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('reading entry: sentence and', len(lean), 'Lean files')
