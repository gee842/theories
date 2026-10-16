# Paid verification and the survival of its maintenance practice

This extension puts two previously fixed conditions inside the dynamics: resistance to unpaid service access through false credentials, and actual delivery of the maintenance purchased with verification fees. The verifiers must be paid from the same output as the useful service. Their maintenance practice is itself subject to replacement by a practice that claims payment without doing the work. Honest peers and functioning verification capacity must jointly make that fraud detectable.

The construction proves a conditional positive result and two failure results. A funded regime can be locally stable and can recover throughout an explicit invariant region while both user participation and honest maintenance are selected on their actual returns. Conversely, removing executable withholding causes institutional loss when both bypass and fraudulent maintenance practices are present. Even with withholding, sufficiently little inherited honest maintenance produces loss that capacity injection alone cannot repair under the stated rules.

This is a bounded extension of the [existing paid correction model](../../model/CONSTRUCTION.md), not a complete account of constitutional survival or a claim of mathematical novelty. Deferred settlement, authentic evidence from successful checks, and peer assignment that cannot be chosen by the audited contractor remain implementation primitives. The modeled threat class is explicit below.

## Task technology and two separate carrier populations

Retain the baseline model's noisy contextual task. A unit mass of service users faces independent equally likely L and R contexts. Without informative evidence it obtains expected output \(y_0=b+\Delta/2\), where \(b\ge0\). A noisy test has accuracy \(\alpha\in(1/2,1]\). Useful paired test-and-action capacity \(C\) produces an expected extra output

\[
Bq(C),\qquad B=\Delta(\alpha-1/2),
\qquad q(C)=\left(\frac C{K+C}\right)^2,
\quad 0<B\le y_0,
\]

with \(K>0\). A fraction \(\chi\in(0,1]\) of the incremental output is privately recoverable. Write

\[
A=\chi B,\qquad 0<A\le B\le y_0,
\qquad r(C)=y_0+Aq(C).
\tag{1}
\]

A separate unit mass of verification contractors supplies maintenance of receipt and access verification. Its private returns govern its own copying process; contractor wages are not silently added to service-user returns. This separation avoids assuming the same actors ignore one of their income streams.

The state variables are

\[
x\in[0,1],\quad C\ge0,\quad G\ge0,\quad h\in[0,1].
\]

Here \(x\) is the share of users adopting the paying access arrangement; \(G\) is paid verification capacity; and \(h\) is the share of contractors that genuinely deliver contracted maintenance. Its complement files false completion claims and delivers no maintenance. These are operating practices, not moral classes of people.

Within this two-practice contractor repertoire, genuine delivery is bundled with truthful peer reporting, and false completion is bundled with nonreporting or collusion. A contractor that delivers maintenance but corrupts its peer reports is a different hybrid practice, not covered by the invasion theorem. The result does not infer an intrinsic honest character from good production.

## Outsider bypass and effective verification

The mechanical success probability of a supported verification check is

\[
p(G)=\frac G{L+G},\qquad L>0.
\]

A randomly assigned peer must also perform the check honestly. The combined effective check probability is

\[
D=h\,p(G).
\tag{2}
\]

The same paid package supports user access checks and contractor completion checks. The conversion cost specified below covers both workloads. Peer assignment is independent of the audited party's choice. Dishonest peers collude or fail to report; they do not provide a free honest monitoring channel. Conditional on an honest effective check, the relevant false claim is correctly rejected. Undetectable attack classes and false accusations are outside this model.

A paying user receives the useful service and pays fraction \(\tau\in(0,1)\) of its direct receipts. A bypass user files a false access claim, pays no fee, and gets the useful service with probability \(1-D\). If blocked, it retains the baseline action. The bypass attempt has zero incremental cost in this deliberately demanding case. It therefore weakly dominates baseline abstention; the model has not created an artificial paying advantage by excluding a costless outside option.

Let

\[
Z=x+(1-x)(1-D),\qquad S=(1-\chi)Bq(C)Z.
\]

