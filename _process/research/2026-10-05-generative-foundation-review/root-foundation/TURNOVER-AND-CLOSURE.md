# Turnover and the necessity of recurrent support

This note strengthens the universal core of [Alignment as the Reproduction of Its Conditions](../../../history/2026-10-05-specialist-dossier/final-synthesis/INTEGRATED-THEORY.md). It establishes two conditional necessity results: unbounded turnover in a finite vulnerable support system requires recurrent external provision or an internal renewal cycle; and bounded component lifetimes give a finite deadline beyond which an acyclic support system cannot function. The second result does not require treating knowledge, authority, or competence as additive stocks.

These are mathematical restrictions on possible histories under explicit premises. They do not establish that every physical system satisfies those premises, that a necessary cycle is sufficient for functioning, or that every maintained component belongs to one mutually maintaining organization. Differential selection is not a premise or a consequence of these results. That mechanism requires an additional causal model.

## 1 From balance to recurrent support

Fix a finite set of support types \(V=\{1,\ldots,n\}\). A type can identify a replaceable functional capacity rather than a particular material component. For each \(i\), suppose an independently justified accounting gives

\[
c_i(t)=c_i(0)+E_i(t)+\sum_{j\in V}R_{ji}(t)-L_i(t),
\qquad c_i(t)\ge0.
\tag{T1}
\]

Here \(c_i(0)<\infty\) is the initially available reserve; \(L_i\) is cumulative loss; \(E_i\) is cumulative provision from outside the tracked organization; and \(R_{ji}\) is cumulative provision credited to activity of type \(j\). All cumulative terms are nonnegative, nondecreasing, zero at zero, and finite at every finite time. A protected positive floor can be subtracted from a capacity before applying this notation.

The quantities must refer to the same enabling function in that row. Equation (T1) does not permit adding unrelated resources as if they were interchangeable. Provision credits must exhaust the actual provision without double counting. If several sources are jointly necessary, a separate event or hypergraph description can retain that conjunction; an additive attribution is not itself a proof that each credited channel can act alone. Every internal source attribution must have a causal interpretation established independently of this accounting.

Define the types with unbounded turnover by

\[
U=\{i\in V:L_i(\infty)=\infty\}.
\tag{T2}
\]

The notation \(X(\infty)\) means the monotone limit as \(t\to\infty\). It does not suppose that an infinite quantity is available at a finite date.

One further premise is essential:

> **Productive vulnerability.** If an internal type supplies unbounded cumulative provision, its own cumulative loss is unbounded:
> \[
> (\exists i:\ R_{ji}(\infty)=\infty)\quad\Longrightarrow\quad L_j(\infty)=\infty.
> \tag{T3}
> \]

This permits finite bursts from a nonrenewed initial reserve. It excludes an immortal supplier that can deliver indefinitely without any turnover of its enabling capacity. A sufficient, quantitatively stronger version is a bound \(R_{ji}(t)\le a_{ji}+b_{ji}L_j(t)\) for every outgoing channel, with finite nonnegative constants in the corresponding units. Another sufficient version simply assumes unbounded loss for every tracked internal supplier. Neither version is a logical consequence of change alone.

Construct a graph on \(U\) with edge \(j\to i\) exactly when \(R_{ji}(\infty)=\infty\). Add an external source vertex \(\partial\) and edge \(\partial\to i\) exactly when \(E_i(\infty)=\infty\). These edges record provision along the actual history, not every provision channel that could have existed.

### Theorem 1 Recurrent support alternative

Under (T1)–(T3), every \(i\in U\) is reachable either from \(\partial\) or from a directed cycle of internal types in \(U\). A self-loop counts as a cycle. If all external provisions are finite in total, every \(i\in U\) is downstream of an internal directed cycle. In particular, if \(U\ne\varnothing\), an internal cycle must exist.

**Proof.** Nonnegativity in (T1) gives

\[
L_i(t)\le c_i(0)+E_i(t)+\sum_jR_{ji}(t).
\tag{T4}
\]

If \(i\in U\), finiteness of \(V\) and of the initial reserve implies that either \(E_i(\infty)=\infty\) or at least one \(R_{ji}(\infty)=\infty\). In the latter case (T3) gives \(j\in U\). Thus every internal vertex has an incoming internal or external edge. Starting from \(i\), follow one incoming edge backward. Either this procedure reaches \(\partial\), or an internal vertex repeats because \(U\) is finite. The repeated portion is a directed cycle, followed in the forward direction by a path to \(i\). If every external total is finite, the first alternative is unavailable. \(\square\)

