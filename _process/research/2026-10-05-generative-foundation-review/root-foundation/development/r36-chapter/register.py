"""R36: the register pass on the decision register (twentieth review F11), English and Chinese.

Each edit is (old, new): every "What would change it" clause that named Ren as the trigger becomes a
condition in the work (a reading of a term argued from Ren's texts, an argument from the work, or a
premise adopted openly); §0 gets a note reading the retired terms and the chapter's former section
numbers in current terms, and its "answered by Ren" paragraph is restated; D14 and D34 are restated
as the AI's readings with Ren's words as their provenance; D10, D11 and D20 get notes in current
terms; headings and index rows drop retired vocabulary, each changed heading keeping its old anchor.
The old wording of every edit is kept here, in OLD of each pair. Each `old` must occur exactly once.

Usage: python3 -B register.py [--apply]   (prints the counts; writes only with --apply)
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path[:0] = [str(ROOT), str(ROOT / 'tools' / 'research')]
from tools.research import moves  # noqa: E402

DC = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
FROZEN = '../../../../theories/becoming/history/THE-THEORY-OF-BECOMING-2026-10-20.md'
NOTE_DATE = '20 October 2026, R36; twentieth review F11'

EN_CLAUSES = [
    ('Ren naming another reading of 生生; a widening part Ren judges degenerative, or the reverse; Ren adopting a measure that orders mixed parts',
     'A reading of 生生, argued from Ren\'s texts, other than this one; a widening part that an argument from the work shows degenerative, or the reverse; a measure that orders mixed parts, adopted openly as a premise beyond widening'),
    ('Ren saying that 生生 names only the direction', 'A reading, argued from Ren\'s texts, under which 生生 names only the direction'),
    ('which Ren judges not 生生', 'which a reading argued from Ren\'s texts shows is not 生生'),
    ('A part Ren judges generative that narrows what can form; Ren defining the pair only at the level of formations',
     'A part that narrows what can form and that an argument from the work shows generative; a reading, argued from Ren\'s texts, that defines the pair only at the level of formations'),
    ('Ren restricting 生 to living formations or to one of the three scopes', 'A reading of 生, argued from Ren\'s texts, restricted to living formations or to one of the three scopes'),
    ('Ren reading 生 only as embodied life.', 'A reading of 生, argued from Ren\'s texts, as embodied life only.'),
    ('Ren reading 生生不息 as endless novelty', 'A reading of 生生不息, argued from Ren\'s texts, as endless novelty'),
    ('Ren counting return as 生生不息 (the decision above then stands); Ren requiring novelty at every step',
     'A reading, argued from Ren\'s texts, that counts return as 生生不息 (the decision above then stands), or that requires novelty at every step'),
    ('Ren reinstating a reading of `living` in the comparison, or choosing a class of drawers for the stepwise reading.',
     'An argument from the work for a reading of `living` in the comparison, or for a class of drawers in the stepwise reading.'),
    ('Ren meaning net inflow by “open”', 'A reading of “open”, argued from Ren\'s texts, as net inflow'),
    ('Ren adopting a valuation of descent, or a measure.', 'A valuation of descent, or a measure, adopted openly as a premise.'),
    ('Ren choosing co-participation; a use of `living` in comparison.', 'An argument from the work for co-participation; a use of `living` in comparison.'),
    ('Ren restricting the axiom to what wants', 'A reading of the condition, argued from Ren\'s texts, restricted to what wants'),
    ('a conveyance relating what Ren would not count as related.', 'a conveyance relating what an argument from the work shows unrelated.'),
    ('Ren reading “not harm” as a constraint on acts rather than a comparison of courses.',
     'A reading of “not harm”, argued from Ren\'s texts, as a constraint on acts rather than a comparison of courses.'),
    ('Ren individuating only members or only lineages;', 'An argument from the work for individuating only members or only lineages;'),
    ('Ren adopting a measure of diversity or complexity', 'A measure of diversity or complexity adopted openly as a premise'),
    ('Ren qualifying “has significance”.', 'A reading of “has significance”, argued from Ren\'s texts, that qualifies it.'),
    ('Ren\'s realizing being not a representation of a boundary but another relation.',
     'A reading of “realizing”, argued from Ren\'s texts, as a relation other than a represented boundary.'),
    ('Ren\'s middle level meaning what one depends on.', 'A reading of the middle level, argued from Ren\'s texts, as what one depends on.'),
    ('Ren\'s “belief” meaning something the presupposition does not state.',
     'A reading of “belief”, argued from Ren\'s texts, under which it means something the presupposition does not state.'),
    ('or another reading of 识 by Ren;', 'or another reading of 识, argued from Ren\'s texts;'),
    ('(1) Another reading of 识 by Ren, or', '(1) Another reading of 识, argued from Ren\'s texts, or'),
    ('(4) Ren saying otherwise of “entangled”.', '(4) another reading of “entangled”, argued from Ren\'s texts.'),
    ('Ren reading “a highly entangled system” as strength alone; a whole with tangled couplings that Ren judges not entangled.',
     'A reading of “a highly entangled system”, argued from Ren\'s texts, as strength alone; a whole with tangled couplings that an argument from the work shows not entangled.'),
    ('Another reading of these terms by Ren;', 'Another reading of these terms, argued from Ren\'s texts;'),
    ('Ren reading 无明 to include the side of the process;', 'A reading of 无明, argued from Ren\'s texts, that includes the side of the process;'),
    ('a name Ren prefers for settling.', 'a name that states settling more exactly.'),
    ('Ren meaning the history itself by “entropy”.', 'A reading of “entropy”, argued from Ren\'s texts, as the history itself.'),
    ('Ren meaning something else by “Fermi\'s diagrams”;', 'A reading of “Fermi\'s diagrams”, argued from Ren\'s texts, as something else;'),
    ('Ren reopening the map of premises.', 'A premise the map does not place, or an argument from the work that reopens the map of premises.'),
    ('Another reading of these sayings by Ren.', 'Another reading of these sayings, argued from Ren\'s texts.'),
    ('Ren saying more of what “situational” means.', 'A reading of “situational”, argued from Ren\'s texts, that this decision does not cover.'),
    ('Ren\'s “continues itself” meaning something other than the source of support.',
     'A reading of “continues itself”, argued from Ren\'s texts, as something other than the source of support.'),
    ('Ren reading the refinement as a change of representation (it would then belong to the representation decisions Ren reserved, section 10), or another reading of amounts.',
     'An argument that the refinement is a change of representation (it would then belong to the representation decisions of section 10), or another reading of amounts.'),
    ('A name whose exact meaning does not match its statement; Ren renaming.',
     'A name whose exact meaning does not match its statement; a better name under the naming criteria.'),
    ('Ren can say otherwise of any of his terms; his words are then the provenance of a further revision, argued from the work.',
     'A further text of Ren\'s on any of his terms is evidence for a revision, argued from the work.'),
]

EN_OTHER = [
    ('not Ren\'s own decision, and Ren can reverse any of them.', 'not Ren\'s own decision, and a better argument revises any of them (D45).'),
    ('If Ren reverses a decision, the reading changes, not the mathematics.', 'If a better argument revises a decision, the reading changes, not the mathematics.'),
    ('Ren can reverse any decision; what changes then is the reading, not the mathematics.',
     'A better argument can revise any decision; what changes then is the reading, not the mathematics.'),
    ('**Answered by Ren, found while deciding.** The following were still listed as open in section 8 or the plan, though Ren\'s words answer them; they are recorded here as Ren\'s words give them, as Ren\'s decisions, not the AI\'s:',
     '**Where Ren\'s words bore on an open item, found while deciding.** The following were still listed as open in section 8 or the plan, though Ren\'s words bear on them; each is decided below as a reading, the AI\'s, with Ren\'s words as its provenance (standard 1 as restated):'),
    # D14
    ('**The level, answered by Ren (not the AI\'s decision).**', '**The level (the AI\'s reading; Ren\'s words of 10 October 2026 its provenance).**'),
    # D34
    ('Ren\'s own words decide this item, not the delegation.', 'Ren\'s words are the provenance of this reading, which stands by the theorems below (D45).'),
    ('was posed after Ren\'s reply and stays Ren\'s (section 10);', 'was posed after Ren\'s reply and is decided with that qualification in the one account (D45);'),
    ('so Ren\'s words now decide this item.', 'so the reading stands by the theorem, and Ren\'s taking it is its provenance.'),
    ('**Reasons.** Ren\'s own words; the theorems\' readings, with their exact bounds.', '**Reasons.** The theorems\' readings, with their exact bounds; Ren\'s words are their provenance.'),
    # index rows
    ('| D11 | S0, range, completion | S0 is wanting; anything (Ren\'s words); N_std |',
     '| D11 | self-significance, range, completion | self-significance is wanting; anything (Ren\'s wording, its provenance); standpoint neutrality |'),
    ('| D14 | level of harm, individuation | the level Ren\'s; lineages to classify, a member\'s ending still a loss |',
     '| D14 | level of harm, individuation | the whole, the system one is in, the self (the AI\'s reading, Ren\'s words its provenance); lineages to classify, a member\'s ending still a loss |'),
    ('| D16 | the axiom, A, G0 | `Unrestricted`; A on living content; the fold answers |',
     '| D16 | the condition, A, living significance | `Unrestricted`; A on living content; living significance a condition |'),
    ('| D18 | route (b) | short of G0\'s scope; both kept |', '| D18 | route (b) | short of living significance\'s scope; both kept |'),
    ('‘situationally’ not read as the bound (Ren\'s words of 15 October)', '‘situationally’ not read as the bound (the AI\'s reading, Ren\'s words of 15 October its provenance)'),
]

EN_HEADINGS = [
    ('## 3. What wants its continuation, and the one axiom', '## 3. What wants its continuation, and the continuation condition'),
    ('### S0, the range of the axiom and the completion', '### Self-significance, the range of the condition and the completion'),
    ('### Reading the axiom, A, and G0', '### Reading the condition, A, and living significance'),
    ('## 4. The route without axiom, feedback and reach', '## 4. The route without the condition, feedback and reach'),
    ('### Route (b) and the axiom', '### Route (b) and the condition'),
    ('## 5. The axiom decomposed, and the generative space', '## 5. The condition decomposed, and the generative space'),
    ('### Registration with any number of conditions, and the tail', '### Coupling with any number of conditions, and the tail'),
]

EN_NOTE_ANCHOR = '**Items asking whether a reading is Ren\'s.**'
EN_NOTE = (
    f'**Terms and section numbers ({NOTE_DATE}).** Each decision keeps the wording of its date and is read in current terms: '
    '“the axiom”, “the one axiom” or “Ren\'s axiom” is the continuation condition (`Unrestricted`), which the theory states and does not assert; '
    'G0 is living significance, a condition; S0 is self-significance; N_rel and N_std are relational and standpoint neutrality; '
    'Part I is the theory without the condition and Part II the conditional section; registration and registers are coupling and couples into; '
    'a question said to stay Ren\'s, or to be Ren\'s to state, is decided in the one account (D45), since no reading waits on Ren. '
    'Section numbers of the theory chapter cited in the decisions are those of the edition before R36, '
    f'[kept in history]({FROZEN}); in the current chapter its 6.1–6.4 and 6.7 are §6.2, 6.5, 6.6 and 6.11 are §6.5, 6.8, 6.12 and 6.15 are §6.4, '
    '6.9 and 6.10 are §6.3, and 6.13 and 6.14 are §6.1, and the old anchors still resolve. '
    'The same day every “What would change it” clause that named Ren as the trigger was restated as a condition in the work: '
    'a reading of a term argued from Ren\'s texts, an argument from the work, or a premise adopted openly; '
    'the earlier wording is kept in the [register pass](development/r36-chapter/register.py).'
)

EN_NOTES_AFTER = [
    # D10
    ('**What would change it.** An argument from the work for co-participation; a use of `living` in comparison.',
     f'**Restated in current terms ({NOTE_DATE}).** (3) “With the axiom read as `Unrestricted` (D16), G0 no longer needs transmission along `related`” reads: '
     'under the continuation condition (chapter §6.4), which the theory does not assert, living significance needs no transmission along `related`, '
     'so the discipline does not bear on it; the Reasons\' “the axiom gives significance directly” reads the same way. The original text above is kept.'),
    # D11
    ('**What would change it.** A reading of the condition, argued from Ren\'s texts, restricted to what wants (lives no standpoint holds are then reached only through formed relations).',
     f'**Restated in current terms ({NOTE_DATE}).** (1) S0 is self-significance, the reading of wanting. (2) “The axiom ranges over anything” reads: '
     'the continuation condition ranges over anything; its wording is Ren\'s and is kept as provenance, and the scope stands by its place in the account (D45), '
     'not because his words settle it. That significance still decides nothing about what anyone should do: practical judgment stays with C, L and J1–J4. '
     '(3) S0 with N_std is self-significance with standpoint neutrality, which the condition gives (chapter §6.4); S0 with N_rel is self-significance with '
     'relational neutrality on a connected whole. The original text above is kept.'),
    # D20
    ('**What would change it.** A reading of the middle level, argued from Ren\'s texts, as what one depends on.',
     f'**Restated in current terms ({NOTE_DATE}).** (2) “Gives the axiom\'s comparison on every part within that reach” reads: gives the continuation '
     'condition\'s comparison on every part within that reach (chapter §6.3; `Flow.Balances.comparison_within_reach`). Ren\'s three levels (the whole, the system '
     'one is in, the self) are the provenance of the three regions, which stand by the closures that read them. The original text above is kept.'),
]

ZH_CLAUSES = [
    ('Ren 另指生生的读法；一个扩大而 Ren 判为退化的部分，或相反；Ren 采用一个给混合部分定序的度量',
     '由 Ren 的文本论证、不同于此的生生读法；一个扩大而由工作的论证表明为退化的部分，或相反；作为扩大之外的前提公开采用、给混合部分定序的度量'),
    ('Ren 说生生只指方向', '由 Ren 的文本论证、生生只指方向的读法'),
    ('、而 Ren 判为不是生生的情形', '、而由 Ren 的文本论证的读法表明不是生生的情形'),
    ('一个 Ren 判为生成而缩小能形成者的部分；Ren 只以形成的层次（更新与消耗）为定义。',
     '一个缩小能形成者、而由工作的论证表明为生成的部分；由 Ren 的文本论证、只以形成的层次（更新与消耗）为定义的读法。'),
    ('Ren 把“生”限于活的形成或三种范围之一', '由 Ren 的文本论证、把“生”限于活的形成或三种范围之一的读法'),
    ('Ren 只把“生”读作体现的生命。', '由 Ren 的文本论证、只把“生”读作体现的生命的读法。'),
    ('Ren 把生生不息读作无尽的新', '由 Ren 的文本论证、把生生不息读作无尽的新的读法'),
    ('Ren 把回返算作生生不息（那时上面的决定成立）；Ren 要求每步都新', '由 Ren 的文本论证的读法：把回返算作生生不息（那时上面的决定成立），或要求每步都新'),
    ('Ren 在比较中恢复 `living` 的某个读法，或为逐步读法另划汲取者的类。', '由工作论证的、在比较中用 `living` 的某个读法，或为逐步读法另划的汲取者之类。'),
    ('Ren 以“开放”指净流入', '由 Ren 的文本论证、以“开放”指净流入的读法'),
    ('Ren 采用对世系的估值，或一个度量。', '作为前提公开采用的对世系的估值，或一个度量。'),
    ('Ren 取共同参与；', '由工作论证的共同参与；'),
    ('Ren 把公理限于想要者', '由 Ren 的文本论证、把延续条件限于想要者的读法'),
    ('一种把 Ren 不算作相关者联系起来的输送。', '一种把由工作的论证表明不相关者联系起来的输送。'),
    ('Ren 把“不损”读作对行动的约束，而不是对进程的比较。', '由 Ren 的文本论证、把“不损”读作对行动的约束而不是对进程的比较的读法。'),
    ('Ren 只以成员或只以谱系个体化；', '由工作论证的、只以成员或只以谱系的个体化；'),
    ('Ren 采用多样性或复杂性的一个度量', '作为前提公开采用的多样性或复杂性的一个度量'),
    ('Ren 给“has significance”加限定。', '由 Ren 的文本论证、给“has significance”加限定的读法。'),
    ('Ren 所说的实现不是一个边界的表示，而是另一种关系。', '由 Ren 的文本论证、把“实现”读作边界的表示之外的另一种关系的读法。'),
    ('Ren 的中间层次是指所依存的。', '由 Ren 的文本论证、把中间层次读作所依存者的读法。'),
    ('Ren 的“belief”所指不是预设所陈述的。', '由 Ren 的文本论证、使“belief”所指不是预设所陈述者的读法。'),
    ('或 Ren 对识的另一读法；', '或由 Ren 的文本论证的识的另一读法；'),
    ('（1）Ren 对识的另一读法，', '（1）由 Ren 的文本论证的识的另一读法，'),
    ('（4）Ren 对“entangled”的另一说明。', '（4）由 Ren 的文本论证的“entangled”的另一读法。'),
    ('Ren 把“a highly entangled system”只读作强度；一个耦合交缠而 Ren 判为不纠缠的整体。',
     '由 Ren 的文本论证、把“a highly entangled system”只读作强度的读法；一个耦合交缠而由工作的论证表明不纠缠的整体。'),
    ('Ren 对这些用语的另一读法；', '由 Ren 的文本论证的这些用语的另一读法；'),
    ('Ren 把无明读作包括过程一侧；', '由 Ren 的文本论证、把无明读作包括过程一侧的读法；'),
    ('Ren 对安定更喜欢的名称。', '更确切地陈述安定的名称。'),
    ('Ren 以“熵”指历史本身。', '由 Ren 的文本论证、以“熵”指历史本身的读法。'),
    ('Ren 对“Fermi\'s diagrams”的另一所指；', '由 Ren 的文本论证的“Fermi\'s diagrams”的另一所指；'),
    ('Ren 重开前提的地图。', '地图不能安放的前提，或重开前提地图的、由工作的论证。'),
    ('Ren 对这些说法的另一读法。', '由 Ren 的文本论证的这些说法的另一读法。'),
    ('Ren 对“situational”的进一步说明。', '由 Ren 的文本论证、本决定未涵盖的“situational”的读法。'),
    ('Ren 的“continues itself”所指不是支持的来源。', '由 Ren 的文本论证、把“continues itself”读作支持的来源之外者的读法。'),
    ('Ren 把细分读作表示的改变（那就属于 Ren 保留的表示决定，§10），或给出量的另一种读法。', '细分是表示的改变的论证（那就属于 §10 的表示决定），或量的另一种读法。'),
    ('一个名称的确切意义与其陈述不合；Ren 的改名。', '一个名称的确切意义与其陈述不合；依命名标准的更好的名称。'),
    ('Ren 可以对他的任何用语另作说明；那时他的话是进一步修订的来源，由工作论证。', 'Ren 关于他任何用语的进一步文本，是修订的证据，修订由工作论证。'),
]

ZH_OTHER = [
    ('不是 Ren 自己的决定；Ren 可以改其中任何一项。', '不是 Ren 自己的决定；更好的论证可以修订其中任何一项（D45）。'),
    ('Ren 改动一项决定，改的是读法，不是数学。', '更好的论证修订一项决定，改的是读法，不是数学。'),
    ('Ren 可以改其中任何一项；改动的是读法，不是数学。', '更好的论证可以修订其中任何一项；改动的是读法，不是数学。'),
    ('**决定时发现已由 Ren 回答的。** 下列几项在第 8 节或计划中仍列为开放，而 Ren 的原话已经回答；这里照原话记录，它们是 Ren 的决定，不是 AI 的：',
     '**决定时发现 Ren 的话所涉及的开放项。** 下列几项在第 8 节或计划中仍列为开放，而 Ren 的原话涉及它们；每项在下面作为读法决定，是 AI 的读法，Ren 的话是其来源（按重述的标准一）：'),
    ('**层次由 Ren 回答（不是 AI 的决定）。**', '**层次（AI 的读法；Ren 2026-10-10 的话是其来源）。**'),
    ('这一项由 Ren 自己的话决定，不由交托决定。', 'Ren 的话是这一读法的来源，读法凭下面的定理成立（D45）。'),
    ('在 Ren 的回答之后提出，仍属 Ren（§10）；', '在 Ren 的回答之后提出，在一个说明中带这一限定决定（D45）；'),
    ('，所以这一项现在由 Ren 的话决定。', '，所以读法凭定理成立，Ren 取它是其来源。'),
    ('**理由。** Ren 自己的话；定理的读法，带其确切的界。', '**理由。** 定理的读法，带其确切的界；Ren 的话是其来源。'),
    ('| D11 | S0、辖域、补全 | S0 即想要；任何东西（Ren 原话）；N_std |', '| D11 | 自身意义、辖域、补全 | 自身意义即想要；任何东西（措辞是 Ren 的，作为来源）；立场中立 |'),
    ('| D14 | 损的层次、形成的个体化 | 层次由 Ren 答；', '| D14 | 损的层次、形成的个体化 | 整体、所在的系统、自身（AI 的读法，Ren 的话是来源）；'),
    ('| D16 | 读出公理、A、G0 | `Unrestricted`；A 读在活的内容上；折叠已答 |', '| D16 | 读出条件、A、生命意义 | `Unrestricted`；A 读在活的内容上；生命意义是一个条件 |'),
    ('| D18 | 路线 (b) | 不足以达到 G0 的辖域；两者都保留 |', '| D18 | 路线 (b) | 不足以达到生命意义的辖域；两者都保留 |'),
    ('“按情境”不读作界（Ren 2026-10-15 的话）', '“按情境”不读作界（AI 的读法，Ren 2026-10-15 的话是来源）'),
]

ZH_HEADINGS = [
    ('## 3. 想要延续者与一条公理', '## 3. 想要延续者与延续条件'),
    ('### D11. S0、公理的辖域与补全', '### D11. 自身意义、条件的辖域与补全'),
    ('### D16. 读出公理、A 与 G0', '### D16. 读出条件、A 与生命意义'),
    ('## 4. 不用公理的路线、反馈与所及', '## 4. 不用条件的路线、反馈与所及'),
    ('### D18. 路线 (b) 与公理', '### D18. 路线 (b) 与条件'),
    ('## 5. 公理的分解与生成的空间', '## 5. 条件的分解与生成的空间'),
]

ZH_NOTE_ANCHOR = '**问“某读法是否是 Ren 的读法”的项。**'
ZH_NOTE = (
    '**用语与节号（2026-10-20，R36；第二十次审查 F11）。** 每项决定保留其日期的措辞，按现行用语读：'
    '“公理”“一条公理”“Ren 的公理”是延续条件（`Unrestricted`），理论陈述而不断言它；G0 是生命意义，一个条件；S0 是自身意义；'
    'N_rel 与 N_std 是关系中立与立场中立；第一部分是不用条件的理论，第二部分是条件一节；识及、识（registration）是耦合入、耦合；'
    '决定中说仍属 Ren、或由 Ren 陈述的问题，在一个说明中决定（D45），因为没有读法等待 Ren。'
    f'决定中所引理论章节的节号是 R36 之前一版的节号（[保存在历史中]({FROZEN})）；在现行章节中，其 6.1–6.4 与 6.7 是 §6.2，'
    '6.5、6.6 与 6.11 是 §6.5，6.8、6.12 与 6.15 是 §6.4，6.9 与 6.10 是 §6.3，6.13 与 6.14 是 §6.1，旧锚点仍可解析。'
    '同日，凡以 Ren 为触发者的“会改变它的”条款，都重述为工作中的条件：由 Ren 的文本论证的用语读法、由工作的论证，或公开采用的前提；'
    '原措辞保存在[登记处理](development/r36-chapter/register.py)中。'
)

ZH_NOTES_AFTER = [
    ('**会改变它的。** 由工作论证的共同参与；比较中用到 `living`。',
     '**以现行用语重述（2026-10-20，R36；第二十次审查 F11）。** 三中“公理读作 `Unrestricted`（D16）时，G0 不再需要沿 `related` 传递”读作：'
     '在延续条件之下（章节 §6.4，理论不断言它），生命意义不需要沿 `related` 传递，所以纪律不影响它；理由中的“公理直接给出意义”同样读。上面的原文保留。'),
    ('**会改变它的。** 由 Ren 的文本论证、把延续条件限于想要者的读法（那时无人持有的生命只经已形成的关系到达）。',
     '**以现行用语重述（2026-10-20，R36；第二十次审查 F11）。** 一、S0 是自身意义，即“想要”的读法。二、“公理的辖域是任何东西”读作：延续条件的辖域是任何东西；'
     '措辞是 Ren 的，作为来源保留，辖域凭它在说明中的位置成立（D45），不是因为他的话决定了它。这一意义仍不决定任何人该做什么：实践判断仍由 C、L 与 J1–J4 处理。'
     '三、S0 加 N_std 是自身意义加立场中立，由条件给出（章节 §6.4）；S0 加 N_rel 是连通整体上的自身意义加关系中立。上面的原文保留。'),
    ('**会改变它的。** 由 Ren 的文本论证、把中间层次读作所依存者的读法。',
     '**以现行用语重述（2026-10-20，R36；第二十次审查 F11）。** 二中“给出公理的比较”读作：在所及之内的每个部分上给出延续条件的比较（章节 §6.3；'
     '`Flow.Balances.comparison_within_reach`）。Ren 的三个层次（整体、所在的系统、自身）是三个区域的来源，区域凭读出它们的闭包成立。上面的原文保留。'),
]


def apply(path, clauses, other, headings, note_anchor, note, notes_after):
    text = path.read_text()
    counts = {'clauses': 0, 'other': 0, 'headings': 0, 'notes': 0}
    for old, new in clauses + other:
        n = text.count(old)
        if n != 1:
            raise SystemExit(f'{path.name}: expected one occurrence, found {n}: {old[:80]}')
        text = text.replace(old, new)
        counts['clauses' if (old, new) in clauses else 'other'] += 1
    for old, new in headings:
        lines = text.split('\n')
        k = [i for i, l in enumerate(lines) if l == old]
        if len(k) != 1:
            raise SystemExit(f'{path.name}: heading not found once: {old}')
        i = k[0]
        alias = f'<a id="{moves.github_slug(old.lstrip("#").strip())}"></a>'
        lines[i] = new
        if alias not in lines[max(0, i - 4):i]:
            lines.insert(i, alias)
        text = '\n'.join(lines)
        counts['headings'] += 1
    if note_anchor and text.count(note_anchor) == 1 and note not in text:
        text = text.replace(note_anchor, note + '\n\n' + note_anchor)
        counts['notes'] += 1
    for after, add in notes_after:
        if text.count(after) != 1:
            raise SystemExit(f'{path.name}: note anchor not found once: {after[:80]}')
        if add not in text:
            text = text.replace(after, after + '\n\n' + add)
            counts['notes'] += 1
    return text, counts


def main():
    en, ce = apply(DC / 'DELEGATED-CHOICES.md', EN_CLAUSES, EN_OTHER, EN_HEADINGS, EN_NOTE_ANCHOR, EN_NOTE, EN_NOTES_AFTER)
    zh, cz = apply(DC / 'DELEGATED-CHOICES.zh.md', ZH_CLAUSES, ZH_OTHER, ZH_HEADINGS, ZH_NOTE_ANCHOR, ZH_NOTE, ZH_NOTES_AFTER)
    left_en = len(re.findall(r'\*\*What would change it\.\*\*[^*]*\bRen\b(?! *\(\[)', en))
    print('EN', ce, 'ZH', cz)
    if '--apply' in sys.argv:
        (DC / 'DELEGATED-CHOICES.md').write_text(en)
        (DC / 'DELEGATED-CHOICES.zh.md').write_text(zh)
        print('written')


if __name__ == '__main__':
    main()