The public spillover \(S\) is common to all users. Expected private returns and their difference are

\[
U_P=(1-\tau)r(C)+S,
\qquad U_B=y_0+(1-D)Aq(C)+S,
\]

\[
\boxed{s_x:=U_P-U_B=Aq(C)D-\tau r(C)
=(D-\tau)Aq(C)-\tau y_0.}
\tag{3}
\]

Verification is valuable for the paying practice because it limits an alternative's unpaid access. This is a specified participation and financing mechanism, not an assertion that exclusion is always legitimate or that public services must use this arrangement.

## The verification contract and an insider alternative

Collected fee revenue is

\[
F=\tau x r(C).
\tag{4}
\]

A fixed split \(\lambda\in(0,1)\) pays \(\lambda F\) toward useful capacity \(C\). The remainder

\[
V=(1-\lambda)F
\tag{5}
\]

is the verification-contract budget. Each genuine contractor uses a fraction \(m\in(0,1)\) of its assigned budget to produce and maintain \(G\), retaining fraction \(1-m\) as its payment. A fraudulent contractor supplies no maintenance and claims the whole budget. If its false completion claim is detected before final settlement, the assigned tranche is withheld into an inert reserve. Otherwise it retains the whole tranche.

Expected contractor returns are therefore

\[
W_H=(1-m)V,
\qquad W_F=(1-D)V,
\qquad
\boxed{s_h:=W_H-W_F=V(D-m).}
\tag{6}
\]

No fine larger than available receipts is imposed. No already consumed diversion is recovered. The withheld amount is not simultaneously credited as new institutional production. It is recorded by

\[
\dot Q=(1-h)DV,
\tag{7}
\]

where \(Q\) has no feedback into the operating equations. It is a ledger reserve, not a free replenishment mechanism.

The contract relies on conditional release that an effective authentic check can enforce. A claimed detection without the ability to withhold payment does not have the payoff consequences in (6). The negative control below removes that ability rather than assuming it survives by definition.

The flow model assumes coordinated delivery and payment or fully funded procurement: assigned maintenance funds can pay for real delivered work, while final private compensation remains conditional. Ordinary escrow alone does not provide working capital, and checking a promise is not verification of delivery. An installation or procurement system that cannot meet this assumption needs an additional financing state.

## Resource accounting

Aggregate gross output of users is

\[
Y=y_0+Bq(C)Z.
\]

User retention is \(Y-F\). The entire collected flow is allocated exactly once:

\[
\boxed{
\lambda F
+mhV
+(1-m)hV
+(1-h)(1-D)V
+(1-h)DV
=F.
}
\tag{8}
\]

The five terms are useful-capacity spending, delivered verification maintenance, genuine contractor pay, undetected fraudulent pay, and withheld reserve. The first two produce the two capacities, at conversion rates \(\eta_C,\eta_G>0\). The last term has no productive credit. There is no externally financed monitoring stock or sanction reward.

These are spendable-output accounts. They are not a claim of universal material conservation. Repeated task opportunities, conversion technology, and the nondepleting background supply over the modeled horizon remain environmental assumptions. A separate host or natural-resource stock is not included.

## Endogenous replacement and the closed operating system

Both populations use proportional imitation. A carrier samples another carrier and changes practice at a rate proportional to the positive current private-return advantage. With copying speeds \(\kappa,\nu>0\), the deterministic population approximation is

\[
\boxed{
\begin{aligned}
\dot x&=\kappa x(1-x)\,[Aq(C)D-\tau r(C)],\\
\dot C&=\eta_C\lambda\tau x r(C)-\mu_C C,\\
\dot G&=\eta_G m h(1-\lambda)\tau x r(C)-\mu_G G,\\
\dot h&=\nu h(1-h)(1-\lambda)\tau x r(C)\,[D-m],\\
D&=hG/(L+G).
\end{aligned}}
\tag{9}
\]

