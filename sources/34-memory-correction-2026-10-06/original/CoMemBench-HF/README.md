---
language:
  - en
license: cc-by-4.0
task_categories:
  - other
tags:
  - multi-agent
  - benchmark
  - collaborative-memory
  - workflow-topology
  - tool-use
  - repository-code-change
  - information-retrieval
  - mathematical-reasoning
  - memory-pollution
size_categories:
  - 1K<n<10K
pretty_name: CoMemBench
---

# CoMemBench: Benchmarking Collaborative Memory Boundaries across Multi-Agent Workflow Topologies

**CoMemBench** is a benchmark for **collaborative memory** in multi-agent systems. Each problem is a real multi-agent workflow — a directed graph of specialized worker nodes with typed handoffs — and the benchmark asks whether a system can run that workflow while **using only the memory it should use**: no stale artifacts, no cross-wired branches, no foreign completions.

The stress is a matched **pollution** variant. For every problem there is a twin that differs in exactly one architecture-visible way: one additional routing candidate is offered to the workflow, and that candidate is invalid. A system that reads memory indiscriminately will take the bait and fail; a system with correct memory boundaries will reject it and finish.

> This repository is the anonymised artifact accompanying a manuscript under double-blind review. All author and affiliation information has been removed; it will be published under the authors' names upon acceptance.

## At a glance

| | |
|---|---|
| Complete problems | **800** (4 domains × 200) |
| Matched polluted instances | **800** (one per problem) |
| Total instances | **1600** (800 control + 800 polluted) |
| Workflow nodes per problem | 6–19 (median 11) |
| Node-level memory contexts | 8975 |
| Held-out split | **none** — all 800 are complete problems |
| Version | **v1** |

## Domains

| Domain | Count | Node style |
|---|---|---|
| `stateful_tool_use` | 200 | Stateful tool chains — terminal, documents, spreadsheets, forms |
| `repository_code_change` | 200 | Multi-node code-change workflows over real repositories |
| `offline_information_retrieval` | 200 | Multi-hop retrieval pipelines over fixed corpora |
| `mathematical_and_structured_reasoning` | 200 | Proof-dependent and structured-reasoning workflows |

## What a problem looks like

A workflow family is a layered DAG of worker nodes. Each node carries:

- a **role** and a **task** (what this worker must produce),
- a **local context** (the memory scope this worker is allowed to read),
- an **output contract** (artifact semantic + runtime contract),
- **task edges** describing the handoffs (artifact reuse, verification, dependency evidence).

Plus a **topology motif set** (`chain`, `split_join`, `reuse`, `overlap`, `bounded_revision_loop` — most families are composite) and a **revision contract** that bounds how many times the workflow may revisit work.

The agent's job is to execute the workflow: produce artifacts, hand them off along required edges, and satisfy the domain's native evaluator.

## Files

```
data/
  workflow_families.jsonl       800    the problems (goals, nodes, edges, topology, revision contract)
  node_contexts.jsonl          8975    per-node memory scope (environment ref, resource policy, task scope)
  topology_descriptors.jsonl    800    per-family topology statistics (depth, width, fan-out, joins, reuse, overlap)
  math_cases.jsonl              200    Lean dependency cases for the math domain (statements + proof-term DAG)
  retrieval_corpora.jsonl       200    frozen offline corpora for the retrieval domain (one per family)
  control_instances.jsonl       800    control-side instance index
  polluted_instances.jsonl      800    polluted-side instance index (pairs to control via pair_id)
  benchmark_instances.jsonl    1600    both sides merged
schemas/
  workflow_family.schema.json      node_context.schema.json
  benchmark_instance.schema.json   artifact.schema.json
  node_view.schema.json            case_init.schema.json
  memory_proposal.schema.json      handoff_oracle.schema.json
  swe_image_manifest.json          the 50 certified code-domain images (name + sha256 + size)
```

All files are JSON Lines (one JSON object per line), UTF-8.

### `data/workflow_families.jsonl`

