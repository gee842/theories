# Diagnostics & Indices (Practitioner Layer)

Purpose: Provide measurable signals to detect meta‑attractor drift and to gate scaling.

Core indices
- Proxy–Welfare Coupling (PWC): Correlation × local slope sign between domain welfare and its operational proxy. Negative ⇒ optimizing the proxy harms welfare.  
  Source: meta_attractor/meta-attractor-formal.md
- Proxy Dominance Index (PDI): Decision weight placed on the proxy, penalized when PWC ≤ 0. High PDI with low/negative PWC is the canonical failure mode.  
  Source: meta_attractor/meta-attractor-formal.md
- Slack Coefficient (SC): Resource slack × variability penalty × time‑scale safety; (0,1], higher is better.  
  Source: meta_attractor/meta-attractor-formal.md

Proposed extensions (to be validated during site build)
- Complexity Intolerance (CI): Share of key decisions taken with binary thresholds or single‑number gates where multi‑objective gates are warranted. High CI ⇒ nuance suppressed.  
  Source basis: complexity intolerance motif across essays.
- Diversity Exposure (DE): Entropy/diversity of inputs exposed by recommender/decision systems, adjusted for reach. Low DE correlates with polarization and capture risk.  
  Source basis: attention economy analysis.
- Externality Shadow (ES): Ratio of delayed/off‑balance‑sheet harms to recognized on‑dashboard benefits (sector‑specific). High ES ⇒ proxy racing with hidden costs.  
  Source basis: externality and time‑lag themes.
- Capture Risk (CR): Composite of lobbying intensity, revolving‑door hires, and standard‑setting control vs. market share. High CR ⇒ rule‑rewriting likely.  
  Source basis: capture dynamics across documents.

Usage patterns
- Gate scaling: Require SC ≥ threshold and PWC ≥ 0 for expansion; if PDI high and PWC ≤ 0, trigger tripwires and review.
- Reporting: Quarterly dashboards for each domain; pair numbers with qualitative audits to prevent name–reality drift (正名).
