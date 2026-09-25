# Evaluation: define and earn “surpass”

**Proposed on 2026-09-07.** No measurements exist yet. All numbers below are explicit starting targets for preregistration and feasibility review, not forecasts or externally established thresholds.

## The primary question

At a comparable standard of accepted behavior and continuity, does the full system deliver a fixed sequence of useful changes at lower total cost than the strongest tuned alternative? Does accumulated experience improve performance on later unseen work?

An accepted change is an independently specified requested outcome that passes behavioral, state, scope, and applicable performance checks and survives its observation window. Request boundaries are fixed before a run. Splitting one request into many commits cannot increase the count.

Measure agent/infrastructure cost per accepted request, accepted requests per elapsed hour, completion rate, escaped regressions, and human time separately. Include discovery, memory processing, architecture search, verification, integration, failed attempts, migrations, recovery and continuing maintenance. Normalize model/tool prices with a pinned rate table and report raw resource usage. Account for prototype-specific setup cost separately and report amortization assumptions.

The primary cost comparison uses the full request sequence and a fixed budget including a bounded repair allowance. To pass the efficiency gate, both contenders must deliver the same requested outcome set fixed before the run, with all repair costs charged. If either cannot complete that set within the allowance, report a cost/completion frontier and do not award the primary efficiency gate. The initial-completion tolerance below applies before those repairs; it does not permit skipping expensive requests to claim a cost win.

## Competitors that can win

| Baseline | Required strength |
|---|---|
| Strong single agent | Retrieval, compaction, persistent project memory, tests and capable tools. |
| Tuned agent team | Dynamic planning/delegation, integration workers, durable memory and good file ownership. |
| Fixed module stewardship | The same module/runtime/contract primitives as our system, with stable boundaries and capable maintainers. |
| Adaptive workflow/context baseline | A tuned approach capable of improving workflow or memory, informed by the ADAS/AFlow/ACE precedents in SOURCES.md. |
| Full proposed system | Adds adaptive live-software boundaries, conditional evidence, transition-aware learning and measured organization. |

Use identical initial code, models, tool access, runtime, authority rules, budgets and acceptance criteria for the matched comparison. Tune competitors on development workloads with comparable tuning resources. Report tuning/search cost. Do not prevent a baseline from acquiring an obvious engineering improvement merely because our system uses it.

Predeclare a primary tuned baseline using development results. For the competitive cost gate, also compare against the lowest-cost baseline that delivers the same outcome set and meets the quality requirements. Report every qualifying baseline and the cost/quality frontier; an expensive competitor must not be selected merely because its completion score is high. Initial completion is compared with the best baseline completion score.

Also run a separate practical comparison against a then-current established harness in its preferred environment. Do not pool native-environment results with the matched-substrate experiment or attribute every difference to our architecture.

Ablate adaptive boundaries, curated learning, targeted evidence reuse, and adoption assistance separately. Keep the underlying correctness and authority requirements in every variant. If an ablation wins, simplify the full system.

## Workloads and independence

Develop on three differently structured communities. Reserve at least two evaluation communities with unseen request families, semantic surprises, and migration histories. Begin with twenty-change development traces, progress to 200-change comparisons, and then histories up to 1,000 changes.

The public illustrative sequence in experiments/01-community-evolution.md is a development fixture. It cannot be reused as a sealed demonstration of generalization.

Independent authors freeze intended outcomes, historical-state obligations and reference records before runs. Agents may receive normal visible acceptance requirements while final adjudication includes unseen cases. The optimizing system cannot edit sealed adjudication, cost accounting or reference history. Ambiguous domain outcomes require recorded adjudication rather than silent scoring changes.

Use paired initial states and workloads with at least five independent runs per evaluation community, expanding replication based on observed variance. Report confidence intervals at the run/community level, not as if successive changes were independent samples. For an efficiency gate, require the point estimate to reach its stated target and the paired 95% confidence interval to exclude no improvement. This supports an improvement with a target-sized estimate; claiming a demonstrated minimum reduction of 25% would additionally require the confidence bound to exceed 25%. Avoid declaring a general win from two community types alone. Broaden domains before broad claims.

Observe accepted changes for ten subsequent requests or an equivalent fixed operational replay at the end of a sequence. Count regressions discovered during that window and track later discoveries separately. Record human intervention and failed/abandoned branches. Evaluate completion with a fixed timeout and count unfinished outcomes.

