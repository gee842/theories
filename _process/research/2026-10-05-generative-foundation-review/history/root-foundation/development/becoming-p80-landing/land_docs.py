#!/usr/bin/env python3
"""After the checkers and apply_docs.py: the totals in the chapter's section 9 and the study's English summary
(with the sections not yet independently reviewed running to P80's section, and the periphery receipt), the
reading-catalogue entry (sentence, Lean list, and the chapter's new hash), from the receipts.
Usage: python3 -B land_docs.py W S

The entry's hash must be that of the chapter at HEAD (the entry current before this landing), or the run stops so
the entry can be reread against the chapter's change. Run before make_records.py and repoint.py, after every chapter
edit, so the hashes they record are final."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
S = int(sys.argv[2])
D = 'experiments/integrated-correction/general-framework/generative-basis/lean'
receipt = json.loads((W / D / 'becoming/becoming-verification.json').read_text())
periphery = json.loads((W / D / 'universal-ethics/generative-capacity/correction-inquiry-verification.json').read_text())
assert receipt['status'] == periphery['status'] == 'passed'
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


CHAPTER_PATH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
chapter = W / CHAPTER_PATH
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
end = s.index('\n', last.start())
para = s[last.start():end]
para = para.replace(last.group(0), f'The package now has {N_THM} theorems and {N_DECL} declaration audits, over a core closure of {N_CORE} modules and a package of {N_PKG}')
unreviewed = re.search(r', 71 to (\d+) \(72 and 73', para)
assert unreviewed, 'the unreviewed sections changed form; reread the paragraph'
assert int(unreviewed.group(1)) < S, (unreviewed.group(1), S)
para = para.replace(unreviewed.group(0), f', 71 to {S} (72 and 73')
para = sub1(para, r'(The periphery bridge passed against this core \(receipt )\d{8}T\d{6}\.\d+Z\)', r'\g<1>' + periphery['utc'] + ')')
s = s[:last.start()] + para + s[end:]
study.write_text(s)

EN = ("Responses as the dynamics give need no axiom: where the rest follows one law of exchange reading what has stood, two "
      "balanced flows in which the part acts alike are one flow, the course the law generates balances exactly where it is "
      "feasible, and the counterfactual of an act is that course; where the law reads only what each formation registers, "
      "responding through registration is a theorem, with finitely many conditions the least registration being what the "
      "law is sensitive to, so the comparison is decided within the responsive reach with neither the second flow nor the "
      "response supplied; an act not taken is an intervention of the standard causal model (P80; the law is supplied, and "
      "the readings are the AI's, pending Ren). ")
ZH = ("由动力学给出的回应不用公理：其余遵从一个读已立者的交换律时，部分动作相同的两个平衡的流是一个流，律生成的进程恰在可行之处平衡，"
      "一个动作的反事实就是这个进程；律只读各形成所识时，经识回应是定理，条件有限时最小的识是律的敏感，所以比较在回应所及之内决定，"
      "不另给第二个流与回应；未取的动作是标准因果模型的干预（P80；律是给出的，读法是 AI 的，待 Ren）。")
cat = W / 'theories/becoming/results/data/arguments-m-z.json'
raw = cat.read_text()
data = json.loads(raw)
entry = next(d for d in data if d['id'] == 'the-theory-of-becoming')
head_chapter = subprocess.run(['git', 'show', f'HEAD:{CHAPTER_PATH}'], cwd=W, capture_output=True, check=True).stdout
assert entry['source_sha256'] == hashlib.sha256(head_chapter).hexdigest(), \
    'the entry was not current with the chapter at HEAD; reread it against the chapter before refreshing the hash'
after_en = "(P64–P68; the readings are the AI's, pending Ren). "
after_zh = "（P64–P68；读法是 AI 的，待 Ren）。"
assert entry['argument_en'].count(after_en) == 1 and entry['argument_zh'].count(after_zh) == 1
assert EN not in entry['argument_en']
entry['argument_en'] = entry['argument_en'].replace(after_en, after_en + EN)
entry['argument_zh'] = entry['argument_zh'].replace(after_zh, after_zh + ZH)
L = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
lean = entry['lean']
assert L + 'Counterfactual.lean' not in lean
lean.insert(lean.index(L + 'Response.lean') + 1, L + 'Counterfactual.lean')
entry['source_sha256'] = hashlib.sha256(chapter.read_bytes()).hexdigest()
indent = 2 if raw.startswith('[\n  {') else 1
out = json.dumps(data, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else '')
assert json.loads(out) == data
cat.write_text(out)
print('reading entry: sentence,', len(lean), 'Lean files, chapter hash', entry['source_sha256'][:12])
