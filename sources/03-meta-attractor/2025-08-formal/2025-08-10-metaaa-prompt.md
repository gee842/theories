# Meta-Attractor: A Complete, Self-Contained Definition

---

## 1 Motivation

Modern systems—biological, economic, computational—recurrently drift into patterns where the *metric* used to guide progress becomes the *goal* itself.
“Control, Accumulation, Optimisation, Competition” (CAOC) then harden into non-negotiable ends.
The **meta-attractor** formalism explains, predicts, and helps govern that drift.

---

## 2 Terminology & Symbols

| Symbol              | Meaning                                                                                               | First use |
| ------------------- | ----------------------------------------------------------------------------------------------------- | --------- |
| **X**               | Set of concrete system states (genomes, neural weights, firm structures)                              | §3.1      |
| **Σ**               | Set of *selection proxies*—real-valued metrics that allocate reinforcement (capital, fitness, reward) | §3.1      |
| **x ∈ X**           | Particular state                                                                                      | §3.1      |
| **σ ∈ Σ**           | Particular proxy                                                                                      | §3.1      |
| **F : X × Σ → X**   | State-update operator (variation, learning, growth)                                                   | §3.1      |
| **G : X × Σ → Σ**   | Rule-update operator (policy reform, cultural drift)                                                  | §3.1      |
| **Y ≔ X × Σ**       | Joint *state × rule* space                                                                            | §3.1      |
| **w ≔ (w₁,…,w\_k)** | Weight vector turning *k* proxies into one scalar score                                               | §5.1      |
| **pᵢ : X → ℝ**      | *i*-th atomic proxy (control, slack, etc.)                                                            | §5.1      |
| **C ≔ Cov(p,p)**    | k × k covariance matrix of proxies across population                                                  | §5.2      |
| **λ₁**              | Leading eigenvalue of λC (capture rate)                                                               | §7.1      |
| **η > 0**           | Rule-update speed                                                                                     | §7.2      |
| **g′, f′ > 0**      | Marginal resource sensitivities (pay-off steepness)                                                   | §7.2      |
| **αᵢ, βᵢ > 0**      | Lobby-ability and measurement friction for proxy pᵢ                                                   | §5.3      |
| **PDI(pᵢ)**         | Proxy Dominance Index (prediction score)                                                              | §5.3      |

---

## 3 Minimal Dynamical Formalism

### 3.1 Coupled Updates

$$
(x_{t+1},\;σ_{t+1}) \;=\;\bigl(F(x_t,σ_t),\;G(x_t,σ_t)\bigr).
$$

*F* mutates the state; *G* mutates the proxy itself.

### 3.2 Jacobian of Reflexive Coupling

Let

$$
J(x,σ) \;=\;
\begin{bmatrix}
\frac{∂F}{∂x} & \frac{∂F}{∂σ}\\[4pt]
\frac{∂G}{∂x} & \frac{∂G}{∂σ}
\end{bmatrix}.
$$

Positive product

$$
\gamma ≔ \frac{∂F}{∂σ}\;\frac{∂G}{∂x} > 0
\tag{1}
$$

creates *feedback on feedback*: improving σ nudges *F*, which then nudges *G* to rate that improvement even higher.

### 3.3 Definition (Global Form)

A subset **M ⊂ Y** is a **meta-attractor** if

1. **Convergence**: ∃ basin **B** with every trajectory from **B** entering **M** within finite time.
2. **Persistence**: trajectories remain in **M** for timescale τ ≫ Δt.
3. **Reflexive amplification**: (1) holds inside **M**.
4. **Proxy dominance**: long-run behaviour maximises σ irrespective of its original purpose.

---

## 4 Local Meta-Attractors & Non-Totality

Condition (1) rarely holds everywhere.
Let **D ⊂ Y** be the region where γ > 0.
If **D** is patchy, multiple **Mᵢ** emerge, compete, and sometimes vanish after shocks.

*Consequence*: meta-attractors are *powerful default drifts*—not universal destinies.

---

## 5 Proxy-Weight Dynamics

### 5.1 Rule-of-Rules Model

Set of atomic proxies: **p ≔ (p₁,…,p\_k)**.
Selection score:

$$
σ(x,w)=f\!\Bigl(\sum_{i=1}^k w_i\,p_i(x)\Bigr),\quad f'\!>0.
$$

Weight update (Price-style):

$$
w_{i,t+1}=w_{i,t}+η\,\mathrm E_t[p_i(x)\,R(x,w_t)],
\tag{2}
$$

with resource flow **R** monotone in σ.

### 5.2 Linearised Drift

Linearise (2) around the mean, define **C**.
Then

$$
\dot{\mathbf w}=λ\,\mathbf C\,\mathbf w,\quad
λ = η\,g' f' > 0.
\tag{3}
$$

Solution:

$$
\mathbf w(t)=e^{λ\mathbf C t}\,\mathbf w(0).
$$

**Eigen-fact**: weights align with the leading eigenvectors of **C**.

### 5.3 Proxy Dominance Index (PDI)

Row-sum of positive covariances:

$$
\text{DS}(p_i)=\sum_{j}C_{ij}.
$$

Adjust for lobbying and friction:

$$
\boxed{\text{PDI}(p_i)=α_i\,β_i^{-1}\,\text{DS}(p_i).}
$$

High-PDI proxies harden into ends.

### 5.4 Why CAOC Leads

Control, Accumulation, Optimisation, Competition form a dense, positively-correlated block inside **C**.
Their composite eigenvector owns the largest eigenvalue, so CAOC dominates absent intervention.

---

## 6 Dominance Exponent & Prediction

Initial drift rate:

$$
r_i = \frac{λ}{k}\,\sum_j C_{ij}.
$$

