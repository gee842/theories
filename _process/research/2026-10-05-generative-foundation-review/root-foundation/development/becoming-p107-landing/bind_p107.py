#!/usr/bin/env python3
"""P107 landing pass (run from the checkout root, after the core run and the last documentary edit).

usage: bind_p107.py CORE_RECEIPT N [--write] [--list]
CORE_RECEIPT: the run folder's verification.json, relative to the root; N: P107's study section.

1. The three new records: every proof reference is bound to the core run, the run becomes a hashed
   receipt reference, and "receipt bound at landing" names the run.
2. Every record: a reference to a file this landing changed (FILES) gets its current sha256; a proof
   binding whose receipt no longer binds its source's current bytes is re-pointed to the core run when
   that run binds them, else reported. The seven P107 records extend their own P107 note; every other
   changed record gets one paired note naming each file and why it changed.
A changed reference to any other file is reported and left alone.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
LEANROOT = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LEANDIR = LEANROOT + 'becoming/'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
N = int(sys.argv[2])
NEW = {'returning-novelty-forgetting-on-levels', 'premises-read-off-the-exchange', 'unity-of-readings'}
EDITED = {'imbalance-as-relatum', 'map-of-premises', 'process-and-frame-as-readings', 'contextual-registration'}
FILES = {
    RF + 'BECOMING-RENEWAL-READING.md': (
        f'新增第{N}节（从关系开始的重建：Becoming.Novelty、Becoming.Reading、Becoming.Readings）及其英文段；此前各节不变',
        f'section {N} (the relation-first re-founding: Becoming.Novelty, Becoming.Reading, Becoming.Readings) with its English '
        'paragraph; earlier sections unchanged'),
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md': (
        '“完整陈述的理论”第1、3项补上 World 不是起点与前提的独立性；第一部分补上三条规律；§8 的表与 Ren 的选择补上从关系开始的重建；'
        '§9 新增 Novelty、Reading、Readings 三行，Imbalance 行与术语表记 Ren 2026-10-14 的采用；总数改据新回执；此外不变',
        'the theory stated in full, items 1 and 3 (World is not the start; the independence of the premises); Part I (three '
        'laws); the §8 table and Ren\'s choices (the relation-first re-founding); §9 rows for Novelty, Reading and Readings, '
        'and the Imbalance row and glossary recording Ren\'s adoption of 14 October 2026; totals moved to the new receipt; '
        'otherwise unchanged'),
    RF + 'ZERO-PREMISE-PLAN.md': (
        '§1.4 的不平衡一项记 Ren 2026-10-14 的采用；可判定性总数改据重新生成的清单',
        'section 1.4: the imbalance item records Ren\'s adoption of 14 October 2026; decidability totals from the regenerated '
        'inventory'),
    RF + 'DECIDABILITY-INVENTORY.md': None,  # computed from the page's change: inventory_reason()
    LEANDIR + 'Becoming.lean': (
        '导入 Novelty、Reading、Readings 并加模块说明；Imbalance 一项记 Ren 的采用',
        'imports Novelty, Reading and Readings with their module notes; the Imbalance note records Ren\'s adoption'),
    # the new records were written before integration I3a added theorems to these two modules
    LEANDIR + 'Becoming/Recurrence.lean': (
        '整合 I3a 加入 keeps_reach_iff_returns、same_reach_iff_returns、not_returns_iff_loses 及其说明；本记录所引的声明不变',
        'integration I3a added keeps_reach_iff_returns, same_reach_iff_returns and not_returns_iff_loses with their summary; '
        'the declarations this record cites are unchanged'),
    LEANDIR + 'Becoming/Unfolding.lean': (
        '整合 I3a 加入 same_steps_iff_traces 及其说明；本记录所引的声明不变',
        'integration I3a added same_steps_iff_traces with its summary; the declarations this record cites are unchanged'),
    LEANDIR + 'check_becoming.py': (
        'CORE 列表加入三个新模块', 'the CORE list adds the three new modules'),
    LEANDIR + 'becoming-verification.json': (
        '指向新回执', 'points to the new receipt'),
    LEANDIR + 'README.md': (
        '模块表加入 Novelty、Reading、Readings 三行，Imbalance 一行记 Ren 的采用，层内导入补上',
        'the module table adds rows for Novelty, Reading and Readings, the Imbalance row records Ren\'s adoption, and the '
        'within-layer imports are completed'),
    RF + 'DECIDABILITY-INVENTORY.py': (
        'upto_or_fails 归为“找出”', 'upto_or_fails classified as finding a step'),
}
NOTE_ZH = f'2026年10月15日，从关系开始的重建（Becoming.Novelty、Becoming.Reading、Becoming.Readings；研究第{N}节）：'
NOTE_EN = ('15 October 2026, the relation-first re-founding (Becoming.Novelty, Becoming.Reading, Becoming.Readings; study '
           f'section {N}): ')
DID = {False: ('更新哈希：', 'rehashed: '), True: ('更新哈希并改绑新回执：', 'rehashed and rebound to the new receipt: ')}
# a record whose subject is a changed file says, after reading the change, that its claims stand
STANDS = {'counts-exist-where-decided': ('；读过清单的变化，本记录的陈述与局限不变',
                                         '; read against the inventory\'s changes, this record\'s statement and limitations stand')}
OWN_ZH, OWN_EN = ('2026-10-14：新增，按 Ren 批准', '14 October 2026: added under Ren'), ('2026-10-14 P107（', '14 October 2026, P107 (')


INV = RF + 'DECIDABILITY-INVENTORY.md'
CLASSES = [('陈述依赖它', '陈述依赖可判定性的定理', 'statements depending on decidedness'),
           ('只在证明中用到', '只在证明中用到', 'used only in proofs'),
           ('不用到', '不用到', 'unused'),
           ('排中律或其受限形式作为假设', '排中律作为假设', 'excluded middle as a hypothesis'),
           ('计数而可判定被证明', '计数而可判定被证明', 'counting with decidedness proved'),
           ('证明可判定的定义与实例', '证明可判定的定义与实例', 'definitions and instances proving decidedness'),
           ('取可判定族的定义', '计数的原语', 'counting primitives')]
OURS = ('Novelty', 'Reading', 'Readings')
# the page counts the theorems that count with decidedness proved only by module; this is Novelty's one
NOVELTY_PROVED = 'Web.changes_le_stock'


def inventory_reason():
    """The inventory page's change, read off the page before (HEAD) and after: the totals that moved, the totals
    that held, and the rows of the three new modules by class and reason."""
    old = subprocess.run(['git', 'show', 'HEAD:' + INV], capture_output=True, text=True, check=True).stdout
    new = (ROOT / INV).read_text()

    def totals(page):
        part = page[page.index('## 总数 / Totals'):page.index('## 理由 / Reasons')]
        rows = [l.split(' | ') for l in part.splitlines() if l.startswith('| ') and not l.startswith('| 类')]
        out = {}
        for key, _, _ in CLASSES:
            hit = [r for r in rows if r[0].lstrip('| ').startswith(key)]
            assert len(hit) == 1, (key, len(hit))
            out[key] = int(hit[0][-1].rstrip(' |'))
        return out

    def ours(page):
        found, section = [], None
        for line in page.splitlines():
            if line.startswith('## '):
                section = line
            elif line.startswith('| ') and line.split(' | ')[0].lstrip('| ') in OURS:
                cells = line.split(' | ')
                found.append((section, cells[0].lstrip('| '), cells[1].strip('`'), cells[3]))
        return found

    t0, t1 = totals(old), totals(new)
    assert not ours(old), 'the page before already lists rows of the new modules'
    rows = ours(new)
    moved = [(zh, en, t0[k], t1[k]) for k, zh, en in CLASSES if t0[k] != t1[k]]
    held = [(zh, en, t1[k]) for k, zh, en in CLASSES if t0[k] == t1[k] and k in ('排中律或其受限形式作为假设',)]
    proved = '- Novelty: 1' in new and '- Novelty: 1' not in old
    groups = {}
    for _, mod, name, reason in rows:
        groups.setdefault((mod, reason), []).append(name)
    zh_rows = '，'.join(f'{m} 的 ' + '、'.join(ns) + f'（{r.split(" / ")[0]}）' for (m, r), ns in groups.items())
    en_rows = ', '.join(f'Becoming.{m}\'s ' + ' and '.join(ns) + f' ({r.split(" / ")[1]})' for (m, r), ns in groups.items())
    zh = ('据新回执重新生成：' + '，'.join(f'{a} {o} → {n}' for a, _, o, n in moved)
          + (f'（新增的行：{zh_rows}' + (f'；计数而可判定被证明的一条是 Novelty 的 {NOVELTY_PROVED}' if proved else '') + '）')
          + ''.join(f'，{a}仍为 {n}' for a, _, n in held) + '；其余各行不变')
    en = ('regenerated on the new receipt: ' + ', '.join(f'{b} {o} → {n}' for _, b, o, n in moved)
          + (f' (new rows: {en_rows}' + (f'; the one counting with decidedness proved is Novelty\'s {NOVELTY_PROVED}'
                                         if proved else '') + ')')
          + ''.join(f', {b} unchanged at {n}' for _, b, n in held) + '; other rows unchanged')
    return zh, en


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pointer(doc, ptr):
    cur = doc
    for part in ptr.strip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return None
    return cur


def main():
    core = sys.argv[1]
    run = json.loads((ROOT / core).read_text())
    assert run['status'] == 'passed', run['status']
    utc = core.split('/')[-2]
    write = '--write' in sys.argv
    FILES[INV] = inventory_reason()
    print('inventory reason:', FILES[INV][1])
    # source_paths are relative to the lean/ directory that holds becoming/
    module_of = {LEANROOT + path: name for name, path in run['source_paths'].items()}
    receipts = {}

    def receipt(path):
        if path not in receipts:
            receipts[path] = json.loads((ROOT / path).read_text())
        return receipts[path]

    report = {'changed': [], 'unhandled_drift': [], 'unbound': [], 'new_bound': {}}
    for p in sorted(REC.glob('*.json')):
        r = json.loads(p.read_text())
        rid = r['id']
        touched, rebound, extra = [], False, []
        if rid in NEW:
            bound = {b['source'] for b in r['proof_bindings']}
            for ref in r['references']:
                if ref['role'] == 'proof' and ref['path'] not in bound:
                    name = module_of.get(ref['path'])
                    assert name and pointer(run, f'/source_sha256/{name}') == sha(ref['path']), ref['path']
                    r['proof_bindings'].append({'source': ref['path'], 'receipt': core,
                                                'sha256_pointer': f'/source_sha256/{name}',
                                                'success_pointer': '/status', 'success_value': 'passed'})
                    bound.add(ref['path'])
            if not any(x.get('path') == core for x in r['references']):
                r['references'].append({'path': core, 'role': 'receipt', 'sha256': sha(core), 'declarations': []})
            vs = r['validation_scope']
            for lang, old, new in (('en', 'receipt bound at landing', f'receipt {utc}'), ('zh', '回执于落地时绑定', f'回执 {utc}')):
                assert vs[lang].count(old) == 1, (rid, lang)
                vs[lang] = vs[lang].replace(old, new)
            report['new_bound'][rid] = len(r['proof_bindings'])
            extra = ['bound']
        for ref in r.get('references', []):
            path = ref.get('path')
            if not path or 'sha256' not in ref or not (ROOT / path).is_file():
                continue
            if sha(path) != ref['sha256']:
                if path in FILES:
                    ref['sha256'] = sha(path)
                    touched.append(path)
                else:
                    report['unhandled_drift'].append([rid, path])
        for b in r.get('proof_bindings', []):
            src = b.get('source')
            if not src or not (ROOT / src).is_file():
                continue
            cur = sha(src)
            if pointer(receipt(b['receipt']), b['sha256_pointer']) == cur:
                continue
            if pointer(run, b['sha256_pointer']) == cur:
                b['receipt'] = core
                rebound = True
                if src not in touched:
                    touched.append(src)
            else:
                report['unbound'].append([rid, src, b['receipt']])
        if rebound and not any(x.get('path') == core for x in r['references']):
            r['references'].append({'path': core, 'role': 'receipt', 'sha256': sha(core), 'declarations': []})
        if not touched and not rebound and not extra:
            continue
        zh = [f'{t.rsplit("/", 1)[-1]}（{FILES[t][0]}）' if t in FILES else t.rsplit('/', 1)[-1] for t in touched]
        en = [f'{t.rsplit("/", 1)[-1]} ({FILES[t][1]})' if t in FILES else t.rsplit('/', 1)[-1] for t in touched]
        if rid in NEW or rid in EDITED:
            prefix = OWN_ZH if rid in NEW else OWN_EN
            note = r['history'][-1]
            assert note['zh'].startswith(prefix[0]) and note['en'].startswith(prefix[1]), (rid, note['en'][:60])
            if rid in NEW:
                note['zh'] += f'10月15日落地时绑定核心回执 {utc}' + ('，并更新哈希：' + '；'.join(zh) if zh else '') + '。'
                note['en'] += f' At landing on 15 October, bound to the core receipt {utc}' + ('; rehashed: ' + '; '.join(en) if en else '') + '.'
            elif zh:
                note['zh'] += '10月15日落地时更新哈希：' + '；'.join(zh) + '。'
                note['en'] += ' At landing on 15 October, rehashed: ' + '; '.join(en) + '.'
        else:
            tail_zh, tail_en = STANDS.get(rid, ('', ''))
            r.setdefault('history', []).append({'zh': NOTE_ZH + DID[rebound][0] + '；'.join(zh) + tail_zh + '。',
                                                'en': NOTE_EN + DID[rebound][1] + '; '.join(en) + tail_en + '.'})
        report['changed'].append([rid, [t.rsplit('/', 1)[-1] for t in touched], rebound])
        if write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'changed': len(report['changed']), 'new_bound': report['new_bound'],
                      'unhandled_drift': report['unhandled_drift'], 'unbound': report['unbound']}, ensure_ascii=False, indent=1))
    if '--list' in sys.argv:
        for x in report['changed']:
            print(x)


if __name__ == '__main__':
    main()
