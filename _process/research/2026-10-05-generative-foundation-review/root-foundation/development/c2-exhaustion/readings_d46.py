#!/usr/bin/env python3
"""C2 follow-up, 19 October 2026: decide C2's readings in the one account (D45), since no reading waits on Ren any
longer, readings of his own terms included. Adds D46 to DELEGATED-CHOICES (en, zh), corrects study section 186 and the
record where-a-rising-take-ends, which said the readings wait on Ren, then re-points the other records citing the
changed files after reading the change. usage (from the repository root): python3 -B readings_d46.py BASE"""
import glob, hashlib, json, subprocess, sys
from pathlib import Path

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
REC = 'theories/becoming/results/records/where-a-rising-take-ends.json'
SEC = 186
ANCHOR = f'{SEC}-where-a-take-more-than-now-ends-c2'
WORDS = '“integrate all, the theory is a whole, not stitched pieces, go ahead”'


def edit(path, pairs):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        assert text.count(old) == 1, (path, old[:80], text.count(old))
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path)


D46_EN = (
    '<a id="d46-多于此刻的取用终于何处--where-a-rising-take-ends"></a>\n'
    '### Where a rising take ends\n\n'
    f'Where: chapter §6.7, “Where a take more than now ends”, and the exhaustion bullet of the seeking passage; the record '
    f'[where-a-rising-take-ends](../../../../theories/becoming/results/records/where-a-rising-take-ends.md); study section '
    f'{SEC} ([C2](BECOMING-RENEWAL-READING.md#{ANCHOR})). Decided in the one account of D45, where the readings of Ren\'s '
    'own terms no longer wait on him.\n\n'
    '**Decision.** Adopted with exact scope, in D45\'s links of knowing and of continuation. (1) **Exhaustion ends the '
    'seeker.** B2 of 无明 (D26, as revised in D45) is extended. Where the seeking is a take more than now from a condition '
    'given within a bound, exhaustion ends the seeker itself, not only its rises, under balance alone '
    '(`Flow.seeking_ends`). Where renewal depends on what it renews, it also ends every formation depending on the '
    'condition at the need the level falls below (`Flow.seeking_exhausts`). Seeking locked onto a target that cannot '
    'rest, pursued as taking, carries its own ending. (2) **Taking all, as a stage.** Taking all that is given forms, in '
    'one way, as a stage of such a rise, and it is not where the course rests. The full taker of D44 that continues is '
    'one whose take does not keep rising (`Alone.takes_all`). (3) **Not a case of the meta-attractor.** Here the rise is '
    'supplied. The meta-attractor\'s step, winning that buys more power to win (B5, `Becoming.Capture`), would derive the '
    'rise from what taking gains, and that law is open (the next step of target-capture: taking more yields more). So '
    'D44\'s (c) stands, its reason narrowed from “how taking all forms” to “how a take comes to rise from what it '
    'gains”.\n'
    '**Reasons.** (1) and (2) are the theorems read with D26 and D44. (3) keeps the term\'s sense: Ren\'s texts and '
    '`Becoming.Capture` read the meta-attractor as a selection by winning, which this law does not state.\n'
    '**What would change it.** A law deriving a rising take from what taking gains; takes that rise at some steps only; '
    'giving that grows with the take.\n')

