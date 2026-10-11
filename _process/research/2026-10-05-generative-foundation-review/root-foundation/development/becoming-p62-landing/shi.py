#!/usr/bin/env python3
"""The Chinese for "registers" becomes 识 (Ren, 11 October 2026: "for registers, use 识").

Usage: python3 -B shi.py ROOT

- P49, P53 and P55 wrote 反映: every 反映 in their text becomes 识, with the phrasing adjusted
  where a condition or support was the subject (识 takes the formation as subject; a condition
  被识).
- P42 wrote 计入 in the sense of "registers": those phrases are listed exactly and become 识.
  计入 in the sense of "counts, takes into account" (必须计入, 谁的延续计入, 联合计入) stays.

Only the named files and sections are touched; each listed P42 phrase must occur at least once
where it is applied.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = ROOT / f'{RF}/BECOMING-RENEWAL-READING.md'
PLAN = ROOT / f'{RF}/BECOMING-UNIFICATION-PLAN.md'
CHAPTER = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
README = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md'
RECORDS = ROOT / 'theories/becoming/results/records'

# 反映 (P49, P53, P55) -> 识, most specific first.
SHI = [
    ('反映与检验', '识与检验'),
    ('经自身反映的回路所不能反映的', '经自身之识的回路所不能识的'),
    ('反映闭包', '识闭包'),
    ('条件只反映它是否满足所需', '条件只以是否满足所需被识'),
    ('观察的条件反映其水平', '观察的条件以其水平被识'),
    ('支持只反映净交换', '经支持只识得净交换'),
    ('支持只反映与其所依存者的交换', '经支持只识得与其所依存者的交换'),
    ('作为阈值反映', '作为阈值被识'),
    ('经承担自身反映', '经承担自身被识'),
    ('立刻反映', '立刻识之'),
    ('第二步反映它', '第二步识之'),
    ('则反映每一口', '则识每一口'),
    ('无人反映之条件', '无人识之条件'),
    ('自身的反映', '自身之识'),
    ('自己的反映', '自己之识'),
    ('他者的反映', '他者之识'),
    ('它的反映', '它之识'),
    ('经支持的反映', '经支持之识'),
    ('自身反映与', '自身之识与'),
    ('都反映相同', '都识得相同'),
    ('反映相同', '识得相同'),
    ('被反映', '被识'),
    ('所反映', '所识'),
    ('能被反映', '能被识'),
    ('反映', '识'),
]

# 计入 in the sense of "registers" (P42), exact phrases.
JI = [
    ('一个形成的支持只计入与其所依存者的交换', '一个形成经支持只识得与其所依存者的交换'),
    ('形成的支持只计入与其所依存者的交换', '形成经支持只识得与其所依存者的交换'),
    ('一个形成的支持只计入直接到达它的部分', '一个形成经支持只识得直接到达它的部分'),
    ('恰经其与一个条件的净交换计入该条件', '恰经其与一个条件的净交换在该条件上被识'),
    ('反馈至多计入能影响它的', '反馈至多识及能影响它的'),
    ('反馈至多计入其影响闭包', '反馈至多识及其影响闭包'),
    ('反馈至多计入影响闭包', '反馈至多识及影响闭包'),
    ('反馈至多计入它', '反馈至多识及它'),
    ('反馈所能计入的', '反馈所能识的'),
    ('反馈所计入者', '反馈所识者'),
    ('反馈能计入哪些', '反馈能识得哪些'),
    ('不能计入哪些', '不能识得哪些'),
    ('反馈能计入什么', '反馈能识得什么'),
    ('反馈计入什么', '反馈识得什么'),
    ('所能计入的上界', '所能识的上界'),
    ('效果不在其中计入', '效果不在其中被识'),
    ('不在比较中计入', '不在比较中被识'),
    ('比较只计入直接的交换', '比较只识得直接的交换'),
    ('比较只计入部分直接的交换', '比较只识得部分直接的交换'),
    ('它只计入部分直接的交换', '它只识得部分直接的交换'),
    ('所支持的计入定理', '所支持的识的定理'),
    ('不是所计入者的刻画', '不是所识者的刻画'),
    ('而计入与比较定理', '而识与比较定理'),
    ('影响闭包之外不计入', '影响闭包之外不被识'),
    ('部分在所到达之处计入', '部分在所到达之处被识'),
    ('在闭包之内不被计入', '在闭包之内不被识'),
    ('在闭包之内都不被计入', '在闭包之内都不被识'),
    ('每一步都不被计入', '每一步都不被识'),
    ('每步都不被计入', '每步都不被识'),
    ('部分被计入', '部分被识'),
    ('这一损失才被计入', '这一损失才被识'),
    ('时被计入', '时被识'),
]


def shi(text):
    for a, b in SHI:
        text = text.replace(a, b)
    return text


def ji(text, used):
    for a, b in JI:
        if a in text:
            used.add(a)
            text = text.replace(a, b)
    return text


def sections(text, keep):
    """Apply shi() only within the study sections whose heading starts with one of `keep`."""
    parts = re.split(r'(?m)^(?=## )', text)
    return ''.join(shi(p) if any(p.startswith(k) for k in keep) else p for p in parts)


def ji_sections(text, keep, used):
    parts = re.split(r'(?m)^(?=## )', text)
    return ''.join(ji(p, used) if any(p.startswith(k) for k in keep) else p for p in parts)


def lines_with(text, markers, fn):
    return '\n'.join(fn(l) if any(m in l for m in markers) else l for l in text.split('\n'))


used = set()

# Study: P49, P53, P55 sections; P42 and P43 sections.
s = STUDY.read_text()
s = sections(s, ('## 70. ', '## 72. ', '## 73. '))
s = ji_sections(s, ('## 61. ', '## 62. '), used)
STUDY.write_text(s)

# Chapter: every 反映 is P49/P53/P55's; P42's phrases are specific.
c = CHAPTER.read_text()
c = shi(c)
c = ji(c, used)
CHAPTER.write_text(c)

# Plan: rows and bullets of P49, P53, P55; P42's row and bullet.
p = PLAN.read_text()
p = lines_with(p, ('| P49 ', '| P53 ', '| P55 ', '- **P49:**', '- **P53:**', '- **P55:**'), shi)
p = lines_with(p, ('| P42 ',), lambda l: ji(l, used))
PLAN.write_text(p)

# Package README: the rows of Testing, Experiment, Runaway; Feedback's row.
r = README.read_text()
r = lines_with(r, ('[`Becoming.Testing`]', '[`Becoming.Experiment`]', '[`Becoming.Runaway`]'), shi)
r = lines_with(r, ('[`Becoming.Feedback`]',), lambda l: ji(l, used))
README.write_text(r)


def walk_zh(x, fn):
    if isinstance(x, dict):
        return {k: (fn(v) if k == 'zh' and isinstance(v, str) else walk_zh(v, fn)) for k, v in x.items()}
    if isinstance(x, list):
        return [walk_zh(v, fn) for v in x]
    return x


HISTORY = {
    'zh': '2026-10-11：中文的 registers 改为“识”（Ren：“for registers, use 识”），原作“{old}”；断言不变。',
    'en': '2026-10-11: the Chinese for “registers” is now 识 (Ren: “for registers, use 识”), formerly {old}; the claim is unchanged.',
}

for ident, fn, old in [
    ('testing-within-registration', shi, '反映'), ('subthreshold-registration', shi, '反映'),
    ('experiment-needs-return', shi, '反映'), ('runaway-distance-unregistered', shi, '反映'),
    ('feedback-and-reach', lambda t: ji(t, used), '计入'), ('levels-of-closure', lambda t: ji(t, used), '计入'),
    ('comparison-within-reach', lambda t: ji(t, used), '计入'),
    ('consumption-ends-with-feeders', lambda t: ji(t, used), '计入'),
    ('whole-first-and-bounded-centers', lambda t: ji(t, used), '计入'),
]:
    path = RECORDS / f'{ident}.json'
    record = json.loads(path.read_text())
    before = json.dumps(record, ensure_ascii=False)
    record = walk_zh(record, fn)
    if json.dumps(record, ensure_ascii=False) != before:
        record['history'].append({k: v.format(old=old) for k, v in HISTORY.items()})
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        print('record', ident)

unused = [a for a, _ in JI if a not in used]
print('P42 phrases not found:', unused)
