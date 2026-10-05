# Sustaining plural capacities without a common objective

Theoretical extension, 5 October 2026. This note follows [the root foundation](ROOT-FOUNDATION.md) and its [scope and originality assessment](../foundation-assessment/ASSESSMENT.md). It addresses one question: can the exact maintenance result accommodate several distinct capacities, separate resources and competing requirements without replacing them with a common utility? The answer is yes for the explicit class below. No experiment or study implementation is part of this extension.

The result has three parts: an exact condition for indefinite preservation, a certificate of unavoidable finite failure when that condition fails, and an exact maximum duration for constant losses. The proof uses established controlled invariance, time averaging and convex separation. This is an extension of the project's mathematics; scientific priority is not certified.

## Separate requirements and shared activities

Let \(v\in\mathbb R_+^n\) denote nonnegative margins above independently specified capacity floors. Let \(b\in\mathbb R_+^m\) denote distinct protected resource reserves. Capacities and resources need not be interchangeable. One component can concern information discrimination, another executable response, another the availability of a corrective procedure. Each interpretation requires an independently justified measurement law.

Activities \(u\in U\subset\mathbb R^k\) restore capacities through a fixed matrix \(M\) and affect resources through a fixed matrix \(Q\):

\[
\dot v=Mu-\rho(v),\qquad
\dot b=p-Qu.
\tag{PC1}
\]

The vector \(p\) records net outside provision after fixed demands. Entries retain their own physical units; coefficients convert the corresponding activity into each row's units. Nothing requires \(b_1\) to compensate for a violation of \(b_2\), or one person's protected outcome to compensate for another's. The requirement is the conjunction \(v\ge0,b\ge0\), component by component.

Assume:

1. \(U\) is nonempty, compact, convex, fixed during the modeled interval, and physically implementable. Constant activities in \(U\) are available. A formal fractional allocation is not allowed unless the implementation can actually supply it.
2. \(M,Q,p\) are fixed. The locally Lipschitz loss function \(\rho\) satisfies, for a fixed vector \(r\),

\[
\rho_i(v)\ge r_i\quad\text{for every }v\ge0,
\qquad
\rho_i(v)=r_i\quad\text{whenever }v_i=0.
\tag{PC2}
\]

3. Initial margins and reserves are finite and nonnegative. Controls are measurable and use actual available information. Requirements must hold continuously, not just at selected evaluation times.

Condition (PC2) is substantive: the loss at a required floor is globally minimal, and the loss on that boundary face does not rise with the other margins. Separable nondecreasing losses satisfy it; some coupled excess losses do too. It is not a theorem about all physical or institutional processes. Local well-posedness is understood on a neighborhood of the orthant. Bounded activities and the lower loss bound prevent upward finite-time escape along a safe trajectory.

## Exact indefinite feasibility

Define the sustainable activity set

\[
F=\{u\in U:Mu\ge r,\ Qu\le p\}.
\tag{PC3}
\]

**Theorem 1.** From any finite safe initial state, all required capacities and resource reserves can be preserved indefinitely if and only if \(F\ne\varnothing\). If it is nonempty, a constant activity in \(F\) suffices. If it is empty, no adaptive activity schedule succeeds indefinitely from any finite safe initial state.

**Sufficiency.** Choose \(\bar u\in F\). At a face \(v_i=0\), (PC2) gives \(\dot v_i=(M\bar u)_i-r_i\ge0\). Every resource derivative is nonnegative because \(Q\bar u\le p\). Thus the orthant is invariant. The bounded upper growth of every coordinate ensures global continuation of the safe solution. No observation of hidden state is required to execute this constant activity. ∎

**Necessity.** For a safe trajectory through time \(T>0\), define \(\bar u_T=T^{-1}\int_0^T u(t)\,dt\). Integrating (PC1) and using (PC2) yields

\[
M\bar u_T\ge r-v_0/T,
\qquad
Q\bar u_T\le p+b_0/T.
\tag{PC4}
\]

