#!/usr/bin/env python3
"""M3 (Becoming.PoolResponse) landing edits. Every edit must match exactly once.

usage (from the repository root; M3_ROOT names another checkout to edit, such as a worktree):
  python3 -B apply_text.py package                          copy the module in; import, doc bullet, CORE entry, scope
                                                             sentence, README row
  python3 -B apply_text.py text RECEIPT BASE AFTER APART    study, chapter (sections 3, 7.4, 7.7, 8.2, 9, en; 7.4, 7.7
                                                             zh)
RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence), APART the connectivity check's count of spine theorems apart; the section 9 counts are read from
the receipt itself."""
import json, os, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['M3_ROOT']).resolve() if os.environ.get('M3_ROOT') else HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
MODULE = 'Becoming.PoolResponse'
THEOREMS, DECLARATIONS = 18, 21


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, len(pairs))


DOC_AFTER = ('  beyond the closure and separates the two through every pool holding it. In `Clearing`, pooling\n'
             '  with the dweller closes the clearer\'s gap.\n')
DOC = (
    '* `Becoming.PoolResponse` (L4): what a pool\'s acts respond to. Where a law of exchange reads\n'
    '  through the coupling of each formation outside a part, a selection through the acts of a group\n'
    '  outside it is a selection through the group\'s pooled coupling, and what the pool\'s acts\n'
    '  separate some member couples apart, the members listed and decided. The bound is exact where\n'
    '  the coupling classes are decided, and it does not fix response: the law exchanging nothing\n'
    '  reads through every coupling. Under the conditions of the gap for a pool\'s act, nothing within\n'
    '  the pool\'s coupling closure outside the acting part responds to the act; with both acts laws,\n'
    '  nothing is supplied. A pool meets a part\'s responsive reach exactly where the part meets the\n'
    '  pool\'s closure, a pool beyond that reach does not respond, and no member responds before a\n'
    '  difference has entered what it couples into. In `Clearing` what every pool holding the dweller\n'
    '  separates goes unresponded outside the clearer\'s part; in `Loop` a response returns through the\n'
    '  actor\'s coupling closure.\n')
SCOPE_AFTER = '    "pool holding it; in Clearing, pooling with the dweller closes the clearer\'s gap. "\n'
SCOPE = (
    '    "PoolResponse: where a law of exchange reads through the coupling of each formation outside "\n'
    '    "a part, a selection through the acts of a group outside it is a selection through its pooled "\n'
    '    "coupling, and what the acts separate some member couples apart, the members listed and "\n'
    '    "decided; with the coupling classes decided the bound is exact, and the law exchanging nothing "\n'
    '    "shows that coupling does not fix response; under the conditions of the gap for a pool\'s act, "\n'
    '    "nothing within the pool\'s coupling closure outside the acting part responds to the act; a "\n'
    '    "pool meets a part\'s responsive reach exactly where the part meets its closure, a pool beyond "\n'
    '    "the reach does not respond, and no member responds before a difference enters what it "\n'
    '    "couples into; in Clearing what a pool separates goes unresponded outside the clearer\'s part, "\n'
    '    "and in Loop a response returns through the actor\'s coupling closure. "\n')
README_ROW = (
    '| L4 | [`Becoming.PoolResponse`](Becoming/PoolResponse.lean) | what a pool\'s acts respond to (no axiom; the law '
    'each member follows, that it reads through coupling, balance, the timing premises, and for exactness the coupling '
    'classes decided and a condition, are hypotheses of the theorems): a selection through a group\'s acts under a law '
    'reading through coupling is a selection through its pooled coupling (`ExchangeLaw.SelectsThroughActs`, '
    '`ExchangeLaw.Through.selectsThroughAll`); a member acting differently couples apart '
    '(`ExchangeLaw.Through.apart_of_acts`), and what the acts separate some member couples apart, the members listed '
    'and decided (`ExchangeLaw.Through.acts_separate_member`); the bound is exact (`ExchangeLaw.ofClass`, '
    '`ExchangeLaw.acts_alike_all_iff`) and does not fix response (`ExchangeLaw.zero`, '
    '`ExchangeLaw.response_not_fixed_by_coupling`); the gap for a pool\'s response (`Flow.response_alike_pool`, '
    '`Flow.act_unselected_by_acts_pool`, `act_courses_response_alike_pool`); a pool meets a part\'s responsive reach '
    'exactly where the part meets its closure (`Flow.pool_within_response_iff`), and a pool beyond the reach does not '
    'respond (`Flow.pool_alike_beyond_response`); no response before the difference arrives '
    '(`TimedResponse.pool_alike_before`); in `Clearing`, separated and not responded (`Clearing.separated_unresponded`); '
    'in `Loop`, a response returns through the actor\'s coupling closure (`Loop.response_returns`) '
    '([what-a-pools-acts-respond-to](../../../../../../theories/becoming/results/records/'
    'what-a-pools-acts-respond-to.md)) |')


