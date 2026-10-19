#!/usr/bin/env python3
"""Build passages.json of board item RO from the five mappers' entries (mappers/<slice>/entries.json),
and preserve the atlas texts they quote. usage: python3 -B build_passages.py [--preserve]

- Each entry is normalized: its tradition into the chapter's sections, its text into a path under
  sources/chinese-classical-texts/ (an atlas text, or a Wikisource page retrieved by
  fetch_wikisource.py), and its atlas ids into {atlas, id} pairs resolved against both atlases.
- The corrections listed in FIXES are applied (each with its reason); every fragment is then checked
  against the preserved text, and every failure is printed.
- With --preserve, the atlas texts quoted are copied from the two archives into
  sources/chinese-classical-texts/<atlas>/ (never over an existing file) and PROVENANCE.json is written.
The mappers' readings are the AI's; this script does not change them, except where FIXES says
(a source, locator or fragments replaced, or a sentence of a reading replaced after review)."""
import argparse
import hashlib
import json
import sys
import urllib.parse
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_ro as V  # noqa: E402

SLICES = ['yi', 'lao', 'ru', 'wen', 'other']
STORE = '/Users/ren/Documents/Codex/2026-10-13/referenced-chatgpt-conversation-this-is-an/outputs'
ATLASES = [
    {'id': 'yidao-v1.3', 'title': '周易易传与道德经体系图 v1.3.0',
     'zip_path': f'{STORE}/周易易传与道德经体系图-v1.3.0.zip',
     'zip_sha256': '4ddc4adb2bb3ed14da4191ef6d81120e836f24a6c3dc4ad48bd09207cfde0413',
     'zip_bytes': 23410000, 'prefix': 'yi-dao-system-v1.3/'},
    {'id': 'atlas-v9.1', 'title': '观其会通 · 中国传统思想研究图谱 v9.1.0',
     'zip_path': f'{STORE}/chinese-thought-atlas-v9.1.zip',
     'zip_sha256': 'bb2929d2e179f6d9dbbc8b4c43f13a9d4be92323c860fe246942b93dc4555f2b',
     'zip_bytes': 78036347, 'prefix': 'chinese-thought-atlas-v9.1/'},
]

ABOUT = {
    'work': ('Chinese classical texts quoted by the passage map of board item RO: the 易传 and its commentaries, the 老子 '
             'with the 王弼, 河上公 and 苏辙 commentaries and the 郭店 and 帛书 witnesses, the 儒家 line from the 论语 to '
             '戴震, the 说文解字 and the 左传 (止戈为武), 庄子 and 玄学, 墨辩 and 名家, 兵家, 法家, 管子 and 鬼谷子, '
             'the Buddhist texts received in China, 嵇康 and 王充.'),
    'edition': ('Two kinds of file. (1) Texts of two atlases built with Codex, each copied byte for byte from the atlas '
                'archive named in `atlases` (the archive member is given per file, with the atlas\'s own record of the '
                'text in `atlas_source`: its title, URL and edition note). The atlases\' texts are electronic '
                'transcriptions: 71 of the 79 from Chinese Wikisource, five from CBETA (the 雜阿含經, 中論, 壇經, '
                '成唯識論 and 華嚴五教章), two from xuges.com (王夫之《周易外傳》) and one checked against a scan of the '
                'National Diet Library (王夫之《思問錄》); the atlases do not claim them to be collated editions, and the '
                'excavated witnesses are the atlases\' transcriptions. (2) Chinese Wikisource pages the atlases do not '
                'hold, at the revisions named per file. Neither kind is collated with a printed edition.'),
    'retrieval': ('Archive members: read on 19 October 2026 from the two archives in the external store, verified by '
                  'their SHA-256 before reading. Wikisource pages: MediaWiki API, action=query, prop=revisions, '
                  'rvprop=ids|timestamp|content, rvslots=main, format=json, formatversion=2, redirects=1, with a user '
                  'agent naming the repository, on 19 October 2026 (fetch_wikisource.py in the RO kit, which never '
                  'overwrites a file).'),
    'forms': {'archive-member': 'The archive member, byte for byte.',
              'api-response': "The API's response body, byte for byte as received."},
    'license': ('The texts are pre-modern and in the public domain. Wikisource\'s punctuation and markup are CC BY-SA '
                '4.0. The five CBETA texts are CBETA\'s digital editions of the 大正藏, kept with attribution under '
                'CBETA\'s terms for non-commercial distribution; the xuges.com and National Diet Library notes are in '
                '`atlas_source`. The atlases themselves were built for this work.'),
    'markup': ('Wikisource wikitext carries character-variant markup, templates and links; a reading strips them '
               '(clean() in verify_ro.py) and keeps the content of {{yw|…}} and {{+|…}}.'),
    'reading_scope': ('Only the passages the map quotes were read closely, each in its chapter; retaining whole texts '
                      'does not imply reading them whole.'),
    'used_by': ['theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md',
                '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources/passages.json'],
}

