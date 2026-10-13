"""Reproduce the fixed landing configuration from the preserved package drafts.
This scans declarations for record bindings, not for proof verification. No Lean files change.
"""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
DEV = HERE.parent
sys.path.insert(0, str(DEV / 'becoming-landing-kit'))
import kit

packages = [
 dict(number=77, module='Listing', imports=['Decidedness','Sampling','Resolution'], title_zh='列出一次所承诺的', title_en='What listing once commits to',
 zh='列表恰在成员间同一已定时能列出一次（`listsOnce_iff_decided`），所含关系项的数唯一且恰在此时存在；否证形式的规律不需这一前提。按世界的关系不可分辨地计数，对每个世界都固定数目等价于排中律（`World.numbers_indiscernible_iff_em`）；按出现读保持数量与局部规律，但不跨步追踪出现。',
 en='A list can be listed once exactly where identity among its members is decided (`listsOnce_iff_decided`); its number of members is unique and exists exactly then. Refutation laws need no such premise. Fixing every list\'s number up to relational indiscernibility in every world is equivalent to excluded middle (`World.numbers_indiscernible_iff_em`). Reading by occurrence keeps amounts and local laws without tracking occurrences across steps.',
 boundary_zh='与配置相同（`Alike`）的连接及另外 24 个被归类为不需前提的用处之推论尚未证明。原有 Distinct 清点是 193c5511 的历史快照。',
 boundary_en='The connection to likeness of configurations (`Alike`) and corollaries for the other 24 uses classified as premise-free remain open. The Distinct inventory is a historical snapshot at 193c5511.',
 records=['listing-once-is-decided-identity','relata-counted-up-to-indiscernibility']),
 dict(number=78, module='Order', imports=['Sampling'], title_zh='变化的次序', title_en='The order of change',
 zh='停顿保留世界的前提、段的总量及复现，速率与储备的步数依读法而定；给定覆盖交换的足迹，交换无交集的相邻交换保持全部前提，恰可达到保持其有交集交换偏序的重编号（`Footprinted.sorts_iff`、`Footprinted.converse`）。移除空步保留前提、普查与总量。',
 en='Stuttering keeps the premises, stretch totals and recurrence, while rates and reserves counted in steps depend on the reading. For a given footprint containing the exchanges, commuting unjoined neighbouring exchanges keeps every premise and reaches exactly the renumberings preserving the partial order of joined exchanges (`Footprinted.sorts_iff`, `Footprinted.converse`). Removing idle steps keeps premises, censuses and totals.',
 boundary_zh='足迹给定；移除空步使用给定的移动步。最小足迹、Foata 正规形、重排中的普查与连续时间未证明。',
 boundary_en='The footprint and the moving steps used to remove idle steps are supplied. The least footprint, a Foata normal form, censuses along reorderings and continuous time remain open.',
 records=['only-the-order-of-change-registers','exchanges-commute-unless-joined','order-of-exchanges-is-the-invariant']),
 dict(number=79, module='OneStep', imports=['Counting','Sampling'], title_zh='一步与逐步选择家族的全部规律', title_en='All laws of one step and of families chosen step by step',
 zh='一步的样式恰在遵守每步的规律与所名局部条件的规律时由一个世界实现（`OneStep.every_iff`、`OneStep.laws`）；所取非零须有取者，所给非零须有给者。给者、容量与活动的增量精确刻画；单一家族上的运行加跨步接续，逐步选家族时耗减所加的是按正水平计数的连续（`OneStep.step_runsDown_iff`），严格弱于逐位置追踪。',
 en='A pattern of one step is realized by a world exactly where it obeys the law of every step and the law of each named local condition (`OneStep.every_iff`, `OneStep.laws`); nonzero taking needs a taker and nonzero giving a giver. Givers, capacity and activity are characterized exactly. Runs on one family add chaining; for families chosen step by step, running down adds continuity counted at positive levels (`OneStep.step_runsDown_iff`), strictly weaker than tracking positions.',
 boundary_zh='完备性限于所给样式与条件；活跃者计数、整段上的容量与活动仍开放。',
 boundary_en='Completeness is for the stated patterns and conditions; counts of active relata and capacity and activity over runs remain open.',
 records=['laws-of-one-step-complete','one-step-missing-laws','runs-on-families-chosen-step-by-step']),
 dict(number=82, module='Weighted', imports=['Capture','Resolution'], title_zh='加权历史及其损失', title_en='Weighted histories and their losses',
 zh='给定权重及其规律、动作与配置的有限列表，有限步数的历史权重之和恰是逐步转移（`Weights.sum_courses`）；可能性的实例就是核心的迹，计数保留可能性。经一个有代表的描述，在所有步数上的精确保留恰是一步的可归并（`Weights.lumped_iff`）；截断、抵消、未保留的记忆与回路各有明确边界见证。',
 en='Given weights with their laws and finite lists of moves and configurations, the sum of histories over a finite horizon is exactly stepwise transfer (`Weights.sum_courses`). Possibility is the core\'s trace relation, and counting preserves possibility. For a description with representatives, exact preservation at every horizon is exactly one-step lumpability (`Weights.lumped_iff`); truncation, cancellation, unkept memory and loops have explicit boundary witnesses.',
 boundary_zh='不推出实际权重、带相位的振幅、无限和收敛或一般权重的记忆恢复；权重自身的规律是公开的结构字段。',
 boundary_en='Actual weights, phased amplitudes, convergence of infinite sums and memory restoration for general weights are not derived; the weight laws are explicit structure fields.',
 records=['sum-over-histories-exact','losses-of-the-sum-over-histories']),
 dict(number=84, module='Transmission', imports=['Premises'], title_zh='传递的精确条件与边界', title_en='The exact conditions and boundary of transmission',
 zh='传递恰是承继与所需之界（`Flow.transmitsWithin_iff`）；先前没有依存时承继就是形成的规律，一般的形成与持有分解用到已定。去掉给予者的一条依存保持其余前提而破坏起约束的传递（`World.drop_but`）；在所名有限、平衡、耗散、体现与支持条件下，取用的读法加上取用即依存推出传递（`World.transmitting_of_drawn`）。',
 en='Transmission is exactly inheritance with a need bound (`Flow.transmitsWithin_iff`); where no dependence was held before, inheritance is the forming law, while the general forming/holding split uses decidedness. Dropping one dependence of a giver keeps the other premises and breaks binding transmission (`World.drop_but`). Under the named finite, balance, dissipation, embodiment and support conditions, a reading of drawing together with drawing being depending derives transmission (`World.transmitting_of_drawn`).',
 boundary_zh='这不是从其余核心前提单独推出传递；链接仅充分，水平无界的情形与新依存的形成仍开放。',
 boundary_en='This does not derive transmission from the other core premises alone; the link is sufficient only, and unbounded levels and the formation of new dependences remain open.',
 records=['transmission-is-inheritance-and-need','transmission-independent-where-it-binds']),
 dict(number=85, module='Succession', imports=['Continuation'], title_zh='没有哪个来源复现的供给', title_en='Fed without any source recurring',
 zh='`Successive.relay` 给出平衡、耗散且只有活跃者给予的流，池每步被供给，而每个来源只在自己的那一步参与与活跃；延续所需的供给不要求哪个来源形成复现。这推进 continuing-self-fed-from-beyond，不另立成果。',
 en='`Successive.relay` gives a balanced, dissipative flow in which only active formations give, the pool is fed at every step, and each source participates and is active at its own step only. Continuing to be fed needs no source formation to recur. This advances continuing-self-fed-from-beyond and is not a separate result.',
 boundary_zh='每个来源在自己的那一步仍被需要；同一世界移去来源后仍被供给与来源从流中形成都未证明。',
 boundary_en='Each source is still needed at its own step; remaining fed after removing a source from the same world and the formation of the sources from the flow are not shown.',
 records=['continuing-self-fed-from-beyond']),
]

