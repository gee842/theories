#!/usr/bin/env python3
"""Extend identity-across-steps after P87 checks and docs: record_delta.py W S.
Only this existing record changes; canonical Identity source and prior history remain.
"""
import hashlib
import json
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
S = str(int(sys.argv[2]))
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'becoming-landing-kit'))
import kit

R = kit.Receipts(W)
path = W / kit.RECORDS / 'identity-across-steps.json'
r = json.loads(path.read_text())
assert not any('P87' in h['en'] for h in r['history']), 'P87 already applied; reread the record'
module = 'Becoming.Persistence'
source = kit.lean('Persistence')
assert R.receipt['source_sha256'][module] == kit.sha(W, source), 'P87 receipt does not bind current source'


def pair(zh, en):
    return dict(zh=zh, en=en)


def swap(field, lang, old, new):
    assert r[field][lang].count(old) == 1, (field, lang, old)
    r[field][lang] = r[field][lang].replace(old, new)


r['claim']['zh'] += (' P87：给定任意保持读法 h，保持的名字连续便在每段保持中固定一个名字；对每步都保持的形成，'
    '更新与消耗的整段类别不变（Web.steady_held、Web.renewingIn_held、Web.consumingIn_held）。'
    '保持者的醒来不是保持读法下的生起。Hibernation 表明它比活动与任期的双向连续更强；Dormancy 在无保持的一步上仍容许接续；'
    'Seed 的依存与储备读法给出不同终结。Web.persisting_census 把普查原律实例化于保持，两端同读，条件分别保留；Sleeper 给出混读失败。'
    'World.balanced_reidentify_iff 不加额外假设：改认下世界平衡，恰当它的一一延续在 World.Conserves 内。'
    '原世界平衡时，守恒是步后所立之量相等，并经 exchange_alike_iff 接到相同；保持与断裂不变。关系项相等可判定时，'
    '每种保平衡命名都固定同一、生起或止息的精确条件由 World.fixed_iff、World.arises_fixed_iff、World.ceases_fixed_iff 给出。'
    '每一步之后所立之量区分所有关系项时，保平衡改认是固定改名，类别固定（World.classes_fixed）。'
    'Shuttle 是固定的实例；Lineage 与 Hibernation 的两种命名同时保存逐步关系与平衡却改变生起或类别。')
r['claim']['en'] += (' P87: for any holding predicate h, keeping its names fixes one name over a held stretch and '
    'the whole-run renewing and consuming classes of a formation holding at every step '
    '(Web.steady_held, Web.renewingIn_held, Web.consumingIn_held). Waking from holding is not holding-arising. '
    'Hibernation makes this stronger than two-way activity and tenure continuity; Dormancy permits a join where '
    'nothing holds, and dependence and reserve give Seed different endings. Web.persisting_census instantiates the '
    'original census laws with both ends read through holding and their separate hypotheses retained; Sleeper '
    'refutes mixing the readings. World.balanced_reidentify_iff, without an additional hypothesis, characterizes '
    'balanced re-identifications as one-to-one continuations within World.Conserves. In a balanced world conservation '
    'is equality of standing after the step, linked to likeness through exchange_alike_iff, and keeping and breaking '
    'are invariant. With decidable equality of relata, World.fixed_iff, World.arises_fixed_iff and '
    'World.ceases_fixed_iff characterize identity, arising and ceasing fixed by every balance-preserving naming. '
    'Where standing after every step distinguishes all relata, such namings are fixed renamings and classes are '
    'fixed (World.classes_fixed). Shuttle instantiates this; Lineage and Hibernation permit two namings preserving '
    'per-step relations and balance but changing arisings or classes.')
