# AI/AGI/ASI Readiness — Layered Copy

## Public (plain, ~220 words)
We live inside a pattern that rewards simple numbers (likes, profits, rankings) and then rewrites rules so those numbers keep winning. That pattern—a meta‑attractor—shapes how we build and deploy AI. If we train and release more powerful systems inside this loop, they will supercharge it: the proxy becomes the purpose, and alternatives fade. Before adding speed, we need rails.

What “rails” look like: slow or cap systems where risk runs hot; prove safety before scaling; add “tripwires” so deployment pauses automatically when tests fail; keep independent oversight with real authority; and check a few numbers that tell us whether the proxy is drifting from what we actually care about. When those gates are in place, AI can help us coordinate and protect the commons instead of turning everything into a race.

Short version: Recognize the pattern. Add rails. Then scale.

## Practitioner (policy/product/governance, ~260 words)
Environment selects. Today’s gradients reward capability over safety and legibility over substance. Readiness shifts the gradient: (i) compute tiers unlock only with external safety evidence; (ii) deployments are tripwired (eval fail → pause; rollback tested); (iii) oversight is polycentric with sortition to reduce capture; (iv) minimum diagnostic floors: PWC≥0, SC≥min, PDI in band, CR↓, DE↑; (v) procurement and prestige pay for reliability and resilience, not just speed.

Operational guidance: publish the real objective function; maintain multi‑objective gates (value created, harm avoided, uncertainty reduced); rotate authority and staff (cooling‑off); record provenance for high‑reach content; disclose incidents on a fixed clock. Use dashboards quarterly: pair PWC/PDI/SC with qualitative audits to prevent name–reality drift.

Sequence: Recognize → Slow/Cap → Align → Coordinate → Transform. Don’t scale before evidence. Don’t add thrust before rails.

## Scholar (formal/technical, ~260 words)
Readiness is a two‑timescale control problem. Fast layer: learning/market dynamics; Slow layer: rule space (caps, audits, objective weights, oversight). We seek a meta‑attractor M in rule space such that (i) fast dynamics fall into safe attractors (barrier invariance, negative local exponents), and (ii) the slow update law drives rules back to M under disturbances (meta‑Lyapunov stability).

Sketch: define PWC, PDI, SC as operational diagnostics; add CR and DE. Choose gating sets G where PWC≥0, SC≥τ, PDI≤β, CR≤γ, DE≥δ. Compute gates tie capability to safety evidence; pacing/latency penalties reduce spectral radius in arms‑race subsystems; tripwires define automatic stop when constraints are violated. Oversight is polycentric with sortition to reduce capture probability; provenance constrains deceptive competence. The slow update law adjusts λ (caps, pacing, audit frequency, weights) proportional to measured violations and uncertainty. Provide proofs of invariance on fast layer and convergence on slow layer under bounded noise.

Consequence: readiness constructs a stabilizing meta‑attractor in rule space. Without it, scaling increases variance and deepens lock‑in—amplifying proxy tyranny and capture.
