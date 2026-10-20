"""R36: assemble the Chinese edition of the restructured chapter.

The Chinese edition mirrors the English headings and is shorter: each section of the drafted parts
(draft/ZH-A.md … ZH-D.md) gives its 要点 by hand, and this script adds, from the assembled English
edition, the anchors before each mirrored heading, the theorems the English section states (the
names its bullets lead with) with a link to it, and the records it links. It writes the theorem map
with the records' Chinese titles, the index of formal terms from the frozen Chinese glossary (rows
not among the core terms, first sentence of each meaning), the frozen edition's vocabulary tables
and crosswalk, and its section 11, section references renumbered.

Usage: python3 -B assemble_zh.py ROOT NEW_EN FROZEN_ZH OUT
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble  # noqa: E402
import glossary  # noqa: E402

PARTS = ['ZH-A', 'ZH-B', 'ZH-C', 'ZH-D']
HEAD = re.compile(r'^(#{2,3}) (\d+(?:\.\d+)?)\.? ')
LEAD = re.compile(r'^- ((?:`[^`]+`(?:,? (?:and|with) |, )?)+)')
EN_LINK = 'THE-THEORY-OF-BECOMING.md'

STANDING_ZH = [
    ('theorem, the condition among its hypotheses', '定理，条件在其假设中'),
    ('theorem under stated premises', '在所述前提下的定理'),
    ('theorem without premise', '不加前提的定理'),
    (' (periphery)', '（外围）'),
    ('open target', '开放目标'), ('superseded', '已被取代'), ('assessment', '评估'), ('argument', '论证'),
]
PREMISE_ZH = [
    ('the condition', '条件'), ('living significance', '生命意义'), ('monotonicity and supervenience', '单调与随附'),
    (' (three witnesses)', '（三个见证）'), (' (one instance)', '（一个实例）'), (' (one theorem)', '（一条定理）'),
    ('activity needing support', '活动需要支持'), ('a supplied law of exchange', '给出的交换之律'),
    ('balance', '平衡'), ('dissipation', '耗散'), ('embodiment', '体现'), ('transmission', '传递'),
    ('in the record', '见记录'), (', ', '、'),
]


SPECIAL = {'## 定理图': '## The theorem map', '## 前言': '## Preface', '### (a) ': '### (a) ', '### (b) ': '### (b) '}


def anchors_before(en, head):
    lines = en.split('\n')
    i = next(k for k, l in enumerate(lines) if l.startswith(head))
    out, k = [], i - 1
    while k >= 0 and (lines[k].startswith('<a id=') or not lines[k].strip()):
        if lines[k].startswith('<a id='):
            out.insert(0, lines[k])
        k -= 1
    return out


def slug(root, heading):
    sys.path[:0] = [str(root), str(root / 'tools' / 'research')]
    from tools.research import moves
    return moves.github_slug(heading)


def en_sections(root, en):
    """number -> {anchors, heading, names, records} for every numbered EN heading."""
    lines = en.split('\n')
    out = {}
    for i, l in enumerate(lines):
        m = HEAD.match(l)
        if not m:
            continue
        num = m.group(2)
        anchors, k = [], i - 1
        while k >= 0 and (lines[k].startswith('<a id=') or not lines[k].strip()):
            if lines[k].startswith('<a id='):
                anchors.insert(0, lines[k])
            k -= 1
        depth = len(m.group(1))
        body = []
        for l2 in lines[i + 1:]:
            h = re.match(r'^(#{1,3}) ', l2)
            if h and (len(h.group(1)) <= depth or depth == 2):
                break
            body.append(l2)
        names, recs = [], []
        for b in body:
            lm = LEAD.match(b)
            if lm:
                names += re.findall(r'`([^`]+)`', lm.group(1))
            for r in assemble.REC.findall(b):
                if r not in recs:
                    recs.append(r)
        out[num] = {'anchors': anchors, 'heading': l, 'slug': slug(root, l.lstrip('#').strip()),
                    'names': names, 'records': recs}
    return out


def zh_map(root, en_text):
    table, missing = assemble.theorem_map(root, en_text, zh=True)
    rows = table.split('\n')
    out = ['| 记录 | 地位 | 假设中的 §0 前提 | 节 |', '|---|---|---|---|']
    for r in rows[2:]:
        cells = r.strip('|').split(' | ')
        link, st, pr, sec = [c.strip() for c in cells]
        for a, b in STANDING_ZH:
            st = st.replace(a, b)
        if pr != '—':
            for a, b in PREMISE_ZH:
                pr = pr.replace(a, b)
        out.append(f'| {link} | {st} | {pr} | {sec} |')
    return '\n'.join(out), missing


def zh_first_sentence(text):
    depth, tick = 0, False
    for i, ch in enumerate(text):
        if ch == '`':
            tick = not tick
        elif not tick and ch in '(（':
            depth += 1
        elif not tick and ch in ')）':
            depth = max(depth - 1, 0)
        elif not tick and depth == 0 and ch in '。；':
            return text[:i] + '。'
    return text


def zh_glossary(frozen_zh):
    lines = frozen_zh.split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('## 10. 术语表'))
    retired = next(i for i, l in enumerate(lines) if l.startswith('### 退役的标签'))
    end = next(i for i, l in enumerate(lines) if l.startswith('## 11.'))
    rows, seen = [], set()
    for l in lines[start:retired]:
        if not l.startswith('| ') or l.startswith('|---') or l.startswith('| 中文 |'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split(' | ')]
        if len(c) < 4:
            continue
        zh, en, meaning, lean = c[0], c[1], c[2], c[3]
        if glossary.term_key(en) in glossary.CORE or en in glossary.CORE or zh in seen:
            continue
        seen.add(zh)
        rows.append(f'| {zh}（{en}） | {glossary.renumber(zh_first_sentence(meaning))} | {lean} |')
    tail = '\n'.join(lines[retired:end])
    tail = tail.replace('### 退役的标签', '<a id="退役的标签"></a>\n<a id="retired-labels"></a>\n### (c) 退役的标签与 Lean 名')
    tail = tail.replace('### 退役的 Lean 名（2026年10月18日）', '<a id="退役的-lean-名2026年10月18日"></a>\n**退役的 Lean 名（2026年10月18日）。**')
    tail = tail.replace('### 退役的 Lean 名（2026年10月20日）', '<a id="退役的-lean-名2026年10月20日"></a>\n**退役的 Lean 名（2026年10月20日）。**')
    tail = tail.replace('### 闭与开：对照', '<a id="crosswalk-to-the-corpus-glossary"></a>\n### (d) 与语料词汇表的对照\n\n见[英文版 (d)](THE-THEORY-OF-BECOMING.md#crosswalk-to-the-corpus-glossary)。\n\n<a id="闭与开对照"></a>\n<a id="closing-and-opening-a-crosswalk"></a>\n### (e) 闭与开：对照')
    tail = tail.replace('本章只在此表中解释这些旧标签', '本章只在此处解释这些旧标签')
    s11 = '\n'.join(lines[end - 1 if lines[end - 1].startswith('<a id=') else end:])
    return rows, glossary.renumber(tail), glossary.renumber(s11)


def main():
    root, new_en, frozen_zh, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
    en = new_en.read_text()
    secs = en_sections(root, en)
    text = '\n'.join((HERE / 'draft' / f'{p}.md').read_text().rstrip('\n') + '\n' for p in PARTS)
    lines = text.split('\n')
    res, cur, present = [], None, set(re.findall(r'<a id="([^"]+)"', text))

    def close(num):
        s = secs.get(num)
        if not s:
            return
        subs = [k for k in secs if k.startswith(num + '.')]
        if subs and '.' not in num:
            if s['records']:
                res.append('记录：' + '、'.join(f'[{r}](../results/records/{r}.md)' for r in s['records']) + '。')
                res.append('')
            return
        part = f'完整陈述见[英文版 §{num}]({EN_LINK}#{s["slug"]})。'
        if s['names']:
            names = '、'.join(f'`{n}`' for n in dict.fromkeys(s['names']))
            res.append(f'**定理。** 本节陈述 {names}；{part}')
        else:
            res.append(f'**陈述。** {part}')
        res.append('')
        if s['records']:
            res.append('记录：' + '、'.join(f'[{r}](../results/records/{r}.md)' for r in s['records']) + '。')
            res.append('')

    for l in lines:
        m = HEAD.match(l)
        special = l.startswith('## 定理图') or l.startswith('## 8. ') or l.startswith('## 9. ') or l.startswith('## 10. ') or l.startswith('### (')
        if (m or l.startswith('## ')) and cur is not None:
            close(cur)
            cur = None
        if m:
            num = m.group(2)
            for a in secs.get(num, {}).get('anchors', []):
                aid = re.search(r'id="([^"]+)"', a).group(1)
                if aid not in present:
                    res.append(a)
                    present.add(aid)
            if num.split('.')[0] in '1234567' and not special:
                cur = num
        for zh_head, en_head in SPECIAL.items():
            if l.startswith(zh_head):
                for a in anchors_before(en, en_head):
                    aid = re.search(r'id="([^"]+)"', a).group(1)
                    if aid not in present:
                        res.append(a)
                        present.add(aid)
        res.append(l)
    if cur is not None:
        close(cur)
    text = '\n'.join(res)
    table, missing = zh_map(root, en)
    text = re.sub(r'<!-- theorem-map:begin -->.*?<!-- theorem-map:end -->',
                  lambda _m: '<!-- theorem-map:begin -->\n' + table + '\n<!-- theorem-map:end -->', text, flags=re.S)
    rows, tail, s11 = zh_glossary(frozen_zh.read_text())
    text = text.replace('<!-- glossary-index -->', '\n'.join(['| 术语 | 含义 | Lean |', '|---|---|---|'] + rows) + '\n\n' + tail.strip('\n'))
    s11 = s11.replace('§6.15', '§6.4').replace('理论的完整陈述', '定理图')
    frozen_row = ('| 移至历史 | [生成／变化之论，2026-10-20](../history/THE-THEORY-OF-BECOMING-2026-10-20.zh.md) | '
                  '本章 2026 年 10 月 20 日改组（R36）之前的中文版，连同英文版原样冻结（回执 `_process/architecture/moves/R36-chapter.json`）。'
                  '它所陈述的每项结果、前提、边界、反例与开放项都在本章英文版或其所链接的记录中；保存审计见[研究 §227](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#227-the-chapter-once-r36)。 |')
    s11 = re.sub(r'(\|---\|---\|---\|\n)', lambda m: m.group(1) + frozen_row + '\n', s11, count=1)
    text = text.rstrip('\n') + '\n\n' + s11.strip('\n') + '\n'
    out.write_text(text)
    print(f'wrote {out}: {len(text.encode())} bytes, {text.count(chr(10))} lines; unplaced records: {missing}', file=sys.stderr)


if __name__ == '__main__':
    main()
