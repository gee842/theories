#!/usr/bin/env python3
"""Run (a)'s deltas to existing records, after the new records are written (make_records.py runs it).
python3 -B record_delta.py W S   (S the study section of P76; P81's is S + 1)

- attraction-is-not-returning (P81): the next_delta items on processes that are not determined and on Captured's
  rule region are answered by necessarily-drawn-is-not-returning; the limitation narrowed; related; history.
- recurrence-without-premise (P81): the next_delta item on losing nothing and returning for processes that are not
  determined is answered by returning-where-the-course-branches; the limitation narrowed; related; history.
- configurations-alike-by-relation (P76, P81): the next_delta's restatement item narrowed to what P81 left and its
  constructive-condition item answered for linear tests by tests-fix-likeness-where-determined; the limitation
  narrowed; related; history.
- target-capture (P81): related (Captured's rule region as an absorbing region); history.
Each old text is asserted; if one has changed, reread the record and adapt this script. Claims are unchanged.
"""
import json
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
S76 = str(int(sys.argv[2]))
S81 = str(int(sys.argv[2]) + 1)
RECORDS = W / 'theories/becoming/results/records'


def load(record_id):
    return json.loads((RECORDS / f'{record_id}.json').read_text())


def save(r):
    (RECORDS / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(r['id'], ': run (a) delta applied')


def swap(r, field, lang, old, new):
    assert r[field][lang].count(old) == 1, f'{r["id"]} {field} ({lang}) changed: reread it'
    r[field][lang] = r[field][lang].replace(old, new)


def relate(r, record_id, zh, en):
    assert all(x['id'] != record_id for x in r['related']), (r['id'], record_id)
    r['related'].append({'id': record_id, 'detail': {'zh': zh, 'en': en}})


def history(r, zh, en):
    r['history'].append({'zh': zh, 'en': en})


r = load('attraction-is-not-returning')
swap(r, 'next_delta', 'zh',
     '不确定过程上的吸引：可能被吸入与必然被吸入，与 Becoming.Experiment 的带动作运行相接；Capture 落地后，Captured 的规则区域作为 '
     'Law.Absorbing 与 Law.DrawnInto 的实例定理；',
     '不确定过程上的吸引与 Captured 的规则区域作为吸收区域已由 necessarily-drawn-is-not-returning 给出（P81）；在界内被吸入；')
swap(r, 'next_delta', 'en',
     "Attraction for processes that are not determined, possibly and necessarily drawn, connected with "
     "Becoming.Experiment's runs with moves; once Capture has landed, Captured's rule region as an instance of "
     "Law.Absorbing and Law.DrawnInto; ",
     "attraction for processes that are not determined and Captured's rule region as an absorbing region are given by "
     'necessarily-drawn-is-not-returning (P81); being drawn in within a bound; ')
swap(r, 'limitations', 'zh', '主律只对确定的律，不确定过程上的吸引（可能与必然被吸入）没有陈述',
     '主律在此只对确定的律（对每个过程，必然被吸入恰是不返回，可能被吸入允许返回，见 necessarily-drawn-is-not-returning，P81）')
swap(r, 'limitations', 'en',
     'the main law is for determined laws only, and attraction for processes that are not determined (possibly or '
     'necessarily drawn) is not stated',
     'the main law is here for determined laws only (for every process, necessarily drawn is not returning and possibly '
     'drawn allows return: see necessarily-drawn-is-not-returning, P81)')
relate(r, 'necessarily-drawn-is-not-returning',
       '对每个过程的主律：必然被吸入恰是不返回，可能被吸入允许在另一路径中返回；Captured 的规则区域是吸收区域。',
       "The main law for every process: necessarily drawn is exactly not returning, possibly drawn allows return on "
       "another course; Captured's rule region is an absorbing region.")
history(r, f'2026-10-12 P81：next_delta 中不确定过程上的吸引与 Captured 规则区域两项由 necessarily-drawn-is-not-returning 回答；'
           f'见整合文档 §{S81}。断言不变。',
        f"2026-10-12 P81: the next_delta items on attraction for processes that are not determined and on Captured's rule "
        f'region are answered by necessarily-drawn-is-not-returning; see §{S81} of the integration note. The claim is '
        f'unchanged.')
save(r)

r = load('recurrence-without-premise')
swap(r, 'next_delta', 'zh', '非确定过程的无损与回返；',
     '非确定过程的无损与回返已由 returning-where-the-course-branches 给出（P81）；对每个能动的构型不加选择地陈述沿运行的定律；')
swap(r, 'next_delta', 'en', 'losing nothing and returning for processes that are not determined; ',
     'losing nothing and returning for processes that are not determined are given by '
     'returning-where-the-course-branches (P81); the laws along runs stated for every configuration that can move, '
     'without a choice; ')
swap(r, 'limitations', 'zh', '无损、回返与保留可能的等价只对确定的律，非确定过程的形式未陈述',
     '无损、回返与保留可能的等价只对确定的律（对每个过程三者分开：保留每个可能不给回返，合并不必失去可能，不合并沿运行给回返，'
     '见 returning-where-the-course-branches，P81）')
swap(r, 'limitations', 'en',
     'the equivalence of losing nothing, returning and keeping every possibility is for determined laws, and no form '
     'for processes that are not determined is stated',
     'the equivalence of losing nothing, returning and keeping every possibility is for determined laws (for every '
     'process the three come apart: keeping every possibility does not give returning, a merge need not lose a '
     'possibility, merging nothing gives returning along runs; see returning-where-the-course-branches, P81)')
relate(r, 'returning-where-the-course-branches',
       '对每个过程：返回的精确条件，三方等价在路径分支时分开之处。',
       'For every process: the exact condition for returning, and where the three-way equivalence comes apart when the '
       'course branches.')
history(r, f'2026-10-12 P81：next_delta 中非确定过程的无损与回返一项由 returning-where-the-course-branches 回答；'
           f'见整合文档 §{S81}。断言不变。',
        f'2026-10-12 P81: the next_delta item on losing nothing and returning for processes that are not determined is '
        f'answered by returning-where-the-course-branches; see §{S81} of the integration note. The claim is unchanged.')
save(r)

r = load('configurations-alike-by-relation')
swap(r, 'next_delta', 'zh',
     '第一部分以 Determined 陈述的定理在相同之下重述（DeterminedAt），或说明何处需要相等；核心中经同样检验推出相同的构造性条件；',
     '第一部分以 Determined 陈述的定理中 P81 尚未重述的（Mechanism 的 Image／FactorsThrough 刻画、not_fixes_other_of_new、'
     'Joint 的 determined_dichotomy、carries_law_iff 的双向形式；其余见 determinacy-up-to-likeness）；核心中分支检验固定相同的'
     '构造性证明（线性检验的条件由 tests-fix-likeness-where-determined 给出，P76）；')
swap(r, 'next_delta', 'en',
     'Restating the Part I theorems stated with Determined up to likeness (DeterminedAt), or saying where equality is '
     'needed; a constructive condition in the core under which passing the same tests makes configurations alike; ',
     "Restating up to likeness the Part I theorems stated with Determined that P81 did not (Mechanism's "
     "characterization through Image and FactorsThrough, not_fixes_other_of_new, Joint's determined_dichotomy, the "
     'two-way form of carries_law_iff; the rest are in determinacy-up-to-likeness); a constructive proof in the core '
     'that branching tests fix likeness (the condition for linear tests is given by '
     'tests-fix-likeness-where-determined, P76); ')
swap(r, 'limitations', 'zh',
     '经同样检验的配置相同需要分支条件，没有陈述（外围在像有限时有 same_iff_bisimilar，要经典逻辑）；'
     '第一部分以 Determined 陈述的定理在相同之下成立，没有陈述；',
     '经同样检验的配置相同：两个框架在相同之下确定时由 tests-fix-likeness-where-determined 陈述（P76），分支检验在核心中没有陈述'
     '（外围在像有限时有 same_iff_bisimilar，要经典逻辑）；第一部分以 Determined 陈述的定理在相同之下的重述见 '
     'determinacy-up-to-likeness（P81），其中几项仍待重述；')
swap(r, 'limitations', 'en',
     'That configurations passing the same tests are alike needs a condition on branching and is not stated (the '
     'periphery has same_iff_bisimilar for image-finite models, classically); that the Part I theorems stated with '
     'Determined hold up to likeness is not stated; ',
     'That configurations passing the same tests are alike is stated where both frames are determined up to likeness, '
     'by tests-fix-likeness-where-determined (P76), and for branching tests not in the core (the periphery has '
     'same_iff_bisimilar for image-finite models, classically); the Part I theorems stated with Determined are '
     'restated up to likeness in determinacy-up-to-likeness (P81), a few still to be; ')
relate(r, 'tests-fix-likeness-where-determined',
       '检验固定相同的构造性条件：两个框架在相同之下确定。',
       'The constructive condition under which tests fix likeness: both frames determined up to likeness.')
relate(r, 'determinacy-up-to-likeness',
       '第一部分以 Determined 陈述的定理在相同之下的重述，以及需要相等之处的见证。',
       'The Part I theorems stated with Determined restated up to likeness, with witnesses where equality is needed.')
history(r, f'2026-10-12 P76、P81：next_delta 中检验的构造性条件一项由 tests-fix-likeness-where-determined 回答（§{S76}），'
           f'相同之下重述一项的主要部分由 determinacy-up-to-likeness 回答（§{S81}）。断言不变。',
        f'2026-10-12 P76, P81: the next_delta item on a constructive condition for tests is answered by '
        f'tests-fix-likeness-where-determined (§{S76}), and the main part of the item on restating up to likeness by '
        f'determinacy-up-to-likeness (§{S81}). The claim is unchanged.')
save(r)

r = load('target-capture')
relate(r, 'necessarily-drawn-is-not-returning',
       'Captured 的规则区域是吸收区域；改过的状态或规则被吸入且不返回（P81）。',
       "Captured's rule region is an absorbing region; a reformed state or rule is drawn in and never returns (P81).")
history(r, f'2026-10-12 P81：Captured 的规则区域作为吸收区域由 necessarily-drawn-is-not-returning 陈述；见整合文档 §{S81}。断言不变。',
        f"2026-10-12 P81: Captured's rule region as an absorbing region is stated by necessarily-drawn-is-not-returning; "
        f'see §{S81} of the integration note. The claim is unchanged.')
save(r)
