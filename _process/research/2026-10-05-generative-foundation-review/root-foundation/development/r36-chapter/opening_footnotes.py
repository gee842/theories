"""R36: point OPENING's footnotes (AI-written) at the restructured chapter; the body, in Ren's voice, is not
touched (every link to the chapter is in a footnote; the old anchors stay as aliases). Without --apply, a dry run."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
P = ROOT / 'theories/becoming/OPENING.md'
C = 'chapters/THE-THEORY-OF-BECOMING.md#'
REPL = [
    ('[section 6.15](' + C + '615-若任何东西的延续都有意义--if-the-continuation-of-anything-has-significance)',
     '[section 6.4](' + C + '64-the-continuation-condition)'),
    ('[section 6.8](' + C + '68-一条公理推出什么p39-what-the-one-axiom-yields-p39)',
     '[section 6.4](' + C + '64-the-continuation-condition)'),
    ('[section 6.11](' + C + '611-the-condition-decomposed-the-selfs-presupposition-and-the-step-of-invariance)',
     '[section 6.5](' + C + '65-scope-and-order-the-step-of-invariance-c-and-practical-judgment)'),
    ('[the theory stated whole](' + C + '第一部分的总陈述--part-i-stated-whole)', '[the theorem map](' + C + 'the-theorem-map)'),
    (C + '4-集体动力学--collective-dynamics)', C + '4-collective-dynamics)'),
    (C + '0-前提卡--premise-card)', C + '0-premise-card)'),
    (C + '7-ai-对齐--ai-alignment)', C + '7-ai-alignment)'),
    (C + '8-开放纲领--open-programme)', C + '8-open-programme)'),
    (C + '9-形式脊柱--the-formal-spine)', C + '9-the-formal-spine)'),
]


def main():
    lines = P.read_text().split('\n')
    counts = {}
    for i, line in enumerate(lines):
        for old, new in REPL:
            if old in line:
                if not line.startswith('[^'):
                    raise SystemExit(f'line {i + 1}: a chapter link outside the footnotes; leave the body to a proposal')
                counts[old[:60]] = counts.get(old[:60], 0) + line.count(old)
                line = line.replace(old, new)
        lines[i] = line
    print(counts, sum(counts.values()))
    if '--apply' in sys.argv:
        P.write_text('\n'.join(lines))
        print('applied')


if __name__ == '__main__':
    main()
