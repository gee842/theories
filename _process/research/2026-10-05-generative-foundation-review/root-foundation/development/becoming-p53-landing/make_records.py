#!/usr/bin/env python3
"""Write the P53 record (experiment-needs-return) into a checkout.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC SECTION P49_SECTION

Reference hashes are the current bytes of ROOT; the receipts' stamps and counts are read from
them. Rerun after any edit to a referenced file, after reading that edit.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REVIEWED, SEC, P49SEC = sys.argv[2:5]
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
EXPERIMENT = f'{D}/Becoming/Experiment.lean'
JOINT = f'{D}/Becoming/Joint.lean'
RECURRENCE = f'{D}/Becoming/Recurrence.lean'
FRAME = f'{D}/Becoming/Frame.lean'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-11-wisdom-from-registration.md'

receipt = json.loads((ROOT / RECEIPT).read_text())
peri = json.loads((ROOT / PERI_RECEIPT).read_text())
assert receipt['status'] == peri['status'] == 'passed'
RUN, PERI_RUN = receipt['utc'], peri['utc']
spine = [m for m in receipt['modules'] if m['spine']]
N_MODULE = next(m for m in receipt['modules'] if m['module'] == 'Becoming.Experiment')['theorems']
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_PKG = len(spine)
N_CORE = len(receipt['core_closure'])
N_INH = len(receipt['inherited_receipts'])


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def zh_en(zh, en):
    return {'zh': zh, 'en': en}


def ref(path, role, declarations=None):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declarations or []}


def binding(path, module):
    return {'source': path, 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def dep(ident, detail, output, inp, conditions, evidence):
    return {'id': ident, 'relation': 'formal-reuse', 'detail': detail,
            'interface': {'output': output, 'input': inp, 'conditions': conditions, 'evidence': evidence}}


def related(ident, detail):
    return {'id': ident, 'detail': detail}


def B(*names):
    return ['Becoming.' + n for n in names]


DECLS = B('Run.Takes', 'Run.StepsOf', 'Run.Fixes', 'Run.fixes_of_takes', 'retarget', 'retarget_determined',
          'retarget_step', 'Run.stepsOf_retarget', 'Run.not_fixes_of_untaken', 'Run.fixes_on_return',
          'Run.ordered_of_ne', 'Run.not_fixes_other_of_new', 'keepHistory', 'keepHistory_length',
          'keepHistory_new', 'keepHistory_determined', 'keepHistory_fixes_nothing_else', 'Run.StepsThrough',
          'Run.FixesThrough', 'Run.fixesThrough_of_takes', 'FactorsThrough', 'Run.stepsThrough_of_factors',
          'Run.generalizes', 'Run.projection_returns', 'Confound.Move', 'Confound.next', 'Confound.process',
          'Confound.states', 'Confound.outcome', 'Confound.determined', 'Confound.move_idle',
          'Confound.hidden_two', 'Confound.aligned', 'Confound.varied', 'Confound.run',
          'Confound.aligned_with_hidden', 'Confound.moveDecides', 'Confound.moveDecides_determined',
          'Confound.misattributes', 'Confound.confounded', 'Confound.varied_refutes')

record = {
    'schema_version': 1,
    'id': 'experiment-needs-return',
    'title': zh_en(
        '实验需要返回：相对于确定性，记录恰在取过之处固定一个动作的结果；自己的动作若换一个会怎样，只在配置返回之处被固定；保留历史的'
        '运行永不返回，所以实验需要一个关于何者无关的模型',
        'Experiment needs return: relative to determinacy, the record fixes a move\'s outcome exactly where it was taken; '
        'what one\'s act would have done otherwise is fixed only where the configuration returns; a kept history never '
        'returns, so experiment needs a model of what is irrelevant'),
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F11',
    'reviewed_at_utc': REVIEWED,
    'claim': zh_en(
        '设 r 是过程 P 的一个运行。相对于确定性，直到某步的记录把动作 a 在配置 s 的结果固定为 u，是指容许 r 在该步之前每一步的每个确定'
        '过程都把 a 在 s 送到 u（Run.Fixes）。运行在某步之前取过 a 于 s，记录就把它固定为运行所到之处（Run.fixes_of_takes）；P 确定、'
        '有两个不同的配置而运行没有取过 a 于 s 时，记录不固定它的任何结果，无论什么被反映：把 a 在 s 改送到任一配置、其余不变的过程仍'
        '确定，并容许运行的每一步（retarget、retarget_determined、Run.stepsOf_retarget、Run.not_fixes_of_untaken）。所以在配置返回之处，'
        '另一个动作的结果被固定（Run.fixes_on_return）；配置永不返回的运行，在经过的每个配置只固定它所取的动作（Run.not_fixes_other_of_new）。'
        '保留其所经配置与动作之历史的过程（keepHistory，Law.withHistory 带动作的对应）中，历史每步长一，所以每步都是新的'
        '（keepHistory_length、keepHistory_new），确定性保持（keepHistory_determined），关于自己的动作除了所做的什么都不固定'
        '（keepHistory_fixes_nothing_else）。经投影 π 读：运行取过 a 于投影为 k 的配置，经投影的记录固定其结果（Run.fixesThrough_of_takes）；'
        'P 的步经 π 分解为确定过程 Q 时（FactorsThrough），所固定的结果就是投影为 k 的每个配置经 π 的结果，无论运行是否经过它'
        '（Run.generalizes）；有限多个投影配置之内，投影从每一步起都返回（Run.projection_returns，revisits_from 的实例）。Confound 中'
        '配置是一个隐藏位与一个结果，每步翻转隐藏位、把结果设为步前的隐藏位，动作不造成差别（Confound.move_idle）；只读结果时，直到第二步'
        '的记录固定左得假、右得真（Confound.misattributes）；动作与隐藏位同步时，“动作决定结果”的确定模型在每一步都容许投影各步'
        '（Confound.confounded）；在隐藏位与第一步不同之处再向左，没有确定过程容许直到第五步的投影各步（Confound.varied_refutes）。'
        '不用 Lean 公理。',
        'Let r be a run of a process P. Relative to determinacy, the record up to a step fixes the outcome of move a at '
        'configuration s to u when every determined process admitting each step of r before it sends a at s to u '
        '(Run.Fixes). Once the run has taken a at s, the record fixes it to where the run went (Run.fixes_of_takes); '
        'where P is determined, there are two different configurations and the run has not taken a at s, the record '
        'fixes no outcome of it, whatever registers: the process sending a at s to any configuration and otherwise as P '
        'is still determined and admits every step of the run (retarget, retarget_determined, Run.stepsOf_retarget, '
        'Run.not_fixes_of_untaken). So where the configuration returns, another move\'s outcome is fixed '
        '(Run.fixes_on_return), and a run whose configurations never return fixes, at each configuration it passes, no '
        'move other than the one it takes (Run.not_fixes_other_of_new). In the process keeping the history of '
        'configurations and moves passed through (keepHistory, the counterpart with moves of Law.withHistory) the past '
        'grows by one at each step, so every step is new (keepHistory_length, keepHistory_new), determinacy is kept '
        '(keepHistory_determined), and nothing about one\'s own acts but what one did is fixed '
        '(keepHistory_fixes_nothing_else). Read through a projection π: once the run has taken a at a configuration '
        'projecting to k, the record so read fixes its outcome (Run.fixesThrough_of_takes); where P\'s step factors '
        'through π into a determined process (FactorsThrough), the fixed outcome is the outcome, read through π, at every '
        'configuration projecting to k, passed by the run or not (Run.generalizes); within finitely many projected '
        'configurations the projection returns from every step on (Run.projection_returns, an instance of '
        'revisits_from). In Confound the configuration is a hidden bit and an outcome, each step flips the hidden bit and '
        'sets the outcome to the hidden bit before the step, and the move makes no difference (Confound.move_idle); read '
        'through the outcome, the record up to the second step fixes left to false and right to true '
        '(Confound.misattributes); with the moves in step with the hidden bit, the determined model in which the move '
        'decides the outcome admits the projected steps at every step (Confound.confounded); moving left again where the '
        'hidden bit differs from the first step, no determined process admits the projected steps up to the fifth '
        '(Confound.varied_refutes). No Lean axiom is used.'),
    'hypotheses': [
        zh_en('固定相对于确定性：比较的是容许记录的确定过程类（Joint.Determined），不是对展开的假设；“未取的不被固定”另要实际过程确定、'
              '有两个不同的配置。',
              'Fixing is relative to determinacy: the comparison is over the class of determined processes admitting the '
              'record (Joint.Determined), not an assumption about the unfolding; “an untaken move is not fixed” further '
              'needs the actual process determined and two different configurations.'),
        zh_en('投影是模型（FactorsThrough），由运行之外给出；有限多个投影配置是写在 projection_returns 中的条件。',
              'The projection is a model (FactorsThrough), supplied from outside the run; finitely many projected '
              'configurations is the condition written into projection_returns.'),
        zh_en('见证的结论：Confound 的过程与运行。', 'For the witness: Confound\'s process and runs.'),
        zh_en('离散的步（从第 0 步计）；配置与动作是任意类型。', 'Discrete steps, counted from step 0; configurations and '
              'moves of any type.'),
    ],
    'correspondence': zh_en(
        'P49 留下的开放项（审查 F6）：一个动作造成什么，是有与无此动作的两段历史的比较。Ren 在 P49 落地后写“land and merge all, then '
        'continue”，看过结果后写“no extra review needed, merge, then continue”。读法（AI 的，待 Ren）：实验是在配置（按实验者的读法）返回'
        '之处变动自己的动作；重复是这一返回；对照是步骤经读法分解的模型；与略去者无关的变动是随机化的结构形式；以 P49 的反映为读法，阈下'
        f'与所及之外的不见是不分解的情形。见整合文档 §{SEC}。',
        'P49\'s open item (review F6): what an act does compares the history with it and the history without it. After '
        'P49 landed Ren wrote “land and merge all, then continue”, and on the result “no extra review needed, merge, then '
        'continue”. Readings (the AI\'s, pending Ren): an experiment is varying one\'s own act where the configuration, '
        'as the experimenter reads it, returns; replication is that return; a control is the model that the step factors '
        'through the reading; variation independent of what is left out is the structural form of randomization; with '
        'P49\'s registration as the reading, threshold and reach blindness are cases where the step does not factor. See '
        f'§{SEC} of the integration note.'),
    'canonical_source': EXPERIMENT,
    'aliases': [*B('Run.Fixes', 'Run.fixes_of_takes', 'Run.not_fixes_of_untaken', 'Run.fixes_on_return',
                   'Run.not_fixes_other_of_new', 'keepHistory', 'keepHistory_new', 'keepHistory_fixes_nothing_else',
                   'Run.FixesThrough', 'FactorsThrough', 'Run.generalizes', 'Run.projection_returns',
                   'Confound.misattributes', 'Confound.confounded', 'Confound.varied_refutes'),
                'experiment', '实验', 'replication', '重复', 'control', '对照', 'confound', '混杂'],
    'dependencies': [
        dep('joint-difference-making',
            zh_en('复用 Determined：动作决定一步。这里问记录在何处固定动作所造成的；Joint 问一个部分是否造成差别。',
                  'Reuses Determined: the move determines the step. Here the question is where the record fixes what a '
                  'move does; Joint asks whether a part makes the difference.'),
            zh_en('确定性。', 'Determinacy.'), zh_en('所比较的过程类。', 'The class of processes compared.'),
            zh_en('无。', 'None.'), JOINT),
        dep('recurrence-without-premise',
            zh_en('复用 revisits_from（投影的返回）与 Law.withHistory 的形式（带动作的 keepHistory）。',
                  'Reuses revisits_from (the projection\'s return) and the form of Law.withHistory (keepHistory with '
                  'moves).'),
            zh_en('有限多个配置之内的返回；保留的历史永不返回。', 'Return within finitely many configurations; a kept '
                  'history never returns.'),
            zh_en('投影的返回；保留历史者只固定所做的。', 'The projection\'s return; a kept history fixes only what was '
                  'done.'),
            zh_en('无。', 'None.'), RECURRENCE),
        dep('testing-within-registration',
            zh_en('推进 P49 的开放项：一个动作造成什么只相对于模型才可检验（Flow.beyond_needs_model）；这里给出展开自身在何处固定它，'
                  '所需的模型是确定性加一次返回，或一个投影。',
                  'Advances P49\'s open item: what an act does is testable only relative to a model '
                  '(Flow.beyond_needs_model); here the unfolding itself fixes it where it returns, the model needed being '
                  'determinacy with one return, or a projection.'),
            zh_en('一个动作的检验需要模型。', 'Testing an act needs a model.'),
            zh_en('实验的条件。', 'The conditions of experiment.'),
            zh_en('无。', 'None.'), f'{D}/Becoming/Testing.lean'),
    ],
    'related': [
        related('scientific-inquiry-foundation', zh_en('这一开放目标的一个部分：在脊柱上陈述实验、重复与对照的结构条件；不确立整个目标。',
                                                       'One part of this open target: the structural conditions of '
                                                       'experiment, replication and control, stated on the spine; it does '
                                                       'not establish the whole target.')),
        related('finite-fallible-inquiry-necessity', zh_en('外围的信息界；这里在脊柱上：记录在何处固定动作的结果。',
                                                           'The periphery\'s information bound; here on the spine: where the '
                                                           'record fixes what an act does.')),
        related('subthreshold-registration', zh_en('那里交换随反映时阈下的差别保持；这里，以反映为投影，阈下的不见是步骤不经所反映者分解的'
                                                   '情形（读法）。',
                                                   'There a difference below the threshold stays where the exchange follows '
                                                   'registration; here, with registration as the projection, blindness '
                                                   'below the threshold is a case where the step does not factor through '
                                                   'what registers (a reading).')),
    ],
    'counterexamples': [
        {'path': EXPERIMENT, 'detail': zh_en(
            '错误的投影误归因而永不被否证：Confound 中动作不造成差别，只读结果时记录固定左得假、右得真；动作与隐藏位同步时，“动作决定结果”的'
            '确定模型在每一步都被容许（Confound.misattributes、Confound.confounded）。只有与隐藏位错开的动作否证它（Confound.varied_refutes）。',
            'A wrong projection misattributes and is never refuted: in Confound the move makes no difference, yet read through '
            'the outcome the record fixes left to false and right to true, and with the moves in step with the hidden bit the '
            'determined model in which the move decides the outcome is admitted at every step (Confound.misattributes, '
            'Confound.confounded). Only moves varied against the hidden bit refute it (Confound.varied_refutes).')},
    ],
    'limitations': zh_en(
        '形成变动其动作、保留或遗忘其历史、形成投影都不推出；实际展开经哪个投影分解是经验问题；随机或不确定的过程没有陈述；全配置的返回在'
        '实际中罕见，正面结果实际上都经投影；与 Becoming.Testing 的反映的形式桥接没有陈述；动作与隐藏者的何种相关使模型永不被否证，一般形式'
        '没有陈述；读法是 AI 的，待 Ren；不含伦理谓词。',
        'That a formation varies its acts, keeps or forgets its history, or forms a projection is not derived; which '
        'projection the actual unfolding factors through is empirical; random or undetermined processes are not treated; '
        'whole configurations rarely return in practice, so the positive results in practice go through projections; the '
        'formal bridge to Becoming.Testing\'s registration is not stated; the general form of which correlation between '
        'moves and what is hidden leaves a model unrefuted is not stated; the readings are the AI\'s, pending Ren; contains '
        'no ethical predicate.'),
    'validation_scope': zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.Experiment 的 {N_MODULE} 项定理全部空依赖，其中含 Run.fixes_of_takes、'
        'Run.not_fixes_of_untaken、keepHistory_fixes_nothing_else、Run.generalizes 与 Confound.varied_refutes；同一回执覆盖包内 '
        f'{N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，{N_INH} 个继承模块的当前字节与已通过回执一致；'
        f'外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、InquirySufficiency、RelationalRenewal、L1–L4 与根模块 '
        f'Becoming）的导入闭包恰为这 {N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq '
        '依赖 propext，没有源声明使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{SEC}；按 Ren 的“no extra review needed”不作独立审查。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {N_MODULE} theorems of Becoming.Experiment all have empty '
        'axiom reports, among them Run.fixes_of_takes, Run.not_fixes_of_untaken, keepHistory_fixes_nothing_else, '
        f"Run.generalizes and Confound.varied_refutes; the same receipt covers the package's {N_PKG} modules (including "
        f'the import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration audits, and {N_INH} inherited '
        f'modules whose current bytes match passed receipts; periphery receipt {PERI_RUN} passed. The checker also '
        'verifies core purity: the import closure of the core (GenerativeCore, InquirySufficiency, RelationalRenewal, '
        f'L1–L4 and the root module Becoming) is exactly these {N_CORE} modules, every source declaration in it has an '
        'empty axiom report (of the constants Lean generates, only the injectivity lemmas of constructors with fields, '
        'injEq, depend on propext; no source declaration uses them, and the checker lists them), and it compiles from '
        "Lean's prelude alone (the foundation's import Std removed for that run). The author's counterreview is in "
        f'§{SEC} of the integration note; at Ren\'s “no extra review needed” there is no independent review.'),
    'references': [
        ref(EXPERIMENT, 'proof', DECLS),
        ref(JOINT, 'proof', B('Determined')),
        ref(RECURRENCE, 'proof', B('revisits_from', 'Law.withHistory', 'Law.orbit')),
        ref(FRAME, 'proof', B('Run')),
        ref(f'{D}/Becoming/Testing.lean', 'proof', B('Flow.beyond_needs_model')),
        ref(RECEIPT, 'receipt'),
        ref(STUDY, 'integration'),
        ref(CHAPTER, 'statement'),
        ref(SOURCE, 'provenance'),
    ],
    'proof_bindings': [binding(EXPERIMENT, 'Becoming.Experiment'), binding(JOINT, 'Becoming.Joint'),
                       binding(RECURRENCE, 'Becoming.Recurrence'), binding(FRAME, 'Becoming.Frame'),
                       binding(f'{D}/Becoming/Testing.lean', 'Becoming.Testing')],
    'next_delta': zh_en(
        '以 Becoming.Testing 的反映为投影的形式桥接：经所反映者的实验何时是对的；动作与隐藏者的何种相关使模型永不被否证的一般形式；'
        '不确定过程中的实验。',
        'The formal bridge with Becoming.Testing\'s registration as the projection: when an experiment through what '
        'registers is right; the general form of which correlation between moves and what is hidden leaves a model '
        'unrefuted; experiment in undetermined processes.'),
    'history': [zh_en(
        '2026-10-11 P53：新增，按 Ren“land and merge all, then continue”与“no extra review needed, merge, then continue”；统一计划 P53；'
        f'回答 P49（§{P49SEC}）的开放项；见整合文档 §{SEC}。',
        '2026-10-11 P53: added, following Ren\'s ‘land and merge all, then continue’ and ‘no extra review needed, merge, then '
        f'continue’; unification plan P53; answers the open item of P49 (§{P49SEC}); see §{SEC} of the integration note.')],
}

path = ROOT / 'theories/becoming/results/records' / f'{record["id"]}.json'
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('wrote', path.relative_to(ROOT))
