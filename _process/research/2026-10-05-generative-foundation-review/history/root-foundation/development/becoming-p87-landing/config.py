"""P87: extend identity-across-steps; no duplicate result. S is assigned by the integrator.
Use ../becoming-landing-kit after the preserved module passes the consolidated checker.
"""
LABEL = 'P87 Persistence'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md'
PACKAGES = [dict(
    module='Persistence', package='becoming-p87-landing', key='PERSISTENCE', prefix='p87', after='Identity',
    scope_before='Identity: re-identifying formations one to one at each step',
    bullet="""* `Becoming.Persistence` (L3): continuity across dormancy and identity read from relations
  (P87). Keeping the names of what holds fixes the class of a formation holding throughout,
  strictly beyond activity and tenure continuity; where nothing holds it leaves the join open.
  A re-identification balances exactly where its continuation lies within conservation. In a
  balanced world, conservation identifies equal standings after the step; distinct standings
  fix identity, classes and arisings, while Lineage and Hibernation leave alternatives. Census
  laws are instantiated with both ends read through holding. The choice of holding and of
  conservation as the continuation remains a reading; classes under splits or merges,
  undermining under conservation and a mixed-reading census law remain open.""",
    scope=('Persistence: for any holding predicate, keeping its names fixes classes of formations holding throughout; '
           'a held census instantiates both continuation recurrence laws with their separate no-split, no-merge, '
           'boundedness and decidability hypotheses. A world under re-identification balances exactly where its '
           'one-to-one continuation lies within conservation, with no additional hypothesis; in a balanced world '
           'conservation is equality of standing after the step and agrees with exchange likeness. With decidable '
           'equality, identity, arising and ceasing fixed by all balanced re-identifications have exact conservation '
           'criteria. Distinct standings fix classes. Hibernation, Dormancy, Seed, Sleeper, Shuttle and Lineage '
           'separate the holding readings, show the mixed census failure and bound the identity claim.'),
    readme_zh='跨过休眠的连续与关系所固定的同一（P87）：持续有所保持时类别不变；平衡的改认恰在守恒延续内，所立之量相异时固定同一；同量与休眠见证保留读法边界',
    readme_en='continuity across dormancy and identity fixed by relations (P87): continued holding fixes class; balanced re-identifications are exactly those within conservation, distinct standings fix identity, and witnesses preserve the boundaries',
    imports_zh=('`Identity` 导入 `Population`；', '`Identity` 导入 `Population`；`Persistence` 导入 `Identity` 与 `Unfolding`；'),
    imports_en=('`Identity` imports `Population`;', '`Identity` imports `Population`; `Persistence` imports `Identity` and `Unfolding`;'),
)]
PLAN_ZH = ('| P87 休眠中的连续与关系所固定的同一 ✓ | 复用 identity-across-steps，新增 Becoming.Persistence（{N_PERSISTENCE} 项定理）；'
           '保持持续有所保持的形成的名字固定其类别；平衡的改认恰在守恒延续内，同量保留选择，异量固定同一。'
           '普查两端同读保持，原有条件分别保留。侵蚀、分裂／合并下的类、混合普查与保持的读法仍开放；研究 §{S_PERSISTENCE}。 |')
PLAN_EN = ('- **P87:** extends identity-across-steps with Becoming.Persistence ({N_PERSISTENCE} theorems): keeping the '
           'names of formations holding throughout fixes their classes; balanced re-identifications lie exactly within '
           'conservation, equal standings leave choice and distinct standings fix identity. The census reads both ends '
           'through holding under its original separate hypotheses. Undermining, classes under splits or merges, a '
           'mixed census and the holding reading remain open; study §{S_PERSISTENCE}.')
CHAPTER_ZH = ('**休眠中的连续与关系所固定的同一（P87）。** 先读同一展开中哪些关系跨过不活跃的一步仍保持：给定保持的读法 '
              '`h`，`Web.persisting h` 以它读活动。醒来者若此前已保持，在这个读法下不是生起；保持的名字逐步延续，便在每段保持中'
              '只有一个名字，始终保持者的更新／消耗类别不变（`Web.steady_held`、`Web.renewingIn_held`、`Web.consumingIn_held`）。'
              '这比原有活动与任期的双向连续更强（`Hibernation.readings`），而在没有任何保持的一步上仍不约束接续（`Dormancy.held_both`）。'
              '依存与储备给种子不同的终结读法（`Seed.held_readings`）；普查两端必须同读保持，混读可以失败（`Web.persisting_census`、`Sleeper.held_readings`）。\n\n'
              '世界的改认保持平衡，恰当它每步所接续者在守恒关系 `World.Conserves` 内（`World.balanced_reidentify_iff`，无附加假设）。'
              '平衡世界中这就是步后所立之量相等，也就是交换框架的相同（`World.balanced_reidentify_iff_alike`）。'
              '关系项相等可判定时，同一与生起／止息在每种保平衡命名下固定的精确条件由 `World.fixed_iff`、`World.arises_fixed_iff`、'
              '`World.ceases_fixed_iff` 给出；每步之后所立之量区分所有关系项时也固定类别（`World.classes_fixed`）。'
              '`Lineage.world_readings` 与 `Hibernation.world_readings` 保留反例：平衡可同时容许不同的生起与类别。'
              '保持的读法及把守恒读作延续属于 AI 的解释，待 Ren；侵蚀、分裂／合并下的类别与混合普查的充分条件未证明。'
              '[记录](../results/records/identity-across-steps.md)；[研究 §{S_PERSISTENCE}]({STUDY_PERSISTENCE})。')
