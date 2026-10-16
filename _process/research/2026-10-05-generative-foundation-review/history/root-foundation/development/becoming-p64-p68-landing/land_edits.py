#!/usr/bin/env python3
"""Landing edits for P64–P68 in a checkout W: copy the four modules, apply capture.patch, and edit the
root module, the checker's CORE and scope, and the Lean README. Usage: python3 -B land_edits.py W"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
PKG = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/becoming-p64-p68-landing'
B = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'

for m in ('Attraction', 'Mechanism', 'Response', 'Selection'):
    shutil.copyfile(PKG / f'lean/Becoming/{m}.lean', B / f'Becoming/{m}.lean')
subprocess.run(['git', 'apply', str(PKG / 'capture.patch')], cwd=W, check=True)
assert (B / 'Becoming/Capture.lean').read_bytes() == (PKG / 'lean/Becoming/Capture.lean').read_bytes()


def edit(path, pairs):
    s = path.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path.name, a[:80], s.count(a))
        s = s.replace(a, b)
    path.write_text(s)
    print('edited', path.relative_to(W))


def declared(module, names):
    text = (B / f'Becoming/{module}.lean').read_text()
    for n in names:
        last = n.split('.')[-1]
        assert (re.search(rf'^(theorem|def|structure|inductive|abbrev|lemma)\s+\S*{re.escape(last)}\b', text, re.M)
                or re.search(rf'^namespace {re.escape(n)}$', text, re.M)), (module, n)


BULLET_L3 = """* `Becoming.Mechanism` (L3): a projection of configuration carries a determined law exactly
  where configurations alike under it go alike, the image of the step being the least
  candidate; what the step does not depend on is re-absorbed in one step; a system changing its
  own rule is one determined process on the joint configuration, and the state has a law of its
  own exactly where the rule makes no difference to it; a law through a projection is not fixed
  where not yet taken. The standard causal model x′ = F(x, u, ε) is a determined process whose
  move is the input and the noise: an intervention is a move not taken, noise a move not
  represented. The readings are the AI's, pending Ren.
* `Becoming.Attraction` (L3): for every determined law, with no premise, a configuration is
  drawn into an absorbing region exactly where it does not return, and what is drawn in never
  comes back; what can be had n steps on is absorbing and every lost possibility is drawn into
  it; of two merged configurations not both return; within finitely many configurations
  attraction is merging and what returns draws in everything else, while an open world
  separates them; under a process, entering an invariant region locks in. The readings are the
  AI's, pending Ren.
"""
BULLET_L4 = """* `Becoming.Response` (L4): where the rest responds through its registration, a supplied
  premise, the comparison is decided within the part's responsive reach, its closure under
  affecting what is registered: the dual of the registration closure, and, registering support
  only, the union of the members' reach closures. Beyond it every formation registers and
  exchanges alike. The readings are the AI's, pending Ren.
* `Becoming.Selection` (L4): two histories are selected alike by every selection through a
  selector's registration exactly when it registers them alike; with the rest fixed, selection
  is blind beyond the registration closure, so an ending within a candidate's reach closure and
  beyond the selector's registration closure is not selected, while pooled registration selects
  it; where reaching beyond raises what registers, selection favours it. The readings are the
  AI's, pending Ren.
"""
root = B / 'Becoming.lean'
edit(root, [
    ('import Becoming.Experiment\n', 'import Becoming.Experiment\nimport Becoming.Mechanism\nimport Becoming.Attraction\n'),
    ('import Becoming.Runaway\n', 'import Becoming.Runaway\nimport Becoming.Response\nimport Becoming.Selection\n'),
    ('* `Becoming.Substitution` (L3):', BULLET_L3 + '* `Becoming.Substitution` (L3):'),
    ('* `Becoming.Boundaries` (L4):', BULLET_L4 + '* `Becoming.Boundaries` (L4):'),
    ("""  where the next configuration depends on the rule and not the state, reforming the state alone
  is re-absorbed. The readings are the AI's, pending Ren.""",
     """  where the next configuration depends on the rule and not the state, reforming the state alone
  is re-absorbed, the instance of `Becoming.Mechanism`'s re-absorption with the rule as the
  projection. The readings are the AI's, pending Ren."""),
])

