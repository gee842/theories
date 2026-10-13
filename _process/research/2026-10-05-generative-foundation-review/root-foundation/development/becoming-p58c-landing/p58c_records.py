#!/usr/bin/env python3
"""P58c records: python3 -B p58c_records.py ROOT SECTION
Every record naming a renamed declaration takes the new name in its current body and in validation scopes citing
HEAD's current core receipt (which the following repoint step advances). History and scopes of genuinely older
receipts keep their names. Prose is stated at the strength proved; new declarations are listed; one history line each.
Changed documentary content receives the current UTC review time, without claiming an independent proof review."""
from datetime import datetime, timezone
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import p58c_names as N  # noqa: E402

ROOT, SEC = Path(sys.argv[1]).resolve(), sys.argv[2]
RECORDS = ROOT / 'theories/becoming/results/records'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-rest-family-strengths.md'
KEEP = {'history', 'validation_scope'}
receipt = json.loads((ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json').read_text())
assert receipt['status'] == 'passed'
run = receipt['utc']
DATE = f'{run[:4]}-{run[4:6]}-{run[6:8]}'
CORE_PATH = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json'
BASE_UTC = json.loads(subprocess.check_output(['git', '-C', str(ROOT), 'show', f'HEAD:{CORE_PATH}']))['utc']
REVIEWED = datetime.now(timezone.utc).isoformat(timespec='seconds')

# (old, new) on the text after the names are renamed; each must occur exactly once in the record
PROSE = {
 'listing-once-is-decided-identity': [
  ('耗散使每个可枚举的世界归于静止（World.Enumerated、World.Enumerated.not_recurring）',
   '在平衡、耗散且生起体现的条件下，每个可枚举世界的生起与止息都不复现（World.Enumerated、World.Enumerated.not_recurring）'),
  ('dissipation brings every enumerated world to rest (World.Enumerated, World.Enumerated.not_recurring)',
   'under balance, dissipation and embodied arising, neither arising nor ceasing recurs in an enumerated world '
   '(World.Enumerated, World.Enumerated.not_recurring)')],
 'becoming-renewal-reading': [
  ('falls_not_recurring 与 drawdown_finite 直接调用', 'falls_not_recurring 与 Conditions.drawdown_not_recurring 直接调用'),
  ('falls_not_recurring and drawdown_finite directly call', 'falls_not_recurring and Conditions.drawdown_not_recurring directly call')],
 'ceasing-needs-arising': [
  ('那里生起停止由水平的规律给出，止息停止由本规律给出', '那里生起从某步起停止不能被否证由水平的规律给出，止息的也由本规律给出'),
  ('there arising stops by the law of standing and ceasing stops by this law',
   'there that arising stops from some step on cannot be refuted by the law of standing, and the same of ceasing by this law')],
 'coming-and-ceasing-keep-pace': [
  ('“从某步起不上升的观测量只下降有限次”', '“从某步起不上升的观测量不在任意晚的步下降”'),
  ('an observable never rising from some step on falls only finitely often',
   'an observable never rising from some step on does not fall at arbitrarily late steps')],
 'continued-change-needs-openness': [
  ('生起停止（World.arising_stops_unrefuted）', '生起从某步起停止不能被否证（World.arising_stops_unrefuted）'),
  ('arising stops (World.arising_stops_unrefuted)', 'that arising stops from some step on cannot be refuted (World.arising_stops_unrefuted)'),
  ('生起与止息都不复现（World.comes_to_rest_unrefuted）：水平不再变化，所以体现的生起停止，并且它从某步起停止不能被否证：',
   '世界从某步起静止不能被否证（World.RestsFrom），所以生起与止息都不复现（World.comes_to_rest_unrefuted）：水平从某步起不再变化不能被否证，'
   '所以体现的生起从某步起停止不能被否证：'),
  ('comes to rest: neither arising nor ceasing recurs (World.comes_to_rest_unrefuted)',
   'is such that its resting from some step on cannot be refuted (World.RestsFrom), so neither arising nor ceasing recurs '
   '(World.comes_to_rest_unrefuted)'),
  ('世界不有限而归于静止，它的地关系项闲置（World.hatch_rests_unrefuted）',
   '世界不有限，它的地关系项闲置，而它从某步起静止不能被否证（World.hatch_rests_unrefuted）'),
  ('and the world, though not finite, its ground relata idle, comes to rest (World.hatch_rests_unrefuted)',
   'and that the world, though not finite, its ground relata idle, rests from some step on cannot be refuted '
   '(World.hatch_rests_unrefuted)'),
  ('生起停止（arising_stops_unrefuted）', '生起停止不能被否证（arising_stops_unrefuted）'),
  ('Arising stops (arising_stops_unrefuted)', 'Arising stopping unrefuted (arising_stops_unrefuted)'),
  ('rests 与这里的 rests_unrefuted_around', 'rests_unrefuted 与这里的 rests_unrefuted_around'),
  ('rests and rests_unrefuted_around here', 'rests_unrefuted and rests_unrefuted_around here'),
  ('，rests 是它的有限情形', '，rests_unrefuted 是它的有限情形'),
  ('and rests is its finite case', 'and rests_unrefuted is its finite case'),
  ('水平的静止定理（stills、', '水平的静止定理（change_stops_unrefuted_around、'),
  ('the standing rest theorems (stills, ', 'the standing rest theorems (change_stops_unrefuted_around, '),
  ('所以止息也停止，不用判定程序（P58；', '所以止息从某步起停止也不能被否证，不用判定程序（P58；'),
  ('so ceasing stops too, with no decision procedure (P58; ',
   'so that ceasing stops from some step on cannot be refuted either, with no decision procedure (P58; '),
  ('在这样归于静止的世界中', '在静止这样不能被否证的世界中', 2),
  ('in a world that comes to rest so,', 'in a world whose rest is so unrefuted,', 2),
  ('水平的变化只能有限多次', '水平的变化不在任意晚的步发生'),
  ('它比 rests 多涵盖的', '它比 rests_unrefuted 多涵盖的'),
  ('changes of standing happen only finitely often', 'changes of standing do not happen at arbitrarily late steps'),
  ('so it covers beyond rests only relata', 'so it covers beyond rests_unrefuted only relata'),
  ('交换也归于静止：', '交换也不复现：'),
  ('The exchange comes to rest as well:', 'The exchange does not recur either:'),
  ('每步都被围住，归于静止（World.openness_contingent）', '每步都被围住，生起不复现（World.openness_contingent）'),
  ('with every step enclosed and come to rest (World.openness_contingent)',
   'with every step enclosed and arising does not recur (World.openness_contingent)')],
 'laws-at-coarser-steps': [
  ('有限世界在粗步上读出时仍静止（World.sample_rests_unrefuted）',
   '有限世界在粗步上读出时，从某步起静止仍不能被否证（World.sample_rests_unrefuted）'),
  ('A finite world read at a coarser step still rests (World.sample_rests_unrefuted)',
   'Of a finite world read at a coarser step, that it rests from some step on still cannot be refuted '
   '(World.sample_rests_unrefuted)')],
 'map-of-premises': [
  ('生起与止息都不再复现，不用判定程序，证明用到其中的平衡、耗散与体现（premised_rests_unrefuted）',
   '从某步起静止不能被否证，所以生起与止息都不再复现，不用判定程序，证明用到其中的平衡、耗散与体现（premised_rests_unrefuted）'),
  ('neither arising nor ceasing recurs, with no decision procedure, the proof using balance, dissipation and embodiment '
   'among them (premised_rests_unrefuted)',
   'that it rests from some step on cannot be refuted, so neither arising nor ceasing recurs, with no decision procedure, '
   'the proof using balance, dissipation and embodiment among them (premised_rests_unrefuted)'),
  ('它在第一步之后归于静止（World.hatch_rests_unrefuted）', '它在第一步有一次生起与一次止息，此后从某步起静止不能被否证（World.hatch_rests_unrefuted）'),
  ('It comes to rest after the first step (World.hatch_rests_unrefuted)',
   'Across the first step one relatum arises and one ceases, and that it rests from some step on cannot be refuted '
   '(World.hatch_rests_unrefuted)'),
  ('有限世界中全部前提一起归于静止，', '有限世界中全部前提一起使其从某步起静止不能被否证，'),
  ('That all premises together bring a finite world to rest', 'That all premises together leave a finite world resting unrefuted')],
 'reserve-defers-ending': [
  ('只在有限多步活跃（Carries.active_not_recurring）', '不在任意晚的步活跃（Carries.active_not_recurring）'),
  ('is active only finitely often (Carries.active_not_recurring)', 'is not active at arbitrarily late steps (Carries.active_not_recurring)'),
  ('形成只在有限多步生起（Carries.arising_not_recurring）', '形成不在任意晚的步生起（Carries.arising_not_recurring）'),
  ('a formation arises only finitely often (Carries.arising_not_recurring)',
   'a formation does not arise at arbitrarily late steps (Carries.arising_not_recurring)'),
  ('从某步起不上升的储备只下降有限多次', '从某步起不上升的储备不在任意晚的步下降'),
  ('a reserve that never rises from some step on falls only finitely often',
   'a reserve that never rises from some step on does not fall at arbitrarily late steps')],
 'rest-at-every-resolution': [
  ('单位固定时取用封闭家族停止（Flow.taking_not_recurring）', '单位固定时取用封闭家族不复现（Flow.taking_not_recurring）'),
  ('with the unit fixed, taking from a closed family stops (Flow.taking_not_recurring)',
   'with the unit fixed, taking from a closed family does not recur (Flow.taking_not_recurring)'),
  ('所以单位固定时交换的静止（World.exchange_not_recurring）依赖量子', '所以单位固定时交换不复现（World.exchange_not_recurring）依赖量子'),
  ("So the exchange's rest with a fixed unit (World.exchange_not_recurring) relies on the quantum",
   'So that the exchange does not recur with a fixed unit (World.exchange_not_recurring) relies on the quantum'),
  ('每个固定尺度的转移停止（Trickle.exchange_not_recurring）', '每个固定尺度的转移都不复现（Trickle.exchange_not_recurring）'),
  ('transfers of each fixed size stop (Trickle.exchange_not_recurring)', 'transfers of each fixed size do not recur (Trickle.exchange_not_recurring)')],
 'rest-with-refinement-counted': [
  ('生起与止息都不复现（World.rests_unrefuted_refinement_counted）',
   '世界从某步起静止不能被否证，所以生起与止息都不复现（World.rests_unrefuted_refinement_counted）'),
  ('生起与止息都不复现（World.rests_unrefuted_without_refinement，',
   '世界从某步起静止不能被否证，所以生起与止息都不复现（World.rests_unrefuted_without_refinement，'),
  ('neither arising nor ceasing recurs (World.rests_unrefuted_refinement_counted)',
   'that the world rests from some step on cannot be refuted, so neither arising nor ceasing recurs '
   '(World.rests_unrefuted_refinement_counted)'),
  ('neither arising nor ceasing recurs (World.rests_unrefuted_without_refinement,',
   'that the world rests from some step on cannot be refuted, so neither arising nor ceasing recurs '
   '(World.rests_unrefuted_without_refinement,')],
 'space-and-its-parts': [
  ('生起与止息都不复现，不用判定程序（World.rests_unrefuted）',
   '世界从某步起静止（World.RestsFrom）不能被否证，所以生起与止息都不复现（World.not_recurring_of_rests_unrefuted），'
   '不用判定程序（World.rests_unrefuted；两半在共同的一步合起，World.rests_unrefuted_iff）'),
  ('neither arising nor ceasing recurs, with no decision procedure (World.rests_unrefuted)',
   'that the world rests from some step on (World.RestsFrom) cannot be refuted, so neither arising nor ceasing recurs '
   '(World.not_recurring_of_rests_unrefuted), with no decision procedure (World.rests_unrefuted; the two halves join at a '
   'common step, World.rests_unrefuted_iff)'),
  ('不要求活动可判定，名称不变，陈述更强。', '不要求活动可判定，陈述更强（P58；P58c 再把陈述加强为从某步起静止不能被否证，名称随之改）。'),
  ('need no decided activity, their names unchanged and their statements stronger.',
   'need no decided activity, their statements stronger (P58; P58c strengthened them again, to resting from some step on '
   'being unrefutable, and renamed them so).')],
}
PROSE.setdefault('becoming-renewal-reading', []).extend([('从某步起不再上升的自然数可观测量只能下降有限次', '从某步起不再上升的自然数可观测量不在任意晚的步下降'), ('never rises from some step on falls only finitely often;', 'never rises from some step on does not fall at arbitrarily late steps;')])
PROSE.setdefault('continued-change-needs-openness', []).extend([('Standing stops changing, so embodied arising stops, and that it stops from some step on cannot be refuted:', 'That standing stops changing from some step on cannot be refuted, so that embodied arising stops from some step on cannot be refuted either:')])
PROSE.setdefault('generation-is-replenishment', []).extend([('从不上升的量只下降有限次', '从不上升的量不在任意晚的步下降'), ('A quantity that never rises falls only finitely often', 'A quantity that never rises does not fall at arbitrarily late steps')])
PROSE.setdefault('reserve-defers-ending', []).extend([('从某步起不上升的观测量只下降有限多次', '从某步起不上升的观测量不在任意晚的步下降'), ('An observable that never rises from some step on falls only finitely often', 'An observable that never rises from some step on does not fall at arbitrarily late steps'), ('不被支持的形成只在有限多步活跃', '不被支持的形成不在任意晚的步活跃'), ('An unsupported formation is active only finitely often', 'An unsupported formation is not active at arbitrarily late steps')])
PROSE.setdefault('rest-with-refinement-counted', []).extend([('细分从 T 起不给该家族时取用停止（Flow.taking_needs_refinement', '细分从 T 起不给该家族时取用不复现（Flow.taking_needs_refinement'), ('taking from a family closed from T on stops where the refinement gives it nothing from T on', 'taking from a family closed from T on does not recur where the refinement gives it nothing from T on')])
PROSE.setdefault('space-and-its-parts', []).extend([('从某步起不被支持的形成只活跃有限多次', '从某步起不被支持的形成不在任意晚的步活跃'), ('A formation unsupported from some step on is active only finitely often', 'A formation unsupported from some step on is not active at arbitrarily late steps')])
PROSE.setdefault('unceasing-generation-needs-renewal', []).extend([('从某步起家族中没有条件上升时，消耗它的事件只发生有限次', '从某步起家族中没有条件上升时，消耗它的事件不在任意晚的步发生'), ('If from some step none of them rises, events depleting the family occur only finitely often', 'If from some step none of them rises, events depleting the family do not occur at arbitrarily late steps'), ('在家族不再上升之后只活跃有限次', '在家族不再上升之后不在任意晚的步活跃'), ('is active only finitely often once none of them rises any more', 'is not active at arbitrarily late steps once none of them rises any more'), ('条件被消耗，生起停止；', '条件被消耗，生起不复现；'), ('consume it, and arising stops;', 'consume it, and arising does not recur;'), ('以消耗为条件的生起停止。', '以消耗为条件的生起不复现。'), ('and arising on a consumed condition stops', 'and arising on a consumed condition does not recur')])
ADD = {   # record: (file suffix, after declaration, new declarations, also aliases)
 'space-and-its-parts': ('Becoming/Space.lean', 'Becoming.World.rests_unrefuted',
                         ['Becoming.World.RestsFrom', 'Becoming.World.rests_unrefuted_iff',
                          'Becoming.World.not_recurring_of_rests_unrefuted'], True),
 'laws-of-one-step': ('Becoming/Locality.lean', 'Becoming.ceasing_steps_found',
                      ['Becoming.ceasing_steps_unrefuted', 'Becoming.Covers.ceasing_stops_unrefuted'], False),
 'rest-with-refinement-counted': ('Becoming/Resolution.lean', 'Becoming.World.rests_unrefuted_of_after',
                                  ['Becoming.World.restsFrom_of_after'], False),
}
HIST_ZH = (f'{DATE} P58c：静止一族按强度命名（Ren 于 2026-10-12：“agree with you”，{SOURCE}）：名称恰是陈述所证的强度。'
           '从某步起静止不能被否证的定理名为 …_unrefuted（其陈述加强为 ¬¬∃N, World.RestsFrom N）；只证不复现的名为 …_not_recurring；'
           '“只有有限次”“停止”“归于静止”在文字中改为所证的强度。见整合文档 §{sec}。历史与旧回执的验证范围保留当时名称；随当前回执推进的验证范围使用现名。')
HIST_EN = (f'{DATE} P58c: the rest family named by strength (Ren, 12 October 2026: “agree with you”, {SOURCE}): each name says the strength '
           'its statement proves. Theorems proving that resting from some step on cannot be refuted are named …_unrefuted '
           '(their statements strengthened to ¬¬∃N, World.RestsFrom N); those proving only non-recurrence are named '
           '…_not_recurring; prose saying “finitely often”, “stops” or “comes to rest” now says the strength proved. See §{sec} '
           'of the integration note. History and scopes of older receipts retain former names; scopes advancing with '
           'the current receipt use current names.')


def once(text, old, new, where):
    n = text.count(old)
    assert n == 1, (where, n, old[:100])
    return text.replace(old, new)


changed = []
for f in sorted(RECORDS.glob('*.json')):
    rec = json.loads(f.read_text())
    body = {k: v for k, v in rec.items() if k not in KEEP}
    dumped = json.dumps(body, ensure_ascii=False)
    scope = rec.get('validation_scope', {})
    old_scope = json.dumps(scope, ensure_ascii=False)
    current_scope = N.rename(old_scope) if BASE_UTC in old_scope else old_scope
    if not N.old_left(dumped) and f.stem not in PROSE and f.stem not in ADD and current_scope == old_scope:
        continue
    new = N.rename(dumped)
    for old, rep, *count in PROSE.get(f.stem, []):
        assert new.count(old) == (count[0] if count else 1), (f.stem, new.count(old), old[:100])
        new = new.replace(old, rep)
    body = json.loads(new)
    if f.stem in ADD:
        path, after, decls, alias = ADD[f.stem]
        ref = next(x for x in body['references'] if x['path'].endswith(path))
        i = ref['declarations'].index(after) + 1
        ref['declarations'][i:i] = [d for d in decls if d not in ref['declarations']]
        if alias:
            i = body['aliases'].index(after) + 1
            body['aliases'][i:i] = [d for d in decls if d not in body['aliases']]
    left = N.old_left(json.dumps(body, ensure_ascii=False))
    assert not left, (f.stem, left)
    for k in rec:
        if k not in KEEP:
            rec[k] = body[k]
    if current_scope != old_scope:
        rec['validation_scope'] = json.loads(current_scope)
    rec['reviewed_at_utc'] = REVIEWED
    rec['history'].append({'zh': HIST_ZH.format(sec=SEC), 'en': HIST_EN.format(sec=SEC)})
    f.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
    changed.append(f.stem)
print(len(changed), 'records:', ' '.join(changed))
