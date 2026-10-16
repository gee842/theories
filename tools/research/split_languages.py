#!/usr/bin/env python3
"""Split a hand-written Markdown file that interleaves Chinese and English into two files.

  python3 -B tools/research/split_languages.py FILE --en OUT_EN --zh OUT_ZH [--report REPORT.json]

Deterministic and read-only on FILE. The rules:

- A heading "中文 / English" splits at " / " (either order). Each output gets
  `<a id="ORIGINAL"></a>` before its heading when the heading's original GitHub anchor
  would otherwise be lost, so `FILE#anchor` links still resolve. A heading in one script
  goes to that language; the other output keeps its anchor as a bare `<a id>`.
- Each paragraph, list item, blockquote paragraph or HTML line is classified by script after
  removing inline code, link targets, URLs, Lean names and Chinese quoted inside an English
  sentence: mostly CJK goes to zh, otherwise en. English that only quotes terms such as 生生
  stays en. A unit made of one Chinese half and one English half joined by " / " splits.
- A table cell "zh / en" (or "zh<br>en") splits into its halves. A table whose cells are
  Chinese only goes to zh, and the en output carries `<!-- zh-only table: see NAME.zh.md -->`.
  An English-only table goes to en.
- Code blocks, blank lines, links-only lines, bare HTML tags and front matter go to both;
  bilingual link labels "zh / en" inside them take the matching half.

The report lists zh-only spans: Chinese blocks with no English block of comparable length
in the same section (zh length about 0.36 of English, accepted between 0.12 and 1.2), with
their line numbers. These are what the English file would lack.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.research.reading_catalogue import numbered, slug  # noqa: E402

CJK = re.compile(r'[　-〿㐀-䶿一-鿿豈-﫿＀-￯]')
HAN = re.compile(r'[㐀-䶿一-鿿豈-﫿]')
LATIN = re.compile(r'[A-Za-z]')
FENCE = re.compile(r'^\s*(```|~~~)')
HEADING = re.compile(r'^(#{1,6})\s+(.+?)\s*#*\s*$')
LIST_ITEM = re.compile(r'^(\s*)(?:[-*+]|\d+[.)])\s+')
TABLE_ROW = re.compile(r'^\s*\|')
TABLE_RULE = re.compile(r'^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$')
BARE_HTML = re.compile(r'^\s*(?:<[^>\n]+>\s*)+$')
LINK = re.compile(r'(!?)\[([^\]\n]*)\]\(([^)\n]*)\)')
CODE = re.compile(r'`+[^`\n]*`+')
URL = re.compile(r'<?https?://\S+>?')
# Dotted or underscored identifiers and CamelCase words carry no language.
# So do labels such as G0, P58b or AI.
LEAN = re.compile(r"\b[A-Za-z_][\w']*(?:\.[\w'!?]+)+\b|\b\w*_\w+\b|\b[A-Z][a-z]+(?:[A-Z][a-z0-9]*)+\b|"
                  r"\b[A-Z]{1,2}\d+[a-z]?\b|\b[A-Z]{1,3}\b")
QUOTED = re.compile(r'“[^”\n]*”|「[^」\n]*」|『[^』\n]*』')
SLUG_LABEL = re.compile(r"^[\w./#'-]+$", re.A)
ZH_RATIO, LOW, HIGH = 0.36, 0.12, 1.2


def strip(text: str) -> str:
    """The prose that decides the language: no code, link targets, URLs or Lean names."""
    text = CODE.sub(' ', text)
    text = LINK.sub(lambda m: ' ' if SLUG_LABEL.match(m[2]) else ' ' + m[2] + ' ', text)  # an id or file name as label carries no language
    text = URL.sub(' ', text)
    text = re.sub(r'<[^>\n]*>', ' ', text)
    return LEAN.sub(' ', text)


def counts(text: str) -> tuple[int, int]:
    return len(HAN.findall(text)), len(LATIN.findall(text))


def script(text: str) -> str:
    """'zh', 'en' or 'none' for the prose of `text`."""
    prose = strip(text)
    han, latin = counts(prose)
    if not han and not latin:
        return 'none'
    if han and latin:
        # Words quoted in the other language (Ren's English in a Chinese sentence, 生生 in an
        # English one): decide on the sentence around the quotations, when there is one.
        h2, l2 = counts(QUOTED.sub(' ', prose))
        if h2 * 3 + l2 >= 12:
            han, latin = h2, l2
    # One Han character carries about as much as three Latin letters.
    return 'zh' if han * 3 >= latin else 'en'


SEPARATORS = (re.compile(r' ?/ '), re.compile(r'<br>'))  # "中文 / English", "（注）/ English", "中文<br>English"


def halves(text: str, separators=SEPARATORS) -> tuple[str, str] | None:
    """(zh, en) when `text` is one Chinese half and one English half joined by a separator
    outside code and links; None otherwise."""
    masked = CODE.sub(lambda m: '\0' * len(m[0]), text)
    masked = LINK.sub(lambda m: '\0' * len(m[0]), masked)
    masked = re.sub(r'／', '\0', masked)  # the fullwidth slash is part of Chinese text
    for sep in separators:
        at = [m.span() for m in sep.finditer(masked)]
        if len(at) != 1:
            continue
        left, right = text[:at[0][0]], text[at[0][1]:]
        a, b = script(left), script(right)
        if {a, b} == {'zh', 'en'}:
            return (left, right) if a == 'zh' else (right, left)
    return None


def split_labels(line: str, lang: str) -> str:
    """In a line kept for both, give each bilingual link label its matching half."""
    def label(m):
        h = halves(m[2])
        if not h:
            return m[0]
        return f'{m[1]}[{h[0].strip() if lang == "zh" else h[1].strip()}]({m[3]})'
    return LINK.sub(label, line)


def links_only(text: str) -> bool:
    rest = LINK.sub(' ', CODE.sub(' ', text))
    rest = re.sub(r'<[^>\n]*>', ' ', rest)
    return bool(LINK.search(text)) and not re.search(r'[A-Za-z㐀-鿿]', re.sub(r'^\s*(?:[-*+]|\d+[.)])\s+', '', rest))


def split_cell(cell: str) -> tuple[str, str, str]:
    """(zh, en, kind) for one table cell; kind is 'pair', 'zh', 'en' or 'none'."""
    h = halves(cell.strip())
    if h:
        return ' ' + h[0].strip() + ' ', ' ' + h[1].strip() + ' ', 'pair'
    kind = script(cell)
    return cell, cell, kind


def cells(row: str) -> list[str]:
    body = row.strip()
    if body.startswith('|'):
        body = body[1:]
    if body.endswith('|') and not body.endswith('\\|'):
        body = body[:-1]
    out, current, i = [], '', 0
    while i < len(body):
        c = body[i]
        if c == '\\' and i + 1 < len(body):
            current += body[i:i + 2]
            i += 2
            continue
        if c == '`':
            j = body.find('`', i + 1)
            if j > 0:
                current += body[i:j + 1]
                i = j + 1
                continue
        if c == '|':
            out.append(current)
            current = ''
        else:
            current += c
        i += 1
    out.append(current)
    return out


class Splitter:
    def __init__(self, text: str, name: str):
        self.lines = text.split('\n')
        self.name = name
        self.en: list[str] = []
        self.zh: list[str] = []
        self.blocks: list[dict] = []  # classified prose blocks, for the report
        self.misclassified_candidates: list[dict] = []
        self.section = '(before the first heading)'
        self.tables = {'split': 0, 'zh_only': 0, 'en_only': 0, 'mixed': 0}
        headings = [HEADING.match(l)[2] for l in self.heading_lines()]
        self.original_anchors = iter(numbered([slug(h) for h in headings]))
        self.en_slugs: list[str] = []
        self.zh_slugs: list[str] = []

    def heading_lines(self):
        fence = None
        for line in self.lines:
            m = FENCE.match(line)
            if m:
                fence = None if fence == m[1] else (fence or m[1])
                continue
            if fence is None and HEADING.match(line):
                yield line

    def both(self, line: str):
        self.en.append(split_labels(line, 'en'))
        self.zh.append(split_labels(line, 'zh'))

    def emit(self, lang: str, lines: list[str], start: int, kind: str):
        target = self.zh if lang == 'zh' else self.en
        target.extend(lines)
        text = '\n'.join(lines)
        self.blocks.append({'lang': lang, 'start': start + 1, 'end': start + len(lines), 'section': self.section,
                            'kind': kind, 'chars': len(re.sub(r'\s+', ' ', strip(text)).strip()), 'text': text})

    def unit(self, lines: list[str], start: int, kind: str):
        """A paragraph, list item or blockquote paragraph."""
        text = '\n'.join(lines)
        if links_only(text) or BARE_HTML.match(text) and not re.search(r'>[^<\s][^<]*<', text):
            for line in lines:
                self.both(line)
            return
        h = halves(text) if len(lines) == 1 else None
        if h:
            prefix = re.match(r'^(\s*(?:[-*+]|\d+[.)]|>)?\s*)', text)[1]
            zh, en = h
            zh = zh if zh.startswith(prefix) else prefix + zh.lstrip()
            en = en if en.startswith(prefix) else prefix + en.lstrip()
            self.emit('zh', [zh.rstrip()], start, kind + '-half')
            self.emit('en', [en.rstrip()], start, kind + '-half')
            return
        lang = script(text)
        if lang == 'none':
            for line in lines:
                self.both(line)
            return
        han, latin = counts(strip(text))
        if han and latin and 0.15 < (han * 3) / (han * 3 + latin) < 0.85:
            self.misclassified_candidates.append({'line': start + 1, 'assigned': lang, 'han': han, 'latin': latin,
                                                  'text': text[:200]})
        self.emit(lang, lines, start, kind)

    def heading(self, line: str, index: int):
        marks, title = HEADING.match(line)[1], HEADING.match(line)[2]
        original = next(self.original_anchors)
        self.section = title
        h = halves(title)
        if h:
            zh_title, en_title = h[0].strip(), h[1].strip()
            number = re.match(r'(?:§\s?)?\d+(?:\.\d+)*\.?\s+', title)  # "6.1 中文 / English": both keep 6.1
            if number:
                zh_title = zh_title if zh_title.startswith(number[0]) else number[0] + zh_title
                en_title = en_title if en_title.startswith(number[0]) else number[0] + en_title
        else:
            lang = script(title)
            zh_title = title if lang in ('zh', 'none') else None
            en_title = title if lang in ('en', 'none') else None
        for out, slugs, text in ((self.en, self.en_slugs, en_title), (self.zh, self.zh_slugs, zh_title)):
            if text is None:
                out.append(f'<a id="{original}"></a>')
                continue
            own = numbered(slugs + [slug(text)])[-1]
            slugs.append(slug(text))
            if own != original:
                out.append(f'<a id="{original}"></a>')
            out.append(f'{marks} {text}')
        if not h and zh_title is not None and en_title is None:
            self.blocks.append({'lang': 'zh', 'start': index + 1, 'end': index + 1, 'section': title, 'kind': 'heading',
                                'chars': len(strip(title).strip()), 'text': line})

    def table(self, rows: list[str], start: int):
        """Split cells "zh / en"; a table with Chinese cells and no English cell is Chinese (its
        bilingual labels take their Chinese half); in a table with both, the English output drops
        a column headed in Chinese only whose cells are Chinese, and keeps other Chinese cells."""
        grid = [None if TABLE_RULE.match(row) else [split_cell(c) for c in cells(row)] for row in rows]
        kinds = [k for parts in grid if parts for _, _, k in parts]
        has_pair, has_zh, has_en = 'pair' in kinds, 'zh' in kinds, 'en' in kinds
        stem = Path(self.name).stem

        def render(lang, keep=None):
            out = []
            for row, parts in zip(rows, grid):
                columns = range(len(parts)) if parts else range(row.count('|') - 1)
                keep_ = [c for c in columns if keep is None or c in keep]
                if parts is None:
                    rule = cells(row)
                    out.append('|' + '|'.join(rule[c] for c in keep_ if c < len(rule)) + '|')
                else:
                    out.append('|' + '|'.join((parts[c][0] if lang == 'zh' else parts[c][1]) for c in keep_ if c < len(parts)) + '|')
            return out

        def block(lang, kind, chars, text):
            self.blocks.append({'lang': lang, 'start': start + 1, 'end': start + len(rows), 'section': self.section,
                                'kind': kind, 'chars': chars, 'text': text})

        if has_zh and not has_en:
            self.tables['zh_only'] += 1
            self.zh.extend(render('zh') if has_pair else rows)
            self.en.append(f'<!-- zh-only table: see {stem}.zh.md -->')
            block('zh', 'table', sum(len(strip(r).strip()) for r in rows), '\n'.join(rows))
        elif has_en and not has_zh and not has_pair:
            self.tables['en_only'] += 1
            self.en.extend(rows)
        elif not has_zh:
            self.tables['split'] += 1
            self.zh.extend(render('zh'))
            self.en.extend(render('en'))
        else:
            self.tables['mixed'] += 1
            body = [parts for parts in grid[1:] if parts]
            header = grid[0] or []
            width = max(len(parts) for parts in grid if parts)
            def column(c):
                return [parts[c][2] for parts in body if c < len(parts)]
            drop = {c for c in range(width) if c < len(header) and header[c][2] == 'zh'
                    and all(k in ('zh', 'none') for k in column(c))}
            keep = [c for c in range(width) if c not in drop]
            self.zh.extend(render('zh'))
            self.en.extend(render('en', set(keep)))
            left = [(parts[c][1]) for parts in body for c in keep if c < len(parts) and parts[c][2] == 'zh']
            if left:  # Chinese cells the English table keeps as they are
                block('zh', 'table-cells', sum(len(strip(x).strip()) for x in left),
                      f'{len(left)} Chinese-only cells kept in the English table\n' + '\n'.join(x.strip() for x in left))

    def run(self):
        lines, i, n = self.lines, 0, len(self.lines)
        if lines and lines[0].strip() == '---':
            j = next((k for k in range(1, n) if lines[k].strip() == '---'), None)
            if j is not None:
                for line in lines[:j + 1]:
                    self.both(line)
                i = j + 1
        while i < n:
            line = lines[i]
            m = FENCE.match(line)
            if m:
                j = i + 1
                while j < n and not lines[j].lstrip().startswith(m[1]):
                    j += 1
                for k in range(i, min(j + 1, n)):
                    self.both(lines[k])
                i = j + 1
                continue
            if not line.strip():
                self.both(line)
                i += 1
                continue
            if HEADING.match(line):
                self.heading(line, i)
                i += 1
                continue
            if TABLE_ROW.match(line):
                j = i
                while j < n and TABLE_ROW.match(lines[j]):
                    j += 1
                self.table(lines[i:j], i)
                i = j
                continue
            if BARE_HTML.match(line) and not re.search(r'>[^<\s][^<]*<', line):
                self.both(line)
                i += 1
                continue
            if line.lstrip().startswith('>'):
                j = i
                while j < n and lines[j].lstrip().startswith('>') and lines[j].strip() not in ('>',):
                    j += 1
                if j == i:  # a bare '>' separating quoted paragraphs
                    self.both(line)
                    i += 1
                    continue
                self.unit(lines[i:j], i, 'quote')
                i = j
                continue
            m = LIST_ITEM.match(line)
            if m:
                indent = len(m[1])
                j = i + 1
                while j < n and lines[j].strip() and not LIST_ITEM.match(lines[j]) and not HEADING.match(lines[j]) \
                        and not TABLE_ROW.match(lines[j]) and len(lines[j]) - len(lines[j].lstrip()) > indent:
                    j += 1
                self.unit(lines[i:j], i, 'list-item')
                i = j
                continue
            j = i + 1
            while j < n and lines[j].strip() and not HEADING.match(lines[j]) and not LIST_ITEM.match(lines[j]) \
                    and not TABLE_ROW.match(lines[j]) and not FENCE.match(lines[j]) and not lines[j].lstrip().startswith('>'):
                j += 1
            self.unit(lines[i:j], i, 'paragraph')
            i = j
        return self

    def zh_only_spans(self):
        """Chinese blocks with no English block of comparable length in the same section."""
        spans = []
        sections: dict[str, list[dict]] = {}
        for b in self.blocks:
            sections.setdefault(b['section'], []).append(b)
        for name, blocks in sections.items():
            english = [b for b in blocks if b['lang'] == 'en' and b['chars']]
            used = set()
            for b in blocks:
                if b['lang'] != 'zh' or not b['chars']:
                    continue
                candidates = [(abs(e['start'] - b['start']), k) for k, e in enumerate(english) if k not in used
                              and LOW <= b['chars'] / max(e['chars'], 1) <= HIGH]
                if b['kind'] != 'table' and candidates:
                    used.add(min(candidates)[1])
                    continue
                if b['kind'] == 'heading':
                    continue
                spans.append({'section': name, 'start': b['start'], 'end': b['end'], 'kind': b['kind'],
                              'chars': b['chars'], 'bytes': len(b['text'].encode()), 'first_line': b['text'].split('\n')[0][:160]})
        return spans

    def report(self, en_path, zh_path):
        spans = self.zh_only_spans()
        by_section: dict[str, dict] = {}
        for s in spans:
            entry = by_section.setdefault(s['section'], {'spans': 0, 'bytes': 0, 'chars': 0})
            entry['spans'] += 1
            entry['bytes'] += s['bytes']
            entry['chars'] += s['chars']
        en_text, zh_text = '\n'.join(self.en), '\n'.join(self.zh)
        return {'source': self.name, 'source_bytes': len('\n'.join(self.lines).encode()),
                'en': {'path': str(en_path), 'bytes': len(en_text.encode()), 'lines': len(self.en)},
                'zh': {'path': str(zh_path), 'bytes': len(zh_text.encode()), 'lines': len(self.zh)},
                'tables': self.tables,
                'zh_only': {'spans': len(spans), 'bytes': sum(s['bytes'] for s in spans), 'by_section': by_section, 'list': spans},
                'mixed_script_units': self.misclassified_candidates,
                'rule': 'zh-only: a Chinese block with no English block in the same section whose length is comparable '
                        f'(zh/en prose length between {LOW} and {HIGH}); a Chinese-only table counts in full.'}


def tidy(lines: list[str]) -> list[str]:
    """Collapse the runs of blank lines a removed block leaves, outside code blocks."""
    out, fence = [], None
    for line in lines:
        m = FENCE.match(line)
        if m:
            fence = None if fence == m[1] else (fence or m[1])
        if fence is None and not m and not line.strip() and (not out or not out[-1].strip()):
            continue
        out.append(line)
    return out


def split(text: str, name: str) -> Splitter:
    s = Splitter(text, name).run()
    s.en, s.zh = tidy(s.en), tidy(s.zh)
    return s


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file')
    parser.add_argument('--en', required=True)
    parser.add_argument('--zh', required=True)
    parser.add_argument('--report')
    args = parser.parse_args(argv)
    source = Path(args.file)
    outputs = [Path(args.en).resolve(), Path(args.zh).resolve()] + ([Path(args.report).resolve()] if args.report else [])
    if source.resolve() in outputs:
        parser.error('an output path is the input file')
    s = split(source.read_text(), source.name)
    Path(args.en).write_text('\n'.join(s.en))
    Path(args.zh).write_text('\n'.join(s.zh))
    report = s.report(args.en, args.zh)
    if args.report:
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    summary = {k: v for k, v in report.items() if k not in ('zh_only', 'mixed_script_units')}
    summary['zh_only'] = {k: v for k, v in report['zh_only'].items() if k != 'list'}
    summary['mixed_script_units'] = len(report['mixed_script_units'])
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