SCOPE_L3 = (
    '    "Mechanism: a projection of configuration carries a determined law exactly where configurations "\n'
    '    "alike under it go alike under it, the image of the step being the least process the step factors "\n'
    '    "through; what the step does not depend on is re-absorbed in one step, Capture\'s rule holding the "\n'
    '    "outcome being the instance with the rule as the projection; a system changing its own rule is one "\n'
    '    "determined process on the joint configuration, the state having a law of its own exactly where "\n'
    '    "the rule makes no difference to it; a law through a projection is not fixed where not yet taken; "\n'
    '    "the standard model x\' = F(x, u, e) is a determined process whose move is the input and the noise, "\n'
    '    "an intervention is a move not taken and noise a move not represented, the model with the noise "\n'
    '    "forgotten being determined exactly where the noise makes no difference. "\n'
    '    "Attraction: for every determined law, with no premise, a configuration is drawn into an absorbing "\n'
    '    "region exactly where it does not return, and what is drawn in never comes back; what can be had n "\n'
    '    "steps on is absorbing and every possibility lost by step n is drawn into it; of two merged "\n'
    '    "configurations not both return; within finitely many configurations attraction is merging and "\n'
    '    "what returns draws in everything else, while counting on draws without merging; under any "\n'
    '    "process, once inside an invariant region what lies outside cannot be had again, and leaving a "\n'
    '    "region needs a move that does not keep it. "\n')
SCOPE_L4 = (
    '    "Response: where every formation outside a part exchanges alike across each step up to which it "\n'
    '    "has registered alike, a supplied premise of which the rest held fixed is a case, every formation "\n'
    '    "beyond the part\'s responsive reach, its closure under affecting what is registered, registers and "\n'
    '    "exchanges alike, the difference between two flows reaches none of them and the comparison is "\n'
    '    "decided within the reach; registering support only, with one flow, the responsive reach is the "\n'
    '    "union of the members\' reach closures; in the trophic cascade it is the wolves, the deer and the "\n'
    '    "forest, and in a two-party loop the difference returns to the part\'s own support. "\n'
    '    "Selection: two histories are selected alike by every selection through a selector\'s registration "\n'
    '    "exactly when the selector registers them alike, and likewise for pooled registration; with the "\n'
    '    "rest fixed, selection and scoring are blind beyond the registration closure; the clearer\'s "\n'
    '    "selection misses the dweller\'s ending, which the dweller\'s and the pooled registration select; a "\n'
    '    "flow reaching beyond the registration closure to raise a gauged store is selected, alike with "\n'
    '    "raising it without reaching beyond; selection supplying the carriers, their share rises among "\n'
    '    "descendants. "\n')
edit(B / 'check_becoming.py', [
    ('"Becoming.Experiment",', '"Becoming.Experiment", "Becoming.Mechanism", "Becoming.Attraction",'),
    ('"Becoming.Runaway",', '"Becoming.Runaway", "Becoming.Response", "Becoming.Selection",'),
    ('    "Substitution: in the support-gated law,', SCOPE_L3 + '    "Substitution: in the support-gated law,'),
    ('    "Boundaries: along a relation a boundary of a formation', SCOPE_L4 + '    "Boundaries: along a relation a boundary of a formation'),
    ('    "is re-absorbed from the next step on. "\n',
     '    "is re-absorbed from the next step on, the instance of Mechanism\'s re-absorption with the rule as "\n'
     '    "the projection. "\n'),
])