def package():
    shutil.copyfile(HERE / 'Becoming/PoolResponse.lean', ROOT / PKG / 'Becoming/PoolResponse.lean')
    print('copied Becoming/PoolResponse.lean')
    edit(f'{PKG}/Becoming.lean', [
        ('import Becoming.SelectionPool\n', 'import Becoming.SelectionPool\nimport Becoming.PoolResponse\n'),
        (DOC_AFTER, DOC_AFTER + DOC),
    ])
    edit(f'{PKG}/check_becoming.py', [
        ('"Becoming.SelectionPool", ', '"Becoming.SelectionPool", "Becoming.PoolResponse", '),
        (SCOPE_AFTER, SCOPE_AFTER + SCOPE),
    ])
    readme = f'{PKG}/README.md'
    text = (ROOT / readme).read_text(encoding='utf-8')
    row = next(line for line in text.split('\n') if line.startswith('| L4 | [`Becoming.SelectionPool`]'))
    edit(readme, [(row + '\n', row + '\n' + README_ROW + '\n')])


CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER_ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
SR = '../../../' + STUDY
MOD = f'../../../{PKG}/Becoming/PoolResponse.lean'
REC = '../results/records/what-a-pools-acts-respond-to.md'
RECLINK = f'[what-a-pools-acts-respond-to]({REC})'
M2LINK = '[what-pooled-coupling-reaches](../results/records/what-pooled-coupling-reaches.md)'


def receipt_counts(rid):
    d = json.loads((ROOT / PKG / 'becoming-checks' / rid / 'verification.json').read_text())
    assert d['status'] == 'passed', d['status']
    mods = {m['module']: m for m in d['modules']}
    th = lambda names: sum(int(mods[n]['theorems']) for n in names)
    return {
        'core': (len(d['core_modules']), th(d['core_modules'])),
        'foundation': (len(d['foundation_modules']), th(d['foundation_modules'])),
        'closure': (len(d['core_closure']), th(d['core_closure'])),
        'bridge': (len(d['bridge_modules']), th(d['bridge_modules'])),
        'spine': th(d['spine_modules']),
        'audited': sum(len(mods[n]['declarations']) for n in d['spine_modules']),
        'pj': (len(d['periphery_join_modules']), th(d['periphery_join_modules'])),
        'inherited': len(d['inherited_receipts']),
        'compile': len(d['compile_order']),
        'injeq': (len(d['generated_axiom_dependencies']), len(d['bridge_generated_axiom_dependencies'])),
        'own': int(mods[MODULE]['theorems']),
        'ran': len(d['lean_steps']['ran']),
        'reused': len(d['lean_steps']['reused']),
        'own_decls': len(mods[MODULE]['declarations']),
    }


def n(x):
    return f'{x:,}'


def subn1(pattern, repl, text, what):
    text, k = re.subn(pattern, repl, text)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


def replace_once(text, old, new, what):
    if text.count(old) != 1:
        sys.exit(f'{what}: expected one match, found {text.count(old)}')
    return text.replace(old, new)


def insert_after_line(text, start, new, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0] + 1:idx[0] + 1] = new.split('\n')
    return '\n'.join(lines)


def replace_line(text, start, new, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0]:idx[0] + 1] = new.split('\n')
    return '\n'.join(lines)


