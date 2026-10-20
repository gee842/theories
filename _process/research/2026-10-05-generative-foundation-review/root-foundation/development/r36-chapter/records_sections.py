"""R36: renumber the citations of the old chapter's section 6 in the live fields of records.

The restructured chapter has five sections in section 6 (study section 227). A record citing the frozen
edition's numbering is re-pointed by content, each mapping read against the new chapter:

  old 6.15 (if the continuation of anything has significance)   -> 6.4
  old 6.12 (courses compared on possibilities)                  -> 6.5  (Ranking.possible_extends_iff is in 6.5)
  old 6.11 (the condition decomposed)                           -> 6.5
  old 6.7, the reading S0 as wanting                            -> 6.2
  old 6.7, the witnesses Downstream, Mortal, ...                -> 6.3  (the derived extent and its witnesses)

Only live fields change (not history, text_versions, references or proof_bindings); a quotation of the old
chapter's words (what-taking-all-excludes, correspondence) is kept as quoted. Each record whose text changes
gets one history note (en and zh); the hash re-points go through repoint.py. Without --apply, a dry run.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
RECORDS = ROOT / 'theories/becoming/results/records'
SKIP = {'history', 'text_versions', 'references', 'proof_bindings'}

# record id -> list of (old substring, new substring); each must occur in some live field
EDITS = {
    'comparison-by-widening': [('(chapter section 6.12)', '(chapter section 6.5)'), ('（章节 §6.12）', '（章节 §6.5）')],
    'continuation-condition-decomposition': [('chapter sections 6.11 and 8.5', 'chapter sections 6.5 and 8.5'),
                                             ('见理论 §6.11 与 §8.5', '见理论 §6.5 与 §8.5')],
    'continuation-condition-yields-living-significance': [
        ('(the reading of section 6.7:', '(the reading of section 6.2:'), ('（§6.7 的读法：', '（§6.2 的读法：'),
        ('the reading of section 6.7 is', 'the reading of section 6.2 is'), ('第 6.7 节的读法是', '第 6.2 节的读法是')],
    'metaethical-core-characterization': [
        ('the conditional section 6.15 of the chapter', 'the conditional section 6.15 of the chapter (section 6.4 since R36)'),
        ('章节 §6.15 的条件小节', '章节 §6.15 的条件小节（R36 起为 §6.4）')],
    'only-the-order-of-change-shows': [('the condition of section 6.15 uses', 'the condition of section 6.4 uses'),
                                       ('§6.15 的条件所用者', '§6.4 的条件所用者')],
    'positive-ground-open-futures': [('(chapter section 6.15;', '(chapter section 6.4;'), ('（章节 §6.15，', '（章节 §6.4，')],
    'ranking-under-readings': [('in chapter section 6.12.', 'in chapter section 6.5.'), ('理由见章节 §6.12。', '理由见章节 §6.5。')],
    'unity-of-readings': [('(the condition of section 6.15)', '(the condition of section 6.4)'),
                          ('（§6.15 的条件）', '（§6.4 的条件）')],
    'what-taking-all-excludes': [('the witnesses of section 6.7', 'the witnesses of section 6.3'),
                                 ('第 6.7 节的见证', '第 6.3 节的见证'), ('第 6.7 节见证', '第 6.3 节见证')],
    'where-two-courses-rejoin': [("the chapter's section 6.15", "the chapter's section 6.4"),
                                 ('本章第 6.15 节', '本章第 6.4 节'), ("section 6.15's comparison", "section 6.4's comparison"),
                                 ('经第 6.15 节的比较', '经第 6.4 节的比较')],
    'wisdom-root-without-axiom': [('chapter section 6.15', 'chapter section 6.4'), ('章节 §6.15', '章节 §6.4')],
    'wisdom-root': [('(chapter section 6.15;', '(chapter section 6.4;'), ('（章节 §6.15，', '（章节 §6.4，')],
}

NOTE = {
    'en': '20 October 2026, R36 (the chapter, once): the canonical chapter was restructured, its 20 October edition '
          'frozen in theories/becoming/history/THE-THEORY-OF-BECOMING-2026-10-20.md; this record\'s citations of '
          'the old section numbering re-pointed by content ({pairs}). The claim is unchanged.',
    'zh': '2026年10月20日，R36（本章只陈述一次）：规范章节重排，10月20日版冻结于 '
          'theories/becoming/history/THE-THEORY-OF-BECOMING-2026-10-20.md；本记录对旧节号的引用按内容重指（{pairs}）。论断不变。',
}


def replace_live(x, old, new, count):
    if isinstance(x, dict):
        return {k: (v if k in SKIP else replace_live(v, old, new, count)) for k, v in x.items()}
    if isinstance(x, list):
        return [replace_live(v, old, new, count) for v in x]
    if isinstance(x, str) and old in x:
        count[0] += x.count(old)
        return x.replace(old, new)
    return x


def pairs_of(edits):
    import re
    seen = []
    for old, new in edits:
        a, b = re.search(r'6\.\d+', old).group(), re.findall(r'6\.\d+', new)[-1]
        if (a, b) not in seen:
            seen.append((a, b))
    return seen


def main():
    apply = '--apply' in sys.argv
    out = {}
    for rid, edits in EDITS.items():
        p = RECORDS / f'{rid}.json'
        d = json.loads(p.read_text())
        counts = []
        for old, new in edits:
            c = [0]
            d = replace_live(d, old, new, c)
            if not c[0]:
                raise SystemExit(f'{rid}: {old!r} not found in a live field')
            counts.append(c[0])
        pr = pairs_of(edits)
        en = ', '.join(f'section {a} to {b}' for a, b in pr)
        zh = '、'.join(f'§{a} 改为 §{b}' for a, b in pr)
        d['history'] = d.get('history', []) + [{'en': NOTE['en'].format(pairs=en), 'zh': NOTE['zh'].format(pairs=zh)}]
        out[rid] = {'replacements': sum(counts), 'pairs': pr}
        if apply:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print('applied' if apply else 'dry run')


if __name__ == '__main__':
    main()