r['hypotheses'] += [
    pair('P87 保持读法 h 给定；活动、依存分别包含于 h 时才推出原有连续条件。整段类别等价还要求该形成在每一步都保持。',
         'P87 supplies a holding predicate h; activity and dependence contained in it separately yield the original continuity conditions. Whole-run class equivalence additionally requires that formation to hold at every step.'),
    pair('P87 的保持普查要求普查，以及保持活动、Continues、Continued 与延续关系 R 四种可判定性。止息复现推出生起复现用无分裂；反向用无合并及从某步起固定的普查上界；两端均按保持读。',
         'The P87 holding census requires a census and decisions of held activity, Continues, Continued and continuation R. Ceasing recurring implies arising recurring under no split; the converse uses no merge and an eventual fixed census bound. Both ends use holding.'),
    pair('保平衡改认的守恒等价不加假设；守恒等价于步后同量须原世界平衡。fixed_iff、arises_fixed_iff、ceases_fixed_iff 还用关系项相等可判定；classes_fixed 用每一步后所立之量区分所有关系项及原世界与改认世界平衡。',
         'The conservation characterization of balanced re-identifications adds no hypothesis; equivalence to equal post-step standing assumes the original world balanced. fixed_iff, arises_fixed_iff and ceases_fixed_iff also use decidable equality of relata. classes_fixed requires post-step standing to distinguish every relatum at every step, with both original and re-identified worlds balanced.'),
]
r['correspondence']['zh'] += (' P87 的 h、活动或依存作为 Holds，以及把所立之量守恒读作延续，均是公开的读法；不声称它们穷尽现实的物质、信息或组织连续。')
r['correspondence']['en'] += (' P87 supplies h and offers activity-or-dependence as Holds and conservation of standing as a continuation reading; these do not exhaust actual material, informational or organizational continuity.')
swap('limitations', 'zh', '双向的连续也不约束跨过休眠的接续',
     '原有双向连续不约束跨过休眠的接续；P87 的保持连续固定每步保持者的类别，但无保持的一步仍容许接续')
swap('limitations', 'en', 'even two-way continuity does not constrain succession across dormancy',
     'the original two-way continuity does not constrain succession across dormancy; P87 holding continuity fixes the class of a formation holding throughout, but a step with no holding still permits a join')
swap('limitations', 'zh', '从关系推出同一的完整说明（物质、信息或组织的连续）没有给出',
     'P87 刻画保平衡命名下守恒所固定的同一，但同量处仍有选择；守恒下的一般侵蚀、分裂／合并下的类别与任期、活动／保持混读的普查条件，以及从物质、信息或组织连续推出同一的完整说明未给出')
swap('limitations', 'en', 'a full account deriving identity from relations (continuity of material, information or organization) is not given',
     'P87 characterizes identity fixed by conservation under balanced namings but leaves choice where standings coincide; undermining under conservation, classes and tenure under splits or merges, mixed activity/holding census conditions and a full material, informational or organizational account remain open')
swap('next_delta', 'zh', '跨过休眠也成立的连续读法（例如不活跃时持续的依存）；',
     'P87 已给出跨过持续保持之休眠的连续读法，仍待选择 h 并给出混合活动／保持的普查条件；')
swap('next_delta', 'en', 'a continuity reading that reaches across dormancy (for example a dependence that persists while inactive); ',
     'P87 gives a continuity reading across continued holding through dormancy; choosing h and mixed activity/holding census conditions remain open; ')
swap('next_delta', 'zh', '从物质、信息或组织的连续推出同一。',
     '守恒下的一般侵蚀；P87 的保平衡命名刻画之外，同量处及物质、信息或组织连续如何进一步固定同一。')
swap('next_delta', 'en', 'deriving identity from continuity of material, information or organization.',
     'undermining under conservation; beyond P87\'s characterization of balanced namings, how identity is further fixed where standings coincide or by continuity of material, information or organization.')

r['dependencies'].append(dict(
    id='configurations-alike-by-relation', relation='formal-reuse',
    detail=pair('P87 通过既有交换框架的相同解释保平衡改认，不另立相同定义。',
                'P87 uses likeness in the existing exchange frame to characterize balanced re-identification, without a parallel likeness definition.'),
    interface=dict(
        output=pair('exchangeFrame、Alike 与 exchange_alike_iff。', 'exchangeFrame, Alike and exchange_alike_iff.'),
        input=pair('World.balanced_reidentify_iff_alike。', 'World.balanced_reidentify_iff_alike.'),
        conditions=pair('原世界平衡；改认在每一步一一对应。', 'The original world balances; re-identification is one to one at each step.'),
        evidence=kit.lean('Unfolding'))))
