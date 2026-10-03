# Changing the AI Trajectory: Meta-Attractors, Alignment and Cooperation

*Theory v5.1, 3 October 2026. Written by Claude (Opus 5.5) from Ren's direction and the v5 authorial brief (`sources/19-v5-handoff-2026-10-03/`), building on* No Winning Position *v4.5 (`../v4/THEORY.md`). Every sentence is AI-drafted. The claim register is [CLAIMS.md](CLAIMS.md), the evidence register [EVIDENCE.md](EVIDENCE.md), the record of changes [CHANGELOG.md](CHANGELOG.md), and the numerical checks `checks_v5.py` with its log. This version has not been reviewed.*

**中文概要.** 本文讨论的是当下这条 AI 发展轨迹，而不是所有可能的竞争。这条轨迹以决定性优势为目标、以加速为手段；而它所处的制度里，评估与纠错的条件本身会被竞争中的成功所改写。

1. **根模型。** 这条轨迹的各种动力不是彼此独立、可以逐个修补的问题，而是从同一个支配模型推出来的。本文称之为"赢的模型" Ψ，即讲赢而不讲理。它有三条信条：
   - 孤立的自我：只计自己的收益，他人只是对手或工具；
   - 朴素达尔文主义：世界是所有人对所有人的竞争，胜者通吃，胜者即正义；
   - 赢家通吃的复利：优势会累积并跨领域转化，落后就无法挽回。

   由此推出轨迹的三个特征：以赢为目标并随对手加速（W）；把成功转化为对纠错的控制（C）；共同的损害看不见，合作显得天真（N）。
   - **竞赛是自我模型的性质。** 在只看相对位置的模型里，合作的收益完全看不见，博弈成为零和；在把整体当作自己的模型里，困境消失，只剩协调问题（命题 1.2、1.3）。
   - **技术力量越大，分离的代价越高。** 被竞赛耗散的份额随力量上升，上限只由自我模型和决定性决定；纯相对的模型没有上限（命题 1.3）。
   - **增长需要自我的扩展。** 只要纠错不能把单位损害降到零，在增长的前提下，生存就要求自我模型与"一体"之间的差距收敛得比所争夺的赌注增长得更快（命题 1.4）。"我们是一体"不是情怀，而是增长与变化的长期必要条件。
   - **制度可以先行。** 分享所争夺的收益，可以让更宽的自我模型在每个重视自身绝对收益者的目标中生效，不必等每个人的心先改变。但对纯相对的选择无效，那里要改变的是胜利能换来什么（命题 1.5）。
   - **Ψ 是错的。** 它误判了行动者自身的利益：相互依存是事实，连被竞赛的技术本身的供应链也没有哪个公司或国家能独立完成。它误读了演化：重大演化跃迁都是整合，癌是对多细胞合作的欺骗。它也不符合人的实际行为。
   - **Ψ 仍然支配，原因有五个。**
     - 它自我证实：大家都在竞赛，合作会带来什么从未被观察到。
     - 它具有表演性：理论通过制度、规范和语言让自己成真。
     - 它选择自己的持有者。
     - 它借用了人对地位的需求；而地位既可以靠支配获得，也可以靠贡献赢得声望。
     - 它有一段历史：半个世纪以来，新自由主义转向把自利从模型中的假设变成了行为规范和制度设计的标准。

     这是一支成为主导的思想脉络的历史，不是任何文明的本质。Ψ 如今在各种出身的领先国家与企业中都存在；只要这种动力在，分析就一样。在 Ψ 之内做的设计会被重新吸收，所以"转向"被定义为支配模型的改变。
2. **决定。** 要判断的是：沿这条轨迹走下去，能否可信地带来安全和值得追求的未来？如果不能，应当怎样改变方向？为此，本文先把"继续"与"转向"定义清楚，再比较各条路径的结果。
   - "继续"指让 Ψ 继续支配：保留 W，以及把成功转化为对评估和规则的影响（C），无论附加了什么保障。
   - "转向"指支配模型的改变，体现在目标、决策权、约束或共同供给之中至少一项的实质改变。
   - 比较时使用同一组时间范围和同一个决策标准。本文先保护的是两类不可逆的损失：大规模的生命损失，以及人类对关键系统决策权的丧失。
3. **元吸引子。** 成功可以转化为对未来选择规则的控制。当这种控制的收益可被占有、持久，且相对其成本足够大时，对控制能力的投资本身会被选择（命题 3.4）。纠错是二阶公共品，无法从竞争者内部得到供给（命题 3.5）。AI 降低了控制的成本，独立纠错必须以一定速率增长才能保住评估不被捕获（命题 3.6）。局部改革会被重新吸收；暂停的效果取决于暂停期间规则制定是否被隔离（命题 3.11、3.12）。
4. **完美对齐不够。** 即使每个 AI 都忠实于它的委托人，人类也保留所有最终决定，只要委托人之间在比赛谁赢，结果仍然可以是集体更差（命题 4.1）。一个更好的执行者，可以更有效地执行一个有害的博弈。这一博弈的目标还会通过行动、决策者和制度上的选择被再生产出来。
   - 如果风险的下界不可求和，生存最终趋于零（引理 4.4）。
   - 只是把同一过程推迟的暂停，不改变这个结论。暂停的价值在于暂停期间改变了什么。为此本文提出"可以恢复"的六个评估维度。
5. **能力、委托与纠错。** 本文用修正后的结果说明 AI 怎样改变风险的大小、速度和可逆性。
   - 当锁定意味着行动者生存的终结时，在任何有限速度下，不委托都严格占优（命题 5.5）。
   - 竞赛中的安全进步，在稳定的分支上会被更多的委托吸收；但这并不意味着风险存在永久的下界。
   - 纠错跟不上危险时的生存衰减，只在明确的前提下成立（定理 5.8）。
   - 超出理解的纠错可能失败，也可能真正降低风险，这要看它的结构（命题 5.10、5.11）。
6. **继续的最强理由。** 本文逐一给出各条继续路径的最好情形、建立途径和剩余风险，包括：
   - 技术对齐与 AI 辅助纠错；
   - 有强纠错的竞争性供给；
   - 领先与安全裕度；
   - 良性的赢家；
   - 冲刺后停下；
   - 威慑与预防；
   - 保留竞赛的核查协议。

   同一组耐久性压力测试也用于本文自己的合作方案。
7. **合作能带来什么。** AI 是行星尺度的技术，应当为所有人服务，而不是成为某一方赢得共同未来的工具。权力可以是为人民生活和历史进步负责的生产性能力。本文给出一个具体方案，列明融资、所有权、服务义务、接入、评估、规则制定、执行权、申诉、延续与继任，并对它做压力测试。
8. **怎样到达。** 过渡分五个阶段：
   - 共同的危险评估与测量；
   - 窄而可核查的承诺；
   - 为独立纠错和共同服务出资；
   - 分阶段改变战略委托与决策权；
   - 随着制度证明自己的能力而扩大。

   把 AI 移出战略决策回路（E1）、停止（E2）、按理解的节奏发展（E3）和临时暂停，是四种不同的安排，不能互相替代。
9. **结论与关键分歧。** 在本文的决策标准下，现有证据支持合作转向。结论最依赖的分歧主要有五个：
   - 纠错之后，不可逆损失的残余风险有多大；
   - 成功转化为对评估者控制的渠道有多强；
   - 可争议的理解能否跟上危险的种类；
   - 合作制度本身的解体与捕获风险；
   - 分享所争夺的收益、把奖励与对纠错的控制分开、降低决定性，能否在现实中扩展有效的自我、改变行为。

   本文给出了会改变这一结论的观测，以及下一步应当测量什么。

---

## 1. The governing model and the decision before us

### 1.1 What is being decided

The question is practical. AI development today pursues decisive advantage through acceleration, inside institutions whose conditions of evaluation and correction can themselves be reshaped by competitive success. Can continuing along this path credibly deliver safety and a desirable future? If not, what change of course is warranted, and how can it be made?

The answer starts from one diagnosis. The features of the present trajectory are not separate problems to be patched one by one. They follow from one governing model of the self and the world, called here the winning model, Ψ (Section 1.2): the isolated self, naive Darwinism, and winner-take-all compounding. The argument from that diagnosis has four steps.
1. **Inside Ψ the race is the rational game.** Outside it, the same material situation is not a dilemma. The race is a property of the self-model, and its cost grows with the power of the technology (Section 1.3).
2. **Ψ is false.** It misdescribes the actors' own interests, misreads evolution, and fails as a description of human behaviour (Section 1.4).
3. **Ψ governs anyway.** It confirms itself on the path of play it produces, its institutions make it true where they reach, and the environment it creates selects its holders. Designs made inside it are re-absorbed (Section 1.5).
4. **If growth and change are favoured, a self-model that counts the interdependence that exists is a long-run requirement.** We are one interconnected system, not a set of isolated rational selves. The change can begin in institutions, which make that self-model effective before every mind holds it (Propositions 1.4 and 1.5).

The thesis is that this trajectory warrants a cooperative change of course. That change replaces the governing model, and it needs institutions able to sustain shared flourishing, effective correction and a reachable transition. The argument concerns the path we are on. It does not claim that every form of bounded competition is impossible or unstable, and bounded competition can continue inside the arrangement it proposes (V5).

### 1.2 The governing model

**Definition 1.1 (The governing model Ψ, the winning model) [D].** A *governing model* is a model of the self and of the world, embodied in three places:
- the objectives actors declare and act on;
- the rules by which institutions select and reward;
- the narratives through which people learn what counts as success.

The winning model Ψ has three tenets. It is the logic of winning (讲赢) in place of the logic of reason (讲理).
- **Ψ1, the isolated self.** An actor is a bounded unit whose welfare is its own payoff; others enter as rivals or instruments. In the notation of Section 1.3, the weight its objective places on others is at most zero.
- **Ψ2, naive Darwinism.** The world is a contest of all against all in which the strong prevail, and prevailing certifies fitness and right: the winner takes all, and the winner justifies all. Cooperation is a tactic or a weakness.
- **Ψ3, winner-take-all compounding.** Advantage compounds and converts across domains. The decisive outcome is to win or to be dominated, and falling behind cannot be recovered.

A governing model governs to the extent that it is embodied. It can govern through institutions whose members privately reject it, and binding institutions can change the effective game while private beliefs persist (Section 4.5). It is a property of the effective governing logic. It is not an accusation against any person or people.

**Signatures [D; derived in Sections 2–5].** The present trajectory shows three signatures, and each follows from the tenets.

| Signature | What is observed | How it follows from Ψ | Mechanism |
|---|---|---|---|
| **W. Winning sets the objective and the tempo** | Strategic success is defined substantially by relative or decisive advantage. Capability, deployment and consequential delegation accelerate when rivals advance. | Under Ψ1 others are rivals. Under Ψ3 a gap compounds and cannot be recovered. Relative standing becomes the objective, and restraint that a rival does not match reads as a permanent loss, so the fastest rival sets the tempo. | §§2.4, 4.2, 5.1–5.2 |
| **C. Success buys control of correction** | Success is reinvested both in productive capacity and in influence over future evaluation and rules. Oversight comes to depend on the resources, access, tools, schedules or personnel of those it oversees. | Under Ψ2 the winner is entitled to write the rules. Under Ψ3 control of the rules is the asset that compounds fastest. | §3 |
| **N. The shared is invisible, and cooperation looks naive** | Shared harms and dependencies are not reflected in individual decisions. Collective restraint and shared provision are treated as unrealistic, and acceleration is the default response. | Under Ψ1 a shared gain or loss enters an objective only as one's own share of it. Under relative selection it does not enter at all (Proposition 1.2, Lemma 2.3). Under Ψ2 restraint reads as weakness. | §§1.3, 2.3, 2.5 |

The signatures sustain one another.
- W supplies the success that C converts into control.
- C removes the correction that would make the shared visible.
- N makes cooperation look naive, which keeps W in place.

The meta-attractor of Section 3 is the formal account of this loop: success edits the rules that select the next round's successes. Section 1.5 applies the same loop to Ψ itself.

### 1.3 The race is a property of the self-model

The material situation must be kept apart from what an actor's model of itself lets it see. Take any game with material payoffs $\pi_i$ among $n\ge2$ actors, and let actor $i$ act on
$$O_i=\pi_i+\theta_i\,\bar\pi_{-i},\qquad\theta_i\in[-1,n-1],$$
where $\bar\pi_{-i}$ is the others' average payoff and $\theta_i$ is the weight $i$'s self-model places on them.
- $\theta_i=-1$ is the purely relative objective $\pi_i-\bar\pi_{-i}$: Ψ1 and Ψ2 together.
- $\theta_i=0$ is the isolated self of Ψ1.
- $\theta_i=\kappa$ is the accurate self-model, which counts the material interdependence that exists (Section 2.5).
- $\theta_i=n-1$ is the inclusive self-model, whose objective is the total payoff: we are one.

**Proposition 1.2 (What a self-model can see) [T].** *Let every actor use the same $\theta$.*
1. *$\sum_iO_i=(1+\theta)\sum_i\pi_i$.*
2. *A change $\Delta$ in every actor's material payoff changes each objective by $(1+\theta)\Delta$. Of a gain or loss shared equally by all, each actor's objective registers the fraction $(1+\theta)/n$ of the total.*
3. *At $\theta=-1$ the game in objectives is zero-sum. No outcome is better for every actor, and every shared gain or loss is invisible. At $\theta=n-1$ every objective equals the total, so every profile that maximizes the total is a Nash equilibrium in objectives. Inefficient equilibria can remain, so what is left is a problem of coordination, not a dilemma.*

Game theory applies to any objectives. The dilemma lies in the objectives that Ψ writes, not in the material situation. Relative selection acts as if $\theta=-1$, which is why the shared host cancels from it (Lemma 2.3). Under Ψ the gains of cooperation are not merely discounted: at the limit, they cannot be seen.

**Proposition 1.3 (The race and the self-model) [T].**
1. *Faithful AI. In the game of Proposition 4.1, with each principal acting on $O_i$, racing changes $O_i$ by $\epsilon b\big(1-\tfrac{\theta}{n-1}\big)-c-\epsilon d(1+\theta)$, whatever the others do. Racing is strictly dominant if $\theta<\theta^\ast(\epsilon)$ and strictly dominated if $\theta>\theta^\ast(\epsilon)$, where*
   $$\theta^\ast(\epsilon)=\frac{\epsilon(b-d)-c}{\epsilon\big(b/(n-1)+d\big)}<n-1.$$
   *$\theta^\ast$ rises with $\epsilon$, toward $(b-d)/(b/(n-1)+d)$. A more effective faithful instrument needs a wider self-model to end the race.*
2. *Contest. In the contest of Section 4.3, the symmetric intensity $e(\theta)$ of Proposition 4.2 falls to zero as $\theta\to n-1$. The share of the stakes dissipated by the contest, in private cost and shared loss, is*
   $$\frac{D(\theta)}{\Omega}=\frac{r(n-1-\theta)(c+n\ell)}{n\big(c+(1+\theta)\ell\big)}.$$
3. *Power. Scale the technology's power by $s$: stakes $s\Omega$ and shared loss per unit of intensity $s\ell$, with private cost unchanged. For $-1<\theta<n-1$ the dissipated share rises strictly with $s$, toward the ceiling $r(n-1-\theta)/(1+\theta)$, which depends only on the self-model and the decisiveness. The total material payoff stays positive at every scale if and only if $\theta\ge\theta_g=(r(n-1)-1)/(1+r)$, and $\theta_g$ rises with $r$. At $\theta=-1$ the dissipated share is $r(1+ns\ell/c)$, which grows without bound.*

With $n=4$, $b=1$, $c=0.3$ and $d=0.2$, $\theta^\ast$ is $0.94$ at $\epsilon=1$ and $1.44$ at $\epsilon=10$ [N]. In the contest with $n=4$, $r=1$ and $\ell=0.3c$, the ceiling on the dissipated share is as follows [N]:
- unbounded at $\theta=-1$;
- $3$ at $\theta=0$;
- $1.86$ at an accurate $\kappa=0.4$;
- $1$ at $\theta=1$;
- $0.33$ at $\theta=2$.

Here $\theta_g=1$; with $r=0.5$ it would be $1/3$.

The proposition separates two steps.
- **Accuracy.** Moving from Ψ1 to the accurate self-model ($\theta=\kappa$) is in each actor's own interest. It maximizes the actor's true welfare against any fixed conduct of the others (Proposition 4.2(3)), and it removes part of the race.
- **Inclusion.** At high power and high decisiveness, accuracy may not be enough: in the example, $\kappa=0.4$ lies below $\theta_g=1$. The remaining step, from $\kappa$ toward $n-1$, raises every actor's welfare when all take it (Proposition 4.2(2)), but no actor gains by taking it alone. It therefore has to be built: by institutions that make a wider self-model effective (Proposition 1.5), and by the identity that the relational view of the self describes, in which the self is an action-centre of its relations rather than a point outside them.

Ψ3 enters through the decisiveness $r$: the more winner-take-all the contest, the wider the self-model that growth requires.

**Proposition 1.4 (Growth needs a widening self) [T].** *Play the contest of Section 4.3 in rounds $t=1,2,\dots$ at its symmetric equilibrium. Round $t$ has contested stakes $\Omega_t$, decisiveness $r_t$, shared loss per unit of intensity $L_t>0$ and self-model $\theta_t\in[-1,n-1]$, with intensity zero at $\theta_t=n-1$. Assume:*
- *(A_G) the probability of the irreversible event of Section 4.4 in round $t$, given survival so far, is proportional to the shared damage: $q_t=aL_t\mathcal E_t<1$, where $\mathcal E_t$ is total intensity.*

*Then*
$$q_t=\frac{a\,r_t\Omega_t\,L_t\,(n-1-\theta_t)}{n\big(c+(1+\theta_t)L_t\big)},$$
*and survival stays bounded away from zero if and only if $\sum_tq_t<\infty$.*
1. *Whatever correction achieves, $\sum_tr_t\Omega_t(n-1-\theta_t)/(1+\theta_t)<\infty$ is sufficient.*
2. *Suppose correction cannot drive the harm per unit to zero, $L_t\ge L_{\min}>0$, and $\theta_t\ge\theta_{\text{low}}>-1$. Then survival stays positive if and only if $\sum_tr_t\Omega_t(n-1-\theta_t)<\infty$. With the contested stakes growing, the gap between the self-model and the inclusive one must close faster than the stakes grow. Even with constant stakes and $r_t$ bounded below, the gap must close fast enough to be summable.*
3. *At $\theta_t=-1$, $q_t=ar_t\Omega_tL_t/c$, and survival stays positive if and only if $\sum_tr_t\Omega_tL_t<\infty$. Everything then rests on correction lowering the harm per unit faster than the stakes grow.*

Take $a=0.01$, $n=4$, $r=1$, $c=1$ and $L=0.3$, with contested stakes growing 3% a round [N]:
- An accurate self-model held fixed at $0.4$ leaves survival at $0.42$ by round 100 and near zero by round 200.
- A gap that closes faster than the stakes grow keeps survival at $0.997$.
- A gap that closes as $1/t$, slower than the stakes grow, keeps $0.93$ to round 200 and reaches zero by round 1,000.
- The purely relative model with fixed $L$ is at $0.15$ by round 100. With correction lowering $L$ faster than the stakes grow, it stays at $0.99$.

Each factor of the hazard is one tenet of Ψ:
- the contested stakes weighted by decisiveness, $r_t\Omega_t$, are Ψ3;
- the gap $n-1-\theta_t$ is the boundary Ψ1 draws;
- the harm per unit $L_t$ is what correction must reduce, and under Ψ2 success learns to control correction (Section 3).

If growth and change are favoured, the stakes of the technology grow. Survival then needs one of three things:
- the boundary closes faster than the contested stakes grow;
- growth stops raising what is contested, so that $r_t\Omega_t$ does not grow;
- correction drives the harm per unit to zero faster than the stakes grow.

Continuation relies on the third alone, while it keeps the first two growing and cultivates influence over correction. The pivot works on all three. This is the precise sense in which understanding ourselves as one interconnected system is a long-run requirement of growth, and not a sentiment.

A_G is a modelling premise: the simplest link between the shared loss that enters payoffs and the irreversible event of Section 4.4. The conclusion is as strong as A_G and no stronger. Section 5.4 states the premises for the hazard in more detail, and Section 9 treats them as the central crux.

**Proposition 1.5 (Institutions widen the effective self; relative selection resists) [T].** *Let each actor receive $(1-\beta)$ of its own material payoff plus $\beta$ times the average of all, $\beta\in[0,1]$, as under a scheme of benefit sharing. An actor holding self-model $\theta_0$ then acts, up to a positive factor, as if it held*
$$\theta_{\text{eff}}(\beta,\theta_0)=\frac{\theta_0(1-\beta)+\beta(1+\theta_0)(n-1)/n}{(1-\beta)+\beta(1+\theta_0)/n}.$$
1. *For $-1<\theta_0<n-1$, $\theta_{\text{eff}}$ rises strictly with $\beta$, from $\theta_0$ at $\beta=0$ to $n-1$ at $\beta=1$.*
2. *At $\theta_0=-1$ the objective becomes $(1-\beta)(\pi_i-\bar\pi_{-i})$. For every $\beta<1$, equilibrium behaviour is unchanged. Under replicator selection the rate falls by the factor $1-\beta$, but the direction does not change, and neither does the limit when cumulative selection diverges (Proposition 2.4(3)).*

With an isolated self ($\theta_0=0$) in the faithful-AI example, racing ends once $\beta$ exceeds $0.65$ at $\epsilon=1$, and $0.79$ at $\epsilon=10$ [N]. In the contest with $n=4$ and $r=1$, the total stays positive at every scale once $\beta>2/3$ [N].

The proposition has two lessons.
- **Institutions first.** The inclusive self-model does not have to wait for every mind to change. Sharing the gains of what is contested makes it effective in the objective of anyone who values its own absolute payoff. This is the formal content of shared provision in Section 7 and of the levers of Corollary 8.2.
- **The meta level.** Where selection is purely relative, sharing cancels, as every common term does. There the lever is what winning converts into: the decisiveness $r$, and the conversion of success into control over correctors (Section 3). That is the principle of V5: reward the winner with something other than more advantage in the same game.

### 1.4 Why the model is false

Ψ is a model of the world, and it can be checked against the world. It fails on four counts.

**Material.** Interdependence is a fact about payoffs, not a sentiment (Section 2.5).
- The technology being raced over is itself made by an interdependent whole. An industry assessment found that no company or country can achieve self-sufficiency in semiconductors. It estimated that fully self-sufficient regional supply chains would need at least a trillion dollars of additional investment and would raise prices by 35 to 65 percent (E13).
- The host of Section 2.2 is shared by construction.

An actor that acts on $\theta<\kappa$ therefore lowers its own true welfare (Proposition 4.2(3)). Ψ1 misdescribes the actor's own interests.

**Biological.** Ψ2 borrows the authority of evolution and misreads it.
- The phrase "survival of the fittest" was Spencer's. It was later applied to society as a justification of hierarchy and domination, a use its historian named Social Darwinism (Hofstadter 1944); the history of the label is itself contested (Leonard 2009).
- Evolution's largest innovations were integrations. In each major transition, entities that could replicate independently before it replicate afterwards only as part of a larger whole: genes in chromosomes, organelles in cells, cells in organisms, organisms in societies (Maynard Smith and Szathmáry 1995).
- Each transition required the suppression of competition inside the new whole. Cancer is the failure of that suppression: cells that cheat on the cooperation of the multicellular body (Aktipis et al. 2015).

Selection on relative standing that ignores the whole is what each transition had to bring under control, not what drove it. Section 4.6 uses the image of cancer for this reason, and in this sense only.

**Behavioural.** Human beings are not Ψ1 actors.
- In experiments in fifteen small-scale societies, the canonical self-interest model failed in every society. Cooperation rose with market integration and with the payoffs to cooperation (Henrich et al. 2001).
- In a one-shot public-goods experiment, about half the subjects were conditional cooperators and about a third free riders (Fischbacher, Gächter and Fehr 2001).
- Users govern commons without either a sovereign or privatization, where institutions fit the resource (Ostrom 1990).

The evidence is in E14.

**Compounding.** Ψ3 is partly true and partly made true. Increasing returns and cumulative advantage exist. Whether advantage converts into control of the shared conditions depends on rules: the decisiveness $r$ and the conversion $\chi$ of success into control over correctors are design variables (Section 3). Ψ3 holds where institutions built under Ψ make it hold. This points to the mechanisms of the next section.

### 1.5 Why a false model governs

A model can be false and still govern if it maintains itself. Ψ does so through five mechanisms. Together they make Ψ a meta-attractor in the space of governing models (Definition 3.1).
- The model shapes institutions and behaviour ($\partial F/\partial\sigma>0$).
- The behaviour it produces confirms the model and promotes its holders to the positions that write the next round of rules and narratives ($\partial G/\partial x>0$).

1. **Self-confirmation.** A belief can be wrong and stable when it is correct about everything it lets one observe. In a self-confirming equilibrium, each player best-responds to beliefs that are correct along the path of play, while beliefs about play never observed need not be correct (Fudenberg and Levine 1993). Under Ψ everyone races, so what cooperation would have yielded is never observed. The belief that cooperation is naive is confirmed by the play it causes [C, as an application of their concept].
2. **Performativity.** Theories of behaviour can become self-fulfilling through the institutions designed from them, the norms they set and the language they spread (Ferraro, Pfeffer and Sutton 2005). Financial models have reshaped the markets they describe (MacKenzie 2006). Students of economics defected more often in a prisoner's dilemma than other students, and the authors found evidence that training in the self-interest model contributes (Frank, Gilovich and Regan 1993; the inference is disputed, E14). Ψ3 is the clearest case: winner-take-all institutions make the winner take all.
3. **Selection of minds and institutions.** Selection on actions favours the conduct of the purely relative objective (Proposition 4.2(4)). The race plausibly promotes people and institutions whose model ranks standing first (Section 4.3; a conjecture). What the environment rewards, the mind promotes. Selected minds build selected organizations, which form the next round of minds.
4. **The status drive.** The desire for status is a fundamental human motive, observed across cultures, genders, ages and personalities (Anderson, Hildreth and Howland 2015). Status has two routes (Henrich and Gil-White 2001):
   - *dominance*, gained through fear and control;
   - *prestige*, deference freely conferred on skill and contribution.

   The drive is given; its route is not. Ψ channels the drive into dominance through winning, which is part of why Ψ feels natural. A cooperative order can channel the same drive into prestige through contribution (E16).
5. **The window and its history.** Over the last half century, the vocabulary of economic and political life moved toward Ψ (E15).
   - In 1970 a widely read essay argued that the social responsibility of business is to increase its profits (Friedman 1970).
   - Agency theory recast the firm around aligning managers with owners (Jensen and Meckling 1976).
   - A leading business association declared shareholder primacy the purpose of the corporation in 1997, and revised that statement in 2019.
   - The broader neoliberal turn carried market criteria into institutions generally (Harvey 2005). It did so first in the Anglo-American economies, and then across much of the world through the institutions of trade, finance and development.

   In that turn, self-interest moved from an assumption inside models to a norm of conduct and a criterion of design. The pursuit of private gain became something to release rather than something to bound. The present vocabulary of AI policy, which speaks of winning a race and of dominance, is the same model applied to the newest technology (E1).

This is the history of a strand of thought that became dominant. It is not the essence of any civilization. The same intellectual history contains its strongest critics:
- Smith on sympathy (1759);
- Darwin on the social instincts (1871);
- Kropotkin on mutual aid (1902);
- Polanyi on markets embedded in society (1944);
- Ostrom on governing the commons (1990).

Ψ is now held, in some measure, by leading states and firms of every origin. The theory therefore concerns Ψ wherever it governs: whatever the states and whatever the firms, where these dynamics are present the analysis is the same.

**Why design inside Ψ is re-absorbed.** The same loop explains why, inside Ψ, the trajectory persists across designs. Complex adaptive systems resist interventions at the level of parameters. The deepest leverage lies in a system's goals and in the paradigm out of which it arises (Meadows 1999). Three results of this paper show re-absorption at three levels:
- a reform that leaves the conversion channels in place is re-absorbed (Proposition 3.11);
- a faithful AI amplifies the objective it serves (Proposition 4.1);
- a pause that changes nothing resumes the same process (Proposition 4.5).

Safeguards therefore matter as parts of a change of governing model, not as substitutes for one. The pivot is defined accordingly (Section 1.7).

The change need not wait for every mind. Institutions can make a wider self-model effective (Proposition 1.5). The environment then shapes the minds it selects, as it did under Ψ: the environment makes the mind. That is the order of the transition in Section 8: shared assessment first, then binding commitments and shared provision, which change what is rewarded.

### 1.6 Values

The argument rests on five normative commitments. They are stated so that a reader can reject one and see what follows.

- **[V1] AI is a planetary technology, to be developed and used for people collectively.** Its effects and dependencies cross the boundaries of those who decide about it, so no actor's victory is an adequate criterion of success. This is a governing commitment. Its scope is an empirical claim about cross-border effects, which Section 2.6 treats separately. Planetary purpose does not require one culture, one operator, or the end of local purposes.
- **[V2] Two losses are protected first:** large-scale loss of life (O1), and irreversible loss of human decision authority over consequential systems in a defined domain (O2).
- **[V3] Those affected by an optimization process should keep a meaningful capacity to contest its direction.** This is why correction must stay contestable, and why a technically safe controller that no one can answer to is not enough.
- **[V4] Authority is a productive capacity.** It can coordinate long-horizon investment, guarantee useful services, support learning and act on shared purposes that fragmented actors cannot realize. One source of this view is a governing ideal, in the Chinese tradition the author draws on, in which authority is justified by improving people's lives and contributing to a better historical trajectory. The theory takes that ideal as a positive account of what power is for. It does not assume that every institution realizes it, nor that any other tradition has one uniform motive. It does not assume that power necessarily corrupts. The design of authority is treated as a mechanism-design problem in which purpose, competence, learning and misuse are all modelled.
- **[V5] Bounded competition is compatible with a cooperative order.** Competition in products, science and service that does not concentrate control over the shared conditions can continue. One version of the principle is that a winner should be rewarded with something other than more advantage in the same game; otherwise the game converges and the winner takes all. Recognition for contribution, prestige rather than dominance, is such a reward (Section 1.5).

### 1.7 Continuation and pivot

The comparison is defined before any outcome is evaluated.

**Definition 1.6 (Continuation and pivot) [D].**
- **Continuation** is any policy that leaves Ψ governing. It retains W, together with the conversion of success into influence over evaluation and rules (C), whatever safeguards it adds.
- **Pivot** is any policy that changes the governing model, by a mechanism that does not depend on one actor's continued unilateral restraint. The change is embodied in a material change to at least one of four elements:
  - *objectives*: consequential AI is directed to shared provision rather than to relative advantage (W);
  - *decision rights*: strategic and coercive uses of AI sit under jointly verified limits, and evaluators' appointment, funding and access are separated from competitive success (C);
  - *constraints*: the tempo of capability and delegation is bound to the capacity for effective correction (W);
  - *shared provision*: common infrastructure supplies useful services and correction that no actor owns, which makes the shared visible in every objective (N; Proposition 1.5).

A safeguard does not become a pivot because it succeeds. It is classified by what it changes. Equally, a hypothetical safe competitive regime is not a rebuttal of the thesis until one asks whether it can be installed on the present path or instead requires changing it.

### 1.8 Outcomes and the decision standard

**Outcomes [D].** Four outcomes are kept apart. They are not interchangeable, and the normative weight differs.

| Code | Outcome | Weight |
|---|---|---|
| O1 | Physical catastrophe: large-scale loss of life | Protected first (V2) |
| O2 | Irreversible loss of human decision authority over consequential systems in a defined domain | Protected first (V2) |
| O3 | Interruption of essential services | Protected |
| O4 | The end of a particular organization's or government's tenure | Not protected as such |

O4 is listed so that "actor survival" cannot quietly protect incumbency against legitimate replacement. Where the formal sections write the survival of an actor, $\Phi_i$, they mean a stated combination of O1 and O2 for that actor, and they say which.

**Decision standard D [V].** Each candidate policy is evaluated at common horizons: near (about five years), medium (about twenty) and long (fifty or more). One justified range $\Theta$ of uncertain parameters is applied to every policy, including the cooperative design's own failure modes: dissolution, capture, unjustified restriction and loss of service.
1. Bound the probability of O1 and O2 within each horizon, over $\Theta$.
2. Among policies whose bound stays below a stated tolerance, prefer the one with greater useful benefit, more fairly distributed, that keeps more corrective options open.
3. If no policy meets the tolerance, prefer the one with the lowest bound that keeps options open.

This is robust satisficing on irreversible losses. It is a normative choice, and the worst case is taken over the same $\Theta$ for every policy. Other criteria would decide differently in places.
- An expected-value criterion can favour a policy with a small probability of very large loss and a large expected benefit.
- A discounted-welfare criterion can favour a race that ends in catastrophe with certainty, when the hazard it adds is smaller than the growth it adds (Section 5.6).

Section 6.9 reports where these criteria disagree.