Equivalently, when external totals are finite, every source strongly connected component of this graph contains a cycle. A downstream vertex need not itself lie on a cycle. For example, \(1\leftrightarrow2\to3\) satisfies the graph conclusion although type 3 need not support either 1 or 2. Consequently, the theorem establishes a recurrent supporting core, not complete mutual dependence of every named component. Full organizational closure requires more information about the dependency structure.

The conclusion also does not establish that the cyclic core is independently sufficient. It may additionally need nonrecurrent initial conditions, raw materials, external energy, or conjunctive support channels not captured by an additive attribution. A necessary recurrent cycle can coexist with dependence on external provision.

## 2 A finite deadline without stock variables

The next result formulates the time-scale argument through component lifetimes and actual creation or renewal events.

Assume:

1. There are finitely many relevant support types \(V\). Every function under examination requires a currently functioning instance of at least one of these types.
2. A functioning episode of type \(i\), begun at time \(b\), ends no later than \(b+\tau_i\), where \(0<\tau_i<\infty\). A repair that extends this deadline counts as a new functioning episode, with its own support requirement. Initial episodes begin at times at most zero.
3. Every episode begun after zero requires at least one earlier begun parent episode that is functioning when the new episode begins. If the parent has type \(j\) and the new episode type \(i\), the permitted causal support graph has edge \(j\to i\). Mere historical influence from a parent that has already ceased functioning does not satisfy this premise; any effective stored intermediate is another support episode.
4. No new externally supplied organized episode enters after zero, and no episode arises without the parent required by premise 3. External energy and raw material may be available, but their conversion into a functioning episode still requires that parent.
5. Events have an ordinary causal ordering, with no infinite number of successive renewal events accumulating at a finite time. Types, their lifetime bounds, and the support graph apply throughout the stated interval.

The parent relation can represent assistance, instruction, production, authorization, or repair, if that interpretation is independently supported. A permission that remains effective after its original author leaves is a continuing support episode; it is not automatically absent merely because its author is absent.

### Theorem 2 Acyclic lifetime bound

If the type graph is acyclic, define in a topological order

\[
d_i=\tau_i+\max\bigl(\{0\}\cup\{d_j:j\to i\}\bigr).
\tag{T5}
\]

Every functioning episode of type \(i\) ends by \(d_i\). Consequently no function described in premise 1 can continue beyond

\[
D=\max_i d_i
=\max_{\text{directed paths }p}\sum_{i\in p}\tau_i
\le\sum_i\tau_i.
\tag{T6}
\]

Singleton paths are included. Continued functioning at a time greater than \(D\) therefore implies either a directed cycle in the type graph or a failure of at least one stated premise.

**Proof.** For a type with no incoming edge, no new episode can begin after zero; its initial episodes all end by \(\tau_i=d_i\). Inductively, assume that all predecessor episodes end by their corresponding \(d_j\). A new type-\(i\) episode requires a predecessor functioning at its birth, so it begins no later than \(\max_{j\to i}d_j\) and ends no later than that value plus \(\tau_i\). Initial episodes end by \(\tau_i\), which the extra zero in (T5) covers. Topological induction proves the first claim. The recurrence is the longest weighted path recurrence, giving (T6). \(\square\)

If several parents are jointly required, choosing any one actually required parent preserves the proof. Keeping all obligatory parents can yield a tighter bound, since all must remain available at the birth. The displayed maximum is a safe upper bound covering alternative parents. It does not change an AND requirement into an OR claim of sufficiency.

The finite bound is an observable implication, not merely an asymptotic statement. Once lifetimes and the support interface are bounded independently, continued operation after \(D\) rejects the conjunction of the acyclic model and those bounds. It does not uniquely establish which premise failed. The alternatives include an omitted supplier, a stored intermediate with a longer lifetime, a permitted renewal channel, or a genuinely new functional type.

The no-accumulation assumption makes the event semantics physically ordinary. The acyclic finite-type bound itself already limits the length of each parent chain; it does not rely on counting all births or on a positive lower bound on inter-event time.

## 3 Concrete witnesses and the limits of a cycle

Consider an initial trainer episode of type A lasting at most two years. It can establish type-B training materials lasting at most three years; functioning B materials can establish type-C operator competence lasting at most five years. The only edges are \(A\to B\to C\). Then \(d_A=2\), \(d_B=5\), and \(d_C=10\) years. Creating arbitrarily many copies near the available deadlines cannot extend the last competence beyond year 10 under these premises. Observation of the described function in year 11 forces revision of the acyclic explanation or one of its lifetime and boundary assumptions. The numbers and institutional mapping are a constructed illustration, not estimates.