D46_ZH = (
    '<a id="d46-多于此刻的取用终于何处--where-a-rising-take-ends"></a>\n'
    '### D46. 多于此刻的取用终于何处\n\n'
    f'所在：理论第 6.7 节“Where a take more than now ends”一条与寻求一段的耗尽一条；[where-a-rising-take-ends]'
    f'(../../../../theories/becoming/results/records/where-a-rising-take-ends.md) 的读法；研究第 {SEC} 节。在 D45 的一个说明中决定，'
    'Ren 自己用语的读法不再等待他。\n\n'
    '**决定。** 以确切范围采用，在 D45 的知与延续两环之中。一、**耗尽终结寻求者。** 无明的 B2（D26，经 D45 修订）扩展：寻求是对所给'
    '有界的条件的多于此刻的取用之处，耗尽终结寻求者本身，不只是其上升，仅在平衡之下（`Flow.seeking_ends`）。更新依存于所更新者之处，'
    '它也终结每个在水平落到其下的需要处依存于该条件的形成（`Flow.seeking_exhausts`）。锁定于不能静止之目标的寻求，作为取用而追求时，'
    '自带其终结。二、**取尽所给作为一个阶段。** 取尽所给的一种形成方式是这样一次上升的一个阶段，而不是进程静止之处。D44 中持续的取尽者，'
    '是取用不再上升者（`Alone.takes_all`）。三、**不是元吸引子的情形。** 这里上升是提供的。元吸引子之步，即赢得购得更多赢的能力'
    '（B5，`Becoming.Capture`），会从取用之所得推出上升，而那一定律仍开放（target-capture 的下一步：取用更多带来更多）。所以 D44 的'
    '（c）成立，其理由从“取尽所给如何形成”收窄为“取用如何从其所得开始上升”。\n'
    '**理由。** 一与二是与 D26、D44 一同读的定理。三保持该用语之义：Ren 的文本与 `Becoming.Capture` 把元吸引子读作由赢而来的选择，'
    '这一定律没有陈述它。\n'
    '**会改变它的。** 从取用之所得推出上升之取用的定律；只在某些步上升的取用；随取用增长的给予。\n')


def decisions():
    en = RF + 'DELEGATED-CHOICES.md'
    zh = RF + 'DELEGATED-CHOICES.zh.md'
    t_en = Path(en).read_text(encoding='utf-8')
    row45 = next(line for line in t_en.split('\n') if line.startswith('| D45 | '))
    lin = '<a id="13-一个说明--one-account"></a>\n'
    edit(en, [(row45 + '\n', row45 + '\n| D46 | where a rising take ends (19 October) | adopted with exact scope: exhaustion '
                                'ends the seeker (B2 extended); taking all as a stage of a rise; not a case of the '
                                'meta-attractor |\n'),
              (lin, f'- Ren\'s answer of 19 October 2026, {WORDS}, read with D45 as deciding the readings C2 had left to him: '
                    f'D46 ([study section {SEC}](BECOMING-RENEWAL-READING.md#{ANCHOR})).\n\n' + lin)])
    t = Path(en).read_text(encoding='utf-8')
    Path(en).write_text(t.rstrip('\n') + '\n\n' + D46_EN, encoding='utf-8')
    t_zh = Path(zh).read_text(encoding='utf-8')
    row45z = next(line for line in t_zh.split('\n') if line.startswith('| D45 | '))
    edit(zh, [(row45z + '\n', row45z + '\n| D46 | 多于此刻的取用终于何处（10-19） | 以确切范围采用：耗尽终结寻求者（B2 扩展）；取尽所给作为'
                                  '上升的一个阶段；不是元吸引子的情形 |\n'),
              (lin, f'- Ren 2026-10-19 的回答，{WORDS}，与 D45 一同读作决定 C2 留给他的读法：D46（研究第 {SEC} 节）。\n\n' + lin)])
    t = Path(zh).read_text(encoding='utf-8')
    Path(zh).write_text(t.rstrip('\n') + '\n\n' + D46_ZH, encoding='utf-8')
    print('D46 added')


def study():
    edit(STUDY, [
        ('Boundary: takes that rise only at some steps; unbounded giving; how a take comes to rise (what it gains); the\n'
         '          readings of 无明 and of the meta-attractor, which wait on Ren\n',
         'Boundary: takes that rise only at some steps; unbounded giving; how a take comes to rise (what it gains), which\n'
         '          a case of the meta-attractor would need (D46)\n'),
        ('**Readings that wait on Ren.** Whether this is the boundary of 无明 reached by the seeker itself (B2 of '
         '`Becoming.Seeking`, D26), and whether a take more than now that ends the renewal is a case of the '
         'meta-attractor, read Ren\'s own terms. D44 declined (c), reading taking all as a case of the meta-attractor, in '
         'part because it needed a law of how taking all forms. This item supplies one such law; the reading stays with '
         'Ren.',
         f'**Reading (D46, AI reading).** When this section was written it said these readings wait on Ren. Since his '
         f'answer of 19 October, {WORDS}, no reading waits on him (D45), and D46 decides them in the one account. B2 of '
         '无明 is extended: where the seeking is a take more than now from a bounded giving, exhaustion ends the seeker '
         'itself. Taking all that is given is, in one way, a stage of a rise, not where the course rests. The item is '
         'not read as a case of the meta-attractor, since the rise is supplied, not derived from what taking gains; '
         'D44\'s (c) stands with that narrowed reason.'),
    ])