# ---------------------------------------------------------------- chapter text, en
SEC3_AFTER = '- *What pooled coupling reaches* ('
SEC3 = (
    '- *What a pool\'s acts respond to* ([Becoming.PoolResponse]({MOD}), {RECLINK}). Where a law of exchange reads '
    'through the coupling of each formation outside a part, what a group outside the part decides by its acts is a '
    'selection through its pooled coupling (`ExchangeLaw.Through.selectsThroughAll`), so the laws above hold of what a '
    'pool does. The bound is exact where the coupling classes are decided (`ExchangeLaw.acts_alike_all_iff`), and '
    'coupling does not fix the response: the law that exchanges nothing reads through every coupling '
    '(`ExchangeLaw.response_not_fixed_by_coupling`). Under the conditions of the gap for a pool\'s act, nothing within '
    'the pool\'s coupling closure outside the acting part responds to the act (`Flow.response_alike_pool`; with both '
    'acts laws, `act_courses_response_alike_pool`). A pool meets a part\'s responsive reach exactly where the part '
    'meets the pool\'s closure (`Flow.pool_within_response_iff`), and no member responds before a difference has '
    'entered what it couples into (`TimedResponse.pool_alike_before`). In `Clearing` what every pool holding the '
    'dweller separates goes unresponded outside the clearer\'s part (`Clearing.separated_unresponded`); in `Loop` a '
    'response returns through the actor\'s coupling closure (`Loop.response_returns`). Stated in §7.4 and §7.7. Study: '
    '[section {SEC}]({SR}#{ANCHOR}).')
S74_DIFF_START = '- **Difference is what a pool adds.** A pool\'s selections are one member\'s exactly when'
S74_NEW = (
    '\n'
    'What a pool\'s acts respond to is proved where its members exchange by a law of exchange, again with neither the '
    'condition of §6.15 nor a practical premise ({RECLINK}).\n'
    '\n'
    '- **A pool\'s acts select through its pooled coupling.** Let a law of exchange read through the coupling of each '
    'formation outside a part, and let a pool\'s members lie outside it. Whatever the pool decides by its acts under the '
    'law up to a step, such as a reward, a vote or a correction it gives, is then a selection through its pooled '
    'coupling (`ExchangeLaw.Through.selectsThroughAll`), so the laws above apply to it with that premise derived. A member '
    'that exchanges differently under two histories couples them apart (`ExchangeLaw.Through.apart_of_acts`); where a '
    'list holds the members and each member\'s coupling is decided, a pool whose acts separate two histories has a '
    'member that couples them apart (`ExchangeLaw.Through.acts_separate_member`). The bound is exact: where each '
    'formation\'s coupling classes are decided and there is a condition to exchange with, the members exchange alike '
    'under two histories across a step by every law reading through coupling exactly when they all couple the two '
    'alike up to that step (`ExchangeLaw.acts_alike_all_iff`).\n'
    '- **Coupling bounds response and does not fix it.** Where a member couples two histories apart and the classes are '
    'decided, some law reading '
    'through every coupling takes differently under them, and the law that exchanges nothing reads through every '
    'coupling too (`ExchangeLaw.response_not_fixed_by_coupling`). In `Clearing`, every pool holding the dweller '
    'separates the cleared and the spared world, and every formation outside the clearer\'s part exchanges alike in the '
    'two (`Clearing.separated_unresponded`).\n'
    '- **The gap for a pool\'s response.** Under the conditions of the gap for a pool\'s act, every formation within the '
    'pool\'s coupling closure and outside the acting part exchanges alike with and without the act at every step '
    '(`Flow.response_alike_pool`); where both acts are laws, nothing is supplied (`act_courses_response_alike_pool`). '
    'Some member of a pool lies within a part\'s responsive reach (§2, “The comparison where the rest responds”) '
    'exactly when some member of the part lies within the pool\'s coupling closure drawn through both flows '
    '(`Flow.pool_within_response_iff`), and where the rest responds through its coupling, a pool beyond that reach '
    'does not respond to the part (`Flow.pool_alike_beyond_response`). Under the conditions of '
    '`TimedResponse.coupling_alike_before`, no member responds before a difference has entered what it couples into '
    '(`TimedResponse.pool_alike_before`).\n'
    '- **A response returns through the actor\'s closure.** In `Loop` the second follows a law reading through its '
    'coupling. It couples the first\'s act apart and takes from the first\'s condition otherwise than without the act, '
    'so it lies within the first\'s coupling closure, and the first is unsupported at the third step with the act and '
    'supported without it (`Loop.response_returns`).')
