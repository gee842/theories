#!/usr/bin/env python3
"""Re-point RO's passage map and chapter to SC's laws (board item SC; run from anywhere, after apply_text.py):
  python3 -B patch_ro.py
For the four passages of RO's second gap (同则同之, 名无固宜, the 說文's 止戈 gloss, 书同文): the passage map changes only
through build_passages.py's FIXES, which a rebuild would otherwise overwrite. So this adds one FIXES entry per passage
(declarations of Becoming.SharedCodes and the record a-code-formed-between-formations added, the sentence of each reading
that named the gap replaced in both languages, the gap marked closed with its statement kept), merging into the entry
the 說文 gloss already has (its fragments fix) and appending the others before FIXES's closing brace; adds the
reading_en_sub key to the build where it is missing; rebuilds passages.json and checks that only these four passages
changed. Then rewrites the chapter's passage tables for the traditions touched (verify_ro.py --table), marks the gap's
row in §8 closed (in its "what is missing" cell, as Y5 marks its row) and adds a paragraph after the table, and corrects
§5.4 (which said the spine had no such law) and §11 (the open gaps, as RO or Y5 left the line). Each edit must match
exactly once. Run before make_record.py (whose record binds the chapter and the map as patched); reland.sh runs
verify_ro.py after the record exists."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RO = HERE.parent / 'ro-relational-sources'
ROOT = HERE.parents[5]
PASSAGES = RO / 'passages.json'
CHAPTER = ROOT / 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
RID = 'a-code-formed-between-formations'
STUDY = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
sys.path.insert(0, str(RO))
import verify_ro as V  # noqa: E402

section = re.search(r'^## (\d+)\. A code formed between formations \(SC\)$', STUDY.read_text(), re.M)
assert section, 'study section missing'
N = int(section.group(1))


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


def sc(*names):
    return ['Becoming.SharedCodes.' + n for n in names]


EDITS = {
    'xunzi-tong-ze-tong-zhi': dict(
        declarations=sc('run_held', 'kept_iff', 'run_agrees_every_start_iff', 'reads_iff', 'run_renamed',
                        'never_agrees_of_both', 'TwoFormations.three_agree'),
        zh=('“约定俗成”是编码在使用者之间形成并保持；脊柱只有单向取得（给定编码、教师）与已装入编码在信道变化下的保持（References.stays_iff），'
            '没有编码在使用者关系中形成的律（见缺口）。结构相合，缺约定一环。',
            '“约定俗成”是编码在使用者之间形成并保持（SharedCodes）：听取不造新形（run_held），一组在某义上的相合恰经对它封闭的听取而保持'
            '（kept_iff）；所成之形由起点与听取次序固定，一个次序恰在给每个形成同一来源时从每个起点都形成相合（run_agrees_every_start_iff）；'
            '形成之间恰在编码相合处互读其别（reads_iff，References.stays_iff 的形成之间形式）。不特许任何形式（run_renamed），而既不特许'
            '形式也不特许形成者的律永不使对称的分歧相合（never_agrees_of_both）：约定之成要打破一个对称，中心、偏好之形与听取次序各是一途'
            '（TwoFormations.three_agree），约定俗成是次序一途。结构相合，约定一环已补上。'),
        en=('what the spine lacks is the code formed between users (约定俗成).',
            'the code formed between users (约定俗成) is now SharedCodes: hearing makes no form, agreement is kept exactly '
            'through closed hearings, the start and the order fix the form, users read each other where codes agree, '
            'and a law privileging neither form nor user never settles a symmetric disagreement, so convention breaks a '
            'symmetry by the order of use.')),
    'ru-xunzi-ming-wu-gu-yi': dict(
        declarations=sc('run_renamed_tells_apart_iff', 'renamed_carries_iff', 'never_agrees_of_both',
                        'TwoFormations.three_agree', 'follow_agrees_iff', 'Path.never_agree'),
        zh=('剩余：荀子接着说“其民莫敢托为奇辞以乱正名”，由王者制名并禁止乱名，把约定的形成交给单一中心；而约定在众多使用者之间如何形成、如何'
            '保持，脊柱没有定理（见 gap）。',
            '荀子接着说“其民莫敢托为奇辞以乱正名”，由王者制名并禁止乱名，把约定的形成交给单一中心。SharedCodes 给出两者的关系：改名不改变编码'
            '所分别者，也不改变它是否承载规律（run_renamed_tells_apart_iff、renamed_carries_iff）；既不特许形式也不特许形成者的律永不使对称的'
            '分歧相合（never_agrees_of_both），中心、偏好之形与听取次序各打破一个对称而在一步内相合（TwoFormations.three_agree）：王者制名'
            '是中心一途，约定俗成是次序一途。缺口原拟的陈述（各取其所耦合者中最小编号者之码，恰在每个耦合闭包为全体时静止为同）不成立：在路 '
            'a–c–b 上两端各为其耦合中最小者，永不相合（Path.never_agree）；指针律之下相合恰是指针之路相遇（follow_agrees_iff）。'),
        en=('how a shared naming forms among many users, which Xunzi hands to the king, has no law on the spine.',
            'how a shared naming forms among many users, which Xunzi hands to the king, is SharedCodes: renaming changes '
            'neither what a code tells apart nor what it carries, and a law privileging neither name nor user never '
            'settles a symmetric disagreement, so a centre (the king), a preferred form or the order of use must break '
            'the symmetry; the gap\'s coupling-closure form is false (Path.never_agree).')),
    'shuowen-wu-zhi-ge-gloss': dict(
        declarations=sc('written_rests', 'resolved_alike_merged', 'no_reading_recovers', 'omitted_rest', 'kept_bars',
                        'added_never_replaced', 'Gloss.taken_up_locks', 'Gloss.uptake_loses'),
        zh=('没有断言：律不判楚庄王之规范读法无价值，只判它不是字源。',
            '写回（SharedCodes）：读法一旦写入后人所读的记录，自下一代起即静止并自我确认（written_rests、Gloss.taken_up_locks）；判定相同的'
            '历史被合并，后来的记录读不回此前（resolved_alike_merged、no_reading_recovers）；遗漏之下所静止者不是此前记录所判定之义'
            '（omitted_rest）。只有保留下来的此前记录阻止另一种判定（kept_bars），只增补的记录使判定失去而不被替换（added_never_replaced、'
            'Gloss.uptake_loses）：止为足之读仍可读，靠的是甲骨金文这些保留下来的此前记录。没有断言：律不判楚庄王之规范读法无价值，只判它不是'
            '字源。'),
        en=('and keeps both readings indexed by context since they do not glue.',
            'and keeps both readings indexed by context since they do not glue; written back into the records later '
            'readers learn from, the reading rests at once and confirms itself, and only records kept from before (the '
            'bone and bronze forms) bar it (SharedCodes: written_rests, kept_bars, added_never_replaced).')),
    'shuowen-xu-shu-tong-wen': dict(
        declarations=sc('run_from_imposition', 'source_loses_nothing', 'run_imposed_stays', 'outside_needed',
                        'outside_returns'),
        zh=('与“约定俗成”所说在使用者之间形成的约定不同（见荀子正名条目的缺口）。',
            '与“约定俗成”所说在使用者之间形成的约定不同。SharedCodes 给出强加编码的确切律：强加使所有人在每一义上相合，每个形成恰失去其编码所分'
            '而强加编码所合并者，被强加其编码的形成一无所失（run_from_imposition、source_loses_nothing）；此后在任何听取次序与规则下强加编码'
            '保持（run_imposed_stays），被合并的分别只从强加之外保留的形式回来（outside_needed），从这样的形式则一步即回（outside_returns）。'
            '“古文由此絕”是外面再无保留旧形之处。'),
        en=('unlike a convention formed among users.',
            'unlike a convention formed among users; its loss stays under every later exchange and comes back only from a '
            'form kept outside the imposition (SharedCodes: run_from_imposition, outside_needed).')),
}

BUILD = RO / 'build_passages.py'
src = BUILD.read_text()
# The build must already add declarations and records and mark gaps closed (Y5's keys).
assert "fix.get('declarations_add', [])" in src and "fix.get('records_add', [])" in src, 'build lacks the add keys'
assert "fix.get('gap_closed')" in src, 'build lacks gap_closed'
if "fix.get('reading_en_sub'" not in src:
    ANCHOR = "            if fix:\n                p['corrected'] = fix['why']\n"
    src = once(src, ANCHOR, "            for old, new in fix.get('reading_en_sub', []):\n"
                            "                if old not in p['reading_en']:\n"
                            "                    problems.append(f'{pid}: English reading correction does not apply: {old}')\n"
                            "                p['reading_en'] = p['reading_en'].replace(old, new)\n" + ANCHOR)
assert 'SharedCodes' not in src, 'SC entries already in FIXES'


def lit(s, indent):
    """A Python string literal, split into adjacent literals of at most 100 characters, after a space or a mark."""
    parts, i = [], 0
    while len(s) - i > 100:
        cut = max(s.rfind(c, i + 40, i + 100) for c in ' ，；、。）')
        cut = cut + 1 if cut > 0 else i + 100
        parts.append(s[i:cut])
        i = cut
    parts.append(s[i:])
    if len(parts) == 1:
        return repr(parts[0])
    return '(' + ('\n' + ' ' * (indent + 1)).join(repr(x) for x in parts) + ')'


def entry_text(pid, fix):
    lines = [f'    {pid!r}: {{']
    for k, v in fix.items():
        head = f'        {k!r}: '
        if isinstance(v, str):
            lines.append(head + lit(v, len(head)) + ',')
        elif k in ('reading_sub', 'reading_en_sub'):
            pairs = []
            for old, new in v:
                pad = len(head) + 2
                pairs.append('(' + lit(old, pad) + ',\n' + ' ' * pad + lit(new, pad) + ')')
            lines.append(head + '[' + (',\n' + ' ' * (len(head) + 1)).join(pairs) + '],')
        else:
            lines.append(head + '[' + (',\n' + ' ' * (len(head) + 1)).join(repr(x) for x in v) + '],')
    lines[-1] = lines[-1][:-1] + '},'
    return '\n'.join(lines) + '\n'


GAP = (f'SC (Becoming.SharedCodes, record {RID}, study section {N}); the statement above is kept as proposed, and '
       'where the laws differ from it the record and the study section say so (the coupling-closure form proposed for '
       '名无固宜 is false, Path.never_agree).')
before = {p['id']: p for p in json.loads(PASSAGES.read_text())['passages']}
assert len([i for i in EDITS if i in before]) == len(EDITS)
sys.path.insert(0, str(RO))
ns = {'__file__': str(BUILD), '__name__': 'build_passages'}
exec(compile(src[:src.index('\n\ndef tradition(')], str(BUILD), 'exec'), ns)
FIXES = ns['FIXES']
for pid, e in EDITS.items():
    fix = {'declarations_add': e['declarations'], 'records_add': [RID],
           'reading_sub': [e['zh']], 'reading_en_sub': [e['en']]}
    if 'gap' in before[pid]:
        fix['gap_closed'] = GAP
    why = ('SC: Becoming.SharedCodes proved the code formed between formations the reading named as a gap; its laws '
           'and record added and the sentence that named the gap replaced (both languages)')
    if pid in FIXES:
        # Merge into the entry already there (one key per passage; a second key would drop the first).
        old = FIXES[pid]
        assert not set(old) & set(fix), (pid, set(old) & set(fix))
        merged = {k: v for k, v in old.items() if k != 'why'}
        merged.update(fix)
        merged['why'] = old['why'] + '; ' + why
        i = src.index(f'    {pid!r}: {{')
        j = src.index('},\n', i) + 3
        src = src[:i] + entry_text(pid, merged) + src[j:]
    else:
        CLOSE = '\n}\n\n\ndef tradition('
        src = once(src, CLOSE, '\n' + entry_text(pid, dict(fix, why=why)).rstrip('\n') + CLOSE)
ns = {'__file__': str(BUILD), '__name__': 'build_passages'}
exec(compile(src[:src.index('\n\ndef tradition(')], str(BUILD), 'exec'), ns)
for pid in EDITS:
    assert all(ns['FIXES'][pid][k] == v for k, v in FIXES.get(pid, {}).items() if k != 'why'), pid
    assert ns['FIXES'][pid]['records_add'] == [RID], pid
assert set(ns['FIXES']) == set(FIXES) | set(EDITS)
assert all(ns['FIXES'][k] == FIXES[k] for k in FIXES if k not in EDITS)
BUILD.write_text(src)
import subprocess  # noqa: E402
r = subprocess.run([sys.executable, '-B', str(BUILD)], capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
data = json.loads(PASSAGES.read_text())
after = {p['id']: p for p in data['passages']}
assert set(after) == set(before)
changed = sorted(i for i in after if after[i] != before[i])
assert changed == sorted(EDITS), ('the rebuild changed other passages', changed)
for pid, e in EDITS.items():
    p = after[pid]
    assert p['declarations'][-len(e['declarations']):] == e['declarations'] and p['records'][-1] == RID, pid
    assert e['zh'][1] in p['reading'] and e['en'][1] in p['reading_en'], pid
    assert ('gap' not in p) or p['gap'].get('closed') == GAP, pid
touched = {after[pid]['tradition'] for pid in EDITS}

chapter = CHAPTER.read_text()
for t in sorted(touched):
    b, e = V.begin(t), V.end(t)
    i, j = chapter.index(b) + len(b), chapter.index(e)
    chapter = chapter[:i] + '\n' + V.table(data['passages'], t) + '\n' + chapter[j:]
MODULE = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/SharedCodes.lean'
# §8: the row's "what is missing" cell says the gap is closed, as Y5 marks its row.
chapter = once(chapter, '| 只有单向的取得（给定编码、教师）与装入编码的保持；没有在关系中形成的编码 |',
               f'| 已由 SC 补上（[`Becoming.SharedCodes`]({MODULE})，记录 [{RID}](../results/records/{RID}.md)）；'
               '此前只有单向的取得（给定编码、教师）与装入编码的保持 |')
# §5.4 said the spine had no law of how such a code forms.
chapter = once(chapter, '受控的单字术语因而只能是约定，即在理论的使用者之间形成的一份编码，而脊柱尚无此种编码怎样形成的律（§8）。',
               '受控的单字术语因而只能是约定，即在理论的使用者之间形成的一份编码；这种编码怎样形成、怎样保持，由 `SharedCodes` '
               '给出（§8）：约定之成要打破一个对称，形成后只经对它封闭的听取而保持（`never_agrees_of_both`、`kept_iff`）。')
# §11: the open gaps (the line as RO left it, or as Y5 left it when Y5 lands first).
ELEVEN = {
    '- §8 的七项缺口，各待认领与写成 Lean。':
        '- §8 的七项缺口中，第二项（在形成之间形成的编码）已由 SC 写成；其余六项各待认领与写成 Lean。',
    '- §8 的前六项缺口，各待写成 Lean（已认领者见工作板）；第七项（卦的世界的补充）已由 Y5 写成。':
        '- §8 的第一、三、四、五、六项缺口，各待写成 Lean（已认领者见工作板）；第二项（在形成之间形成的编码）已由 SC 写成，'
        '第七项（卦的世界的补充）已由 Y5 写成。',
}
found = [k for k in ELEVEN if chapter.count(k) == 1]
assert len(found) == 1, ('§11 line not found in a known form', found)
chapter = chapter.replace(found[0], ELEVEN[found[0]])
TABLE_END = '\n\n另有两项已在映射期间由别处完成，或交给别处：'
chapter = once(chapter, TABLE_END, f'''

第二项已由看板项 SC 补上（`Becoming.SharedCodes`，记录 [{RID}](../results/records/{RID}.md)，研究第 {N} 节）。所拟六点都成立，其中几点更确切：相合恰经对一组封闭的听取而保持（`kept_iff`），不是一旦相合即永远；一个次序恰在给每个形成同一来源时从每个起点都形成相合（`run_agrees_every_start_iff`），可成为共有者恰是在用之形（`run_shared_iff_in_use`）；强加的损失在此后每个听取下保持，只从外面保留的形式回来（`run_from_imposition`、`outside_needed`）；写回的读法只为保留的此前记录所阻（`kept_bars`），只增补的记录使判定失去而不被替换（`added_never_replaced`）。另加一律：既不特许形式也不特许形成者的律永不使对称的分歧相合（`never_agrees_of_both`），所以约定之成要打破一个对称，中心、偏好之形与听取次序各是一途（`TwoFormations.three_agree`）。[名无固宜](#p-ru-xunzi-ming-wu-gu-yi)条目所拟的耦合形式不成立：各取其所耦合者中最小编号者之码时，经耦合相连并不保证相合（`Path.never_agree`）。四段的读法已改指向这些律。''' + TABLE_END)
CHAPTER.write_text(chapter)

print('patched', len(EDITS), 'passages;', ', '.join(sorted(touched)))