r['counterexamples'].append(dict(path=source, detail=pair(
    'P87：Hibernation 比较旧连续与保持连续；Dormancy 在无保持时仍容许接续；Seed 的两种 h 给不同终结；Sleeper 反驳混合普查；Lineage.world_readings 与 Hibernation.world_readings 使不同命名同样平衡而有不同生起或类别。',
    'P87: Hibernation separates old and holding continuity; Dormancy permits a join with no holding; two Seed predicates give different endings; Sleeper refutes a mixed census; Lineage.world_readings and Hibernation.world_readings preserve balance under namings with different arisings or classes.')))

names = R.names(module)
assert set(names) <= set(kit.declared(W / source)), 'declaration reader missed P87 names'
named = ['Web.persisting_census', 'Web.steady_held', 'Web.renewingIn_held', 'Web.consumingIn_held',
         'World.balanced_reidentify_iff', 'World.balanced_reidentify_iff_alike', 'World.fixed_iff',
         'World.arises_fixed_iff', 'World.ceases_fixed_iff', 'World.classes_fixed',
         'Lineage.world_readings', 'Hibernation.world_readings']
assert all('Becoming.' + n in names for n in named)
for n in named:
    if 'Becoming.' + n not in r['aliases']:
        r['aliases'].append('Becoming.' + n)


def reference(src, role, declarations=()):
    prior = next((x for x in r['references'] if x['path'] == src and x['role'] == role), None)
    if prior:
        # A changed existing source is reconciled by the landing's guarded repoint step.
        assert prior['sha256'] == kit.sha(W, src), ('existing source changed before P87 reference update', src)
        prior['declarations'] = list(dict.fromkeys(prior['declarations'] + list(declarations)))
    else:
        r['references'].append(dict(path=src, role=role, sha256=kit.sha(W, src), declarations=list(declarations)))


reference(source, 'proof', names)
reference(kit.lean('Unfolding'), 'proof', ['Becoming.Alike', 'Becoming.exchangeFrame', 'Becoming.exchange_alike_iff'])
for src in ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md',
            'sources/15-codex-theory-conversations/2026-10-13-codex-takeover-and-merge.md']:
    reference(src, 'provenance')
for mod in [module, 'Becoming.Unfolding']:
    src = kit.source(mod)
    if not any(x['source'] == src for x in r['proof_bindings']):
        r['proof_bindings'].append(dict(source=src, receipt=kit.RECEIPT,
            sha256_pointer='/source_sha256/' + mod, success_pointer='/status', success_value='passed'))
n = R.theorems('Persistence')
r['validation_scope']['zh'] += f' P87：同一合并回执 {R.run} 实查 Becoming.Persistence 的 {n} 项定理与 {len(names)} 项声明，全部空公理报告；源字节与回执核对一致，外围 {R.peri_run} 通过；整合反审见 §{S}，尚未经独立科学审查。'
r['validation_scope']['en'] += f' P87: the consolidated receipt {R.run} checks Becoming.Persistence, {n} theorems and {len(names)} declarations with empty axiom reports; source bytes match the receipt, periphery {R.peri_run} passed; integration counterreview is in §{S}, without independent scientific review.'
r['history'].append(pair(
    f'2026-10-13 P87：扩展原记录的休眠与关系同一两项，保留原成果及反例；保持连续、保平衡命名的刻画与边界见整合文档 §{S}。',
    f'2026-10-13 P87: extends this record on dormancy and relational identity, preserving prior results and counterexamples; holding continuity, balanced naming and their boundaries are in integration note §{S}.'))
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('identity-across-steps: P87 delta applied')
