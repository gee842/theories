#!/usr/bin/env python3
"""Check the map of the Chinese sources onto the spine (board item RO). usage, from anywhere:
  python3 -B verify_ro.py [--receipt PATH] [--chapter PATH]   # check, exit 1 on any failure
  python3 -B verify_ro.py --table                             # print the chapter's passage tables
  python3 -B verify_ro.py --excerpt                           # rebuild atlas-excerpt.json from the packages

Checks, each against the repository's own files:
  1. every file preserved in sources/chinese-classical-texts/ has the SHA-256 its PROVENANCE.json
     binds, and every file there is bound;
  2. every fragment of passages.json occurs verbatim in the preserved text it names (a Wikisource
     page is read with its markup removed, as in the Y1 check);
  3. every atlas id a passage cites is in atlas-excerpt.json, whose entries are read from the two
     atlases' archives at the SHA-256 the provenance binds; where the archives are present in the
     external store the provenance names, the excerpt is rebuilt from them and must agree;
  4. every declaration a passage names is in the audited declaration list of a core receipt
     (default: the newest under becoming-checks/), or, for a module of this kit not yet landed, in
     its source, reported as such;
  5. every record a passage names exists, and no passage id repeats one of the Y1 passage map;
  6. the chapter's passage tables, between their markers, are the tables printed by --table.
It checks text and names, not the proofs: the core checker proves the declarations."""
import argparse
import hashlib
import html
import json
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT / 'sources/chinese-classical-texts'
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RECORDS = ROOT / 'theories/becoming/results/records'
CHAPTER = ROOT / 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
Y1 = HERE.parent / 'y1-changes/passages.json'
KIND_ZH = {'agreement': '相合', 'scope': '定域', 'divergence': '相分'}
TRADITIONS = ['易传', '老子', '庄子与玄学', '儒家', '文字', '墨家与名家', '兵家、法家与轻重纵横', '佛教', '其他']


def begin(tradition):
    return f'<!-- passage-map:{tradition}:begin -->'


def end(tradition):
    return f'<!-- passage-map:{tradition}:end -->'


def clean(text):
    """Wikitext with its markup removed: character-variant markup, links (their shown text),
    the text templates of the 說文 and 禮記正義 pages ({{yw|…}} and {{+|…}}: their content),
    variant readings (the first), other templates and tags; character references are decoded."""
    text = html.unescape(text)
    text = re.sub(r'\{\{(?:yw|\+)\|([^{}]*)\}\}', r'\1', text)
    text = re.sub(r'-\{(?:[A-Za-z]\|)?|\}-', '', text)
    text = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', text)
    text = re.sub(r'\{\{另\|([^|}]*)\|[^}]*\}\}', r'\1', text)
    text = re.sub(r'\{\{[^{}]*\}\}', '', text)
    return re.sub(r'<[^>]+>', '', text)


def read_text(rel):
    """The text of a preserved file: a .txt as stored; a Wikisource page object or API response
    as its wikitext with the markup removed."""
    path = SRC / rel
    if path.suffix == '.txt':
        return path.read_text()
    data = json.loads(path.read_text())
    page = data['query']['pages'][0] if 'query' in data else data
    return clean(page['revisions'][0]['slots']['main']['content'])


def lean_declarations(text):
    names, stack = set(), []
    for line in text.splitlines():
        m = re.match(r'namespace\s+(\S+)', line)
        if m:
            stack.append(m.group(1))
            continue
        m = re.match(r'end\s+(\S+)', line)
        if m and stack and stack[-1] == m.group(1):
            stack.pop()
            continue
        m = re.match(r'(?:@\[[^\]]*\]\s*)?(?:protected\s+|private\s+|noncomputable\s+)*'
                     r'(theorem|def|structure|inductive|abbrev|instance|lemma)\s+([^\s:({\[]+)', line)
        if m:
            names.add('.'.join(stack + [m.group(2)]))
    return names


