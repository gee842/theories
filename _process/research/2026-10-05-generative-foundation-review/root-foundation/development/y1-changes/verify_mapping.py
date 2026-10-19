#!/usr/bin/env python3
"""Check Y1's mapping of the 周易 and the 易传 onto the spine. usage, from anywhere:
  python3 -B verify_mapping.py [--receipt PATH] [--chapter PATH]   # check, exit 1 on any failure
  python3 -B verify_mapping.py --table                             # print the chapter's passage table

Checks, each against the repository's own files:
  1. every preserved page in sources/zhouyi-yizhuan/ has the bytes and the wikitext its
     PROVENANCE.json binds by SHA-256;
  2. every fragment of passages.json occurs verbatim in the wikitext of its page, read with
     Wikisource's markup removed (character-variant markup -{…}-, links, templates, tags);
  3. every declaration a passage names is in the audited declaration list of a core receipt
     (default: the newest under becoming-checks/); names of Becoming.Hexagrams not yet in that
     receipt are checked against the module's source and reported as such;
  4. the received order of Hexagrams.lean is the order of the preserved pages: page n is the
     n-th hexagram (第n卦), follows page n-1 by its link, and its trigram line (X下Y上) gives
     the six lines of the n-th entry of `order`;
  5. the names the chapter gives to configurations are right: `rising k` and `falling k` are
     the lines of 坤 復 臨 泰 大壯 夬 乾 and 乾 姤 遯 否 觀 剝 坤, `sui` is 隨, and the law of
     waxing and waning carries 隨 → 中孚 → 蠱 → 小過 → 隨 and 乾 → 姤 → … → 坤 → 復 → … → 乾;
  6. the chapter's passage table, between its two markers, is the table printed by --table.
It checks text and names, not the proofs: the core checker proves the declarations."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT / 'sources/zhouyi-yizhuan'
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = ROOT / 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
BEGIN, END = '<!-- passage-map:begin -->', '<!-- passage-map:end -->'
KIND_ZH = {'agreement': '相合', 'scope': '定域', 'divergence': '相分'}
TRIGRAM = {'乾': (1, 1, 1), '兌': (1, 1, 0), '離': (1, 0, 1), '震': (1, 0, 0),
           '巽': (0, 1, 1), '坎': (0, 1, 0), '艮': (0, 0, 1), '坤': (0, 0, 0)}
NUMERAL = '〇一二三四五六七八九'


def chinese_number(n):
    tens, ones = divmod(n, 10)
    return ((NUMERAL[tens] if tens > 1 else '') + ('十' if tens else '') + (NUMERAL[ones] if ones else '')) or '〇'


def page(rel):
    data = json.loads((SRC / rel).read_text())
    return data['query']['pages'][0] if 'query' in data else data


def wikitext(rel):
    return page(rel)['revisions'][0]['slots']['main']['content']


def clean(text):
    text = re.sub(r'-\{(?:[A-Za-z]\|)?|\}-', '', text)                 # character-variant markup
    text = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', text)        # links: the shown text
    text = re.sub(r'\{\{另\|([^|}]*)\|[^}]*\}\}', r'\1', text)           # variant readings: the first
    text = re.sub(r'\{\{[^{}]*\}\}', '', text)                           # other templates
    return re.sub(r'<[^>]+>', '', text)                                  # tags


def table(passages):
    rows = ['| 经文 | 出处 | 关系 | 脊柱上的声明 | 读法（AI） |', '|---|---|---|---|---|']
    for p in passages:
        text = '……'.join(f'「{f}」' for f in p['fragments'])
        decls = '<br>'.join(f"`{d.removeprefix('Becoming.')}`" for d in p['declarations'])
        rows.append(f"| <a id=\"p-{p['id']}\"></a>{text} | {p['locator']} | {KIND_ZH[p['kind']]} | {decls} | {p['reading']} |")
    return '\n'.join(rows)


def lean_declarations(path):
    """Full names of the declarations of one Lean file, by its namespaces."""
    names, stack = set(), []
    for line in path.read_text().splitlines():
        m = re.match(r'namespace\s+(\S+)', line)
        if m:
            stack.append(m.group(1))
            continue
        m = re.match(r'end\s+(\S+)', line)
        if m and stack and stack[-1] == m.group(1):
            stack.pop()
            continue
        m = re.match(r'(?:protected\s+|private\s+|noncomputable\s+)*(theorem|def|structure|inductive|abbrev|instance|lemma)\s+([^\s:({\[]+)', line)
        if m:
            names.add('.'.join(stack + [m.group(2)]))
    return names


def order_literal(path):
    text = path.read_text()
    body = text[text.index('def order : List Hexagram := ['):]
    body = body[:body.index('\n  ]')] if '\n  ]' in body else body[:body.index(']\n')]
    return [tuple(1 if v == 'true' else 0 for v in m.group(1).split(', '))
            for m in re.finditer(r'⟨((?:true|false)(?:, (?:true|false)){5})⟩', body)]


def def_table(path, name):
    text = path.read_text()
    block = text[text.index(f'def {name} : Nat → Hexagram'):]
    block = block[:block.index('\n\n')]
    out = {}
    for m in re.finditer(r'\| (\d+|_) => ⟨((?:true|false)(?:, (?:true|false)){5})⟩', block):
        out[m.group(1)] = tuple(1 if v == 'true' else 0 for v in m.group(2).split(', '))
    return out


def variant(name):
    """One form of the two names Wikisource writes either way (恆/恒, 遯/遁)."""
    return name.replace('恆', '恒').replace('遯', '遁')


def wax_wane(s):
    a, b, c, d, e, f = s
    return (1 - f, a, b, c, d, e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--receipt', type=Path)
    ap.add_argument('--chapter', type=Path, default=CHAPTER)
    ap.add_argument('--table', action='store_true')
    args = ap.parse_args()
    passages = json.loads((HERE / 'passages.json').read_text())['passages']
    if args.table:
        print(table(passages))
        return 0
    failures = []

    # 1. preserved bytes
    prov = json.loads((SRC / 'PROVENANCE.json').read_text())
    for f in prov['files']:
        raw = (SRC / f['file']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != f['sha256']:
            failures.append(f"bytes changed: {f['file']}")
        pg = page(f['file'])
        rev = pg['revisions'][0]
        if rev['revid'] != f['revid'] or pg['title'] != f['title']:
            failures.append(f"revision differs: {f['file']}")
        if hashlib.sha256(rev['slots']['main']['content'].encode()).hexdigest() != f['wikitext_sha256']:
            failures.append(f"wikitext changed: {f['file']}")
    bound = {f['file'] for f in prov['files']}

    # 2. fragments verbatim
    ids = set()
    for p in passages:
        if p['id'] in ids:
            failures.append(f"passage id repeated: {p['id']}")
        ids.add(p['id'])
        if p['source'] not in bound:
            failures.append(f"{p['id']}: source not bound by the provenance: {p['source']}")
            continue
        text = clean(wikitext(p['source']))
        for frag in p['fragments']:
            if frag not in text:
                failures.append(f"{p['id']}: not verbatim in {p['source']}: {frag}")
        if p['kind'] not in KIND_ZH or not p['declarations']:
            failures.append(f"{p['id']}: kind or declarations missing")

    # 3. declarations
    checks = PKG / 'becoming-checks'
    receipt = args.receipt or max(checks.glob('*/verification.json'))
    audited = {d['name'] for m in json.loads(receipt.read_text())['modules'] for d in m['declarations']}
    module = PKG / 'Becoming/Hexagrams.lean'
    if not module.exists():
        module = HERE / 'Becoming/Hexagrams.lean'
    from_source = lean_declarations(module)
    by_source = set()
    for p in passages:
        for d in p['declarations']:
            if d in audited:
                continue
            if d.startswith('Becoming.Hexagram') and d in from_source:
                by_source.add(d)
            else:
                failures.append(f"{p['id']}: no such audited declaration: {d}")

    # 4. the received order
    order = order_literal(module)
    if len(order) != 64:
        failures.append(f'order literal has {len(order)} entries')
    names = []
    previous = None
    for n in range(1, 65):
        pg = page(f'hexagrams/{n:02d}.json')
        title = clean(pg['title'])
        name = title.split('/', 1)[1]
        names.append(name)
        text = clean(wikitext(f'hexagrams/{n:02d}.json'))
        if f'第{chinese_number(n)}卦' not in text:
            failures.append(f'page {n} ({title}) is not marked 第{chinese_number(n)}卦')
        tri = re.search(r'(\S)下(\S)上', text)
        lines = TRIGRAM[tri.group(1)] + TRIGRAM[tri.group(2)]
        if n <= len(order) and order[n - 1] != lines:
            failures.append(f'order entry {n} is not {name} ({tri.group(0)})')
        if previous is not None:
            link = re.search(r'\|\s*next\s*=\s*\[\[\.\./([^|\]]+)', clean_links_kept(previous))
            if not link or variant(re.sub(r'-\{|\}-', '', link.group(1)).strip()) != variant(name):
                failures.append(f'page {n - 1} does not link to {name}')
        previous = wikitext(f'hexagrams/{n:02d}.json')
    named = {lines: names[i] for i, lines in enumerate(order)}

    # 5. named configurations and orbits
    rising, falling = def_table(module, 'rising'), def_table(module, 'falling')
    want_r, want_f = '坤 復 臨 泰 大壯 夬 乾'.split(), '乾 姤 遯 否 觀 剝 坤'.split()
    for k in range(7):
        key = str(k) if k < 6 else '_'
        if named.get(rising[key]) != want_r[k]:
            failures.append(f'rising {k} is not {want_r[k]}')
        if named.get(falling[key]) != want_f[k]:
            failures.append(f'falling {k} is not {want_f[k]}')
    sui = re.search(r'def sui : Hexagram := ⟨([^⟩]*)⟩', module.read_text()).group(1)
    sui = tuple(1 if v == 'true' else 0 for v in sui.split(', '))
    cycle, s = [], sui
    for _ in range(4):
        cycle.append(named[s])
        s = wax_wane(s)
    if cycle != ['隨', '中孚', '蠱', '小過'] or s != sui:
        failures.append(f'the orbit of 隨 is {cycle}')
    s, orbit = (1,) * 6, []
    for _ in range(12):
        orbit.append(named[s])
        s = wax_wane(s)
    if orbit != want_f + want_r[1:6] or s != (1,) * 6:
        failures.append(f'the orbit of 乾 is {orbit}')

    # 6. the chapter table
    if args.chapter.exists():
        text = args.chapter.read_text()
        if BEGIN not in text or END not in text:
            failures.append('chapter has no passage-map markers')
        else:
            got = text[text.index(BEGIN) + len(BEGIN):text.index(END)].strip()
            if got != table(passages):
                failures.append('chapter table differs from passages.json (print it with --table)')
    else:
        failures.append(f'no chapter at {args.chapter}')

    kinds = {k: sum(p['kind'] == k for p in passages) for k in KIND_ZH}
    decls = {d for p in passages for d in p['declarations']}
    print(f"{len(passages)} passages ({kinds['agreement']} agreement, {kinds['scope']} scope, "
          f"{kinds['divergence']} divergence), {sum(len(p['fragments']) for p in passages)} fragments, "
          f"{len(decls)} declarations; receipt {receipt.parent.name}"
          + (f'; {len(by_source)} Hexagrams names checked against the module source, not yet in the receipt' if by_source else ''))
    print('order: 64 pages, trigrams and links agree' if not any('order' in f or 'page' in f for f in failures) else '')
    for f in failures:
        print('FAIL', f)
    return 1 if failures else 0


def clean_links_kept(text):
    return re.sub(r'-\{(?:[A-Za-z]\|)?|\}-', '', text)


if __name__ == '__main__':
    sys.exit(main())