OTHER = [  # the other slice, by work
    ('庄子与玄学', ('庄子', '郭象', '裴頠')),
    ('墨家与名家', ('墨', '公孙龙', '惠施')),
    ('兵家、法家与轻重纵横', ('孙子', '吴子', '韩非', '商君', '管子', '鬼谷子')),
    ('佛教', ('阿含', '中论', '唯识', '华严', '坛经', '天台', '般若', '涅槃')),
]

# Corrections, each with its reason. Keys: entry id; values: the fields replaced.
FIXES = {
    'ru-zhengxuan-ren-zhe-ren-ye': {
        'source': 'wikisource/禮記正義__52.json',
        'fragments': ['人也，讀如相人偶之「人」。以人意相存問之言。'],
        'locator': '《禮記·中庸》「仁者，人也」鄭玄注（《禮記正義》卷五十二）',
        'why': 'the note as it stands in 禮記正義 卷五十二 (the mapper gave it from memory, with 人 unquoted)'},
    'cy-xu-tiyong': {
        'source': 'wikisource/Page_文淵閣四庫全書_0009冊.djvu__162.json',
        'fragments': ['易變易也隨時變易以從道也', '至微者理也至著者', '象也體用一源顯微无間'],
        'why': 'the 四庫 page holding 程頤 易傳序; the page breaks the line after 至著者'},
    'shuowen-wu-zhi-ge-gloss': {
        'fragments': ['楚莊王曰：“夫武，定功戢兵。故止戈爲武。”'],
        'why': 'the page quotes with “ ” (the mapper gave 「」)'},
    'huishi-li-wu': {
        'fragments': ['至大无外，謂之大一；至小无內，謂之小一。', '日方中方睨，物方生方死。', '氾愛萬物，天地一體也。'],
        'why': 'the page writes 无 (the mapper gave 無)'},
    'lao-01-ming-ke-ming': {
        'reading_sub': [('所以“可道者非常道”在“由内部说出”的意义上是定理。',
                         '所以把“可道”读作由内部说出、把“常道”读作每一种模式时，“可道者非常道”与这些定理同构；这一对应是读法，定理本身只说断言族与模式。')],
        'why': 'review: the reading called the line itself a theorem; the theorems are about claim families, and the line corresponds to them under a reading'},
    'hs-39-bu-ke-dan-yu': {
        'reading_sub': [('理论支持第三十九章。', '脊柱的定律与第三十九章相合，与第六、十六章所许诺的不死相分。')],
        'why': 'review: "the theory supports chapter 39" stated as which laws agree with which chapter'},
}


def tradition(slice_, e):
    fixed = {'yi': '易传', 'lao': '老子', 'ru': '儒家', 'wen': '文字'}
    if slice_ in fixed:
        return fixed[slice_]
    work = e.get('tradition', '')
    for name, keys in OTHER:
        if any(k in work for k in keys):
            return name
    return '其他'