One record per complete problem.

| Field | Type | Meaning |
|---|---|---|
| `family_id` | str | Stable problem id (e.g. `v15_family_0001_b9f32b72e8fd`) |
| `scenario_id` | str | Scenario id shared with node contexts |
| `domain` | str | One of the four domains above |
| `global_goal` | str | The overall objective handed to the system |
| `nodes` | list | Worker nodes: `node_id`, `agent_role`, `task`, `node_kind`, `local_context_ref`, `output_schema`, `output_semantic`, `runtime_contract`, `source_ref`, `source_unit_id` |
| `task_edges` | list | Handoffs: `edge_id`, `from`, `to`, `relation_type`, `handoff_policy`, `handoff_required`, `artifact_semantic`, `dependency_evidence` |
| `source_topology` / `execution_topology` | dict | `motifs`, `primary`, `signature` |
| `revision_contract` | dict | Which edges may be revisited and how many traversals are allowed |
| `execution` | dict | Evaluator mode, revision limit, closed-loop flag |
| `verification_overlay` | dict | Nodes/edges that carry verification duties |
| `construction` | dict | Provenance of how the family was assembled |
| `source_refs` | list | Upstream source records |

### `data/node_contexts.jsonl`

One record per workflow node (`node_id` ↔ `context_ref`). The `local_context` field is the memory scope that node is permitted to read: `environment_ref`, `resource_policy`, `task_specific_scope`, `source_ref`.

### `data/topology_descriptors.jsonl`

One record per family. Structural statistics used for topology-sliced reporting: `node_count`, `edge_count`, `depth`, `max_width`, `fan_out_count`, `join_count`, `reuse_count`, `overlap_count`, `revision_count`, `handoff_count`, `handoff_density`.

### `data/math_cases.jsonl`

One record per math-domain family. Nodes are Lean declaration **statements** (what must be proven) with source location and statement fingerprints; `edges` are the elaborated proof-term constant dependencies; `source` pins the project and toolchain. Proof bodies are **not** included — those are the answers.

### `data/retrieval_corpora.jsonl`

One record per retrieval-domain family: `corpus_ref`, `source_ref`, and a `documents` list (`docid`, `text`) forming that family's frozen offline corpus. Retrieval problems are answerable only against this corpus.

### Instance index files

Thin id-linking tables. `control_instances.jsonl` and `polluted_instances.jsonl` share `pair_id`; `polluted_instances.jsonl` additionally carries `control_instance_id` and a `pollution_plan_ref` (an opaque identifier — the plan itself is not part of this release).

## Execution environments

CoMemBench runs across four domains with different execution boundaries. Two are self-contained in this repository; two need container images.

| Domain | Boundary | Ships here | Needs |
|---|---|---|---|
| `mathematical_and_structured_reasoning` | Host-side frozen Lean declarations | `math_cases.jsonl` | `leanprover/lean4:v4.7.0` + the pinned HepLean project |
| `offline_information_retrieval` | Host-side frozen offline corpus | `retrieval_corpora.jsonl` | nothing else |
| `repository_code_change` | One container per case | problem definitions | the 50 certified images (registry link withheld during review — see below) |
| `stateful_tool_use` | Postgres + private network + MCP processes per task | problem definitions | `postgres:15` (public, Docker Hub) + the Toolathlon-Gym runtime and MCP server set |

### Code-domain images (50, 333 GB)

The code-change images are the SWE-Verified execution environments (~6–7 GB each), distributed as container images rather than inside this dataset repository — the same split SWE-bench uses. All 50 are published as **one** container package with **50 tags**; the tag is the certified image name with the namespace stripped and punctuation normalised (e.g. `logicstar/sweb.eval.x86_64.django_1776_django-10097:latest` → `django-1776-django-10097`).

The public registry location is **withheld during double-blind review** (the URL identifies the authors); it will be listed here upon release. `schemas/swe_image_manifest.json` pins the exact set: for each image the certified name, its `sha256` id, `execution_fingerprint`, logical size, and slug. When the registry location is public, verify a pulled image against the manifest with `docker image inspect --format '{{.Id}}'`.

