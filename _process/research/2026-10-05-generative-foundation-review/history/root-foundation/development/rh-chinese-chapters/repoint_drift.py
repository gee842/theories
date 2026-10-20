#!/usr/bin/env python3
"""RH (19 October 2026): re-point the references of records that `make research-render` reports as drifting only
in the sections RH changed, after reading the change. Run from the repository root:

    python3 -B .../rh-chinese-chapters/repoint_drift.py chapter ID ...   # THE-THEORY-OF-BECOMING.md, section 11 only
    python3 -B .../rh-chinese-chapters/repoint_drift.py sources          # chinese-sources-on-the-spine, sections 9 and 11

Each run sets the reference's sha256 to the file's current hash and records the reading in the record's history
(the RO record's RH entry already says what changed and gains the re-pointing clause). Rerun on a reland only after
reading `source_drift` again: a section other than those named here means the text needs reading first."""
import hashlib, json, sys

CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
RECORDS = 'theories/becoming/results/records/{}.json'


def digest(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def repoint(record_id, path):
    f = RECORDS.format(record_id)
    d = json.load(open(f, encoding='utf-8'))
    h, n = digest(path), 0
    for r in d['references']:
        if r['path'] == path and r['sha256'] != h:
            r['sha256'] = h
            n += 1
    assert n == 1, (record_id, n)
    return f, d


def write(f, d):
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


mode, ids = sys.argv[1], sys.argv[2:]
if mode == 'chapter':
    for i in ids:
        f, d = repoint(i, CHAPTER)
        d['history'].append({
            'en': '19 October 2026, RH (the four earlier Chinese chapters): THE-THEORY-OF-BECOMING.md re-pointed. Since '
                  "this record's reviewed hash, the cited text changed only in section 11 (where the earlier chapters "
                  'stand), where RH rewrote the rows of DAO-AND-GENERATIVITY, PRE-QIN-AND-WENYAN, HANZI-AND-THEORY-TREE '
                  'and WANG-YANGMING to say what each live chapter keeps and that its earlier text moved to history. '
                  'Read before re-pointing. The claim is unchanged.',
            'zh': '2026年10月19日，RH（四个较早的中国章节）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 11 节'
                  '（既有章节的位置）改动：RH 改写了 DAO-AND-GENERATIVITY、PRE-QIN-AND-WENYAN、HANZI-AND-THEORY-TREE 与 WANG-YANGMING '
                  '四行，说明各现行章留下什么、原文已移入历史。重新指向前已读。论断不变。'})
        write(f, d)
        print(i)
elif mode == 'sources':
    f, d = repoint('chinese-sources-on-the-spine', SOURCES)
    last = d['history'][-1]
    assert last['en'].startswith('19 October 2026 (RH)'), last
    if 're-pointed' not in last['en']:
        last['en'] += (' CHINESE-SOURCES-AND-BECOMING.md re-pointed after reading: since the reviewed hash only §9 and §11 '
                       'changed, by this step. The claim is unchanged.')
        last['zh'] += 'CHINESE-SOURCES-AND-BECOMING.md 读过改动后重新指向：自所审哈希以来只有 §9 与 §11 改动，即这一步。论断不变。'
    write(f, d)
    print('chinese-sources-on-the-spine')
else:
    sys.exit('mode: chapter ID ... | sources')