def record():
    p = Path(REC)
    d = json.loads(p.read_text())
    before = dict(d['next_delta'])
    dns = d['does_not_show'][2]
    assert dns['en'].startswith('A reading of the seeker'), dns
    d['does_not_show'][2] = {
        'en': 'That the rising take is a case of the meta-attractor: the rise is supplied here, not derived from what '
              'taking gains (D46).',
        'zh': '上升的取用是元吸引子的情形：这里上升是提供的，不是由取用之所得推出（D46）。',
        'kind': 'scope'}
    old_en = 'the readings of 无明 and of the meta-attractor, with Ren;'
    old_zh = '无明与元吸引子的读法，待 Ren；'
    assert d['next_delta']['en'].count(old_en) == 1 and d['next_delta']['zh'].count(old_zh) == 1
    d['next_delta'] = {'en': d['next_delta']['en'].replace(old_en, 'a rising take derived from what taking gains (D46);'),
                       'zh': d['next_delta']['zh'].replace(old_zh, '由取用之所得推出的上升之取用（D46）；')}
    d['correspondence']['en'] += ' The reading is D46 of DELEGATED-CHOICES.'
    d['correspondence']['zh'] += '读法是 DELEGATED-CHOICES 的 D46。'
    d['history'].append({
        'en': '19 October 2026, C2 follow-up: the record said the readings of 无明 and of the meta-attractor wait on Ren; '
              f'since his answer {WORDS} no reading waits on him (D45), so D46 decides them (exhaustion ends the seeker, '
              'B2 extended; not a case of the meta-attractor, the rise being supplied). One item of does_not_show and the '
              f'next step changed; before: "{before["en"]}". The claim is unchanged.',
        'zh': '2026年10月19日，C2 后续：本记录曾说无明与元吸引子的读法待 Ren；自他的回答起不再有读法等待他（D45），所以由 D46 决定'
              '（耗尽终结寻求者，B2 扩展；不是元吸引子的情形，上升是提供的）。“未表明”的一项与下一步改变；原文见英文。论断不变。'})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('edited', REC)


WHAT = {
    'BECOMING-RENEWAL-READING.md': 'section 186 (C2) now states its readings as D46 rather than waiting on Ren',
    'DELEGATED-CHOICES.md': 'D46 added (index row, lineage, decision)',
    'DELEGATED-CHOICES.zh.md': 'D46 added (index row, lineage, decision)',
    'where-a-rising-take-ends.json': 'one item of does_not_show and the next step now name D46',
}


def rehash(base):
    changed = set(subprocess.run(['git', 'diff', '--name-only', base], capture_output=True, text=True).stdout.split())
    h = lambda q: hashlib.sha256(open(q, 'rb').read()).hexdigest()
    at_base = {q: hashlib.sha256(subprocess.run(['git', 'show', base + ':' + q], capture_output=True).stdout).hexdigest()
               for q in changed}
    n = 0
    for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
        d = json.load(open(f))
        files = []
        for r in d.get('references', []):
            if r.get('path') in changed and r.get('sha256') == at_base[r['path']] != h(r['path']):
                r['sha256'] = h(r['path'])
                files.append(r['path'].rsplit('/', 1)[-1])
        if not files:
            continue
        files = sorted(set(files))
        assert all(x in WHAT for x in files), (f, files)
        d['history'].append({
            'en': f'19 October 2026, C2 follow-up (D46): {", ".join(files)} re-pointed after reading the change '
                  f'({"; ".join(x + ": " + WHAT[x] for x in files)}). The claim is unchanged.',
            'zh': f'2026年10月19日，C2 后续（D46）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
        open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        n += 1
        print(f.rsplit('/', 1)[-1], files)
    print(n)


if __name__ == '__main__':
    base = sys.argv[1]
    decisions()
    study()
    record()
    rehash(base)
