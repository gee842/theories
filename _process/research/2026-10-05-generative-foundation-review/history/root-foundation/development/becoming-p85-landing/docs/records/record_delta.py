#!/usr/bin/env python3
"""P85 at landing: the Succession witness is a delta to continuing-self-fed-from-beyond, not a new result.
It adds the witness (aliases, a counterexample entry, a reference and a proof binding), narrows the limitation
and the next delta it answers, and appends a history line.

python3 -B record_delta.py ROOT RECEIPT_STAMP SECTION
(RECEIPT_STAMP: the consolidated receipt that first covers Becoming.Succession; SECTION: the integration note's section.)
Run before `research.py render`; the source and receipt hashes are then refreshed by the landing's usual repoint step,
which reads each changed file, not to silence a failure."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
STAMP, SECTION = sys.argv[2], sys.argv[3]
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{LEAN}/Becoming/Succession.lean'
RECEIPT = f'{LEAN}/becoming-verification.json'
path = ROOT / 'theories/becoming/results/records/continuing-self-fed-from-beyond.json'
r = json.loads(path.read_text())

for alias in ('Becoming.Successive.relay', 'Becoming.Successive.takes_part_once'):
    if alias not in r['aliases']:
        r['aliases'].append(alias)

r['counterexamples'].insert(1, {
    'path': SRC,
    'detail': {
        'zh': '也不必有哪个来源形成复现：Successive 中每步有它自己的源，只在那一步在场并活跃，燃烧那一步的燃料，'
              '向池给予一份；吃者每步从池取用一份。流平衡、耗散，只有活跃的形成给予；池每步从其外得到供给，'
              '而没有哪个来源形成在两步参与，也没有哪个在两步活跃（Successive.relay，由 Successive.takes_part_once 推出）。'
              '每个源仍在它自己的那一步被需要：去掉它，那一步不被供给。',
        'en': 'No source formation need recur either: in Successive each step has its own source, present and active at '
              'that step only, which burns that step\'s fuel and gives the pool one unit; the eater takes one unit from '
              'the pool at every step. The flow balances, is dissipative and only active formations give; the pool is '
              'fed from beyond at every step, while no source formation takes part at two steps and none is active at '
              'two (Successive.relay, from Successive.takes_part_once). Each source is still needed at its own step: '
              'without it that step is not fed.',
    },
})

lim = r['limitations']
old_zh, old_en = 'Lone 中输送的始终是同一个源；', 'in Lone the one source does all the conveying; '
assert old_zh in lim['zh'] and old_en in lim['en']
lim['zh'] = lim['zh'].replace(old_zh, 'Lone 中输送的始终是同一个源，Successive 中没有哪个来源形成复现，而每个源在它自己的那一步仍被需要；')
lim['en'] = lim['en'].replace(old_en, 'in Lone the one source does all the conveying, and in Successive no source formation '
                                      'recurs while each source is still needed at its own step; ')

nd = r['next_delta']
old_zh = '两个可移除的来源交替供给的见证（不需要特定的来源形成）；'
old_en = 'a witness fed alternately by two removable sources (no particular source formation needed); '
assert old_zh in nd['zh'] and old_en in nd['en']
nd['zh'] = nd['zh'].replace(old_zh, '没有哪个来源形成复现的见证已给出（Successive.relay）；可移除的形式，即同一世界去掉一个来源形成后'
                                    '仍每步得到供给（去掉形成会改变水平，所以那是另一个流，以世界为单位的形式是它的位置）；')
nd['en'] = nd['en'].replace(old_en, 'the witness in which no source formation recurs is given (Successive.relay); the '
                                    'removable form, the same world still fed at every step with one source formation '
                                    'taken away (taking a formation away changes the levels, so that is another flow, '
                                    'and the world-level form is its place); ')

digest = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
refs = r['references']
at = next(i for i, x in enumerate(refs) if x['role'] == 'receipt')
refs.insert(at, {'path': SRC, 'role': 'proof', 'sha256': digest, 'declarations': [
    'Becoming.Successive.flow', 'Becoming.Successive.web', 'Becoming.Successive.balances',
    'Becoming.Successive.dissipative', 'Becoming.Successive.acting', 'Becoming.Successive.fed',
    'Becoming.Successive.takes_part_once', 'Becoming.Successive.relay']})
r['proof_bindings'].append({'source': SRC, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/Becoming.Succession',
                            'success_pointer': '/status', 'success_value': 'passed'})

r['history'].append({
    'zh': f'2026-10-12 P85：按 Ren“move towards 100%”加入 Successive（Becoming.Succession）：没有哪个来源形成复现的见证，'
          f'回答本记录 next_delta 中的这一项；合并检查器回执 {STAMP}；见整合文档 §{SECTION}。原有定理不变。',
    'en': f'2026-10-12 P85: following Ren\'s ‘move towards 100%’, Successive (Becoming.Succession) added: the witness in '
          f'which no source formation recurs, answering that item of this record\'s next_delta; consolidated receipt '
          f'{STAMP}; see §{SECTION} of the integration note. The existing theorems are unchanged.',
})

path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('continuing-self-fed-from-beyond: P85 delta applied', digest[:12])

# derived-extent-limits names the same open witness in its next delta; it only points to the witness, binding no proof.
path = ROOT / 'theories/becoming/results/records/derived-extent-limits.json'
r = json.loads(path.read_text())
nd = r['next_delta']
old_zh, old_en = '两个可移除来源交替供给的见证；', 'a witness fed alternately by two removable sources; '
assert old_zh in nd['zh'] and old_en in nd['en'], 'derived-extent-limits next_delta wording changed: reread it'
nd['zh'] = nd['zh'].replace(old_zh, '同一世界去掉一个来源形成后仍每步得到供给的见证（没有哪个来源形成复现的见证已给出：Successive.relay，'
                                    '见 continuing-self-fed-from-beyond）；')
nd['en'] = nd['en'].replace(old_en, 'a witness still fed at every step with one source formation taken away from the same '
                                    'world (the witness in which no source formation recurs is given: Successive.relay, see '
                                    'continuing-self-fed-from-beyond); ')
r['history'].append({
    'zh': f'2026-10-12 P85：next_delta 中“两个可移除来源交替供给的见证”一项改为指向 Successive.relay（没有哪个来源形成复现），'
          f'留下同一世界去掉来源形成的形式；见整合文档 §{SECTION}。断言不变。',
    'en': f'2026-10-12 P85: the next_delta item ‘a witness fed alternately by two removable sources’ now points to '
          f'Successive.relay (no source formation recurs), leaving the form with a source formation taken away from the '
          f'same world; see §{SECTION} of the integration note. The claim is unchanged.',
})
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('derived-extent-limits: P85 next_delta pointer applied')