All depreciation rates are positive. The equations average repeated tasks and assignment events; they are not exact finite-population expectation equations. There is no copying-generated reentry of an extinct practice.

The domain \([0,1]\times[0,\infty)^2\times[0,1]\) is invariant. Capacity inputs are bounded by constants, so every operating trajectory is bounded and exists globally. The reserve \(Q\) can accumulate without bound but has no effect on bounded operating states. Positive interior practice shares remain positive for every finite time.

The four variables close a concrete loop: fraud reduces effective checks and delivered maintenance; weaker checks increase both bypass and false-completion returns; bypass reduces fee revenue; and declining revenue reduces the capacities that make valid checking possible. The reverse loop is feasible only under the conditions derived next.

## Local selection stability of the funded regime

At \(x=h=1\), useful capacity has the scalar equation

\[
\dot C=\eta_C\lambda\tau r(C)-\mu_C C.
\]

Under \(A\le y_0\), it has one positive equilibrium \(C_*\) and a negative derivative there. The proof is the same quotient argument as the baseline model:

\[
\frac{d}{dC}\left[\frac{y_0}C+\frac{AC}{(K+C)^2}\right]
=-\frac{y_0}{C^2}+\frac{A(K-C)}{(K+C)^3}<0.
\tag{10}
\]

The equilibrium verification capacity is

\[
G_*=
\frac{\eta_Gm(1-\lambda)\tau r(C_*)}{\mu_G}.
\tag{11}
\]

Define \(p_*=p(G_*)\), \(q_*=q(C_*)\), \(F_*=\tau r(C_*)\), and \(V_*=(1-\lambda)F_*\). The full-R and genuinely maintained equilibrium is strictly resistant to the two specified replacement alternatives precisely when

\[
\boxed{Aq_*p_*>F_*,\qquad p_*>m.}
\tag{12}
\]

The first condition makes payment preferable to bypass. The second makes delivered maintenance preferable to a false completion claim. Neither condition follows from the other.

The Jacobian at this equilibrium is triangular by blocks when states are ordered \((x,h,C,G)\). Its eigenvalues are

\[
-\kappa[Aq_*p_*-F_*],\qquad
-\nu V_*(p_*-m),\qquad
\eta_C\lambda\tau r'(C_*)-\mu_C,\qquad
-\mu_G.
\tag{13}
\]

The last two are negative by (10) and depreciation. Thus (12) is both sufficient for local asymptotic stability and necessary for strictly negative invasion exponents against these two alternatives. Equality cases are nonhyperbolic and are not included. This is deterministic local resistance to unilateral practices, not resistance to every coordinated deviation or mutation process.

## An exact design threshold with paid insider verification

Fix the task and conversion parameters, including \(m\), but allow the financing fraction \(\tau\) and split \(\lambda\) to be chosen within \((0,1)\). Use dimensionless capacities

\[
c=C/K,\quad g=G/L,
\quad a=\frac{\mu_CK}{\eta_C},
\quad b=\frac{\mu_GL}{\eta_Gm}.
\tag{14}
\]

At a full paying and genuinely maintained equilibrium, actual replacement spending implies

\[
\lambda F=ac,\qquad (1-\lambda)F=bg,
\qquad F=ac+bg.
\tag{15}
\]

The factor \(1/m\) in \(b\) charges genuine contractor pay as well as delivered maintenance. Omitting it would incorrectly treat their compensation as free.

Put

\[
q(c)=\left(\frac c{1+c}\right)^2,
\quad p(g)=\frac g{1+g},
\quad g_{\min}=\frac m{1-m}.
\]

Then a strictly stable selected equilibrium exists for some \(\tau,\lambda\) if and only if

\[
\boxed{
A>A_{\rm crit}:=
\inf_{c>0,\ g>g_{\min}}
\frac{ac+bg}{q(c)p(g)}.
}
\tag{16}
\]