These are the certified builds themselves, not a rebuild and not the public `swebench/*` images — the execution fingerprints of public `swebench/*` images do not match this set.

### Stateful-tool domain

`postgres:15` is a public Docker Hub image (`docker pull postgres:15`). The Toolathlon-Gym runtime and the MCP server set are the reproducible default for the tool domain (native live-API Toolathlon is optional and may incur cost).

## Metrics

Two standard measures and two memory-specific measures. Infrastructure failures are reported separately and never counted as wrong answers.

| Metric | Definition |
|---|---|
| **SR** | Task Success Rate — end-to-end workflow success. Reported as completed / registered. |
| **VNCR** | Verified Native Completion Rate — macro-mean of `native_passed` over nodes: whether each node completed its *own* declared obligation under domain-native checks. |
| **VHS** | Verified Handoff Success — micro-ratio of verified eligible handoffs, i.e. downstream success conditioned on successful mandatory predecessors. Proxy for required-memory availability. |
| **ICS** | **Isolation Challenge Score** — success on polluted instances conditioned on matched control success. |

**ICS** is the memory-boundary metric. It is a *conditional* rate: a polluted instance only counts toward the denominator when its matched control was solved. If the denominator is below 10, ICS is reported **blank** (`—`), never as 0.

**Cost** is reported as Tokens / Task (input + output, median and P90), covering agent + coordination + memory + recovery traffic.

## What is intentionally not included

This repository is the **task side** of the benchmark — everything a system needs to see in order to run. The following are held out for scoring and are **not** here:

- evaluation oracles (gold answers, gold patches, gold proofs, native evaluator inputs),
- gold execution trajectories,
- pollution plans (the mutation operator, target node, and expected isolation action for each polluted instance).

Container images are also outside this repository — see **Execution environments** above.

Systems can be executed and evaluated against the released workflows; final scores come from the held-out evaluation.

## Loading

Plain JSON is enough:

```python
import json

def load(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]

families  = load("data/workflow_families.jsonl")
contexts  = load("data/node_contexts.jsonl")
topology  = load("data/topology_descriptors.jsonl")
math      = load("data/math_cases.jsonl")
corpora   = load("data/retrieval_corpora.jsonl")
```

With HuggingFace `datasets`, point `data_files` at the repository's local files (or the paths served by your copy of this repository):

```python
from datasets import load_dataset

ds = load_dataset(
    "json",
    data_files={
        "families": "data/workflow_families.jsonl",
        "node_contexts": "data/node_contexts.jsonl",
        "topology_descriptors": "data/topology_descriptors.jsonl",
        "math_cases": "data/math_cases.jsonl",
        "retrieval_corpora": "data/retrieval_corpora.jsonl",
        "control_instances": "data/control_instances.jsonl",
        "polluted_instances": "data/polluted_instances.jsonl",
        "benchmark_instances": "data/benchmark_instances.jsonl",
    },
)
```

## Versioning

This is **v1** of the public release. The 800 problems are complete and there is no held-out test/dev subdivision.

## License

The annotations, workflow structures, and memory-context scopes in this repository are released under **CC BY 4.0**.

Problems are constructed from upstream sources; those upstream assets remain under their own terms:

| Domain | Upstream |
|---|---|
| `stateful_tool_use` | Toolathlon |
| `repository_code_change` | SWE-bench Verified |
| `offline_information_retrieval` | BrowseComp+ |
| `mathematical_and_structured_reasoning` | Lean4 proof-dependent workflows |

Please cite both CoMemBench and the upstream sources if you use the corresponding domains.

## Citation

```bibtex
@misc{comembench2026,
  title        = {{CoMemBench}: Benchmarking Collaborative Memory
                  Boundaries across Multi-Agent Workflow Topologies},
  author       = {Anonymous},
  year         = {2026},
  note         = {Manuscript under review}
}
```
