#!/usr/bin/env python3
"""R37: mark the aliases that only an earlier receipt elaborated, as R35 (E8) did.

Rebinding a record's proof bindings to R37's receipt (the Lean files R37 changed) drops the earlier receipt
that listed some of its aliases: declarations of modules no longer in the run, the bridge and instance
modules the F3 sweep moved to lean/history/becoming (`Becoming.Bridge`, `Becoming.CompositionBridge`,
`Becoming.Instances`) and periphery modules outside the run (`deeper/WisdomResponseStructure.lean`,
`ExplanatoryFootprints`, `ExplanatoryJointness`, `DynamicConsequences`). Each such alias is marked
"(retired module)" or "(periphery module)", so it reads as a name, not as a claim on the bound receipts; the
receipts that checked those modules still name them. The pairs are in retired-aliases.json (from the render
log). A history note says which aliases were marked.

usage: python3 -B aliases.py   (once, after rebind.py and repoint.py)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PAIRS = json.load(open(HERE / 'retired-aliases.json'))
by = {}
for ident, alias in PAIRS:
    by.setdefault(ident, []).append(alias)
for ident, aliases in sorted(by.items()):
    f = ROOT / 'theories/becoming/results/records' / (ident + '.json')
    d = json.load(open(f))
    marked = []
    for i, a in enumerate(d['aliases']):
        if a in aliases:
            tag = '(periphery module)' if a.startswith('Generative.') else '(retired module)'
            d['aliases'][i] = f'{a} {tag}'
            marked.append(d['aliases'][i])
    assert len(marked) == len(aliases), (ident, aliases, marked)
    en = (f'{len(marked)} alias' + ('es' if len(marked) > 1 else '') + ' naming declarations of modules no longer in the run, '
          'which only the earlier receipt this record was bound to elaborated, marked as R35 (E8) did: ' + '; '.join(marked) + '.')
    zh = f'{len(marked)} 个指向已不在运行中的模块之声明的别名（只有本记录先前绑定的回执列出它们）按 R35（E8）的做法标出：' + '；'.join(marked) + '。'
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R37'):
        last['en'] = last['en'].rstrip() + ' Also: ' + en
        last['zh'] = last['zh'].rstrip() + '另：' + zh
    else:
        d.setdefault('history', []).append({
            'en': '20 October 2026, R37 (lens B of the twentieth review): the proof bindings to the Lean files R37 changed rebound to its core receipt; ' + en + ' The claim is unchanged.',
            'zh': '2026年10月20日，R37（第二十次评审的 B 视角）：对 R37 改动的 Lean 文件的证明绑定改到其核心回执；' + zh + '论断不变。'})
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(ident, len(marked))