Necessity follows from (12) and (15). For sufficiency, choose \(c,g\) with the ratio strictly below \(A\) and \(g>g_{\min}\), and set

\[
F=ac+bg,\qquad
\lambda=\frac{ac}{F},\qquad
\tau=\frac{F}{y_0+Aq(c)}.
\tag{17}
\]

Both fractions are in \((0,1)\), because \(F<Aq(c)p(g)<y_0+Aq(c)\). These values realize the chosen capacities and both strict selection margins. Equations (10) and (13) then prove stability. No free maximization of \(G\) is being performed; its cost is in the same fee pool as useful capacity.

The threshold has an explicit one-dimensional construction. At fixed \(g\), the unique minimizing \(c\) is

\[
c_{\rm opt}(g)=\frac{1+\sqrt{1+8bg/a}}2.
\tag{18}
\]

Without the lower bound on \(g\), the unique joint minimizer satisfies

\[
ac=bg^2,\qquad c=1+2/g.
\]

Equivalently, \(g_*>0\) is the unique positive root of

\[
bg_*^3-ag_*-2a=0.
\tag{19}
\]

These first-order conditions follow by differentiating the positive ratio in (16). Its value diverges at the positive-domain boundaries. The minimized envelope has derivative with the sign of \(bg^2-ac_{\rm opt}(g)\). This has just one positive zero, since (19) has one positive root. Hence it decreases and then increases. Therefore evaluate (16) by setting

\[
g_{\rm opt}=\max(g_*,g_{\min}),\qquad
c_{\rm opt}=c_{\rm opt}(g_{\rm opt}),
\qquad
A_{\rm crit}=
\frac{a c_{\rm opt}+b g_{\rm opt}}
{q(c_{\rm opt})p(g_{\rm opt})}.
\tag{20}
\]

When \(g_{\rm opt}=g_{\min}\), this evaluates the infimum on the closure of the feasible set. The boundary itself has no strict honesty margin. Strict \(A>A_{\rm crit}\) permits nearby \(g>g_{\min}\) with both margins positive; equality does not.

The threshold is a conditional design feasibility result within this task and attack class, not a welfare optimum. The fee and split in (17) are implemented rules; the model does not explain adoption of every possible competing \(\tau\) and \(\lambda\).

## A region that restores participation and delivered maintenance

Choose positive lower bounds \(0<\underline x,\underline h<1\), \(\underline C,\underline G>0\). Let

\[
\underline D=\underline h\,p(\underline G),\quad
\underline r=r(\underline C),\quad
\underline q=q(\underline C).
\]

Suppose

\[
\delta_x:=(\underline D-\tau)A\underline q-\tau y_0>0,
\qquad
\delta_h:=\underline D-m>0,
\tag{21}
\]

and

\[
\eta_C\lambda\tau\underline x\,\underline r
\ge\mu_C\underline C,
\qquad
\eta_G m\underline h(1-\lambda)\tau\underline x\,\underline r
\ge\mu_G\underline G.
\tag{22}
\]

Then

\[
\mathcal R=
\{x\ge\underline x,\ h\ge\underline h,
\ C\ge\underline C,\ G\ge\underline G\}
\tag{23}
\]

within the physical domain is forward invariant. Both capacity lower faces point inward by (22). The first inequality in (21) implies \(\underline D>\tau\); therefore \(s_x\) is bounded below by \(\delta_x\) throughout the set. The honesty gap \(D-m\) is bounded below by \(\delta_h\). Thus both practice shares are nondecreasing and remain selected at the lower faces.

More strongly,

\[
\dot x\ge\kappa\delta_x x(1-x),
\qquad
\dot h\ge\nu\underline V\delta_h h(1-h),
\quad
\underline V=(1-\lambda)\tau\underline x\,\underline r>0.
\tag{24}
\]

Consequently \(x,h\to1\). Scalar comparison with the unique useful-capacity roots as \(x\to1\) gives \(C\to C_*\). The forcing in the linear verification equation then converges to its genuine-maintenance equilibrium value, giving \(G\to G_*\). This is an explicit recovery region, not only a favorable equilibrium calculation. It does not claim that every initially feasible state enters that region.

