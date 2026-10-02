# Mathematical check of v3 (`main.tex`)

Scope: formal correctness only (statements against proofs in Appendices A and B, plus the numerics in Appendix C and the Figure 2 caption). Style and policy are not assessed.

Version checked: `main.tex` was edited while this review ran. The report refers to the version on disk at 23:41 on 2026-10-02. Two edits affect the formal content. Prop. 1 now states "$\phi_k$ equal", which closes one issue below. A new sentence after Prop. 5 on $f>0$ (line 192) is incorrect for part (iii); see 6.6. Later edits changed only citations and evidence text. Line numbers refer to that version.

How I checked: I re-derived every proof by hand. I re-ran `figures_v3.py`, and `checks.log` and `fig-rate.tex` came out byte-identical. I also wrote separate scripts for each counterexample below (kept in my scratchpad, not in the repo); their numbers are quoted inline.

---

## 0. Verdicts at a glance

| Item | Verdict |
|---|---|
| Lemma 1 (blindness) | CORRECT (one side claim in the text after Def. 2 is too broad, see 13) |
| Prop. 1 | CORRECT now that the statement says $\phi_k$ equal. (ii) is proved only for replicator dynamics, which matters for Thm 1 |
| Prop. 2 | CORRECT WITH MISSING ASSUMPTIONS ($\tau=0$, $\phi$ equal, equal shares, steady-state $V$, $n\ge2$). One small boundary error in (ii). The assumption $h\bar e<\rho$ really is needed (counterexample) |
| Prop. 3 | Formal parts (i)–(iv) CORRECT. The side claim "$L_i$ decreasing in $d_i$" is FALSE. The phrase "cannot invade from rarity" is ambiguous |
| Prop. 4 | (i) CORRECT WITH A MISSING ASSUMPTION ("otherwise identical"). (ii) OVERCLAIMED. (iii) MISSING ASSUMPTION $C_u'(0)>0$. (iv) argued, not proved. The Price caveat in the text cites the wrong part |
| Prop. 5 | (i) algebra CORRECT, but "certified uncaptured" is OVERCLAIMED unless $s_\dE(\cC)$ is the whole row. (ii) one small false edge case. (iii) the bound is CORRECT; the capture step has a fixable proof gap. (iv) CORRECT but not sharp, and needs $d(t)\ge d_0e^{\alpha t}$. **The rate law depends on $f=0$. The new $f>0$ sentence is FALSE for (iii).** The fragmentation factor $k$ is INCONSISTENT with Prop. 3 (it should be $k^2$) |
| Prop. 6 | CORRECT WITH A MISSING ASSUMPTION ($0\le\beta_{\rm out}\le\beta_{\rm in}<1$) |
| Thm 1 | OVERCLAIMED / partly FALSE. The payoff clause fails when $h\bar e\ge\rho$, which (C0) allows. Several hypotheses are hidden. "Captured before" must be made quantitative (counterexample). Branch 2 cites Prop. 6(v), which does not apply |
| Thm 2 | (a) FALSE as stated. "Stays above its floor" fails in the transient (counterexample with the paper's own parameters), and a low-load carrier must be present. (b) essentially CORRECT, but the (I4) witness needs two fixes |
| Cor. 1 | OVERCLAIMED. "Cannot establish" is argued, not proved. "Raises every carrier's absolute payoff" contradicts Prop. 4(ii) and leaves out the cost of correction. "Self-enforcing" contradicts Prop. 4 for (I2) |
| App. B: Lemma 2, Prop. 7(a)–(c) | CORRECT |
| App. B: Prop. 7(d) | CORRECT (the wording of the first clause is unclear) |
| App. B: Prop. 8(i), (ii) | CORRECT |
| App. B: Prop. 8(iii) | FALSE as stated (counterexample). It needs the remaining domains to stay captured |
| App. B: Prop. 9 (pause) | CORRECT. The argument for strictness of $\sigma(0)>1/R$ is incomplete but easy to fix |
| Numerics | Every quoted number reproduces. The caption's $t^\ast\approx6.8$ conflicts with the $t^\ast$ defined in Prop. 5. The Prop. 2 brute-force check never tests the restraint branch. The fragmentation check is circular |

---

## 1. Lemma 1 (Blindness): CORRECT

A relative rule is translation-invariant at each instant, so $F(p,\pi(t)+G(V(t))\mathbf 1)=F(p,\pi(t))$ and the share ODE is unchanged. For payoff-monotone rules, the sign of $\pi_k-\pi_l$ does not change. No issue.

---

## 2. Proposition 1

### 2.1 $\phi_k$ equal (fixed in the current version)
In the earlier version the statement did not assume $\phi_k=\phi_l$; the proof did. The current statement says "carriers differ only in their load ($\phi_k$ equal)", which is sufficient. For the record, without it the claim fails: race carrier $\phi=0,e=\bar e=1$; restrained carrier $\phi=2\nu,e=0$; then $\pi_{\rm restr}-\pi_{\rm race}=\nu>0$ and $E\to0$.

### 2.2 (ii) limsup bound: CORRECT
$\frac{d}{dt}\ln(p_k/p_l)=\nu(\bar e-e_l)>0$ is constant. With finitely many carriers this gives $p_l\to0$ for every $e_l<\bar e$, so $E\to\bar e$. Comparison with the logistic equation for $\dot W=W[\rho(1-W/K)-h(\bar e-\epsilon)]$ gives $\limsup V\le K(1-h(\bar e-\epsilon)/\rho)^+$. Letting $\epsilon\to0$ is legitimate. (iii) follows because $\limsup V<\Vmin$ forces $V<\Vmin$ eventually. Implicit: $V(0)>0$ and $p_{\rm race}(0)>0$ ("present").

### 2.3 Scope note (matters for Thm 1)
(ii) is proved only under replicator dynamics. Thm 1's (C1) says only "relative selection". For autonomous, continuous, relative and payoff-monotone rules the conclusion $E\to\bar e$ can be recovered: pairwise ratios are monotone, and interior rest points are excluded by the strict sign condition. But that argument is not in the paper. The simplest fix is to put replicator dynamics into (C1) (see 8).

---

## 3. Proposition 2 (weight on winning)

### 3.1 Algebra: CORRECT
$\pi_k-\bar\pi$ contains $G$ with weight $(1-\frac1n)-\frac{n-1}{n}=0$. $u_k=w\nu e_k-\frac\lambda n\nu\sum_{j\ne k}e_j+\omega K(1-hE/\rho)+$const, with $w=1+\lambda(n-1)/n$. $\partial u_k/\partial e_k=w\nu-\omega Kh/(n\rho)$, so the sign is that of $w-\theta/n$. Joint payoff depends only on $E$, with slope $n\nu(1-\theta)$. The gap in (iii) is $\omega K-[\nu\bar e+\omega K(1-h\bar e/\rho)]=\nu\bar e(\theta-1)$. Checked by brute force on 1485 profiles covering both branches ($\theta\in\{0.25,2,6,20\}$, $n\in\{2,3,5\}$, $\lambda\in\{0,0.5,2,6\}$, others' actions on a grid): zero mismatches.

### 3.2 Missing assumptions
The proof uses $\tau=0$, $\phi_k\equiv\phi$, equal shares ($E=\frac1n\sum_je_j$) and $V$ at its steady state $V=K(1-hE/\rho)$. None of these is stated. $\bar\lambda$ also needs $n\ge2$.

### 3.3 $h\bar e<\rho$ is necessary (it is stated; this confirms it is needed)
If $h\bar e\ge\rho$, then $V^\ast=K(1-hE/\rho)^+$ is kinked and (i) fails. Take $n=2$, $\lambda=0$, $\nu=K=\rho=\bar e=1$, $h=2$, $\omega=5$. Then $\theta=10$ and $w=1<\theta/n=5$, so the formula says restraint is dominant. But if the rival plays $\bar e$, then $E\ge\rho/h$ whatever $e_k$ is, $V^\ast=0$, and the best response is $\bar e$. Confirmed numerically.

### 3.4 Boundary error in (ii)
"at every $\lambda\ge0$ when $n\ge\theta$": at $n=\theta$ and $\lambda=0$, $w=\theta/n$ and every $e$ is a best response. So depletion is neither dominant nor the unique equilibrium.

### 3.5 "the eventual winner included"
In a symmetric static equilibrium there is no winner; all developers are identical. This is interpretation, not proof. It is harmless if it is kept out of the formal statement.

**Replacement (preamble, line 154, and statement):**
```latex
Selection is the limit of a contest in which only winning counts. Suppose $n\ge2$ symmetric developers ($\phi_k\equiv\phi$, $\tau=0$, equal shares, so that $E=\frac1n\sum_je_j$) choose $e_k\in[0,\bar e]$ to maximize $u_k=\pi_k+\lambda(\pi_k-\bar\pi)$, with the host at its steady state $V=K(1-hE/\rho)$, where ...
```
In (ii): `... whenever $\lambda>\bar\lambda=(\theta-n)/(n-1)$, hence at every $\lambda\ge0$ when $n>\theta$.`
In (iii): `In that equilibrium every developer has a lower absolute payoff than under joint restraint, by $\nu\bar e(\theta-1)$.`

---

## 4. Proposition 3 (control in the largest carriers)

### 4.1 (i)–(iv): CORRECT
- $M_{ij}=c_iL_i\hat R_{ij}=L_ia_i\hat b_{ij}/d_i$, and $\sum_iy_ia_i\zeta_i^\ast L_i=\chi q\,y^\top My$. Correct.
- $y^\top My=s^2\bar y^\top M\bar y$ (the own-share quadratic). Correct.
- $W'(0)>0\iff s>s^\ast$. For $s<s^\ast$, $W(q)<0$ for every $q>0$. $q^\ast=(\chi s^2\bar y^\top M\bar y-f)^+/\gamma$. Correct.
- $\ell(v)=L(v)/v$ is decreasing: $\mu(v)=2-2e^{-v}-v-ve^{-v}$, $\mu(0)=0$, $\mu'=e^{-v}(1+v)-1<0$. Correct.
- Scope: $\sum_{i,j\in\cS}\hat R_{ij}=|\cS|\hat\eta+|\cS|(|\cS|-1)\hat\varphi$. At $s=Y/|\cS|$ the return is $\chi cLY^2(\hat\varphi+(\hat\eta-\hat\varphi)/|\cS|)$. It increases in $|\cS|$ if and only if $\hat\varphi>\hat\eta$. Correct; "only if" could be "if and only if".

### 4.2 FALSE side claim (line 170): "$L_i$ ... decreasing in $d_i$"
$L_i=1-(1-e^{-v})/v$ with $v=\varepsilon_id_iT$ is **increasing** in $d_i$. Faster decay means support reaches its (lower) steady state sooner. Numbers: $v=0.1\Rightarrow L=0.048$; $v=1\Rightarrow L=0.368$; $v=5\Rightarrow L=0.801$. What decreases is $L_i/d_i$, and hence $M_{ij}$, which is what the proof of (iii) actually uses.

**Replacement:**
```latex
where $\hat R_{ij}=a_i\hat b_{ij}/(c_id_i)$ and $L_i=1-(1-e^{-\varepsilon_id_iT})/(\varepsilon_id_iT)\in(0,1)$ is the share of the steady-state return realized within a horizon $T$; $L_i$ increases with $d_i$, but $M_{ij}$, which is proportional to $L_i/d_i$, decreases with $d_i$ (Appendix~\ref{app:proofs}).
```

### 4.3 "capacity cannot invade from rarity" (ambiguous)
What is proved concerns the carrier's decision share $s$, not how rare the trait is. A capacity mutant that arises inside a large carrier has $s>s^\ast$ and is favored however rare it is.

**Replacement:** `A carrier with $s<s^\ast$ that carries capacity is selected against relative to an otherwise identical carrier without it, so capacity cannot spread through carriers below the size threshold.`

### 4.4 Minor
$W$ is a total payoff (it scales with $s$), while replicator fitness is per unit of share ($W/s$). Signs, $s^\ast$ and $q^\ast$ are unaffected because $s$ is fixed. Only the Price-equation gloss in (i) is loose when carriers differ in size.

---

## 5. Proposition 4 (correction not supplied from inside)

### 5.1 (i): CORRECT WITH A MISSING ASSUMPTION
The question was whether two carriers of the same practice that differ only in $u$ are affected identically by the change in $d$. **Yes**, if they also have the same share, profile $\bar y$ and capacity $q$. Shared support acts per decision, keyed support depends on $(q,y,d)$, and $G(V)$ is common, so the payoff difference is $C_u(u_l)-C_u(u_k)<0$. But the statement says only "Among carriers of the same practice". Carriers with the same practice but different $q$ (keyed support) or different $\bar y$ are affected differently, and a higher-$u$ carrier with larger keyed rents can grow faster.

**Replacement:** `(i) Among carriers of the same practice that are otherwise identical (same share, profile and capacity $q$), those investing more in correction are selected against under any payoff-monotone rule, whatever the effect of correction on the field.`

### 5.2 (ii): OVERCLAIMED
The proof covers only the rule-support channel ("appropriable and shared support decline in $d$"). But correction that de-captures $\dS$ restores liability, which raises $V$ and hence $G(V)$ for the incumbent too. Derivation: if correction ends the race, the incumbent gains $\nu\bar e(\theta-1)$ (Prop. 2(iii)) and loses its rule-support rent $\varrho$. With $\nu=\bar e=1$, $\theta=3$, $\varrho=0.5$, its absolute payoff **rises** by $1.5$. This also clashes directly with Cor. 1 ("raises every carrier's absolute payoff"); see 10.

**Replacement:** `(ii) For a carrier that holds rule support, correction lowers the rule-support component of its payoff; with $V$ and $\tau$ held fixed its absolute payoff falls, so incumbents oppose correction unless the gain it brings through $G(V)$ exceeds the support they lose.`

### 5.3 (iii): MISSING ASSUMPTION $C_u'(0)>0$
"fails for small $p_k$" needs $C_u'(0)>0$. With $C_u(u)=u^2/2$, every challenger invests $u_k=\delta p_kG_k'(d)>0$. Free-riding then holds only in aggregate: total contribution $\sum_k\delta p_ku_k=\delta^2G'\sum_kp_k^2\to0$ as the field disperses. (Notation: $G_k'$ collides with $G(V)$.)

**Replacement:** `(iii) If $C_u'(0)>0$, a challenger invests only if its own share of the benefit exceeds the marginal cost, which fails for small shares; in general each challenger's contribution to $d$ is $O(p_k^2)$, so dispersed challengers free-ride.`

### 5.4 (iv): argued, not proved
That the return has the form of Eq. (W) with $\chi_u$ in place of $\chi$ is fine. "It replaces one captured configuration with another" is not derived anywhere.

**Replacement:** `... is control in the sense of Proposition~\ref{prop:control}: it is selected only above the size threshold, and the support it installs is keyed to the corrector rather than restoring baseline rules.`

### 5.5 Multilevel caveat (text, line 184): wrong part cited
Once one practice dominates, the between-group variance vanishes. What then governs the mean of $u$ is the within-group term, which is negative by **(i)**. Part (ii) is about incumbents' absolute payoffs, and in the model the alternative practice is the baseline and holds no rule support, so (ii) does not even apply to it when it dominates.

**Replacement:** `Correction can rise transiently by riding on the success of the practice it favors, the between-group term of the Price equation. Once that practice dominates, the between-group variance vanishes and the within-group term, negative by part~(i), governs; if the dominant practice holds rule support, part~(ii) adds the incumbent's opposition.`

---

## 6. Proposition 5 (required independent correction and its rate)

### 6.1 (i) algebra: CORRECT; "certified uncaptured": OVERCLAIMED
$s_\dE=A/(c_\dE d)+Z/(c_\dE d^2)$, so $s_\dE<1\iff c_\dE d^2-Ad-Z>0\iff d>d^\ast$. Correct, including $q^\ast=\chi\hat Y/(\gamma d)$ from $M=\hat A/d$, which needs $L_i=1$ and the same $d$ in **every row $i$ with $\hat b_{ij}\neq0$**. That holds if cultivated conversion enters only corrector domains; this is not stated.

But $s_\dE(\cC)<1$ does not certify that $\dE$ stays uncaptured. Prop. 7(b) needs the **row sum** $\sum_jR_{\dE j}<1$. If $\dE$ also receives conversion from outside $\cC$, including from itself, it can stay captured. Counterexample: $\cC=\{\dD\}$ captured, $R_{\dE\dD}=0.5$ (so $s_\dE(\cC)<1$) and $R_{\dE\dE}=0.8$, with all other rates 1. Starting from $x_\dE(0)=0.9$, $x_\dE\to1$ (simulated). The same gap appears in Thm 2(a), whose proof says "(I2) in $\dS$ gives $\sum_jR_{\dS j}<1$", which does not follow from $d>d^\ast$ as defined.

**Is $L_i=1$ consistent with $L_i\in[0,1)$?** Yes, as the limit $T\to\infty$. For finite $T$, $L_i<1$ only lowers $q^\ast$, so $d>d^\ast$ remains **sufficient** but (i)'s "only if" is lost. Part (iii) survives because $L$ stays bounded below; even if $d\to0$, $L/d\to\varepsilon T/2$.

**Replacement (setup, line 186):**
```latex
Let a set $\cC\not\ni\dE$ of domains be captured by a dominant carrier that holds it ($y_j=1$ for $j\in\cC$), and let all conversion into $\dE$ originate in $\cC$, so that $s_\dE(\cC)$ is the row sum of $\dE$ and Proposition~\ref{prop:cert}(b) applies. Let cultivated conversion enter only the corrector domains, where independent correction acts at a uniform rate $d$; take the long-horizon limit $T\to\infty$ ($L_i\to1$; for finite $T$, $q^\ast$ is smaller and $d>d^\ast$ remains sufficient) and quadratic cost ($f=0$), and let capacity adjust to ...
```
To keep a general profile instead, write $Z=a_\dE\chi\hat Y\sum_{j\in\cC}\hat b_{\dE j}y_j/\gamma$, which is consistent with the derivation of Prop. 3 (see 6.7).

### 6.2 (ii): small false edge case
"with equality only if $\chi\hat Y=0$": equality holds if and only if $Z=0$. With $\hat B=\sum_j\hat b_{\dE j}=0$ and $\chi\hat Y>0$ there is equality. The scope claim also needs "at fixed share per domain"; at fixed total size it needs $\hat\varphi>\hat\eta$ (Prop. 3(iv)).

**Replacement:** `... with equality if and only if $Z=0$; $d^\ast$ rises with appropriability, with the dominant carrier's size and, at fixed share per domain, its scope, and as $\gamma$ falls.`

### 6.3 (iii) bound: CORRECT
$d^\ast\ge\sqrt{Z/c_\dE}$ because $A\ge0$. $Z(t)=Z_0e^{gt}$, so $d^\ast(t)\ge Se^{gt/2}>d_0e^{\alpha t}\ge d(t)$ for $t>t^\ast$. The formula for $t^\ast$ is correct. Numerically, $d-d^\ast$ changes sign exactly once for $\alpha=0.05$ ($t=6.755$) and $\alpha=0.08$ ($t=21.531$), both before the bounds 9.163 and 22.907.

### 6.4 (iii) "a seeded evaluation domain is then captured": proof gap, fixable
Prop. 8(i) is a constant-parameter result. Here $b_{\dE j}(t)=b^0+q^\ast(t)\hat b$ and $d(t)$ vary. A uniform margin is still available, and the following argument works with no lower bound on $d$:

**Replacement (proof of (iii), after "Then $s_\dE(\cC)>1$"):**
```latex
Since $d(s)\le d_0e^{\alpha s}$, $q^\ast(s)\ge\chi\hat Ye^{(g-\alpha)s}/(\gamma_0d_0)$. Once $x_j\ge\frac12$ on $\cC$, integrating Eq.~(\ref{eq:r}) over the last $\Delta=1/(\varepsilon_\dE d_0e^{\alpha t})$ time units, on which $\int d\le1/\varepsilon_\dE$, gives $a_\dE r_\dE(t)\ge c\,e^{(g-2\alpha)t}$ for some $c>0$; hence $a_\dE r_\dE-c_\dE\to\infty$ and $\operatorname{logit}x_\dE\to\infty$ from any $x_\dE>0$.
```
Simulated with the Figure 2a parameters, $\kappa=\varepsilon=1$ and $x_\dE(0)=10^{-3}$: $\alpha=0.05$ gives $x_\dE\to1$ by $t\approx40$, and $\alpha=0.12$ gives $x_\dE\to0$.

### 6.5 (iv) converse: CORRECT but needs $d(t)\ge d_0e^{\alpha t}$, and is not sharp
(iii) assumes $d(t)\le d_0e^{\alpha t}$. The converse needs the lower bound. Sharp version: if $\alpha\ge g/2$, then $d^\ast(t)e^{-\alpha t}=[Ae^{-\alpha t}+\sqrt{A^2e^{-2\alpha t}+4c_\dE Z_0e^{(g-2\alpha)t}}]/(2c_\dE)$ is nonincreasing, so $d_0>d^\ast(0)$ suffices. This is weaker than $d_0>A/c_\dE+S$. With the Figure 2a parameters, $d_0\in\{0.81,0.85,0.9\}<0.9325$ all keep the certificate on $[0,1000]$ for $\alpha\in\{0.10,0.12\}$. Together with (iii) this gives a clean dichotomy.

**Replacement:** `(iv) Conversely, if $\alpha\ge g/2$ and $d(t)\ge d_0e^{\alpha t}$ with $d_0>d^\ast(0)$, the certificate holds for all $t\ge0$. Hence, for $d(t)=d_0e^{\alpha t}$, the certificate holds for all $t\ge0$ if and only if $\alpha\ge g/2$ and $d_0>d^\ast(0)$.`

### 6.6 HIGH: the half-rate law depends on $f=0$, and the new $f>0$ sentence (line 192) is false for (iii)
With $C(q)=fq+\gamma q^2/2$ and $L=1$, $q^\ast(d)=(\chi\hat Y/d-f)^+/\gamma$. Capacity is cultivated only while $d<\chi\hat Y/f$. Equivalently, the size threshold $s^\ast=\sqrt{fd/(\chi\bar y^\top\hat A\bar y)}$ **rises with $d$**. In that range the algebra does give $A'=A-a_\dE f\hat B/\gamma$, as the sentence says. But $A'\to-\infty$ as $\gamma\to0$, so the bound $d^\ast\ge\sqrt{Z/c_\dE}$ that (iii) relies on fails. In fact $d^\ast(t)\to\max\{A/c_\dE,\chi\hat Y/f\}$: a **level**, not a growth rate.

Numbers (Figure 2a parameters, $f=0.1$, so $\chi\hat Y/f=8$):
- required $d$ at $t=0,20,50,100,200$ is $0.77,3.61,7.95,8.00,8.00$, against $0.8,4.8,94,1.4\times10^4,3\times10^8$ for $f=0$;
- a constant $d=9$ ($\alpha=0<g/2$) gives $s_\dE=0.033$ for all $t$, so the certificate never fails;
- at $t=10$, $A'=-0.069$ and the root is $1.685<\sqrt{Z/c_\dE}=1.719$, so the bound used in (iii) fails.

If $f$ also falls, $f=f_0e^{-g_ft}$, the required growth rate is $\min\{g_f,g/2\}$ (numerically 0.05 for $g_f=0.05$ and 0.10 for $g_f=0.15$, with $g=0.2$). Sufficiency: $\alpha\ge g_f$ and $d_0>\max\{A/c_\dE,\chi\hat Y/f_0\}$ keep $q^\ast=0$ for all time. Necessity: $\alpha<\min\{g_f,g/2\}$ gives $s_\dE\sim e^{(g-2\alpha)t}\to\infty$.

Consequences:
1. "half as fast" in the abstract, the contributions, the end of Section 4, Thm 2 (I2), the instruments list and Table 3 (C3) all hold only when no part of the cost of control is untouched by AI.
2. Thm 1's (C2) "held by a carrier above the size threshold" presupposes $f>0$, while the Prop. 5 that Thm 1 relies on assumes $f=0$. Under (C2) with fixed $f>0$, growing $d$ eventually pushes every carrier below the threshold.

**Replacement for line 192 (first sentence):**
```latex
With a fixed marginal cost $f>0$ that AI does not lower, capacity is cultivated only while $d<\chi\hat Y/f$, that is, while the dominant carrier is above the size threshold, which rises with $d$. In that range (i) holds with $A$ replaced by $A-a_\dE f\sum_{j\in\cC}\hat b_{\dE j}/\gamma$, but as $\gamma\to0$ the requirement converges to the level $\max\{A/c_\dE,\chi\hat Y/f\}$, so the rate law (iii) needs the whole cost of control to fall: if $f$ falls at rate $g_f$, the required growth rate is $\min\{g_f,g/2\}$.
```
Then either keep $f=0$ as a standing assumption in Thm 1 (C2/C3) and Thm 2 (I2), or state the rate as $\min\{g_f,g/2\}$ throughout.

### 6.7 Fragmentation factor (line 192): INCONSISTENT with Prop. 3
In Prop. 3's derivation, capacity converts the carrier's **own** success: $\dot\zeta_i=\varepsilon_i(\chi q\sum_j\hat b_{ij}y_j-d_i\zeta_i)$. Prop. 5's $Z$ uses $\hat B=\sum_{j\in\cC}\hat b_{\dE j}$, with no $y_j$. The two agree only when $y_j=1$ on $\cC$.

Split the carrier into $k$ equal parts. Each part has $\hat Y/k^2$, hence $q^\ast/k^2$, and converts its own success $y_j/k$. Total cultivated conversion is $k\cdot k^{-2}\cdot k^{-1}=k^{-2}$ times the original. The paper's $1/k$ comes from mixing own-success returns with whole-practice conversion. Under a consistent whole-practice model the return would be linear in own share, and splitting would leave the total unchanged. The direction of the claim survives; the factor does not.

**Replacement:** `Splitting a dominant carrier into $k$ equal parts divides cultivated conversion by $k^2$: each part's selected capacity falls by $k^2$, because the return is quadratic in own share, and each part converts only its own success.` The script line `total = k*(s/k)**2` should then become `k*(s/k)**3`, or better, be computed from the model.

---

## 7. Proposition 6 (detection)

All five parts hold for $0\le m\le1$.

- (i): the threshold $(\Valarm-mK)/(1-m)$ has derivative $(\Valarm-K)/(1-m)^2<0$ in $m$. Correct.
- (ii): for $\Vmin\le V\le\Valarm$ and $m>\mfl$, $\tilde V\ge\Vmin+m(K-\Vmin)>\Valarm$. Correct; the strict and weak inequalities are right, so the alarm does not fire even at $V=\Vmin$. For $V>\Valarm$ the proof uses $\tilde V\ge V$, which needs $m\ge0$.
- (iii): correct. Using "for all $t$" is sufficient; "whenever $V(t)\le\Valarm$" (with $m\ge0$) is enough. As stated, the hypothesis carries the ordering "capture before evidence", which is fine.
- (iv): correct. The threshold $\Valarm/K$ is sharp: if eventually $m\ge m_2>\Valarm/K$, then $\tilde V\ge mK>\Valarm$.
- (v): the formula matches simulation to three decimals for $m\in\{0.1,0.3,0.5\}$. It needs $0\le m<\Valarm/K$.

**Missing assumption.** Nothing rules out $\beta_{\rm out}<0$, and then $m<0$ is possible above the band. Example: $V=0.7$, $m=-0.5$ gives $\tilde V=0.55\le\Valarm$, so the alarm fires above the band and (ii)'s "does not fire before" holds vacuously rather than as intended. (iii) also uses $m\le1$ for monotonicity in $V$.

**Replacement (line 198):** `... the rest are formed on shared material and are biased by $\beta_{\mathrm{out}}$, with $0\le\beta_{\mathrm{out}}\le\beta_{\mathrm{in}}<1$:`

**Remark 1 (indistinguishability), minor.** The interval upper end $\tilde V$ corresponds to $m=0$. That is right only if $\beta_{\rm out}$ is also unknown in $[0,\beta_{\rm in}]$. If $\beta_{\rm out}$ is known, the upper end is $(\tilde V-\beta_{\rm out}K)/(1-\beta_{\rm out})$. Say which is meant.

---

## 8. Theorem 1 (No viable winner): OVERCLAIMED, payoff clause FALSE in part

How the proof chains: Prop. 1, then Props. 3–4, then Prop. 5(iii) giving $x_\dE\to1$, then Prop. 6(ii) giving silence, then Prop. 1(iii) giving the crossing. Branch 1 needs only the capture of $\dE$: by (C1), $\tau=0$ until an alarm and no alarm fires, so the capture of $\dS$ is not used. The chain is sound once the following are fixed.

1. **Payoff clause is FALSE when $h\bar e\ge\rho$, which (C0) allows.** Prop. 2(iii) assumes $h\bar e<\rho$. In general the limiting loss is $\omega K\min\{1,h\bar e/\rho\}$ against a gain of $\nu\bar e$. Counterexample: $\rho=h=K=\nu=1$, $\bar e=3$, $\omega=2$, $\Vmin=0.3$. (C0) holds ($3>0.7$) and $\theta=2>1$, but $V\to0$ and the race payoff $\nu\bar e=3$ exceeds the joint-restraint payoff $\omega K=2$. Also, $\theta$ is defined only for linear $G$, which Thm 1 does not assume. The clause also leaves out the dominant carrier's rule-support rents (inside $\phi_k$), which Prop. 4(ii) says are real.
2. **"Captured before the host reaches the alarm level" must be quantitative.** Prop. 6(ii) needs $m(t)>\mfl$ throughout the band, that is $x_\dE(t)>\bar x=(\mfl-\beta_{\rm out})/(\beta_{\rm in}-\beta_{\rm out})$; $x_\dE\to1$ is not enough. Counterexample with the Figure 2b parameters ($\beta_{\rm in}=0.5$, $\beta_{\rm out}=0.05$, so $\bar x=0.841$): $x_\dE$ logistic with midpoint 25 and rate 0.01, a majority before $t_A$ and tending to 1, has $x_\dE(t_A)=0.53$. The alarm fires at $t=44.9$, **before** the floor crossing at $t=53.2$. (With the paper's rate 0.25 the condition is loose: midpoints up to 37 still give silence.)
3. **Hidden hypotheses** needed for Prop. 5(iii): a captured set $\cC\not\ni\dE$ ($x_j\to1$; who captures $\cC$, for example $\dD$, is not derived from the carrier model); $\hat B>0$ and $Z_0>0$; quasi-static $q=q^\ast(t)$; $f=0$ (see 6.6); $\dE$ (and, for branch 2, $\dS$) seeded. For Prop. 1(ii): replicator dynamics, $\phi$ equal, a race carrier present.
4. **Branch 2 cites Prop. 6(v)**, which assumes $\dot V=-\ell V$. That is not the host dynamics. Cite 6(i) for "delayed". It also relies on Prop. 8(iii), which is false as stated (see 11.2). The branch is a disjunction ("crossed unless ...") and so does not establish non-viability. The title "No viable winner" and the abstract's "cannot correct itself" overstate what the theorem delivers: a conditional (ordering plus $\beta_{\rm in}>\mfl$) and a necessary condition for branch 2.
5. The text after the theorem ("capture of correctors arrive within a time $t^\ast$") is not quite right. $t^\ast$ bounds when the **certificate** fails; capture ($x_\dE\to1$) follows with no time bound.

**Replacement statement:**
```latex
\begin{theorem}[No viable winner]\label{thm:fail}
Assume (C0) Eq.~(\ref{eq:C0}); (C1) replicator selection among carriers that differ only in their load, a race-strategy carrier present, and $\tau=0$ unless an alarm fires; (C2) appropriable control, $\chi>0$, with every part of the cost of control falling with AI ($f=0$ in Proposition~\ref{prop:rate}); (C3) the hypotheses of Proposition~\ref{prop:rate}(iii) for $\dE$, with $\cC$ captured and $\dE$ seeded, so that $x_\dE\to1$; and (C4) $0\le\beta_{\mathrm{out}}<\mfl<\beta_{\mathrm{in}}<1$. If evaluation is captured before the evidence, in the sense that $x_\dE(t)>(\mfl-\beta_{\mathrm{out}})/(\beta_{\mathrm{in}}-\beta_{\mathrm{out}})$ whenever $\Vmin\le V(t)\le\Valarm$, the host crosses its floor before any alarm. If moreover $G(V)=\omega V$ and $\omega K\min\{1,h\bar e/\rho\}>\nu\bar e$ (for $h\bar e\le\rho$: $\theta>1$), every carrier's limiting payoff (\ref{eq:pi}), with $\phi_k$ the same in both outcomes, is lower than under joint restraint. If instead $\beta_{\mathrm{in}}\le\mfl$, the alarm is delayed (Proposition~\ref{prop:detect}(i)), and the floor is crossed unless $\tau_d+\tau_r$ fits the remaining window and the liability is not re-absorbed (Proposition~\ref{prop:reform}(iii)).
\end{theorem}
```

---

## 9. Theorem 2 (invariants)

### 9.1 (a) Sufficiency: FALSE as stated
1. **Transient.** Even with (I1) in force from $t=0$, $x_\dS\equiv0$, no capture and no masking, $E$ falls only at the speed of selection while $V$ keeps falling. Counterexample with the paper's own Figure 2b host parameters: $\rho=0.05$, $h=0.08$, $K=1$, $\Vmin=0.3$, $\nu=0.08$, $\tau=2\nu$, two carriers ($e=1$ and $e=0$), replicator dynamics, $p_{\rm race}(0)=0.99$, **$V(0)=K=1$**. The minimum of $V$ is $0.14<\Vmin$; afterwards $V\to1$. With $V(0)=0.35$ and $p_{\rm race}(0)=0.95$: minimum $0.15$. "Stays above its floor from the start for anticipated harms" is false. What is proved is $\liminf V>\Vmin$ (eventual viability).
2. **A low-load carrier must be present.** The proof uses "$\min_ke_k=0$". If every carrier plays $\bar e$, liability lowers all payoffs equally, shares do not move, $E=\bar e$, and $V\to K(1-h\bar e/\rho)^+<\Vmin$. The statement needs a carrier with $he_{\min}<\rho(1-\Vmin/K)$ present.
3. **Selection rule.** "$E(t)\to\min_ke_k$" is proved for replicator dynamics, not for arbitrary payoff-monotone rules (as in 2.3).
4. **Certificate.** "(I2) in $\dS$ gives $\sum_jR_{\dS j}<1$" needs $d^\ast$ to be built from the whole row (6.1) and a uniform margin $d\ge(1+\delta)d^\ast$. Prop. 7(b) uses a fixed negative margin, and pointwise $d(t)>d^\ast(t)$ with $d-d^\ast\to0$ does not give one.
5. For unanticipated harms the proof says "(I3) places decision and reversal inside the window". This is true only if "reversal" includes the selection transient in item 1. Say so.

**Replacement for (I2) and (a):**
```latex
(I2) \emph{independent correctors}: in $\dE$ and $\dS$, $d(t)\ge(1+\delta)\,d^\ast(t)$ for some $\delta>0$, with $d^\ast$ computed from the full row of conversion into each domain; when every part of the cost of control falls at rate $g$, this requires independent correction to grow at least at rate $g/2$;
...
(a) \emph{Sufficiency.} Let selection be replicator dynamics among carriers that differ only in their load, with a carrier of load $e_{\min}$, $he_{\min}<\rho(1-\Vmin/K)$, present. Under (I1)--(I4) the effective liability $\tau(1-x_\dS)$ exceeds $\nu$ after a finite time, depletion is selected against, $E(t)\to e_{\min}$ and $\liminf_tV(t)>\Vmin$: for anticipated harms from the outset, and for unanticipated ones after an alarm that fires above the floor. The host stays above the floor at every $t$ if, in addition, it does so during the transient in which $E$ falls (for instance if carriers switch to restraint as a best response); for unanticipated harms this transient is part of the reversal time in (I3).
```

### 9.2 (b) Indispensability: essentially CORRECT; consistency of each witness checked
- **(I1) dropped**: $\tau=0$. (I2) and (I3) hold, with no capture and no masking. Prop. 1 plus (C0) gives the crossing. Consistent.
- **(I2) dropped**: $d<d^\ast$ in $\dS$ only, with $d>d^\ast_\dE$ so that $\dE$ stays uncaptured and (I3) can hold. Consistent. Use Prop. 8(i) (constant parameters), not Prop. 5(iii). Prop. 1 is applied with $\tau_{\rm eff}(t)\to0$ rather than $\tau=0$; the proof extends because eventually $\nu-\tau_{\rm eff}>\nu/2$. State this.
- **(I3) dropped**: unanticipated harm, $\dE$ uncaptured, $\beta_{\rm out}>\mfl$. Then $m\ge\beta_{\rm out}>\mfl$, so (ii) applies. No alarm means no liability, so (I1) is formally satisfied, and (I2) holds. Consistent.
- **(I4) latency**: $\dot r_\dS\ge-\varepsilon_\dS d'r_\dS$ gives $r_\dS(t)\ge r_\dS(t_1)e^{-\varepsilon_\dS d'(t-t_1)}$, so $a_\dS r_\dS>c_\dS$ and $\dot x_\dS>0$ for at least $\ln(a_\dS r_\dS(t_1)/c_\dS)/(\varepsilon_\dS d')$. **Correct.** Simulated: bound 0.462, actual 0.909. Two fixes:
  1. (I3) cannot "come into force" at $t_1$ if $\dE$ is captured with $\beta_{\rm in}>\mfl$, because then $m(t_1)\approx\beta_{\rm in}$. The witness must take $\dE$ uncaptured, or $\beta_{\rm in}<\mfl$. It also needs $x_\dS(t_1)>1-\nu/\tau$, so that $\tau(1-x_\dS)<\nu$ throughout.
  2. The disjunct "if $V(t_1)$ is close enough to $\Vmin$" is not a valid witness for (I4). By 9.1(1) the floor can then be crossed even without capture. Use only the $\varepsilon_\dS$-small branch, with $V(t_1)$ chosen so that the uncaptured system stays above the floor.

**Replacement (proof, (I4) sentence):**
```latex
\emph{(I4).} Let $\dS$ be captured at $t_1$, with $a_\dS r_\dS(t_1)>c_\dS$ and $x_\dS(t_1)>1-\nu/\tau$, when (I1)--(I3) come into force ($\dE$ uncaptured, or $\beta_{\mathrm{in}}<\mfl$), and choose $V(t_1)$ such that the host would stay above its floor from $x_\dS(t_1)=0$. Since $\dot r_\dS\ge-\varepsilon_\dS d'r_\dS$, $x_\dS$ keeps rising and $\tau(1-x_\dS)<\nu$ for at least $\ln(a_\dS r_\dS(t_1)/c_\dS)/(\varepsilon_\dS d')$, which exceeds the time to cross the floor once $\varepsilon_\dS$ is small enough.
```

---

## 10. Corollary 1 (cooperation is necessary): OVERCLAIMED

1. **"No carrier can establish (I1)–(I4) by its own choices"** is not proved. The proof shows that unilateral contributions are **selected against** (Props. 1 and 4(i)) and are not individually rational for small carriers (4(iii)). It does not show they are infeasible. In Prop. 4's own model a carrier with large $p_k$ can raise $d$ by $\delta p_ku_k$ above $d^\ast$. "Funding of a corrector is conversion $b_{ij}>0$" also contradicts Prop. 4, where a carrier's investment $u$ **raises $d$**. That is a modelling choice made to fit the conclusion. For $\tau$, $\chi$ and $m$, "not a carrier's choice" is true by the model's definition, not by a result.
2. **"When $\theta>1$ the arrangement raises every carrier's absolute payoff (Prop. 2(iii))"** has three problems:
   - (a) it needs $G$ linear and $h\bar e<\rho$ (see 8.1);
   - (b) it directly contradicts Prop. 4(ii), which says correction, part of the arrangement, lowers incumbents' absolute payoffs; the corollary leaves out the rents lost;
   - (c) it leaves out the cost of the independent correction the arrangement funds. By (I2), $d(t)\ge Se^{gt/2}$ grows exponentially while the gain $\nu\bar e(\theta-1)$ is constant, so if the cost is increasing in $d$ (and does not itself fall with AI), the net eventually turns negative.
3. **"Self-enforcing for as long as (I2)–(I4) keep the corrector independent"**: only the first-order part is self-enforcing. Under (I1), $\nu-\tau(1-x_\dS)<0$, so restraint is a best response; correct. But (I2) is a second-order public good, which Prop. 4 shows is **not** supplied from inside. The qualifier assumes away the part that is not self-enforcing. The same overclaim appears in the "Rivals cannot cooperate" paragraph (line 306): "it raises every party's absolute payoff, and once in force it is enforced by the payoffs it creates."

**Replacement:**
```latex
\begin{corollary}[Cooperation is necessary]\label{cor:coop}
No carrier's unilateral contribution to (I1)--(I4) is favored by selection: its unilateral restraint is selected against (Proposition~\ref{prop:first}); its unilateral investment in correction is selected against (Proposition~\ref{prop:correction}(i)) and, for an incumbent, lowers its rule-support payoff (Proposition~\ref{prop:correction}(ii)); and support it gives a corrector in a form keyed to its practice is conversion into that corrector. The invariants concern $\tau$, $d$, $\chi$ and $m$, which all carriers share; they can be sustained only by an arrangement that binds all carriers, including the states in which they operate, and supplies correction from outside their competition. When $G(V)=\omega V$, $h\bar e<\rho$ and $\theta>1$, joint restraint raises each carrier's payoff (\ref{eq:pi}) by $\nu\bar e(\theta-1)$ relative to the race; the arrangement leaves every carrier better off when this gain exceeds its share of the cost of correction and, for incumbents, the rule-support payoff that correction removes. Once (I1) is in force restraint is each carrier's best response; (I2)--(I4) are not self-enforcing (Proposition~\ref{prop:correction}) and must be maintained by the arrangement.
\end{corollary}
```
Line 306 replacement: `... it does not ask any party to sacrifice for another: when $\theta>1$ the gain from a viable host exceeds the private gain from racing, and once liability is in force restraint is each party's best response; the independent corrector, however, must be maintained by the arrangement itself.`

---

## 11. Appendix B

### 11.1 Lemma 2, Prop. 7: CORRECT
- **Lemma 2.** The faces are invariant, $r\ge0$, and $\limsup r_i\le\sum_jb_{ij}/d_i$. The off-diagonal Jacobian entries $\kappa_ia_ix_i(1-x_i)$ and $\varepsilon_ib_{ij}$ are $\ge0$ and all others are zero, so the Kamke condition holds. Correct.
- **Prop. 7(a).** At $Z_\cC$, $\partial\dot x_i/\partial r_i=0$, so the Jacobian is block lower-triangular with eigenvalues $\mp\kappa_ic_i(s_i(\cC)-1)$ and $-\varepsilon_id_i$, using $a_ir_i=c_is_i(\cC)$. The hyperbolicity and stability criteria are correct.
- **Prop. 7(b).** Margin $c_i(\sum_jR_{ij}-1)/2<0$. Correct, for constant parameters.
- **Prop. 7(c).** Checked: every row sum exceeds 1; a set $\cC\ni1$ with $\cC\ne\cD$ is invaded by some $i$ with $R_{i1}>1$; a nonempty $\cC\not\ni1$ has $s_i(\cC)=R_{ii}<1$. Correct. "Configuration" means the corner equilibria $Z_\cC$; interior equilibria are not covered, which is fine as defined.
- **Prop. 7(d).** The pruning induction is correct. Barring ties, the core is internally sustaining and uninvadable, since $s_k(\core)\le s_k(\cC_m)<1$ for pruned $k$. Internally sustaining sets are never pruned. The wording of the first clause, "no capture attracts every state with all shares below one", is unclear; what is proved is stronger.

**Replacement (d), first clause:** `(d) If $\core(\cD)=\emptyset$, every state with all shares below one converges to $Z_\emptyset$; otherwise, ...`

### 11.2 Prop. 8 (cascades and reforms)
- **(i)** Correct (induction with $\liminf r_i\ge\sum_{j\in\cS_k}b_{ij}/d_i$).
- **(ii)** Correct, via comparison (Lemma 2) and then pruning. The re-absorption clause is local, near $Z_\cC$. Correct.
- **(iii) FALSE as stated.** "The domains still captured" may stop being captured once domain $i$ is reset, if they depend on $i$. Counterexample with $D=2$, $a=c=d=1$, $b_{12}=b_{21}=2$ (so $R_{12}=R_{21}=2$ and $R_{11}=R_{22}=0$; $Z_{\{1,2\}}$ is stable), $\kappa_1=\varepsilon_1=5$, $\kappa_2=0.2$, $\varepsilon_2=0.05$. Reset domain 2 to $x_2=0.01$, $r_2=0$ (re-seeded), with domain 1 at $x_1=0.999$, $r_1=2$. Then $s_2(\{1\})=2>1$, yet **both** shares go to 0 (simulated to $t=300$). With the rates swapped the reform is re-absorbed. Thm 1 (branch 2) and Thm 2(b) ("re-absorbed outright") rely on (iii).

**Replacement (iii):**
```latex
(iii) Let a reform reset domain $i$'s share, rule support or own conversion without lowering its inbound conversion $s_i(\cC')$ from a set $\cC'$ of domains that remain captured ($x_j\to1$ on $\cC'$; this holds, for instance, if $s_j(\cC')>1$ for all $j\in\cC'$ and the state is near $Z_{\cC'}$). If $s_i(\cC')>1$, the reform is re-absorbed once $i$ is re-seeded.
```
Proof: `(iii) is (i) with $\cC'$ as seed; that $\cC'$ remains captured follows by comparison with the system in which $x_i\equiv0$, where $Z_{\cC'}$ is stable.`

### 11.3 Prop. 9 (pause): CORRECT
- The equilibria $(0,0)$, $(1,b/d)$ and the saddle $(1/R,c/a)$ are correct.
- $\Phi=axr-cx-\frac{ad}{2b}r^2$ satisfies $\dot\Phi=\kappa x(1-x)(ar-c)^2+\frac{a\varepsilon}{b}(bx-dr)^2\ge0$. Verified; a neat Lyapunov function. Convergence to equilibria follows.
- The nullcline $r=bx/d$ passes through the saddle, so $(x_p,bx_p/d)$ lies strictly NE or SW of it. Correct.
- **$\sigma(0)>1/R$.** The argument "nonincreasing separatrix through $(1/R,c/a)$, $c/a>0$" gives only $\ge$. Strictness: the system is strongly cooperative on $(0,1)\times(0,\infty)$ (irreducible Jacobian), so the point $(1/R,0)$, which lies below the saddle, has a trajectory strictly SW of the saddle for $t>0$, which is inside the open basin of absence; by openness, $(1/R+\delta,0)$ is in that basin too.
- The separatrix does meet $r=0$ at some $x<1$: backward in time, $\dot r<0$ near $x\to1$ while $x$ cannot reach 1 in finite time. Numerically $\sigma(0)\approx0.676$ for $\kappa=\varepsilon=1$ and $R=2$, $0.510$ for $\kappa=0.2,\varepsilon=5$, and $0.9999$ for $\kappa=5,\varepsilon=0.2$; all are $>1/R=0.5$.

**Replacement (last clause of the proof):** `... and $\sigma(0)>1/R$: the system is strongly cooperative in $(0,1)\times(0,\infty)$, so the trajectory from $(1/R,0)$, which lies below the saddle, is strictly south-west of it for $t>0$ and converges to absence; by openness of basins so do $(x,0)$ for $x$ slightly above $1/R$.`

---

## 12. Numerics (Appendix C, Figure 2)

- `python3 figures_v3.py` reproduces `checks.log` and `fig-rate.tex` **byte for byte**.
- **Every number in Appendix C and the Figure 2 caption matches the log**: $d^\ast(0)=0.8$; failure at $6.755$ (bound 9.163) for $\alpha=0.05$ and at $21.531$ (bound 22.907) for $\alpha=0.08$; $A/c_\dE+S=0.9325$; $\mfl=0.4286$; alarms at 37.1, 45.0 and 63.1 against a floor crossing at 53.2; late capture gives alarms at 38.9 and 40.3.
- The text checks out: "sixteen time units before" is 16.1; "halves that window" is 8.2/16.1; "ten time units after" is 9.9.
- **Caption (a), line 213: "overtaken at $t^\ast\approx6.8$".** Prop. 5 defines $t^\ast$ as the bound, which is 9.16 for these parameters; 6.76 is the actual crossing. Replace with: `which is overtaken at $t\approx6.8$, before the bound $t^\ast\approx9.2$ of Proposition~\ref{prop:rate}`. The figure code's "$t^\ast$" label on the vertical line has the same problem.
- **The Prop. 2 brute-force check is vacuous for the threshold.** The script uses $\theta=0.5$, so $w\ge1>\theta/n$ always and only the depletion branch is ever tested. I re-ran it with $\theta\in\{0.25,2,6,20\}$: 1485 cases (1086 depletion, 399 restraint), 0 mismatches. The result is right, but Appendix C's description overstates what the script checks. Change the script to use, for example, `omega in (0.5, 4, 12, 40)` with `theta = omega*K*h/(rho*nu)`. The first Prop. 2 block in the log (`game(...)`) just evaluates the formula; it is not a check.
- **The fragmentation lines are circular** (`k*(s/k)**2` is the claim restated), and the claimed factor is inconsistent (6.7).
- "holds for $\alpha\ge0.1$" is confirmed analytically (6.5) and numerically to $T=1000$.
- In Figure 2b, $E(t)$ and $x_\dE(t)$ are exogenous logistic curves, not outputs of the model's selection dynamics. The caption says "spreading race strategy", which is acceptable, but this is an illustration of Prop. 6 only.

---

## 13. Other small formal points

- **Text after Def. 2 (line 127).** "market-share competition driven by relative profitability" is relative only if profitability enters as **differences**. Ratio-normalized rules, such as $\dot p_k=p_k(\pi_k-\bar\pi)/\bar\pi$, are payoff-monotone but not translation-invariant: $G(V)$ changes their speed. For those rules only the second sentence of Lemma 1 holds.
- **Identification (line 296).** In the regression $\frac{d}{dt}\operatorname{logit}x_i=-\kappa_ic_i+\sum_j\kappa_ic_iR_{ij}(k_i*x_j)$, coefficient divided by intercept is $-R_{ij}$. Write "minus the ratio". The kernel also depends on the unknown $\varepsilon_id_i$, so the regression is nonlinear in that parameter.
- **Prop. 5 setup**: $q^\ast=\chi\hat Y/(\gamma d)$ needs uniform $d$ in **every** row that receives cultivated conversion, not only in the corrector rows (6.1).

---

## 14. Prioritized list

1. **Prop. 5 / Thm 2 (I2) / abstract: the half-rate law needs $f=0$.** The new sentence on line 192 is false for (iii). With a fixed $f>0$ the requirement is a bounded level $\max\{A/c_\dE,\chi\hat Y/f\}$ (constant $d=9$ suffices forever in the Figure 2a setting); with $f$ falling at rate $g_f$ the required rate is $\min\{g_f,g/2\}$. Thm 1's (C2) "above the size threshold" ($f>0$) conflicts with Prop. 5's $f=0$. (6.6)
2. **Thm 2(a) is false as stated.** The host can cross the floor in the selection transient even with (I1)–(I4) in force from $t=0$ and $V(0)=K$ (minimum $V=0.14$ with the paper's parameters). A low-load carrier must be present, and replicator dynamics, a full-row certificate and a uniform margin are needed. Restate as eventual viability plus an explicit transient condition. (9.1)
3. **Thm 1, three fixes:**
   - (a) the payoff clause is false for $h\bar e\ge\rho$, which (C0) allows (counterexample: race 3 against restraint 2), and it needs linear $G$;
   - (b) "captured before" must be the quantitative condition $x_\dE>\bar x$ on the band (counterexample: alarm at 44.9 before the floor at 53.2);
   - (c) state the hidden hypotheses: replicator dynamics, $\cC$ captured, seeding, quasi-static $q$, $f=0$, $\beta\in[0,1)$.
   Also cite Prop. 6(i), not (v). (8)
4. **Cor. 1 overclaims:** "raises every carrier's absolute payoff" contradicts Prop. 4(ii) and leaves out the cost of correction; "self-enforcing" contradicts Prop. 4 for (I2); "cannot establish" is only argued. The same applies to the "Rivals cannot cooperate" paragraph. (10)
5. **Prop. 8(iii) is false as stated** (two-domain counterexample). Require the remaining set to stay captured. Thm 1 branch 2 and Thm 2(b) rely on it. (11.2)
6. **Prop. 5(i), "certified uncaptured":** $s_\dE(\cC)<1$ is not the row sum (counterexample with $R_{\dE\dE}=0.8$). Assume all conversion into $\dE$ comes from $\cC$, or use the full row. This is the same gap as in Thm 2(a)'s step to $x_\dS\to0$. (6.1)
7. **Prop. 3: "$L_i$ decreasing in $d_i$" is false**; it is increasing, and $L_i/d_i$ decreases. (4.2)
8. **Fragmentation factor: $k$ should be $k^2$** under the paper's own Prop. 3 model; the script check is circular. (6.7)
9. **Prop. 4:**
   - (ii) is overclaimed (host channel left out);
   - (i) needs "otherwise identical";
   - (iii) needs $C_u'(0)>0$;
   - (iv) "replaces one captured configuration" is unproved;
   - the Price caveat should cite (i), not (ii). (5)
10. **Prop. 5 smaller items:**
    - (iii) the capture step needs a time-varying argument (one-line fix given);
    - (iv) needs $d(t)\ge d_0e^{\alpha t}$, and the sharp form is $d_0>d^\ast(0)$;
    - (ii) "equality only if $\chi\hat Y=0$" should be "iff $Z=0$". (6.2–6.5)
11. **Thm 2(b)(I4) witness:** take $\dE$ uncaptured or $\beta_{\rm in}<\mfl$, and drop the "$V(t_1)$ close to $\Vmin$" disjunct. (9.2)
12. **Prop. 2:** state $\tau=0$, $\phi$ equal, equal shares, steady-state $V$ and $n\ge2$; "$n\ge\theta$" should be "$n>\theta$". (3)
13. **Prop. 6:** state $0\le\beta_{\rm out}\le\beta_{\rm in}<1$. (7)
14. **Numerics and text:**
    - the caption's $t^\ast\approx6.8$ conflicts with the definition (6.76 is the crossing; $t^\ast=9.16$);
    - the Prop. 2 brute force never tests restraint;
    - Prop. 7(d) wording;
    - the strictness argument in Prop. 9;
    - the upper end in Remark 1;
    - the identification sign;
    - ratio-based market-share rules are not "relative". (11–13)
