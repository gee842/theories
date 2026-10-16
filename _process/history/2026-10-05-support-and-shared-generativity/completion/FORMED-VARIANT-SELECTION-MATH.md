# Formation and differential reconstruction under one law

6 October 2026. AI-authored analytical development for the [accepted dependency-to-regulation connection](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#accepted-work-sequence). It joins the roles of [paid response formation](ENDOGENOUS-REGULATION-MATH.md) and [localized consequence-dependent retention](CONSEQUENCE-RETENTION-SELECTION.md) within one newly declared law. It does not concatenate their differently prepared witnesses or claim the earlier models already supplied this joint preparation.

**Result.** From zero response molecules and zero associations, equally available useful and inactive response types can form, associate, and experience different reconstruction because one restores access to real support. A positive-rate finite-horizon theorem gives an unconditional excess of useful over inactive molecules relative to repair-disabled and equally priced ineffective-repair controls. It also bounds useful copying while the competing type is present. No favorable-founder conditioning or externally supplied reward enters the process. The local-access chemistry, response repertoire, copying specificity and site scaffold remain supplied; their origin and revision are still open.

**Verification scope:** the analytical proofs and exact arithmetic below passed separate collaborating-AI review. The [executable process](../../../../experiments/shared-renewal-capability/regulation/retention/formation/README.md), [independent review](FORMED-VARIANT-SELECTION-REVIEW.md) and [Lean scope note](FORMED-VARIANT-SELECTION-LEAN.md) preserve their distinct evidence. The 53 new Lean declarations certify discrete event structure and ancestry, not these stochastic expectations. None establishes empirical chemical calibration.

## 1. One law, with neither variant initially installed

There is one capture site, intact indicator c∈{0,1}, damage indicator d=1−c, local fuel f∈{0,1}, and resident r∈{∅,A,H}. Useful and inactive response counts a,h include free and resident molecules. Their free counts are \(a^u=a-\mathbf1_{r=A}\) and \(h^u=h-\mathbf1_{r=H}\). Precursor P satisfies P+a+h=M. Common fuel F and incident support E are nonnegative integers. An offspring is free; only association installs a resident.

| Event | Update | Propensity |
|---|---|---|
| Form A | P+F→free A+spent | μdPF |
| Form H | P+F→free H+spent | μdPF |
| Associate type i | Free i becomes resident; F→spent | ξ n_i^u F, only if r=∅ |
| Effective repair | c:0→1; F→spent | ρF, only if r=A and d=1 |
| Capture | E→f | gE, only if c=1 and f=0 |
| Local copy | P+f→free offspring of resident's type+spent | βPf, only if r≠∅ |
| Bulk copy of type i | P+F→free offspring of that template's type+spent | β₀n_iPF |
| Wear | Molecule→P; resident wear also sets r=∅ | δ per molecule |
| Damage | c:1→0 | αc |
| Leakage | One F or f→spent | ℓ per usable fuel unit |

Wear does not reset the site or local fuel. Both types share the same formation, association, copying and wear rules. Their only functional distinction in the main law is that A can repair. The general event rule allows a resident H to use inherited local fuel; reaching such a state also requires enough fuel for its formation and association, and is not asserted for every fixture. The local-copy rule therefore recognizes a present template, not a label meaning “useful.”

The common preparation is

\[
\boxed{M=3,\quad P=3,\quad a=h=0,\quad r=\varnothing,
\quad c=f=0,\quad F=4,\quad E=1.}
\tag{1}
\]

The damaged site couples equally to both candidate-formation routes. The law does not preferentially propose the useful type. The availability of both reaction products and their properties is nevertheless supplied chemistry, not a derivation of an open-ended response repertoire.

Let U,B,R,K_l,K_b,L count total untemplated formation, association, repair, local copying, bulk copying and leakage. Every history preserves

\[
\boxed{F_t+f_t+E_t+U_t+B_t+R_t+K_{l,t}+K_{b,t}+L_t
=F_0+f_0+E_0=5,}
\tag{2}
\]

and P+a+h=3. Each formation, association, repair or copy pays a fuel unit; capture relocates one finite incident packet. Precursors returned by wear carry no restored fuel.

The natural-number rank

\[
V=4E+2(F+f)+c+(a+h)
\tag{3}
\]

strictly decreases on every event: formation, effective repair, either copy, wear and damage decrease it by one; association, capture and leakage decrease it by two. This is the same rank used by the implementation and Lean event-law proof. This gives a deterministic finite event bound. The reachable state space and all rates are also bounded, so the CTMC is nonexplosive. Terminal waiting is not further active renewal. The finite fixture cannot generate indefinite physical activity.

From the same all-damaged, variant-absent and association-absent preparation with F₀<3, capture cannot bootstrap. Before any capture, a successful route must separately pay formation, association and repair. No other event produces common fuel or an intact site. Arbitrarily large uncaptured E does not remove that obstruction.

## 2. An unconditional statistic and its generator

Use

\[
Z=a-h.
\tag{4}
\]

This counts response molecules, excluding unused precursor; it is defined even when neither type exists. It is a signed abundance contrast, **not** a frequency, fixation probability or an assertion about typical trajectories. Recording Z does not affect any transition.

The two formation propensities are equal at every state, so their contributions to its generator cancel exactly. Association, repair, capture, damage and leakage do not directly change Z. Thus

\[
\boxed{\mathcal LZ
=\beta Pf\bigl(\mathbf1_{r=A}-\mathbf1_{r=H}\bigr)
+(\beta_0PF-\delta)Z.}
\tag{5}
\]

The bulk term shows why equal per-capita rates do not generally imply zero expected abundance difference. Its coefficient can correlate with Z through previous repair and fuel use. Nor does the earlier stopped-frequency martingale apply here: untemplated formation continues throughout this law, and Z is a different observable. In particular, a shared-return comparator must be analyzed in its own right rather than declared neutral from the preceding contest theorem.

## 3. Zero-loss reference: exact terminal result and finite-time bound

Set μ=ξ=ρ=g=β=1 and first take β₀=α=δ=ℓ=0. This is an explicit reference law, not the final theorem's absence of costs: formation, association, repair and copying still consume fuel.

No resident can leave in this reference. Only resident A can make the site intact, so reachable states satisfy f>0 ⇒ r=A. Local H copying is therefore impossible. Equation (5) reduces to the nonnegative local A-copy intensity, and Dynkin's formula gives

\[
\mathbb E Z_H=\mathbb E K_{l,A}(H)\ge0.
\tag{6}
\]

This equality integrates over **all** founder outcomes, including H-first and failed histories. It does not discard unfavorable runs.

Consider the explicitly mixed path

\[
\text{form H; form A; associate A; repair; capture; copy A.}
\tag{7}
\]

It pays for two formations, association and repair using the four initial common fuel units. Its copy uses the one newly captured local unit, with H still present. The aggregate exit rates are 24,15,8,3,1,1. The required choices have probabilities 1/2, 6/15, 2/8 and 1/3; capture and the final copy have no competing events. Their product is 1/60.

For H=12, require every wait in (7) to be at most two. Every listed rate is at least one, and e²>7, so its probability exceeds \(\tfrac1{60}(6/7)^6\). Combining this with (6), rather than treating the path's favorable score as representative of other runs, gives

\[
\boxed{\mathbb E Z_{12}^{(0)}>\tfrac1{60}(6/7)^6
=3888/588245.}
\tag{8}
\]

Let K_A^mixed count local A copies whose pre-event state has h>0. At most one local copy can occur because E₀=1 and local fuel starts empty; each such copy consumes that packet. Hence K_A^mixed∈{0,1}, including in the positive-loss law, and the same reference lower bound applies to its expectation. This explicitly witnesses useful reconstruction in the presence of the alternative, without conditioning on a selected founder or survivor.

An exact terminal reference is also available. With no losses or bulk copying, every effective repair is followed by exactly one local A copy. No resident can leave, and a third formation before repair would spend too much common fuel to pay for both association and repair. The successful pre-capture histories partition as follows:

| Prefix through repair | Probability | Is H present at the ensuing local copy? |
|---|---:|---|
| A forms; A associates; repair | 1/50 | No |
| A forms; A associates; one further A or H forms; repair | 2/75 | Half of these histories |
| Two A form; A associates; repair | 1/30 | No |
| A then H form; A associates; repair | 1/60 | Yes |
| H then A form; A associates; repair | 1/60 | Yes |

For example, after the first A forms, formation rates are six for each type and association is three. After direct association, the formation rates are four each and repair is two. After a second formation and association, the two formation rates and repair are one each. These races give the displayed fractions. The prefixes are disjoint and exhaustive, yielding

\[
\boxed{\mathbb E Z_\infty^{(0)}=17/150,\qquad
\mathbb E K_A^{mixed,(0)}(\infty)=7/150.}
\tag{9}
\]

Every productive history has at most six events and every exit rate is at least one. Requiring all its waits to be at most two therefore also gives the stronger useful bound \(\mathbb E Z_{12}^{(0)}>(17/150)(6/7)^6\). The primary theorem below deliberately uses the single mixed path to make its competition witness explicit.

## 4. Two causal controls and a positive-rate theorem

The **repair-disabled control** deletes effective repair. The **ineffective-repair control** instead spends the same one common fuel unit per attempt at the same rule ρF when A occupies a damaged site, but leaves that site damaged. All other rules and initial quantities are identical. Matching the price and propensity rule of an attempt does not assert equality of total expenditure after states diverge.

In either zero-loss reference control, the site stays damaged and local fuel remains absent. Consequently \(\mathcal LZ=0\) and \(\mathbb E Z_H=0\) for every H. The ineffective A-specific attempts can alter common fuel and later formation rates, but A and H formation still have equal instantaneous propensities.

Restore positive nuisance rates in each arm:

\[
\boxed{\alpha=\delta=\ell=\beta_0=\varepsilon=1/1000000.}
\tag{10}
\]

Couple each arm to its own zero-loss reference until its first added event. The hazard of damage, wear, leakage and bulk copying together is at most

\[
\varepsilon(1+3+5+10)=19\varepsilon.
\tag{11}
\]

Here c≤1, a+h≤3, total usable fuel≤5, and P(a+h)≤2 because P+a+h=3 with integer counts; hence PF(a+h)≤10. These bounds include returned precursor and all later states. The event-law ledgers are not restricted to the displayed successful path.

The coupling fails by H with probability at most 19εH. Since −3≤Z≤3, a single arm's expected Z changes by at most 6·19εH. Comparing two independently coupled arms costs at most 228εH. Thus, for either control C,

\[
\boxed{\mathbb E Z_{12}^{\rm effective}
-\mathbb E Z_{12}^{C}
>\frac{3888}{588245}-\frac{2736}{1000000}
=\frac{28482021}{7353062500}>0.00387.}
\tag{12}
\]

The mixed-copy mark has range [0,1], so one-arm coupling gives the separate bound

\[
\boxed{\mathbb E K_A^{mixed}(12)
>\frac{3888}{588245}-\frac{228}{1000000}
=\frac{187694007}{29412250000}>0.00638.}
\tag{13}
\]

These results establish both an unconditional causal abundance contrast and actual copying while an alternative is present, with paid formation and association, finite support, damage, wear, leakage and common-pool copying. The bounds are conservative and intentionally uncalibrated. They do not establish a fixation advantage or a positive difference on every realized history.

The positive-rate repair-disabled process additionally has exact label-swap symmetry: swapping A and H everywhere preserves every rule and the initial state. Its expected Z is therefore exactly zero. The ineffective-repair process does **not** have that symmetry because only A pays futile attempts. With bulk copying, its expectation cannot be declared zero from (5); the two-arm perturbation above deliberately does not assume this.

## 5. The same work chemistry changes direction with source availability

Add a catalytic-work loss parameter σ. Split an A repair attempt into two branches with total propensity ρF: rate (1−σ)ρF repairs while retaining the resident; rate σρF repairs while converting the resident to precursor and leaving the site vacant. Both spend one common fuel. This is a declared reaction cost, not a negative score supplied by an observer.

Use σ=1/10000 and nuisance rates α=δ=ℓ=β₀=ε=1/1000000000. This is a separately declared sign-comparison fixture, selected analytically before numerical evaluation. Keep M=3, F₀=4 and H=12. Compare E₀=1 with E₀=0 while keeping **all** chemistry and rate parameters fixed. The repair-disabled arm remains exactly label-symmetric in either environment, so its expected Z is zero. The following bounds use that verified symmetry rather than assuming neutrality of the ineffective-repair control.

With E₀=1, first compare the zero-nuisance σ>0 law with the σ=0 reference. Without damage or resident wear, there is at most one repair attempt. The attempt's outcome differs with probability at most σ, giving an expectation perturbation at most 6σ for Z. Restoring nuisance rates costs at most 6·19εH. Using the all-prefix bound after (9),

\[
\boxed{\mathbb E Z_{12}^{E=1}
>\frac{17}{150}(6/7)^6-6\sigma-1368\varepsilon
>0.0443.}
\tag{14}
\]

With E₀=0, local fuel remains zero even after repair. In the zero-nuisance reference with the same σ,

\[
\mathcal LZ=-\sigma\rho F\mathbf1_{r=A,d=1}\le0.
\tag{15}
\]

The first repair attempt has exactly the same prefix law as in the source-present reference: capture cannot occur before repair. Its terminal probability is 17/150. Every successful prefix has at most four events; requiring each wait to be at most two bounds its probability by H=12 below by \((17/150)(6/7)^4\). Its catalytic-loss probability is σ times that bound. Symmetric formation cancels in expectation, giving a negative contribution equal to expected catalytic losses.

The source-free nuisance hazard is at most 16ε: site one, templates three, usable fuel four, and PF(a+h) at most eight. Its one-arm expectation perturbation is at most 6·16ε·12=1152ε. Therefore

\[
\boxed{\mathbb E Z_{12}^{E=0}
<-\sigma\frac{17}{150}(6/7)^4+1152\varepsilon
<-0.00000496.}
\tag{16}
\]

The same formation, access and work rules thus yield opposite expected type contrasts relative to the repair-disabled control as the source changes. The negative margin is deliberately small: this is an existence proof, not a robustness estimate or a biological rate claim. Source removal alone, without differential work loss, need not produce a negative contrast: a shared fuel burden can reduce total reconstruction without favoring either label. Counts, copying, capture and work losses must be reported separately. This sign change does not mean the mechanism learned to revise its rule when the source disappeared.

## 6. Diagnostic cases and changes of statistic

The first analytical fixture used M=2,F₀=3,E₀=1. Its zero-loss expected Z is 1/18, but productive copying requires the prefix A formation → A association → repair. If both types form before repair, too little common fuel remains to associate and repair. Its enrichment therefore concerns differential clonal reconstruction across symmetric founder histories; it is not evidence of mixed-population competition. This limitation prompted the primary redesign to M=3,F₀=4 before the primary numerical run. The smaller fixture remains a useful boundary case and must not be retrospectively presented as having closed that interface.

A **shared-return diagnostic** moves captures into common F and replaces the local-copy channel by ordinary copying of either type from common F at per-capita rate βPF, with β=1 and β₀=0 in its reference. This primary copying route is available from the start, including from initial common fuel. Paid association and repair remain unchanged. Exact first-step recursion under this distinct law gives expected terminal Z=4/147 for the main M=3,F₀=4 fixture (and 1/48 for the earlier M=2,F₀=3 fixture). For the main fixture, conditioning only to evaluate the recursion after the symmetric first formation gives values 253/147 and −5/3; their equal-weight average is 4/147. The recursion is \(v(x)=\sum_y q(x,y)v(y)/\sum_yq(x,y)\), with v=a−h at absorbing states. All reachable transitions decrease the corresponding finite rank, so this evaluation has no recurrence ambiguity.

These shared-return values are not zero. Symmetric untemplated formation, type-dependent effects on the resource history, and a count contrast are different conditions from the earlier fixed-seed, no-immigration frequency martingale. The shared diagnostic does not serve as an unproved upper bound at H=12, and is not needed for (12)–(16). A reported frequency with a convention for an empty population likewise remains a separate observable.

The executable no-copy diagnostic makes the distinction concrete: expected A and H counts are equal, but the expected A fraction, assigning 1/2 when the population is empty, is about 0.514444 at H=12. Type composition correlates with total population size because repair changes ongoing formation. The ineffective-repair arm also has an above-half mean fraction without local copying. Empty populations are very rare in these cases. Thus a mean fraction above one half cannot by itself establish the copying effect proved here; the signed-count generator identity and separately marked mixed-copy events identify that effect.

With positive wear and finite support, the ledger bounds all births. Eventually every remaining response molecule disappears, so Z tends to zero almost surely. The positive and negative theorems concern a declared finite horizon; they do not establish indefinitely retained abundance differences.

## 7. What is joined, and what still cannot change

The new law generates both candidate molecules from an initially empty response population, pays for their association, and connects actual repair consequences to differential reconstruction. This closes the preparation mismatch between a variant-absent formation witness and an already seeded contest **for this explicit finite construction**. It replaces neither earlier source law; their claims and failure cases retain their scopes.

The model still fixes how damage triggers proposals, which two chemistries can form, how a template specifies its offspring, and which resident accesses local fuel. States change the available resources and occupants, but there is no inherited variant of the association/copying rule itself and no transition that creates one. Thus the construction has an effective selector with changing inputs, not a derived mechanism for revising the selector. Intervening on μ, locality, σ or the copying law between arms is an analyst's comparison, not endogenous revision.

The next bridge must represent alternative selection mechanisms as actual formed, maintained and transmissible structures; derive their consequences and retention under the same resource history; and preserve neutral sharing, exploitation and costly failure regimes. Individual learning would additionally require a continuing organization whose own response mechanism changes through the specified history. Neither a positive Z nor a formal proof of it supplies the representation and evaluative capacities used by the concern results.

Exact arithmetic check:

```python
from fractions import Fraction as Q
mixed = Q(1, 60) * Q(6, 7)**6
assert mixed == Q(3888, 588245)
assert mixed - Q(2736, 1000000) == Q(28482021, 7353062500)
assert mixed - Q(2736, 1000000) > Q(387, 100000)
assert mixed - Q(228, 1000000) == Q(187694007, 29412250000)
assert mixed - Q(228, 1000000) > Q(638, 100000)
sigma, eps = Q(1, 10000), Q(1, 1000000000)
positive = Q(17, 150) * Q(6, 7)**6 - 6*sigma - 1368*eps
negative = sigma * Q(17, 150) * Q(6, 7)**4 - 1152*eps
assert positive > Q(443, 10000)
assert negative > Q(496, 100000000)
assert (Q(253, 147) - Q(5, 3))/2 == Q(4, 147)
```

These arithmetic checks do not certify the generator, coupling or physical interpretation; those require the separate mathematical argument and review.