A cycle can remove this particular deadline. Let A and B episodes each last two time units. Begin with an A episode at time zero; it creates B at time one, that B creates A at time two, and so on. Each birth has a live, earlier parent, and all lifetimes are respected. The type graph is \(A\leftrightarrow B\), while the particular episodes form a forward causal chain. This is an admissible indefinitely renewing schedule if all unmodeled resource and other requirements are supplied. The type cycle does not imply an event causing its own earlier cause.

Conversely, the same permitted cycle can fail. If creating B from A takes three time units while every A episode expires after two and no intermediate stores the required support, the specified route cannot complete. A graph without rates, deadlines, resources, and actual execution cannot establish viability. The earlier [integrated theory](../../../history/2026-10-05-specialist-dossier/final-synthesis/INTEGRATED-THEORY.md) supplies those further requirements.

A stock witness of Theorem 1 is \(c_1=c_2=1\), \(L_1(t)=L_2(t)=t\), \(R_{12}(t)=R_{21}(t)=t\), and \(E_1=E_2=0\). Both balances hold and the recurrent graph has a two-cycle. These capacities are organized functional stocks, not conserved matter: external feedstock and energy can power the described transformations without directly providing organized replacements. The witness verifies consistency of the mathematical premises; it does not model a thermodynamically isolated perpetual machine.

## 4 Why the physical and boundary premises matter

**A durable supplier.** Let type 1 have constant capacity, no loss, and supply \(R_{12}(t)=t\). Let type 2 lose and receive at that same rate. Type 2 persists indefinitely in the acyclic graph \(1\to2\). This violates productive vulnerability for type 1 and the finite lifetime premise for its event representation. The example locates a missing premise; it does not establish that an actual physical supplier is immortal.

**Finite total loss.** A capacity \(c(t)=1+e^{-t}\) loses continuously but remains above one forever, with no provision. Its loss is finite in total. Continual change or a positive instantaneous loss rate alone does not imply reserve exhaustion. For a stock theorem, unbounded cumulative required loss is the relevant assumption.

**Unbounded novelty of types.** Suppose type \(i\) begins at time \(i\), functions for two time units, and creates the next type at time \(i+1\). The function can continue forever along the infinite acyclic chain \(0\to1\to2\to\cdots\). Every instance turns over; no finite deadline for all types follows. Grouping these distinct realizations under one recurring functional role produces a type self-loop, but the adequacy of that grouping must preserve the relevant causal and functional distinctions. It cannot be used to assume the conclusion.

**External organization.** Recurrently importing a trained operator, replacement controller, or effective institutional rule can support internal functioning without an internal renewal cycle. Theorem 1 records this as external recurrent provision. Expanding the boundary may reveal the supplier's renewal system, but the theorem does not assert that the expansion eventually ends in one finite internally closed organization.

**External energy and immutable constraints.** The absence of external organized replacements is not the absence of energy, matter, or lawful physical constraints. A maintained enzyme can catalyze replacements using imported substrates and energy; the feedstock and the organized catalyst have different causal roles. Where raw inputs spontaneously yield an effective functional instance without a required internal parent, the event theorem's parent premise fails. An undegrading physical constraint can also supply support outside the productive-vulnerability class. Relabeling either case as internal renewal would conceal the premise rather than prove it.

**Recurrent edges without full closure.** Infinite cumulative service on a finite edge implies arbitrarily late service under local finiteness. Nevertheless, its occurrence need not mean all edges are simultaneously active, that they share one token-level ancestry, or that every vertex helps reproduce every other vertex. Time aggregation reveals a recurring causal support template, not instantaneous reciprocal causation.

**Substitution and changing roles.** Material replacement within a retained functional role fits either theorem when the measurements and lifetime bounds apply to that role. Changes in the function itself require an explicit amended description. If no finite set of roles with valid bounds covers the evolving process, the finite-type theorem is unavailable. A sequence of locally valid descriptions is not automatically one globally finite description.

## 5 A quantitative strengthening when service bounds are available

The existence of a cycle is only a topological prerequisite. A further conditional bound rules out cycles whose maximum possible amplification is too small.

Let \(S_i(t)\) be a nonnegative cumulative service or production measure for type \(i\), finite at every finite time and measured in its own fixed units. It must be independently specified, not obtained by adding different recipients' incommensurable capacities. Suppose independently justified bounds give