# Explicit cross-module producer declarations, checked against the current receipt. Own-module
# declarations are grouped by source sections from the curated drafts' exact aliases; no theorem
# is inferred from wording or from a historical scratch check.
builds = {
 'listing-once-is-decided-identity': ['Distinct','World.rests','World.Finite','World.CountedBy','Decided'],
 'relata-counted-up-to-indiscernibility': ['Decided','Alike','Flow.BalancesOn.sample'],
 'only-the-order-of-change-registers': ['Flow.sample','Web.sample','World.sample','Flow.BalancesOn.sample','Flow.DissipatesOn.sample'],
 'exchanges-commute-unless-joined': ['Flow.Balances','Flow.Dissipative','Flow.Acting','Flow.Taking','Web.Dependent','Web.Embodied','Flow.TransmitsWithin'],
 'order-of-exchanges-is-the-invariant': ['Flow','Web'],
 'laws-of-one-step-complete': ['Flow.takers','counting_laws','tally_iff_counted','World.ofRoles','Flow.BalancesOn','Flow.RunsDownOn'],
 'one-step-missing-laws': ['Flow.BalancesOn.comesToStand_iff','Flow.BalancesOn.ceasesToStand_iff'],
 'runs-on-families-chosen-step-by-step': [],
 'sum-over-histories-exact': ['carries_law_iff','Generative.Trace'],
 'losses-of-the-sum-over-histories': [],
 'transmission-is-inheritance-and-need': ['Flow.TransmitsWithin','Flow.transmitted_supported','Flow.transmitted_within','Flow.Descends'],
 'transmission-independent-where-it-binds': ['World.Premise.Holds','World.Finite','World.Transmitting'],
}
R = kit.Receipts(HERE.parents[5])
records = {}
for p in packages:
    if p['number'] == 85:
        continue
    folder = DEV / f'becoming-p{p["number"]}-landing'
    ds = kit.declared(folder/'lean/Becoming'/f'{p["module"]}.lean')
    for record_id in p['records']:
        draft=json.loads((folder/'docs/records'/f'{record_id}.json').read_text())
        aliases=[x for x in draft['aliases'] if x.startswith('Becoming.')]
        assert all(x in ds for x in aliases), (record_id, [x for x in aliases if x not in ds])
        names = [x.removeprefix('Becoming.') for x in aliases]
        sec = list(dict.fromkeys(ds[x] for x in aliases))
        # Source blocks between the selected public endpoints also carry the supporting lemmas.
        if record_id == 'listing-once-is-decided-identity':
            sec = list(dict.fromkeys(ds.values()))[:7]
        elif record_id == 'relata-counted-up-to-indiscernibility':
            sec = list(dict.fromkeys(ds.values()))[7:]
        elif record_id == 'only-the-order-of-change-registers':
            all_sec=list(dict.fromkeys(ds.values()));sec=all_sec[:15]+['Removing idle steps']
        elif record_id == 'laws-of-one-step-complete':
            sec=list(dict.fromkeys(ds.values()))[:16]+sec
            sec=list(dict.fromkeys(sec))
        for x in builds[record_id]:
            full=x if x.startswith('Generative.') else 'Becoming.'+x
            assert full in R.owner, (record_id,'external declaration missing',x)
        provenance = ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md']
        if p['number'] == 77:
            provenance.append(kit.DEV + '/becoming-p77-landing/inventory/INVENTORY.md')
        records[record_id] = dict(package=p['module'].upper(),sections=sec,named=names,builds_on=builds[record_id],provenance=provenance)
for p in packages:
    if p['number'] == 85:
        p['reuses'] = ['continuing-self-fed-from-beyond', 'derived-extent-limits']
        continue
    folder = DEV / f'becoming-p{p["number"]}-landing'
    deps = []
    for rid in p['records']:
        draft = json.loads((folder/'docs/records'/f'{rid}.json').read_text())
        deps.extend(x['id'] for x in draft['dependencies'] if x['id'] not in records)
    p['reuses'] = list(dict.fromkeys(deps))
(HERE/'content.json').write_text(json.dumps(dict(packages=packages,records=records),ensure_ascii=False,indent=2)+'\n')
print('Wrote landing content:',len(packages),'modules,',len(records),'new records')
