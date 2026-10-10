# 登记与检验：反馈的三种不见 / Registration and testing: three blindnesses of feedback

2026-10-11，Asia/Bangkok。AI（Claude Opus 5.5）应 Ren 的提议撰写的研究笔记与计划。Ren 写道（[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-wisdom-from-registration.md)）：

> I am suddenly having a great idea: can becoming provide wisdoms to avoid run away feedbacks and the identification of knowledge, learning, and scientific principles like falsifiability
>
> I think all the wisdoms about wisdoms, how to think, learn, update, are all explained within what we have, if not not proved yet

本文是计划：不向核心加入定理，不登记成果。下面的“已检查”都指脊柱上已有的 Lean 定理；“读法”是 AI 的，待 Ren；“待证”是拟议的陈述。

**状态（P49）。** Ren 答“agree with you, great job, start now. for 4, you can explore which option is better, then make decision”，这一阶段已作为统一计划 P49 完成（起草时编为 P47）：模块 `Becoming.Testing`，结果、审查的收窄与第 4 问的决定见 §7 与[研究 §{S}](BECOMING-RENEWAL-READING.md#{ANCHOR})。§0–§6 是阶段开始之前写的计划，保留原文；其中的读法与拟议陈述已被 §7 收窄或取代。

**Status (P49).** Ren answered “agree with you, great job, start now. for 4, you can explore which option is better, then make decision”, and the stage is done as unification plan P49 (drafted as P47): module `Becoming.Testing`; the results, the review's narrowing and the decision on question 4 are in §7 and study section {S}. Sections 0–6 are the plan as written before the stage and are kept as written; §7 narrows or replaces their readings and proposed statements.

2026-10-11, Asia/Bangkok. A research note and plan written by the AI (Claude Opus 5.5) on Ren's proposal. Nothing enters the core and no result is registered. "Checked" cites Lean theorems already on the spine, "reading" is the AI's (pending Ren), and "to prove" marks a proposed statement.

## 0. 摘要 / Summary

**中文。** 脊柱已经含有这一提议的根。一个形成能登记的，只是跨过它所依存者的交换；它经由支持所登记的，有三种不见：
- **阈下不见**：水平在跌破需要之前不改变支持；
- **视界外不见**：有限的历史不判定一种活法是更新还是消耗；
- **不返之不见**：作用所及而不在影响闭包之内者，永不登记。

失控的反馈，是在这三种不见之一中运行的回路。认识、学习与科学是跨过这三种不见而登记的方式：
- 量度读出阈下的水平；
- 作出可被否证之预测的延续模型越过视界；
- 他者的登记与仪器扩大所及。

可否证性因此不是外加于科学的方法规则：它就是被展开纠正的条件，即一个主张与其对手在所能登记之处有所不同。这些都在第一部分之内，不用公理。不伤及永不返回者，则需要覆盖所及的意义（Ren 的“所在的系统”）或第二部分的公理。

**English.** The spine already holds the root of the proposal. What can register in a formation is only exchange across what it depends on. Feedback through support has three blindnesses:
- **threshold blindness**: a level does not change support until it falls below the need;
- **horizon blindness**: no finite history decides whether a way of drawing renews or consumes;
- **reach blindness**: what the formation's exchange reaches outside its influence closure never registers.

A runaway is a loop that runs inside one of these blindnesses. Knowing, learning and science are the ways of registering across them:
- measurement registers the level below the threshold;
- models of continuation with refutable predictions cross the horizon;
- others' registration and new instruments widen the reach.

Falsifiability is then not a method rule added to science. It is the condition of being corrected by the unfolding: a claim and its rivals must differ somewhere that can register. All of this is Part I, with no axiom. Not harming what never returns needs significance that covers reach, Ren's "system that one is in" (P42), or Part II's axiom.

## 1. 根：已检查的 / The root: what is already checked

**Registration** (P42, `Becoming.Feedback`, on branch `p42-p43-feedback-boundaries`, commit c9c219e3, not yet on main):
- `Flow.Balances.support_agrees`: in balanced flows, a formation's support registers only its exchanges with what it depends on.
- `Flow.Balances.agrees_iff_even`: a part registers on a condition exactly through its net exchange with it, so different activity with the same net is indistinguishable there.
- `Flow.Balances.unregistered_beyond_influence`: nothing whose members lie beyond a formation's influence closure registers in it.
- `Clearing.unregistered` (witness): the clearer's support is the same at every step whether or not its clearing ends the dweller.
- `Margin.reach_without_misjudgment` (witness): reach is not sufficient for registration.

**Threshold** (main):
- `Web.supported_iff_admits` (`Becoming.Admission`): support is admission by the levels of required conditions, a threshold on each.
- `Carries.lasts` (`Becoming.Reserve`): a reserve defers the end and does not escape it.
- `Flow.Balances.consumption_ends_with_feeders` (`Becoming.Interdependence`): consumption fed only by unsupported feeders lasts at most as many steps as the level it consumes.

**Horizon** (main, `Becoming.Horizon`):
- `prefix_does_not_decide`: for every horizon `h`, a renewing run and a consuming run agree up to `h`.
- `Feedback.prefix_does_not_decide`: the same holds in the support-gated law. The renewing schedule never reaches the threshold below which renewal stops, so feedback does not change the result.
- The module's own reading: classifying a stretch of drawing requires an account of where the run goes, not only its past.

**Enclosure** (main):
- `rise_with_fall`: across a dissipated step, a rise comes with a fall in the same family.
- `World.comes_to_rest` and `World.arising_opens`: under enclosure, change comes to rest, and arising without end needs openness.
- `Clearing.closure_supported`: a loss beyond the feeding closure need not return.

**Judgment** (main, `Becoming.Inquiry`):
- `commonResponse_judge_iff`: judgment under uncertainty is a one-step inquiry.
- `commonResponse_antitone`: refining observation narrows belief and keeps every common response.

## 2. 推出什么 / What follows

**(a) Runaway feedback.** [reading, built on checked pieces]
- Reinforcement is not the danger; the meta-attractor's claim 33 already holds that self-reinforcement is direction-neutral.
- Inside an enclosure, every rise is a fall elsewhere and change comes to rest (checked). A loop that keeps going draws from beyond its enclosure (checked).
- The danger is the open loop. The loop's gains register in it. Its losses do not: they either fall beyond its influence closure (reach blindness) or stay inside its reserve until the break (threshold blindness).
- And no prefix tells overdraw that will stop from overdraw that will not (horizon blindness).
- So steering by feedback alone cannot tell a runaway from a sustainable draw. That the three blindnesses hold is checked; the general statement about policies is T5 (to prove).

On the AI's reading, Ren's 心 and 理 (2026-10-04, 「不能让正反馈循环失控」) fit here:
- 心's loop registers through support;
- 理 is the model that registers what support cannot: the level, where the run goes, and what the reach does.

This reading is pending Ren.

**(b) Knowledge and learning.** [reading; partly checked]
- Learning is a change of organization through what registers.
- Reasoning over the same registration cannot make a new distinction. Checked forms: `support_agrees` here, and the periphery's information bound [finite-fallible-inquiry-necessity](../../../../theories/becoming/results/records/finite-fallible-inquiry-necessity.md).
- Updating keeps whatever was robust (`commonResponse_antitone`, checked).
- Survival is not truth: two formations with different unexercised contents have the same support (`support_agrees`). This is also the preserved counterexample in [SCIENTIFIC-PHILOSOPHY §3.4](../../../../theories/becoming/chapters/SCIENTIFIC-PHILOSOPHY.md).

**(c) Falsifiability.** [to prove: T2–T4] A claim is testable by a formation exactly where the claim and its rivals differ in what can register in that formation. This sharpens Popper in three ways:
- **It is relational.** "My clearing ends the dweller" cannot be refuted from the clearer's support, and can be from the dweller's (`Clearing.unregistered`). Criticism is registration from another position. This gives Longino's social objectivity a structural form.
- **It moves with reach.** An instrument is a new exchange, so a claim untestable today can become testable.
- **Long-run claims are untestable from the record.** "I am renewing" is never refuted by a prefix (`prefix_does_not_decide`). Only a model of continuation makes it testable: it predicts levels that register. So avoiding a runaway needs models with risky predictions, not track records.

**(d) The theory applies to itself.** [reading]
- Each premise carves a proper part of the space (`World.contingent`, checked), so each premise is falsifiable.
- The laws of the whole exclude no unfolding beyond what the representation excludes. So they are necessary and not empirical. For counting this is checked (`tally_iff_counted`, `counting_laws`). In general it is a remark of the chapter, not a Lean statement.
- So Part I already has Popper's demarcation as its architecture: the whole is necessary, and its parts are empirical. This meets Ren's "the theory of becoming is deductively necessary; generative is a part of its manifold".

**(e) Dogmatism, the meta-attractor and capability outrunning correction.** [reading]
- These have one structure: a formation's reach widens while what registers in it narrows. It may suppress critics, or edit the rules that would report its losses.
- The structure is the same at the cognitive, institutional and ecological scale.
- "No better guardian" gets a structural form: no single formation's influence closure need cover another's reach (`Clearing`), so only distributed registration covers it.

## 3. 停在哪里 / Where it stops

- **Wanting and forming.** That a formation forms a model, or wants to avoid a runaway, is not derived (`Becoming.Feedback` lists this). Model formation is in the cognition results at their own scope. The spine has no bridge yet between `Flow` and `Becoming.Inquiry`.
- **Calibration.** Registration bounds what can be told apart. It does not say what a registration is about; see the sensor-reversal case in SCIENTIFIC-PHILOSOPHY §3.2.
- **Induction.** Which laws hold is empirical. The spine says this of its own premises.
- **Ethics.** On route (b), a center's own reason reaches its feeding closure. So prudence covers the runaways whose losses come back. Not harming what never comes back, like the dweller, needs one of two things:
  - significance covering reach, Ren's weaker level, under which `Clearing.reach_counts_dweller` counts the dweller;
  - Part II's axiom.

## 4. 拟议的形式阶段 / Proposed formal stage

Every statement goes in the pure core with empty axiom reports. The stage builds on `Becoming.Feedback` and `Becoming.Horizon`, so it comes after c9c219e3 lands. The module name is Ren's to choose (§5); `Becoming.Testing` is a placeholder.

- **T1. Registration equivalence.** Define two flows (or runs) as alike for `f` up to `t` when they give `f` the same support at each step before `t`. Then every response that is a function of `f`'s registration agrees on them. Bridge: an inquiry in `Becoming.Inquiry` whose sensing factors through registration has the same scope and common responses on alike flows.
- **T2. Refutation needs reach.** A claim is refutable by `f` at `t` in a flow when no flow satisfying the claim is alike for `f` up to `t`. A claim that differs from its rivals only in parts beyond `f`'s influence closure is never refutable by `f` (from `unregistered_beyond_influence`). Reach is necessary and not sufficient (`Margin`).
- **T3. Testability is relational.** In `Clearing`, the claim that the clearing ends the dweller is unrefutable for the clearer and refutable for the dweller.
- **T4. Horizon.** For every `h`, neither "renews" nor "consumes" is refutable by the first `h` steps (from `Feedback.prefix_does_not_decide`). A continuation model's prediction of the level at `h` is refutable at `h`.
- **T5. Threshold blindness.** Statement:
  - Take the support-gated law, and two starts that differ only in the stock of a required condition.
  - Every policy whose draws are a function of its support history draws alike in both until the poorer stock's support fails.
  - So no support-only policy both keeps its support in the poorer world and draws in the richer world for as long as that world supports it.
  - A policy that also registers the level can do both.

  T5 is the formal content of "knowledge lets one avoid a runaway without ceasing to live". It is the stage's central statement.

**Reuse and merge.** This generalizes B3 and B4 of the [无明 boundary plan](WUMING-BOUNDARY-PLAN.md) from seeking to inquiry:
- B3's "no such mark ever comes" is already `Clearing.unregistered`;
- B4's "明 is inquiry whose reach covers what support does not mark" becomes T2–T5.

The two plans should be one stage, not two.

**Order.** The stage comes after c9c219e3 lands. It is to be placed against P44 (G0 audit) and the 无明 stage at Ren's choice.

## 5. 属于 Ren 的选择 / Choices for Ren

1. Whether this becomes a stage, and its place relative to P44 and the 无明 stage.
2. Names. The AI's candidates are threshold, horizon and reach blindness, with Chinese 阈下不见, 视界外不见 and 不返之不见; the module is `Becoming.Testing` or another formal name.
3. Whether 理 is read as the model that registers across the three blindnesses (§2a).
4. Whether a formation's own standing level counts as registered, beside its support. This is a representation choice, and it changes T5's boundary.

## 6. 什么会改变这一论述 / What would change the account

- A support-only policy that, in the support-gated law, keeps its support in the poorer world while drawing fully in the richer one would refute T5.
- A correction channel that reaches a formation from beyond its influence closure without passing through its exchanges would refute the exclusivity of reach blindness. That would mean an omitted relation in the representation, and it should be reported.
- A finite-history reading that credits every renewing run and no consuming run would contradict `prefix_does_not_decide`. It cannot exist on the spine, but a richer representation of runs could change what "prefix" means.
- If T1's bridge to `Becoming.Inquiry` cannot be stated without importing beyond the core, the bridge moves to the periphery, and that is reported.

## 7. 结果（P49）/ Result (P49)

模块 `Becoming.Testing` 在纯净核心中，公理报告为空；平衡只在被计入的条件上逐步假设（`Flow.BalancesOn`）。下面对照 §4 的拟议陈述；“读法”仍是 AI 的，经独立审查收窄，待 Ren。

The module `Becoming.Testing` is in the pure core with empty axiom reports; balance is assumed only on the conditions registered, at each step (`Flow.BalancesOn`). Against the proposed statements of §4, with the readings still the AI's, narrowed by the independent review and pending Ren:

- **T1 → registering alike and the bridge.** A step's registration is exact: a condition depended on and not observed registers only whether it meets the need, an observed one its level (`Web.alike_of_threshold`, `Web.observed_level_registers`). The bridge is stated at the level of a judgment: a judgment from registration is a common response of `Becoming.Inquiry` over the formation's belief, kept as later steps and more observation narrow it (`Web.belief_judge_iff`, `belief_judge_later`, `belief_judge_widen`). The multi-step `Scope` bridge, with a policy whose sensing factors through registration, remains open.
- **T2 → reach.** Refutation is defined over level histories (`Web.Refutes`). Where the members of a region closed under being affected through what is registered respond only through their own registration, nothing beyond it registers within it (`Flow.alike_within_closed`). The fixed-rest form is an instance, so no claim met by the levels without a part beyond the registration closure is refuted within it (`Flow.unrefuted_beyond_registration`). The registration closure replaces the influence closure: it holds it and is it under support only.
- **T3 → relational testing.** As proposed (`Clearing.tested_by_dweller`), with pooled testing added (`Clearing.pooled`).
- **T4 → horizon and models.** Without a model no finite record refutes a claim about what follows it (`Web.tail_unrefuted`). Relative to a model of the exchange, a formation observing a stock refutes at the first step every false claim that it comes to nothing (`Flow.refutes_tail_within`). Refutation relative to a model is refutation of the model and the claim together (`Web.refutesWithin_iff_conjunction`); a wrong model refutes what holds, and registration refutes the model (`Stationary`). Where the continuation is open no finite reading is exact (`Renewable.no_exact_finite_reading`). §2(c)'s "long-run claims are untestable from the record" holds where the continuation is open, not relative to a model.
- **T5 → the threshold laws.** The policy statement is replaced by laws on the exchange around the formation. Where the exchange on what it registers follows its registration (`Flow.ExchangeFollows`, a supplied hypothesis), a difference stays as it was while it registers alike (`Flow.difference_kept`) and changes only after the two webs' support diverges (`Flow.difference_changes_after_divergence`); one stock higher by `d` stands `d` higher at every step before which the lower web supported it (`Flow.subthreshold_alike`). `SupportDrawn` witnesses it, joint failure keeps the difference (`JointFailure`), and observing the stock lifts it (`Gauged`). §6's first test is answered within the hypothesis. Where others respond to the stock itself the hypothesis fails, and a higher stock can end the formation first (`Attracting.higher_breaks_first`): §2(a)'s "the losses do not register until the break" holds only where the exchange follows registration.

**第 4 问的决定 / The decision on question 4.**
- **Base.** The base registers support only (`supportOnly`).
- **Own standing.** In the one-kind reading, own standing registers through self-bearing (`Web.SelfBearing`), as a threshold, like any condition depended on.
- **A gauge of oneself.** `ownStanding` is an observation premise, like `Gauged`'s gauge of the stock.
- **Why.** The first draft counted own standing as registered. The review's arguments, and the AI's own, are in study section {S}.1. The deciding points:
  - an exact self-gauge by default supplies a knower rather than explaining one;
  - the default would make blindness to one's own depletion inexpressible (`Gauged.own_is_stock`), the central runaway case;
  - the weakest base gives the strongest statements, each observation stated as a local premise where it is used.
- **Scope.** No theorem changes, since `obs` is a parameter. `SelfPrey.threshold_on_oneself` gives the contrast: through support a bite registers only where it brings the prey below its need, while a gauge of oneself registers every bite.

**名称 / Names.** The Lean names follow the review and Ren's naming criteria: `subthreshold_alike`, `difference_kept`, `ExchangeFollows`, `RegistersAlikeUpTo` and `SupportDrawn`. The prose keeps "threshold, horizon and reach blindness" as readings, each with its scope. Whether to replace the Chinese 计入 for "registers" (candidate 反映) goes to Ren; any replacement would apply to P42 and P49 together.

**§6 中的检验 / The tests of §6.**
- **The first test.** Under the hypothesis it cannot be met: a support-only exchange keeps the difference until support diverges.
- **The second test.** It is now a precise statement. A correction channel from beyond the registration closure needs a member responding to something it does not register, or an exchange or observation that widens the closure (`withinRegistration_mono_obs`, `withinRegistration_mono_flow`).
- **The third test.** Unchanged.
- **The fourth.** The bridge to `Becoming.Inquiry` was stated within the core.