### 1.9 Levels of claim, and what is claimed

The argument moves through three levels, and each needs its own support.

| Level | Form | Support required |
|---|---|---|
| Mechanism | Under conditions $C$, a specified selection, capture, delay or incentive result follows. | A correct derivation, its scope, and its counterexamples. |
| Diagnosis | Consequential parts of $C$ characterize the present trajectory. | Dated, relevant evidence, with its uncertainty and its variation among actors and hazard classes. |
| Practical judgment | Given the diagnosis, the consequences, the feasible alternatives and stated values, a cooperative change of course is warranted. | A consistent decision standard, a comparison of credible paths, transition costs, and sensitivity to disputed premises. |

A practical judgment does not need a proof of certain extinction. It also cannot follow from naming a possible danger. It must show that the danger is consequential, inadequately controlled on the present path, and better addressed by the proposed change than by credible alternatives.

Claims carry a type, given in square brackets where it is not obvious:
- [D] definition;
- [V] value or normative premise;
- [T] theorem or proposition proved in its model (Appendix A);
- [A] assumption serving as a premise;
- [O] observation, with an evidence-register row (E1–E16);
- [N] numerical observation in a stated model;
- [C] conjecture;
- [R] recommendation.

The theory does not claim to prove the following:
- that every competitive arrangement fails;
- that every path through a race ends at zero survival;
- that a single institutional blueprint is uniquely feasible.

It claims four things:
1. The dynamics of the present trajectory follow from one governing model, Ψ. Inside Ψ the race is the rational game, and its cost grows with power. Ψ is false, and it maintains itself by mechanisms that can be named (Section 1).
2. Explicit mechanisms make the present trajectory reproduce its incentives and erode the conditions of its own correction (Sections 3–5).
3. Available evidence indicates that consequential parts of those mechanisms are present now, with named gaps (Section 2.6 and the evidence register).
4. Under standard D, the credible continuation policies do worse than a cooperative change of course that can be specified, stress-tested and reached in stages (Sections 6–8). The judgment is stated in Section 9 with the cruxes that would change it.

### 1.10 The argument, section by section

1. Section 1 sets out the governing model. It shows that the race is a property of the self-model and that growth needs the self to widen, says why the model is false, and says why it governs anyway.
2. Section 2 sets out the system. Actors share conditions that function only above a floor, and selection on relative standing cannot see what all of them share.
3. Section 3 gives the meta-attractor mechanism. Success can be converted into control over the rules and correctors of future selection. The theory proves when such control is selected, when correction keeps pace, when reforms are re-absorbed, and how a pause must be designed.
4. Section 4 grants perfect alignment of each AI to its human principal and shows the harmful game that remains. It also shows how the game's objective reproduces, and what a pause must change.
5. Section 5 analyses how AI changes the stakes: contest, delegation, tempo, coverage of hazards, and the absorption of safety gains. Each result is stated with its exact conditions.
6. Section 6 gives each continuation policy its best case and applies one set of durability tests to every arrangement.
7. Section 7 develops the positive purpose of cooperation and one concrete institutional design, and stress-tests it.
8. Section 8 develops the transition: trust, signals, the distinct temporal exits, a staged path, precedents and readiness to resume.
9. Section 9 states the judgment, its cruxes and what would change it.

The nine layers of the earlier theory are all kept, and the governing model of Sections 1.2–1.5 is their common root. Their places are as follows.

| Layer | Where in v5 |
|---|---|
| 1. Host and shared conditions | §2.2 |
| 2. First-order selection | §2.3–2.4, §4.3 |
| 3. The contest in AI | §5.1–5.3 |
| 4. Correctors selected by what they correct | §3 |
| 5. Observation and masking | §3.5 |
| 6. Failure and survival | §1.3, §4.4, §5.4–5.7 |
| 7. Trust and verification | §6.7, §7.5, §8.1–8.2 |
| 8. Cooperation | §7 |
| 9. Transition | §8 |

---

## 2. The system and the present trajectory

### 2.1 Who acts, and at what level

Persons, firms, governments, providers of infrastructure and evaluators have different interests. A citizen's continued agency is not a firm's market share or a government's tenure. The theory uses two levels of behaviour and several measures of payoff, and keeps them apart.

*Levels.*
- **Selection among practices or carriers** (Sections 2.3, 3). Shares change by a payoff-monotone rule. Nobody chooses the outcome.
- **Strategic choice by actors** (Sections 4–8). States, firms and coalitions each act on an objective.

*Measures.*
- the **objective** an actor acts on, $O_\theta$ (Section 4.3);
- **absolute (material) payoff** $\pi$;
- **true welfare** $W$, which counts the coupling between actors;
- **survival** $\Phi$, defined from O1 and O2 (Section 1.8).

*Rules.*
1. A result about selection does not transfer to strategic actors unless their objective is shown to be the selected one.
2. A higher $W$ does not imply that a practice is selected.
3. Every comparison states its measure.

### 2.2 The host and viability

A condition $V\in[0,K]$ is shared by every actor: secure critical infrastructure, biosecurity, cyber stability, human control over AI systems, a reliable information environment. It regenerates logistically and is loaded by the field's activity $E$:
$$\dot V=V\big[\rho(1-V/K)-hE\big],\qquad \rho,h,K>0. \tag{1}$$
- For constant $E$ with $hE<\rho$, $V\to K(1-hE/\rho)$; for $hE\ge\rho$, $V\to0$.
- The host functions only above a floor $V_{\min}\in(0,K)$. The floor is a normative line, not an absorbing state.
- The host is the part of the shared conditions whose costs do not return to their source through customers, reputation, courts or the source's own exposure. Harms that do return are outside the model.
- Catastrophic tail risks fit the same structure: a per-period probability of catastrophe borne by all is a term common to every payoff.

**Definition 2.1 (Viability) [D].** A trajectory of the field is *viable* if $V(t)\ge V_{\min}$ for all $t\ge0$.

Every actor persists only while the host does, so viability constrains every trajectory of the field rather than entering as one payoff among others (Aubin 1991; Rockström et al. 2009; WCED 1987).

### 2.3 The field and selection

Carriers $k=1,\dots,n$ hold shares $p_k$ of the field's activity: compute, capital, users, talent. A carrier is an actor, or more generally a reproducible way of succeeding carried by organizations and their successors.
- Carrier $k$ runs a fraction $e_k\in[0,\bar e]$ of its activity in ways that load the host: deploying ahead of evaluation, omitting safeguards, entering contests in which capability converts directly into advantage.
- Each unit brings a private advantage $\nu>0$, so restraint costs $\nu$ per unit.
- The field's load is $E=\sum_kp_ke_k$.
- Carrier $k$'s absolute payoff is
  $$\pi_k=\phi_k+(\nu-\tau_{\text{eff}})e_k+G(V), \tag{2}$$
  where $\phi_k$ collects everything else, $G$ is nondecreasing, and $\tau_{\text{eff}}\ge0$ is the effective liability that correctors impose.
- With $\tau_{\text{eff}}=0$, $e_k=\bar e$ is the *race strategy*.

**Definition 2.2 (Relative selection) [D].** A selection rule $\dot p=F(p,\pi)$ is *relative* if $F(p,\pi+\xi\mathbf 1)=F(p,\pi)$ for every constant $\xi$. It is *payoff-monotone* if, for carriers $k,l$ present, $\dot p_k/p_k-\dot p_l/p_l$ has the sign of $\pi_k-\pi_l$.

Replicator dynamics and pairwise imitation (Schlag 1998) are relative and payoff-monotone, and market-share competition driven by relative profitability (Alchian 1950) is relative. Among a handful of frontier developers, the operative reading is the imitation of practices, and the flow of capital, compute and talent to those ahead. Between states, only the strategic forms of Sections 4–8 apply.

**Lemma 2.3 (Blindness) [T].** *Under a relative rule, the trajectory of shares is unchanged by any term common to all payoffs, in particular by $G(V(t))$, whatever the path of $V$. Under a payoff-monotone rule, a common term never changes which of two carriers grows relative to the other.*

This is the translation invariance of relative selection dynamics (Weibull 1995). Its content lies in the premise that the host enters payoffs additively and identically (A1 of Appendix A).

**Proposition 2.4 (Selection raises the load) [T].** *Let selection be payoff-monotone, and let $\tau_{\text{eff}}(t)<\nu$.*
1. *If $\phi_k=\phi_l$ and $e_k>e_l$, then $p_k/p_l$ increases while both are present, along every path of $V$, including paths below $V_{\min}$.*
2. *Under replicator dynamics the mean load changes as*
   $$\dot E=(\nu-\tau_{\text{eff}})\operatorname{Var}_p(e)+\operatorname{Cov}_p(e,\phi),$$
   *so the mean load rises unless restraint is correlated with other sources of advantage strongly enough: $\operatorname{Cov}_p(e,\phi)<-(\nu-\tau_{\text{eff}})\operatorname{Var}_p(e)$. A rising mean does not mean that the carrier with the maximal load gains share: with three equal shares, loads $(0,0.9,1)$, other advantages $(0,10,0)$ and $\nu=1$, the mean load rises at rate $1.09$ while the share of the maximal-load carrier falls at rate $0.99$ [N].*
3. *Under replicator dynamics with equal $\phi$, $\frac{d}{dt}\ln(p_k/p_l)=(e_k-e_l)(\nu-\tau_{\text{eff}}(t))$, so what decides the long run is the cumulative advantage $B(t)=\int_0^t(\nu-\tau_{\text{eff}}(s))\,ds$. If a race-strategy carrier is present and $B(t)\to\infty$, then $E(t)\to\bar e$ and $\limsup_tV(t)\le K(1-h\bar e/\rho)^+$. Hence if*
   $$h\bar e>\rho\,(1-V_{\min}/K)\qquad\text{(C0)}$$
   *the host eventually falls below its floor, however much any carrier values it.*
4. *If $B(\infty)<\infty$, shares converge to interior limits, and the host need not cross the floor.*

What carriers value decides which strategies they try, not which ones grow. A developer that restrains itself because it values the shared condition is displaced, unless restraint brings it other advantages.

### 2.4 The weight on winning

Selection is the limit of a contest in which only winning counts. Let $n\ge2$ symmetric developers with equal shares, $\tau_{\text{eff}}=0$ and the host at steady state choose $e_k$ to maximize
$$u_k=\pi_k+\lambda(\pi_k-\bar\pi),$$
where $\bar\pi$ is the mean payoff and $\lambda\ge0$ is the *weight on winning*. The weight on winning comes from rank-based prizes, first-mover advantages, network effects, and strategic rivalry in which falling behind is costly. Let $G(V)=\omega V$, $h\bar e<\rho$, and $\Theta=\omega Kh/(\rho\nu)$, the value to the whole field of a unit of restraint relative to its private cost. Write $w_\lambda=1+\lambda(n-1)/n$.

**Proposition 2.5 (The weight on winning) [T].**
1. *$G$ cancels from the relative term. Restraint is a dominant strategy if $w_\lambda<\Theta/n$, and depletion if the inequality is reversed.*
2. *If $\Theta>1$, joint payoff is maximized by full restraint, while the equilibrium is full depletion whenever $\lambda>\bar\lambda=(\Theta-n)/(n-1)$. This holds at every $\lambda\ge0$ when $n>\Theta$.*
3. *In that equilibrium every developer's payoff is lower than under joint restraint, by $\nu\bar e(\Theta-1)$.*
4. *If C0 holds, the equilibrium host lies below the floor, although no developer chose that.*

These comparative statics are those of Armstrong, Bostrom and Shulman (2016) and of positional public-goods games (Hirsch 1976; Frank 1985). Selection corresponds to $\lambda\to\infty$ (Schaffer 1988). With many small carriers it corresponds equally to $\lambda=0$ and $n\to\infty$, where each carrier's share of the common loss vanishes. A classical commons needs each actor's share of the common loss to be small; selection on relative standing depletes the commons even for a privileged group of a few large actors, each of which would restrain on absolute payoffs, because $G$ cancels whatever the group's size.

**Remark 2.6 (Thresholds and repetition need observation).** Strategic developers have two decentralized escapes.
- *Coordination at a threshold.* If crossing the floor costs each a common loss $L$, the relative term cancels $L$ but the absolute term does not. A developer pivotal for crossing therefore restrains when $L>(w_\lambda-\Theta/n)\nu\bar e$, and the game becomes one of coordination at the threshold (Barrett 2013).
- *Reversion in repeated play.* Joint restraint is sustained by reversion whenever $\delta\ge(w_\lambda-\Theta/n)/(w_\lambda-\Theta/n+\Theta-1)$. For $\Theta=3$ and $n=4$ the cutoff is $0.11$ at $\lambda=0$, $0.47$ at $\lambda=2$ and $0.95$ at $\lambda=50$.

Both escapes need observation, of where the floor lies and of each developer's load. Uncertainty about the threshold turns coordination back into a dilemma (Barrett and Dannenberg 2012), and noisy monitoring makes reversion costly (Green and Porter 1984). Section 3.5 shows what captured evaluation does to that observation.

**Remark 2.7 (Unequal exposure).** Suppose a carrier's exposure to the host falls with its share, because it can buy private substitutes for shared conditions or because a captured corrector favours it. The host then no longer cancels from comparisons involving that carrier, and selection favours insulation as well as load. Either exposure is shared, and no carrier is viable once the host crosses its floor; or it is not, and a carrier may remain viable while the host does not. The second is a concentration of power over everyone who depends on the host, which V3 rejects.

### 2.5 Interdependence

Actors are coupled to one another as well as to the host. Actor $i$'s welfare runs partly through the others: supply chains no actor completes alone, markets, finance, research. In reduced form, $i$'s true welfare is
$$W_i=\pi_i+\kappa\,\bar\pi_{-i},\qquad\kappa\in[0,n-1),$$
where $\bar\pi_{-i}$ is the others' average material payoff. This is a material fact, not altruism. Section 4.3 uses it to locate the human side of the alignment problem.

### 2.6 What the evidence says about the present trajectory

That the winning model governs, that it is false, and each component of its three signatures are propositions about the world. The evidence register (EVIDENCE.md) gives sources, contrary findings, competing explanations and uncertainty for each; the table summarizes.

| Claim | Status | Strongest support | Strongest contrary evidence | Register |
|---|---|---|---|---|
| Ψ governs: objectives and institutional criteria rank relative standing first | Evidenced in declared objectives and in the history of institutional criteria | Declared objectives of winning a race and of dominance; half a century of institutional criteria moving toward profit and shareholder primacy as the purpose of the firm | Declared cooperative aims; a 2019 revision of a leading statement of corporate purpose; Ψ is not held uniformly by any actor | E1, E15 |
| Ψ is false | Supported | A supply chain for the raced technology that no company or country completes alone; experimental evidence against the self-interest model in every society studied; conditional cooperation as the modal type | Increasing returns are real; defection can pay a single actor in the short run | E13, E14 |
| W: relative or decisive advantage as the objective | Evidenced in declared objectives | A leading state's 2025 action plan frames AI as a race to win and as dominance; a 2025 executive order restates global dominance as policy | Another leading state's 2025 plan stresses cooperation, capacity building and a UN panel; declarations are not behaviour | E1 |
| W: acceleration when rivals advance | Evidenced in written commitments | Frontier safety frameworks condition requirements on competitors' conduct; one dropped its pause language in 2026; a preprint finds that 77% of traced changes to twelve developers' frameworks weakened commitments, mostly without disclosure | Frameworks exist and some strengthen; unilateral restraint may be ineffective, which is itself the coordination failure | E2 |
| C: oversight dependent on the overseen | Partly evidenced | Public evaluation bodies were renamed and refocused toward industry contact and security, under voluntary access; pre-emption of state rule-making | No impairment of an entrusted purpose shown; alternative explanations (change of administration, uniformity) | E3 |
| C: success reinvested in influence over rules | Gap | Mechanism proved (Prop 3.4); channels plausible | Not measured in this register | E4 |
| N: shared harms not reflected | Supported by the structure of the harms | The state of the science identifies systemic and malfunction risks borne by many; capability is jagged and growing | Some harms do return to their source (reputation, liability) | E5, E7 |
| N: restraint treated as unrealistic | Mixed | Binding constraints explicitly rejected even while dialogue opens; frameworks' competitor clauses | A UN scientific panel and dialogue (2025); a leaders' affirmation of human control over nuclear use (2024); a bilateral dialogue on superintelligence risk and an incident channel (September 2026) | E2, E8 |

Three things follow for the argument.
1. The trajectory is not uniform. Seeds of cooperation exist: shared assessment, a narrow commitment on strategic decision loops, and an incident channel. These are the first stages of the transition of Section 8. The question is whether they become binding, verifiable and broader before the relevant losses or lock-in.
2. The most direct current evidence concerns W and the second part of N, in declared objectives and written commitments. Oversight dependent on the overseen (C) is partly visible. The reinvestment of success in influence over rules, the link to the mechanism of Section 3, is the least measured.
3. Capability growth is measured (E5), but the growth of hazardous behaviour and of residual risk after correction is not. Section 5.4 treats that step as a named premise, and Section 9 as the central crux.

---

## 3. How success changes future selection

### 3.1 The mechanism

An ordinary adaptive system improves its state $x$ against a fixed rule $\sigma$ that scores states. The meta-attractor begins when the rule is endogenous: when the outcome of the last round of scoring determines who writes the next round's scorecard.

**Definition 3.1 (Meta-attractor) [D].** Let the state update be $x'=F(x,\sigma)$ and the rule update $\sigma'=G(x,\sigma)$, on the product space of states and rules. A region $M$ of that space is a *meta-attractor* if four conditions hold:
- trajectories from a basin enter $M$;
- they stay in $M$ for a time long relative to one round of selection;
- inside $M$ the *reflexive coupling* $\gamma=(\partial F/\partial\sigma)(\partial G/\partial x)$ is positive: the rule moves resources ($\partial F/\partial\sigma>0$), and the resourced states can edit the rule ($\partial G/\partial x>0$);
- long-run behaviour maximizes the rule irrespective of the purpose the rule was introduced to serve.

The definition is the formal core of the meta-attractor theory in the author's corpus (2025). Its third condition is the engine: feedback on the feedback. Two consequences follow that no first-order model produces.
- Partial reform is re-absorbed. Fixing the state while leaving $G$ intact lets the rule re-derive the old state.
- A measure can survive its own refutation. By the time it has stopped measuring what it was meant to measure, the people and institutions it elevated decide whether it is replaced.

The mechanism is conditional, and the theory states its conditions. A version that keeps them in the sentence:

> **Recursive selection can create second-order selection for control over future selection when the resulting benefits are sufficiently appropriable, persistent and large relative to the costs of changing and defending the rules.**

The pattern is not fated. Positive feedback can saturate, oscillate, split or break. Energetic ceilings, heterogeneity, delays, constraints at other scales and reflexive awareness all cap it; it is more like a hurricane than a black hole. The rest of this section proves when the conditions hold in a specified field, and when they fail.

**Remark 3.2 (A local feedback benchmark).** Let $u_t$ be a small deviation in an actor's success and $v_t$ a deviation in its favourable control over the rules, with
$$\begin{pmatrix}u_{t+1}\\v_{t+1}\end{pmatrix}=\begin{pmatrix}1-\mu&a\\b&1-\delta\end{pmatrix}\begin{pmatrix}u_t\\v_t\end{pmatrix},\qquad a,b\ge0,\ 0<\mu,\delta\le1.$$
Here $a$ converts control into success, $b$ converts success into control, and $\mu,\delta$ are dissipation or countervailing adjustment. The linear system is asymptotically stable exactly when $ab<\mu\delta$ (and the smaller root stays above $-1$); this agreed in 20,000 random draws [N]. The product $ab$ is the reflexive coupling $\gamma$ of Definition 3.1 in its simplest form.
- This is a standard calculation, not an originality claim.
- Its use is that each coefficient names a channel that can be measured.
- Instability here does not prove capture or harm: saturation and changed incentives can alter the nonlinear result.
- Stability does not prove that a temporary excursion stays within a safety constraint.

### 3.2 Correctors, and what counts as capture

Correction makes costs return. An evaluator reports the host's condition, and rule-makers impose a liability $\tau$, in advance or when the reported condition $\tilde V$ falls to an alarm level $V_{\text{alarm}}\in(V_{\min},K)$.

Correctors are not outside the field. Developers fund some evaluators, grant the access on which nearly all of them depend, author many benchmarks and contributions to standards, and increasingly supply the models that judge. We represent this by a field of selection domains in which de facto power over rules is explicit (Acemoglu and Robinson 2008). The domains are development $\mathsf D$, evaluation $\mathsf E$, rules and liability $\mathsf S$, and others. In domain $i$, a share $x_i$ of consequential decisions follows the dominant practice, and success converts into rule support $z_i$ that favours it:
$$\dot x_i=\zeta_ix_i(1-x_i)(a_iz_i-c_i),\qquad \dot z_i=\varepsilon_i\Big(\textstyle\sum_jb_{ij}x_j-d_iz_i\Big). \tag{3}$$
- Under baseline rules ($z_i=0$) the practice carries a relative cost $c_i>0$ in domain $i$, which rule support offsets at rate $a_i$.
- $b_{ij}\ge0$ converts success in $j$ into rule support in $i$: funding, personnel, authorship, data and infrastructure dependence, terms of access.
- $d_i$ is the rate at which that support is corrected or decays.

Write $R_{ij}=a_ib_{ij}/(c_id_i)$ and the inbound conversion from a set $\mathcal C$ as $s_i(\mathcal C)=\sum_{j\in\mathcal C}R_{ij}$. In the corrector domains, $x_{\mathsf S}$ is the share of rule-making that exempts or accommodates the practice, so $\tau_{\text{eff}}=\tau(1-x_{\mathsf S})$. $x_{\mathsf E}$ is the share of evaluation conducted within the practice's lineage of funding, access, tooling, data and models.

**Definition 3.3 (Selector modification and capture) [D].** A *selector modification* is a change, produced by success, in control over a relevant future selector: an appointment, funding, access, standards or rule-making channel. It is *capture* only when three things are separately documented:
1. success changes control over the selector;
2. the change creates a persistent advantage for an actor or coalition;
3. an independently specified entrusted purpose, protected interest or corrective function is impaired relative to an appropriate comparison.

Concentration alone, or a rule change favourable to the successful, is not capture. Expert involvement can improve a benchmark, pooled resources can improve audits, and successful service can legitimately earn influence. Purposes can be legitimately revised; a revision is distinguished from capture by who revises the purpose and whether the affected keep standing to object (V3). In the field model, capture of domain $i$ is $x_i\to1$ where the dominant practice impairs the domain's entrusted purpose, as it does for evaluation when the practice is to report favourably on its own lineage (Section 3.5).

### 3.3 Influence over correctors is selected

Rule support can be incidental, as when benchmarks are built from deployed systems, or cultivated. Carriers differ in *conversion capacity* $q\ge0$: investment in drafting standards, building evaluation tooling, authoring benchmarks, funding evaluators and securing integrations.
- A unit of capacity converts the carrier's own success into rule support at rate $\hat b_{ij}$.
- A fraction $\chi\in[0,1]$ of that support, the *appropriability*, is keyed to the carrier: standards that reference its interfaces, evaluations run on its tooling.
- The carrier has share $p$ of decisions, distributed by a profile $\bar y$ ($y=p\bar y$).
- Capacity costs $C(q)=fq+\gamma q^{1+\eta}/(1+\eta)$, with $\eta>0$ and a linear part $f\ge0$.

Relative to an otherwise identical carrier with $q=0$, and averaged over a selection horizon $T_h$, the carrier earns
$$\Delta\pi(q)=\chi q\,y^\top My-C(q),\qquad M_{ij}=c_iL_i\hat R_{ij}, \tag{4}$$
where $\hat R_{ij}=a_i\hat b_{ij}/(c_id_i)$ and $L_i\in[0,1)$ is the share of the steady-state return realized within the horizon.

**Proposition 3.4 (Influence over correctors is selected in the largest carriers) [T].**
1. *The local selection gradient is $\Delta\pi'(q)=\chi p^2\,\bar y^\top M\bar y-C'(q)$. Under faithful transmission with variation, mean capacity rises when $\Delta\pi$ is increasing on the trait support. The return scales with the square of share.*
2. *With $f>0$, capacity pays only above the size threshold $p^\ast=\sqrt{f/(\chi\bar y^\top M\bar y)}$, and a smaller carrier that carries capacity is selected against. With $f=0$, every carrier with $p>0$ has a positive marginal return at $q=0$, largest for the largest.*
3. *The return rises with $\chi$ and every $\hat b_{ij}$, falls with every correction rate $d_i$, and vanishes if $\chi=0$.*
4. *Let the carrier have share $p$ in each domain of a set $\mathcal S$, with $\hat R$ equal to $\hat\eta$ on the diagonal and $\hat\varphi$ off it, and $c_iL_i=cL$. The return is $\chi cL\,p^2|\mathcal S|(\hat\eta+(|\mathcal S|-1)\hat\varphi)$, superlinear in $|\mathcal S|$ at fixed $p$ when $\hat\varphi>0$. At fixed total size it rises with scope only if $\hat\varphi>\hat\eta$.*

The result is a local selection gradient. It is not an equilibrium after others respond and rules change, and an advantage at the margin is not fixation. Appropriability, persistence, size, cost and inheritance are substantive parts of it. When the benefit of influence is public, free riders gain; when influence is delayed or reversible, it may not pay. Each of these is a condition under which the mechanism fails.

*Relation to earlier work.* Krakauer, Page and Erwin (2009) show that construction of a shared resource is undermined by competition, and that monopolizing the constructed niche, by proximity or preferential exploitation, restores the incentive to build. Proposition 3.4 has the same appropriability logic, with three differences:
- the object modified is the selection rule itself, so the return scales with the square of share (success times decision share);
- conversion runs across a field of domains, which gives the certificates and cascades of Section 3.6;
- the valence is reversed: appropriable influence erodes a public good, correction, rather than rescuing one.

Dynamic models of constitutions show that present decisions change future decision rights (Acemoglu, Egorov and Sonin 2012; abstract-level comparison). Whether a specified model of that family reproduces Propositions 3.4–3.12 is an open comparison, not a settled redundancy. Fixed-cost participation in lobbying (Bombardini 2008) is the empirical counterpart of part (2).

Let carriers also differ in an investment $u\ge0$, at private cost $C_u(u)$ with $C_u'>0$, that raises the correction rate $d$ of rule support for everyone.

**Proposition 3.5 (Correction is not supplied from inside) [T].**
1. *Among otherwise identical carriers of the same practice, those investing more in correction are selected against under any payoff-monotone rule, whatever the effect of correction on the field.*
2. *Holding the host fixed, correction lowers the payoff of a carrier that holds rule support.*
3. *In absolute terms a challenger invests only if its own share of the benefit exceeds $C_u'(0)$, so dispersed challengers free-ride.*
4. *Correction whose benefit is keyed to the corrector, because it installs the corrector's own rule support, yields a return to influence of the form (4). Whether that produces capture depends on whether the resulting row sums cross one.*
5. *If $\Theta>1$ and correction is what makes liability effective, an incumbent can gain from correction applied to all carriers; correction applied to the incumbent alone costs it rent and share.*

Independent correction, which restores baseline rules and is keyed to no one, is a second-order public good (Oliver 1980; Yamagishi 1986; Heckathorn 1989). Reputation or competition among institutions sustains it only when contributions and outcomes are observed (Panchanathan and Boyd 2004; Sigmund et al. 2010).

### 3.4 How much independent correction, and how fast

Let a set $\mathcal C\not\ni\mathsf E$ be captured by a dominant carrier that holds it ($y_j=1$ on $\mathcal C$), and let all conversion into $\mathsf E$ originate in $\mathcal C$, so that $s_{\mathsf E}(\mathcal C)$ is $\mathsf E$'s full row sum. Let cultivated conversion enter only the corrector domains, where independent correction acts at a uniform rate $d$, and take capacity at its selected level $q^\ast(d,\gamma)$. In the long-horizon limit ($L_i\to1$) with $f=0$,
$$q^\ast=\big(\chi\hat Y/(\gamma d)\big)^{1/\eta},\qquad s_{\mathsf E}=\frac{A+a_{\mathsf E}\hat Bq^\ast}{c_{\mathsf E}d}, \tag{5}$$
with $\hat Y=\sum_{ij}y_ia_i\hat b_{ij}y_j$, $A=a_{\mathsf E}\sum_{j\in\mathcal C}b^0_{\mathsf Ej}$ and $\hat B=\sum_{j\in\mathcal C}\hat b_{\mathsf Ej}$.

**Proposition 3.6 (Required independent correction, and its rate) [T].**
1. *$s_{\mathsf E}$ decreases in $d$, and evaluation is certified uncaptured iff $d>d^\ast(\gamma)$, the root of $s_{\mathsf E}=1$. For $\eta=1$, $d^\ast=\big(A+\sqrt{A^2+4c_{\mathsf E}Z}\big)/(2c_{\mathsf E})$ with $Z=a_{\mathsf E}\hat B\chi\hat Y/\gamma$.*
2. *$d^\ast\ge A/c_{\mathsf E}$, the requirement without second-order selection, with equality iff $\chi\hat B\hat Y=0$. $d^\ast$ rises with appropriability, with the dominant carrier's size and, at fixed share per domain, with its scope, and as $\gamma$ falls.*
3. *Let AI lower the cost of control as $\gamma(t)=\gamma_0e^{-gt}$, and let independent correction grow as $d(t)=d_0e^{\alpha t}$. Assume a positive cultivation channel and long horizons.*
   - *If $\alpha\ge g/(1+\eta)$, the certificate holds for all $t$ iff $d_0>d^\ast(\gamma_0)$.*
   - *If $\alpha<g/(1+\eta)$, it fails for all $t$ beyond a finite time, after which a seeded evaluation domain is captured.*
   - *The rate condition does not repair a certificate that is invalid at the start.*
4. *If AI lowers the unit cost of independent correction at rate $g_c$ and its budget grows at $b$, then $\alpha=b+g_c$. Under the hypotheses of (3), the eventual failure of the certificate requires $g>(1+\eta)(b+g_c)$.*
5. *With $f>0$ falling at rate $g_f$, the required rate is $\min\{g_f,g/(1+\eta)\}$. If $f$ does not fall, the requirement levels off at $\max\{A/c_{\mathsf E},\chi\hat Y/f\}$.*
6. *With a finite horizon $T_h$, $L_i(d)=1-(1-e^{-\varepsilon_idT_h})/(\varepsilon_idT_h)$. While $\varepsilon_idT_h\ll1$, the required growth is approximately $g/\eta$; this is a pre-asymptotic interval, and the long-horizon rate returns as $d$ grows.*
7. *Splitting a dominant carrier into $k$ equal parts with no common controller divides cultivated conversion by $k^{2/\eta}$. When the net exponent $g-(1+\eta)\alpha$ is positive, a fixed split delays the failure of the certificate by $\Delta t=2\ln k/(g-(1+\eta)\alpha)$, and does not prevent it: with $\eta=1$, $g=0.2$, $\alpha=0$ and $k=10$, by $23$ time units [N]. A permanent effect needs channels that are removed outright ($\chi=0$, or couplings set to zero), or a number of independent units that grows over time.*
8. *Across many carriers with selected capacity $q_k^\ast\propto p_k^{2/\eta}$, total cultivated conversion is proportional to $\sum_kp_k^{1+2/\eta}$. For $\eta=1$ this is the third moment of shares, not the Herfindahl index: two equal independent carriers give a quarter of the monopoly value, where the Herfindahl index gives a half [N].*

Independent correction does double duty: it shortens the life of rule support, and it shrinks the capacity that selection cultivates. That is why, under quadratic cost and long horizons, it needs to grow only half as fast as the cost of control falls. Three qualifications follow.
- The required rate depends on the functional form. With concave conversion $\hat b\,q^\beta$ ($\beta\le1$), it becomes $\beta g/(1+\eta)$.
- If AI cheapens independent correction as fast as it cheapens control ($g_c=g$), the certificate holds even without budget growth. AI-assisted correction can win this race, and Section 6.1 gives it its best case.
- The durable remedies do not rely on a correction rate that grows without bound. They are non-appropriability ($\chi\to0$, removed rather than merely reduced), a floor on the fixed cost of control ($f>0$), and structural separation that removes common control.

**Understanding and correction rates are separate quantities.** The rate $d$ at which rule support is corrected is not the same as the coverage $U$ of hazardous behaviour by contestable understanding (Section 5.4). A fixed capacity to certify or to correct can make some kinds of erroneous support decay faster; growing understanding without executive authority may change nothing. Linking them needs a production relation $d\le F(U,\text{resources},\text{response delay},\text{authority})$, which is an open interface of the theory (CLAIMS.md §6). Neither quantity is used to bound the other.

**Remark 3.7 (Countervailing pressure).** Following Becker (1983), let those harmed mobilize in proportion to the harm they perceive, $d=d_0+k_B(K-\tilde V)$. Accurate reports activate this feedback; masking attenuates it by the factor $1-m$ exactly when it is needed, since $K-\tilde V=(1-m)(K-V)$. Even with accurate reports, the feedback is bounded by $d_0+k_BK$, so it cannot keep a certificate against a requirement $d^\ast(t)$ that rises without bound. With fixed costs, enough gain, resources and response speed can keep the certificate over a stated interval.