## A separate loss basin from insufficient useful service

Institutional loss need not begin with corruption. Choose \(C_\ell>0\) such that

\[
s_\ell:=(1-\tau)Aq(C_\ell)-\tau y_0<0,
\qquad
0<x_\ell<\min\left(1,
\frac{\mu_C C_\ell}{\eta_C\lambda\tau r(C_\ell)}\right).
\tag{25}
\]

The region \(x\le x_\ell, C\le C_\ell\), with arbitrary \(h\in[0,1]\) and \(G\ge0\), is forward invariant. The upper useful-capacity face points inward by the second inequality. Since \(D\le1\), the user advantage throughout the region satisfies \(s_x\le s_\ell<0\), so the upper prevalence face also points inward. In fact,

\[
\dot x\le-\kappa(-s_\ell)(1-x_\ell)x,
\]

which proves exponential decay. Fees are consequently integrable and vanish, giving \(C,G\to0\) by their linear depreciation equations. Genuine maintenance can remain common while its useful-service financing disappears. This basin is distinct from the low-honesty failure below.

## Too little inherited genuine maintenance defeats capacity alone

Suppose \(0\le h_0<m\). Since \(D\le h\), the honesty share is nonincreasing while it is below \(m\), and stays at most \(h_0\). For \(0<h_0<m\),

\[
-\dot h
=\nu h(1-h)V(m-D)
\ge\nu(1-h_0)(m-h_0)hV.
\]

Hence

\[
\boxed{
\int_0^\infty h(t)V(t)\,dt
\le\frac{h_0}{\nu(1-h_0)(m-h_0)}<\infty.
}
\tag{26}
\]

For \(h_0=0\), the same integrability is immediate. Genuine verification maintenance is therefore integrable over time. The stable linear equation for \(G\) implies \(G\to0\), and thus \(D\to0\). Eventually

\[
s_x\le A D-\tau y_0\le-\tau y_0/2<0.
\]

For every initial \(x_0<1\), proportional copying then gives \(x\to0\) exponentially after a finite date. Fees vanish and the useful-capacity equation gives \(C\to0\).

This is a global loss result for all finite initial capacities under the stated low-honesty condition. Raising \(C\) or \(G\) alone cannot restore the operating regime at fixed contracts and copying rules. A change in the inherited contractor mixture, entry of a new practice, or altered compensation would be a different intervention. An arbitrarily large finite initial injection, a finite number of finite injections, or an external stock input with finite total mass can delay failure but does not invalidate (26) or the eventual capacity-loss conclusion. Indefinite outside replenishment is a different system and is not covered by this claim.

The share \(h\) need not tend to zero. Once work and fees disappear, its copying process slows; indeed, when \(0<h_0<m\) and \(x_0<1\), the eventual fee integral is finite and the logit of \(h\) has finite total drift, leaving a positive limiting share. The failure is loss of functioning capacity and its financing, not a claim that every honest contractor is eliminated. At \(x_0=1\), bypass is absent and copying cannot introduce it; the proof still gives \(G\to0\), but does not assert user exit or \(C\to0\). These boundary exceptions are features of the specified transmission rule.

## Why paying verifiers without executable recourse is insufficient

Consider an intervention that removes completion auditing or makes its result unable to withhold the fraudulent tranche. The outsider access technology may initially continue. A false completion claim now receives \(V\), while genuine delivery retains \((1-m)V\). Thus

\[
\dot h=-\nu m Vh(1-h),\qquad
\dot G=\eta_GmhV-\mu_GG.
\tag{27}
\]

For \(h_0<1\),

\[
\frac{d}{dt}\log(1-h)=\nu m hV,
\]

so

\[
\int_0^\infty hV\,dt
\le\frac{-\log(1-h_0)}{\nu m}<\infty.
\tag{28}
\]

