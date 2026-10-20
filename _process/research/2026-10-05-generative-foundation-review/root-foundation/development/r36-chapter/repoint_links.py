"""R36: point links to the canonical chapter at its live headings.

Every old anchor stays in the restructured chapter as an alias (`<a id>`) before the heading that now holds
its content, so old links resolve; this re-points the links of live, hand-written files to that heading's own
slug and, where the link text names the old section number, to the new number. Generated pages, Ren's own
texts (OPENING's body, the generativity chain), AGENTS.md, sources, history and dated study sections are not
touched. Without --apply, a dry run.

Usage: python3 -B repoint_links.py [--apply] FILE ...
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
sys.path[:0] = [str(ROOT)]
from tools.research import moves  # noqa: E402

CHAPTER = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
ALIAS = re.compile(r'<a id="([^"]+)"')
LINK = re.compile(r'\[([^\]]*)\]\(((?:[^)\s]*/)?THE-THEORY-OF-BECOMING\.md)#([^)\s]+)\)')


def live_map():
    """anchor -> (live slug, section number of that heading or None)"""
    pending, out, live = [], {}, {}
    seen = {}
    for line in CHAPTER.read_text().split('\n'):
        pending += ALIAS.findall(line)
        m = HEADING.match(line)
        if m:
            slug = moves.github_slug(m.group(2))
            if slug in seen:
                seen[slug] += 1
                slug = f'{slug}-{seen[slug]}'
            else:
                seen[slug] = 0
            num = re.match(r'(\d+(?:\.\d+)?)\.?\s', m.group(2))
            num = num.group(1) if num else None
            live[slug] = num
            out[slug] = (slug, num)
            for a in pending:
                out.setdefault(a, (slug, num))
            pending = []
    return out, live


def old_number(anchor):
    m = re.match(r'(\d+)-', anchor)
    if not m:
        return None
    d = m.group(1)
    return d if len(d) == 1 or d in ('10', '11') else d[0] + '.' + d[1:]


def main():
    apply = '--apply' in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith('--')]
    amap, live = live_map()
    total = 0
    for f in files:
        p = ROOT / f
        text = p.read_text()
        changes = []

        def sub(m):
            label, path, anchor = m.groups()
            if anchor in live:
                return m.group(0)
            if anchor not in amap:
                changes.append(('UNRESOLVED', anchor))
                return m.group(0)
            slug, num = amap[anchor]
            old = old_number(anchor)
            if old and num and old != num:
                label = re.sub(r'(?<![\d.])' + re.escape(old) + r'(?![\d])', num, label)
            changes.append((anchor[:50], slug, m.group(1), label))
            return f'[{label}]({path}#{slug})'

        new = LINK.sub(sub, text)
        # the same anchors in JSON or Python sources ("path": "...md#anchor")
        def sub_plain(m):
            anchor = m.group(2)
            if anchor in live or anchor not in amap:
                return m.group(0)
            changes.append((anchor[:50], amap[anchor][0]))
            return m.group(1) + amap[anchor][0]
        if not f.endswith('.md'):
            new = re.sub(r'(THE-THEORY-OF-BECOMING\.md#)([^)\s"\']+)', sub_plain, new)
        for c in changes:
            print(f, *c, sep=' | ')
        total += len(changes)
        if apply and new != text:
            p.write_text(new)
    print('changes', total, 'applied' if apply else 'dry run')


if __name__ == '__main__':
    main()