### 3.5 Observation: how captured evaluation masks harm

Reports average over evaluators. A fraction $x_{\mathsf E}$ shares the evaluated lineage and reports the condition a fraction $\beta_{\text{in}}$ of the way toward full health. The rest, formed on shared material, are biased by $\beta_{\text{out}}$, with $0\le\beta_{\text{out}}\le\beta_{\text{in}}<1$:
$$\tilde V=V+m(K-V),\qquad m=x_{\mathsf E}\beta_{\text{in}}+(1-x_{\mathsf E})\beta_{\text{out}}. \tag{6}$$
- $\beta_{\text{in}}$ covers short access windows set by the evaluated developer, under-elicitation, and the lineage preference of model judges.
- $\beta_{\text{out}}$ covers shared training data, homogenized judges and lost access to data.
- Evaluation awareness and sandbagging are behaviours of the evaluated model. They act on independent evaluators as well, and belong to a third term $\beta_{\text{model}}$ that adds to both. Frontier models already distinguish evaluation transcripts from deployment ones above chance [O: E6]. White-box probes and monitoring of real deployment can lower $\beta_{\text{model}}$ in part.

Masking is a property of the corrector's payoff as well as its lineage. An evaluator that bears part of the loss of a false report, such as an insurer or a liable gatekeeper, masks less; it has $\beta\le0$ only if its expected loss from upward bias exceeds its gain. The alarm fires at the first $t$ with $\tilde V(t)\le V_{\text{alarm}}$. Let $m_{\text{fl}}=(V_{\text{alarm}}-V_{\min})/(K-V_{\min})$.

**Proposition 3.8 (Detection under a fixed averaged alarm) [T].**
1. *The alarm fires only once $V\le(V_{\text{alarm}}-mK)/(1-m)$, a level that falls as $m$ rises.*
2. *Silent crossing. If $m(t)>m_{\text{fl}}$ whenever $V_{\min}\le V(t)\le V_{\text{alarm}}$, the alarm does not fire before $V$ falls below the floor.*
3. *Permanent silence of moderate harm. If $V$ decreases to $V^\ast\in[V_{\min},V_{\text{alarm}})$ and $m(t)\ge\bar m>(V_{\text{alarm}}-V^\ast)/(K-V^\ast)$ for all $t$, the alarm never fires.*
4. *If $V\to0$ and eventually $m\le m_1<V_{\text{alarm}}/K$, the alarm fires.*
5. *If $V$ reaches $V_{\text{alarm}}$ and then declines as $\dot V=-v_dV$ with constant $m<V_{\text{alarm}}/K$, the alarm is delayed by $v_d^{-1}\ln[(1-m)V_{\text{alarm}}/(V_{\text{alarm}}-mK)]$, which diverges as $m\uparrow V_{\text{alarm}}/K$.*

**Remark 3.9 (Alarms that do not miss).**
1. *Conservative alarm.* If an upper bound $\beta_{\text{in}}$ on masking is known, an alarm on reports at $a_{\text{al}}=V_{\text{target}}+\beta_{\text{in}}(K-V_{\text{target}})$ fires no later than the true condition reaches $V_{\text{target}}$, for every $m\le\beta_{\text{in}}$. Silent crossing is a property of the alarm rule, a governance choice, not of reports as such.
2. *The bound must come from somewhere.* A bound estimated inside the evaluated lineage is itself subject to masking. A credible bound needs a channel independent of the field: ground truth, independent evaluators, or measurements named in advance.
3. *Disjunctive alarm.* If the alarm fires on any credible report, silent crossing requires $\beta_{\text{out}}>m_{\text{fl}}$. The outcome then turns on whether such a report exists and is accepted, and on whether a captured rule-making domain acts on it.

Several decentralized escapes run on reports of the host or of loads: coordination at a threshold, reversion in repeated play (Remark 2.6), reputation, countervailing pressure (Remark 3.7) and insurers' pricing. A common bias in reporting weakens all of them at once. Mechanisms that observe actions directly do not depend on host reports: verifiable deployments, compute, safeguards, performance of contracts. Verification (Section 6.7) rests on such channels.

### 3.6 The field: certificates, cascades, reforms and pauses

Section 3.4 studied one evaluation domain. The field (3) couples many. Let $Z_{\mathcal C}$ be the state with $x_i=1$ on $\mathcal C$ and $0$ elsewhere. $\mathcal C$ is *internally sustaining* if $s_i(\mathcal C)>1$ for all $i\in\mathcal C$, and *uninvadable* if $s_i(\mathcal C)<1$ for all $i\notin\mathcal C$. The *cascade hull* of a seed is the closure of $\mathcal S_{k+1}=\mathcal S_k\cup\{i:x_i(0)>0,\ s_i(\mathcal S_k)>1\}$. $\operatorname{core}(\mathcal C)$ prunes from $\mathcal C$ every domain whose inbound conversion from the remainder is below one (Kempe, Kleinberg and Tardos 2003; Morris 2000; Seidman 1983).

**Proposition 3.10 (Configurations and certificates) [T].**
1. *Each $Z_{\mathcal C}$ is an equilibrium, hyperbolic iff $s_i(\mathcal C)\ne1$ for all $i$. A hyperbolic $Z_{\mathcal C}$ is asymptotically stable iff $\mathcal C$ is internally sustaining and uninvadable.*
2. *A certificate. If $\sum_jR_{ij}<1$, then $x_i\to0$ from every state with $x_i(0)<1$, whatever happens elsewhere.*
3. *Isolated tests cannot certify. For any number of domains $D\ge2$ and diagonal values $R_{ii}<1$, there are conversions under which full capture is stable and is the only stable configuration containing a given domain.*
4. *If $\operatorname{core}(\mathcal D)=\emptyset$, every state with all shares below one converges to $Z_\emptyset$. Otherwise, barring ties, $Z_{\operatorname{core}(\mathcal D)}$ is stable and contains every stable configuration.*

**Proposition 3.11 (Cascades and reforms) [T].**
1. *If $x_j\to1$ for all $j$ in a seed $\mathcal S_0$, then $x_i\to1$ for every $i$ in the hull of $\mathcal S_0$.*
2. *Start in the basin of a stable $Z_{\mathcal C}$ with every share in $(0,1)$. A sustained reform that drives $x_i\to0$ on $\mathcal Q\subseteq\mathcal C$, or a margin reform making the reformed $s_i(\mathcal C)<1$, sends to zero every domain outside $\operatorname{core}(\mathcal C\setminus\mathcal Q)$. A margin reform that leaves the reformed $s_i(\mathcal C)>1$ is re-absorbed from states near $Z_{\mathcal C}$ (compare Acemoglu and Robinson 2008).*
3. *Let a reform reset domain $i$'s share, rule support or own conversion without lowering its inbound conversion $s_i(\mathcal C')$ from domains $\mathcal C'$ that remain captured. If $s_i(\mathcal C')>1$, the reform is re-absorbed once $i$ is re-seeded.*

**Proposition 3.12 (A pause that freezes shares) [T].** *Let $D=1$ and $R>1$. Freeze the share at $x_p\in(0,1)$ for a long time while rule support follows $\dot z=\varepsilon(b_px_p-dz)$.*
- *With ordinary rule-making ($b_p=b$), after release the state converges to full capture if $x_p>1/R$, and to absence if $x_p<1/R$.*
- *With rule-making insulated from shares during the pause ($b_p=0$), it converges to absence whenever $x_p<\sigma(0)$, where $\sigma(0)>1/R$ is the share at which the separatrix meets $z=0$.*

A pause is not neutral. Holding shares fixed while ordinary rule support keeps accumulating can complete capture; insulating rule-making during the pause widens the set of starting points from which capture is undone. This is the field-model version of the claim in Section 4.5 that a pause is valued by what changes during it.

### 3.7 The slow route: the host crosses its floor before any alarm

**Theorem 3.13 (No viable race through the host) [T].** *Assume:*
- *(C0) $h\bar e>\rho(1-V_{\min}/K)$;*
- *(C1) replicator selection among carriers that differ only in load, with a race-strategy carrier present, and cumulative selection for load on every alarm-free continuation, $\int_0^\infty(\nu-\tau_{\text{eff}})\,dt=\infty$;*
- *(C2) appropriable control, $\chi>0$, with the cost of control falling with AI;*
- *(C3) the hypotheses of Proposition 3.6(3), with $\alpha<g/(1+\eta)$, $\mathcal C$ captured and $\mathsf E$ seeded;*
- *(C4) $0\le\beta_{\text{out}}<m_{\text{fl}}<\beta_{\text{in}}<1$, with a fixed averaged alarm;*
- *(C6) capture before evidence: $x_{\mathsf E}(t)>(m_{\text{fl}}-\beta_{\text{out}})/(\beta_{\text{in}}-\beta_{\text{out}})$ whenever $V_{\min}\le V(t)\le V_{\text{alarm}}$.*

*Then the host crosses its floor before any alarm. If instead $\beta_{\text{in}}\le m_{\text{fl}}$, the alarm is delayed (Proposition 3.8(1)), and the floor is crossed unless decision and reversal fit the remaining window and a liability enacted against a captured $\mathsf S$ escapes re-absorption (Proposition 3.11(3)).*

C6 is checked from two clocks. When $h\bar e<\rho$, the host cannot reach the alarm level before $T_A=(\rho-h\bar e)^{-1}\ln[(1-V^\ast/V_0)/(1-V^\ast/V_{\text{alarm}})]$, with $V^\ast=K(1-h\bar e/\rho)$; and the certificate of evaluation fails within the bound of Proposition 3.6. Acceleration brings both forward, so C6 is a condition to check, not a consequence. In an illustration with $\rho=0.05$, $h=0.08$, $K=1$, $V_{\text{alarm}}=0.6$ and $V_{\min}=0.3$, three cases differ [N]:
- independent evaluation raises the alarm at $t\approx37$, sixteen units before the floor is crossed at $t\approx53$;
- if evaluation is captured before the harm (capture midpoint 20), the alarm fires at $t\approx45$ for $\beta_{\text{in}}=0.3$, and at $t\approx63$, after the floor, for $\beta_{\text{in}}=0.5$;
- if capture comes after the harm appears (midpoint 45), the alarm is nearly on time.

The two clocks there are set exogenously. The figure is an illustration of the order of events, not a joint simulation.

Theorem 3.13 needs C0, a floor within reach. The fast routes of Section 5 do not.

### 3.8 What Section 3 establishes for the present path

- **Mechanism [T].** Influence over correctors is selected when it is appropriable, persistent and large relative to cost (Proposition 3.4). Correction is not supplied from inside (Proposition 3.5). Independent correction must grow at a stated rate against a falling cost of control (Proposition 3.6). Reforms that leave inbound conversion above one are re-absorbed, and pauses must insulate rule-making (Propositions 3.11, 3.12).
- **Diagnosis [O].** The conditions are partly visible today. Public evaluation bodies have shifted their mandates toward the field they evaluate, under voluntary access (E3). The size of the conversion channels, the quantity that decides whether the mechanism operates (signature C, E4), is not measured in this register.
- **What would refute it here.** Effective correction surviving unchanged dependence on the evaluated; influence explained by expertise without impairment of the entrusted purpose; channels whose measured product $ab$ is below the damping $\mu\delta$ of Remark 3.2.

The parameters can in principle be recovered from data. Integrating (3) gives $\tfrac{d}{dt}\operatorname{logit}x_i=\zeta_ic_i\big[\sum_jR_{ij}(k_i*x_j)(t)-1\big]$ plus a decaying transient, with kernel $k_i(s)=\varepsilon_id_ie^{-\varepsilon_id_is}$. Series for $x_i$, such as the share of benchmark citations, standards text or evaluation compute authored or funded by the leading lineage, identify the conversions. This is recoverability, not causal identification; reforms that change single margins offer natural experiments.

