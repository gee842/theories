#!/usr/bin/env python3
"""Y4: re-point the canonical chapter reference of Y3's record hexagram-world-laws after reading the change. That
reference was already stale at the landing base for sections the record does not cite (rehash_refs.py leaves such a
reference as it was); Y4's section 11 row names the record, so the drift check reads it as cited. The section 11
statement-source row of the chapter on the 易传 now also names fixed-places-and-sole-lines, and section 1 gains the
paragraph on 王弼's readings after this record's; the claim is unchanged.
usage (from the landing checkout's root, after apply_text.py): python3 -B repoint_y3.py"""
import hashlib, json

f = 'theories/becoming/results/records/hexagram-world-laws.json'
p = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
d = json.load(open(f, encoding='utf-8'))
cur = hashlib.sha256(open(p, 'rb').read()).hexdigest()
refs = [r for r in d['references'] if r['path'] == p and r['sha256'] != cur]
if not refs:
    print('hexagram-world-laws: nothing to re-point')
    raise SystemExit
for r in refs:
    r['sha256'] = cur
d['history'].append({
    'en': '19 October 2026, Y4 (Becoming.HexagramSites): THE-THEORY-OF-BECOMING.md re-pointed after reading the change '
          '(section 11: the statement-source row of the chapter on the 易传 now also names fixed-places-and-sole-lines; '
          'Y4 also added the section 1 paragraph on 王弼\'s readings of the places after this record\'s, and the earlier '
          'changes since this record bound the file are in sections it does not cite). The claim is unchanged.',
    'zh': '2026年10月19日，Y4（Becoming.HexagramSites）：读过改动后，THE-THEORY-OF-BECOMING.md 重新指向（第 11 节易传一章的'
          '陈述来源行增列 fixed-places-and-sole-lines；第 1 节在本记录的段落之后增加王弼之读一段）。论断不变。'})
open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('hexagram-world-laws: re-pointed', len(refs))