ROWS = {
    'Mechanism': ('L3', [
        'carries_law_iff', 'Image.least', 'Coarse', 'Switching', 'DependsOnlyOn.reabsorbed', 'Law.reabsorbed',
        'adaptive_state_law_iff', 'Switching.no_state_law', 'Run.not_fixesThrough_of_goAlike',
        'inputs_intervention_unfixed', 'forget_inputs_determined_iff'],
        '机制与标准因果模型（不加前提）：投影承载确定的规律，恰当经它相同的配置同去（`carries_law_iff`），步骤经投影读的像是它分解到的最小过程（`Image.least`）；承载规律对描述变粗变细都不单调（`Coarse`、`Switching`）；所不依者一步之内被重新吸收（`DependsOnlyOn.reabsorbed`、`Law.reabsorbed`；`Becoming.Capture` 的 `Law.reform_reabsorbed` 是它以规则为投影的实例）；改变自身规则的系统是联合配置上的确定过程，状态恰在规则对它不造成差别之处有自己的规律（`adaptive_state_law_iff`、`Switching.no_state_law`）；经投影的规律在未取之处不被固定（`Run.not_fixesThrough_of_goAlike`）；x′ = F(x, u, ε) 是动作为输入与噪声的确定过程，干预是未取的动作，噪声是未表示的动作（`inputs_intervention_unfixed`、`forget_inputs_determined_iff`）；读法是 AI 的，待 Ren',
        "a projection carries a determined law exactly where configurations alike under it go alike (`carries_law_iff`), the image of the step being the least candidate (`Image.least`); carrying a law is monotone neither toward coarser nor toward finer descriptions (`Coarse`, `Switching`); what the step does not depend on is re-absorbed in one step (`DependsOnlyOn.reabsorbed`, `Law.reabsorbed`; `Becoming.Capture`'s `Law.reform_reabsorbed` is its instance with the rule as the projection); a system changing its own rule is one determined process on the joint configuration, and the state has a law of its own exactly where the rule makes no difference to it (`adaptive_state_law_iff`, `Switching.no_state_law`); a law through a projection is not fixed where not yet taken (`Run.not_fixesThrough_of_goAlike`); x′ = F(x, u, ε) is a determined process whose move is the input and the noise, an intervention a move not taken and noise a move not represented (`inputs_intervention_unfixed`, `forget_inputs_determined_iff`); the readings are the AI's, pending Ren"),
    'Attraction': ('L3', [
        'Law.drawn_iff_not_returns', 'Law.DrawnInto.never_back', 'Law.reachable_absorbing', 'Law.lost_drawn',
        'Law.Merges.not_both_return', 'Law.lossless_iff_none_drawn', 'Law.drawnInto_returning',
        'Law.succ_drawn_lossless', 'Invariant.locks_out', 'Run.leaving_needs'],
        '吸引与锁定（不加前提）：对每个确定的律，配置被某个吸收区域吸入恰当它不返回（`Law.drawn_iff_not_returns`），被吸入者不再回来（`Law.DrawnInto.never_back`）；n 步后可得者是吸收区域，丧失的可能被吸入它（`Law.reachable_absorbing`、`Law.lost_drawn`）；被合并的两个配置不都返回，不需要有限性（`Law.Merges.not_both_return`）；有限多配置之内吸引即合并，返回者的区域吸入其余一切，开放的世界把两者分开（`Law.lossless_iff_none_drawn`、`Law.drawnInto_returning`、`Law.succ_drawn_lossless`）；过程中进入不变区域即锁定，离开需要不保持它的动作（`Invariant.locks_out`、`Run.leaving_needs`）；读法是 AI 的，待 Ren',
        'for every determined law, with no premise, a configuration is drawn into an absorbing region exactly where it does not return (`Law.drawn_iff_not_returns`), and what is drawn in never comes back (`Law.DrawnInto.never_back`); what can be had n steps on is absorbing and every lost possibility is drawn into it (`Law.reachable_absorbing`, `Law.lost_drawn`); of two merged configurations not both return, with no finiteness (`Law.Merges.not_both_return`); within finitely many configurations attraction is merging and what returns draws in everything else, while an open world separates them (`Law.lossless_iff_none_drawn`, `Law.drawnInto_returning`, `Law.succ_drawn_lossless`); under a process, entering an invariant region locks in, and leaving needs a move that does not keep it (`Invariant.locks_out`, `Run.leaving_needs`); the readings are the AI\'s, pending Ren'),
    'Response': ('L4', [
        'Flow.RespondsThroughRegistration', 'Flow.withinResponse_iff_registration', 'Flow.withinResponse_supportOnly_iff',
        'Flow.alike_beyond_response', 'Flow.not_differs_beyond_response', 'Flow.Balances.comparison_within_response',
        'Trophic.within_response_iff', 'Loop.returns'],
        '其余回应时的比较（不用公理；经识回应 `Flow.RespondsThroughRegistration` 是给出的前提，其余固定是它的情形）：回应所及是部分对经所识者影响的闭包，与识闭包对偶，只识支持、一个流时恰是成员所及闭包之并（`Flow.withinResponse_iff_registration`、`Flow.withinResponse_supportOnly_iff`）；回应所及之外的每个形成识得相同、交换相同，差别到不了它（`Flow.alike_beyond_response`、`Flow.not_differs_beyond_response`），比较在回应所及之内决定（`Flow.Balances.comparison_within_response`）；营养级联中回应所及恰是狼群、鹿与森林（`Trophic.within_response_iff`）；两方回路中差别经回应回到部分自身的支持（`Loop.returns`）；读法是 AI 的，待 Ren',
        "the comparison where the rest responds (no axiom; responding through registration, `Flow.RespondsThroughRegistration`, is a supplied premise, the rest held fixed a case of it): the responsive reach is the part's closure under affecting what is registered, the dual of the registration closure, and, registering support only with one flow, exactly the union of the members' reach closures (`Flow.withinResponse_iff_registration`, `Flow.withinResponse_supportOnly_iff`); every formation beyond it registers and exchanges alike and the difference reaches none of them (`Flow.alike_beyond_response`, `Flow.not_differs_beyond_response`), so the comparison is decided within it (`Flow.Balances.comparison_within_response`); in the trophic cascade the responsive reach is exactly the wolves, the deer and the forest (`Trophic.within_response_iff`); in a two-party loop the difference returns to the part's own support (`Loop.returns`); the readings are the AI's, pending Ren"),
    'Selection': ('L4', [
        'Web.selects_alike_iff', 'Flow.unselected_beyond_registration', 'Clearing.unselected', 'Clearing.selected_pooled',
        'Diversion.favours', 'Diversion.blind_to_source', 'share_rises_through'],
        '经识的选择（不用公理，选择经识是写在定理中的条件）：两段历史被每个经选择者之识的选择选得相同，恰当选择者把它们识得相同，合起来的识亦然（`Web.selects_alike_iff`）；其余交换固定时，选择与评分在识闭包之外不见（`Flow.unselected_beyond_registration`）；清除者的选择不见栖居者的终结，栖居者之识与合起来的识选出它（`Clearing.unselected`、`Clearing.selected_pooled`）；伸出识闭包之外而抬高所识存储的流被选中，且与不伸出的抬高选得相同（`Diversion.favours`、`Diversion.blind_to_source`）；选择给出携带者时后代中的份额上升（`share_rises_through`，`share_rises` 的应用）；读法是 AI 的，待 Ren',
        "selection through registration (no axiom; that a selection goes through registration is a condition written into the theorems): two histories are selected alike by every selection through a selector's registration exactly when the selector registers them alike, and likewise for pooled registration (`Web.selects_alike_iff`); with the rest of the exchange fixed, selection and scoring are blind beyond the registration closure (`Flow.unselected_beyond_registration`); the clearer's selection misses the dweller's ending, which the dweller's and the pooled registration select (`Clearing.unselected`, `Clearing.selected_pooled`); a flow reaching beyond the registration closure to raise a gauged store is selected, alike with raising it without reaching beyond (`Diversion.favours`, `Diversion.blind_to_source`); selection supplying the carriers, their share rises among descendants (`share_rises_through`, an application of `share_rises`); the readings are the AI's, pending Ren"),
}