Convexity and closedness place \(\bar u_T\) in \(U\). If the trajectory stays safe forever, compactness supplies a convergent subsequence as \(T\to\infty\). Its limit belongs to \(F\). Terminal margins need not be bounded, and the activity need not become stationary. ∎

This identifies a limit on what adaptation can accomplish in this class. Adaptation can change transient performance and remaining duration. It cannot make indefinite joint preservation possible when the sustainable activity set is empty. Learning unknown laws, opening new activities, changing technology or revising requirements changes the premises rather than evading the theorem.

## A certificate of unavoidable failure

If \(F\) is empty, consider the compact convex set

\[
K=\{(Mu-r,\ p-Qu):u\in U\}.
\tag{PC5}
\]

It is disjoint from the nonnegative orthant. Strong separation supplies nonnegative weights \(\lambda\in\mathbb R_+^n\), \(\mu\in\mathbb R_+^m\), not both zero, with

\[
\beta:=\min_{u\in U}
\{\lambda^{\mathsf T}(r-Mu)+\mu^{\mathsf T}(Qu-p)\}>0.
\tag{PC6}
\]

The nonnegative signs follow because the orthant is unbounded in every positive coordinate. Conversely, such weights immediately exclude a feasible activity in \(F\). Thus this is an exact infeasibility certificate, not just a sufficient diagnostic that may fail to detect a deficit.

**Theorem 2.** Every safe interval under any admissible adaptive policy satisfies

\[
T\le
\frac{\lambda^{\mathsf T}v_0+\mu^{\mathsf T}b_0}{\beta}.
\tag{PC7}
\]

**Proof.** While every requirement holds, \(W=\lambda^{\mathsf T}v+\mu^{\mathsf T}b\ge0\). Equations (PC1), (PC2) and (PC6) give \(\dot W\le-\beta\). Integration proves the bound. The boundary at the displayed deadline may itself be safe; acceptable service cannot extend beyond it. ∎

The weights are a proof device, not welfare weights. They identify a combination of shortages that every allowed activity fails to cover. No controller is instructed to maximize \(W\), and no protected violation is permitted in exchange for a gain elsewhere. Changing measurement units changes the corresponding weights. There is no newly identified universal scalar alignment gradient here.

## Exact maximum duration for constant losses

When \(\rho(v)\equiv r\), the infimum of the certificate bounds is sharp. A horizon \(T>0\) is feasible exactly when some \(\bar u\in U\) satisfies

\[
v_0+T(M\bar u-r)\ge0,
\qquad
b_0+T(p-Q\bar u)\ge0.
\tag{PC8}
\]

Necessity follows by taking the time average of any successful activity schedule. Sufficiency follows by using that average constantly: the state moves along a straight line between safe endpoints, so every intermediate state is safe.

Applying separation to the compact set of endpoints yields the exact optimum

\[
T^*=\inf_{\lambda,\mu\ge0:\,\beta(\lambda,\mu)>0}
\frac{\lambda^{\mathsf T}v_0+\mu^{\mathsf T}b_0}
{\beta(\lambda,\mu)},
\qquad \inf\varnothing=\infty.
\tag{PC9}
\]

To see exactness, an infeasible horizon has a nonnegative separating weight for which its initial weighted margin is less than \(T\beta\); every feasible horizon satisfies the opposite inequality for every such weight. Compactness also gives an attainable finite maximal endpoint. Infinite duration is covered by Theorem 1.

If \(U\) is a polytope, this is a linear optimization problem after setting \(z=T\bar u\). For example, \(U=\{u\ge0:Gu\le g\}\) gives linear constraints \(z\ge0\), \(T\ge0\), \(Gz\le Tg\), \(v_0+Mz-Tr\ge0\), and \(b_0+Tp-Qz\ge0\), while maximizing \(T\). The objective is a declared service duration with every protected condition retained. It is not an aggregation of those conditions into a common moral value.

