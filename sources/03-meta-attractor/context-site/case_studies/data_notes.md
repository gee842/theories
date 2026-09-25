# Data Notes for Case Studies (Attention, Growth–Finance)

Common variables
- Time window: quarterly observations over ≥ 3 years to capture dynamics.
- Units: platform-product-region (Attention); firm-sector-country (Finance).
- Controls: seasonality, policy shocks, major product changes.

Attention economy
- Engagement (f): minutes/session, CTR, sessions/user/day.
- Welfare (W): survey wellbeing indices; content quality flags; exposure diversity (Shannon entropy across sources/topics); misinformation prevalence.
- Decision weights: inferred from OKRs/roadmaps/comp plans (text mining proxies); A/B rollout cadence as optimization intensity.
- Slack inputs: moderation staffing, review latency, rate-limit policies, circuit breakers.
- Sources: platform transparency reports, academic datasets, public policy changes (e.g., EU DSA), third‑party audits.

Growth–Finance
- Proxy (f): EPS, revenue growth, valuation multiples, AUM.
- Welfare (W): TFP growth, resilience indicators (cash buffers, supplier diversity), innovation diversity (HHI over patents/products), externalities (carbon intensity).
- Capture signals (CR): lobbying spend, revolving‑door hires, standards committees participation vs. market share.
- Slack inputs: reserves, leverage ratios, decision latency (board cadence) vs. optimization cadence (earnings cycles).
- Sources: Compustat/CRSP (or analogues), company filings, OpenSecrets/Transparency registers, patent databases, sector HHI from market reports.

Computation
- PWC: rolling correlation + local slope from nonparametric regression within intensity bands.
- PDI: weight of proxy in decisions from comp plans/OKRs (text vectors) and budget shares.
- SC: calculate from operational capacity, load variability, and decision/optimization timing.