def table(passages, tradition):
    rows = ['| 原文 | 出处 | 关系 | 脊柱上的声明与记录 | 读法（AI） |', '|---|---|---|---|---|']
    for p in passages:
        if p['tradition'] != tradition:
            continue
        text = '……'.join(f'「{f}」' for f in p['fragments'])
        decls = '<br>'.join(f"`{d.removeprefix('Becoming.')}`" for d in p['declarations'])
        recs = '<br>'.join(f"[{r}](../results/records/{r}.md)" for r in p.get('records', []))
        cell = decls + ('<br>' if decls and recs else '') + recs
        rows.append(f"| <a id=\"p-{p['id']}\"></a>{text} | {p['locator']} | {KIND_ZH[p['kind']]} | {cell} | {p['reading']} |")
    return '\n'.join(rows)


def excerpt_from_packages(prov):
    """The cited atlas records, read from the two packages (zip archives in the external store the
    provenance names, each checked against its SHA-256); None where an archive is absent."""
    out = {}
    for atlas in prov['atlases']:
        path = Path(atlas['zip_path'])
        if not path.exists():
            return None
        if hashlib.sha256(path.read_bytes()).hexdigest() != atlas['zip_sha256']:
            raise SystemExit(f"{atlas['id']}: the archive differs from the bound SHA-256")
        with zipfile.ZipFile(path) as zf:
            def read(name, zf=zf, prefix=atlas['prefix']):
                return zf.read(prefix + name).decode()
            out[atlas['id']] = load_atlas(atlas['id'], read)
    return out