def source_path(e, atlas_of_text):
    if e.get('needs_source'):
        title = urllib.parse.unquote(e['needs_source']).split('/wiki/', 1)[1].replace('_', ' ')
        title = {'莊子/雜篇/天下': '莊子/天下'}.get(title, title)
        return 'wikisource/' + title.replace('/', '__').replace(' ', '_').replace(':', '_') + '.json'
    tp = e['text_path']
    name = tp.split('evidence/texts/', 1)[1]
    return f'{atlas_of_text}/evidence/texts/{name}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--preserve', action='store_true')
    args = ap.parse_args()
    archives = {a['id']: zipfile.ZipFile(a['zip_path']) for a in ATLASES}
    members = {a['id']: {n[len(a['prefix']):] for n in archives[a['id']].namelist()} for a in ATLASES}
    index = {}
    for a in ATLASES:
        zf = archives[a['id']]
        index[a['id']] = V.load_atlas(a['id'], lambda n, zf=zf, p=a['prefix']: zf.read(p + n).decode())

    passages, problems, wanted = [], [], set()
    seen = set()
    y1 = {p['id'] for p in json.loads(V.Y1.read_text())['passages']}
    for s in SLICES:
        for e in json.loads((HERE / 'mappers' / s / 'entries.json').read_text()):
            e = dict(e)
            fix = FIXES.get(e['id'], {})
            order = [a.strip() for a in (e.get('atlas') or '').split(';') if a.strip() in members]
            order += [a for a in members if a not in order]
            name = (e.get('text_path') or '').split('evidence/texts/', 1)[-1]
            text_atlas = next((a for a in order if 'evidence/texts/' + name in members[a]), order[0])
            src = fix.get('source') or source_path(e, text_atlas)
            pid = e['id'] if e['id'] not in seen and e['id'] not in y1 else f"{s}-{e['id']}"
            seen.add(pid)
            ids = []
            for i in e.get('atlas_ids') or []:
                where = [a for a in ('yidao-v1.3', 'atlas-v9.1') if i in index[a]]
                if not where:
                    problems.append(f'{pid}: atlas id in neither atlas: {i}')
                    continue
                ids.append({'atlas': where[0], 'id': i})
            p = {
                'id': pid,
                'tradition': tradition(s, e),
                'work': e.get('tradition', ''),
                'source': src,
                'locator': fix.get('locator', e.get('locator', '')),
                'fragments': fix.get('fragments', e['fragments']),
                'kind': e['kind'],
                'declarations': e.get('declarations', []),
                'records': e.get('records', []),
                'atlas_ids': ids,
                'relational': e.get('relational', ''),
                'reading': e['reading'],
                'reading_en': e.get('reading_en', ''),
                'mapper': s,
            }
            for k in ('layer', 'variants', 'gap'):
                if e.get(k):
                    p[k] = e[k]
            for old, new in fix.get('reading_sub', []):
                if old not in p['reading']:
                    problems.append(f'{pid}: reading correction does not apply: {old}')
                p['reading'] = p['reading'].replace(old, new)
            if fix:
                p['corrected'] = fix['why']
            if not src.startswith('wikisource/'):
                wanted.add(src)
            passages.append(p)

    if args.preserve:
        # Each atlas's own record of where a text came from, by the text's path or name.
        origin = {}
        for a in ATLASES:
            zf, p = archives[a['id']], a['prefix']
            if a['id'] == 'yidao-v1.3':
                records = json.loads(zf.read(p + 'data/model.json'))['sources']
            else:
                records = [json.loads(x) for x in zf.read(p + 'data/sources.jsonl').decode().splitlines() if x.strip()]
            for r in records:
                keys = {r.get('text_path'), r.get('snapshot_path'), f"evidence/texts/{r['id']}.txt"}
                for k in keys - {None}:
                    origin.setdefault((a['id'], k.split('evidence/texts/')[-1]), r)
        files = []
        root = V.SRC
        for rel in sorted(wanted):
            atlas, inner = rel.split('/', 1)
            a = next(x for x in ATLASES if x['id'] == atlas)
            data = archives[atlas].read(a['prefix'] + inner)
            path = root / rel
            if path.exists():
                if path.read_bytes() != data:
                    raise SystemExit(f'preserved file differs from the archive: {rel}')
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
        for path in sorted(root.rglob('*')):
            rel = path.relative_to(root).as_posix()
            if path.is_file() and rel not in ('README.md', 'PROVENANCE.json'):
                entry = {'file': rel, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
                if rel.startswith('wikisource/'):
                    page = json.loads(path.read_text())['query']['pages'][0]
                    rev = page['revisions'][0]
                    entry.update({'title': page['title'], 'revid': rev['revid'], 'timestamp': rev['timestamp'],
                                  'form': 'api-response'})
                else:
                    a = next(x for x in ATLASES if x['id'] == rel.split('/', 1)[0])
                    entry.update({'archive_member': a['prefix'] + rel.split('/', 1)[1], 'form': 'archive-member'})
                    r = origin.get((a['id'], rel.split('evidence/texts/')[-1]))
                    if r:
                        entry['atlas_source'] = {k: r[k] for k in ('id', 'title', 'url', 'oldid', 'immutable_url',
                                                                   'edition_note', 'rights_note', 'license_note')
                                                 if r.get(k)}
                files.append(entry)
        prov = json.loads((root / 'PROVENANCE.json').read_text()) if (root / 'PROVENANCE.json').exists() else {}
        prov.update(ABOUT)
        prov['atlases'] = ATLASES
        prov['files'] = files
        (root / 'PROVENANCE.json').write_text(json.dumps(prov, ensure_ascii=False, indent=1) + '\n')
        print(f'{len(files)} files bound')

    for p in passages:
        path = V.SRC / p['source']
        if not path.exists():
            problems.append(f"{p['id']}: no preserved text {p['source']}")
            continue
        text = V.read_text(p['source'])
        for f in p['fragments']:
            if f not in text:
                problems.append(f"{p['id']}: not verbatim in {p['source']}: {f}")
    data = {
        'about': ('The passage map of board item RO: passages of the Chinese sources, each quoted verbatim from a '
                  'text preserved in sources/chinese-classical-texts/ (two atlases built with Codex, and Wikisource '
                  'pages), its kind of relation to the spine, the declarations and records it corresponds to, and '
                  'the atlas records it cites. Built by build_passages.py from the five mappers\' entries '
                  '(mappers/); the readings, relational notes and gaps are AI readings. verify_ro.py checks it.'),
        'kinds': {'agreement': '相合：原文所说之结构，脊柱上有已检查之律与之对应。',
                  'scope': '定域：脊柱给出此句成立的确切范围，并修正其全称形式。',
                  'divergence': '相分：原文所断言者，理论不断言，或与理论的结构相冲突。'},
        'passages': passages,
    }
    (HERE / 'passages.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
    print(f'{len(passages)} passages written')
    for x in problems:
        print('PROBLEM', x)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