S74_READING_OLD = (
    '*Reading* [AI reading, open]. Alignment, so read, is neither fitting one party to another\'s preferences nor '
    'fitting all to a fixed common utility. It is pooling couplings across intelligences, so that what any member\'s '
    'acts do beyond its own coupling closure couples into some member of the pool and can be corrected there. The laws '
    'above give the reading its exact part. Pooling moves the gap to the pool\'s coupling closure and does not remove '
    'it: what a pool does jointly beyond that closure is separated only through formations beyond it that couple the '
    'difference apart, such as those whose support the act changes. So a pool of intelligences reaches what its acts '
    'do to formations outside it only through members whose couplings reach that difference. That a separated '
    'difference is then corrected is not proved: selection is not response (§7.7). Members correct one another, and no '
    'member\'s couplings are the pool\'s.')
S74_READING_NEW = (
    '*Reading* [AI reading, open]. Alignment, so read, is neither fitting one party to another\'s preferences nor '
    'fitting all to a fixed common utility. It is pooling couplings across intelligences, so that what any member\'s '
    'acts do beyond its own coupling closure couples into some member of the pool, whose acts can respond to it there. '
    'The laws above give the reading its exact part. Pooling moves the gap to the pool\'s coupling closure and does not '
    'remove it: what a pool does jointly beyond that closure is separated only through formations beyond it that couple '
    'the difference apart, such as those whose support the act changes, and nothing within the closure responds to it. '
    'So a pool of intelligences reaches what its acts do to formations outside it only through members whose couplings '
    'reach that difference, and its acts respond to that difference only through such members. Coupling makes a '
    'response possible and does not make it happen: within the bound, the law each member follows decides. A response '
    'reaches an actor\'s own act only through what the actor\'s coupling closure couples into, and correction and '
    'escalation share that structure, a loop through another\'s coupling and response. Which loops correct is not '
    'proved (§7.7). Members correct one another, if at all, through such loops, and no member\'s couplings are the '
    'pool\'s.')
S77_OLD = (
    '- **Coupling is not compliance.** That a system couples into a consequence does not make its selections respond to '
    'it. How training installs a selection through what it couples into is open, and so is the evidence for an '
    'identified installation (§7.6, §8.7).')
S77_NEW = (
    '- **Coupling is not compliance.** That a system couples into a consequence does not make its selections respond to '
    'it. Where a member\'s law reads through its coupling, coupling bounds what its acts respond to, exactly, and fixes '
    'nothing within the bound (`ExchangeLaw.response_not_fixed_by_coupling`; in `Clearing`, '
    '`Clearing.separated_unresponded`). Which law a system\'s acts follow, how training installs one that responds to '
    'what it couples into, and the evidence for an identified installation are open (§7.6, §8.7).\n'
    '- **Which responses correct.** A response reaches an actor\'s own act only through the actor\'s coupling closure, '
    'and correction and escalation both have that structure (§7.4, `Loop.response_returns`). Which loops correct, '
    'toward what, and members that read one another\'s coupling directly are open (§8.2, “Selection, causes and '
    'experiment”).')
S82_OPEN_OLD = '.) Whether what is drawn beyond is depended on;'
S84_OLD = 'alignment for all as pooled coupling across intelligences; '
S84_NEW = ('alignment for all as pooled coupling across intelligences, whose acts respond to a difference only '
           'through members that couple it apart, with correction and escalation read as one loop through another\'s '
           'coupling and response; ')
S84_ZH_OLD = '为一切的对齐读作跨智能的合起来的耦合；'
S84_ZH_NEW = '为一切的对齐读作跨智能的合起来的耦合，其动作只经把差别耦合得有别的成员回应它，纠正与升级读作同一种经他者耦合与回应的回路；'
S82_OPEN_NEW = ('.) Which responses to what a pool\'s acts separate correct the act, and how a member\'s law comes to '
                'respond to what it couples into; whether what is drawn beyond is depended on;')