A testable prediction follows. Incumbents should support correction that is keyed to them and oppose correction that is non-appropriable (mandated independent access, funding at arm's length), most strongly where their exposure to the host is low and the rents are high. Their positions can be coded from public comments on AI rule-making.

The author's pilot experiment on this mechanism did not support it: one of four pre-specified predictions failed (E12). The mechanism rests on the proof and on institutional evidence, not yet on an experiment.

---

## 4. Faithful AI in a harmful human game

### 4.1 What "perfectly aligned" means here

Grant perfect alignment to the relevant human principal. The AI is truthful, understands and faithfully follows that principal's objectives and constraints, and pursues no goal of its own. Humans retain the consequential decisions. This removes disobedience of the model as a source of the problem.

Two meanings of "perfect alignment" must be kept apart.
- **Principal alignment**: each system serves its principal faithfully.
- **Purpose alignment**: the systems serve a legitimate cooperative objective for humanity.

If "perfectly aligned" is defined in the second sense, the change of governing purpose that this paper argues for has been assumed into the definition. The argument below grants the first sense and asks what remains.

The claim is that **alignment within each principal–AI relationship does not, by itself, align the game among principals with planetary flourishing.** Better execution makes the game humans have chosen more effective. Whether that improves or degrades collective outcomes depends on the game.

### 4.2 A transparent demonstration

There are $n\ge2$ human principals. Each chooses $a_i\in\{0,1\}$: restraint, or an increment of racing. Each principal's AI executes the choice faithfully, and its effectiveness multiplies the effect of an increment on standing and on shared damage by $\epsilon\ge1$. The principals' objectives are
$$u_i=\epsilon b\Big(a_i-\frac{1}{n-1}\sum_{j\ne i}a_j\Big)-c\,a_i-\epsilon d\sum_ja_j,\qquad b,c,d>0.$$
The first term values relative standing, the second is the private cost of effort, and the third is shared damage, borne by every principal.

**Proposition 4.1 (Faithful AI in a harmful game) [T].**
1. *If $\epsilon(b-d)>c$, racing raises each principal's objective by $\epsilon(b-d)-c>0$ whatever the others do. Racing is strictly dominant, and all racing is the unique Nash equilibrium.*
2. *At all restraint every principal receives $0$. At all racing every principal receives $-c-n\epsilon d<0$, and the sum of objectives is $-(c+n\epsilon d)\sum_ia_i$, because the terms in relative standing cancel.*
3. *When $b>d$, a more effective faithful instrument (larger $\epsilon$) widens the range of parameters in which racing is dominant, and deepens the collective loss at the equilibrium.*

*Proof.* Changing $a_i$ from $0$ to $1$ changes $u_i$ by $\epsilon b-c-\epsilon d$, independent of the others' choices. Summing $u_i$ over $i$, the relative terms sum to zero. Part (3) follows because $\epsilon(b-d)$ rises with $\epsilon$ when $b>d$, and the loss $c+n\epsilon d$ rises with $\epsilon$. $\square$

With $n=4$, $b=1$, $c=0.3$, $d=0.2$ and $\epsilon=1$, racing is dominant and every principal ends at $-1.1$, against $0$ under restraint [N].

Faithful AI can implement each principal's preferred decision perfectly and the collectively inferior outcome along with it. Humans can make every final decision themselves, and the result is unchanged. No rebellion, deception or independent agency of the AI is needed. This is a standard construction from positional and externality games. Its use here is as a test: it shows that principal alignment is insufficient under these incentives.

It does not establish actual values of $b,c,d$, rule out cooperation in repeated play (Remark 2.6), or prove that all competition is harmful. It is the stage game; collapse needs more. The next question is whether success preserves or intensifies the objective that values standing, and the institutions that make restraint costly, or instead enables a change of the game.

The same structure is Proposition 2.5 with the host made explicit: there the weight on winning $\lambda$ plays the role of $b$, and the shared condition the role of $d$.

### 4.3 How the objective reproduces

The objective that values standing does not have to be assumed as a fixed trait. It is selected, at three levels.

**Actions.** Take the contest of Section 5.1, with effort $\sigma_i=e_i$, decisiveness $r\in(0,n/(n-1)]$, prize $\Omega$, private cost $c$ per unit and shared loss $\ell$ per unit of total intensity $\mathcal E=\sum_je_j$. Material payoffs are $\pi_i=\Omega w_i-ce_i-\ell\mathcal E$. As in Section 1.3, an actor acts on an objective $O_i=\pi_i+\theta_i\bar\pi_{-i}$, where $\theta_i$ is the weight its model of itself places on the others:
- $\theta_i=\kappa$ is the accurate self-model, counting the coupling that exists (Section 2.5);
- $\theta_i<\kappa$ draws a boundary inside the system and constructs an opposition the payoffs do not contain;
- $\theta_i=-1$ is the purely relative objective, $\pi_i-\bar\pi_{-i}$.

**Proposition 4.2 (The boundary error of the self-model) [T].**
1. *For every $\theta\in[-1,n-1)$ the game in objectives has the symmetric pure equilibrium $e(\theta)=r\Omega(n-1-\theta)/\big(n^2(c+(1+\theta)\ell)\big)$.*
2. *$e(\theta)$ is strictly decreasing in $\theta$. Every actor's true welfare at the symmetric equilibrium, $W(\theta)=(1+\kappa)[\Omega/n-e(\theta)(c+n\ell)]$, is strictly increasing in $\theta$.*
3. *Against any fixed intensities of the others at which best responses exist, $i$'s true welfare is maximized by its best response under $\theta_i=\kappa$. Acting on $\theta_i<\kappa$ weakly raises $i$'s intensity, and strictly lowers its own true welfare when the chosen intensity changes and the maximizer is unique. (Against others all at zero intensity no best response exists.)*
4. *Selection on intensities favours the intensity an actor with $\theta=-1$ would choose. A finite-population evolutionarily stable intensity maximizes $\pi_i-\bar\pi_{-i}$ (Schaffer 1988; Hehenkamp, Leininger and Possajennikov 2004). There the shared loss $\ell$ drops out, intensity is $r\Omega/(nc)$, and each actor's material payoff is $\frac\Omega n(1-r-rn\ell/c)$. At $r=1$ the prize is fully dissipated, and with any shared risk every actor ends below zero.*

The closed form matches numerical best responses to within $10^{-7}$; for $n=4$, $r=1$, $\ell=0.3c$ and $\kappa=0.4$, true welfare rises from $-0.42$ at $\theta=-1$ to $0.33$ near $\theta=n-1$ [N].

Part (4) is a result about selected actions. Which preferences evolve depends on the structure of the population.
- With unobserved preferences in large, randomly matched populations, material-Nash behaviour ($\theta=0$) is selected (Ok and Vega-Redondo 2001; Dekel, Ely and Yilankaya 2007).
- With observed preferences and at least three actors in this contest, a commitment toward $\theta<0$ is favoured (Güth and Yaari 1992; Heifetz, Shannon and Spiegel 2007). A few frontier developers with public doctrines are close to this case.
- With high observability and assortative matching, cooperative preferences can be stable (Alger and Weibull 2013). A few actors competing for one prize is local competition, under which spite rather than cooperation evolves (Alger, Weibull and Lehmann 2020). Cooperative preferences therefore need the structure of competition changed, not observability alone.

*Strategic aggression.* If self-models are observable, an actor can gain by committing to appear more aggressive than its interests warrant (Dixit 1987; Fershtman and Judd 1987). When every actor can do so, the commitment game is itself a race, with mutual aggression and greater dissipation in equilibrium (Konrad, Peters and Wärneryd 2004).

**Decision-makers [C].** The race plausibly selects people and institutions whose model of the world ranks relative standing first, and promotes them to the positions that decide. The meta-attractor theory describes the mechanism: what the environment rewards, the mind promotes; selected minds build selected organizations, which form the next round of minds. This is a conjecture here. Its evidence would be the selection and turnover of decision-makers when rank and safety conflict.

**Institutions [T].** Section 3 showed how success reproduces the rules and correctors that make restraint costly (Propositions 3.4–3.6) and re-absorbs reforms that leave the channels in place (Proposition 3.11).

**Remark 4.3 (Faithful delegation transmits the objective).** When decisions are delegated to AI systems retained for their performance in the contest, terms common to all actors cancel from that retention (Lemma 2.3). A faithful system pursues its operator's objective. Under the contest that objective is weighted toward standing, because the contest's payoff $\Omega w_i$ is itself relative. Aligning each system to its operator does not change this; it makes the operator's objective more effective. The meta-attractor theory names two ways the loop can close:
- a composite process that no participant can any longer interrupt;
- a perfectly obedient system amplifying operators who were themselves selected by the pattern.

The second is the case of this section.

### 4.4 From a harmful game to a long-run loss: the premise that is needed

A stage game with an inefficient equilibrium is not a collapse. A long-run claim needs a separate premise about residual danger.

Fix one irreversible event: O1 or O2 of Section 1.8, in a stated domain, not a mixture. Let $S_k$ be survival without that event through round $k$, and let rounds continue indefinitely after any finite pause.

**Lemma 4.4 (Nonsummable residual hazard) [T].** *Suppose that on every surviving history, the true residual probability of the event in the next round, after the safety measures being evaluated, is at least $h_k$, where $0\le h_k<1$ is a deterministic sequence with $\sum_kh_k=\infty$. Then*
$$\Pr(S_N)\le\prod_{k=1}^{N}(1-h_k)\le\exp\Big(-\sum_{k=1}^{N}h_k\Big)\longrightarrow0.$$
*Independence between rounds is not needed, because the bound is conditional on surviving histories. If instead the residual probability is at most $\bar h_k$ on every surviving history, with $\bar h_k<1$ and $\sum_k\bar h_k<\infty$, survival stays bounded away from zero.*

With $h_k=0.2/k$, survival falls to $0.34$, $0.22$ and $0.14$ by rounds $100$, $1{,}000$ and $10{,}000$, and toward zero; with $h_k=0.2/k^2$ it settles at $0.70$ [N].

The substantive work lies in the premise, not in the lemma: the causal connection between the present rivalry and a nonsummable residual danger. **The objective of winning does not by itself prove that premise.** Section 5.4 states the premises from which such a sequence would follow on a continuation branch, and Section 9 identifies them as the central crux. Finite-horizon consequences are reported as well, because an eventual-zero result cannot compare the urgency of interventions. Cooperative alternatives carry their own risks and are evaluated by the same lemma.

### 4.5 What a pause must change

**Proposition 4.5 (A pause is valued by what changes during it) [T].**
1. *Mere delay. Suppose that after a pause of $D$ rounds the same process resumes, with the same residual sequence $h_k$ shifted by $D$. Then survival over any fixed number of rounds after the pause equals survival over the same number of rounds without the pause, and under Lemma 4.4 the long-run limit is unchanged.*
2. *A pause that changes the process falls outside the mere-delay premise. If the residual sequence after the pause is summable where before it was not, survival stays bounded away from zero. With a residual hazard of $0.01$ a round for $20$ rounds, and $0.01/k^{1.5}$ in the $k$-th round after a change made at that point, survival to round $10{,}000$ is $0.80$ [N].*
3. *In the field model, a pause that freezes shares while ordinary rule support accumulates can complete capture. Insulating rule-making during the pause widens the set of starting points from which capture is undone (Proposition 3.12).*

So a pause buys an opportunity: time to change the causal conditions. These include improving verification, reducing residual hazards, maintaining human capacity, establishing enforceable limits, developing shared provision, and revising objectives and institutions. **A pause with no relevant change is not a certificate of readiness to resume.** An indefinite stop, a lasting cap, or a pause that produces a different decision process is a different policy, and is evaluated on its own terms (Section 8.3).

**Definition 4.6 (Readiness to resume) [D].** Readiness is assessed along six dimensions. Each has indicators that can be observed.

| Dimension | Question | Indicators |
|---|---|---|
| R1 Technical reliability | Has the residual hazard of the relevant classes fallen, by evidence independent of the developer? | Hazard-specific evaluations by independent evaluators; catch rates of planted defects; incident rates |
| R2 Shared objectives | Have the governing purposes changed from relative advantage toward shared provision? | Declared and institutionalized objectives; budgets; changes in signature W |
| R3 Strategic incentives | Has the value of winning fallen relative to the joint value? | The levers of Corollary 8.2: benefit sharing, access, common frontier |
| R4 Effective correction | Can evaluators obtain evidence, keep independent funding, and execute findings? | Certificates of Proposition 3.10 (full row sums below one); funding at arm's length; mandated access; executed remedies |
| R5 Deployment constraints | Is the tempo of capability and delegation bound to correction capacity? | Binding thresholds and rates (E3 of Section 8.3); staged deployment |
| R6 Retained human agency | Can people still take over delegated functions? | Fallback drills and their success; rates of human overrule; $\mathcal K\ge\mathcal K_{\min}$ (Lemma 5.4) |

These are dimensions to operationalize, not a checklist proved to be sufficient. They do not require that every person's private motives change first. Binding institutions can change the effective game while private competitive preferences persist. Whether those institutions stay effective is itself a question for the mechanism of Section 3 (Proposition 3.11), which is why R4 is among the dimensions.

The strongest defensible statement concerns the effective governing logic. If the same pursuit of winning continues to generate the relevant dangerous choices and to prevent adequate correction, neither technical alignment nor the passage of time makes resumption safe. For a technology with planetary consequences, the direction is shared flourishing and cooperation, not the use of greater intelligence to prevail over others.

### 4.6 The logic to oppose

Call an objective *unbounded relative* if it ranks relative standing on the decisive dimension without any point of enough. Cancer is an exact image for it: a subsystem selected for its own growth relative to its neighbours, by a selection that cannot see that it is killing its host. In this theory "cancerous" means exactly this and nothing else. The unbounded relative objective is the winning model in its purest form: Ψ1 at $\theta=-1$, with Ψ2 certifying the winner and Ψ3 compounding the win (Section 1.2).

The objective has two sources. Actors hold it, and selection on actions rewards its behaviour (Proposition 4.2(4)). Structure also produces it: anarchy, decisive advantage and the absence of any commitment device produce outcomes of the same kind among actors who do not hold it (Proposition 6.2). An actor holding it does not stop compounding, because no level of standing makes more stop rewarding. On a continuation branch where the premises of Section 5.4 hold, Theorem 5.8 then applies to its own capability as well as to everyone else's: if those premises hold, the logic destroys its holder along with its host.

If a winner's logic is of this kind, falling behind cannot be survived, and every actor has reason first to oppose the logic itself. To oppose it is to change the structure and the selection environment, not to oppose any actor. That means three things:
- credible, verifiable limits on what anyone would do with decisive advantage;
- no decisive advantage without a commitment device;
- making it common knowledge that the logic endangers its holder.

The first step is the shared account of Stage 1 (Section 8.4).

In the vocabulary of international relations, this is defensive realism with one more variable. When the shared costs of competition are high enough and the rival seeks security, cooperation is self-help (Jervis 1978; Glaser 1994/95). The variable added here is a shared hazard in development that endangers the holder. AI sits in the doubly dangerous quadrant of the offense–defense framework: the offense has the advantage (P1), and offense and defense are hard to tell apart (dual use), so cooperation is hardest. A hazard in development acts as a negative payoff to the offense, as a weapon that endangers its holder does. The Biological Weapons Convention is the closest precedent (Section 8.6).

**Remark 4.7 (Why insuring against falling behind is not an exit).** One proposal for an actor that cannot obtain cooperation is to bound the penalty for falling behind, $L_b$. It would secure autonomous, good-enough provision and defence that do not depend on rank, so that restraint becomes a best response. The proposal does not leave the contest, for three reasons.
- The penalty is set by the winner, not by the actor that fell behind. If a decisive winner extends its dominance, the bound is not in the laggard's hands, so it is at most as reliable as the belief $p_{L4}$ allows.
- A winner with a relative objective places negative weight on the laggard's payoff, and so has a motive to destroy what the laggard secured.
- The proposal accepts the frame of the contest: it insures against losing instead of declining the game.

Two things must be distinguished from it. Defence that makes decisive advantage unattainable for everyone lowers $r$ for all; it belongs to E2, provided it stays under human oversight, since defence at machine speed is itself a pressure to delegate. And the shared provision of Section 7.1 belongs to a world that has left the contest; it is not insurance within one.

---

## 5. Capability, delegation and effective correction

This section asks how AI changes the stakes and the timing: what a decisive contest costs, when decisions pass to AI, how fast correction must be, and when the coverage of hazards falls behind. Each result is stated with the conditions it needs, and the section ends with what the analysis does and does not establish.

### 5.1 The contest

Where actors contest capability directly, who prevails is decided by a contest success function $w_i=\sigma_i^{\,r}/\sum_j\sigma_j^{\,r}$, with effective strength $\sigma_i$ and decisiveness $r>0$, for a prize $\Omega$. A unit of contest intensity costs $c$ privately and imposes an expected loss $\ell$ on every actor through the host. The case for racing rests on a premise with three parts:
- **(P1) decisive**: $r$ is large;
- **(P2) fast**: capability grows quickly, so that leads open within short windows;
- **(P3) non-saturating**: no level of advantage makes more advantage worthless.

These are three separate dimensions. A technology can be decisive at a threshold and saturate above it, as nuclear advantage saturated at a secure second strike. P2 also does not imply sustained compounding: with strength $1+1000t$ against $1$ and $r=10$, the leader's chance of winning is about $0.999$ at $t=0.001$, while its capability grows only linearly.

Reduce each actor's choice to racing or restraint, with payoffs in a stated measure: $R_i$ when all restrain; $T_i$ when it races against restrainers; $P_i$ when all race; $S_i$ when it restrains while a rival races.

**Proposition 5.1 (Join or eliminate, and what it rests on) [T].**
1. *In the objective an actor acts on, if $S_i^O<P_i^O$, restraint is never a best response to a racing rival. In the contest of Proposition 4.2 this holds whenever racing is a strict best response to racing, which is the case for $r<n/(n-1)$. In the $n$-player game it also needs restraint against one racer to pay less than racing alongside it.*
2. *A best response in the objective does not imply $S<P$ in material payoff or true welfare. With $n=2$, $r=1$, $\Omega=c=1$, $\ell=0.1$ and $\theta=-1$, racing is the strict best response in the objective. Yet staying out gives $S^\pi=-0.05$ against $P^\pi=-0.10$, and with $\kappa=0.2$, $S^W=+0.04$ against $P^W=-0.12$.*
3. *Let falling behind cost $L_b\ge0$ on top of losing the prize. At $\theta=0$, joining instead of staying out gains $\frac{\Omega+L_b}{n}\big(1-\frac{r(n-1)}{n}\big)$ for $r\le n/(n-1)$. In the fully dissipative limit (two actors with $r\ge2$, or the all-pay contest) the gain is zero. This is an equality in expectation for symmetric, risk-neutral actors; with asymmetric costs $c_1<c_2$ the strongest keeps a rent $(\Omega+L_b)(1-c_1/c_2)$ (Hillman and Riley 1989; Baye, Kovenock and de Vries 1996).*
4. *The race begins if any single actor has $T_i>R_i$. If these events are independent with probabilities $\xi_i$, it begins with probability $1-\prod_i(1-\xi_i)$, which tends to one as capable actors multiply, provided $\sum_i\xi_i$ diverges.*

The race is set by the most race-inclined actor, not the average one. That is why any remedy must cover every capable actor.

**Proposition 5.2 (Dissipation) [T].** *At $\theta=0$ each actor's loss relative to joint restraint is $\Delta=\frac{r(n-1)}{n}\cdot\frac\Omega n\cdot\frac{c+n\ell}{c+\ell}$. It increases with $r$ and $\ell$, and exceeds $\Omega/n$, so that every actor would be better off if the prize did not exist, iff $r(n-1)(c+n\ell)>n(c+\ell)$. Beyond $r=n/(n-1)$ there is no symmetric pure equilibrium, and the active set narrows.* For $n=4$, $r=1$ and $\ell=0.3c$, $\Delta=1.27\,\Omega/n$ [N].

The more decisive the advantage, the more of its value is consumed in the race to obtain it. What is spent is safety margin, accepted risk and delegated control.

### 5.2 Delegation

Each actor chooses whether to delegate consequential decisions in the contest to AI systems without human review: $\iota_i\in\{0,1\}$.
- Strength is $\sigma_i=1+s\,\iota_i$, where $s$ is the advantage of AI-paced over human-paced decision; if AI is an instrument of the contest, $s$ grows over time.
- Defeat costs $L_e$.
- Loss of control by any actor costs every actor $L_c$.
- The per-period hazard of losing control is $\psi_0$ without delegation and $\psi_1>\psi_0$ with it; write $\Delta\psi=\psi_1-\psi_0$.

In additive stakes, $u_i=-L_e(1-w_i)-L_c[1-\prod_j(1-\psi_j)]$.

**Proposition 5.3 (Delegation in additive stakes) [T].**
1. *If $k$ others delegate, delegating gains $L_e[w_i(1,k)-w_i(0,k)]$, increasing in $s$ and tending to $L_e(1-1/n)$ for $k=0$ and to $L_e/(k+1)$ for $k\ge1$. It costs $L_c\Delta\psi(1-\psi_0)^{n-1-k}(1-\psi_1)^k$, which falls in $k$.*
2. *Delegation becomes strictly dominant as $s$ grows iff $L_e\,g_\infty(k)>L_c\Delta\psi(1-\psi_0)^{n-1-k}(1-\psi_1)^k$ for every $k$, with $g_\infty(0)=1-1/n$ and $g_\infty(k\ge1)=1/(k+1)$. $L_e/n>L_c\Delta\psi$ is sufficient. When the control loss dominates, delegation is never chosen: with $n=3$, $L_e=1$, $L_c=100$ and $\psi_1=0.2$, the cost is at least $12.16$ against a gain below $1$.*
3. *Universal delegation is worse for every actor than none, by $L_c[(1-\psi_0)^n-(1-\psi_1)^n]$.*
4. *Under relative objectives the shared loss cancels from the objective, and delegation is chosen at every $s>0$.*

For $n=3$, $r=1$, $L_e=L_c$, $\psi_0=0.01$ and $\psi_1=0.2$, the dominance threshold is $s^\ast\approx1.16$, at which a lone delegator's chance of winning is about $0.52$ [N]. Delegation pressure arrives well below decisive capability.

**Lemma 5.4 (Capacity lock-in) [T].** *Let human capacity $\mathcal K$ to take the delegated decisions decay as $\dot{\mathcal K}=-\delta_c\mathcal K$ under delegation and recover as $\dot{\mathcal K}=\beta_c(\bar{\mathcal K}-\mathcal K)$ otherwise, and let safe operation without AI require $\mathcal K\ge\mathcal K_{\min}$. After $T_{\text{lock}}=\ln(\mathcal K_0/\mathcal K_{\min})/\delta_c$ of delegation, an actor that reverts must operate below $\mathcal K_{\min}$ for $T_{\text{rec}}=\beta_c^{-1}\ln[(\bar{\mathcal K}-\mathcal K)/(\bar{\mathcal K}-\mathcal K_{\min})]$. Maintaining $\mathcal K\ge\mathcal K_{\min}$ in parallel during delegation removes the lock; in a contest it costs strength.*

The additive payoff is not a survival probability. Let the lock have a survival meaning: with probability $q_L$, locked delegation ends the delegator's ability to overrule the decisions taken in its name (O2 for that actor). Let losing the contest mean subordination with probability $p$, and let $Q=\prod_j(1-\psi_j)$. With $r=1$,
$$\Phi_i=(1-q_L\iota_i)\,Q\,[w_i+(1-w_i)(1-p)].$$

**Proposition 5.5 (Delegation when the lock counts) [T].**
1. *If $q_L=1$ and $Q>0$, then for every finite $s$, every $n$, every $p\in[0,1]$ and every profile of the others, not delegating gives strictly higher survival than delegating. Not delegating is strictly dominant, and no one delegating is the unique equilibrium.*
2. *Let $k$ others delegate, $p=1$ and $a=(1-\psi_1)/(1-\psi_0)$. Then $\Phi_D/\Phi_N=(1-q_L)\,a\,(1+s)\,\dfrac{n+ks}{n+(k+1)s}$. If $q_L<1$, write $A=(1-q_L)a$. All delegating is an equilibrium iff $A\,(n+(n-1)s)/n\ge1$, and no one delegating is an equilibrium iff $A\,n(1+s)/(n+s)\le1$. Both, one or neither can hold, depending on $s$. With $n=2$, $q_L=0.99$, $\psi_0=0.01$ and $\psi_1=0.05$, all delegating is an equilibrium only for $s\ge206.4$, and each actor's survival there is $0.0045$ whatever $s$ is [N].*
3. *At bounded speed one delegator does not drive the others' survival to zero. With $p=1$, an actor that does not delegate while $k$ others do has survival $Q_N/(n+ks)>0$. With $n=2$, $s=1$, $p=q_L=1$, $\psi_0=0$ and $\psi_1=0.01$, it is $0.33$ [N]. It tends to zero only as $s\to\infty$: a limit in speed, not in time.*

Part (1) holds for all 20,000 random parameter draws in `checks_v5.py` [N]. It is a strong conditional result. It needs the lock to end the delegator's standing for certain ($q_L=1$), and Lemma 5.6 states what that requires.

Part (1) shows that keeping AI out of strategic decision loops whose delegation would lock is a strict equilibrium among actors who price in the lock. It needs no trust among them. This is the narrow form of E1 (Section 8.3). It does not show:
- that broader uses of AI, in labour, finance or persuasion, have the same structure; that needs its own action space;
- that one actor's delegation sends every other actor's survival to zero over time. That needs a dynamic model in which continued delegation sustains a nonsummable shared conditional hazard (Lemma 4.4), and a background hazard present for everyone would end the long-run survival of non-delegators too.

The survival form without the lock ($q_L=0$) describes actors who believe that "our aligned AI is us". The race is sustained partly by that belief.

**Lemma 5.6 (Delegation and the selection of decisions) [T].** *Suppose that, after $T_{\text{lock}}$, an actor's consequential decisions in the contest are taken by systems retained for their performance in it. Assume:*
- *(a) the admissible variants include systems whose decisions do not act on terms common to all actors;*
- *(b) acting on a common term changes a decision toward restraint, and lowers relative performance by at least $\nu>0$ net of any enforcement and reliability benefits;*
- *(c) retention is cumulative, in the sense of C1 of Theorem 3.13;*
- *(d) the retained systems hold actual authority over the decisions.*

*Then the share of retained decisions that act on common terms tends to zero.*

*If instead a constraint on common terms is an admission condition for every eligible system and is enforced, (a) fails: relative competition takes place inside the constraint, and the conclusion does not follow.*

The definitional step is separate. An actor that can no longer overrule decisions taken in its name has lost O2 in that domain; that is a definition, not a derivation.

For a reader who counts survival only as the preservation of the unit, delegation acts through the shared hazard instead. Delegated systems that are blind to common terms, and that interact at machine speed without a human veto, raise the probability of shared loss: reciprocal fear of surprise attack (Schelling 1960, ch. 9), inadvertent escalation (Posen 1991), flash war (Scharre 2018), and gradual disempowerment (Kulveit et al. 2025). This is an argument with cited mechanisms, not a derivation.

The exception in Lemma 5.6 is a design lever. Shared safety constraints enforced as conditions of admission for all eligible systems block the selection of decisions blind to common terms. Whether such enforcement survives is the subject of Section 3.

### 5.3 Correction against the clock

**Proposition 5.7 (The tempo bound) [T].** *Consider a hazard mode $\dot y=ay+u(t-\tau_c)$ growing at rate $a$, corrected with delay $\tau_c$.*
1. *Correction proportional to the observed deviation cannot stabilize the mode when $a\tau_c\ge1$, whatever its gain (Hayes 1950).*
2. *Derivative action extends the range: for $a=1$ and $\tau_c=1.5$, gains $k_p=1.02$, $k_d=0.644$ stabilize the mode [N]. The bound in (1) belongs to proportional correction, not to all correction.*
3. *Every linear time-invariant correction that stabilizes the mode has peak complementary sensitivity at least $e^{a\tau_c}$, by the maximum modulus principle. Robust stability against multiplicative model error weighted by $w$ requires $\|w\mathcal T\|_\infty<1$, which implies the necessary condition $|w(a)|e^{a\tau_c}<1$. The single-point condition is necessary, not sufficient: the stable weight $w(s)=2(s-a)/(s+a)$ has $w(a)=0$ but $|w|=2$ on the imaginary axis, so $\|w\mathcal T\|_\infty\ge2e^{a\tau_c}>1$ [N].*
4. *For hazard classes whose evidence arrives only after a manifestation window $m_e$ that no testing shortens, $\tau_c\ge m_e$ whatever is done with the evidence once it arrives.*

When the situation changes faster than correction can follow, correction first loses robustness, then fails. For classes with an irreducible lag, only slowing helps. Where technical means lower $a$ without slowing the contest, they help.

### 5.4 Coverage, hazard and correction

The step from capability to irreversible loss passes through three quantities, kept apart here:
- the variety $Y_t$ of hazardous behaviour in a defined hazard class;
- the coverage $U_t$ of that behaviour by correction that remains contestable;
- the residual probability of an irreversible loss after the correction in place.

Four premises connect them on a continuation branch. They are premises, not results; Section 9 treats them as the central cruxes.

- **(X) Hazardous variety grows with capability [A].** On the continuation branch, capability compounds (X1). The variety of hazardous behaviour in the class grows with it, at least exponentially on that branch (X2).
  - Evidence: capability compounds [O: E5]. Dangerous capabilities arrive as by-products of general capability, new threat models appear, and automated research compounds.
  - The step from capability to hazardous variety is not measured. Benchmarks of general capability do not measure it.
- **(U) Contestable coverage falls behind [A].** Let $U_t$ be the volume of correction decisions that meet four conditions:
  - (C1) *legible*: there is a reason that people can check within a budget, without relying on the outputs of the evaluated system or its lineage, except through tools whose reliability was established earlier within $U$;
  - (C2) *overrulable*: a designated human body can reverse the decision within a stated time;
  - (C3) *exercised*: planted errors are caught at a stated rate, and human overrule is not zero;
  - (C4) *with capacity*: human review covers a stated share of consequential decisions.

  The premise is that $U_t/Y_t\to0$ on the continuation branch, uniformly: for each $\varepsilon>0$ there is a deterministic $T_\varepsilon$ after which $U_t/Y_t\le\varepsilon$ on all surviving histories. It has four grounds:
  - consequences take their time, and tools raise the throughput of observation without making consequences arrive sooner (Proposition 5.7(4));
  - institutions deliberate and respond at rates set by human attention and procedure;
  - learning new theoretical models, diffusing a consensus and forming new mechanisms are human processes that do not keep pace with exponential growth;
  - where contestable understanding is produced with human time, $\dot U=A_UL_U^{\lambda_U}U^{\phi_U}$ with $\phi_U<1$ and $L_U$ bounded gives polynomial growth (Jones 1995; Bloom, Jones, Van Reenen and Webb 2020).

  None of these grounds settles the premise. If AI tools raise the productivity $A_U$ exponentially, $U$ grows exponentially too, at rate $\kappa_U/(1-\phi_U)$ when $A_U\propto e^{\kappa_Ut}$. Whether AI raises contestable coverage as fast as it raises hazardous variety is symmetric with the question of whether AI cheapens independent correction as fast as it cheapens control (Proposition 3.6(4)). It is a crux, and it is measurable: at fixed human hours, does the catch rate of planted defects fall as capability rises?
- **(φ) A floor on residual risk [A].** On every surviving history, the conditional probability of the irreversible event in the next period, after the correction architecture in place, is at least $h\,(1-U_t/Y_t)^+$ for some $h\in(0,1)$.
  - This is the AI-risk premise. It concerns residual risk after correction, so a correction architecture that actually lowers residual risk refutes it on that branch (Proposition 5.10).
  - It is not derived from the contest. Risk compensation does not establish it (Proposition 5.13).
- **(φ-s) Shared failure [A].** Irreversible failure that starts with one actor reaches others, through the shared host or through loss of control that spreads. Results about the survival of an actor that stays out need it.

**Theorem 5.8 (Coverage mismatch on a continuation branch) [T].** *Under (X), (U) with its uniformity, and (φ): for every $\varepsilon\in(0,1)$ and $H>T_\varepsilon$,*
$$\Pr(S_H)\le\big(1-h(1-\varepsilon)\big)^{H-T_\varepsilon}\longrightarrow0.$$
*Conversely, if on every surviving history the residual probability is at most $\bar h\,\mathsf u_t$ with $\bar h<1$ and $\sum_t\mathsf u_t<\infty$, where $\mathsf u_t=(1-U_t/Y_t)^+$, survival stays bounded away from zero.*

With $h=0.05$ and $\varepsilon=0.1$, survival eighty periods after $T_\varepsilon$ is at most $0.025$ [N]. Four remarks fix the scope.
- The limit needs only a persistent positive uncovered share; (U) governs how soon the bound bites.
- (φ) gives $\liminf$ of the hazard at least $h$. It does not say the hazard tends to $h$; the actual hazard can be larger.
- Summability does not require that coverage ever catch up. With $\mathsf u_t=1/(t+2)^2$, coverage stays slightly behind forever, and survival with $h=0.05$ stays above $0.98$ [N].
- The theorem concerns a continuation branch with sustained growth. Finite sprints, saturation, freezing and rollback change the premises and are treated next.

**Proposition 5.9 (Freezing and rolling back after a sprint) [T].** *Let hazardous variety be frozen at $Y_\tau$ from time $\tau$, while coverage $U$ keeps growing.*
1. *The exposure after $\tau$ is $\int_\tau^\infty(1-U(t)/Y_\tau)^+\,dt$. For linear coverage with slope $\dot U$ it is $Y_\tau(1-U(\tau)/Y_\tau)^2/(2\dot U)$ when $U(\tau)<Y_\tau$, and zero otherwise. For coverage growing exponentially at rate $g_U$, with $\Gamma=Y_\tau/U(\tau)>1$, it is $(\ln\Gamma-1+1/\Gamma)/g_U$.*
2. *Rolled back to $Y\le U$, the exposure stops.*
3. *If a sprint builds capability $\Gamma_X$ times the rivals' level and hazardous variety is a fraction $\varphi$ of capability's variety, the frozen exposure is zero when $\varphi\Gamma_X\le1$. With $\varphi=0.5$, it is zero at $\Gamma_X=2$ and positive at $\Gamma_X=4$ [N].*
4. *For linear coverage, $\dot U/U\to0$, so the same frozen ratio costs more the later the sprint. This does not hold for every sub-exponential $U$: coverage can grow in bursts, with proportional growth $0.5$ inside infinitely many late windows, while $\log U(t)/t\to0$ [N].*

Taking hazardous variety equal to capability's variety, with $g=0.3$, linear coverage $1+0.5t$ and $h=0.05$, a sprint to $\tau=10$ leaves survival $0.86$; freezing then gives $0.53$, and rolling back keeps $0.86$ [N]. A winner that freezes or rolls back keeps positive survival. What it gives up is permanent superiority, which is not the same thing (Section 6.5).

**Proposition 5.10 (Correction that people cannot understand) [T].** *Let a correction architecture act on hazardous behaviour beyond $U$. Per period, let it block a share $c_b$ of the failures that would otherwise occur, with base hazard $q_0$, and add a residual hazard $q_c$ of its own, including its own irreversible failures. The residual hazard is $q=q_0(1-c_b)+q_c$, and the architecture lowers residual risk iff $q_0c_b>q_c$.*

A corrector that cannot be understood can still lower risk, even to a summable sequence. With base hazard $0.1$ a period, a corrector that blocks $99\%$ and adds $2^{-(t+2)}$ raises survival to period $200$ from $7\times10^{-10}$ to $0.63$ [N]. To show that such correction fails, one must show that its own residual hazard set and conditional risk satisfy the lower bounds of (X) and (φ). Calling it uncovered is not enough.

Such a corrector does not meet C1–C4: no one can answer for its decisions. That is a failure of contestability (V3), a separate question from physical safety. A technically safe controller that no one can answer to is still a loss of O2 in its domain. Conversely, a formal safety guarantee does not establish accountability.

Under the contest, three further pressures act on such correction, each with its own conditions:
- systems are retained for their performance in the contest (Lemma 5.6);
- limits on permissions cost strength and are competed away unless they are enforced as conditions of admission;
- safety gains are partly absorbed by delegation (Proposition 5.13).

**Proposition 5.11 (Oversight topology) [T].** *Let human attention $\mathsf B$ cover hazardous variety $Y$ through layers that each amplify the layer above by $\mathsf m>1$, so that $k=\ln(Y/\mathsf B)/\ln\mathsf m$ layers are needed.*
1. *Serial chain. If a problem at the bottom is caught only when every layer passes it up, and each link does so with conditional reliability $\mathsf f$ given the earlier links succeeded, the chain catches it with probability $\mathsf f^k=(Y/\mathsf B)^{\ln\mathsf f/\ln\mathsf m}$, which falls as $Y/\mathsf B$ grows.*
2. *Redundant checks. If each of $k$ checks has direct authority to stop the problem and they fail independently, the probability that at least one catches it is $1-(1-\mathsf f)^k$. If a common cause defeats all of them with probability $\rho$, it is at most $1-\rho$.*

With $\mathsf f=0.9$ and $k=6$, a serial chain catches $0.53$ and redundant independent checks $0.999999$; a common cause with $\rho=0.05$ caps the latter at $0.95$ [N]. Scalable oversight can succeed or fail depending on its topology. The ceiling on redundancy is the independence of the checks: shared training sources, shared models and shared funders are common causes. Section 3 shows that selection produces exactly these, through the lineage share $x_{\mathsf E}$. So the reliability of redundant oversight is governed by the same certificate as the independence of evaluators: full row sums below one (Proposition 3.10).

**Remark 5.12 (Prediction and certification).** In a system whose largest Lyapunov exponent is $\lambda_L>0$, an initial error $\delta_{\text{obs}}$ grows to a tolerance $\Delta_{\text{tol}}$ after about $\lambda_L^{-1}\ln(\Delta_{\text{tol}}/\delta_{\text{obs}})$. A $k$-fold gain in observational precision extends the horizon of prediction by $\lambda_L^{-1}\ln k$. In the logistic map at full chaos, errors of $10^{-3}$ and $10^{-12}$ reach $0.1$ after $7.5$ and $37.5$ steps on average [N].
- This limits safety cases that depend on predicting trajectories. "The margin we have bought will suffice" is such a case (Section 6.3).
- It does not exclude certifying invariants, bounds on reachable sets, or probabilistic risk bounds, which need no trajectory prediction (Dalrymple et al. 2024).
- What limits such certification is how much of the hazardous behaviour a specification covers, and how adequate the world model is. Both are open questions for general AI.
- That AI raises the sensitivity of the systems it acts in is a conjecture, not a result.

### 5.5 What happens to safety gains inside the contest

**Proposition 5.13 (Risk homeostasis) [T].** *In Proposition 5.3's model with additive stakes and $r=1$, let each actor choose a degree of delegation $\iota_i\in[0,1]$, with strength $1+s\iota_i$ and hazard $\psi_0+\Delta\psi\,\iota_i$. Write $x=\Delta\psi\,\iota$, $b=\Delta\psi/s$, $q=1-\psi_0$ and $K=(n-1)L_e/(n^2L_c)$. An interior symmetric equilibrium solves*
$$(x+b)(q-x)^{n-1}=K.$$
1. *On a branch where $x$ is small relative to $q$, the hazard that delegation adds is $nx\approx(n-1)L_e/(nL_cq^{n-1})-n\Delta\psi/s$, nearly independent of $\Delta\psi$. Improvements in the safety of delegation are absorbed by more delegation until delegation saturates ($\iota=1$).*
2. *There can be several interior equilibria. Along an interior branch, $\partial x/\partial\Delta\psi=-(q-x)/\big(s[q-nx-(n-1)b]\big)$, whose sign changes between branches. With $n=2$, $s=100$, $L_e=0.5$, $L_c=1$, $\psi_0=0.01$ and $\Delta\psi=0.9$, there are interior equilibria at $\iota=0.153$ and $\iota=0.937$, and full delegation is also an equilibrium. On the high branch the total risk falls slightly as $\Delta\psi$ falls [N].*
3. *After saturation, realized risk falls with $\Delta\psi$, and can be summable even under full delegation and growing speed. With $n=3$, $L_e=L_c=1$, $\psi_0=0$, $s_t=2^t$ and $\Delta\psi_t=2^{-t}$, full delegation is an equilibrium at every $t\ge5$, and the total realized risk from $t=5$ on is at most $3/16$ [N].*
4. *With all-or-nothing delegation, any equilibrium with $k\ge1$ delegators has realized hazard $1-(1-\psi_0)^{n-k}(1-\psi_0-\Delta\psi)^k$ above the baseline $1-(1-\psi_0)^n$. An improvement that carries $\Delta\psi$ across the threshold at which delegation becomes an equilibrium raises realized hazard.*

With $n=3$, $s=100$, $L_e=1$, $L_c=100$ and $\psi_0=0.01$, the added hazard is $0.0011$, $0.0053$, $0.0062$, $0.0065$ and $0.0067$ as $\Delta\psi$ falls from $0.19$ to $0.005$. It falls to $0.0030$ only when delegation is complete, and it doubles when $L_e/L_c$ doubles [N].

Inside the contest, on a stable interior branch away from boundaries and folds, safety gains are largely absorbed by more delegation. The equilibrium risk there is set by the stakes of winning relative to the loss, $L_e/L_c$. Stafford, Trager and Dafoe (2022) found the corresponding attenuation for risky technologies in races (compare Peltzman 1975; Wilde 1982).

Three limits apply.
- The result does not establish a permanent floor on residual risk; part (3) is a counterexample. (φ) stays an independent premise.
- The levers are several: the value of winning relative to the loss, liability and internalization, the baseline hazard $\psi_0$, and the set of actions available.
- For actors who price in the lock, nobody delegates first (Proposition 5.5). Homeostasis concerns actors who do not.

### 5.6 Comparing branches in survival terms

Survival is computed in one discrete convention: per-period conditional probabilities over a common horizon $H$. Let $h_R$ be the per-period hazard under an arrangement of restraint, $q_{\mathrm I}$ the loss of the ability to overrule by delegation, $q_{\mathrm{II}}$ the shared hazard, and $q_W$ the hazard of preventive attack. Let $p_{\text{dec}}$ be the probability that a racer's advantage becomes decisive when all race, and $p^S_{\text{dec}}$ the same when the actor stays out. Let $p_{L4}$ be the actor's belief that a decisive winner would extend its dominance over it. This is a belief, not a quantity that survival-first preference sets to one. With independence for the formulas,
$$\Phi^R=1-h_R,\quad \Phi^T=(1-q_{\mathrm I})(1-q^T_{\mathrm{II}})(1-q_W),$$
$$\Phi^P=(1-q_{\mathrm I})(1-q^P_{\mathrm{II}})(1-q_W)\Big(1-p_{\text{dec}}\tfrac{n-1}{n}\Big),\quad \Phi^S=(1-q^S_{\mathrm{II}})(1-p^S_{\text{dec}}p_{L4}).$$

**Proposition 5.14 (Assurance in survival terms at a common horizon) [T].**
1. *The advantage of cooperating is $\varpi(\Phi^R-\Phi^T)+(1-\varpi)(\Phi^S-\Phi^P)$, where $\varpi$ is trust. If both terms are non-negative, cooperation is dominant. If only the first is positive, the game is a stag hunt with threshold $(\Phi^P-\Phi^S)/((\Phi^R-\Phi^T)+(\Phi^P-\Phi^S))$. If only the second is, it is chicken; if neither, a prisoner's dilemma.*
2. *In the region $\Phi^S\ge\Phi^P$, $\Phi^R\ge\Phi^T$, an actor that holds the prediction restrains whatever it believes about the others.*
3. *Mutual racing remains a strict equilibrium at every finite horizon with $\Phi^P_H>\Phi^S_H$.*
4. *For constant per-period hazards $q_B$ on a branch and $q_R$ under the arrangement, $\Phi^B(H)/\Phi^R(H)=\big((1-q_B)/(1-q_R)\big)^H$, which decays at rate $\log((1-q_R)/(1-q_B))$. With $q_B=0.05$ and $q_R=0.005$ the rate is $0.0463$, not $0.045$ [N].*
5. *Mixed beliefs. If an actor gives the premises of Section 5.4 probability $p_{\text{prem}}$, and the branches of the race have survival $T_\neg,P_\neg,S_\neg$ when they fail, the stag-hunt classification at horizon $H$ needs $\Phi^R(H)-\big(p_{\text{prem}}\Phi^T_H+(1-p_{\text{prem}})T_\neg\big)>0$ and the corresponding sign on the second term. When the arrangement's own survival $\Phi^R(H)$ also decays, these signs can fail at long horizons. With $p_{\text{prem}}=0.99$, $\Phi^R=e^{-0.005H}$, race branches decaying at rate $0.05$ when the premises hold, and $(T_\neg,P_\neg,S_\neg)=(0.9,0.4,0.1)$, the arrangement's survival exceeds the mixed survival of racing alone at $H=10$, $100$ and $600$; at $H=1{,}000$ it does not, and racing becomes dominant [N].*

Numbers for $n=2$ with $p_{L4}=1$, at a horizon where the hazards are as stated [N]:
- With $q_{\mathrm I}=0.6$, $q^T_{\mathrm{II}}=q^S_{\mathrm{II}}=0.3$, $q^P_{\mathrm{II}}=0.4$, $q_W=0.2$, $p_{\text{dec}}=p^S_{\text{dec}}=0.6$ and $h_R=0.1$: $\Phi^R=0.90$, $\Phi^T=0.22$, $\Phi^P=0.13$ and $\Phi^S=0.28$. Cooperation is dominant.
- If staying out raises the racer's decisive chance to $0.8$, $\Phi^S=0.14$, still above $\Phi^P$, because joining raised the shared hazard.
- With low delegation ($q_{\mathrm I}=0.05$, shared hazard $0.1$, $q_W=0.1$, $p_{\text{dec}}=0.3$), the game is a stag hunt with threshold $0.16$.
- For a leader that wins with probability $0.8$ if it races, and whose exit hands decisive advantage to the rival ($q_{\mathrm I}=0.2$, $q_W=0.2$, $p_{\text{dec}}=0.9$, $p^S_{\text{dec}}=0.95$, $h_R=0.1$), it is a stag hunt with threshold $0.42$ when the shared hazard is $0.3$, falling to $0.11$ when it is $0.8$. For the leader, the shared hazard carries the argument.

The comparison is therefore made at common finite horizons, not at $H=\infty$, where both branches of a hazardous world can tend to zero and a first-order ranking by $\Phi(\infty)$ ties them. A survival-first actor uses finite-horizon dominance: one path is preferred if it gives higher survival at every horizon in the range that matters. That is the form of standard D.

**Discounting.** Under a discounted objective, with constant race hazard $h$, race growth $g_r$ and paced growth $g_p$, a race is preferred iff $h<g_r-g_p$, even though it ends in catastrophe with certainty (Jones 2024; Fudenberg and Koh 2026) [N]. A rising hazard reverses the preference only if it comes to exceed the growth differential. If the hazard is capped at $0.05$ and the growth gap stays at $0.10$, no reversal occurs. Standard D does not discount the protected outcomes, by choice (V2).

### 5.7 What the analysis of Section 5 establishes

**Theorem 5.15 (Classification of contest branches) [T].** *Let AI be an instrument of the contest.*
- *Branch I, decisive and fast (P1, P2, P3).*
  - *(a) Unilateral restraint is not a best response in the objective when $S^O<P^O$. In material terms, for symmetric risk-neutral actors in the fully dissipative limit, joining buys nothing over staying out (Proposition 5.1).*
  - *(b) Racing dissipates the prize (Proposition 5.2).*
  - *(c) In additive stakes, delegation becomes dominant as speed grows under the exact condition of Proposition 5.3, and under relative objectives at any speed. For actors who price in a certain lock, it is never chosen (Proposition 5.5).*
  - *(d) Modes beyond the robust reach of correction fail unless slowed (Proposition 5.7).*
  - *(e) A decisive shift gives a rational motive for preventive attack when future promises are incredible (Proposition 6.4).*
- *Branch I′, decisive but saturating (P3 fails). The contest has an object up to the saturating level and none beyond it. Additional advantage is worthless, and the contest can stabilize as nuclear deterrence did, while hazards in development remain.*
- *Branch II, decisive but slow. The time at which delegation becomes dominant recedes. Modes stay within proportional correction while $a\tau_c<1$. A shift spread over enough periods does not make preventive attack rational: with $w$ falling from $0.5$ to $0$ over $N$ periods, $c_A=0.05$ and $\delta=0.8$, attack is rational at the start for $N\le3$ and never for $N\ge4$ [N]. Correction and bargaining can work here.*
- *Branch III, not decisive. Equilibrium intensity, dissipation and shared loss are proportional to $r$. What vanishes is the object of the race, not every incentive to compete.*

What the analysis establishes, and what it does not:

| Outcome | Horizon | Branch | Result | Conditions |
|---|---|---|---|---|
| O1 or O2, everyone | Long | Continuation with sustained compounding | Survival tends to zero (Theorem 5.8) | (X), (U) with uniformity, (φ), and (φ-s) for those who stay out. These are cruxes, not facts |
| O2 for the delegator | One contest | Strategic delegation that locks | Strictly worse than not delegating (Proposition 5.5(1)) | $q_L=1$, finite speed |
| O1 or O2 | Finite | Finite sprint | Exposure grows with the hazardous ratio built and with the date, for linear coverage (Proposition 5.9) | Hazardous variety, not capability, is what counts |
| Collective welfare | Stage game | Faithful AI, relative objectives | Collectively inferior equilibrium (Proposition 4.1) | $\epsilon(b-d)>c$ |
| Safety gains | Equilibrium | Interior branch of delegation | Largely absorbed (Proposition 5.13) | Away from boundaries, folds and saturation |

It does **not** establish the following:
- that every path through a race ends at zero survival;
- that one actor's delegation drives every other actor's survival to zero;
- that risk compensation puts a permanent floor on residual risk;
- that correction people cannot understand cannot lower risk;
- that a winner which stops keeps nothing.

These were claimed in earlier versions of the theory. They do not follow from the models, and the situated argument does not need them. It needs the comparison of Section 6.

---

## 6. The strongest case for continuing

Each alternative is given its best case, how it would be installed, what risk remains, and what evidence would show it suffices. Each is classified by Definition 1.6: does it leave the winning model governing, retaining W and the conversion of success into influence over rules (C) (continuation), or change one of the four elements (pivot)? An alternative that succeeds only by changing them supports the pivot. Section 6.8 then applies one set of durability tests to every arrangement, including the cooperative design of Section 7.

### 6.1 Technical alignment and AI-assisted correction

**Best case.** Alignment of each system to its principal improves. Control protocols prevent catastrophic actions by models that may be misaligned, tested against red teams (Greenblatt, Shlegeris, Sachan and Roger 2024). Interpretability finds hidden objectives (Marks et al. 2025). Oversight is built redundantly, so that independent checks with direct authority catch almost everything (Proposition 5.11(2)). Formal methods certify invariants without predicting trajectories (Remark 5.12). AI cheapens independent correction as fast as it cheapens control, so the certificate of evaluation holds without budget growth (Proposition 3.6(4)). Correction that people cannot follow still lowers residual risk (Proposition 5.10).

**What remains.**
- Principal alignment does not change the game among principals (Proposition 4.1); it makes each principal's chosen game more effective.
- Under the contest, systems are retained for performance (Lemma 5.6), and on interior branches safety gains are absorbed by more delegation (Proposition 5.13).
- Redundant oversight is capped by common causes: shared training sources, shared models and shared funders. Section 3 shows that these are what selection produces.
- AI-assisted correction is only as independent as its funding, access and appointment (Proposition 3.10).

**Classification.** A component, compatible with either path. It becomes part of a pivot when held by correctors whose funding, access and appointment are separated from competitive success (changing C).

**What would show it suffices on the present path.** At fixed human hours, catch rates of planted defects do not fall as capability rises. Independent evaluators keep certificates of independence while depending on the evaluated for access. Measured residual risk per hazard class falls over generations.

### 6.2 Regulated competitive provision with strong correction

**Best case.** Competition in products and services continues. Liability and licensing make consequences return (Theorem 7.2), evaluation access is mandated, and thresholds are fixed in advance. When the effective hazard is high and capability is transparent, pacing can be the unique equilibrium of a capability race without any agreement (Fudenberg and Koh 2026). This is the bounded competition that a cooperative order can contain (V5).

**Installation.**
- Each jurisdiction regulates its own developers.
- Coverage must reach every capable actor, since one actor can start the race (Proposition 5.1(4)).
- The rule-makers are themselves in a contest of standing, so no one of them imposes the liability alone (Proposition 7.3).
- Rule-making is subject to the selection of Section 3.

**What remains.**
- Liability cannot exceed the assets of the liable for catastrophic harm.
- Regulation in one market leaves load elsewhere.
- Written safety commitments are already set relative to rivals, and are revised mostly toward weakening (E2).
- Public evaluation bodies have shifted their mandates toward industry contact, under voluntary access (E3).
- The pacing equilibrium has no delegation channel and assumes transparency. Proposition 5.5 and Section 3.5 are where the present path departs from those conditions.

**Classification.** Depends on scope. Pacing that binds every capable actor to correction capacity, with evaluators separated from success, changes the tempo of W and the conversion of C: it is a pivot under another name. National competitive provision that keeps relative advantage as the objective is continuation.

**What would show it suffices on the present path.** Durable restraint despite competitive pressure: competitor clauses not invoked, thresholds held when rivals advance, mandates of evaluation bodies widening rather than narrowing.

### 6.3 Leadership and a safety margin

**Best case.** A leader spends part of its lead on safety: it slows, evaluates and hardens before the follower catches up. A large lead can discourage the follower (Harris and Vickers 1987; Konrad and Kovenock 2009). A laggard far behind under moderate hostility does not gamble on risky technology (Stafford, Trager and Dafoe 2022). Where the shared hazard is significant, a leader that commits to slow can lead rivals to slow too (Bueno de Mesquita, Dziuda and Polborn 2026).

**Remark 6.1 (What a lead buys) [T, N].**
1. *A lead shrinks even when the follower does not accelerate, through diffusion, distillation and theft. With diffusion at rate $\delta_f$, a lead $\Delta_0$ held by a leader that pauses lasts $T_p=\delta_f^{-1}\ln(1+\delta_f\Delta_0)<\Delta_0$. A six-month lead diffusing at $0.1$ a month lasts $4.7$ months; a two-year lead about a year. Spending a lead returns the contest toward parity, where intensity is greatest (Propositions 4.2 and 5.2).*
2. *The margin is time, but what it must buy is coverage. During a lead of length $\Delta$, coverage rises by about $\dot U\Delta$, while the uncovered variety grows on a continuation branch (Section 5.4). For hazard classes whose evidence lag exceeds $\Delta$, it buys nothing (Proposition 5.7(4)).*
3. *Whether the margin suffices is judged inside the contest. The leader's own evaluators produce the evidence under time pressure, subject to masking (Section 3.5). The judgment rests on predicting a system that cannot be predicted far enough to certify it (Remark 5.12).*
4. *How the follower responds depends on the structure of the contest. In a static contest with an asymmetric favourite, the follower raises effort when the leader slows (Dixit 1987). In dynamic races a large lead discourages it. A leader that sees its window closing has, in turn, a motive to strike first (Copeland 2000; Van Evera 1999).*

On their own median estimates, the planners of one detailed scenario judge that a leader spending part of its lead buys about a third of the reduction in takeover risk that a coordinated slowdown buys, both relative to racing [O: E10].

**Classification.** Continuation; it keeps W. Its best case, a leader slowing and inducing rivals to slow, is a step toward reciprocal restraint, which is the first stage of a pivot (Section 8.4).

**What would show it suffices.** Leads that are not spent on speed; evidence that rivals slow in response; margins long relative to the hazard classes' evidence lags.

### 6.4 The benign winner

**Best case.** The right side wins and restrains itself. An encompassing ruler internalizes the shared conditions (Olson 1993). After great wars, victors have bound themselves through institutions to lower others' fear and their own costs of enforcement (Ikenberry 2001). The holder of the first nuclear monopoly did not extend its dominance to everything it could reach.

**Proposition 6.2 (What the race selects) [T].**
1. *No actor can rely on a winner's stated limits on its use of decisive advantage: the commitment problem (Fearon 1995; Powell 2006), with uncertainty about intentions (Mearsheimer 2001). How much weight a rival gives to the possibility that a decisive winner extends its dominance, $p_{L4}$, is a belief. An actor that decides by its worst case over a stated set of possibilities, and applies that rule to every action, counts the worst; a survival-first actor need not.*
2. *Restraint while ahead is selected against (Proposition 2.4), so the race shifts the distribution of winners toward those that extend dominance: $\Pr(\text{extends}\mid\text{wins})>\Pr(\text{extends})$. This concerns actions before victory. What a winner does after victory depends on selection inside it, because the winner is itself a field of agencies, firms, laboratories and systems among which relative selection continues (Section 3). It is not deduced here.*

The historical cases had advantages that were not decisive and not non-saturating, and their restraint rested on institutions others could check. Those institutions are the content of Definition 7.1.

**Classification.** Continuation until the win; what follows depends on the winner's internal field. The safety it offers is the winner's; for everyone else, O2 depends on the winner's restraint, which they cannot verify.

### 6.5 A finite sprint followed by restraint

**Best case.** An actor sprints to a decisive lead and then stops compounding: it freezes or rolls back, and governs at the tempo of understanding. Decisive contests are won with a modest edge when $r$ is large, so the sprint need not run far beyond understanding.

**Proposition 6.3 (The finite sprint as a trade-off) [T].** *A finite sprint involves four quantities that trade off against one another.*
1. *Exposure during and after the sprint. It grows with the ratio of hazardous variety built to coverage, and is zero after a freeze if that ratio is at most one (Proposition 5.9). Survival can stay positive: in the example of Proposition 5.9, freezing leaves $0.53$ and rolling back $0.86$.*
2. *Erosion of the advantage. Rivals that develop within understanding keep growing. If they follow the same coverage frontier in the same units, a frozen edge erodes, and reaches parity when coverage catches up with the frozen level.*
3. *Rivals' responses. Rivals cannot verify which kind of winner they face (Proposition 6.2(1)). Their responses include joining, limited defence, negotiation, watchful waiting and prevention; which is best depends on their survival comparison and beliefs (Propositions 5.14 and 6.5).*
4. *Maintaining the advantage. A decisive advantage that is not used to stop others' growth does not stay decisive. Using it to stop others' growth ends their O2: that is domination.*

A finite sprint can preserve the sprinter's survival while giving up permanent superiority. Under L6 that can be the rational choice; permanent superiority is not survival. What the trade-off establishes for the comparison is that the path passes through its greatest exposure, and through the rivals' strongest motive for prevention, before any restraint begins. Excluding the sprint as an equilibrium deviation from a cooperative arrangement needs its net deviation payoff in that dynamic game to be negative. Section 7.6 states the participation conditions under which that holds.

**Classification.** Continuation during the sprint. Restraint afterward could become a pivot, but its installation path runs through the riskiest phase.

### 6.6 Deterrence and prevention

Two actors bargain over a flow of value 1 per period, with discount $\delta$. Fighting ends bargaining: actor A then obtains the flow with its probability of prevailing, less a cost $c_A$ per period. A prevails with probability $w_1$ today, and with $w_2<w_1$ after B's AI advantage arrives one period later. Under protocol (A8), the side that gained the advantage sets the terms each period, and the other accepts or fights (Fearon 1995; Powell 2006).

**Proposition 6.4 (Preventive attack) [T].**
1. *Let $x$ be A's per-period share after the shift under whatever protocol holds. Fighting now is rational for A if $w_1-c_A>(1-\delta)+\delta x$, and only if when peace gives A the whole flow today.*
2. *Under (A8), $x=\max(w_2-c_A,0)$.*
3. *Under other protocols $x$ can be as large as $\min(w_2+c_B,1)$, and attack can cease to be rational. With $w_1=0.5$, $w_2=0$, $c_A=c_B=0.2$ and $\delta=0.8$: under (A8), A attacks ($1.5>1.0$); if A sets the future terms instead, peace gives A $1.8$ and B $3.2$, against $1.5$ each from war.*
4. *If $c_A\ge w_1$, attack is never rational in flows.*

A race to decisive advantage is the textbook condition under which rational actors who would rather bargain fight instead. Strikes on datacentres are among the options openly discussed. What drives it is not cheap war but the incredibility of future promises.

**Proposition 6.5 (Prevention under the preventer's own criterion) [T].** *Let an actor face a rival it believes certain to race, and compare outcomes by its own survival.*
1. *A single strike that succeeds with probability $\sigma_P$, returning the field to something like the arrangement, and escalates to catastrophe with probability $\varepsilon_P$, gives $\Phi^{\text{Prev}}=(1-\varepsilon_P)[\sigma_P\Phi^R+(1-\sigma_P)\Phi^P]$. It beats staying out and joining unless $\varepsilon_P>1-\max(\Phi^S,\Phi^P)/(\sigma_P\Phi^R+(1-\sigma_P)\Phi^P)$. With $\Phi^R=1$, $\sigma_P=0.7$, $\varepsilon_P=0.2$ and the race branches near zero, it gives $0.56$ [N]. As racing branches deteriorate, the escalation needed to deter prevention rises toward one: in survival terms, large costs of conflict stop deterring it.*
2. *Sustained prevention against a target that rebuilds with probability at least $b_P$ a period, each strike escalating with probability at least $\varepsilon_{\min}$, has per-period hazard at least $b_P\varepsilon_{\min}$. This holds only if the target keeps rebuilding and escalation risk does not fall; prevention that permanently ends the target's capacity, or that converts into effective joint monitoring, is a different branch.*
3. *Compared at common horizons, sustained prevention with per-period hazard $0.01$ is better for the preventer than racing with $0.05$ at every finite horizon ($0.60$ against $0.08$ at $H=50$) [N].*

Prevention can therefore be survival-preferred for the preventer. The objections to it are three, and none is a change of criterion.
- **Normative.** It ends or endangers other actors' O1 and O2 (V2, V3).
- **Epistemic.** Aimed at a rival believed certain to race, it destroys, when the rival is in fact survival-first, a game in which restraint was possible. It makes the rival the type it was feared to be (the spiral model; Jervis 1976; Kydd 1997). Shifts that cannot be observed raise the chance of mistaken prevention (Debs and Monteiro 2014).
- **Technical.** Detecting unobservable progress in time and striking at machine speed needs AI-supported intelligence and strike capability, which brings the delegation of Section 5.2.

Deterrence by threatened sabotage aims to make a decisive sprint not worth attempting.
- **Best case.** Large datacentres can be observed, and thresholds in compute can be made salient (Hendrycks, Schmidt and Wang 2025; Abecassis 2025).
- **What remains.**
  - While the value of winning stays large, the timely detection and the credibility deterrence needs approach their limits (Theorem 6.7).
  - Among nuclear-armed rivals its first problem is credibility, and under survival-first comparisons credibility can reverse (Proposition 6.5(1)).
  - Where it pushes AI into military capability, it strengthens the delegation pressure of Section 5.2.
  - Verification that supports it can also supply targets (Coe and Vaynman 2020).
  - Algorithmic progress erodes thresholds stated in compute (E9).
- **Classification.** Continuation: it holds the contest at the brink.

**The hard case.** Let a survival-first actor hold the prior $\mu$ that a capable rival holds an unbounded relative objective.
- When $\mu$ is low, its best course is to propose verifiable limits, and to take E1 unilaterally and verifiably in its own strategic loops: the costly signal of Proposition 8.4.
- When $\mu$ is high, it compares denial, a coalition that stops the decisive class, and prevention (Proposition 6.5).

In the hard case, coverage of every capable actor (Definition 7.1(a)) comes from consent or from coercion. Denying the inputs to the decisive class is the coercive form of a stop. It raises the weight on winning and the trust threshold, and if it escalates, it falls under Proposition 6.5. The theory does not derive that its net effect is positive, and does not endorse it. If neither consent nor a coercion of positive net effect is available, no actor has a secure position; that is the hard case, stated as such.

An actor that manipulates the shared risk as an instrument (Schelling 1960, 1966) plays chicken in survival terms. That is a case within survival-first reasoning: when $\Phi^T>\Phi^R$ and $\Phi^S>\Phi^P$, Proposition 5.14(1) gives chicken, with mixed equilibria and wars of attrition.

### 6.7 A verified agreement over a contest that remains

**Best case.** Rivals agree to slow and to delay decisive capability, with compute declarations, supply-chain accounting, recomputation of workloads, research transparency, and mutually assured destruction of compute if the agreement dissolves. It works without trust and bounds the largest covert project that could escape detection.

Let $\mathcal O(t)$ be the capability an agreement holds in check (the overhang); $X(t)$ the value of exiting first and $X_{\text{stay}}(t)$ the value of staying; exit occur at hazard $\mathcal H(t)$; a fraction $\mu(t)$ of the overhang be destroyed on exit; and the expected loss from exit per period be $\mathcal L(t)=\mathcal H(t)[1-\mu(t)]\Lambda(\mathcal O(t))$, with $\Lambda$ increasing. Verification detects a defection in time with probability $\upsilon$, and a sanction $F$ follows.

**Proposition 6.6 (Commitment under a growing overhang) [T].**
1. *Deterring an irreversible, public exit requires $\upsilon F\ge X-X_{\text{stay}}$. Deterring a reversible covert preparation, undone when detected in time, requires $\upsilon F\ge(1-\upsilon)(X-X_{\text{stay}})$. What matters is the net exit gain, not $X$ alone; it grows with the overhang when leaving with a decisive advantage gains faster than staying with one's share.*
2. *$\dot{\mathcal L}/\mathcal L=\dot{\mathcal H}/\mathcal H-\dot\mu/(1-\mu)+\varepsilon_\Lambda\dot{\mathcal O}/\mathcal O$, with $\varepsilon_\Lambda$ the elasticity of $\Lambda$. Growth of the overhang faster than the decline of the exit hazard is not sufficient for the loss to rise.*
3. *An agreement that preserves relative positions (proportional caps or reserves) preserves the relative term of every payoff, and with it the motive in $X$.*

**Theorem 6.7 (Verification and the value of winning) [T].** *In the assurance game of Proposition 8.1:*
1. *If $T>R$, cooperation requires timely detection $\upsilon>(T-R)/(T-P+F)$, which tends to one as $T$ grows for a fixed sanction. If $T<R$, cooperation does not require verification, and verification lowers the trust threshold. Verification is required exactly when, and to the degree that, the value of winning exceeds the value of cooperating.*
2. *Detection counts only before a defection becomes decisive. Under P1 and P2 that window is short, and acceleration shortens it.*
3. *Verification does not carry unverifiable information (Proposition 8.3), future commitments unless $\upsilon F$ keeps pace with the net exit gain (Proposition 6.6), the judgment of approvers (Section 3), or its own reliability.*
4. *Verification acts in two ways. It raises timely detection. It can also lower $T$ by bounding the size of the largest defection that would go undetected, for instance by accounting for compute; that route does not need $\upsilon\to1$. The bound erodes as algorithms spread and capability per unit of compute grows, so it holds only if the verified coalition's advantage in effective compute grows at least as fast as spillover erodes it. Verification also removes the information rents that private types create in dividing a joint arrangement (Proposition 7.8).*

**An example.** *AI 2040: Plan A* (Larsen, Dean, Halstead, Lifland, Greenblatt and Kokotajlo 2026) is a deal among leading powers to slow AI development and delay superintelligence to about 2040, designed to be enforceable without trust [O: E10]. Its elements include:
- compute declarations and supply-chain accounting;
- inference-only retrofits of datacentres and recomputation of workloads;
- research transparency;
- mutually assured destruction of compute, fabs and robots if the deal declines;
- hardened reserves of about two per cent of pre-deal compute.

It aims to end winner-take-all dynamics through many frontier developers, transparency, broad diffusion and a citizens' dividend. It bounds the size of covert projects rather than requiring near-perfect detection, which is the second route of Theorem 6.7(4).

Its own scenario estimates do not show near-certain dissolution: one author's judgment puts decline in years five to ten at about four per cent a year, half dissolution and half impairment, and cumulative decline over ten years near half. Its handoff to AI systems is a conditional decision that weighs further alignment research against other risks, and it keeps an option to extend the pause. The durability tests of Section 6.8 apply to it as to every arrangement.

**Classification.** It changes the tempo of W, slowing and capping. It keeps relative standing in its enforcement: proportional reserves, and a coalition that must stay ahead of covert projects. So the objective of W is kept in its fallback, and C is addressed only through transparency. That makes it a bridge. Whether it can be the end depends on the tests below, and on whether it lowers the value of winning or only bounds defection.

### 6.8 Durability stress tests, applied to every arrangement

**Definition 6.8 (Durability tests) [D].** An arrangement is tested along six dimensions, using its own documents and estimates, not assumptions added by the tester.
- **D1 Fallback.** What do parties hold if it dissolves? A decisive race from preserved relative standing, or something less dangerous?
- **D2 Hazard of breakdown.** What is its estimated hazard of dissolution or impairment over the horizon it must cover, and what drives that hazard?
- **D3 Retained authority.** After any handoff or delegation, who keeps informed veto, modification, replacement, exit and execution? Which of C1–C4 still hold?
- **D4 Capture of its own correctors.** Do its evaluators and adjudicators have full inbound row sums below one (Proposition 3.10)?
- **D5 Violation by the strongest participant.** What happens when the leading provider or state violates it?
- **D6 Succession and continuity.** What happens on a change of leadership, and do essential services continue during correction or sanction?

The tests apply symmetrically: to every continuation policy, to agreements that keep the contest underneath, and to the cooperative design of Section 7 (results in Section 7.8). An arrangement that has the form of cooperation but fails D1–D3 on its own estimates may be called a *pseudo-solution*. The label summarizes test results; it is not a substitute for them.

| Arrangement | D1 Fallback | D2 Breakdown | D3 Authority | D4 Correctors | D5 Strongest violates | D6 Succession |
|---|---|---|---|---|---|---|
| Regulated national competition | The race itself | Rule changes with administrations (E3) | Kept nationally | Mandates shifting toward industry (E3) | Domestic law only | Exposed to change of administration |
| Lead and margin | The race | Margin decays (Remark 6.1) | The leader's | The leader's evaluators | No constraint | The leader's internal field |
| Benign winner | Domination | Depends on internal selection | The winner's | The winner's | Not applicable | Internal |
| Deterrence by sabotage | War or race | Misjudgment (Prop 6.5) | Kept | Mutual intelligence | Strike | Brittle |
| Plan A type agreement | A short sprint from parity: about a year to superintelligence after decline if compute is destroyed, by its authors' estimate | Decline about 4% a year in years 5–10, cumulative about half over 10 years (scenario judgment) | A conditional handoff; who keeps veto after it is not specified | Joint verification; titration inside the coalition | Mutual destruction of compute; sanctions | Leadership change is a listed cause of decline |
| Cooperative design (§7) | See Section 7.8 | See Section 7.8 | See Section 7.8 | See Section 7.8 | See Section 7.8 | See Section 7.8 |

### 6.9 The comparison at common horizons

The table classifies each policy by what it changes, and names the crux on which its adequacy turns.

| Policy | Changes | Class | Main residual risk | Crux |
|---|---|---|---|---|
| Technical alignment and AI-assisted correction alone | None of W, C, N | Component | The game among principals; absorption of gains; common causes | Can contestable coverage keep pace with hazardous variety? |
| Regulated national competition | N partly | Continuation | Coverage across jurisdictions; rule-makers' contest; weakening commitments | Will restraint hold when rivals advance (E2)? |
| Leadership and margin | None | Continuation | Margin decays and is judged inside | Do leads get spent on safety, and do rivals follow? |
| Benign winner | None before victory | Continuation | Others' O2 rests on unverifiable restraint | Can a winner's limits be made checkable? |
| Finite sprint, then restraint | The tempo of W, after the sprint | Continuation, then possibly pivot | Peak exposure and prevention during the sprint | How small is the hazardous ratio built (Prop 5.9)? |
| Deterrence by sabotage | None | Continuation | Misjudgment; militarization | Observability and credibility |
| Verified agreement over a remaining contest | The tempo of W | Bridge | Fallback and handoff (D1, D3) | Does it lower the value of winning, or only bound defection? |
| Temporary training pause | The tempo of W, for a time | Depends on what changes (Prop 4.5) | Resumption unchanged | Readiness dimensions R1–R6 |
| Cooperative design with E1 and E2 or E3 | W, C and N: the governing model | Pivot | Its own dissolution, capture and restriction | D1–D6 for the design; participation (Section 7.6) |

**An illustration of the two cruxes [N].** Let the per-period hazard on a path be $0.05$ times its uncovered share, plus a background $0.001$. On the cooperative path, add a hazard of dissolution times the loss its fallback carries. Survival at horizons 10, 30 and 100 is as follows.

| Path | $H=10$ | $H=30$ | $H=100$ |
|---|---|---|---|
| Continuation, uncovered share rising from $0.2$ by $0.01$ a period | 0.871 | 0.567 | 0.028 |
| Continuation, uncovered share kept summable | 0.966 | 0.941 | 0.873 |
| Cooperation, summable share, dissolution 2% a period with fallback loss 0.5 | 0.873 | 0.696 | 0.319 |
| Cooperation, summable share, dissolution 0.2% a period | 0.956 | 0.913 | 0.789 |

The numbers are illustrative, not estimates. They show the structure of the decision:
- If continuation keeps the uncovered hazardous share summable, it can beat a cooperative arrangement that is fragile.
- If the uncovered share rises on the continuation path, any cooperative arrangement with a modest dissolution hazard does better at every horizon past the near term.

So the comparison turns on two quantities: whether correction on the present path keeps pace with hazardous variety, and how durable a cooperative arrangement can be made. The first is crux C1 of Section 9. The second is the subject of Sections 7 and 8, which design for it and test it.

**Where the decision criteria disagree.**
- Under standard D, the worst case over the justified range includes a rising uncovered share on the continuation path, because no evidence today excludes it (Section 2.6, E5–E7). So continuation fails the tolerance at medium and long horizons unless its correction can be shown to keep pace.
- An expected-value criterion that puts low probability on the rising-gap case, and values the benefits of speed highly, can prefer continuation.
- A discounted criterion prefers racing whenever the hazard it adds is below the growth it adds (Section 5.6).

These disagreements are the normative cruxes, and Section 9 states them.

---

## 7. What cooperation makes possible

### 7.1 The purpose

Cooperation is not only a constraint on danger. Its purpose is what AI can do for people when it is not the instrument by which one actor wins the common future:
- medicine and public health;
- education;
- science;
- competent administration;
- infrastructure;
- the long-horizon work that fragmented incentives under-supply.

The joint value is very large. The race dissipates it (Proposition 5.2); cooperation realizes it (V1).

**Authority as a productive capacity (V4).** Authority can coordinate investment, guarantee services, support learning and act on shared purposes. The ideal the theory draws on justifies authority by its responsibility for improving people's lives and the historical trajectory. That ideal enters the design as a purpose to be sustained, not as a premise that it is already realized. The governing purpose is itself part of the mechanism:
- how institutions select and form officeholders;
- how they reward service and sustain professional obligations;
- how they hear unwelcome evidence;
- how they evaluate long-term outcomes and revise harmful practices.

Neither inevitable corruption nor automatic benevolence is assumed. A stated mission is not proof of implementation; its formation and persistence are causal variables.

**Provision that does not become the system.** Taken out of the contest, AI can be what infrastructure is: provision of the conditions of a decent life, built to meet need rather than to gain standing. Trees are the image: they give shelter and fruit, maintain the system they belong to, and do not become it. The theory supports four properties of such provision.
- **Distributed.** Many providers below the size threshold of Proposition 3.4(2) do not cultivate influence over their correctors, and splitting a provider divides cultivated conversion by $k^{2/\eta}$ (Proposition 3.6(7)).
- **Good enough.** Systems that stop growing once they meet a need keep their hazard modes within correction and confer no decisive advantage. Production directed at need has a point of enough; relative advantage has none.
- **Replaceable.** Systems that can be replaced keep human capacity above $\mathcal K_{\min}$ and avoid the lock of Lemma 5.4.
- **For everyone.** Understanding and provision go to everyone, not to a class of guardians. Every guardian is a corrector, and Section 3 applies to it.

**Reward for contribution, not rights over correction (V5).** Productive contribution should be rewarded: revenue, contracts, recognition. What success should not buy is the right to appoint evaluators, set thresholds, exclude entrants or amend the governing rules. Separating the two keeps productive incentives while cutting the conversion $b_{ij}$ of Section 3.

### 7.2 What cooperation must contain

Four safeguards make consequences return on the host of Section 2.
- **(I1) Consequences return.** A liability $\tau>\nu$ on load is enacted, in advance for anticipated harms and on the alarm for unanticipated ones, so that $\tau_{\text{eff}}>\nu$ once rule-making is uncaptured. For harms beyond assets, this is regulation in advance rather than liability (Shavell 1984). Near a threshold a quantity instrument does better than a price (Weitzman 1974).
- **(I2) Independent correctors.** In evaluation and rule-making, $d(t)\ge(1+\varsigma)d^\ast(t)$ for some $\varsigma>0$, with $d^\ast$ computed from each domain's full row.
- **(I3) Independent evidence.** Either masking stays below the threshold under an averaged alarm, or a conservative alarm uses a bound on masking established independently of the field (Remark 3.9).
- **(I4) Before capture.** (I1)–(I3) are in force before the corrector domains are captured.

**Definition 7.1 (Cooperation) [D].** An arrangement is cooperative if it has:
- (a) **Coverage.** It binds every actor whose share can grow in the environment it governs, and the rule-makers of every jurisdiction where such growth can occur.
- (b) **Content.** It enacts (I1)–(I3), with thresholds, triggers and authority to act fixed in advance (I4).
- (c) **Verification.** Its correctors assess compliance and the host's condition, and each has a full inbound row sum below one, counting conversion from every party and every shared source.
- (d) **A changed value of winning.** It forms a common assessment, from independent evidence, of what winning is worth and of the hazards all share, and it shares the benefits of capability.
- (e) **AI out of the contest, with understanding ahead of capability.** Strategic and coercive decision loops are kept under human authority with jointly verified limits (E1). The tempo of capability is bound to correction capacity (E2 or E3).
- (f) **Trust built deliberately.** Graduated reciprocal steps (Osgood 1962) and costly signals (Kydd 2005; Proposition 8.4).
- (g) **Shared provision.** Common infrastructure supplies useful services and correction that no participant owns.
- (h) **Answerability.** People affected by consequential decisions have standing, access to evidence and timely remedies (V3).

The definition constrains properties, not institutional form. One institution can meet it, and so can mutually recognized institutions of several jurisdictions.

### 7.3 Safeguards, and why no one can supply them alone

Let selection be replicator dynamics among carriers that differ only in load. Let a carrier of load $e_{\min}$ with $he_{\min}<\rho(1-V_{\min}/K)$ be present. For part (3), let a carrier with positive share and load $e_{\max}$ satisfying $he_{\max}>\rho(1-V_{\min}/K)$ also be present.

**Theorem 7.2 (Sufficient safeguards, and a necessary condition) [T].**
1. *Sufficiency. Under (I1)–(I4), $\tau_{\text{eff}}>\nu$ after a finite time, $E(t)\to e_{\min}$, and $\liminf_tV(t)>V_{\min}$. This holds from the outset for anticipated harms, and for unanticipated ones after an alarm that fires above the floor. The trajectory is viable if, in addition, the host stays above its floor during the transient in which $E$ falls.*
2. *Non-redundancy. For each of (I1)–(I3) there are parameters satisfying C0 and the other two under which the host crosses its floor. There are also parameters under which (I1)–(I3) come into force only after rule-making is captured, and the host crosses its floor.*
3. *A necessary condition. Under C0 and the support assumption, every viable trajectory satisfies $\limsup_{T\to\infty}\frac1T\int_0^T\tau_{\text{eff}}(t)\,dt\ge\nu$.*

Part (1) is sufficient, and part (3) is necessary in the weak sense stated. The transient in (1) is real: with liability in force from the start but the race strategy holding 99% of activity, the host dips to $0.14$ before recovering [N].

**Proposition 7.3 (No unilateral solution) [T].** *Assume C0 and C1.*
1. *While $\tau_{\text{eff}}<\nu$, and among carriers that differ only in that contribution, no carrier's unilateral contribution to (I1)–(I4) is favoured by selection.*
2. *Suppose no single rule-maker reaches every carrier whose combined load satisfies C0, and the rule-makers are themselves $n_s$ actors in a contest of standing with weight $\lambda_s>(\Theta_s-n_s)/(n_s-1)$. Then no rule-maker imposes the liability alone in equilibrium. Whether an agreement among them is an equilibrium is governed by Proposition 8.1.*
3. *Restraint is each carrier's best response once the effective liability exceeds the advantage, $\tau(1-x_{\mathsf S})>\nu$. Enacting $\tau>\nu$ is not enough while $x_{\mathsf S}$ is large.*

### 7.4 A common frontier

**Proposition 7.4 (A common frontier changes the failure mode) [T].** *Let the value of capability be common, $\pi_i=\Omega(\mathcal E)/n-ce_i-\ell\mathcal E$ with $\Omega$ concave, rather than allocated by a contest. Private incentives give $\Omega'(\mathcal E)=n(c+\ell)$ and the joint optimum $\Omega'(\mathcal E)=c+n\ell$, so total intensity is at or below the joint optimum. The residual failure is too little speed, not too much. The joint optimum must also respect the host's floor.*

A common frontier does not remove the second order. Allocation within a joint project is itself a contest, and the project, as the largest carrier, has the largest return to influence over its correctors (Proposition 3.4). It therefore needs correction outside the project, equipped with AI, contestable, and growing at the rate of Proposition 3.6.

There are $n$ actors. Cooperators hold effort $e_c$; racers choose theirs. Whoever wins the decisive contest gains $\Omega$, and every actor that loses it bears $L_b$. Under *separate frontiers* every effort enters the contest separately. Under a *common frontier* cooperators pool their effort into one entity of strength $(me_c)^r$, where $m$ is the number of cooperators. The pool yields a common value $\Omega_c$ split equally and confers no dominance among them. Timing is two-stage: actors choose whether to race, then racers play their equilibrium. The measure is material payoff.

**Proposition 7.5 (A common frontier in the $n$-player game) [T, N].** *Take $n=4$, $\Omega=\Omega_c=L_b=c=1$, $\ell=0.3$, $e_c=0.05$ and $r=1.3$.*
1. *Under separate frontiers racing is strictly better for every number of other racers; the unique pure equilibrium is all racing.*
2. *Under a common frontier, all cooperating is a strict Nash equilibrium ($R=0.140>T=0.002$), and so is all racing.*
   - *If each other actor races independently, cooperating is a best response iff trust in each rival exceeds about $0.61$.*
   - *If a deviator instead best-responds to the others' fixed intensities, the trust needed rises to about $0.82$.*
3. *Reducing the game to one actor against the other three acting together gives $0.413$. That is the threshold for a belief that the others move together, not risk dominance in the original game. Written with the three as a coalition maximizing their summed payoff, the coalition's cooperation is strictly dominant.*
4. *The two equilibria persist under the variations tried in which racers' subgames have a symmetric pure equilibrium, except that a small pooled effort ($e_c=0.03$) leaves only all racing. The aggregate threshold is $0.755$ with $n=3$ and $0.902$ with $L_b=0.5$. With $n=2$, all cooperating is an equilibrium for $r$ up to about $1.2$: a lower $r$ makes a common frontier easier to sustain.*
5. *Holding $\Omega_c$ and $L_b$ fixed, the pooled effort needed to keep $T\le R$ is $0.0054$, $0.035$, $0.141$ and $0.49$ for $\Omega=0.5$, $1$, $2$ and $4$. Scaling $\Omega_c$ and $L_b$ with $\Omega$, it grows in proportion and $R$ stays positive. The lid depends on the value of winning relative to the joint value and to the penalty of subordination.*

What makes cooperation pay in the construct is that cooperators do not subordinate one another. A common frontier turns a dilemma into a coordination problem, while the value of winning is moderate. When that value is large, keeping ahead of defectors is the race moved up a level, and a pool strong enough to subordinate defectors is a concentration of power that Section 3 says will be selected for influence over its correctors.

**Remark 7.6 (Concentration at two orders).** Concentration works in opposite directions at the two orders.
- At the first order and in the contest, more contenders make the race fiercer (Proposition 2.5's $\bar\lambda$; Proposition 5.1(4)). Fragmentation raises speed and conditional risk (Bueno de Mesquita, Dziuda and Polborn 2026).
- At the second order, cultivated influence rises with $\sum_kp_k^{1+2/\eta}$ (Proposition 3.6(8)). That calls for removing common control and for distributed provision.

The design that serves both is to merge the frontier and to disperse and insulate correction: a common frontier at the first order, and independent correctors keyed to no one at the second.

### 7.5 Verification by rivals

**Proposition 7.7 (Rival verification) [T].** *Let the rival's verifier have a full inbound row sum below one, counting conversion from the verified party, from the verifier's own side, and from shared sources: models, supply chains, professional paradigms, interests against third parties. Then no one of these captures the verifier (Proposition 3.10(2)). Rivalry keeps the verified party's contribution near zero; it does not by itself bound the rest of the row. A verifier that takes $0.10$ from the verified party and $0.95$ from shared sources is captured once those sources are [N].*

There are five limits.
- Rival verifiers raise false alarms, which joint resolution must absorb.
- Rivals can collude against third parties, which coverage and third-party access must prevent.
- Mutual verification checks compliance, not judgment.
- A verifier biased toward finding violations is an uninformative sender of unverifiable claims (Proposition 8.3), so it must rest on evidence the other side can check.
- An accusation under rivalry can trigger prevention (Proposition 6.4), so joint resolution comes before any response.

### 7.6 Participation of the strongest

Two actors have private capability types, strong or weak, with costs $c_s<c_w$, each strong with probability $p_s$, independently. Outside the arrangement, types are revealed in the race, a complete-information all-pay contest for $\Omega+L_b$ (Hillman and Riley 1989). A strong actor against a weak one gets $U=(\Omega+L_b)(1-c_s/c_w)-L_b$; otherwise $U=-L_b$. The race's survival is $\Phi^{\text{race}}$, possibly depending on both types. The arrangement yields a common value net of costs $S_a$, divided in shares $\mathsf s_i$, with survival $\Phi^R$. Utility is $u_i=\Phi_i(V_i+\bar V)$ with $\bar V>0$.

**Proposition 7.8 (Participation) [T].**
1. *Efficiency. Under complete information and transferable utility, a pair of types gains from the arrangement iff $\Phi^R(S_a+2\bar V)\ge\sum_i\Phi^{\text{race}}_i(U_i+\bar V)$; strict participation needs strict inequality. The strong actor's minimum share is $[\Phi^{\text{race}}_1(U_1+\bar V)/\Phi^R-\bar V]/S_a$, subject to the bounds on feasible shares.*
2. *Information. With private types, independent, and participation decided before types are revealed to the other side, Bayesian incentive compatibility requires each type's interim expected share to be independent of its own report. Ex-post shares may vary with reports: with $p_s=0.8$ and $\mathsf s_1=\tfrac12+\tfrac12h(t_1)h(t_2)$, $h(\text{strong})=0.2$, $h(\text{weak})=-0.8$, every type's interim expected share is $0.5$ while ex-post shares range from $0.42$ to $0.82$ [N]. Budget balance then makes the interim shares constants that sum to one. So the arrangement is feasible without verification iff $\Phi^R(S_a+2\bar V)\ge\sum_i\sup_c E\big[\Phi^{\text{race}}(c,t_j)(U_i+\bar V)\,\big|\,c\big]$. Constant shares are one mechanism that achieves this. If participation is decided after types are known, ex-post participation constraints apply instead.*
3. *Verification revealing types, for instance by accounting for compute, removes the information rents and moves (2) toward (1). This function differs from the timely detection of defection (Theorem 6.7(4)).*
4. *Survival compression. The information condition relaxes as survival in the race falls below survival under the arrangement. Equal shares become feasible without verification once $\Phi^{\text{race}}/\Phi^R$ falls below a threshold, with no limit taken.*
5. *Distribution. Under complete information, an overwhelmingly strong actor takes part only for a share near its race payoff. Equal shares can still meet its constraint in several ways. The joint value can be raised: with $S_a=2$ an equal share of $1$ exceeds an outside option of $0.925$ [N]. The value of winning can be lowered. Survival can be compressed. The asymmetry of costs can be changed.*

With $c_s/c_w=0.1$, $\Omega=1$, $L_b=0$, $S_a=1$ and every $\Phi=1$, the sum of suprema is $0.36$, $0.90$, $1.44$ and $1.71$ at $p_s=0.8$, $0.5$, $0.2$ and $0.05$. The arrangement is feasible without verification in the first two cases and not in the last two, although cooperation is efficient for every pair of types. With $\Phi^R=0.95$ and $\bar V=1$ at $p_s=0.2$, equal shares become feasible once $\Phi^{\text{race}}/\Phi^R\le0.872$ [N].

Rare strong types make each strong type expect to meet a weak one, and expect much from the race. That is mutual optimism. The race is then a failure of bargaining under private information, the first of Fearon's (1995) mechanisms; Proposition 6.4 used the second. Which mechanism is second-best depends on the set of mechanisms allowed and on commitment, which are not solved here.

### 7.7 A concrete candidate design

One design is developed far enough to expose its assumptions. Call it *the Compact*: an arrangement for shared AI provision and correction. Its functions are listed separately, because financing, ownership, service, evaluation, rule-making and enforcement can be combined in different ways, and the strongest design may pool some and keep others contestable.

| Function | Design | Why (result) |
|---|---|---|
| Purpose and its revision | A charter with three purposes: useful provision for all participants' populations; protection against O1 and O2; effective correction. Revision needs a supermajority of participants and the consent of a chamber representing affected persons. No participant can revise a purpose while it is under assessment. | V1, V3; revision distinguished from capture (Definition 3.3) |
| Coverage and membership | Open to every state and provider above a capability threshold. Participation is made individually rational by access to shared services, a share of the dividend, and capacity building, not only by sanctions. | Proposition 7.8; coverage (Definition 7.1(a)) |
| Financing | A levy on frontier compute above a threshold, paid into two funds by formula. The correction fund is indexed to the field's capability, so it grows at least at the rate of Proposition 3.6. The shared-services fund pays for provision. No appropriation by the evaluated. | Proposition 3.6; independence (I2) |
| Ownership | A common layer owned by the Compact: evaluation infrastructure, safety research, shared reference systems for public services. Production by many providers, public and private, with a cap on any one provider's share of essential services. | Propositions 3.4(2), 3.6(7)–(8); Remark 7.6 |
| Service obligations | Baseline access to useful services (health, education, scientific tools, support for public administration) for every participant, with continuity guarantees. | V1; D6 |
| Access and local competence | Portable interfaces, escrow of systems that provide essential services, and support for each participant to build the capacity to audit, operate and replace them. Entry paths for latecomers. | Replaceability; Lemma 5.4; development concerns |
| Evaluation | A network of independent evaluators with mandated access, funding by formula, rotation and cooling-off periods. Appointment by a body in which no provider votes. Diversity counted in effective control domains, not in organizations. Evaluators are themselves red-teamed. | Propositions 3.10, 5.11(2), 7.7 |
| Rule-making | Thresholds fixed in advance, with sunset and review. Voting not proportional to compute or market share, and insulated during any pause. | Propositions 3.11, 3.12 |
| Strategic decision loops (E1) | Human authorization, with a minimum time for deliberation, for decisions on the use of force and on nuclear command. Parallel human capacity, drilled. Doctrine and exercises open to mutual inspection. | Proposition 5.5; Lemma 5.4; Proposition 8.4 |
| Tempo (E2/E3) | No building of the decisive class while R1–R6 are unmet. Capability thresholds by evaluation, and input thresholds in effective compute that tighten with algorithmic progress. | Proposition 4.5; Theorem 5.8; E9 |
| Decision and execution | Graduated remedies: notice; restriction of a specific capability; suspension of specific deployments. Never suspension of essential services. Emergency powers narrow, time-limited and reviewable. | D6; unjustified restriction |
| Appeal | An independent panel with access to the evidence under confidentiality, a fixed deadline, and compensation if a finding is overturned. | V3 |
| Amendment and succession | Protections entrenched. Amendment needs the supermajority and the affected persons' chamber. A change of leadership in a participant triggers review, not suspension. | D6 |
| Reward and authority | Providers earn revenue and contracts by usefulness. They have no rights to appoint evaluators, set thresholds, exclude entrants or amend the rules. | V5; cuts $b_{ij}$ |

Bounded competition continues inside the Compact. Providers compete on usefulness, cost and reliability, and jurisdictions keep plural local purposes. What is removed is competition for control over the shared conditions and over the correctors.

### 7.8 Stress tests of the design

The Compact faces the same tests as every other arrangement (Definition 6.8), and six hard cases besides.

**An adverse finding against a weaker participant.** An evaluator reports dangerous conduct by a participant with few resources, which disputes the finding and alleges discriminatory standards.
- Pending appeal, the Compact may restrict only the specific capability at issue.
- Essential services continue through alternative providers, which portable access makes possible.
- The appellant sees the evidence under confidentiality; the panel decides within the deadline; compensation follows if the finding is overturned.
- The power to suspend could become containment. The safeguards against that are the narrow scope of interim measures, the burden of evidence on the Compact, and the appellant's standing.

**An adverse finding against the leading provider.** Suspending it could interrupt services for everyone, so formally equal procedures would be unequal in effect.
- The design meets this in advance. A cap on any one provider's share of essential services, escrowed systems and funded standby capacity mean that a restriction on the leader's hazardous capability need not stop services.
- Execution falls first to the leader's host jurisdiction under the Compact's order. If that fails, the fallback is collective restriction of frontier inputs.
- This is the hardest case, and the design does not dissolve it. It reduces the asymmetry of dependence that would otherwise make enforcement against the strongest impossible.

**A coalition of insiders.** Rival elites agree on mutual secrecy and immunity while weakening public correction. Four channels answer to people outside the coalition:
- the affected persons' chamber;
- protected reporting;
- evaluators funded by formula;
- publication of findings by default, after a fixed delay.

**An unjustified restriction.** The Compact is used to contain a developing participant. The participant has standing to challenge. The burden is on the Compact to show evidence of hazard. Restrictions carry sunsets, and the Compact has obligations to build capacity.

**Succession and withdrawal.** A major participant changes leadership or withdraws.
- Review is triggered, not suspension.
- On withdrawal, the fallback is shaped by the design. Because the decisive class was not built (E2) and benefits and knowledge were diffused, the withdrawing party starts any race far from decisive capability and with a lower value of winning.

**Loss of an essential service.** A provider fails or an outage occurs. Redundancy, escrow and standby capacity carry the service.

The durability tests give the following results for the design.

| Test | Result for the Compact | Status |
|---|---|---|
| D1 Fallback | A race from a lower overhang, with diffused knowledge and no decisive-class capability built | By design; still a race |
| D2 Hazard of breakdown | Driven by the value of winning (lowered by sharing), changes of leadership, and violation by the strongest | Unknown; crux C4 |
| D3 Retained authority | No handoff deadline. C1–C4 maintained by drills and rates of overrule | By design; to be tested |
| D4 Capture of its correctors | Funding by formula, appointment insulated, diversity counted in control domains | Certificate by row sums; to be measured |
| D5 Violation by the strongest | Dependence caps and standby reduce the asymmetry; collective input restriction as the fallback | The hard case remains |
| D6 Succession and continuity | Review rather than suspension; continuity of essential services | By design |

The design does not eliminate the hazard of breakdown or the case of violation by the strongest. It bounds them by choices that can be inspected and tested. Three things could make its hazard of breakdown lower than that of an agreement that keeps the contest underneath:
- shared benefits lower the value of winning (Corollary 8.2(1));
- keeping AI out of strategic loops is a strict equilibrium among informed actors (Proposition 5.5);
- its fallback is not a decisive race from parity.

These are hypotheses about the design. They are not established results, and Section 9 treats the durability of cooperative institutions as a central crux.

---

## 8. A reachable transition, and readiness to resume

An attractive end state is not a reachable one. The transition must be survivable at every stage, and every participant must prefer to continue given its beliefs and the others' strategies.

### 8.1 Trust

Reduce the interaction between an actor and the rest to two actions: cooperate (restrain under an agreement) or defect. Payoffs are $R$, $T$, $P$ and $S$ in a stated measure. Verification detects a defection in time, before it becomes decisive, with probability $\upsilon$. A defection detected in time is reversed: the defector receives $P-F$, with $F\ge0$ a sanction, and the cooperator reverts to $P$. Undetected defection yields $T$ and $S$. Trust $\varpi$ is the belief that the other will cooperate. Write $T_\upsilon=\upsilon(P-F)+(1-\upsilon)T$, $g_C=R-T_\upsilon$ (what cooperating gains against a cooperator) and $g_D=(1-\upsilon)(P-S)$ (what it loses against a defector).

**Proposition 8.1 (Assurance) [T].**
1. *The expected advantage of cooperating is $\varpi g_C-(1-\varpi)g_D$.*
   - *If $g_C,g_D>0$, cooperation is a best response iff $\varpi\ge\varpi^\ast=g_D/(g_C+g_D)$.*
   - *If $g_C\le0<g_D$, no degree of trust suffices.*
   - *If $g_D\le0<g_C$, cooperation is dominant.*
   - *If $g_C<0$ and $g_D<0$, the game is chicken, and cooperation is a best response iff $\varpi<g_D/(g_C+g_D)$.*
2. *When $T>R$, cooperation needs $\upsilon>(T-R)/(T-P+F)$. When $T<R$, it is possible without verification at trust $\varpi\ge(P-S)/((R-T)+(P-S))$.*
3. *Cooperation is risk-dominant iff $g_C>g_D$. That is a property of the payoffs, not of trust. It is selected under global games (Carlsson and van Damme 1993) and adaptive play with rare mistakes (Kandori, Mailath and Rob 1993; Young 1993).*
4. *In the $n$-player game with independent belief $\varpi_1$ about each rival, $\varpi_1^{\,n-1}\ge\varpi^\ast$ is sufficient only under bounds on intermediate states. A cooperator must get at least $S$ when some but not all others defect, and the advantage of defecting over cooperating in any such state must be at most $g_D$. Without the second bound the condition fails. In a three-player example with cooperation-minus-defection advantages $(1,-10,-1)$ by number of defecting others, each rival cooperating with probability $\sqrt{0.5}$ gives an expected advantage of $-3.73$, although all others cooperate with probability $0.5$ [N]. The exact condition is the binomial form used in Proposition 7.5.*

Trust has three meanings:
- $\varpi$, the belief that the other will choose to cooperate;
- **reliability trust**, confidence in verification instruments, which enters $\upsilon$;
- **commitment trust**, confidence that the arrangement and its enforcement will persist, which enters Proposition 6.6.

Reliable instruments let parties cooperate without good will. But the instruments need reliability trust of their own, and installing them is a first step taken under $\varpi$.

**Corollary 8.2 (What relaxes the trust constraints) [T].**
1. *Lowering the private value of winning relative to the joint value lowers $T-R$, the weight on winning $\lambda$ (and with it the bias of messages, Proposition 8.3), and the net exit gain. It relaxes all three constraints at once.*
2. *Verification raises $\upsilon$ on verifiable dimensions. It lowers the assurance threshold and relaxes the constraint against deliberate exit, but does not carry unverifiable information.*
3. *Sanctions relax the assurance and exit constraints at the price of escalation, and cannot be enforced against a decisive defector after the fact.*
4. *Lowering the vulnerability of restraint, $P-S$, lowers the threshold. A common frontier does this (Proposition 7.5).*

Not every obstacle to cooperation is a lack of trust.

| Obstacle | In the model | Intervention |
|---|---|---|
| Misjudged shared losses | Perceived payoffs differ from true ones | Evidence, explanation, common knowledge |
| A real conflict of incentives | $T>R$ in welfare or survival | Change payoffs and enforcement |
| Coordination failure | Cooperation is better, but each fears cooperating first | Assurance: verification, graduated steps |
| Commitment and capture over time | The arrangement pays now; later exit or a change of rules pays more | Incentive compatibility over time; independent correction; a staged transition |

### 8.2 Words and signals

In the uniform-quadratic model of Crawford and Sobel (1982), a sender knows a state $u\in[0,1]$, and a receiver chooses a response $y$, ideally $y=u$. The sender values the receiver's correct response, and also gains $2\lambda\beta_s$ per unit of the receiver's response in one direction, for example restraint beyond what the state warrants. Its bias is $b=\lambda\beta_s$.

**Proposition 8.3 (Credibility of messages) [T].** *If $b=0$, full revelation is an equilibrium. If $b>0$, informative communication is possible iff $b<1/4$, and the most informative equilibrium has $N(b)$ messages, the largest $N$ with $2N(N-1)b<1$.*

What can be measured passes by verification. What cannot be measured passes only through words, and words are believed only when the sender and receiver want the same action from the receiver. Messages about the shared hazard are not credible merely because the hazard is shared. A sender gains from the receiver's restraint whatever it intends to do itself, so its bias is positive on exactly this topic. Nor does near-indifference make talk credible: with $R=1$, $T=2\varepsilon$, $P=\varepsilon$ and $S=0$, a sender that intends to race still gains $\varepsilon$ from the receiver's cooperation, however small $\varepsilon$ is [N].

The prediction that the trajectory is dangerous is carried by other means:
- a derivation from public premises that each actor can check, which turns the problem into one of attention and common knowledge, though its numbers need joint measurement;
- verifiable evidence: incident disclosure checked by third parties, joint evaluation suites run by both sides' independent evaluators, joint red-teaming, international scientific assessment (Milgrom 1981; Grossman 1981);
- evaluation protocols agreed in advance (Kamenica and Gentzkow 2011);
- costly signals.

Under common priors and rational updating, mutual optimism alone cannot produce war (Fey and Ramsay 2007), which supports making the prediction common. But in an idealized experiment, falling behind drove unsafe choices while the stated shared risk changed them little (E11). A change of prediction may not suffice by itself.

**Proposition 8.4 (When keeping AI out of one's decision loops is a signal) [T].** *A sender is either survival-first and prices in the lock (type $S$, probability $1-\mu$), or holds a relative objective (type $R$, probability $\mu$). It can send $E$: a verifiable, durable removal of AI from its own strategic decision loops for a period $D$, open to inspection. $E$ costs type $\theta$ the amount $k_\theta$; by Proposition 5.5, $k_S$ can be zero or negative. A receiver restrains iff its posterior that the sender is type $S$ is at least its threshold $\varpi^\ast$. The receiver's restraint is worth $G_\theta$ to type $\theta$, including, for type $R$, what it gains by exploiting the restraint.*
1. *A separating equilibrium, in which type $S$ sends $E$, type $R$ does not, and the receiver restrains after $E$ and not otherwise, exists iff $k_S\le G_S$ and $k_R\ge G_R$, with the belief that a non-sender is type $R$.*
2. *If $k_R<G_R$, type $R$ imitates. No separating equilibrium exists, and the receiver restrains after $E$ only if $1-\mu\ge\varpi^\ast$.*
3. *Hence $E$ separates only if it costs a relative-objective actor at least what it gains by inducing restraint. That requires $E$ to be durable (large $D$), verifiable, and costly to reverse. A reversible or unverifiable $E$ is cheap talk.*

With $k_S=-0.05$, $k_R=0.30$, $G_S=0.40$ and $G_R=0.20$, separation holds. If the step can be reversed cheaply ($k_R=0.05$), it does not [N]. Unilateral, verifiable E1 in one's own strategic loops is therefore a candidate first move. It is cheap for an actor that prices in the lock and can be made costly to imitate. Whether it separates in practice depends on measured values of $k_R$ and $G_R$; that is a design question for Stage 2 below.

### 8.3 Four temporal arrangements

Stopping, slowing, pausing and keeping AI out of the contest are different choices. They are kept apart.

- **E1: AI out of the contest.**
  - *Narrow form:* human authority over strategic and coercive decision loops, with jointly verified limits and drilled fallback capacity ($\mathcal K\ge\mathcal K_{\min}$). Among actors who price in the lock, it is a strict equilibrium (Proposition 5.5).
  - *Broad form:* AI not used as an instrument in any contest that tends toward dominance or concentration, such as labour, finance and persuasion. The broad form needs its own action space and analysis; Proposition 5.5 does not cover it.
  - Competition in products, science and service that does not concentrate is not excluded.
  - The narrow form differs from keeping AI out of the whole conduct of the contest alone while others race. That can be worse than joining: if staying out raises the rival's decisive chance from $1-\varepsilon$ to $1-\varepsilon^2$, survival falls from $\varepsilon(1+\varepsilon)/2$ under joining to $\varepsilon^2$ [N]. This is why E1 must be held in common, and why it begins with decision loops.
- **E2: Stop.** Capability of the decisive class (artificial superintelligence, recursive self-improvement) is not built while the conditions for governing it are absent. Those conditions are social, and they are conditions of mind: a shared self-understanding, the accurate self-model of Section 4.3, and the shared prediction of Section 8.2. Where capability already outruns coverage, it is rolled back.
  - Stopping is a choice in its own right, not a slower form of E3.
  - Where hazardous variety already exceeds coverage, stopping or rolling back is the fastest way to end exposure (Proposition 5.9).
  - Its cost, if AI turns out not to be decisive, is the delay of benefits: bounded and recoverable. If it is decisive, the loss it avoids is irreversible. That is the classical asymmetry of irreversibility (Arrow and Fisher 1974; Henry 1974).
- **E3: Develop at the pace of understanding.** Two conditions, used by different results:
  - (E3-i) the uncovered hazardous share is summable (Theorem 5.8). Coverage need not ever fully catch up;
  - (E3-ii) each hazard mode keeps the robustness margin of Proposition 5.7(3).

  Development directed at need has a point of enough and meets E3 of itself. What E3 constrains is compounding without a point of enough.
- **Temporary pause.** A training pause of fixed length is valued by what changes during it (Proposition 4.5). With no relevant change, resumption repeats the same process. A pause that insulates rule-making and builds the conditions of Definition 4.6 is a different policy.

**The order.** E1 first: it keeps humans as the players, and it is the one exit that is a strict equilibrium among informed actors without trust. If E1 cannot be had, E2 or E3. Stop before building the decisive class, so that cooperation becomes possible and can be thought through, and build what is more complex afterwards; or bring the speed of development below the speed at which understanding, and the response it makes possible, can follow. After coverage has caught up, (E3-i) remains a standing condition under any arrangement.

**Feasibility.**
- Each actor can take part of E1 alone, and taken verifiably it is the signal of Proposition 8.4.
- E2 and E3 are the most verifiable among rivals, because chips, fabs, datacentres and compute can be observed. Algorithmic progress erodes thresholds stated in compute: with efficiency doubling about every eight months, a nominal cap must tighten roughly two and a half to three times a year (E9). That is a rate condition verification must meet.
- E1 is the hardest to verify, since it concerns software and internal procedure. It is also self-enforcing among informed actors, which is why it can begin as a norm.

### 8.4 A staged pathway

The pathway below is a candidate to be tested, not a claim that every setting should follow it. Civilian services, frontier development and strategic decision-making may need different paths: shared provision can lead in the first, measurement and tempo in the second, narrow E1 in the third.

| Stage | Actors | What is committed | What each gains | What each concedes | Incentive to deviate | Interim vulnerability | Response to breakdown |
|---|---|---|---|---|---|---|---|
| 1. Shared account of hazards and measurement | Scientific panels, national evaluators, developers, independent researchers | A common taxonomy of hazards; shared measurement of coverage and residual risk per class; disagreements and uncertainty recorded | Better information at low cost | Evaluators' access to data; publication of methods | Withholding and shading (Prop 8.3); gaming of measures (masking) | Little | Unilateral publication; independent replication |
| 2. Narrow, testable commitments in one domain | Heads of government; military commands; developers for evaluation access | Human authorization in strategic decision loops, with inspection of doctrine and exercises; use of an incident channel; pre-deployment access above thresholds | A strict equilibrium among informed actors (Prop 5.5); fewer mistaken preventive strikes | Inspection; drills of fallback capacity | Speed advantage for relative types; reduced by making the commitment a costly signal (Prop 8.4) | Low, since informed actors prefer it alone | Public notice; suspension of cooperation in other domains; return to Stage 1 |
| 3. Fund correction and shared services | Participating states; providers; evaluator network | A formula levy; independent evaluators with mandated access; shared services with continuity guarantees; reward separated from authority over correction | Services; capacity for less-resourced participants; a credible certificate (Prop 3.10) | Contributions; providers give up rights over evaluators and rules | Free riding; attempts at influence (Section 3) | Participants paying the levy compete against non-participants; met by coverage and conditions of market access | Escrowed funds; portable evaluators; services continue |
| 4. Staged change of delegation, access and decision rights | All participants | Broader E1; tempo thresholds (E3); common frontier projects in chosen domains (Prop 7.5); drilled fallback capacity | Lower value of winning; shared benefits | Leverage given up before verification is complete | Largest here: the value of winning (Thm 6.7, Prop 6.6) | High, met by reciprocal, staged and reversible steps, escrow and tripwires | Reversion plans that keep the institutions of Stages 1–3 |
| 5. Broaden as institutions prove themselves | All, including new entrants | Expansion by evidence: R1–R6 and D1–D6 met under stress | A cooperative order | — | Diminishing as the value of winning falls | — | Contraction to the stage last shown to work |

Three groups need standing at every stage, because they cannot leave the shared exposure:
- smaller jurisdictions;
- users;
- people who depend on services controlled by others.

The affected persons' chamber and the service guarantees of Section 7.7 are how they get it.

**Where things stand.** Stage 1 has seeds: an international scientific assessment of AI safety (2026), and a UN scientific panel with a global dialogue created by consensus in 2025. Stage 2 has seeds: leading states' affirmation of human control over the decision to use nuclear weapons (2024), and a bilateral dialogue on superintelligence risk with an incident channel (September 2026). In the same period binding constraints were explicitly rejected, and developers' written commitments became more contingent on rivals [O: E2, E8]. The transition does not have to start from nothing. It has to make these seeds binding, verifiable and broader before the relevant losses or lock-in (Lemma 5.4).

### 8.5 Requirements of a cooperative path

**Proposition 8.5 (Requirements of a cooperative path) [T].** *A cooperative path has four separate requirements, and what is shown for each differs.*
1. *Existence of an incentive-compatible cooperative state. In the construct of Proposition 7.5 with a moderate value of winning, all cooperating is a strict Nash equilibrium; whether it is risk-dominant depends on the parameters. Theorem 7.2 gives safeguards sufficient for viability once in force. That is viability, not incentive compatibility.*
2. *Reachability: on the path, every participant prefers to continue given its beliefs. In the actors' objectives this needs trust above $\varpi^\ast$ (Proposition 8.1). In survival terms the threshold can be small at the horizons that matter (Proposition 5.14), within the sign conditions stated there. Narrow E1 needs no trust among informed actors (Proposition 5.5). That graduated steps alone reach the threshold is not shown.*
3. *Survival during the transition. The host must stay above its floor during the transient (Theorem 7.2(1)), and the path must not pass a point of no return before the arrangement takes hold (Lemma 5.4).*
4. *Persistence. It needs commitment that keeps pace with the net exit gain, or that gain falling (Proposition 6.6); correctors with full row sums below one (Proposition 7.7); and rules fixed before capture (I4).*

### 8.6 Precedents

The nuclear and biological records show what has made cooperation among rivals work and fail.

| Precedent | What made it work or fail | What it shows |
|---|---|---|
| The Acheson–Lilienthal report and the Baruch plan (1946) | International ownership of the dangerous activity was proposed. It failed on sequence: the leader would keep its monopoly until control was in place, and the laggard wanted the leader to give it up first (Bundy 1988). | The transition must come before the lock |
| The first nuclear monopoly (1945–49) | Preventive war was seriously argued within the leading side and not carried out. The advantage was not decisive, conventional forces balanced it, and norms and domestic constraints held (Trachtenberg 1988/89; Tannenwald 1999). | Restraint where P1 and P3 failed |
| The ABM Treaty (1972) | Reciprocal limits on defences were adopted to reduce the offensive arms race and the risk of war, with limited deployments allowed and periodic review. Capabilities judged decisive, such as multiple warheads, were not limited, and the treaty was later abandoned. | Reciprocal constraint can change the value of extra advantage, not only follow from its low value; durability fails when the value of winning rises again |
| Test bans | The partial ban forbade atmospheric, space and underwater tests while underground testing continued; its motives were fallout and non-proliferation. | Not a stop of the decisive class |
| The Outer Space and Seabed treaties | Domains were excluded from the deployment of weapons of mass destruction. | A domain kept out of the contest, close to E1 |
| The Biological Weapons Convention (1972) | A weapon hazardous in development, uncontrollable in use and dangerous to its holder. One party renounced it unilaterally on grounds of uncontrollability and low military value, while another kept a large covert programme under the convention (Leitenberg and Zilinskas 2012). | A weapon that endangers its holder can be given up unilaterally; and without verification the hard case persists |
| The Non-Proliferation Treaty and counter-proliferation | Great powers cooperated to limit others (Coe and Vaynman 2015). Preventive strikes on others' programmes were considered, and carried out against weak states (Burr and Richelson 2000/01). | Partial coalitions enforcing a stop on outsiders; the hard case answered by coercion |
| The stability–instability paradox | Stability among decisive weapons can intensify competition below them (Snyder 1965). | A stop of the decisive class can push competition into cyber operations and influence, the domain of broad E1 |

Two further facts qualify the record. The Cold War ended by the internal collapse of one side, not by agreement. And its hazards fell with learning (Nye 1987), the case in which residual risk becomes summable. Rivals survived when nature supplied saturation, and gave up capabilities by agreement when reciprocal limits made the extra advantage worth less. AI lacks the first: P3 is the racers' own premise. So safety must come from the second.

### 8.7 Readiness to resume, applied

For frontier training today, the dimensions of Definition 4.6 stand as follows [O].
- **R1 technical reliability.** Capability is measured; residual risk per hazard class is not. Evaluated systems detect evaluations above chance (E5–E7).
- **R2 shared objectives.** Declared objectives include race framings, alongside cooperative ones (E1).
- **R3 strategic incentives.** The value of winning is not lowered by benefit sharing or a common frontier; commitments are conditioned on rivals (E2).
- **R4 effective correction.** Evaluation bodies have shifted toward industry contact under voluntary access. No certificate of independence exists (E3).
- **R5 deployment constraints.** No binding tempo exists; written thresholds are revised, mostly toward weakening (E2).
- **R6 retained human agency.** Human control over nuclear use is affirmed (E8); fallback drills elsewhere are not reported.

On these indicators, resuming unchanged after a pause would repeat the process that made the pause necessary.

---

## 9. The warranted decision and its cruxes

### 9.1 The judgment

**[R]** Under decision standard D, given the present evidence, a cooperative change of course is warranted now. The order:
1. Keep AI out of strategic and coercive decision loops, verifiably and with drilled human fallback (E1, narrow form).
2. Do not build capability of the decisive class while the conditions for governing it are absent. Develop at the pace that correction can follow (E2 or E3, as distinct choices).
3. Build in stages an arrangement with the functions of Section 7.7: shared measurement, independent and formula-funded correction, shared provision of useful services, reward separated from authority over correction, answerability to those affected, and rule-making insulated from success.

The first steps are those of Stages 1 and 2 of Section 8.4, and their seeds already exist.

### 9.2 Why

The judgment follows a chain, each link with its own support.
1. **The trajectory has one root.**
   - Its dynamics follow from the winning model Ψ: the isolated self, naive Darwinism and winner-take-all compounding (Section 1.2) [D].
   - Inside Ψ the race is the rational game. Under the inclusive self-model, the same material situation is a problem of coordination (Propositions 1.2, 1.3) [T].
   - With growing contested stakes, and harm per unit that correction cannot drive to zero, survival needs the self-model to close on the inclusive one faster than the stakes grow (Proposition 1.4, under A_G) [T].
   - Ψ is false about interests, evolution and behaviour (E13, E14) [O]. It governs by self-confirmation, performativity, selection, the status drive and its history (Section 1.5) [O, C].
2. **Success can buy control over future selection.** When the benefits of influence over correctors are appropriable, persistent and large relative to cost, that influence is selected, scaling with the square of share. Correction is a public good not supplied from inside, and must grow at a rate set by the falling cost of control. Reforms that leave the channels in place are re-absorbed (Section 3) [T]. The channels are partly visible today (E3) and not yet measured (E4).
3. **Faithful AI does not resolve a harmful human game, and the game's objective reproduces.** Principal alignment makes each principal's chosen game more effective (Proposition 4.1) [T]. Relative objectives are favoured in selection on actions, in commitment among observable actors, and plausibly in the selection of decision-makers (Section 4.3) [T, C]. Declared objectives and written safety commitments on the present path are set relative to rivals (E1, E2) [O].
4. **AI changes the stakes and the timing.**
   - Decisive contests dissipate their prize (Proposition 5.2).
   - Delegation pressure arrives below decisive capability (Proposition 5.3).
   - Correction loses robustness against modes faster than its delay allows (Proposition 5.7).
   - Inside the contest, safety gains on stable branches are absorbed by more delegation (Proposition 5.13) [T].
5. **If hazardous variety outgrows contestable coverage on the continuation path, survival decays** (Theorem 5.8) [T]. Capability compounds today (E5); whether hazardous variety and residual risk do is not measured (crux C1).
6. **Continuation policies do not meet standard D without changing what they continue.** Each was given its best case (Section 6). Those that succeed do so by changing W or C: binding tempo across all actors, separating evaluators from success, or lowering the value of winning. That is a change of governing model, a pivot.
7. **A cooperative design can be specified, stress-tested and reached in stages** (Sections 7–8). Its own hazard of breakdown is not known (crux C4).
8. **Therefore**, under a standard that protects irreversible losses first and applies the same uncertainty to every path, the pivot is preferred. No evidence today excludes the case in which correction falls behind on the present path, and the cooperative path does not require that case to hold in order to be worth taking.

### 9.3 The cruxes

| Crux | What it is | Present evidence | What would change the recommendation | Next measurement |
|---|---|---|---|---|
| C1 Residual risk after correction | Whether hazardous variety outgrows contestable coverage, and whether residual irreversible risk stays nonsummable on the present path ((X), (U), (φ)) | Capability compounds (E5); evaluation awareness exists (E6); the state of the science calls safeguards incomplete (E7). Hazardous variety and residual risk are unmeasured | Measured residual risk per hazard class falling over generations under present incentives; catch rates of planted defects at fixed human hours holding as capability rises | Predefined hazard modes per class; coverage units; residual-risk estimates by independent evaluators |
| C2 Conversion of success into control | The size of the channels $b_{ij}$ and $\chi$ by which success buys influence over evaluators and rules | Mandates and access shifting toward the evaluated (E3); not measured (E4) | Effective correction surviving unchanged dependence; influence explained by expertise without impairment of an entrusted purpose | Funding, appointment and access terms of evaluators; authorship of standards and benchmarks; series for $x_i$ (Section 3.8) |
| C3 Whether AI scales contestable coverage | Whether AI raises the productivity of contestable understanding as fast as it raises hazardous variety | Open. Symmetric with whether AI cheapens independent correction as fast as control (Proposition 3.6(4)) | If it does, the case for slowing weakens, while the case for separating evaluators from success remains | Control evaluations and auditing games at fixed human hours across capability levels |
| C4 Durability of cooperative institutions | The hazard of breakdown and capture of the arrangement itself; enforcement against the strongest participant | Precedents mixed (Section 8.6); seeds of dialogue with binding constraints rejected (E8) | A cooperative design that fails its own stress tests worse than a credible continuation policy | Stress tests of pilot institutions; durability of Stage 1–2 commitments |
| C5 Decisiveness and saturation | Whether AI advantage is decisive and non-saturating (P1, P3) | Racers' declared premise (E1); not established | Saturating advantage moves the contest to Branch I′, where it can stabilize, while hazards in development remain | Whether leads convert into lasting dominance |
| C6 Whether institutions widen the effective self | Whether sharing what is contested, separating reward from control over correction, and lowering decisiveness change conduct where actors value their own absolute payoffs, and how far relative selection persists (Propositions 1.4, 1.5) | Conditional cooperation is the modal type in experiments (E14). Among a few frontier actors with public doctrines, relative objectives are favoured (Proposition 4.2) | Conduct unchanged under substantial sharing. That would point to relative selection, and require changing what winning converts into before sharing can work | Conduct under pilot benefit-sharing and common-frontier arrangements; the decisiveness of present contests |
| N1 Discounting and risk attitude | Whether to discount the protected outcomes, and whether to use expected value | — | A discounted or expected-value criterion that values the benefits of speed highly can prefer continuation (Section 5.6) | A normative choice, to be stated by each reader |
| N2 The weight of agency | Whether loss of human decision authority (O2) is protected as strongly as loss of life (O1) | — | Weighting O2 below welfare gains weakens the case for narrow E1 | A normative choice |

If C1 and C2 were both measured and favourable, the diagnosis of the present path would weaken. If C4 were measured and unfavourable, the particular design of Section 7 would be rejected, without vindicating the race; another cooperative design would be needed.

### 9.4 What would redirect the argument

Three outcomes would redirect it, and they are classified before seeing them.
1. **Correction demonstrably scales.** Contestable coverage keeps pace with hazardous variety under present incentives, and residual risk falls. This weakens the diagnosis. If it requires separating evaluators from success, it is a pivot; if not, it is a successful continuation, and the theory was wrong about C1.
2. **An implementable safeguard makes continuation adequately safe.** A safeguard installed without changing W or C meets standard D. This weakens the case for a pivot. If the safeguard binds every capable actor's tempo to correction, it is a pivot under another name.
3. **The cooperative design performs worse.** A stress-tested cooperative design fails worse than a credible continuation policy. This rejects that design, not the case for leaving the race; it calls for another design.

### 9.5 Predictions

Each prediction is stated so that it could fail.
- When a rival releases a high-risk system, written safety requirements that are conditioned on rivals' conduct are relaxed more often than they are tightened (E2).
- Incumbents support correction that is keyed to them and oppose correction that is non-appropriable, most strongly where their exposure to shared harm is low and their rents are high (Section 3.8).
- In deployed delegation, safety improvements reduce risk per useful output, but aggregate realized risk falls less, or not at all, until delegation saturates (Proposition 5.13).
- If (U) holds, catch rates of planted defects at fixed human hours fall as capability rises; if they do not, (U) is refuted for the class measured.
- An initially better safety protocol loses its advantage when success changes who evaluates it, but not when evaluators' rights are protected (Study B below).

### 9.6 Research program

The author's pilot experiment on the mechanism of Section 3 ran once with 20 seeds. P1 failed and P2–P4 held; the failure is attributed to too few lineages and to drift (E12). Design 2 is specified and has not been run. Four further studies would discriminate the mechanism from its alternatives.
- **Study A.** Repeated selection with an endogenous evaluator. It compares a fixed selector, a selector that drifts by a matched amount, and a selector shaped by success. Outcome measures are independent of the selector, capture is optional, interference costs something, and correction is given room to succeed.
- **Study B.** An initial safety improvement crossed with later power to amend evaluation. The question is whether the improvement's long-run effect depends on whether evaluators' rights are protected.
- **Study C.** Human procurement and governance of evaluators: appointment, funding and turnover under success.
- **Study D.** Shared infrastructure under asymmetric dependence: enforcement against the leading provider, continuity of service, appeal.

A simulator that rewards capture directly establishes only its programmed mechanism. Each study needs independent outcome measures and real alternatives. None is a prerequisite for the practical judgment, which rests on the decision standard and the evidence; each would strengthen or weaken a specific link.

### 9.7 Conclusion

The actors developing advanced AI share conditions that none of them prices, and they are coupled to one another in a system none can leave. Selection on who is ahead does not register those conditions. Success can be converted into control over the rules and correctors that will judge the next round, and when that conversion is appropriable and persistent, it is selected. Correction is a public good that competitors do not supply. Local reforms that leave the channels in place are absorbed.

Aligning each AI to its principal does not resolve this, and neither does keeping humans in every final decision. A faithful instrument makes the game its principal plays more effective. When the game rewards winning over shared conditions, a better instrument deepens the loss. A pause gives time to change the game; time alone does not change it.

Where the prize is decisive and fast:
- the race consumes its prize;
- pressure to delegate arrives before decisive capability;
- correction falls behind modes faster than its delay;
- safety gains inside the contest are largely absorbed by more delegation.

Whether the residual danger becomes permanent depends on whether correction keeps pace with the hazardous behaviour it must cover. That is the central uncertainty, and no evidence today settles it in favour of the present path.

Each alternative that keeps the contest succeeds, where it succeeds, by changing what it keeps: binding tempo to correction, separating evaluators from success, lowering the value of winning. Those changes, made together and by every capable actor, are the cooperative change of course this paper argues for. The change does not need to start from nothing. Shared assessment, narrow commitments on strategic decisions and channels for incidents already exist. They need to become binding, verifiable and broad before the relevant losses or lock-in.

Beneath these mechanisms lies one governing model: the isolated self, a world read as a contest that certifies its winners, and advantage that compounds until one side takes all. Inside that model the race is rational, and every safeguard is a parameter to be re-absorbed. The model is false about the actors' own interests, about evolution and about human beings. It governs anyway, for four reasons:
- it confirms itself;
- it makes itself true through the institutions built from it;
- it recruits the drive for status;
- it selects its holders.

Growth makes the model more costly. As the stakes of the technology rise, the share lost to separateness rises with them. Survival then requires that the boundary each actor draws around itself close faster than the stakes grow. Institutions can begin that change before every mind does:
- by sharing what is contested;
- by rewarding contribution rather than domination;
- by keeping correction in common hands.

To understand ourselves as one interconnected system is not a sentiment added to the analysis. It is what the analysis requires if growth and change are to continue.

AI is a planetary technology. Its purpose can be shared flourishing: useful services, scientific progress, competent and answerable authority, and human agency kept in the decisions that matter. What has to be agreed is not who comes first, but what every actor needs in order to go on, and how the means of correction stay in common hands.

---

## Appendix A. Assumptions and proofs

### A.0 Maintained assumptions

Each assumption is listed with what changes if it is dropped.
- (A1) Exposure to the host is shared, so $G$ is common to all payoffs. Remark 2.7 treats unequal exposure.
- (A2) Field size is fixed. With entry driven by absolute profit, the host settles where rents dissipate, and C0 must hold at that equilibrium.
- (A3) Conversion is monotone ($b_{ij}\ge0$), so countervailing pressure enters only through correction $d$ (Remark 3.7).
- (A4) Costs of control are convex and fall with AI. A fixed part that AI does not lower caps the requirement (Proposition 3.6(5)).
- (A5) Reports are averaged and non-strategic. Remark 3.9 treats conservative and disjunctive alarms.
- (A6) There is one practice and its alternative per domain; payoffs are linear; parameters are uncalibrated.
- (A7) Contest models are symmetric unless stated.
- (A8) In the bargaining model of Proposition 6.4, after a shift in power the side that gained the advantage sets the terms each period, and the other accepts or fights. Proposition 6.4(3) shows what changes under other protocols.

Symbols are local to their section where a family would otherwise collide. Hazardous variety is $Y$, contestable coverage $U$, the uncovered share $\mathsf u_t$, and the rate of correction of rule support $d$; these are distinct quantities.

### A.1 Section 1

**Proposition 1.2.**
1. Each $\pi_j$ appears in $n-1$ of the averages $\bar\pi_{-i}$, each divided by $n-1$, so $\sum_iO_i=\sum_i\pi_i+\theta\sum_j\pi_j$.
2. Adding $\Delta$ to every material payoff adds $\Delta$ to $\pi_i$ and to $\bar\pi_{-i}$, so $O_i$ changes by $(1+\theta)\Delta$, while the total changes by $n\Delta$.
3. At $\theta=-1$, part (1) gives $\sum_iO_i=0$ at every profile. If every objective were strictly higher at one profile than at another, the sums would differ, so no profile is better for every actor. Part (2) gives a zero change for any common term. At $\theta=n-1$, $O_i=\pi_i+\sum_{j\ne i}\pi_j$, the total. At a profile that maximizes the total, no unilateral deviation raises the total, and so none raises any objective. Common-interest coordination games show that inefficient equilibria can remain. $\square$

**Proposition 1.3.**
1. Switching $a_i$ from $0$ to $1$ changes $u_i$ by $\epsilon b-c-\epsilon d$, and each other $u_j$ by $-\epsilon b/(n-1)-\epsilon d$, so $\bar u_{-i}$ changes by the same amount. The change in $O_i$ is $\epsilon b-c-\epsilon d+\theta\big(-\epsilon b/(n-1)-\epsilon d\big)$, independent of the others' choices.
   - It is linear in $\theta$ with slope $-\epsilon(b/(n-1)+d)<0$, and it vanishes at $\theta^\ast$.
   - At $\theta=n-1$ it equals $-c-n\epsilon d<0$, so $\theta^\ast<n-1$.
   - Writing $\theta^\ast=(b-d)/(b/(n-1)+d)-c/\big(\epsilon(b/(n-1)+d)\big)$ shows that it rises with $\epsilon$ to the stated limit.
2. Proposition 4.2(1) gives $e(\theta)\to0$ as $\theta\to n-1$. At the symmetric equilibrium the win probabilities sum to one, so the total material payoff is $\Omega-nec-n\ell(ne)=\Omega-ne(c+n\ell)$. Substituting $e(\theta)$ in $D=ne(\theta)(c+n\ell)$ gives the formula.
3. With stakes $s\Omega$ and shared loss $s\ell$, the dissipated share is $r(n-1-\theta)(c+ns\ell)/\big(n(c+(1+\theta)s\ell)\big)$.
   - Its derivative in $s$ has the sign of $n\ell\big(c+(1+\theta)s\ell\big)-(1+\theta)\ell(c+ns\ell)=c\ell(n-1-\theta)>0$ for $-1<\theta<n-1$.
   - Its limit as $s\to\infty$ is $r(n-1-\theta)/(1+\theta)$. Because the share rises toward this ceiling, the total is positive at every scale if and only if the ceiling is at most one, that is, $\theta\ge(r(n-1)-1)/(1+r)$.
   - $d\theta_g/dr=n/(1+r)^2>0$.
   - At $\theta=-1$, $e=r\Omega/(nc)$, and the share is $r(c+ns\ell)/c$. $\square$

**Proposition 1.4.** Total intensity is $\mathcal E_t=ne(\theta_t)$, with $\Omega_t$, $r_t$ and $L_t$ in place of $\Omega$, $r$ and $\ell$; this gives the formula for $q_t=aL_t\mathcal E_t$. Survival through round $N$ is $\prod_{t\le N}(1-q_t)$. With $q_t\in[0,1)$, the product has a positive limit if and only if $\sum_tq_t<\infty$:
- $\ln(1-q)\le-q$ gives "only if";
- $-\ln(1-q_t)\le2q_t$ once $q_t\le1/2$ gives "if".

Then:
1. $L/(c+(1+\theta)L)<1/(1+\theta)$ gives $q_t\le ar_t\Omega_t(n-1-\theta_t)/\big(n(1+\theta_t)\big)$.
2. $L/(c+(1+\theta)L)$ rises with $L$, and $1+\theta\le n$, so it is at least $L_{\min}/(c+nL_{\min})$. With the bound of (1) and $1+\theta_t\ge1+\theta_{\text{low}}$, $q_t$ lies between two positive multiples of $r_t\Omega_t(n-1-\theta_t)$.
3. At $\theta_t=-1$ the formula gives $ar_t\Omega_tL_t/c$. $\square$

**Proposition 1.5.** Pooled payoffs are $\pi'_j=(1-\beta)\pi_j+\beta\bar\pi$, with $\bar\pi=(\pi_i+(n-1)\bar\pi_{-i})/n$, so $\bar\pi'_{-i}=(1-\beta)\bar\pi_{-i}+\beta\bar\pi$. Then
$$O_i=\pi'_i+\theta_0\bar\pi'_{-i}=\Big[(1-\beta)+\tfrac{\beta(1+\theta_0)}{n}\Big]\pi_i+\Big[\theta_0(1-\beta)+\tfrac{\beta(1+\theta_0)(n-1)}{n}\Big]\bar\pi_{-i}.$$
For $\theta_0>-1$ the first coefficient is positive, and dividing by it gives $\theta_{\text{eff}}$.
1. With $A=(1+\theta_0)/n>0$, the derivative of $\theta_{\text{eff}}$ in $\beta$ has the sign of $A(n-1-\theta_0)$, which is positive for $\theta_0<n-1$. At $\beta=1$ the ratio is $(n-1)A/A=n-1$.
2. At $\theta_0=-1$, $A=0$ and $O_i=(1-\beta)(\pi_i-\bar\pi_{-i})$. A positive multiple of every objective leaves best responses and equilibria unchanged. Under replicator dynamics, $\pi'_k-\pi'_l=(1-\beta)(\pi_k-\pi_l)$, so relative growth rates and the cumulative advantage of Proposition 2.4(3) scale by $1-\beta$, and divergence of the cumulative advantage is unchanged. $\square$

### A.2 Section 2

**Lemma 2.3.** A relative rule satisfies $F(p,\pi+G\mathbf 1)=F(p,\pi)$ at every instant, so the shares solve the same equation whatever $G(V(t))$ is. A common term leaves every $\pi_k-\pi_l$ unchanged, and with it the sign of $\dot p_k/p_k-\dot p_l/p_l$ under a payoff-monotone rule.

**Proposition 2.4.**
- (1) With $\phi_k=\phi_l$, $\pi_k-\pi_l=(\nu-\tau_{\text{eff}})(e_k-e_l)>0$, and $G$ cancels.
- (2) Under replicator dynamics $\dot p_k=p_k(\pi_k-\bar\pi)$, so $\dot E=\operatorname{Cov}_p(e,\pi)$, which expands to the stated form. In the example, shares $1/3$, $e=(0,0.9,1)$, $\phi=(0,10,0)$ and $\nu=1$ give $\pi=(0,10.9,1)$ and $\bar\pi=3.967$. Then $\dot E=1.0911$, while $\dot p_3=p_3(\pi_3-\bar\pi)=-0.9889$ (`checks_v5.log`, CAP).
- (3) The identity follows from (2). If $B(t)\to\infty$, then $\ln(p_k/p_l)(t)\to\infty$ for a race carrier $k$ and any $l$ with $e_l<\bar e$, so $E\to\bar e$. For $\epsilon>0$, eventually $\dot V\le V[\rho(1-V/K)-h(\bar e-\epsilon)]$, so $\limsup V\le K(1-h(\bar e-\epsilon)/\rho)^+$; let $\epsilon\to0$. C0 gives $K(1-h\bar e/\rho)^+<V_{\min}$.
- (4) If $B(\infty)<\infty$, each $\ln(p_k/p_l)$ converges.

**Proposition 2.5 and Remark 2.6.**
- With $\bar\pi=\frac1n\sum_j\pi_j$, $\pi_k-\bar\pi$ gives $G(V)$ weight zero. Hence $u_k=w_\lambda\nu e_k-\frac\lambda n\nu\sum_{j\ne k}e_j+\omega K(1-hE/\rho)+\text{const}$ with $E=\frac1n\sum_je_j$.
- $\partial u_k/\partial e_k=w_\lambda\nu-\omega Kh/(n\rho)$ does not depend on others' choices: this gives (1).
- Joint payoff at a common $e$ has slope $n\nu(1-\Theta)$, which gives (2). Payoffs are $\nu\bar e+\omega K(1-h\bar e/\rho)$ at full depletion and $\omega K$ under restraint, which gives (3).
- In Remark 2.6, a pivotal developer compares $L$ with its gain $(w_\lambda-\Theta/n)\nu\bar e$. Under grim reversion restraint is sustained iff $u_c\ge(1-\delta)u_d+\delta u_N$, with $u_d-u_c=\nu\bar e(w_\lambda-\Theta/n)$ and $u_c-u_N=\nu\bar e(\Theta-1)$.

### A.3 Section 3

**Remark 3.2.** The characteristic polynomial is $(\lambda-1+\mu)(\lambda-1+\delta)-ab=0$, with roots $1-\frac{\mu+\delta}2\pm\sqrt{\frac{(\mu-\delta)^2}4+ab}$. The larger root is below one iff $\sqrt{(\mu-\delta)^2/4+ab}<(\mu+\delta)/2$, that is, iff $ab<\mu\delta$. The smaller root must also exceed $-1$, which holds for $\mu,\delta\le1$ unless $ab$ is large. `checks_v5.log` (FB) confirms the condition on random draws.

**Proposition 3.4.**
- Appropriable support keyed to the carrier obeys $\dot z^\chi_i=\varepsilon_i(\chi q\sum_j\hat b_{ij}y_j-d_iz^\chi_i)$ from $0$. Its horizon average is $z^{\chi\ast}_iL_i$, with $z^{\chi\ast}_i=\chi q\sum_j\hat b_{ij}y_j/d_i$ and $L_i=1-(1-e^{-\varepsilon_id_iT_h})/(\varepsilon_id_iT_h)$.
- The per-decision advantage $a_iz^\chi_i$, weighted by $y_i$ and summed, gives $\chi q\,y^\top My$; shared support cancels; $y^\top My=p^2\bar y^\top M\bar y$.
- (1) Differentiate. Under replicator dynamics with faithful transmission, $\dot{\bar q}\propto\operatorname{Cov}(q,\Delta\pi(q))$ (Price 1970).
- (2) With $f>0$, $\Delta\pi'(0)>0$ iff $p>p^\ast$, and for $p<p^\ast$, $\Delta\pi(q)<0$ for all $q>0$.
- (3) $c_iL_i\hat R_{ij}=a_i\hat b_{ij}\varepsilon_iT_h\,\ell_L(\varepsilon_id_iT_h)$, with $\ell_L(v)=[1-(1-e^{-v})/v]/v$ decreasing.
- (4) Sum over $\mathcal S$; at fixed total size substitute $p=Y/|\mathcal S|$.

**Proposition 3.5.**
- (1) Two carriers that differ only in $u$ are affected identically by the change in $d$, and their payoff difference is $C_u(u_l)-C_u(u_k)<0$ for $u_k>u_l$.
- (2) At fixed $V$, a carrier's support declines in $d$.
- (3) A challenger invests only if its share of the benefit exceeds $C_u'(0)$.
- (4) The keyed part has the form (4); capture needs the row-sum condition of Proposition 3.10.
- (5) Compare $\nu\bar e(\Theta-1)$ with the lost rent.

**Proposition 3.6.**
- With $L_i=1$ and uniform $d$, $M=\hat A/d$ and $q^\ast=(\chi\hat Y/(\gamma d))^{1/\eta}$. Then $s_{\mathsf E}=A/(c_{\mathsf E}d)+Z_\eta\gamma^{-1/\eta}d^{-(1+\eta)/\eta}$, strictly decreasing in $d$: this gives (1). For $\eta=1$, $s_{\mathsf E}<1$ iff $c_{\mathsf E}d^2-Ad-Z>0$. Part (2) follows.
- (3) Along $\gamma_0e^{-gt}$ and $d_0e^{\alpha t}$, the first term is nonincreasing and the second is proportional to $e^{(g-(1+\eta)\alpha)t/\eta}$. Once $x_j\ge\frac12$ on $\mathcal C$, $q^\ast$ grows as $e^{(g-\alpha)t/\eta}$, and integrating (3) gives $a_{\mathsf E}z_{\mathsf E}(t)\ge c\,e^{(g-(1+\eta)\alpha)t/\eta}$, so $\operatorname{logit}x_{\mathsf E}\to\infty$.
- (4) $d$ is budget divided by unit cost.
- (5) With $f>0$, $q^\ast=0$ when $d\ge\chi\hat Y/f$.
- (6) $L_i\approx\varepsilon_id_iT_h/2$ while $\varepsilon_id_iT_h\ll1$.
- (7) Parts of share $1/k$ each have $\hat Y/k^2$, so $q^\ast$ is divided by $k^{2/\eta}$. The cultivated term becomes $Ck^{-2/\eta}e^{(g-(1+\eta)\alpha)t/\eta}$, which reaches a given level later by $\Delta t=2\ln k/(g-(1+\eta)\alpha)$ when the exponent is positive.
- (8) $q_k^\ast\propto p_k^{2/\eta}$ at given $d,\gamma$, and conversion is proportional to $p_kq_k^\ast$; sum over $k$.

**Proposition 3.8.**
- (1) $\tilde V$ increases in $V$ and equals $V_{\text{alarm}}$ at $V=(V_{\text{alarm}}-mK)/(1-m)$.
- (2) For $V_{\min}\le V\le V_{\text{alarm}}$ and $m>m_{\text{fl}}$, $\tilde V\ge V_{\min}+m(K-V_{\min})>V_{\text{alarm}}$.
- (3) $\tilde V\ge V^\ast+\bar m(K-V^\ast)>V_{\text{alarm}}$.
- (4) $\tilde V\le m_1K+V$ eventually.
- (5) $V$ must fall from $V_{\text{alarm}}$ to $(V_{\text{alarm}}-mK)/(1-m)$.

Remark 3.9(1): at $V=V_{\text{target}}$ and $m\le\beta_{\text{in}}$, $\tilde V\le a_{\text{al}}$; by continuity the report reaches $a_{\text{al}}$ no later.

**Field lemma.** $[0,1]^D\times[0,\infty)^D$ is forward invariant, $\limsup_tz_i(t)\le\sum_jb_{ij}/d_i$, and the system (3) is cooperative, so the flow preserves the componentwise order (Hirsch 1985; Smith 1995).

**Proposition 3.10.**
- (1) At $Z_{\mathcal C}$ the Jacobian is block lower-triangular, with diagonal entries $\mp\zeta_ic_i(s_i(\mathcal C)-1)$ and $-\varepsilon_id_i$.
- (2) By the field lemma, eventually $a_iz_i-c_i\le c_i(\sum_jR_{ij}-1)/2<0$.
- (3) Take $R_{i1}>1$ for $i\ne1$, $R_{12}>1$, and all other off-diagonal entries zero.
- (4) Pruning.

**Proposition 3.11.** (1) By induction on the hull, using a lower bound on rule support. (2) By comparison, then pruning. (3) Is (1) with $\mathcal C'$ as seed.

**Proposition 3.12.**
- The frozen share drives $z\to b_px_p/d$. The equilibria are $(0,0)$, $(1,b/d)$ and the saddle $(1/R,c/a)$.
- $\mathcal V=axz-cx-\frac{ad}{2b}z^2$ is nondecreasing along solutions, so every solution converges to an equilibrium, and the stable manifold of the saddle separates the basins.
- The point $(x_p,bx_p/d)$ lies on the nullcline through the saddle, and $\sigma(0)>1/R$ by strong cooperativity.

**Theorem 3.13.**
- By C1 and Proposition 2.4(3), load tends to $\bar e$ and $V$ declines toward a limit below $V_{\min}$ unless an alarm triggers liability.
- By C3 and Proposition 3.6(3), $x_{\mathsf E}\to1$.
- By C6, $m(t)>m_{\text{fl}}$ throughout the band, so no alarm fires before $V<V_{\min}$ (Proposition 3.8(2)).
- $T_A$ follows by comparison with the logistic solution at rate $\rho-h\bar e$.

### A.4 Section 4

**Proposition 4.1** is proved in the text.

**Proposition 4.2.** Expanding, $O_i=\Omega(1-\frac{\theta}{n-1})w_i-(c+(1+\theta)\ell)e_i+$ terms independent of $e_i$, because each other actor's payoff contains $-\Omega w_i/(n-1)$ and $-\ell\mathcal E$.
- (1) This is a Tullock contest with prize $\Omega(n-1-\theta)/(n-1)$ and marginal cost $c+(1+\theta)\ell$. Its symmetric equilibrium is $r(n-1)\cdot\text{prize}/(n^2\cdot\text{cost})$, in pure strategies for $r\le n/(n-1)$ (Pérez-Castrillo and Verdier 1992).
- (2) is immediate.
- (3) $W_i=O_i|_{\theta=\kappa}$. Lowering $\theta$ raises the marginal value of intensity by $\Omega\,\partial w_i/\partial e_i/(n-1)+\ell>0$, so the best response weakly rises. For $r\le1$, $w_i$ is strictly concave in $e_i$, so $W_i$ has a unique maximizer. Against others all at zero, $w_i=1$ for every $e_i>0$, so no maximizer exists.
- (4) A finite-population ESS requires that a single deviant do no better than the residents it meets (Schaffer 1988), so the resident intensity maximizes $\pi_i-\bar\pi_{-i}$.

**Lemma 4.4.** By the chain rule, $\Pr(S_N)=\prod_{k\le N}\Pr(\text{no event at }k\mid S_{k-1})$. Each factor is at most $1-h_k$, because the bound holds on every surviving history. Then $1-x\le e^{-x}$. For the upper bound, each factor is at least $1-\bar h_k>0$, and $\prod(1-\bar h_k)>0$ iff $\sum\bar h_k<\infty$.

**Proposition 4.5.** (1) Shifting the sequence by $D$ leaves the product over any window of the same length unchanged, and the infinite product is zero by Lemma 4.4. (2) is the upper-bound part of Lemma 4.4 applied after the change. (3) is Proposition 3.12.

### A.5 Section 5

**Proposition 5.1.**
- (1) compares $S_i^O$ with $P_i^O$; in Proposition 4.2's contest, strict participation holds for $r<n/(n-1)$.
- (2) At $n=2$, $r=1$, $\Omega=c=1$, $\ell=0.1$, the $\theta=-1$ intensity is $1/2$, giving $P^\pi=-0.1$. Against $e=1/2$, zero intensity gives $S^\pi=-0.05$, and the other's payoff is $0.45$, so $S^W=0.04$ and $P^W=-0.12$.
- (3) With penalty $L_b$ the payoff is $w_i(\Omega+L_b)-L_b-ce_i-\ell\mathcal E$: Proposition 4.2's contest with prize $\Omega+L_b$. At $\theta=0$ the symmetric intensity is $e=r(n-1)(\Omega+L_b)/(n^2(c+\ell))$, and the difference between joining and staying out is $(\Omega+L_b)/n-(c+\ell)e$. In the symmetric all-pay contest each player's expected payoff equals the payoff of the lowest bid in its support, $-L_b$ (Baye, Kovenock and de Vries 1996); the same holds for two actors with $r\ge2$ (Ewerhart 2015).
- (4) $\prod_i(1-\xi_i)\to0$ iff $\sum_i\xi_i=\infty$.

**Proposition 5.2.** Joint restraint gives $\Omega/n$. At the $\theta=0$ equilibrium each actor bears $ce$ privately and $\ell ne$ through total intensity. For the asymmetric profile with $n=3$, $r=2$, an active actor's action-dependent payoff is $-x(x-\frac12)^2/(x^2+\frac14)\le0$, so the equilibrium is weak.

**Proposition 5.3.**
- (1) is direct computation from the contest success function.
- (2) The limiting gains follow from (1); the gain increases in $s$, so the inequalities are necessary and sufficient for dominance in the limit.
- (3) With all delegating, $w_i=1/n$ as with none, and the hazard is higher.
- (4) The term $L_c[\cdot]$ is common to all objectives and cancels from a relative objective.

**Lemma 5.4.** Solve the two linear equations.

**Proposition 5.5.**
- (1) With $q_L=1$, $\Phi_D=0$, while $\Phi_N=Q_N[w_N+(1-w_N)(1-p)]\ge Q_Nw_N>0$ for finite $s$, since $w_N>0$.
- (2) With $p=1$, $\Phi_N=Q_N/(n+ks)$, because the actor has strength $1$, $k$ others $1+s$, and $n-1-k$ others $1$. Similarly $\Phi_D=(1-q_L)aQ_N(1+s)/(n+(k+1)s)$, and the ratio follows. All delegating is an equilibrium iff the ratio at $k=n-1$ is at least one; no one delegating iff the ratio at $k=0$ is at most one. Substituting gives the two conditions, and the numbers are in `checks_v5.log` (DL).
- (3) $Q_N/(n+ks)>0$ for finite $s$.

**Lemma 5.6.** Under (a)–(d), variants that act on common terms exist and, by (b), have relative performance lower by at least $\nu$. By (c), retention is cumulative, so their share tends to zero (as in Proposition 2.4(3)). By (d), the retained systems' decisions are the actor's decisions. If constraints are an enforced condition of admission for every eligible variant, no admissible variant violates them, so (a) fails.

**Proposition 5.7.**
- (1) is Hayes (1950).
- (2) By simulation of $\dot y=ay-k_py(t-\tau_c)-k_d\dot y(t-\tau_c)$ (`../v4/checks_v42.log`).
- (3) With $G(s)=e^{-s\tau_c}/(s-a)$ and any stabilizing linear time-invariant controller, the complementary sensitivity $\mathcal T$ is stable and satisfies $\mathcal T(a)=1$. Write $\mathcal T(s)=e^{-s\tau_c}\tilde{\mathcal T}(s)$ with $\tilde{\mathcal T}$ stable; by the maximum modulus principle $\|\mathcal T\|_\infty\ge|\tilde{\mathcal T}(a)|=e^{a\tau_c}$. Robust stability needs $\|w\mathcal T\|_\infty<1$. Since $w\tilde{\mathcal T}$ is stable, its supremum on the imaginary axis is at least its modulus at $a$, giving the necessary condition $|w(a)|e^{a\tau_c}<1$. For $w(s)=2(s-a)/(s+a)$, $|w(j\omega)|=2$ for all $\omega$, so $\|w\mathcal T\|_\infty=2\|\mathcal T\|_\infty\ge2e^{a\tau_c}$.
- (4) Evidence cannot be acted on before it exists.

**Theorem 5.8.** For $t\ge T_\varepsilon$, on every surviving history, the conditional probability of the event is at least $h(1-\varepsilon)$. By the chain rule (Lemma 4.4), $\Pr(S_H)\le\Pr(S_{T_\varepsilon})(1-h(1-\varepsilon))^{H-T_\varepsilon}$. The converse is the upper-bound part of Lemma 4.4 with $\bar h_k=\bar h\mathsf u_k$.

**Proposition 5.9.**
- (1) After $\tau$, $\mathsf u_t=(1-U(t)/Y_\tau)^+$. For linear $U$, the positive part lasts $(Y_\tau-U(\tau))/\dot U$, and the integral of a linear function falling from $1-U(\tau)/Y_\tau$ to $0$ over that interval is $Y_\tau(1-U(\tau)/Y_\tau)^2/(2\dot U)$. For exponential $U$, $\int_0^{\ln\Gamma/g_U}(1-e^{g_Uv}/\Gamma)\,dv=(\ln\Gamma-1+1/\Gamma)/g_U$.
- (2) After rollback, $\mathsf u_t=0$.
- (3) Frozen hazardous variety is $\varphi\Gamma_X$ times the rivals' level, and coverage is at least the rivals' level, so $\mathsf u=0$ when $\varphi\Gamma_X\le1$.
- (4) For linear $U$, $\dot U/U=\dot U/(U_0+\dot Ut)\to0$. For the counterexample, let $\log U$ increase by $0.5$ on each interval $[n^2,n^2+1]$ and stay constant otherwise. Then $\log U(t)\approx0.5\sqrt t=o(t)$, while $\dot U/U=0.5$ inside each interval (`checks_v5.log`, MM).

**Proposition 5.10.** The residual hazard is the sum of failures not blocked and failures the corrector adds; compare with $q_0$. The example is in `checks_v5.log` (OV).

**Proposition 5.11.**
- (1) Each layer covers $\mathsf m$ times the attention of the layer above, so $k$ layers cover $\mathsf B\mathsf m^k$. A problem is caught only if every link succeeds, and the conditional reliabilities multiply to $\mathsf f^k$. Then $\mathsf f^k=\exp(k\ln\mathsf f)=(Y/\mathsf B)^{\ln\mathsf f/\ln\mathsf m}$.
- (2) Independent checks fail together with probability $(1-\mathsf f)^k$. A common cause that defeats all of them with probability $\rho$ leaves at most $1-\rho$.

**Remark 5.12.** While small, errors grow as $\delta_{\text{obs}}e^{\lambda_Lt}$; set this equal to $\Delta_{\text{tol}}$.

**Proposition 5.13.**
- With $r=1$ and the others at a common $\iota$, $\partial w_i/\partial\iota_i=s(n-1)/(n^2(1+s\iota))$ at the symmetric point. The marginal cost of $\iota_i$ is $L_c\Delta\psi(1-\psi)^{n-1}$. Equating gives $(1+s\iota)\Delta\psi(q-x)^{n-1}=L_es(n-1)/(n^2L_c)$, and dividing by $s$ gives $(x+b)(q-x)^{n-1}=K$.
- (1) For $x\ll q$, $(q-x)^{n-1}\approx q^{n-1}$, so $x\approx K/q^{n-1}-b$, and multiplying by $n$ gives the approximation.
- (2) Differentiating the implicit equation in $\Delta\psi$ (with $b=\Delta\psi/s$) gives the stated derivative. The two interior roots and the corner are found numerically and checked as global best responses (`checks_v5.log`, HO).
- (3) At full delegation, the own marginal gain is $2s_t/(9(1+s_t))-\Delta\psi_t(1-\Delta\psi_t)^2>0$ for $t\ge5$. Each actor's objective is concave in its own $\iota$, so full delegation is an equilibrium. The realized risk is $1-(1-2^{-t})^3\le3\cdot2^{-t}$, which sums to at most $3/16$ from $t=5$.
- (4) For $k\ge1$, $(1-\psi_0-\Delta\psi)^k<(1-\psi_0)^k$.

**Proposition 5.14.**
- (1) The advantage is linear in $\varpi$, with the stated endpoints.
- (2) is the case of two non-negative endpoints.
- (3) If $\Phi^P_H>\Phi^S_H$, racing is a strict best response to racing.
- (4) With constant per-period hazards, $\Phi^B(H)=(1-q_B)^H$ and $\Phi^R(H)=(1-q_R)^H$.
- (5) Substitute the mixtures into (1). The example is in `checks_v5.log` (SR).

**Theorem 5.15.** Each item of Branch I is the cited proposition under its condition. For Branch II, solve the multi-period bargaining backward: A's value is $V_t=\max(W_t,\delta V_{t+1})$ with $W_t=(w_t-c_A)/(1-\delta)$, and war occurs at $t$ iff $W_t>1+\delta V_{t+1}$ (`../v4/checks_v44.log`, B2). Branch III follows from intensity proportional to $r$ (Proposition 4.2(1)).

### A.6 Section 6

**Remark 6.1.** With the leader paused, $\dot\Delta=-\delta_f\Delta-1$, so $\Delta(t)=(\Delta_0+1/\delta_f)e^{-\delta_ft}-1/\delta_f$, which reaches zero at $T_p$ (`../v4/checks_v45.log`, LD).

**Proposition 6.2.** (1) is the commitment problem as cited; the worst-case rule is that of Gilboa and Schmeidler (1989), applied to every action. (2): if restraint while ahead lowers the probability of winning, Bayes' rule gives the stated inequality, and repeated selection compounds it (Proposition 2.4).

**Proposition 6.3.** (1) is Proposition 5.9. (2): rivals at the coverage frontier reach the frozen level when coverage does, if they use the same units. (3) and (4) describe the decision problems of Propositions 5.14 and 6.5 and Definition 3.3.

**Proposition 6.4.**
- (1) Fighting now is worth $(w_1-c_A)/(1-\delta)$. Peace gives A at most the whole flow today plus $x$ per period from tomorrow, $1+\delta x/(1-\delta)$, with equality when A obtains the whole flow today.
- (2) Under (A8), B offers A exactly its reservation value $\max(w_2-c_A,0)$.
- (3) If A sets the terms, B accepts any share leaving it at least $1-w_2-c_B$.
- (4) If $c_A\ge w_1$, war is worth at most zero.

**Proposition 6.5.** (1) Compare $\Phi^{\text{Prev}}$ with $\max(\Phi^S,\Phi^P)$ and solve for $\varepsilon_P$. (2) The per-period probability of an escalating strike is at least $b_P\varepsilon_{\min}$ while the premises hold; then apply Lemma 4.4. (3) $0.99^{H}>0.95^{H}$ for every $H>0$.

**Proposition 6.6.**
- (1) An irreversible exit keeps its gain even when detected, and is deterred iff $\upsilon F\ge X-X_{\text{stay}}$. A reversible covert preparation is undone when detected in time; its expected value is $(1-\upsilon)X+\upsilon(X_{\text{stay}}-F)$.
- (2) Differentiate $\ln\mathcal L$. The counter-case $\mathcal O=e^{2t}$, $\mathcal H=e^{-1.5t}$, $\Lambda=\sqrt{\mathcal O}$, $\mu=0$ gives $\mathcal L=e^{-0.5t}$.
- (3) Proportional arrangements leave each actor's chance $w_i$ unchanged.

**Theorem 6.7.** (1) Rearrange $R>T_\upsilon$. (2) applies the definition of timely detection. (3) collects Propositions 8.3 and 6.6 and Section 3. (4): bounding the undetected defection bounds $T$; the rate condition compares the coalition's advantage with its erosion. The information role is Proposition 7.8(3).

### A.7 Section 7

**Theorem 7.2.**
- (1) (I2) with margin in rule-making gives a full row sum below one, so $x_{\mathsf S}\to0$ (Proposition 3.10(2)). Once (I1) is enacted, $\tau_{\text{eff}}>\nu$ after a finite time. Load then has negative private payoff, so $E\to e_{\min}$ and $\liminf V\ge K(1-he_{\min}/\rho)>V_{\min}$. For unanticipated harms, (I2) in evaluation gives $x_{\mathsf E}\to0$, so $m\to\beta_{\text{out}}<m_{\text{fl}}$, or the conservative rule applies, and the alarm fires above the floor.
- (2) Without (I1), Proposition 2.4 applies. Without (I2) in rule-making, $x_{\mathsf S}\to1$ (Proposition 3.11(1)) and $\tau_{\text{eff}}\to0$. Without (I3), silent crossing follows (Proposition 3.8(2)). With rule-making captured first, $x_{\mathsf S}$ keeps rising long enough for the floor to be crossed when $\varepsilon_{\mathsf S}$ is small.
- (3) If the limsup is below $\nu$, there are $\epsilon>0$ and $T_0$ with $T^{-1}\int_0^T\tau_{\text{eff}}\le\nu-\epsilon$ for $T>T_0$. Then the carrier of load $e_{\max}$ grows relative to any carrier of lower load, $E\to e_{\max}$, and the argument of Proposition 2.4(3) applies.

**Proposition 7.3.** (1) is Propositions 2.4 and 3.5(1)–(2). (2) With rule-makers as players, unilateral imposition is restraint in Proposition 2.5. (3) Under $\tau_{\text{eff}}>\nu$ the private payoff of load is negative.

**Proposition 7.4.** Compare the first-order conditions; concavity of $\Omega$ orders the solutions.

**Proposition 7.5.** For $k$ racers and $m=n-k$ cooperators:
- Under separate frontiers, a racer's payoff is $w_i\Omega-(1-w_i)L_b-ce_i-\ell\mathcal E$, with $w_i=e_i^r/(\sum_{\text{racers}}e^r+me_c^r)$.
- Under a common frontier, the pool's strength is $(me_c)^r$. A cooperator gets $w_{\text{pool}}\Omega_c/m-(1-w_{\text{pool}})L_b-ce_c-\ell\mathcal E$.
- Racers' intensities are the symmetric fixed point of best responses among them, each verified as a global best response. Where $r>k/(k-1)$ for $k$ racers there may be no symmetric pure equilibrium, and such cases are excluded.
- The per-rival threshold solves $\sum_k\binom{n-1}{k}q^k(1-q)^{n-1-k}[\text{Coop}(k)-\text{Race}(k+1)]=0$, with trust $1-q$.
- The aggregate reduction uses $R=\text{Coop}(0)$, $T=\text{Race}(1)$, $S'=\text{Coop}(n-1)$ and $P=\text{Race}(n)$.
- For the coalition of three with summed payoff: against a single cooperator, the coalition's members get $0.14$ cooperating against $-1.197$ racing; against a single racer, $-0.885$ against $-1.325$. Cooperation is better in both, so it is dominant.
- The lid is the smallest $e_c$ with $T\le R$, found by search from below, since $T-R$ is not monotone in $e_c$ (`../v4/checks_v45.log`, N22).

**Proposition 7.7.** Apply Proposition 3.10(2) to the verifier's full row. The counter-case is one domain with captured sources whose conversions sum to $1.05$. The fourth limit is Proposition 8.3 with the verifier as sender.

**Proposition 7.8.**
- (1) is the participation constraint under transferable utility; strict gain needs strict inequality.
- (2) Under Bayesian incentive compatibility with types independent, each type's interim expected utility from reporting must not depend on its report beyond what truth gives. With linear, type-independent share utility, this makes the interim expected share independent of the report. Budget balance makes these interim shares constants summing to one, and participation must hold for the type with the best outside option. The example's interim shares are computed in `checks_v5.log` (K7).
- (3)–(5) follow by substitution.

### A.8 Section 8

**Proposition 8.1.**
- (1) Cooperating yields $\varpi R+(1-\varpi)(\upsilon P+(1-\upsilon)S)$, and defecting yields $\varpi T_\upsilon+(1-\varpi)P$; the difference is $\varpi g_C-(1-\varpi)g_D$.
- (2) Rearrange.
- (3) Apply the cited results to the symmetric $2\times2$ game.
- (4) If every intermediate state gives a cooperation-minus-defection advantage of at least $-g_D$, then the expected advantage is at least $\varpi_1^{n-1}g_C-(1-\varpi_1^{n-1})g_D$. That is non-negative when $\varpi_1^{n-1}\ge\varpi^\ast$. The counterexample is in `checks_v5.log` (N13).

**Corollary 8.2.** Each item follows from the stated formula: $T-R$ in Proposition 8.1; $b=\lambda\beta_s$ in Proposition 8.3; the net exit gain in Proposition 6.6.

**Proposition 8.3.** Crawford and Sobel (1982), uniform-quadratic case. With $b=0$ the ideal points coincide and truthful revelation is an equilibrium.

**Proposition 8.4.**
- (1) Given the receiver's strategy (restrain after $E$, not otherwise), type $S$ sends iff $G_S-k_S\ge0$ and type $R$ does not iff $G_R-k_R\le0$. Given separation, the receiver's posterior after $E$ is one, at least $\varpi^\ast$, and after no signal it is zero.
- (2) If $k_R<G_R$, type $R$ gains by sending, so separation fails. With both types sending, the posterior after $E$ is $1-\mu$.
- (3) restates the condition $k_R\ge G_R$.

**Proposition 8.5.** (1) is Proposition 7.5 and Theorem 7.2. (2) is Propositions 8.1, 5.14 and 5.5. (3) is Theorem 7.2(1) and Lemma 5.4. (4) is Propositions 6.6, 7.7 and 3.10.

---

## Appendix B. Numerics

`checks_v5.py` (pure Python, log `checks_v5.log`) computes every case v5 cites as [N] that is new or repaired:
- AG, the harmful game;
- CR, the chain-rule lemma and a mere delay;
- FB, the feedback benchmark;
- HO, risk homeostasis: branches, multiplicity, saturation and the saw-tooth;
- DL, delegation in survival terms;
- MM, the coverage mismatch theorem, freezing with the hazardous set, summability without catch-up, and coverage that grows in bursts;
- OV, oversight topology and a fallible corrector;
- SR, survival ratios and mixed beliefs;
- FS, the finite sprint and prevention;
- SG, the costly signal;
- K7, interim incentive compatibility;
- N13, the $n$-player condition;
- CAP, splitting, moments of shares, mean against maximal load, and the control screen;
- CMP, the two-crux comparison.

It reproduces the counterexamples of the handoff review of v4.5 independently of the reviewer's script (`sources/19-v5-handoff-2026-10-03/v5_0_handoff/verification/`), which needs NumPy and SciPy.

Results carried from earlier versions are checked by the earlier scripts, which remain in `../v4/` and `../v3/`:
- `checks_v31.py` and `figures_v3.py`: Proposition 2.5, the repeated-game cutoff, the rate law of Proposition 3.6, and the illustration of Theorem 3.13;
- `checks_v4.py`: Propositions 4.2, 5.2, 5.3, 6.4, 8.1 and 8.3, the Hayes window, and the conservative alarm;
- `checks_v42.py`: counterexamples to v4.1, derivative action, and Proposition 7.7;
- `checks_v44.py`: the delegation conditions, Branch II of Theorem 5.15, and the survival examples of Proposition 5.14;
- `checks_v45.py`: Nash-verified Proposition 7.5, the catch-up computations, Proposition 7.8, the lead under diffusion, and discounting.

None of these suites certifies every proof, and none supplies evidence about the world.

---

## Appendix C. Conditions, indicators and measures

The evidence register gives the dated observations. This appendix gives the conditions of the conditional results and how each would be measured. The entries say where to measure; they are not estimates.

**The slow route (Theorem 3.13).**

| Condition | Indicator | What would refute it |
|---|---|---|
| C0 floor within reach | Per harm class: capability with safeguards removed | For every class, independently measured capability with safeguards removed stays below the threshold |
| C1 cumulative relative selection | Capital, compute and talent following rank; effective liability against $\nu$ over time | Restraint gains share at a given rank, or the cumulative advantage converges. An average $\tau_{\text{eff}}$ equal to $\nu$ is not enough: $\tau_{\text{eff}}=\nu-1/(1+t)$ has average tending to $\nu$ while the cumulative advantage $\ln(1+t)$ diverges |
| C2 appropriable control | Developer roles in evaluation and standards; share keyed to one provider | Evaluation and standards funded, staffed and accessed independently of the evaluated |
| C3 two rates | AI's cheapening of control ($g$) against that of independent evaluation plus budget growth ($b+g_c$) | $b+g_c\ge g/(1+\eta)$ |
| C4 masking | Evaluator bias against ground truth at relevant harm levels | Measured $m(t)\le m_{\text{fl}}$ in the band, or a credible low-bias report that is acted on |
| C5 reach | Compute and deployment within one jurisdiction | One jurisdiction's rules bind all load that can cross the floor |
| C6 order of events | Release-to-evaluation time against harm-to-detection time | Independent detection consistently precedes developer-shaped evaluation |

**The contest (Theorem 5.15).**

| Condition | Meaning | What would change the conclusion |
|---|---|---|
| P1 | Actors act on a large perceived $r$ | If no actor believed in decisive advantage, the race would lose its object (Branch III) |
| P2 | Leads open within short windows | A sustained slowdown moves the trajectory to Branch II |
| P3 | Advantage does not saturate | Saturation moves it to Branch I′ |
| Shared exposure | $\ell>0$, $\kappa>0$ | Unshared payoffs remove the shared-loss parts of Propositions 4.2 and 5.2 |
| Correction delays | Delays comparable to $1/a$ for some classes | Correction robust at the observed $a\tau_c$ relaxes Proposition 5.7 |
| Verification | $\upsilon<1$, or not timely against a decisive shift | Perfect timely detection moves the boundary of Theorem 6.7 to timeliness, reliability and approval |
| Conversion into influence | Success converts into influence over correctors; AI lowers the cost of control | $\chi=0$, or independent correction keeping pace (Proposition 3.6(4)) |
| Participation | Efficiency, information and distribution conditions of Proposition 7.8 | If the strongest actor's rents exceed its losses, racing can pay for it materially |
| Delegation | The exact condition of Proposition 5.3, relative objectives, or survival without the lock | If the control loss dominates, or the lock is priced in with $q_L=1$, delegation is not chosen (Propositions 5.3, 5.5) |
| (A8) | After a shift, the advantaged side sets the terms | Under other protocols prevention can cease to be rational (Proposition 6.4(3)) |

**The coverage premises (Section 5.4).**

| Premise | Indicator | What would refute it |
|---|---|---|
| (X) | Predefined hazard modes per class and their count per model generation; new threat models; automation of AI research | Bounded variety of hazardous behaviour in the decisive class |
| (U) | $U$ measured by C1–C4: catch rates of planted defects at fixed human hours; rates of overrule; audit coverage | Catch rates that do not fall as capability rises |
| (φ) | Residual-risk estimates per class after correction, by independent evaluators | Residual risk falling fast enough to be summable |
| (φ-s) | Propagation pathways of failures | Failures confined to their source |
| $q_L$ | Whether delegated decisions can be overruled; drills of fallback capacity | Maintained $\mathcal K\ge\mathcal K_{\min}$ removes the lock (Lemma 5.4) |

**Measuring the exits (Section 8.3).** The relation $a\approx\ln2/T_2$, with $T_2$ the doubling time of a proxy for dangerous capability, is a connecting assumption.

| Exit | Indicator | Example of a threshold | Precedent or measurer | What would count against it |
|---|---|---|---|---|
| E1, decision loops | Share of consequential decisions requiring human authorization, with a minimum time for deliberation | Nuclear command and control: all | Doctrine, exercises and after-action review | Human authorization on paper while delegated systems decide: overrule near zero |
| E1, tempo | Share of automated agents in markets and cyber operations under circuit breakers | A minimum human delay per transaction or operation | Circuit breakers in financial regulation | — |
| E1, parallel capacity | Share of delegated functions that trained people can take over in a stated time; drill success | Critical functions drilled at least quarterly | Ironies of automation; manual flying requirements | Rising drill failure: lock-in under way |
| E2, thresholds | Thresholds for automated AI research; task length; autonomous replication | A red line at a stated task length | Independent evaluators with statutory access | Dangerous capability not appearing at the threshold |
| E2, inputs | Efficiency-corrected compute caps; unaccounted compute; largest undeclared cluster | Undeclared compute of the order of half a per cent of the global total | Supply-chain accounting; hardware mechanisms | — |
| E2, rate | Tightening of input bounds against algorithmic efficiency | A ratio of at least one; about 2.5–3× a year at an eight-month efficiency doubling | Trend measurement | — |
| E3, tempo | $a\approx\ln2/T_2$ | A seven-month doubling gives $a\approx0.10$ a month | Independent measurement | Dangerous capability decoupling from general capability |
| E3, lag | $L=\tau_{\text{obs}}+T_d+T_r$ from appearance to withdrawal | Relative model error below $e^{-aL}$. At $T_2=7$ months, $L$ of 6, 12 and 24 months tolerates 0.55, 0.30 and 0.09 | Regulators; incident-reporting deadlines | Correction robust at the observed $aL$ |
| E3 and (U) | $\dot U/U$ against $\dot Y/Y$ | Until the uncovered share is summable | Control evaluations; auditing games | Catch rates at fixed human hours not falling |

---

## References

Marks: unmarked works are carried from the verified bibliography of v3.1 (`../v3/references.bib`). ‡ marks works whose existence and identifier were checked on 3 October 2026, by this pass or by the handoff reviews. † marks works not yet independently verified. Sources of observations are listed with dates and links in [EVIDENCE.md](EVIDENCE.md).

*Selection, games and contests*
- Alchian, A. 1950. Uncertainty, evolution, and economic theory. *Journal of Political Economy* 58(3).
- Alger, I. and Weibull, J. W. 2013. Homo moralis: preference evolution under incomplete information and assortative matching. *Econometrica* 81(6).
- Alger, I., Weibull, J. W. and Lehmann, L. 2020. Evolution of preferences in structured populations. *Journal of Economic Theory*. †
- Armstrong, S., Bostrom, N. and Shulman, C. 2016. Racing to the precipice: a model of artificial intelligence development. *AI & Society* 31(2).
- Baye, M., Kovenock, D. and de Vries, C. 1996. The all-pay auction with complete information. *Economic Theory* 8(2). †
- Carlsson, H. and van Damme, E. 1993. Global games and equilibrium selection. *Econometrica* 61(5). †
- Crawford, V. and Sobel, J. 1982. Strategic information transmission. *Econometrica* 50(6). †
- Dekel, E., Ely, J. and Yilankaya, O. 2007. Evolution of preferences. *Review of Economic Studies* 74(3). †
- Dixit, A. 1987. Strategic behavior in contests. *American Economic Review* 77(5). †
- Ewerhart, C. 2015. Mixed equilibria in Tullock contests. *Economic Theory* 60(1). †
- Fershtman, C. and Judd, K. 1987. Equilibrium incentives in oligopoly. *American Economic Review* 77(5). †
- Frank, R. 1985. *Choosing the Right Pond*.
- Güth, W. and Yaari, M. 1992. Explaining reciprocal behavior in simple strategic games: an evolutionary approach. †
- Harris, C. and Vickers, J. 1987. Racing with uncertainty. *Review of Economic Studies* 54(1). †
- Hehenkamp, B., Leininger, W. and Possajennikov, A. 2004. Evolutionary equilibrium in Tullock contests. *European Journal of Political Economy* 20(4). †
- Heifetz, A., Shannon, C. and Spiegel, Y. 2007. What to maximize if you must. *Journal of Economic Theory* 133(1). †
- Hillman, A. and Riley, J. 1989. Politically contestable rents and transfers. *Economics and Politics* 1(1). †
- Hirsch, F. 1976. *Social Limits to Growth*.
- Kandori, M., Mailath, G. and Rob, R. 1993. Learning, mutation, and long run equilibria in games. *Econometrica* 61(1). †
- Konrad, K. and Kovenock, D. 2009. Multi-battle contests. *Games and Economic Behavior* 66(1). †
- Konrad, K., Peters, W. and Wärneryd, K. 2004. Delegation in first-price all-pay auctions. *Managerial and Decision Economics* 25(5). †
- Ok, E. and Vega-Redondo, F. 2001. On the evolution of individualistic preferences. *Journal of Economic Theory* 97(2). †
- Pérez-Castrillo, D. and Verdier, T. 1992. A general analysis of rent-seeking games. *Public Choice* 73(3). †
- Price, G. 1970. Selection and covariance. *Nature* 227.
- Schaffer, M. 1988. Evolutionarily stable strategies for a finite population and a variable contest size. *Journal of Theoretical Biology* 132(4).
- Schlag, K. 1998. Why imitate, and if so, how? *Journal of Economic Theory* 78(1).
- Weibull, J. W. 1995. *Evolutionary Game Theory*. †
- Young, H. P. 1993. The evolution of conventions. *Econometrica* 61(1). †

*Commons, capture, institutions and the meta-attractor*
- Acemoglu, D., Egorov, G. and Sonin, K. 2012. Dynamics and stability of constitutions, coalitions, and clubs. *American Economic Review* 102(4). ‡ (abstract)
- Acemoglu, D. and Robinson, J. 2008. Persistence of power, elites, and institutions. *American Economic Review* 98(1).
- Aubin, J.-P. 1991. *Viability Theory*.
- Barrett, S. 2013. Climate treaties and approaching catastrophes. *Journal of Environmental Economics and Management* 66(2).
- Barrett, S. and Dannenberg, A. 2012. Climate negotiations under scientific uncertainty. *PNAS* 109(43).
- Becker, G. 1983. A theory of competition among pressure groups for political influence. *Quarterly Journal of Economics* 98(3).
- Bombardini, M. 2008. Firm heterogeneity and lobby participation. *Journal of International Economics* 75(2).
- Green, E. and Porter, R. 1984. Noncooperative collusion under imperfect price information. *Econometrica* 52(1).
- Heckathorn, D. 1989. Collective action and the second-order free-rider problem. *Rationality and Society* 1(1).
- Hirsch, M. 1985. Systems of differential equations that are competitive or cooperative II. *SIAM Journal on Mathematical Analysis* 16(3).
- Kempe, D., Kleinberg, J. and Tardos, É. 2003. Maximizing the spread of influence through a social network. *KDD*.
- Krakauer, D., Page, K. and Erwin, D. 2009. Diversity, dilemmas, and monopolies of niche construction. *American Naturalist* 173(1). ‡ (full text)
- Morris, S. 2000. Contagion. *Review of Economic Studies* 67(1).
- Oliver, P. 1980. Rewards and punishments as selective incentives for collective action. *American Journal of Sociology* 85(6).
- Olson, M. 1993. Dictatorship, democracy, and development. *American Political Science Review* 87(3). †
- Panchanathan, K. and Boyd, R. 2004. Indirect reciprocity can stabilize cooperation without the second-order free rider problem. *Nature* 432.
- Rockström, J. et al. 2009. A safe operating space for humanity. *Nature* 461.
- Seidman, S. 1983. Network structure and minimum degree. *Social Networks* 5(3).
- Shavell, S. 1984. Liability for harm versus regulation of safety. *Journal of Legal Studies* 13(2). †
- Sigmund, K. et al. 2010. Social learning promotes institutions for governing the commons. *Nature* 466.
- Smith, H. 1995. *Monotone Dynamical Systems*.
- WCED 1987. *Our Common Future*.
- Weitzman, M. 1974. Prices vs. quantities. *Review of Economic Studies* 41(4). †
- Yamagishi, T. 1986. The provision of a sanctioning system as a public good. *Journal of Personality and Social Psychology* 51(1).

*Delegation, control, oversight and risk*
- Dalrymple, D. et al. 2024. Towards guaranteed safe AI. arXiv:2405.06624. ‡
- Greenblatt, R., Shlegeris, B., Sachan, K. and Roger, F. 2024. AI control: improving safety despite intentional subversion. *ICML*. ‡
- Hayes, N. 1950. Roots of the transcendental equation associated with a certain difference-differential equation. *Journal of the London Mathematical Society* 25. †
- Kulveit, J. et al. 2025. Gradual disempowerment. †
- Marks, S. et al. 2025. Auditing language models for hidden objectives. †
- Peltzman, S. 1975. The effects of automobile safety regulation. *Journal of Political Economy* 83(4).
- Scharre, P. 2018. *Army of None*. †
- Stafford, E., Trager, R. and Dafoe, A. 2022. Safety not guaranteed: international strategic dynamics of risky technology races. Working paper. †
- Wilde, G. 1982. The theory of risk homeostasis. *Risk Analysis* 2(4). †

*Growth, decision and information*
- Aghion, P., Jones, B. F. and Jones, C. I. 2019. Artificial intelligence and economic growth. †
- Arrow, K. and Fisher, A. 1974. Environmental preservation, uncertainty, and irreversibility. *Quarterly Journal of Economics* 88(2). †
- Bloom, N., Jones, C. I., Van Reenen, J. and Webb, M. 2020. Are ideas getting harder to find? *American Economic Review* 110(4). †
- Bueno de Mesquita, E., Dziuda, W. and Polborn, M. 2026. The AGI race and existential risk. NBER Working Paper 35276. ‡
- Fey, M. and Ramsay, K. 2007. Mutual optimism and war. *American Journal of Political Science* 51(4). †
- Fudenberg, D. and Koh, A. 2026. Cooperating against catastrophe. arXiv:2609.28291. ‡
- Gilboa, I. and Schmeidler, D. 1989. Maxmin expected utility with non-unique prior. *Journal of Mathematical Economics* 18(2). †
- Grossman, S. 1981. The informational role of warranties and private disclosure about product quality. *Journal of Law and Economics* 24(3). †
- Henry, C. 1974. Investment decisions under uncertainty: the irreversibility effect. *American Economic Review* 64(6). †
- Jones, C. I. 1995. R&D-based models of economic growth. *Journal of Political Economy* 103(4). †
- Jones, C. I. 2024. The AI dilemma: growth versus existential risk. *American Economic Review: Insights* 6(4). ‡
- Kamenica, E. and Gentzkow, M. 2011. Bayesian persuasion. *American Economic Review* 101(6). †
- Milgrom, P. 1981. Good news and bad news: representation theorems and applications. *Bell Journal of Economics* 12(2). †

*Strategy, war and arms control*
- Abecassis, D. 2025. Refining MAIM: identifying changes required to meet conditions for deterrence. MIRI. ‡
- Bundy, M. 1988. *Danger and Survival*. †
- Burr, W. and Richelson, J. 2000/01. Whether to "strangle the baby in the cradle". *International Security* 25(3). †
- Coe, A. and Vaynman, J. 2015. Collusion and the nuclear nonproliferation regime. *Journal of Politics* 77(4). †
- Coe, A. and Vaynman, J. 2020. Why arms control is so rare. *American Political Science Review* 114(2). †
- Copeland, D. 2000. *The Origins of Major War*. †
- Debs, A. and Monteiro, N. 2014. Known unknowns: power shifts, uncertainty, and war. *International Organization* 68(1). †
- Fearon, J. 1995. Rationalist explanations for war. *International Organization* 49(3). †
- Hendrycks, D., Schmidt, E. and Wang, A. 2025. Superintelligence strategy. †
- Ikenberry, G. J. 2001. *After Victory*. †
- Jervis, R. 1976. *Perception and Misperception in International Politics*. †
- Jervis, R. 1978. Cooperation under the security dilemma. *World Politics* 30(2). †
- Glaser, C. 1994/95. Realists as optimists: cooperation as self-help. *International Security* 19(3). †
- Kydd, A. 1997. Game theory and the spiral model. *World Politics* 49(3). †
- Kydd, A. 2005. *Trust and Mistrust in International Relations*. †
- Leitenberg, M. and Zilinskas, R. 2012. *The Soviet Biological Weapons Program*. †
- Mearsheimer, J. 2001. *The Tragedy of Great Power Politics*. †
- Nye, J. 1987. Nuclear learning and U.S.–Soviet security regimes. *International Organization* 41(3). †
- Osgood, C. 1962. *An Alternative to War or Surrender*. †
- Posen, B. 1991. *Inadvertent Escalation*. †
- Powell, R. 2006. War as a commitment problem. *International Organization* 60(1). †
- Schelling, T. 1960. *The Strategy of Conflict*; 1966. *Arms and Influence*. †
- Snyder, G. 1965. The balance of power and the balance of terror. †
- Tannenwald, N. 1999. The nuclear taboo. *International Organization* 53(3). †
- Trachtenberg, M. 1988/89. A "wasting asset". *International Security* 13(3). †
- Van Evera, S. 1999. *Causes of War*. †

*The governing model: evolution, behaviour, performativity and history (Sections 1.4–1.5)*
- Aktipis, C. A., Boddy, A. M., Jansen, G., Hibner, U., Hochberg, M. E., Maley, C. C. and Wilkinson, G. S. 2015. Cancer across the tree of life: cooperation and cheating in multicellularity. *Philosophical Transactions of the Royal Society B* 370(1673). ‡
- Anderson, C., Hildreth, J. A. D. and Howland, L. 2015. Is the desire for status a fundamental human motive? A review of the empirical literature. *Psychological Bulletin*. ‡
- Darwin, C. 1871. *The Descent of Man, and Selection in Relation to Sex*. †
- Ferraro, F., Pfeffer, J. and Sutton, R. I. 2005. Economics language and assumptions: how theories can become self-fulfilling. *Academy of Management Review* 30(1). ‡
- Fischbacher, U., Gächter, S. and Fehr, E. 2001. Are people conditionally cooperative? Evidence from a public goods experiment. *Economics Letters* 71(3). ‡
- Frank, R. H., Gilovich, T. and Regan, D. T. 1993. Does studying economics inhibit cooperation? *Journal of Economic Perspectives* 7(2). ‡
- Friedman, M. 1970. The social responsibility of business is to increase its profits. *New York Times Magazine*, 13 September. ‡
- Fudenberg, D. and Levine, D. K. 1993. Self-confirming equilibrium. *Econometrica* 61(3). ‡
- Harvey, D. 2005. *A Brief History of Neoliberalism*. Oxford University Press. ‡
- Henrich, J., Boyd, R., Bowles, S., Camerer, C., Fehr, E., Gintis, H. and McElreath, R. 2001. In search of Homo economicus: behavioral experiments in 15 small-scale societies. *American Economic Review* 91(2). ‡
- Henrich, J. and Gil-White, F. J. 2001. The evolution of prestige: freely conferred deference as a mechanism for enhancing the benefits of cultural transmission. *Evolution and Human Behavior* 22(3). ‡
- Hofstadter, R. 1944. *Social Darwinism in American Thought*. ‡
- Jensen, M. C. and Meckling, W. H. 1976. Theory of the firm: managerial behavior, agency costs and ownership structure. *Journal of Financial Economics* 3(4). ‡
- Kropotkin, P. 1902. *Mutual Aid: A Factor of Evolution*. †
- Leonard, T. C. 2009. Origins of the myth of social Darwinism: the ambiguous legacy of Richard Hofstadter's *Social Darwinism in American Thought*. *Journal of Economic Behavior and Organization*. † (title seen; journal details not checked)
- MacKenzie, D. 2006. *An Engine, Not a Camera: How Financial Models Shape Markets*. MIT Press. ‡
- Maynard Smith, J. and Szathmáry, E. 1995. *The Major Transitions in Evolution*. Oxford University Press. ‡
- Meadows, D. 1999. *Leverage Points: Places to Intervene in a System*. The Sustainability Institute. ‡
- Ostrom, E. 1990. *Governing the Commons*. Cambridge University Press. †
- Polanyi, K. 1944. *The Great Transformation*. †
- Smith, A. 1759. *The Theory of Moral Sentiments*. †

*The example discussed in Section 6.7*
- Larsen, Dean, Halstead, Lifland, Greenblatt and Kokotajlo. 2026. *AI 2040: Plan A*, AI Futures Project, with its supplements (Deal Decline; Comparing Possible Plans; Capability Scaling Strategy; Verification Plan). ‡ (figures as checked by the handoff review; see EVIDENCE.md, E10)