CHAPTER_EN = ('**Continuity across dormancy and identity fixed by relations (P87).** Read which relations hold through an '
              'inactive step in the same unfolding. For any holding predicate `h`, `Web.persisting h` reads activity by it: '
              'waking from holding is not arising, and keeping the names of what holds fixes one name over each held '
              'stretch and the class of a formation holding throughout. Hibernation makes this stronger than two-way '
              'activity and tenure continuity; Dormancy leaves a join open where nothing holds. Dependence and reserve '
              'give the seed different ending readings, and the census laws retain their separate hypotheses with both '
              'ends read through holding; Sleeper refutes mixing the readings.\n\n'
              'A re-identification balances exactly where its continuation lies within `World.Conserves`, without an '
              'additional hypothesis. In a balanced world this is equality of standing after the step, connected to '
              'exchange likeness. With decidable equality, `World.fixed_iff`, `World.arises_fixed_iff` and '
              '`World.ceases_fixed_iff` give the exact invariants of every balanced naming. Distinct standings at '
              'every step also fix classes. Lineage and Hibernation show balanced namings with different arisings '
              'or classes. The holding and conservation readings await Ren; undermining, classes under splits or '
              'merges and sufficient conditions for a mixed census remain open. '
              '[Record](../results/records/identity-across-steps.md); [study §{S_PERSISTENCE}]({STUDY_PERSISTENCE}).')
OLD_ZH = '- 依存与同一：跨过休眠的连续读法；整体的依存与侵蚀怎样由部分构成；延续关系下的类与侵蚀；整段上对延续关系的精确条件（跨一步的条件已给出，P32）；从关系推出跨步的同一。'
NEW_ZH = '- 依存与同一：P87 给出跨过持续保持的休眠的连续读法与守恒固定同一的精确边界；仍待选保持的关系，未给出混合活动／保持的普查条件、守恒下的侵蚀、分裂／合并下的类与任期；整体的依存与侵蚀怎样由部分构成；整段上对延续关系的精确条件（跨一步的条件已给出，P32）；所立之量相同处及物质、信息或组织连续所需的进一步同一读法。'
OLD_EN = "- Dependence and identity: a reading of continuity across dormancy; how a whole's dependence and undermining are made up of its parts'; class and undermining under continuation relations; an exact condition on continuation relations over a run (across one step it is given, P32); deriving identity across steps from relations."
NEW_EN = "- Dependence and identity: P87 gives continuity through continued holding across dormancy and the exact boundary of identity fixed by conservation; the holding relation remains a choice, and mixed activity/holding census conditions, undermining under conservation, and classes and tenure under splits or merges remain open; how a whole's dependence and undermining are made up of its parts'; an exact condition on continuations over a run (across one step it is given, P32); further identity readings where standings coincide or material, information or organization continuity matters."
CHAPTER_EDITS = [
    ('before', '## 3. 认识与探究 / Knowing and inquiry', CHAPTER_ZH + '\n\n' + CHAPTER_EN),
    ('before', '| 读法 |', '| 休眠与关系所固定的同一（P87） | 保持的名字延续固定始终保持者的类别；平衡改认恰在守恒内，所立之量相异时固定同一，相同处有反例；读法与进一步边界保持开放（[identity-across-steps](../results/records/identity-across-steps.md)） |'),
    ('replace', OLD_ZH, NEW_ZH), ('replace', OLD_EN, NEW_EN),
    ('after_line', '| L3 | [Becoming.Identity]', '| L3 | [Becoming.Persistence]({LEAN}/Persistence.lean) | 休眠中的连续；任意保持读法与同读保持的普查；保平衡改认恰在守恒内，异量固定同一、类别及生起，同量与休眠见证保留边界 | {N_PERSISTENCE} |'),
]
READING = dict(
    after_zh='同一个展开读作萌出或合并时各有一半失效。',
    after_en='one unfolding read as budding or as joining defeating one half each. ',
    zh='保持的名字延续固定跨过休眠而始终保持者的类别；保平衡改认恰在守恒延续内，所立之量相异时固定同一，同量保留选择；保持读法、侵蚀与混合普查仍开放（P87）。',
    en='Keeping the names of what holds fixes classes through held dormancy; balanced re-identifications lie exactly within conservation, distinct standings fix identity and equal standings leave choice; holding readings, undermining and a mixed census remain open (P87). ',
    lean_after='Identity.lean',
)
HISTORY = {}
RECORDS = {}
DELTAS = ['record_delta.py']
