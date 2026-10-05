# Identical observations under a change of latent origin

Analytic extension, 5 October 2026. Derived after the frozen simulation, not used to change its policies or results. This is an elementary identification argument, with no claim of novelty or empirical universality.

Consider x_next=a x+u+g+w, y=x+b+ε, z=x+d+η, with constant b,d,g. Assume the class of possible initial states, parameters, and observation laws admits the shifts below. Couple the same realized noise and internal controller randomness in the two worlds. A controller may use the full permitted observation/action history, including deciding when to observe z, but not hidden parameters supplied by an oracle.

For constant c set x′=x+c, b′=b−c, d′=d−c, and g′=g+(1−a)c. Then y′=x+c+b−c+ε=y and z′=z. Equal histories yield equal controller actions and acquisition decisions. Moreover

\[
a(x+c)+u+g+(1-a)c+w=(ax+u+g+w)+c.
\]

The shifted state relation is preserved at the next step. Induction establishes equality of every observed history and action sequence. Randomized procedures also have the same distribution when their internal randomness is coupled. Further processing of this history cannot distinguish the two worlds.

Two shift-invariant combinations, directly recoverable in the noiseless case, are b−d and g+(1−a)b. Indeed y−z=b−d+ε−η, while y_next−a y−u=g+(1−a)b+w+ε_next−a ε. Statistical identification with noise requires further assumptions about its law. The augmented state (x,b,d,g) has the unobservable direction (1,−1,−1,1−a). With both sensors and the next ordinary observation, the linear observation structure has rank three, leaving this one-dimensional ambiguity when the full shifted class is allowed.

By contrast, if g is known zero and a≠1, the noiseless inverse is

\[
b=(y_1-a y_0-u_0)/(1-a),\quad x_0=y_0-b,\quad d=z_0-x_0.
\]

Thus a biased reference is not fundamentally unidentifiable under the anchored model. An estimator that assumes d=0 can still be misspecified. These are different claims.

At a=1, even known g does not remove the shift ambiguity. When a is near one, the noiseless inverse has a small denominator, and noisy estimation requires care; identifiability is not the same as accurate estimation at finite sample size.

A fixed prior may also remove distributional equivalence. For example, if E[x_0]=0 is known and measurement noises have known zero means, repeated-episode means anchor E[y_0]=b and E[z_0]=d when those biases are fixed across episodes. Shifting initial states while pretending to retain that same prior is not an admissible counterexample. Statistical identification across episodes does not give an exact state value from a single noisy episode.

For a concrete loss counterexample take a=.8, zero noise and u=0. World A has (x_0,b,d,g)=(0,0,0,0). World B has (1,−1,−1,.2). Both always report y=z=0, but x is respectively zero and one. The 60-step squared-state losses are zero and 60. Therefore observation/action invariance does not imply loss invariance when the target remains absolute x=0.

If the target or coordinate convention were shifted together with x, a coordinate-relative loss could instead be invariant. That would be a different evaluative mapping. A proof must specify what changes and what stays fixed.

The [exact checks](results/analytic-extension-checks.json) use rational arithmetic on six coupled trajectories of twenty steps each. The proof covers the full stated class; those finite checks corroborate its implementation. It neither proves all self-knowledge impossible nor imports the unanchored assumptions into the earlier anchored simulation.