def load_atlas(atlas_id, read):
    """Every record of an atlas that an id can cite: id -> (kind, evidence quotes)."""
    records = {}

    def quotes(r):
        out = [x['quote'] for x in r.get('evidence', []) if isinstance(x, dict) and x.get('quote')]
        return out + ([r['quote']] if isinstance(r.get('quote'), str) and r['quote'] else [])
    if atlas_id == 'yidao-v1.3':
        model = json.loads(read('data/model.json'))
        for kind, value in model.items():
            if isinstance(value, list):
                for r in value:
                    if isinstance(r, dict) and isinstance(r.get('id'), str):
                        records[r['id']] = (kind, quotes(r))
    else:
        def jl(name):
            return [json.loads(line) for line in read('data/' + name).splitlines() if line.strip()]
        for c in jl('concepts.jsonl'):
            for s in c['senses']:
                records[s['sense_id']] = ('sense', quotes(s))
        for name in ('expressions.jsonl', 'knowledge_nodes.jsonl', 'knowledge_relations.jsonl',
                     'comparisons.jsonl', 'relations.jsonl'):
            for r in jl(name):
                if isinstance(r.get('id'), str):
                    records.setdefault(r['id'], (name.split('.')[0], quotes(r)))
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--receipt', type=Path)
    ap.add_argument('--chapter', type=Path, default=CHAPTER)
    ap.add_argument('--table', action='store_true')
    ap.add_argument('--excerpt', action='store_true')
    args = ap.parse_args()
    data = json.loads((HERE / 'passages.json').read_text())
    passages = data['passages']
    if args.table:
        for t in TRADITIONS:
            if any(p['tradition'] == t for p in passages):
                print(f'### {t}\n\n{begin(t)}\n{table(passages, t)}\n{end(t)}\n')
        return 0
    prov = json.loads((SRC / 'PROVENANCE.json').read_text())
    cited = {(a['atlas'], a['id']) for p in passages for a in p.get('atlas_ids', [])}
    if args.excerpt:
        full = excerpt_from_packages(prov)
        if full is None:
            raise SystemExit('a package named in the provenance is not present')
        excerpt = {'about': 'The atlas records the passage map cites, read from the packages the '
                            'provenance binds (verify_ro.py --excerpt). quotes: the record\'s evidence quotes.',
                   'records': {f'{a}:{i}': {'kind': full[a][i][0], 'quotes': full[a][i][1]}
                               for a, i in sorted(cited) if i in full.get(a, {})}}
        (HERE / 'atlas-excerpt.json').write_text(json.dumps(excerpt, ensure_ascii=False, indent=1) + '\n')
        missing = sorted(f'{a}:{i}' for a, i in cited if i not in full.get(a, {}))
        print(f"{len(excerpt['records'])} records written" + (f'; not in the atlases: {missing}' if missing else ''))
        return 1 if missing else 0

    failures = []
    # 1. preserved files
    bound = {}
    for f in prov['files']:
        path = SRC / f['file']
        if not path.exists():
            failures.append(f"missing preserved file: {f['file']}")
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != f['sha256']:
            failures.append(f"bytes changed: {f['file']}")
        bound[f['file']] = f
    for path in SRC.rglob('*'):
        rel = path.relative_to(SRC).as_posix()
        if path.is_file() and rel not in bound and rel not in ('README.md', 'PROVENANCE.json'):
            failures.append(f'file not bound by the provenance: {rel}')

    # 2. fragments verbatim
    ids = set()
    y1 = {p['id'] for p in json.loads(Y1.read_text())['passages']} if Y1.exists() else set()
    for p in passages:
        if p['id'] in ids or p['id'] in y1:
            failures.append(f"passage id repeated: {p['id']}")
        ids.add(p['id'])
        if p['tradition'] not in TRADITIONS:
            failures.append(f"{p['id']}: tradition not listed: {p['tradition']}")
        if p['source'] not in bound:
            failures.append(f"{p['id']}: source not bound by the provenance: {p['source']}")
            continue
        text = read_text(p['source'])
        for frag in p['fragments']:
            if frag not in text:
                failures.append(f"{p['id']}: not verbatim in {p['source']}: {frag}")
        if p['kind'] not in KIND_ZH or not (p['declarations'] or p.get('records')):
            failures.append(f"{p['id']}: kind, or declarations and records, missing")

    # 3. atlas ids
    excerpt = json.loads((HERE / 'atlas-excerpt.json').read_text())['records']
    for a, i in sorted(cited):
        if f'{a}:{i}' not in excerpt:
            failures.append(f'atlas id not in the excerpt: {a}:{i}')
    full = excerpt_from_packages(prov)
    rebuilt = 'packages absent: excerpt not rebuilt'
    if full is not None:
        for key, rec in excerpt.items():
            a, i = key.split(':', 1)
            if i not in full.get(a, {}) or full[a][i][1] != rec['quotes']:
                failures.append(f'excerpt differs from the package: {key}')
        rebuilt = 'excerpt rebuilt from the packages and agrees'

    # 4. declarations
    checks = PKG / 'becoming-checks'
    receipt = args.receipt or max(checks.glob('*/verification.json'))
    audited = {d['name'] for m in json.loads(receipt.read_text())['modules'] for d in m['declarations']}
    kit_sources = set()
    for path in (HERE / 'Becoming').glob('*.lean') if (HERE / 'Becoming').exists() else []:
        landed = PKG / 'Becoming' / path.name
        kit_sources |= lean_declarations((landed if landed.exists() else path).read_text())
    by_source = set()
    for p in passages:
        for d in p['declarations']:
            if d in audited:
                continue
            if d in kit_sources:
                by_source.add(d)
            else:
                failures.append(f"{p['id']}: no such audited declaration: {d}")

    # 5. records
    for p in passages:
        for r in p.get('records', []):
            if not (RECORDS / f'{r}.json').exists():
                failures.append(f"{p['id']}: no such record: {r}")

    # 6. the chapter tables
    if args.chapter.exists():
        text = args.chapter.read_text()
        for t in TRADITIONS:
            if not any(p['tradition'] == t for p in passages):
                continue
            if begin(t) not in text or end(t) not in text:
                failures.append(f'chapter has no passage-map markers for {t}')
                continue
            got = text[text.index(begin(t)) + len(begin(t)):text.index(end(t))].strip()
            if got != table(passages, t):
                failures.append(f'chapter table for {t} differs from passages.json (print it with --table)')
    else:
        failures.append(f'no chapter at {args.chapter}')

    kinds = {k: sum(p['kind'] == k for p in passages) for k in KIND_ZH}
    per = {t: sum(p['tradition'] == t for p in passages) for t in TRADITIONS}
    decls = {d for p in passages for d in p['declarations']}
    print(f"{len(passages)} passages ({kinds['agreement']} agreement, {kinds['scope']} scope, "
          f"{kinds['divergence']} divergence), {sum(len(p['fragments']) for p in passages)} fragments, "
          f"{len(decls)} declarations, {len(cited)} atlas ids; receipt {receipt.parent.name}; {rebuilt}"
          + (f'; {len(by_source)} names checked against the kit modules, not yet in the receipt' if by_source else ''))
    print('by tradition: ' + ', '.join(f'{t} {n}' for t, n in per.items() if n))
    for f in failures:
        print('FAIL', f)
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