For nonlinear losses satisfying (PC2), the constant-loss optimum remains an upper bound. It need not be attained. It is sharp across the whole stated class when only the lower loss vector and the other supplied data are known, because the constant-loss member realizes it.

### A small exact example

There are two distinct capacities. Each loses \(2/5\) per time unit. Activities satisfy \(u_1,u_2\ge0\) and \(u_1+u_2\le1\). A resource replenishes at \(3/5\) and is consumed at \(u_1+u_2\). Each capacity alone could be sustained, but sustaining both requires \(u_1+u_2\ge4/5\), exceeding the renewable resource supply.

Take \(v_0=(1/10,1/10)\) and \(b_0=1/5\). With \(\lambda=(1,1)\), \(\mu=1\), the certificate has \(\beta=1/5\) and initial value \(W_0=2/5\), so no policy can preserve all requirements beyond time two. Constant \(u_1=u_2=7/20\) reaches both capacity floors and zero resource reserve exactly at time two. The bound is attained. These rational calculations were checked directly; they are a constructed example, not observations.

## Relation to the earlier information theorem

For a channel with required reliability \(c_i^*\), the earlier repair law maps to this form through

\[
v_i=\frac1{\alpha_i}\log\frac{1-c_i^*}{1-c_i},
\qquad
\rho_i(v_i)=\frac{\delta_i}{\alpha_i}
\left(\frac{e^{\alpha_i v_i}}{1-c_i^*}-1\right).
\tag{PC10}
\]

Then \(\dot v_i=u_i-\rho_i(v_i)\), and the minimum maintenance demand is \(r_i=\delta_i c_i^*/[\alpha_i(1-c_i^*)]\). This recovers the single-channel result and extends its indefinite-feasibility logic to several channels and separate resources. The finite-initial-margin version takes \(c_i(0)<1\); the earlier perfect-channel argument handles the singular endpoint separately. The sum of such coordinates is not a claim that facts, skills, permissions or resources have identical physical laws.

## Where the extension stops

Convexity must describe actual simultaneous or fractional activity. For losses \((1/2,1/2)\), zero initial margins, and only the two activities \((1,0)\) and \((0,1)\), the unavailable average activity would preserve both floors. No ordinary switching schedule can do so from zero: the sum of the margins remains zero, so safety forces both to remain zero and requires the missing midpoint activity almost everywhere. With positive buffers, alternating the two activities can instead be sustainable. The implementation and initial reserve matter.

State-dependent activity availability also needs a different analysis. For \(\dot v=u-1\), \(0\le u\le\min\{v,1\}\), and \(v(0)=1/2\), replacing actual availability with the fixed envelope \([0,1]\) falsely permits \(u=1\). Every actual safe trajectory satisfies \(v(t)\le1-e^t/2\) and cannot continue beyond \(\log2\).

The minimum-loss premise cannot be removed. With \(\dot v=-(1-v)^2\), no activity, and \(v(0)=1\), the state persists forever although the loss at the floor is one. Protection at an interior state defeats a criterion based only on floor losses.

Finally, a changing requirement changes the feasible set being asked about. The theorem applies to a declared set of requirements and dynamics over its stated interval. It does not derive legitimate goals, settle disagreement, or ensure an uninformed controller can identify the true model. These limitations preserve the situated character of the theory rather than hiding it in a universal objective.

The substantive result is that plural requirements are compatible with an exact feasibility theory. A system can face an unavoidable joint deficit even when each local requirement appears manageable. The mathematical alternative is between a sustainable operating set and a certificate of unavoidable failure, with every protected condition kept explicit.

Two internal agents independently derived and challenged the extension, including the convexity, loss and activity-availability qualifications. The lead integration checked the matrix formulation, finite-horizon separation argument and exact example. This is internal theoretical review, not an external priority assessment or empirical validation.