# ---------------------------------------------------------------- chapter text, zh
S74_ZH_DIFF_START = '- **差别是一组所加的。** 一组的选择恰是一个成员的选择'
S74_ZH_NEW = (
    '\n'
    '一组的动作回应什么，在其成员按一个交换律交换之处已证明，同样既不用 §6.15 的条件，也不用实践前提（{RECLINK}）。\n'
    '\n'
    '- **一组的动作经其合起来的耦合而选择。** 设一个交换律经一个部分之外每个形成的耦合而读，一组的成员都在这个部分之外。那么这组到'
    '某步为止以其动作在此律下所决定的一切，例如它给出的奖励、表决或纠正，都是经其合起来之耦合的选择'
    '（`ExchangeLaw.Through.selectsThroughAll`），所以上面的规律适用于它，那一前提由推导得出。在两段历史之下交换不同的成员，经其耦合'
    '使它们有别（`ExchangeLaw.Through.apart_of_acts`）；成员由一个列表列出、每个成员的耦合已判定时，其动作分开两段历史的组，有一个'
    '经其耦合使它们有别的成员（`ExchangeLaw.Through.acts_separate_member`）。此界是精确的：每个形成的耦合类已判定、并有一个可交换'
    '的条件时，成员在某步按每个经耦合而读的律对两段历史交换相同，恰当他们到该步为止都把两者耦合得无别'
    '（`ExchangeLaw.acts_alike_all_iff`）。\n'
    '- **耦合界定回应，不确定回应。** 一个成员把两段历史耦合得有别、类已判定时，有一个经每个耦合而读的律对两者取得不同，而什么也不交换的律'
    '也经每个耦合而读（`ExchangeLaw.response_not_fixed_by_coupling`）。`Clearing` 中，每个含有栖居者的组分开清除的与不清除的世界，'
    '而清除者部分之外的每个形成在两者中交换相同（`Clearing.separated_unresponded`）。\n'
    '- **一组之回应的缺口。** 在一组之动作的缺口的条件下，这组耦合闭包之内、行动部分之外的每个形成，在每一步有与无此动作时交换相同'
    '（`Flow.response_alike_pool`）；两个动作都是律时，不另给任何东西（`act_courses_response_alike_pool`）。一组的某个成员在一个'
    '部分的回应所及之内，恰当该部分的某个成员在这组经两条流所取的耦合闭包之内（`Flow.pool_within_response_iff`）；其余经其耦合回应时，'
    '在此所及之外的组不回应该部分（`Flow.pool_alike_beyond_response`）。在 `TimedResponse.coupling_alike_before` 的条件下，差别进入'
    '一个成员所耦合入者之前，该成员不回应（`TimedResponse.pool_alike_before`）。\n'
    '- **回应经行动者的闭包返回。** `Loop` 中，第二者遵从一个经其耦合而读的律。它经其耦合使第一者的动作有别，并从第一者的条件取得'
    '与无此动作时不同，所以它在第一者的耦合闭包之内；有此动作时第一者在第三步不被支持，无此动作时被支持（`Loop.response_returns`）。')
S74_ZH_READING_OLD = (
    '读法（AI 的，开放）：如此读，对齐既不是使一方适合另一方的偏好，也不是使一切适合一个固定的共同效用。它是跨智能地把耦合合起来，'
    '使任何成员的动作在其自身耦合闭包之外所做的，耦合入组中的某个成员，并能在那里被纠正。上面的规律给出这一读法的精确部分。合起来把'
    '缺口移到这组的耦合闭包，并不消除它：一组合起来在这一闭包之外所做的，只经闭包之外、经其耦合使差别有别的形成被分开，例如支持被此'
    '动作改变的形成。所以一组智能及于其动作对组外形成所做的，只经其耦合及于这一差别的成员。被分开的差别随后被纠正，并未证明：选择不是'
    '回应（§7.7）。成员互相纠正，没有哪个成员的耦合就是这组的耦合。')
S74_ZH_READING_NEW = (
    '读法（AI 的，开放）：如此读，对齐既不是使一方适合另一方的偏好，也不是使一切适合一个固定的共同效用。它是跨智能地把耦合合起来，'
    '使任何成员的动作在其自身耦合闭包之外所做的，耦合入组中的某个成员，这组的动作能在那里回应它。上面的规律给出这一读法的精确部分。'
    '合起来把缺口移到这组的耦合闭包，并不消除它：一组合起来在这一闭包之外所做的，只经闭包之外、经其耦合使差别有别的形成被分开，例如'
    '支持被此动作改变的形成；闭包之内无物回应它。所以一组智能及于其动作对组外形成所做的，只经其耦合及于这一差别的成员，它的动作也只经'
    '这样的成员回应这一差别。耦合使回应可能，不使回应发生：在此界之内，由每个成员所遵从的律决定。回应只经行动者耦合闭包所耦合入者及于'
    '其自身的动作；纠正与升级共有这一结构，即经他者的耦合与回应的回路。哪些回路纠正，并未证明（§7.7）。成员若互相纠正，也只经这样的'
    '回路；没有哪个成员的耦合就是这组的耦合。')
