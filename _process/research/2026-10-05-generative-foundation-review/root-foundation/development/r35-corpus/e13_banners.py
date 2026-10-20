#!/usr/bin/env python3
"""R35 step 3, E13: dated round banners at chapter heads go to history; one status line takes their place.

A banner is a paragraph before the chapter's first `##` that opens in bold (or as a bold quote) with a date of
2026 in its lead, the round-by-round notices of 5-13 October 2026. Each live chapter below keeps its title, its
dated authorship line and its opening statement; its banners move verbatim, in order, to
theories/becoming/history/<NAME>-rounds-2026-10-20.md (with the source path and commit), and one status line saying
what the chapter is now and where the banners went takes the place of the first. The 17 October "Restructured"
notes are already status lines pointing to history and stay; BECOMING-FOUNDATION's banner of 19 October is its
current status line and stays. Links inside a moved banner are relative to theories/becoming/chapters/ (said in
the history file); the history file is frozen, not rewritten.

usage (from the checkout root): python3 -B e13_banners.py [--apply]
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CH = ROOT / 'theories/becoming/chapters'
HI = ROOT / 'theories/becoming/history'
APPLY = '--apply' in sys.argv
DATE = re.compile(r'20\d\d-\d\d-\d\d|\d{1,2} (?:October|September) 2026|2026年\d{1,2}月\d{1,2}日')
GOAL = '../../../GOALS.md'
R = '../results/records/'

EN = {
    'THE-THEORY-OF-EVOLUTION': ('live: the chapter of the separately authorized evolution programme (goal '
                                f'[theory-of-evolution]({GOAL}#theory-of-evolution)), cited by §2 and §8.2 of '
                                '[the canonical chapter](THE-THEORY-OF-BECOMING.md)'),
    'WISDOM-AND-CONTEXT': f'live: statement source of the open target [wisdom-root]({R}wisdom-root.md) (canonical chapter §8.1)',
    'CHOICE-AND-GENERATIVE-CONTEXT': f'live: statement source of [open-form-realization-under-revision]({R}open-form-realization-under-revision.md)',
    'BASIC-CONFLICT-JUDGMENT': f'live: statement source of [finite-aggregation-within-restorable-basic-losses]({R}finite-aggregation-within-restorable-basic-losses.md)',
    'ZERO-AXIOM-PRACTICAL-JUDGMENT': f'live: statement source of the open target [universal-practical-warrant]({R}universal-practical-warrant.md) (canonical chapter §8.1)',
    'ETHICAL-LEARNING': f'live: statement source of [organizational-formation-from-generative-comparison]({R}organizational-formation-from-generative-comparison.md)',
    'PRACTICAL-JUDGMENT': f'live: statement source of [practical-judgment-under-living-significance]({R}practical-judgment-under-living-significance.md)',
    'MARKETS-AND-GENERATIVE-REGIMES': 'live: statement source of the market records, cited by §4 of [the canonical chapter](THE-THEORY-OF-BECOMING.md)',
    'MATHEMATICAL-CORE': 'live: an exposition of the foundation module `GenerativeCore`, unchanged since 6 October 2026',
    'SCIENTIFIC-PHILOSOPHY': 'live: statement source of the open target on scientific inquiry (canonical chapter §8.1)',
}
ZH = {
    'ZERO-AXIOM-PRACTICAL-JUDGMENT.zh': f'现行：开放目标 [universal-practical-warrant]({R}universal-practical-warrant.md) 的陈述来源（规范章节 §8.1）',
    'ETHICAL-LEARNING.zh': f'现行：[organizational-formation-from-generative-comparison]({R}organizational-formation-from-generative-comparison.md) 的陈述来源',
}


def banners(text):
    """(head paragraphs, indexes of banners) for the part before the first `##`."""
    cut = text.find('\n## ')
    cut = len(text) if cut < 0 else cut
    head = text[:cut]
    paras = head.split('\n\n')
    idx = []
    for i, p in enumerate(paras):
        s = p.lstrip()
        lead = s[:200]
        if (s.startswith('**') or s.startswith('> **')) and DATE.search(lead.split('**')[1] if '**' in lead else '') \
                and 'Restructured' not in lead and '重构' not in lead:
            idx.append(i)
    return head, paras, idx, text[cut:]


commit = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', '--short=9', 'HEAD'], capture_output=True, text=True).stdout.strip()
total = 0
for name, status in list(EN.items()) + list(ZH.items()):
    path = CH / f'{name}.md'
    text = path.read_text()
    head, paras, idx, rest = banners(text)
    if not idx:
        print(name, 'no banners')
        continue
    zh = name in ZH
    base = name[:-3] if name.endswith('.zh') else name
    hist = HI / (f'{base}-rounds-2026-10-20.zh.md' if name.endswith('.zh') else f'{base}-rounds-2026-10-20.md')
    rel = f'../history/{hist.name}'
    dates = sorted({d for i in idx for d in DATE.findall(paras[i][:200])})
    if zh:
        line = (f'> **状态：**{status}。2026 年 10 月各轮的说明（{len(idx)} 段）原文保存在[轮次历史]({rel})。')
        title = f'# {base}：各轮说明（2026-10-20 移出）'
        about = (f'R35（第二十次评审 E13）把这些段落从 `theories/becoming/chapters/{name}.md` 的章首原文移到这里'
                 f'（提交 `{commit}` 时的文本，顺序不变）。其中的相对链接以 `theories/becoming/chapters/` 为基准。')
    else:
        notes = 'Its dated round note of October 2026 is' if len(idx) == 1 else f'Its {len(idx)} dated round notes of October 2026 are'
        line = f'> **Status:** {status}. {notes} kept verbatim in [its rounds history]({rel}).'
        title = f'# {base}: round notes (moved 20 October 2026)'
        about = (f'Moved verbatim by R35 (twentieth review, E13) from the head of `theories/becoming/chapters/{name}.md`, '
                 f'as of commit `{commit}`, in their order. Their relative links are relative to `theories/becoming/chapters/`.')
    kept = [p for i, p in enumerate(paras) if i not in idx]
    kept.insert(idx[0], line)
    new = '\n\n'.join(kept) + rest
    body = '\n\n'.join(paras[i] for i in idx)
    hist_text = f'{title}\n\n{about}\n\n---\n\n{body}\n'
    total += len(idx)
    print(f'{name}: {len(idx)} banners, {len(body.encode())} bytes -> {hist.relative_to(ROOT)}')
    if APPLY:
        assert not hist.exists(), hist
        hist.write_text(hist_text)
        path.write_text(new)
print(total, 'banners')