\[
S_i(t)\le a_i+b_iL_i(t),\quad
R_{ji}(t)\le\alpha_{ji}S_j(t),\quad
E_i(t)\le e_i<\infty,
\tag{T7}
\]

with all constants finite and nonnegative and conversion coefficients carrying the required units. Individual routing bounds \(\alpha_{ji}\) may be conservative; they need not be simultaneously attained. Set

\[
k_i=a_i+b_i[c_i(0)+e_i],\qquad B_{ij}=b_i\alpha_{ji}.
\tag{T8}
\]

Equations (T4) and (T7) imply \(S(t)\le k+BS(t)\). If the nonnegative matrix \(B\) has spectral radius \(\rho(B)<1\), the nonnegative inverse \((I-B)^{-1}=\sum_{m\ge0}B^m\) exists, and

\[
S(t)\le (I-B)^{-1}k\quad\text{for every }t.
\tag{T9}
\]

**Proof.** Rearrange the finite-time inequality as \((I-B)S(t)\le k\) and multiply by the entrywise nonnegative inverse. \(\square\)

Then (T4) and the routing bounds give a finite total-loss bound for every type. Thus under (T7), unbounded required turnover with only finite external organized provision requires \(\rho(B)\ge1\). This is a necessary condition for this particular independently justified bound, not a sufficient growth law or an exact bifurcation threshold of an unspecified nonlinear system. Loose bounds can satisfy \(\rho(B)\ge1\) while the actual system still fails. Any finite acyclic routing graph has nilpotent \(B\), so its spectral radius is zero; Theorem 1's obstruction then has a quantitative finite-reserve counterpart.

This obstruction is invariant under positive changes of service units. If \(S'=DS\) for a positive diagonal matrix \(D\), then \(B'=DBD^{-1}\), so \(\rho(B')=\rho(B)\). This is a specified mathematical invariance; it does not imply that arbitrary coarse-graining preserves the causal support graph or the validity of the bounds.

For instance, two types with routing only to each other, \(\alpha_{12}=\alpha_{21}=1\), and \(b_1=b_2=1/2\) give \(B=\begin{pmatrix}0&1/2\\1/2&0\end{pmatrix}\) and \(\rho(B)=1/2\). A cycle is present, but finite seeds and finite external organized inputs permit only finite total output under these service bounds. This concerns output of functional provision per unit of incurred loss, not an assumed thermodynamic efficiency for an arbitrary social variable.

## 6 Prior work and the scientific claim

Organizational closure already treats biological constraints as mutually maintained across relevant timescales. The biological organization literature explicitly considers changing material realizations and functions while maintaining relations of dependence. This note follows that research direction rather than claiming to originate it. See [Mossio, Montévil, and Longo, 2016](https://montevil.org/publications/articles/2016-mml-theoretical-principles-organization/).

The graph step is established mathematics. In elementary catalytic reaction systems, Steel and Hordijk's Theorem 1 characterizes autocatalytic sets by directed cycles and describes recurrent cores with downstream components. Their graph construction also uses formal self-loops for catalysts supplied by the food set. Our theorem retains an explicit external vertex because external organizational supply is precisely the alternative to internal recurrence that must remain visible. Their paper also distinguishes a network's catalytic structure from its ability to be established through available precursor reactions and develops extensions with rates. See [Steel and Hordijk, 2018, Sections 1 and 2](https://arxiv.org/html/1801.03953v2).

The graph lemma, topological lifetime induction, and nonnegative matrix bound are elementary consequences of established methods. They have been proved here to expose the premises and their implications; no claim of theorem priority has been established. The candidate contribution to this project is their integration into a cross-domain diagnostic: distinguish inherited reserve from renewal; distinguish internally renewed support from continuing external organizational provision; derive a deadline for acyclic explanations; and preserve the separate obligations of establishing feasible rates, actual execution, and legitimate evaluations.

The strongest warranted foundational statement is therefore:

> For a finite system whose functioning supports must turn over, continuation beyond inherited lifetimes requires either renewed support from outside the tracked organization or recurrence in its internal support relations. When that external organizational provision is absent and the turnover premises hold, an internal recurrent supporting core is necessary. Its effective rates, resources, timing, selection, and evaluation determine whether it actually sustains an acceptable function.

This advances the argument from a representation theorem to a necessity theorem about turnover and support. Its mathematical universality is genuine within its premises. Establishing those premises across physical domains, and establishing differential selection or full mutual closure, remain separate scientific claims.