S77_ZH_OLD = (
    '- **耦合不是服从。** 系统耦合入一个后果，并不使它的选择回应这个后果。训练怎样装入经其所耦合入者的选择，仍开放；对已识别装置的'
    '证据也是如此（§7.6；§8“经验对应”）。')
S77_ZH_NEW = (
    '- **耦合不是服从。** 系统耦合入一个后果，并不使它的选择回应这个后果。成员的律经其耦合而读时，耦合精确地界定其动作所回应的，'
    '而在此界之内什么也不确定（`ExchangeLaw.response_not_fixed_by_coupling`；`Clearing` 中，`Clearing.separated_unresponded`）。'
    '系统的动作遵从哪个律，训练怎样装入回应其所耦合入者的律，以及对已识别装置的证据，仍开放（§7.6；§8“经验对应”）。\n'
    '- **哪些回应纠正。** 回应只经行动者的耦合闭包及于其自身的动作，纠正与升级都有这一结构（§7.4，`Loop.response_returns`）。'
    '哪些回路纠正、朝向什么，以及成员直接读彼此的耦合，仍开放（§8“进一步的证明”）。')


def text_phase(rid, base, after, apart):
    c = receipt_counts(rid)
    assert (c['own'], c['own_decls']) == (THEOREMS, DECLARATIONS), (c['own'], c['own_decls'])
    spine = n(c['spine'])
    # ------------------------------------------------------------ study
    study = (ROOT / STUDY).read_text(encoding='utf-8')
    sec = max(int(x) for x in re.findall(r'^## (\d+)\. ', study, re.M)) + 1
    body = (HERE / 'study_m3.txt').read_text(encoding='utf-8')
    body = body.replace('{N}', str(sec)).replace('{RECEIPT}', rid).replace('{APART}', apart).replace('{SPINE}', spine)
    assert '{' not in body, 'unfilled placeholder'
    marker = '## Ren’s words quoted in passages that exist only in the Chinese edition'
    assert study.count(marker) == 1
    study = study.replace(marker, body.rstrip('\n') + '\n\n' + marker)
    (ROOT / STUDY).write_text(study, encoding='utf-8')
    print('study section', sec)
    anchor = f'{sec}-what-a-pools-acts-respond-to-m3'
    fill = lambda t: (t.replace('{MOD}', MOD).replace('{RECLINK}', RECLINK).replace('{SEC}', str(sec))
                      .replace('{SR}', SR).replace('{ANCHOR}', anchor))
    # ------------------------------------------------------------ chapter, en
    ch = (ROOT / CHAPTER).read_text(encoding='utf-8')
    ch = insert_after_line(ch, SEC3_AFTER, fill(SEC3), 'section 3 bullet')
    ch = insert_after_line(ch, S74_DIFF_START, fill(S74_NEW), 'section 7.4 bullets')
    ch = replace_once(ch, S74_READING_OLD, S74_READING_NEW, 'section 7.4 reading')
    ch = replace_once(ch, S77_OLD, S77_NEW, 'section 7.7')
    ch = replace_once(ch, S84_OLD, S84_NEW, 'section 8.4 open readings')
    # section 8.2, "Selection, causes and experiment"
    lines = ch.split('\n')
    rows = [i for i, line in enumerate(lines) if line.startswith('| Selection, causes and experiment | (Stated: ')]
    assert len(rows) == 1, rows
    row = lines[rows[0]]
    close = row.index('.)')
    row = row[:close] + '; what a pool\'s acts respond to: `Becoming.PoolResponse`' + row[close:]
    row = replace_once(row, S82_OPEN_OLD, S82_OPEN_NEW, 'section 8.2 open item')
    row = replace_once(row, M2LINK, M2LINK + ', ' + RECLINK, 'section 8.2 record link')
    lines[rows[0]] = row
    ch = '\n'.join(lines)
    # section 9
    ch = subn1(r'finds [\d,]+ of the [\d,]+ spine theorems apart from both base families at the last rerun',
               f'finds {apart} of the {spine} spine theorems apart from both base families at the last rerun', ch,
               'section 9 connectivity')
    ch = subn1(r'\d+ modules counting the root `Becoming`, and \d+ in the core closure with the foundation',
               f'{c["core"][0]} modules counting the root `Becoming`, and {c["closure"][0]} in the core closure with the '
               'foundation', ch, 'section 9 module counts')
    start = ch.index('**The current receipt.**')
    end = ch.index('Further facts about the receipt:', start)
    para = ch[start:end]
    old_rid = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
    para = para.replace(old_rid, rid)
    para = subn1(r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*? in the working tree, and it passed\.',
                 f'It was checked with Lean 4.29.1 on main {base} ({after}) with M3 (`Becoming.PoolResponse`, '
                 f'[study §{sec}]({SR}#{anchor})) in the working tree, and it passed.', para, 'receipt sentence')
    rows = {
        '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
        '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
        '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
        '| Spine (core and bridge) |': f' {spine} theorems |',
        '| Audited spine declarations |': f' {n(c["audited"])} |',
        '| Modules in the compile order |': f' {c["compile"]} |',
    }
    lines = para.split('\n')
    for i, line in enumerate(lines):
        for head, tail in rows.items():
            if line.startswith(head):
                lines[i] = head + tail
        if line.startswith('| Periphery-join modules'):
            assert f'| {c["pj"][0]} modules, {n(c["pj"][1])} theorems,' in line, line
        if line.startswith('| Inherited modules bound'):
            assert f'| {c["inherited"]} (' in line, line
        if line.startswith('| Generated `injEq`'):
            assert f'| {c["injeq"][0]} in the core closure, {c["injeq"][1]} on the bridge side' in line, line
    # since F1 the receipt's bridge side is two rows, the eight bridges and the pure periphery joins
    sides = [re.match(r'\| (?:Bridges \([^|]*\)|Pure periphery joins) \| (\d+) modules, ([\d,]+) theorems \|$', line)
             for line in lines if line.startswith(('| Bridges (', '| Pure periphery joins |'))]
    assert len(sides) == 2 and all(sides), sides
    assert (sum(int(m.group(1)) for m in sides), sum(int(m.group(2).replace(',', '')) for m in sides)) == c['bridge']
    para = '\n'.join(lines)
    ch = ch[:start] + para + ch[end:]
    ch = subn1(r'That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran [\d,]+\.',
               f'That run reused {n(c["reused"])} cached Lean steps from `~/.cache/becoming-lean` and ran {n(c["ran"])}.',
               ch, 'section 9 steps')
    # the reruns run in landing order up to U's sentence, which follows the last of them (F1's since 18 October)
    follows = ' U\'s 44 join modules state the laws'
    row = [line for line in ch.split('\n') if line.startswith('| Integration of the spine |')]
    assert len(row) == 1 and row[0].count(follows) == 1 and row[0].index('Rerun with') < row[0].index(follows)
    ch = replace_once(ch, follows, f' Rerun with M3 (receipt {rid}), it counts {apart} of {spine}, none in `{MODULE}`.'
                      + follows, 'connectivity rerun')
    (ROOT / CHAPTER).write_text(ch, encoding='utf-8')
    print('edited', CHAPTER)
    # ------------------------------------------------------------ chapter, zh
    zh = (ROOT / CHAPTER_ZH).read_text(encoding='utf-8')
    zh = insert_after_line(zh, S74_ZH_DIFF_START, fill(S74_ZH_NEW), 'zh section 7.4 bullets')
    zh = replace_once(zh, S74_ZH_READING_OLD, S74_ZH_READING_NEW, 'zh section 7.4 reading')
    zh = replace_once(zh, S77_ZH_OLD, S77_ZH_NEW, 'zh section 7.7')
    zh = replace_once(zh, S84_ZH_OLD, S84_ZH_NEW, 'zh section 8 open readings')
    (ROOT / CHAPTER_ZH).write_text(zh, encoding='utf-8')
    print('edited', CHAPTER_ZH)


if __name__ == '__main__':
    if sys.argv[1:2] == ['package']:
        package()
    elif sys.argv[1:2] == ['text'] and len(sys.argv) == 6:
        text_phase(*sys.argv[2:6])
    else:
        sys.exit(__doc__)