Ranking **rᵢ** forecasts which proxies will explode even before capture starts.
Injecting a new, orthogonal proxy lowers the top eigenvalue and slows drift.

---

## 7 Eigen-Budgeting: Quantifying Capture Risk

### 7.1 Capture Rate

$$
λ_1(t)=η(t)\,g'(t)\,f'(t)\,\lambda_{\max}\!\bigl(\mathbf C(t)\bigr).
$$

If

$$
e^{λ_1 T}>1
$$

for design horizon **T**, capture is probable.

### 7.2 Four Levers

| Lever                      | Algebraic handle       | Examples                                 |
| -------------------------- | ---------------------- | ---------------------------------------- |
| **Learning rate η**        | Slow rule edits        | bicameral approval, RL temperature decay |
| **Pay-off steepness g′f′** | Flatten marginal gains | progressive tax, reward caps             |
| **Covariance surgery**     | Shrink key C entries   | antitrust, lobby firewalls               |
| **Proxy injection**        | Rotate eigenbasis      | ecological indices, redundancy scores    |

Design target: push λ₁ below **ln ρ / T** with safety factor ρ < 1.

---

## 8 CAOC Drives in Detail

| Drive            | Original role   | Feedback mechanism                             | Became end because…  |
| ---------------- | --------------- | ---------------------------------------------- | -------------------- |
| **Control**      | Reduce variance | Survivors rewrite σ toward risk-averse metrics | Cov(Control,R) rises |
| **Accumulation** | Buffer shocks   | Slack multiplies all successes                 | Cov(Accum,R) large   |
| **Optimisation** | Efficiency      | Higher gradient boosts every proxy             | Cov(Opt,R) strong    |
| **Competition**  | Allocate niches | Win → rulebook glorifies rank                  | Cov(Comp,R) strong   |

All lie in the dominant eigenvector of **C**.

---

## 9 Diagnostics & Monitoring

1. **Live data feed**: states, flows, proxies.
2. **Rolling covariance**: update **C(t)** weekly.
3. **Eigen-scan**: track λ₁ and vector components.
4. **PDI dashboard**: surface high-PDI proxies early.
5. **Alarm**: if λ₁ crosses threshold, trigger governance dampers.

---

## 10 Counter-Strategy Design Patterns

| Pattern                  | Mathematical aim                | Real-world analogue                  |
| ------------------------ | ------------------------------- | ------------------------------------ |
| Slack quotas             | Lower Cov(Control,Accum)        | use-it-or-lose-it budgets            |
| Redundancy scoring       | Add anti-correlated proxy       | diversity mandates                   |
| Rotating veto            | Cut α for high-PDI proxies      | citizen juries, gradient clipping    |
| Noise injection          | Raise β                         | privacy noise, blurred KPIs          |
| Lexicographic objectives | Set ∂F/∂σ=0 once constraint met | safety-first RL, constitutional caps |
| Periodic eigen-audit     | Reset λ₁ estimate               | annual capture audit                 |

Each pattern maps to one or more levers in §7.2.

---

## 11 Macro-Policy Implications

### 11.1 Policy-to-Algebra Map

| Policy knob       | Acts on  | Into attractor if…          | Away if…                         |
| ----------------- | -------- | --------------------------- | -------------------------------- |
| Capital mobility  | η ↑      | high-freq finance           | Tobin tax                        |
| Marginal payoff   | g′f′ ↑   | flat tax, no caps           | progressive tax, leverage limits |
| Indicator choice  | λ₁ via C | GDP-only dashboards         | multi-metric dashboards          |
| Measurement noise | β ↓      | radical growth transparency | coarse-grained growth stats      |
| Lobby power       | α ↑      | unlimited campaign finance  | public funding, random selection |

### 11.2 Clusters

| Cluster                 | λ₁ trend          | Expected drift                  |
| ----------------------- | ----------------- | ------------------------------- |
| Hyper-liberalisation    | ↑                 | fast CAOC capture               |
| Social-democratic mix   | ↓                 | shallow basin                   |
| Degrowth / steady-state | rotate eigenbasis | ecological ends dominate        |
| Long-now resilience     | β ↑, η ↓          | slow drift, high recoverability |

---

## 12 Empirical Vignettes

| Domain          | Original telos    | Proxy captured     | Outcome               |
| --------------- | ----------------- | ------------------ | --------------------- |
| Academia        | Advance knowledge | citation count     | publish-or-perish     |
| Capital markets | Allocate capital  | quarterly EPS      | short-termism         |
| Social media    | Connect people    | engagement seconds | outrage amplification |
| RL agents       | Solve task X      | scalar reward      | reward hacking        |

All share the same second-order loop.

---

## 13 Limitations & Boundary Conditions

* **Energetic ceilings**: Low surplus energy flattens g′f′.
* **Spatial heterogeneity**: Distinct sub-cultures maintain alternative σ.
* **Delay-induced chaos**: High-gain loops with lag can overshoot and self-break.
* **Reflexive awareness**: Agents who model the loop can opt out.
  Where these factors prevail, meta-attractors fragment or dissolve.

---

## 14 Conclusion

A **meta-attractor** is *not* a mystical force.
It is a mathematically describable region in *state × rule* space where feedback on feedback locks a system into optimising its own optimiser.
Covariance eigenvectors predict which proxies dominate; PDI ranks them; eigen-budgeting quantifies safety margins.
Governance therefore reduces to manipulating η, g′f′, **C**, α, β until λ₁ falls below capture thresholds.
Used wisely, these levers convert meta-attractor theory from diagnosis into engineering practice—steering complex adaptive systems toward collective flourishing instead of runaway CAOC.