An escaped-regression rate is the fraction of accepted requests with at least one attributable regression found during that observation window. For the provisional quality gate, require no observed increase and a one-sided 95% upper bound on the noncritical rate difference of at most one percentage point. Any known critical state violation blocks promotion. Human time must show no observed increase; report uncertainty and use a provisional 10% relative noninferiority margin for its upper bound. These finite-data margins do not establish identical risks or human cost. Insufficient precision leaves the relevant claim unresolved.

## Provisional advancement gates

| Claim | Target | Interpretation |
|---|---|---|
| Mechanism works | All specified state invariants hold in the twenty-change development fixture; all deliberately planted nonlocal semantic changes are detected before activation. | A small finite correctness gate, not proof of general correctness. |
| First competitive advantage | At least 25% lower total agent/infrastructure cost per accepted change after delivering the same outcome set; initial completion no more than 2 percentage points below the best baseline; no observed increase in escaped-regression rate or human time, subject to the uncertainty rules above. | Main gate over 200-change evaluations against the lowest-cost qualifying baseline. All known critical state violations block promotion. |
| Strong superiority | At least 2× accepted evolution per unit agent/infrastructure cost with the same quality and human-effort gates. | Longer-range ambition; the first 25% result is an intermediate milestone. |
| Learning pays for itself | At least 20% lower total agent/infrastructure cost on difficulty-matched unseen work than the same system with learning disabled, including learning/search cost. | Evaluate after accumulated history with the same outcome and quality gates; report human time separately. |
| Local work resists unrelated growth | Median local-change cost rises no more than 25% over matched early/late windows or catalog-growth pairs. | Fix active obligations and workload difficulty; publish tail costs, contract sizes and ancestor work. |
| Useful large concurrency | At least 3× accepted-change throughput at 1,000 versus 100 active workers, with no more than 50% higher cost per accepted change and the same quality gates. | A stretch gate on preregistered workloads with sufficient independent ready work. Report useful saturation on coupled workloads. |
| Runtime isolation | Warm forum p95 latency rises no more than 10% as dormant catalog grows from 100 to 10,000 modules at fixed active load and hardware. | One installed-catalog result; separately report cold load, generation latency, storage/index costs and background activity. |

These thresholds may be revised after a development pilot, with reasons recorded **before** sealed evaluations. Do not revise a failed threshold retrospectively and retain the original claim.

## Five independent axes of scale

| Axis | Proposed range |
|---|---|
| Installed definitions and dormant instances | 10 → 100 → 1,000 → 10,000 |
| Active workers | 1 → 8 → 32 → 100 → 250 → 1,000 |
| Successive accepted and attempted changes | 20 → 200 → 1,000 |
| Semantic dependency structure | Sparse → clustered → densely coupled, at matched catalog size |
| Concurrent audiences and maintained versions | 1 → 10 → 100 |

An active worker is executing a substantive implementation, verification, integration or transition assignment. Idle maintainers, critic labels and duplicate make-work do not count. Report actual concurrency distributions, productive worker-hours, queue delay and accepted throughput.

Large-concurrency experiments increase total available resources; they test throughput and cost efficiency rather than constant-cost acceleration. Keep per-worker hardware/model assumptions explicit. Under insufficient independent work, effective throttling is the desired behavior. Separate a thousand workers across many communities from a thousand on one application.

## Diagnostic measurements

Predict the affected set before implementation. Record false negatives, unnecessary propagation and later frontier expansion. Measure state/effect accesses that violate declared boundaries. Include total and tail context for workers, ancestors, discovery and reconciliation.

Track contract size, unresolved assumptions, evidence-cache invalidations, broader-check discoveries, architecture churn, active adapters, retired obligations, and the payback time of a restructuring. An unchanged signature does not count as unchanged meaning.

For product outcomes, measure member task completion, explanation and correction time, adoption, abandonment and maintenance ownership. A synthetic agent impersonating a community member cannot establish cultural fit or member satisfaction.

## What would falsify the central thesis

Adaptive organization may cost more than it saves. Summaries may grow toward the whole application. Verification reuse may suppress necessary rechecking. Learning may memorize development fixtures. Flexible forks may accumulate obligations faster than they create value. A tuned conventional team may equal or beat the full system.

Report these as results. The credible superiority claim is always tied to a workload, comparison, resource budget and observation period.
