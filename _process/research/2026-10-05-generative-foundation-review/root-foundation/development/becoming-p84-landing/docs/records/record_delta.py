#!/usr/bin/env python3
"""P84 at landing: evolution-on-descent's next delta asks whether TransmitsWithin can be derived; P84 answers it.
Points that item to the two new records, narrows the limitation sentence and appends a history line.
python3 -B record_delta.py ROOT SECTION   (run before `research.py render`)"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTION = sys.argv[2]
path = ROOT / 'theories/becoming/results/records/evolution-on-descent.json'
r = json.loads(path.read_text())

nd = r['next_delta']
old_en = 'whether TransmitsWithin can be derived from how giving and dependence form in the one-kind reading, rather than supplied; '
assert old_en in nd['en'], 'evolution-on-descent next_delta (en) changed: reread it'
nd['en'] = nd['en'].replace(old_en, 'whether TransmitsWithin can be derived is answered by transmission-is-inheritance-and-need and '
                            'transmission-independent-where-it-binds (P84): not from the other premises, and from a reading of '
                            'drawing with drawing being depending; a law of forming that is also necessary; ')
zh_marks = [m for m in ('TransmitsWithin 能否', 'TransmitsWithin 是否') if m in nd['zh']]
assert len(zh_marks) == 1, 'evolution-on-descent next_delta (zh) changed: reread it'
head, tail = nd['zh'].split(zh_marks[0], 1)
end = tail.index('；') + 1
nd['zh'] = head + ('TransmitsWithin 能否推出已由 transmission-is-inheritance-and-need 与 transmission-independent-where-it-binds '
                   '回答（P84）：不能由其余前提推出，可由取用的读法加上取用即依存推出；同时是必要条件的形成规律；') + tail[end:]

lim = r['limitations']
old_en = "transmission (TransmitsWithin) is a premise, and the spine does not derive that descendants take up their parents' dependences"
assert old_en in lim['en'], 'evolution-on-descent limitation (en) changed: reread it'
lim['en'] = lim['en'].replace(old_en, "transmission (TransmitsWithin) is a premise here; P84 proves it independent wherever it binds "
                              "and derives it from a reading of drawing with drawing being depending (see "
                              "transmission-independent-where-it-binds)")
old_zh = '传递（TransmitsWithin）是前提，脊柱不推出后代承接亲代的依存'
assert old_zh in lim['zh'], 'evolution-on-descent limitation (zh) changed: reread it'
lim['zh'] = lim['zh'].replace(old_zh, '传递（TransmitsWithin）在此是前提；P84 证明它在起约束之处独立，并由取用的读法加上取用即依存推出'
                              '（见 transmission-independent-where-it-binds）')
r['related'].append({'id': 'transmission-is-inheritance-and-need', 'detail': {
    'zh': '传递的确切形式：承继加所需之界；演化的界在一次世系上，只需某个被支持的给予者。',
    'en': 'The exact form of transmission: inheritance with the need within a bound; the evolution bounds at one descent, '
          'needing only some supported giver.'}})
r['history'].append({
    'zh': f'2026-10-12 P84：next_delta 中传递能否推出一项由 transmission-is-inheritance-and-need 与 '
          f'transmission-independent-where-it-binds 回答；见整合文档 §{SECTION}。断言不变。',
    'en': f'2026-10-12 P84: the next_delta item on deriving transmission is answered by transmission-is-inheritance-and-need '
          f'and transmission-independent-where-it-binds; see §{SECTION} of the integration note. The claim is unchanged.'})
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('evolution-on-descent: P84 delta applied')