def row(m):
    layer, names, zh, en = ROWS[m]
    declared(m, names)
    return f'| {layer} | [`Becoming.{m}`](Becoming/{m}.lean) | {zh} / {en} |\n'


readme = B / 'README.md'
s = readme.read_text()


def after_row(s, module, text):
    i = s.index(f'| [`Becoming.{module}`](Becoming/{module}.lean) |')
    i = s.rindex('\n', 0, i) + 1
    j = s.index('\n', i) + 1
    return s[:j] + text + s[j:]


s = after_row(s, 'Experiment', row('Mechanism') + row('Attraction'))
s = after_row(s, 'Runaway', row('Response') + row('Selection'))
readme.write_text(s)
edit(readme, [
    ('`Experiment` 导入 `Joint` 与 `Recurrence`；', '`Experiment` 导入 `Joint` 与 `Recurrence`；`Mechanism` 导入 `Experiment`；`Attraction` 导入 `Recurrence`；'),
    ('`Capture` 导入 `Evolution`、`Locality` 与 `Recurrence`；', '`Capture` 导入 `Evolution`、`Locality`、`Recurrence` 与 `Mechanism`；'),
    ('`Runaway` 导入 `Testing`；', '`Runaway` 导入 `Testing`；`Response` 导入 `Testing`；`Selection` 导入 `Testing` 与 `Capture`；'),
    ('`Experiment` imports `Joint` and `Recurrence`;', '`Experiment` imports `Joint` and `Recurrence`; `Mechanism` imports `Experiment`; `Attraction` imports `Recurrence`;'),
    ('`Capture` imports `Evolution`, `Locality` and `Recurrence`;', '`Capture` imports `Evolution`, `Locality`, `Recurrence` and `Mechanism`;'),
    ('`Runaway` imports `Testing`;', '`Runaway` imports `Testing`; `Response` imports `Testing`; `Selection` imports `Testing` and `Capture`;'),
    ('（`Law.reform_reabsorbed`、`Captured`）', '（`Law.reform_reabsorbed`，`Becoming.Mechanism` 的 `Law.reabsorbed` 以规则为投影的实例；`Captured`）'),
    ('(`Law.reform_reabsorbed`, `Captured`)', "(`Law.reform_reabsorbed`, the instance of `Becoming.Mechanism`'s `Law.reabsorbed` with the rule as the projection; `Captured`)"),
])
