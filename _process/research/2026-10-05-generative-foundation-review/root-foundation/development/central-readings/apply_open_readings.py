#!/usr/bin/env python3
"""A1 (18 October 2026): the list of open readings, at M1's request after its landing of chapter section 7. In the English
chapter's section 8.4 it adds the readings sections 7.2-7.5 mark open (M1's line, with the three open readings of 7.3 it
did not name) and completes the where-a-level-couples entry with its second clause. The Chinese edition's section 8 had
no such list: it gets one, mirroring 8.4, and five of its block headings get the closing bold marker the restructure
(54180d652) dropped. Every edit must match exactly once; a file already edited is skipped.
usage (from the repository root): python3 -B apply_open_readings.py"""
import sys

CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CZ = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
LIGHT = '../../../sources/15-codex-theory-conversations/2026-10-18-the-light-and-alignment-for-all.md'
LEVEL = '../results/records/where-a-level-couples.md'
OBS = '../results/records/observation-is-a-route.md'

EN = [
    ('it marks where a level can couple into a formation by level, as dependence marks where it can couple by threshold.\n'
     '- Kept as a conjecture',
     "it marks where a level can couple into a formation by level, as dependence marks where it can couple by threshold; "
     "registration bounds coupling, and a law's responses are its couplings.\n"
     '- Kept as a conjecture'),
    ('`apart_only_downstream` shows only that observing lies within the downstream, the reading taken on 18 October 2026 '
     '(D43).\n',
     '`apart_only_downstream` shows only that observing lies within the downstream, the reading taken on 18 October 2026 '
     '(D43).\n'
     '- §7.2–§7.5: 无明 read as the position of every formation in alignment; capability read as reach, the gap being '
     'reach less coupling; 明 read as a relation that widens as measurement, models and others are joined; holding 明 '
     'for others (measurement, models others can check, pools that include those an act reaches), with correction '
     "reaching the rule and each law's scope kept exact; alignment for all as pooled coupling across intelligences; the "
     f"conditional direction's opportunities to correct read as the routes of 明 ([source]({LIGHT})).\n"),
]

ZH = [
    ('\n\n**仍属于 Ren 的\n',
     '\n\n**尚未采用的读法**（AI 的，开放）。\n\n'
     f'- [where-a-level-couples]({LEVEL})：`obs` 不是耦合与读之外的第二种关系：它标出水平能经水平耦合入形成之处，如依存标出能经阈'
     '耦合之处；所识界定耦合，律的回应即其耦合。\n'
     f'- 作为猜想保留，不是读法（[observation-is-a-route]({OBS})）：观察不是依赖之外的第二种关系。`apart_only_downstream` 只表明'
     '观察在下游之内，这是 2026-10-18 所取的读法（D43）。\n'
     '- 第 7.2–7.5 节：无明读作对齐中每个形成的位置；能力读作所及，缺口是所及减去耦合；明读作关系，随量度、模型与他者的接入而扩展；'
     '为他者持明（量度、他者能检查的模型、包含动作所及者的组），纠正须及于规则，各规律的范围保持精确；为一切的对齐读作跨智能的合起来'
     f'的耦合；有条件之方向中纠正的机会读作明之路（[来源]({LIGHT})）。\n\n'
     '**仍属于 Ren 的**\n'),
    ('\n**依 Ren 的交托决定的读法\n', '\n**依 Ren 的交托决定的读法**\n'),
    ('\n**哲学根据\n', '\n**哲学根据**\n'),
    ('\n**经验对应\n', '\n**经验对应**\n'),
    ('\n**进一步的证明\n', '\n**进一步的证明**\n'),
]

MARK = {CH: '- §7.2–§7.5: 无明 read as the position', CZ: '**尚未采用的读法**（AI 的，开放）'}


def main():
    for path, pairs in ((CH, EN), (CZ, ZH)):
        text = open(path, encoding='utf-8').read()
        if MARK[path] in text:
            print('already edited', path)
            continue
        for old, new in pairs:
            n = text.count(old)
            if n != 1:
                sys.exit(f'{path}: expected one match, found {n}: {old[:90]!r}')
            text = text.replace(old, new)
        open(path, 'w', encoding='utf-8').write(text)
        print('edited', path, len(pairs))


if __name__ == '__main__':
    main()