Consequently \(G\to0\), then \(D\to0\). With \(x_0<1\), the previous argument gives \(x,C\to0\). This holds regardless of the initial finite capacities and their initially favorable selection margins. Genuine maintenance is invasible without recourse; an initially pure honest population \(h_0=1\) is an invariant but invasion-unstable boundary and is explicitly excluded from the global conclusion.

This counterexample distinguishes generating evidence from having effective authority over payment. It also shows why introducing an internally financed verification stock alone would not close the problem: its delivered maintenance can itself be selected away.

## A witness with both forms of opposition admitted

Use the noisy task \(y_0=1\), \(B=A=.8\), and take

\[
K=L=\mu_C=\mu_G=\kappa=1,\quad
\tau=3/20,\quad \lambda=m=1/2,
\quad\eta_C=800/29,\quad\eta_G=1600/29,
\quad\nu=10.
\]

The full paying and genuinely maintained equilibrium is exactly

\[
x=h=1,\qquad C_*=G_*=3.
\]

At this point \(q_*=9/16\), \(p_*=3/4\), \(r_*=1.45\), \(F_*=.2175\), and \(V_*=.10875\). The user advantage is \(.12\); the contractor advantage is \(V_*(p_*-m)=.0271875\). Neither practice is sustained by a welfare bonus.

An explicit recovery region uses

\[
\underline x=\underline h=.9,
\qquad\underline C=2.5,
\qquad\underline G=2.1.
\]

Its effective check lower bound is approximately \(.6096774193548388\). The user and honesty margins in (21) are approximately \(.037623436471362764\) and \(.10967741935483877\). The two inward capacity margins in (22) are approximately \(.1220971147079517\) and \(.25988740323715653\). All are strict. Initial \((x,h,C,G)=(.92,.92,2.6,2.2)\) therefore recovers through endogenous copying and paid replacement, despite both bypass users and fraudulent contractors being present.

Under the same parameters, any \(h_0<.5\) and \(x_0<1\) loses operating capacity for all finite \(C_0,G_0\). Disabling executable withholding also causes loss whenever both fraudulent maintenance and bypass are present.

The separate useful-service loss basin can use \(x_\ell=.15\) and \(C_\ell=.4\), for which \(s_\ell=-463/4900<0\) and the funding bound in (25) is strict. Initial \((x,h,C,G)=(.1,.93,.2,2.4)\) lies in that basin despite a high inherited share of genuinely delivered maintenance.

For the exact design threshold, \(a=b=29/800\) and \(g_{\min}=1\). The unconstrained root and capacity are

\[
g_*=1.5213797068045676,\qquad
c_{\rm opt}=2.314596212276752,
\]

and \(A_{\rm crit}\simeq.4726017227793541<.8\). The witness is a feasible design, not the unique or socially optimal design. All numbers are mathematical examples, not estimates of real institutional capacity.

## What is endogenous and what remains assumed

Collected revenue, both operational capacities, delivered maintenance, the prevalence of bypass, and the prevalence of false completion are endogenous. A successful regime has no permanently honest guardian population or externally replenished monitoring stock. An inherited minority of both attack practices can be selected downward in the certified region; outside it, their growth can undermine the institution.

The result nevertheless depends on a finite task and attack repertoire. It assumes a physical or technical means of delaying assigned payment, authentic observable completion evidence when a supported honest check succeeds, peer assignment the audited party cannot direct, and a fixed allocation split. It does not model coordinated capture of that settlement primitive, arbitrary rewriting of the contract, attacks on the evidence technology itself, coercive removal of peers, or control of the random assignment process. It also leaves rights, legitimate participation and false-positive harms outside the scalar resource account.

These are explicit residual conditions to test, not an assertion that the regress of institutional accountability has been eliminated. The narrower advance is an internally financed maintenance and verification system whose own delivery practice faces a profitable false-claim alternative, with proved conditions for survival, recovery, and failure under that threat.
