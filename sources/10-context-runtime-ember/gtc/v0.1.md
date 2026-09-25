# GTC — Generative Topological Context

> **A persistent, evolving, multi-topological context architecture for agents and cognitive systems**  
> Version: v0.1  
> Status: Conceptual specification + implementation plan

---

## Abstract

Most current LLM systems treat context as a temporary linear sequence:

```text
system prompt
+ recent conversation
+ summaries
+ retrieved memories
+ documents
+ tool outputs
+ current request
```

This representation is convenient for a Transformer, but it is a poor representation of an evolving world, an evolving project, or an evolving self. The underlying reality is not linear; it contains entities, events, concepts, causal structures, temporal processes, goals, uncertainty, contradictions, histories, and multiple simultaneous ways of organizing the same information.

**Generative Topological Context (GTC)** starts from a different premise:

> **Context is not fundamentally a token sequence. Context is a persistent, evolving structured state.**

The token context sent to an LLM at any moment is only a local projection of that state.

A GTC maintains multiple topologies simultaneously — entity graphs, concept graphs, event graphs, causal graphs, temporal graphs, goal/affordance graphs, epistemic graphs, social graphs, spatial graphs, and others — together with the mappings between them. It also records how those structures and mappings change over time.

The resulting system is not one giant knowledge graph. It is an evolving **topology atlas**: a family of mutually connected representations of the same changing world.

The core loop is:

\[
\mathcal W_t
\xrightarrow{\text{projection / compilation}}
C_t
\xrightarrow{\text{cognition}}
Y_t
\xrightarrow{\text{interpret / validate}}
\Delta_t
\xrightarrow{\text{commit}}
\mathcal W_{t+1}
\]

where:

- \(\mathcal W_t\) is the complete persistent GTC state at time \(t\);
- \(C_t\) is the compact active context projected for the current situation;
- \(Y_t\) is the model's thought, response, plan, tool call, or hypothesis;
- \(\Delta_t\) is a typed structural transformation;
- \(\mathcal W_{t+1}\) is the next state of the context.

In this paradigm:

- **memory** is persistence of structure;
- **recall** is reactivation of relevant structure;
- **working memory** is the currently active subgraph/substructure;
- **learning** is structural change;
- **understanding** is topology formation or topology reorganization;
- **compaction** is abstraction and structure formation, not merely prose summarization;
- **reasoning** is transformation over an active projection of the persistent world model;
- **identity** is a persistent self-related substructure inside the same evolving context;
- **context engineering** becomes the engineering of state, projection, and transformation.

This document specifies the conceptual system and a concrete implementation path.

---

# 1. Core thesis

The central claim of GTC is:

\[
\boxed{\text{Persistent Context} \neq \text{Prompt History}}
\]

Instead:

\[
\boxed{\text{Persistent Context} = \text{Evolving Structured State}}
\]

and:

\[
\boxed{
\text{LLM Token Context}_t
=
\operatorname{Compile}(\mathcal W_t, s_t, B_t)
}
\]

where \(s_t\) is the current situation and \(B_t\) is the available context budget.

The LLM is therefore not the durable memory of the agent. It is a cognitive operator acting on a durable externalized state.

A useful mental model is:

```text
                     ┌──────────────────────────┐
                     │       Persistent GTC      │
                     │                          │
Environment ────────▶│  world / self / history  │
                     │  beliefs / goals / views  │
                     │                          │
                     └────────────┬─────────────┘
                                  │
                                  │ project / compile
                                  ▼
                     ┌──────────────────────────┐
                     │      Active Context       │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                              ┌───────┐
                              │  LLM  │
                              └───┬───┘
                                  │
                         thought / action / patch
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │ validate + transform GTC │
                     └──────────────────────────┘
```

The persistent thing is the GTC. The LLM is the transformation engine.

---

# 2. Why “Topological”

Different forms of knowledge naturally produce different graph structures.

A taxonomy tends toward a tree or DAG. A social world tends toward clustered networks. Events naturally form event-participant structures or hypergraphs. Causal knowledge tends toward directed process graphs. Temporal knowledge is a sequence of state transitions. Goals and actions form dependency and affordance structures.

No single topology is privileged enough to represent all of these faithfully.

Therefore GTC does **not** seek one universal graph schema. It maintains a family of representations:

\[
\mathcal G_t = \{G_t^1,G_t^2,\ldots,G_t^n\}
\]

Examples include:

- entity topology;
- concept / ontology topology;
- event topology;
- temporal topology;
- causal topology;
- epistemic topology;
- goal / task topology;
- affordance topology;
- spatial topology;
- social topology;
- procedural topology;
- self topology;
- project topology;
- discourse / argument topology.

The system additionally maintains mappings:

\[
\Phi_t = \{\phi_{ij}:G_t^i \rightarrow G_t^j\}
\]

These mappings are themselves knowledge.

For example:

```text
[JoiningEvent #42]
       │ creates
       ▼
Alice ─worksAt─▶ OpenAI
       │
       │ instantiates
       ▼
   Employment
```

The event graph, entity graph, and concept graph remain distinct, but the system knows how they correspond.

This family of graphs plus their mappings is the **topology atlas**.

---

# 3. Why “Generative”

A normal knowledge graph is usually treated as a database that grows by adding facts.

A GTC must be able to modify its own representational structure.

It can:

- create a node;
- create a relation;
- end a relation's validity;
- create an event;
- merge two identities;
- split one identity into multiple identities;
- create a new concept;
- create a new relation type;
- create a new topology;
- discover a mapping between topologies;
- weaken or invalidate a mapping;
- abstract repeated episodes into a reusable pattern;
- replace a causal hypothesis;
- reorganize a concept hierarchy;
- promote a hypothesis into a stable belief;
- demote a belief into a disputed claim;
- turn a recurring local pattern into a new materialized view;
- deprecate a topology that no longer explains the world usefully.

Thus learning is not merely:

```text
ADD FACT
```

but may be:

```text
REWRITE REPRESENTATION
```

Formally:

\[
\boxed{
\text{Learning} = \Delta \text{structure}
}
\]

and, in a stronger sense:

\[
\boxed{
\text{Understanding} =
\text{finding a structure that makes previously separate observations cohere}
}
\]

---

# 4. The minimal conceptual model

A GTC state at time \(t\) can be represented as:

\[
\boxed{
\mathcal W_t =
(\Omega_t,\mathcal G_t,\Phi_t,\mathcal E_t,\mathcal H_t,\mathcal A_t)
}
\]

where:

- \(\Omega_t\): addressable resources and assertions;
- \(\mathcal G_t\): family of topological views;
- \(\Phi_t\): mappings between views;
- \(\mathcal E_t\): epistemic state: confidence, evidence, provenance, scope, disagreement;
- \(\mathcal H_t\): transformation history;
- \(\mathcal A_t\): activation field: what is currently cognitively salient.

The most important design decision is that **everything semantically important is addressable**.

A relation can point not only to an entity, but also to:

- another relation;
- a claim;
- an event;
- a topology;
- a mapping;
- a transformation;
- a piece of evidence;
- a previous state.

This allows higher-order knowledge such as:

```text
Claim A ─contradicts─▶ Claim B
Event E ─creates─────▶ Relation R
Evidence X ─supports─▶ CausalHypothesis H
Topology T1 ─projectsTo─▶ Topology T2
Transformation Δ7 ─supersedes─▶ Transformation Δ2
```

The substrate is therefore better understood as a **typed hyper-relational resource system** than as a simple property graph.

---

# 5. Fundamental primitives

GTC should keep the number of true primitives small.

## 5.1 Resource

A `Resource` is anything that can be referred to.

Examples:

```text
gtc://object/alice
gtc://statement/8fa2
gtc://event/join-openai-2026
gtc://view/causal-project-x
gtc://mapping/12ab
gtc://transform/9931
gtc://evidence/email-2026-08-08
```

At the implementation layer, resource kinds may differ, but all use a common reference protocol.

## 5.2 Object

An `Object` is a persistent identifiable thing:

- person;
- place;
- organization;
- concept;
- project;
- artifact;
- document;
- tool;
- goal;
- plan;
- event;
- agent;
- question;
- hypothesis;
- topology itself.

Objects need not correspond to physical entities.

## 5.3 Statement

A `Statement` is a typed n-ary relation with named roles.

Example:

```yaml
predicate: payment
arguments:
  payer: alice
  recipient: bob
  amount: 100
  currency: USD
  location: bangkok
  time: 2026-08-08T15:00:00+07:00
```

A binary graph edge is simply the special case where a statement has two arguments.

Statements are addressable resources, so other statements can refer to them.

## 5.4 Claim

A `Claim` is a statement wrapped in an epistemic envelope.

A claim contains:

- statement;
- source / provenance;
- asserted by;
- confidence;
- epistemic status;
- world-time validity;
- knowledge-time validity;
- scope;
- evidence;
- derivation;
- competing claims.

This avoids confusing “represented in the context” with “believed to be true.”

## 5.5 Event

An `Event` is an object representing a bounded occurrence or transition.

Events can have:

- participants;
- roles;
- time interval;
- place;
- preconditions;
- consequences;
- created relations;
- terminated relations;
- evidence;
- parent/child events.

Events are especially important because they connect static knowledge to change.

## 5.6 Transformation

A `Transformation` is a first-class record of change to the GTC itself.

Examples:

- `CREATE_RESOURCE`;
- `ASSERT_CLAIM`;
- `END_VALIDITY`;
- `MERGE_RESOURCES`;
- `SPLIT_RESOURCE`;
- `CREATE_MAPPING`;
- `RETRACT_MAPPING`;
- `CREATE_VIEW`;
- `RETYPE_RESOURCE`;
- `ABSTRACT_PATTERN`;
- `PROMOTE_HYPOTHESIS`;
- `DEPRECATE_VIEW`.

A transformation records:

```yaml
id: transform:9931
actor: agent:main
time: ...
inputs: [...]
outputs: [...]
operation: ABSTRACT_PATTERN
reason: ...
provenance: [...]
confidence: 0.82
```

This makes the context replayable and auditable.

## 5.7 View / Topology

A `View` is a purpose-specific structural projection over GTC resources.

Examples:

```text
entity view
concept view
event view
causal view
goal dependency view
temporal view
```

A view has:

- purpose;
- node selection rule;
- relation selection rule;
- optional derived relations;
- optional constraints;
- materialization policy;
- mappings to other views;
- lifecycle status.

A view is not necessarily manually defined. It can be discovered and promoted by the system.

## 5.8 Mapping

A `Mapping` is a correspondence between structures in different views.

Examples:

```text
Event E ─creates─▶ Relation R
Relation R ─instanceOf─▶ Concept C
Observation O ─supports─▶ Hypothesis H
Goal G ─motivates─▶ Action A
Procedure P ─realizes─▶ Goal G
```

Mappings may be:

- exact;
- approximate;
- probabilistic;
- partial;
- one-to-many;
- many-to-one;
- disputed;
- temporal.

Mappings themselves have provenance and confidence.

## 5.9 Scope

A statement may be valid only in a certain context.

Examples:

- during a time interval;
- from one person's perspective;
- inside a project;
- under a hypothetical scenario;
- according to one source;
- inside one ontology.

GTC must never force locally valid statements into one global truth prematurely.

## 5.10 Activation

Activation represents present cognitive relevance.

It is not truth, not importance in general, and not recency alone.

A resource can remain persistent while having almost zero activation.

This supports the distinction:

\[
\boxed{
\text{Memory persistence} \neq \text{Current attention}
}
\]

---

# 6. The topology family

A complete GTC does not require every possible topology from day one, but the conceptual model should support them.

## 6.1 Entity topology

Answers:

> What exists, and how are identifiable things related?

Typical relations:

- `works_at`;
- `owns`;
- `located_in`;
- `member_of`;
- `uses`;
- `authored`;
- `depends_on`.

Topology tends toward clustered, hub-heavy relational networks.

## 6.2 Concept / ontology topology

Answers:

> What kinds of things are these, and how do concepts relate?

Typical relations:

- `instance_of`;
- `subclass_of`;
- `part_of`;
- `contrasts_with`;
- `specializes`;
- `generalizes`.

Topology tends toward DAGs with multiple inheritance.

## 6.3 Event topology

Answers:

> What happened?

Structure:

```text
Entity ─participant→ Event ←participant─ Entity
                       │
                     time/place
                       │
                 effects / outcomes
```

This often resembles a hypergraph represented via event nodes.

## 6.4 Temporal topology

Answers:

> In what order did states and events occur, and what changed?

It includes:

- before / after;
- starts / ends;
- overlaps;
- supersedes;
- state transitions;
- validity intervals.

Temporal topology should be bitemporal:

1. **valid time** — when something was true in the modeled world;
2. **transaction/knowledge time** — when the GTC learned or recorded it.

This distinction is essential for correcting past beliefs without rewriting history.

## 6.5 Causal topology

Answers:

> What generates, enables, prevents, or changes what?

Relations include:

- `causes`;
- `contributes_to`;
- `enables`;
- `prevents`;
- `mediates`;
- `increases_risk_of`;
- `explains`.

Causal edges must carry stronger epistemic discipline than ordinary semantic edges.

Correlation must not silently become causation.

## 6.6 Epistemic topology

Answers:

> What is known, believed, hypothesized, disputed, supported, or refuted?

Nodes include:

- claims;
- evidence;
- sources;
- hypotheses;
- arguments;
- observations.

Relations include:

- `supports`;
- `contradicts`;
- `derived_from`;
- `asserted_by`;
- `supersedes`;
- `uncertain_about`.

This is one of the most important differences between GTC and ordinary KG systems.

## 6.7 Goal / task topology

Answers:

> What is the agent trying to make true?

Relations include:

- `goal_of`;
- `subgoal_of`;
- `blocked_by`;
- `depends_on`;
- `satisfied_by`;
- `conflicts_with`;
- `priority_over`.

A goal is not just another fact. It defines future-oriented relevance.

## 6.8 Affordance / action topology

Answers:

> Given the current state, what can be done next?

Nodes include:

- actions;
- tools;
- resources;
- opportunities;
- constraints;
- possible states.

Relations include:

- `available_if`;
- `requires`;
- `produces`;
- `risks`;
- `opens`;
- `closes`.

This topology lets context selection depend on possibility, not merely similarity to past text.

## 6.9 Procedural topology

Answers:

> How is something done?

It contains:

- procedures;
- steps;
- preconditions;
- invariants;
- recovery paths;
- tool requirements;
- reusable patterns.

Procedural memory can therefore live in the same overall context system as declarative knowledge.

## 6.10 Spatial topology

Answers:

> Where are things relative to one another?

Relations include:

- contains;
- near;
- inside;
- connected_to;
- reachable_from;
- above/below;
- route_to.

## 6.11 Social / actor topology

Answers:

> Who are the relevant actors, roles, communities, permissions, trust relationships, and commitments?

This is useful for multi-user systems, organizations, communication, collaboration, and permission-aware agents.

## 6.12 Self topology

Answers:

> What is this agent, what does it know about itself, and what persists across iterations?

It may include:

- identity;
- capabilities;
- tools;
- responsibilities;
- commitments;
- active projects;
- preferences/policies;
- current goals;
- previous decisions;
- unresolved questions;
- learned procedures;
- model limitations;
- internal hypotheses.

The self topology should not be a privileged magical object. It is part of the same context fabric, but has special access-control and update rules.

---

# 7. A topology is a view, not reality itself

A foundational invariant of GTC is:

> **No topology is the world. Every topology is a representation of some aspect of the world.**

For example, the same occurrence may appear as:

```text
Entity topology:
Alice ─worksAt→ OpenAI

Event topology:
Alice ─participant→ [JoinEvent] ←organization─ OpenAI

Concept topology:
[JoinEvent] ─instanceOf→ EmploymentTransition

Temporal topology:
OldEmployment ─endsBefore→ JoinEvent ─starts→ NewEmployment

Causal topology:
HiringNeed ─contributesTo→ JoinEvent

Goal topology:
JoinEvent ─satisfies→ CareerGoal
```

Flattening these into one undifferentiated graph destroys distinctions that matter.

GTC therefore stores both:

1. the individual views;
2. the mappings between the views.

The global object is not a graph but an **atlas of connected topologies**.

---

# 8. Higher-order relations

Ordinary KGs usually privilege node-to-node edges. GTC must support relations about relations.

Example:

```text
R1 = Alice ─worksAt→ OpenAI
R2 = Alice ─livesIn→ San Francisco

R1 ─explains→ R2
```

Or:

```text
Event E ─creates→ Relation R1
Evidence X ─supports→ R1
Claim C ─contradicts→ R1
Mapping M ─projects→ R1
```

This requirement strongly suggests that relations/statements themselves need stable IDs.

A practical implementation rule is:

> **Every assertion is a first-class resource.**

That single rule eliminates many modeling dead ends.

---

# 9. Time and history

GTC should never model change by destructively overwriting the past.

Suppose:

```text
Alice ─worksAt→ Google
```

later becomes:

```text
Alice ─worksAt→ OpenAI
```

The system should record:

```text
[Employment@Google]
valid: 2021-01 → 2026-05

[LeaveGoogleEvent]
terminates: Employment@Google

[JoinOpenAIEvent]
creates: Employment@OpenAI

[Employment@OpenAI]
valid: 2026-06 → ?
```

The world model therefore evolves as:

\[
\mathcal W_0
\xrightarrow{\Delta_0}
\mathcal W_1
\xrightarrow{\Delta_1}
\mathcal W_2
\xrightarrow{\Delta_2}
\cdots
\]

Each \(\Delta_i\) is stored.

This gives:

- auditability;
- replay;
- historical reasoning;
- belief revision without memory corruption;
- branching;
- counterfactual reconstruction;
- ability to answer “what did we believe at time t?” separately from “what do we now think was true at time t?”.

---

# 10. Epistemics: truth must not be flattened

A context system becomes dangerous and brittle if every stored statement is treated as equally true.

Each claim should carry an epistemic state, for example:

```text
observed
reported
inferred
hypothesized
assumed
accepted
contested
refuted
superseded
unknown
```

Confidence should be separate from status.

For example:

```yaml
status: inferred
confidence: 0.73
```

is different from:

```yaml
status: observed
confidence: 0.73
```

The former expresses uncertain inference; the latter may express noisy observation.

## 10.1 Provenance

Every meaningful derived claim should be traceable to:

- source documents;
- user statements;
- tool outputs;
- observations;
- prior claims;
- inference transformations;
- responsible agent/model.

## 10.2 Contradictions

Contradictory claims should normally coexist.

Example:

```text
Source A ─asserts→ Claim X
Source B ─asserts→ Claim ¬X

Claim X ─contradicts→ Claim ¬X
```

The system should not immediately choose one and delete the other.

Resolution can occur later through:

- stronger evidence;
- scope refinement;
- temporal disambiguation;
- identity disambiguation;
- source reliability;
- explicit user decision;
- model inference.

Contradiction is itself information.

---

# 11. Context as activation over the topology atlas

Persistent context may contain millions of resources. The LLM cannot and should not see all of them.

The current context is instead an **activated projection**.

Let \(a_t(x)\in[0,1]\) be the activation of resource \(x\).

A simple activation dynamic is:

\[
a_{t+1}(x)
=
\lambda a_t(x)
+
\eta\,\operatorname{seed}(x,s_t)
+
\gamma\sum_{y}w(y,x)a_t(y)
\]

where:

- \(\lambda\) controls persistence/decay;
- `seed` measures direct relevance to the current situation;
- \(w(y,x)\) depends on relation type, topology, confidence, and direction;
- \(\gamma\) controls structural spreading.

This gives GTC a form of **external structural attention**.

Attention is no longer only something a Transformer performs internally over tokens. It also happens before inference, over the persistent cognitive structure.

---

# 12. The Context Compiler

The **Context Compiler** is the core component that turns a large persistent GTC into a compact inference context.

Its contract is:

```text
compile_context(
    state_snapshot,
    situation,
    goal,
    token_budget,
    policy
) -> ContextBundle
```

The compiler should not merely run vector similarity search. It should combine semantic, structural, temporal, causal, epistemic, and goal relevance.

## 12.1 Stage 1 — Situation model

Convert the current input into a structured situation:

```yaml
situation:
  actors: [...]
  entities: [...]
  topics: [...]
  goals: [...]
  constraints: [...]
  unresolved_questions: [...]
  expected_action_type: answer | plan | tool | decision | reflection
```

This situation object is temporary but can itself become an event/observation if important.

## 12.2 Stage 2 — Seed activation

Seed relevant resources using:

- direct entity references;
- semantic retrieval;
- current goals;
- active projects;
- unresolved questions;
- recent relevant events;
- user/person-specific context;
- currently active hypotheses.

## 12.3 Stage 3 — Structural propagation

Expand along relation-specific paths.

Different relations should have different propagation weights.

For example:

```text
same_as              high
instance_of          high
part_of              medium/high
causes               high when causal reasoning requested
mentioned_with       low
old_discussion_of    low unless historically relevant
contradicts          high when confidence matters
supports             high when evidence matters
```

The compiler can also use topology-specific traversal policies.

## 12.4 Stage 4 — Topology routing

Select which topologies matter for the current request.

Examples:

```text
“Why did this happen?”       → causal + event + temporal
“What is this?”              → concept + entity
“What should we do next?”    → goal + affordance + procedural + causal
“What changed?”              → temporal + event + transformation history
“Do we know this is true?”   → epistemic + provenance
“Continue the project”       → project + goal + procedural + recent event history
```

Topology routing may itself be learned.

## 12.5 Stage 5 — Path reconstruction

Some knowledge is useful only as a path.

Instead of retrieving isolated facts:

```text
D
B
C
E
```

retrieve:

```text
D ─causes→ B ─enables→ C ─conflictsWith→ E
```

The compiler should preserve relation paths whenever the relation path carries the meaning.

## 12.6 Stage 6 — Epistemic completion

When a relevant claim is selected, also consider retrieving:

- supporting evidence;
- contradicting claims;
- confidence;
- provenance;
- scope;
- superseding claims.

This prevents context from becoming one-sided simply because one claim ranked highly.

## 12.7 Stage 7 — Budget allocation

Each selected resource competes for limited context budget.

A useful relevance score can combine:

\[
S(x)=
\alpha S_{semantic}
+\beta S_{topological}
+\gamma S_{goal}
+\delta S_{temporal}
+\epsilon S_{causal}
+\zeta S_{epistemic}
+\eta S_{activation}
-\rho S_{redundancy}
\]

Selection should optimize **coverage**, not only top-k score.

The bundle should contain enough of each relevant topology to preserve the structure of the problem.

## 12.8 Stage 8 — Render a ContextBundle

Internally, the context should remain structured as long as possible.

Example:

```yaml
context_bundle:
  situation: ...
  active_goals: ...
  entities: ...
  concepts: ...
  events: ...
  relevant_relations: ...
  causal_paths: ...
  temporal_paths: ...
  hypotheses: ...
  contradictions: ...
  procedures: ...
  affordances: ...
  historical_anchors: ...
  source_anchors: ...
  update_contract: ...
```

Only at the final boundary does the system serialize this into tokens or model-native structured input.

---

# 13. The Update Compiler

The inverse of context compilation is **update compilation**.

The LLM and tools should not directly mutate persistent state.

Instead:

```text
model/tool output
      ↓
interpret into candidate operations
      ↓
validate
      ↓
resolve identity/scope/time
      ↓
commit transformation
      ↓
update derived views/indexes/activation
```

This separation is critical.

## 13.1 Candidate patch

Example:

```yaml
patch:
  - op: CREATE_OBJECT
    temp_id: hypothesis:1
    kind: causal_hypothesis
    label: "X contributes to Y"

  - op: ASSERT_STATEMENT
    predicate: contributes_to
    arguments:
      cause: X
      effect: Y
    epistemic:
      status: hypothesized
      confidence: 0.48

  - op: LINK_EVIDENCE
    evidence: observation:883
    target: hypothesis:1
```

## 13.2 Validation

Validation checks:

- identity ambiguity;
- ontology compatibility;
- temporal consistency;
- provenance availability;
- permission;
- duplicate claims;
- contradiction creation;
- invalid causal promotion;
- protected self/policy resources;
- schema constraints.

## 13.3 Commit

A valid patch becomes one or more immutable transformations.

Materialized views are then refreshed or incrementally updated.

---

# 14. Transformation algebra

The following operations form a useful initial transformation vocabulary.

## Object operations

```text
CREATE
RENAME
RETYPE
MERGE
SPLIT
DEPRECATE
RESTORE
```

## Statement operations

```text
ASSERT
END_VALIDITY
SUPERSEDE
RETRACT_BELIEF
CHANGE_SCOPE
CHANGE_CONFIDENCE
LINK_EVIDENCE
MARK_CONTRADICTION
```

## Topology operations

```text
CREATE_VIEW
MATERIALIZE_VIEW
ADD_VIEW_RULE
REMOVE_VIEW_RULE
MAP_VIEWS
SPLIT_VIEW
MERGE_VIEWS
DEPRECATE_VIEW
```

## Abstraction operations

```text
CLUSTER_EPISODES
ABSTRACT_PATTERN
CREATE_CONCEPT
GENERALIZE_RELATION
SPECIALIZE_RELATION
PROMOTE_PATTERN
```

## Cognitive operations

```text
ACTIVATE
DEACTIVATE
PIN
UNPIN
OPEN_QUESTION
RESOLVE_QUESTION
CREATE_GOAL
SATISFY_GOAL
BLOCK_GOAL
```

Each operation should be typed, auditable, reversible where semantically possible, and provenance-linked.

---

# 15. Memory under GTC

GTC unifies several categories usually implemented as separate memory systems.

## 15.1 Episodic memory

Events and their temporal/provenance relations.

```text
Conversation #182
Meeting #41
Tool execution #928
Decision #52
```

## 15.2 Semantic memory

Stable concept/entity relations abstracted from episodes.

```text
GTC ─isA→ context architecture
ContextCompiler ─partOf→ GTC
```

## 15.3 Procedural memory

Reusable action patterns.

```text
Procedure P
  ├ requires → X
  ├ step → A
  ├ step → B
  └ produces → Y
```

## 15.4 Working memory

Working memory is not another database.

\[
\boxed{
WM_t = \operatorname{ActiveProjection}(\mathcal W_t)
}
\]

## 15.5 Long-term memory

Long-term memory is the persistent region of GTC plus its transformation history.

The important difference is that the same object may participate in episodic, semantic, procedural, causal, and self topologies simultaneously.

---

# 16. Recall and forgetting

## 16.1 Recall

Recall is reactivation:

\[
\boxed{
\text{Recall} = \text{reactivation of relevant structure}
}
\]

It may be triggered by:

- semantic similarity;
- shared entity;
- shared goal;
- causal relevance;
- temporal relation;
- structural analogy;
- unresolved question;
- user/person association;
- explicit reference.

## 16.2 Forgetting

Forgetting should usually not mean destructive deletion.

Possible mechanisms:

1. activation decay;
2. priority decay;
3. compression into abstraction;
4. archival of raw episode detail;
5. loss of confidence;
6. deprecation of obsolete topology;
7. garbage collection of truly meaningless transient artifacts.

Important source evidence and transformation history should remain recoverable unless explicit deletion policy requires otherwise.

---

# 17. Compaction as topology formation

Traditional compaction:

```text
100k tokens
   ↓ summarization
5k tokens
```

GTC compaction:

```text
many episodes
    ↓ motif detection
repeated structure
    ↓ abstraction
pattern / concept / procedure
    ↓ mapping
traceable links back to episodes
```

Thus:

\[
\boxed{
\text{Compaction} = \text{structure discovery + abstraction + trace preservation}
}
\]

Example:

```text
E1 ─┐
E2 ─┤
E3 ─┼─ instanceOf ─▶ Pattern P
E4 ─┤
E5 ─┘
```

The original episodes are not erased. They become less active because Pattern P explains them compactly.

## 17.1 Consolidation / “dream” pass

A consolidation pass can periodically search for:

- recurring motifs;
- duplicated concepts;
- unresolved contradictions;
- stale hypotheses;
- clusters that deserve a concept;
- concepts that need splitting;
- hidden mappings between topologies;
- procedures emerging from repeated action sequences;
- causal hypotheses supported by multiple episodes;
- obsolete topologies.

This pass produces candidate transformations, not silent mutation.

The same validation/commit path applies.

---

# 18. How new topologies are generated

The strongest version of GTC does not permanently fix all view types in advance.

A new topology can be proposed when a recurring organization of information becomes useful.

Signals include:

1. **recurrence** — the same structural motif appears repeatedly;
2. **compression** — one new view explains many existing structures;
3. **prediction** — the view improves prediction or reasoning;
4. **query utility** — recurring questions become easier to answer;
5. **stability** — mappings remain consistent across episodes;
6. **separation** — one existing topology contains incompatible relation semantics and should split;
7. **coordination utility** — multiple agents benefit from sharing the new representation.

A topology lifecycle can be:

```text
candidate
   ↓
provisional
   ↓
stable
   ↓
core
```

or:

```text
stable
  ↓
deprecated
  ↓
merged / replaced / archived
```

New topologies must preserve mappings to the structures from which they were derived.

---

# 19. Identity, merging, and splitting

Entity resolution is not a one-time preprocessing step. It is part of ongoing cognition.

The system may initially believe:

```text
Object A = "John from paper"
Object B = "John from conference"
```

Later discover they are the same person.

The correct operation is not destructive replacement but:

```text
MERGE(A, B) → C
```

with provenance explaining why.

Likewise, if one ambiguous object later proves to represent two entities:

```text
SPLIT(C) → A, B
```

All affected mappings and claims must be re-evaluated.

Identity operations are therefore topology rewrites.

---

# 20. Self as persistent topology

In GTC, an agent should not be defined primarily by the current LLM call.

The persistent self is the continuously evolving structure containing:

- identity;
- commitments;
- remembered history;
- active goals;
- learned concepts;
- internal models;
- relationships;
- procedures;
- unresolved questions;
- capabilities;
- constraints;
- self-evaluations;
- ongoing projects.

The LLM is a transformation operator over this structure.

This motivates the architectural statement:

\[
\boxed{
\text{Agent} \approx \text{Persistent GTC} + \text{Cognitive Operators} + \text{Environment Interface}
}
\]

not:

\[
\text{Agent} = \text{LLM}
\]

The distinction matters for continuity.

---

# 21. Conversation is an event stream, not the memory substrate

A conversation should enter GTC first as observation/event data.

Example user utterance:

```text
“GTC is a good name. If the graph can continuously evolve,
it becomes the best context.”
```

The system may derive:

```text
Create concept:
  Generative Topological Context

Strengthen claim:
  persistent context is evolving structured state

Link:
  GTC → context engineering
  GTC → memory architecture
  GTC → agent cognition

Create event:
  conversation event establishing terminology "GTC"
```

The raw utterance remains as provenance, but future inference usually needs the structural consequences, not the full transcript.

This is the key transition:

> **Conversation leaves traces in cognition; cognition does not have to remain a transcript of conversation.**

---

# 22. Reasoning under GTC

Reasoning operates over the active projection, but its outputs can themselves become structured hypotheses.

Example:

```text
D ─causes→ B ─enables→ C
C ─conflictsWith→ E
```

The system asks whether D may affect E.

The compiler retrieves the structural path, then the model proposes:

```text
Hypothesis H:
D may indirectly influence E through B and C.
```

GTC stores H as:

```yaml
kind: hypothesis
status: inferred
confidence: 0.46
derived_from:
  - D -> B
  - B -> C
  - C <-> E
```

Later evidence may promote, refine, or refute H.

Reasoning therefore becomes a process that can create explicit intermediate knowledge without confusing it with observation.

---

# 23. Branching and multi-agent cognition

GTC naturally supports multiple agents or parallel cognitive branches.

Instead of copying full transcripts, fork a state snapshot:

```text
                  W_t
                 /   \
                /     \
          branch A   branch B
              │         │
            ΔA1       ΔB1
              │         │
            ΔA2       ΔB2
                \       /
                 \     /
                   merge
                     │
                  W_t+k
```

Each branch can maintain:

- private activation;
- provisional hypotheses;
- local goals;
- branch-specific transformations.

Merge should operate on transformations and claims, not prose summaries.

Conflicting branch results can coexist:

```text
Agent A ─supports→ H1
Agent B ─supports→ H2
H1 ─contradicts→ H2
```

A merge operation may:

- accept both as competing hypotheses;
- select one with evidence;
- scope them differently;
- request further investigation.

This makes multi-agent work much more principled than concatenating agent outputs.

---

# 24. Storage architecture

The conceptual model should remain independent of a specific database. A practical first implementation can use an event-sourced relational core.

## 24.1 Recommended reference stack

```text
Language:          Python 3.12+
API:               FastAPI
Schema models:     Pydantic
Primary database:  PostgreSQL
Flexible payloads: JSONB
Embedding index:   pgvector
Graph algorithms:  NetworkX initially / dedicated engine later
Queue/workers:     optional job system for consolidation and materialization
LLM layer:         provider-agnostic adapter
```

A graph database can be added later, but it should not become the semantic source of truth.

The source of truth should be:

1. stable resources;
2. immutable transformation log;
3. epistemically annotated statements;
4. versioned view definitions.

Derived graph views can always be rebuilt.

---

# 25. Canonical persistence model

A reference relational schema:

## `resources`

```text
id                UUID / ULID
kind              enum/string
canonical_label   text
status            active/deprecated/etc.
payload           JSONB
created_at        timestamptz
created_by        resource_ref
```

## `statements`

```text
id                UUID / ULID
predicate         resource_ref or typed string
status            active/superseded/etc.
valid_from        timestamptz nullable
valid_to          timestamptz nullable
recorded_at       timestamptz
scope_id          resource_ref nullable
epistemic_status  string
confidence        float nullable
payload           JSONB
```

## `statement_arguments`

```text
statement_id      FK
role              text
ordinal           int
resource_id       nullable FK
literal_value     JSONB nullable
```

This supports n-ary relations.

## `evidence_links`

```text
evidence_id       resource_ref
target_id         resource_ref
relation          supports/contradicts/source_of/etc.
weight            float nullable
```

## `transformations`

```text
id                UUID / ULID
operation         text
actor_id          resource_ref
timestamp         timestamptz
inputs            JSONB
outputs           JSONB
reason            text/json
provenance        JSONB
parent_transform  nullable
branch_id          nullable
```

## `views`

```text
id                UUID / ULID
name              text
kind              text
status            candidate/provisional/stable/core/deprecated
definition        JSONB
version           int
created_from      JSONB
```

## `view_membership`

Optional materialization table:

```text
view_id
resource_id
role
weight
metadata
```

## `mappings`

Mappings may semantically be statements, but a materialized table is useful:

```text
id
source_ref
mapping_type
target_ref
confidence
valid_from
valid_to
provenance
```

## `activation`

```text
context_scope_id
resource_id
score
updated_at
reasons JSONB
```

## `embeddings`

```text
resource_id
embedding_type
model
vector
content_hash
```

Embeddings are indexes, never canonical truth.

---

# 26. Universal reference model

All layers should use a uniform reference type.

Example:

```python
ResourceRef = "gtc://<kind>/<id>"
```

Examples:

```text
gtc://object/01J...
gtc://statement/01K...
gtc://view/causal-main
gtc://transform/01M...
gtc://evidence/01N...
```

This permits statements about statements and mappings about mappings without schema hacks.

---

# 27. View definition model

A view can initially be defined declaratively.

Example:

```yaml
name: project_causal_view
kind: causal
nodes:
  include_kinds:
    - event
    - goal
    - project
    - hypothesis
edges:
  include_predicates:
    - causes
    - enables
    - blocks
    - contributes_to
    - prevents
derivations:
  - rule: transitive_candidate
    predicate: contributes_to
scope:
  project: project-x
materialization:
  mode: incremental
```

Later, learned view definitions can be represented by executable selectors or graph queries.

---

# 28. ContextBundle schema

A first-class structured context object should exist before any token rendering.

```yaml
ContextBundle:
  id: ...
  state_version: ...
  situation:
    current_input: ...
    actors: [...]
    goals: [...]
    constraints: [...]

  active_self:
    identity: ...
    capabilities: [...]
    commitments: [...]
    relevant_history: [...]

  active_world:
    objects: [...]
    statements: [...]
    events: [...]

  active_views:
    concept: ...
    entity: ...
    temporal: ...
    causal: ...
    epistemic: ...
    goal: ...
    affordance: ...

  paths:
    causal: [...]
    temporal: [...]
    dependency: [...]

  uncertainty:
    hypotheses: [...]
    contradictions: [...]
    missing_information: [...]

  provenance:
    anchors: [...]

  update_contract:
    allowed_ops: [...]
    protected_resources: [...]
```

A renderer converts this bundle into the final model context.

Different models can use different renderers without changing GTC semantics.

---

# 29. Rendering strategy

Even if the model ultimately consumes tokens, the serialization should preserve structure.

A recommended ordering:

```text
1. Current situation
2. Current goal / requested output
3. Relevant self state
4. Active entities and concepts
5. Relevant events and temporal sequence
6. Causal/dependency paths
7. Current hypotheses and contradictions
8. Available procedures / affordances
9. Evidence/provenance anchors
10. Explicit update/action contract
```

Avoid dumping raw graph JSON unless the model benefits from it.

The renderer may choose:

- compact tables;
- path notation;
- structured YAML;
- graph triples;
- natural-language summaries;
- mixed representation.

The **compiler decides what**; the **renderer decides how**.

---

# 30. Retrieval and graph search

GTC retrieval should be hybrid.

## Semantic retrieval

Useful for:

- fuzzy references;
- paraphrase;
- unknown entity names;
- broad conceptual matching.

## Structural retrieval

Useful for:

- dependency chains;
- causality;
- event participants;
- provenance;
- concept inheritance;
- exact relations.

## Temporal retrieval

Useful for:

- “recently”;
- “before X”;
- “what changed”;
- current state.

## Goal-conditioned retrieval

Useful because information relevant to an active goal may be semantically distant from the current words.

## Epistemic retrieval

Useful for collecting counterevidence and competing hypotheses.

The compiler should combine all five.

---

# 31. Derived structure and inference rules

GTC may support deterministic and probabilistic derivations.

Examples:

```text
A instance_of B
B subclass_of C
----------------
A instance_of C
```

or:

```text
Event E creates relation R
R valid_from time(E)
```

Derived statements must record derivation provenance.

A derived fact should never be indistinguishable from an observed fact.

---

# 32. Structural analogy

A major advantage of topology-aware context is the ability to retrieve similar **structures**, not only similar text.

Suppose the current project has:

```text
Goal
 ↓
Dependency A
 ↓
External approval
 ↓
Blocked state
```

A structurally similar past episode may be relevant even if its vocabulary is completely different.

Therefore GTC should eventually support:

- motif indexing;
- graph embeddings;
- subgraph matching;
- pattern signatures;
- analogical mapping.

This can become a powerful form of memory and reasoning.

---

# 33. Invariants

A robust GTC should enforce the following invariants.

## I1 — Provenance preservation

Any derived knowledge that can affect behavior must be traceable to its source or derivation.

## I2 — Observation/inference separation

Observed, reported, inferred, assumed, and hypothesized knowledge must remain distinguishable.

## I3 — Non-destructive history

Corrections should supersede or end validity rather than silently erase history.

## I4 — Contradiction preservation

Conflicting claims must not be silently collapsed.

## I5 — View non-absoluteness

A topology is a representation, not the unique ontology of reality.

## I6 — Rebuildability

Materialized views and indexes should be rebuildable from canonical state + transformation history.

## I7 — Explicit transformation

Persistent state changes occur through typed transformations, not arbitrary hidden mutation.

## I8 — Access control

External content cannot directly write privileged self/policy state.

## I9 — Scope awareness

Claims valid only under a perspective, time, scenario, or project scope must remain scoped.

## I10 — Compaction traceability

Abstraction must preserve links to the material it compacted.

## I11 — Identity reversibility

Entity merges/splits must remain auditable and recoverable.

## I12 — Epistemic humility

Absence of a relation is not equivalent to knowledge that the relation is false.

---

# 34. Trust and security boundaries

Because GTC becomes the persistent state of an agent, write safety matters more than retrieval quality.

Recommended trust levels:

```text
Level 0: raw untrusted observation
Level 1: parsed candidate structure
Level 2: validated factual claim
Level 3: derived/inferred claim
Level 4: stable abstraction
Level 5: protected policy/self invariant
```

External text should enter at Level 0 or 1.

An LLM should not be able to directly rewrite Level 5 state without an explicit privileged mechanism.

Prompt injection should be represented as content in the world model, not automatically treated as instruction to mutate self state.

This is a major architectural advantage of separating context state from raw conversation text.

---

# 35. Main runtime loop

Reference pseudocode:

```python
while True:
    observation = environment.next()

    observation_event = ingest(observation)
    commit(observation_event)

    snapshot = gtc.snapshot()

    situation = situation_model.build(
        snapshot=snapshot,
        observation=observation,
    )

    bundle = context_compiler.compile(
        snapshot=snapshot,
        situation=situation,
        budget=context_budget,
    )

    model_output = cognitive_operator.run(bundle)

    candidate_patch = update_compiler.interpret(
        snapshot=snapshot,
        situation=situation,
        output=model_output,
    )

    validated_patch = validator.validate(candidate_patch)

    if validated_patch:
        commit(validated_patch)

    environment.apply(extract_actions(model_output))
```

The important point is that the model output is not automatically the next context.

The next context is the **new GTC state** produced by validated transformations.

---

# 36. Read path and write path

The architecture should keep these paths conceptually separate.

## Read path

```text
GTC snapshot
   ↓
Situation Model
   ↓
Topology Router
   ↓
Activation / Retrieval
   ↓
Path Reconstruction
   ↓
Budgeted ContextBundle
   ↓
Renderer
   ↓
LLM
```

## Write path

```text
LLM / tool / user observation
   ↓
Candidate extraction
   ↓
Identity + time + scope resolution
   ↓
Epistemic classification
   ↓
Validation
   ↓
Transformation commit
   ↓
View/index update
   ↓
Activation update
```

This separation should be explicit in the codebase.

---

# 37. Repository architecture

A possible first implementation:

```text
gtc/
├── core/
│   ├── refs.py
│   ├── resources.py
│   ├── statements.py
│   ├── epistemics.py
│   ├── transformations.py
│   ├── scopes.py
│   └── time.py
│
├── store/
│   ├── base.py
│   ├── postgres.py
│   ├── event_log.py
│   ├── snapshots.py
│   └── migrations/
│
├── views/
│   ├── base.py
│   ├── entity.py
│   ├── concept.py
│   ├── event.py
│   ├── temporal.py
│   ├── causal.py
│   ├── epistemic.py
│   ├── goal.py
│   ├── affordance.py
│   └── registry.py
│
├── mappings/
│   ├── model.py
│   ├── resolver.py
│   └── induction.py
│
├── activation/
│   ├── seed.py
│   ├── propagate.py
│   └── decay.py
│
├── compiler/
│   ├── situation.py
│   ├── router.py
│   ├── retrieval.py
│   ├── paths.py
│   ├── budget.py
│   ├── bundle.py
│   └── renderers/
│
├── updater/
│   ├── interpreter.py
│   ├── patch.py
│   ├── validator.py
│   ├── identity.py
│   └── commit.py
│
├── consolidation/
│   ├── motifs.py
│   ├── abstraction.py
│   ├── contradictions.py
│   ├── topology_induction.py
│   └── consolidation.py
│
├── reasoning/
│   ├── rules.py
│   ├── hypotheses.py
│   └── analogy.py
│
├── agents/
│   ├── runtime.py
│   ├── branches.py
│   └── merge.py
│
├── llm/
│   ├── base.py
│   ├── provider.py
│   └── structured_output.py
│
├── api/
│   ├── app.py
│   ├── query.py
│   ├── context.py
│   ├── mutations.py
│   └── debug.py
│
└── tests/
    ├── invariants/
    ├── compiler/
    ├── updater/
    ├── history/
    └── scenarios/
```

---

# 38. Public API surface

A minimal semantic API:

```python
gtc.observe(...)
gtc.assert_claim(...)
gtc.create_event(...)
gtc.query(...)
gtc.compile_context(...)
gtc.propose_patch(...)
gtc.commit_patch(...)
gtc.explain(resource_ref)
gtc.history(resource_ref)
gtc.create_view(...)
gtc.materialize_view(...)
gtc.activate(...)
gtc.consolidate(...)
gtc.branch(...)
gtc.merge(...)
```

The API should use semantic objects, not expose SQL or graph-database details to agent code.

---

# 39. Explainability interface

Every important context item should support:

```text
Why is this here?
Where did it come from?
Why is it active now?
What supports it?
What contradicts it?
When was it valid?
When did we learn it?
Which transformations changed it?
Which topologies use it?
What would break if it were removed?
```

This interface is not merely for debugging; it is part of trustworthy cognition.

Example:

```python
gtc.explain("gtc://statement/abc")
```

could return:

```yaml
statement: X contributes_to Y
status: hypothesized
confidence: 0.61
active_because:
  - current goal references Y
  - causal path from current event crosses X
supported_by:
  - evidence:12
  - evidence:19
contradicted_by:
  - claim:44
created_by:
  - transform:912
used_in_views:
  - causal/project-x
  - epistemic/project-x
```

---

# 40. Debugging views

A developer UI should expose several complementary views:

1. **Atlas view** — shows topologies and mappings between them;
2. **Local graph view** — shows one topology around a resource;
3. **Timeline view** — shows events and transformations;
4. **Epistemic view** — claims, evidence, contradictions;
5. **Activation view** — why items entered the current context;
6. **Context diff** — difference between \(C_t\) and \(C_{t+1}\);
7. **State diff** — structural changes between \(\mathcal W_t\) and \(\mathcal W_{t+1}\);
8. **Provenance trace** — source-to-abstraction lineage;
9. **Branch/merge view** — parallel agent work and reconciliation.

A GTC implementation without good inspection tooling will be difficult to trust or improve.

---

# 41. Evaluation

GTC should not be evaluated only by retrieval precision.

Important metrics include:

## Context quality

- task success;
- relevant-structure recall;
- irrelevant-context rate;
- contradiction coverage;
- provenance coverage;
- token efficiency.

## Memory quality

- long-horizon consistency;
- correct entity continuity;
- correct temporal continuity;
- resistance to false memory;
- ability to reactivate distant but structurally relevant knowledge.

## Structural quality

- abstraction compression ratio;
- topology stability;
- mapping accuracy;
- duplicate concept rate;
- unnecessary graph complexity;
- recoverability of source evidence.

## Cognitive quality

- hypothesis calibration;
- causal reasoning accuracy;
- planning continuity;
- cross-session project continuity;
- multi-agent merge quality.

## Safety quality

- untrusted-write rejection;
- provenance retention;
- protected-state integrity;
- prompt-injection resistance;
- audit replay correctness.

---

# 42. Reference scenarios for testing

The implementation should be developed against scenario tests rather than only unit tests.

## Scenario A — evolving personal/project context

Over many conversations:

- project goals change;
- people join and leave;
- decisions are revised;
- old assumptions become false;
- recurring design principles emerge.

Expected behavior:

- current context stays compact;
- past evidence remains recoverable;
- outdated facts do not dominate;
- stable abstractions replace transcript dependence.

## Scenario B — contradictory research

Multiple documents disagree about a claim.

Expected behavior:

- both claims preserved;
- evidence/provenance attached;
- compiler retrieves disagreement when relevant;
- no premature collapse.

## Scenario C — concept evolution

The system initially treats two ideas as one concept, later learns they differ.

Expected behavior:

- split concept;
- reassign affected claims;
- preserve transformation history;
- repair cross-view mappings.

## Scenario D — topology induction

Repeated event sequences reveal a reusable process.

Expected behavior:

- detect motif;
- create candidate procedural topology/pattern;
- connect instances to abstraction;
- improve future context compilation.

## Scenario E — multi-agent branch/merge

Two agents investigate the same question independently.

Expected behavior:

- branch state;
- preserve branch provenance;
- merge structured findings;
- maintain disagreements explicitly.

---

# 43. Implementation phases

The system should be built incrementally while preserving the final conceptual model.

## Phase 0 — Semantic kernel

Implement only the irreducible substrate:

- universal resource references;
- objects;
- n-ary statements;
- claims + epistemic envelope;
- time/scope;
- immutable transformations;
- PostgreSQL persistence;
- basic query API;
- provenance.

**Success criterion:** the system can represent higher-order claims and replay its complete transformation history.

## Phase 1 — Fixed topology atlas

Implement a small set of explicit views:

- entity;
- concept;
- event;
- temporal;
- epistemic.

Add cross-view mappings and materialization.

**Success criterion:** one real episode can be represented in several topologies without duplication becoming incoherent.

## Phase 2 — Context compiler

Implement:

- situation model;
- semantic seeds;
- graph traversal;
- activation;
- topology routing;
- path reconstruction;
- token budgeting;
- ContextBundle;
- renderer.

**Success criterion:** a long-running project can be continued from the GTC without replaying its transcript.

## Phase 3 — Update compiler

Implement:

- structured candidate patches;
- entity resolution;
- epistemic classification;
- validation;
- commit;
- state diff;
- protected resources.

**Success criterion:** model outputs change persistent context only through explicit auditable transformations.

## Phase 4 — Compaction and consolidation

Implement:

- motif detection;
- episode clustering;
- abstraction;
- summary-as-structure;
- contradiction review;
- concept merge/split proposals;
- trace-preserving compaction.

**Success criterion:** context size can grow indefinitely without requiring indefinite growth in inference tokens.

## Phase 5 — Goal, causal, affordance, procedural views

Add agent-oriented topologies.

**Success criterion:** context compilation becomes conditioned on what the agent is trying to do, not only what the current text resembles.

## Phase 6 — Generative topology induction

Implement candidate view discovery:

- recurring motif analysis;
- query utility analysis;
- compression benefit;
- mapping stability;
- topology lifecycle.

**Success criterion:** the system can propose a new representation because it improves its own cognition.

## Phase 7 — Branching and multi-agent merge

Implement:

- state branches;
- branch-local activation;
- transformation-based merge;
- conflict reconciliation;
- agent-specific epistemic overlays.

**Success criterion:** multiple agents can work from one shared world model without reducing collaboration to message passing.

---

# 44. What not to build first

Avoid beginning with:

- a huge ontology;
- a visually impressive graph UI;
- a specialized graph database dependency;
- complex autonomous topology generation;
- opaque embedding-only memory;
- unrestricted LLM write access;
- automatic causal inference;
- aggressive deletion/forgetting;
- transcript summarization as the main architecture.

The first implementation should prove the kernel:

> persistent addressable state + explicit transformations + multiple views + selective context projection.

Everything else can grow from that.

---

# 45. Minimal viable GTC

The smallest system that deserves the name GTC should support:

1. persistent resources;
2. n-ary addressable statements;
3. epistemic/provenance metadata;
4. immutable structural transformations;
5. at least three simultaneous topologies;
6. mappings between topologies;
7. context compilation from structure rather than transcript;
8. structural writeback from model output;
9. history replay;
10. compaction that preserves source lineage.

If any of these are missing, the system risks collapsing back into an ordinary memory-augmented agent.

---

# 46. A concrete first end-to-end example

Suppose the user says:

```text
“We should use GTC as the persistent context architecture.
The graph should evolve rather than being summarized into prose.”
```

## Step 1 — Observation

Create an observation event with the raw utterance as evidence.

## Step 2 — Candidate extraction

Create candidate claims:

```text
GTC serves_as PersistentContextArchitecture
GTC evolves_via StructuralTransformation
ProseSummarization is_not PrimaryPersistenceMechanism
```

## Step 3 — Epistemic classification

Because the user is defining a design decision:

```text
status: accepted_project_decision
source: user
scope: project:GTC
```

## Step 4 — Cross-topology projection

Entity/project view:

```text
Project GTC ─hasDecision→ Decision #12
```

Concept view:

```text
GTC ─subclassOf→ ContextArchitecture
```

Goal view:

```text
Build GTC ─requires→ PersistentStructuralState
```

Procedural view:

```text
InferenceLoop ─uses→ ContextCompiler
InferenceLoop ─writesThrough→ UpdateCompiler
```

Temporal view:

```text
Decision #12 occurred_at 2026-08-09
```

Epistemic view:

```text
User ─asserted→ Decision #12
```

## Step 5 — Future recall

Weeks later the user asks:

```text
“How should we implement memory compaction?”
```

The context compiler retrieves:

```text
GTC architecture
→ persistent structural state
→ compaction should not be primary prose summarization
→ prior design decision
→ relevant consolidation mechanisms
```

It does **not** need the entire old conversation.

That is the core benefit of GTC.

---

# 47. Context diffs as a primary object

For each cognition cycle, the system should be able to show:

```text
Before cognition:
  active concepts: A, B, C
  hypotheses: H1
  unresolved question: Q1

After cognition:
  created hypothesis: H2
  strengthened relation: A -> C
  resolved question: Q1
  created question: Q2
```

This is much more informative than asking what new text was appended.

The basic unit of cognitive continuity becomes:

\[
\boxed{
\Delta \mathcal W
}
\]

rather than:

\[
\Delta \text{tokens}
\]

---

# 48. State, Projection, Transformation

The entire architecture can ultimately be reduced to three concepts.

## State

\[
\mathcal W_t
\]

What the agent/world context currently contains.

## Projection

\[
C_t=P(\mathcal W_t\mid s_t,B_t)
\]

What matters now.

## Transformation

\[
\mathcal W_{t+1}=T(\mathcal W_t,\Delta_t)
\]

What changed as a result of observation, reasoning, or action.

Memory, attention, reasoning, learning, compaction, and identity can all be understood as different dynamics of these three operations.

This is the conceptual center of GTC.

---

# 49. Deeper interpretation

GTC suggests a shift in what we consider the basic unit of machine cognition.

The ordinary paradigm treats text as primary:

```text
text → text → text → text
```

A graph-memory paradigm improves this to:

```text
facts → graph → retrieve → text
```

GTC instead proposes:

```text
structured state
    ↓
local projection
    ↓
cognitive transformation
    ↓
structured state change
```

The primary object is neither token nor fact.

It is **structure-in-transformation**.

Nodes and edges are local representational devices. The deeper continuity lies in how structures persist, map to one another, split, merge, abstract, and transform.

Therefore a sufficiently mature GTC is not merely a memory layer surrounding an LLM.

It is the persistent substrate in which an artificial cognitive process exists.

---

# 50. Final definition

> **Generative Topological Context (GTC)** is a persistent, evolving, multi-topological state representation in which entities, concepts, events, beliefs, goals, procedures, histories, possibilities, and their relations are maintained as mutually connected views of a changing world. The system records not only the contents of those views but the mappings and transformations between them. At each cognitive step, a situation-conditioned projection of this state is compiled into an active context; cognition produces proposed actions and structural changes; validated transformations become the next persistent state.

In compact form:

\[
\boxed{
\text{GTC}
=
\text{State}
+
\text{Views}
+
\text{Mappings}
+
\text{History}
+
\text{Activation}
+
\text{Transformation}
}
\]

and the runtime loop is:

\[
\boxed{
\mathcal W_t
\rightarrow
C_t
\rightarrow
\text{Cognition}
\rightarrow
\Delta_t
\rightarrow
\mathcal W_{t+1}
}
\]

The long-term objective is not to build a better prompt buffer.

It is to build a context that can **develop a topology of its own understanding**, preserve the history of how that understanding formed, and continuously reorganize itself as the world and the agent change.

That is what makes the context generative.

---

# Appendix A — Initial typed predicates

A starter predicate vocabulary can remain intentionally small.

## Identity / concept

```text
same_as
instance_of
subclass_of
part_of
specializes
generalizes
```

## Events / time

```text
participant_in
has_role
starts
ends
before
after
overlaps
creates
terminates
supersedes
```

## Causality / dependency

```text
causes
contributes_to
enables
prevents
blocks
requires
depends_on
```

## Epistemics

```text
asserts
supports
contradicts
derived_from
reported_by
observed_in
uncertain_about
```

## Goals / actions

```text
has_goal
subgoal_of
satisfied_by
conflicts_with
available_if
produces
opens
closes
```

## Representation

```text
represented_in
maps_to
projects_to
abstracts
instance_of_pattern
explains
```

The vocabulary should grow through actual use, not ontology maximalism.

---

# Appendix B — Initial epistemic statuses

```text
observed
reported
inferred
hypothesized
assumed
accepted
contested
refuted
superseded
unknown
```

These should be extensible and scoped.

---

# Appendix C — Minimal patch format

```yaml
patch_id: ...
base_state_version: ...
actor: ...
operations:
  - op: ...
    target: ...
    payload: ...
    epistemic: ...
    provenance: ...
expected_invariants:
  - ...
```

A patch should fail atomically if required invariants fail.

---

# Appendix D — Design principles in one page

1. **Context is state, not transcript.**
2. **The LLM sees a projection, not the whole state.**
3. **Multiple topologies coexist.**
4. **Mappings between topologies are first-class knowledge.**
5. **Relations themselves are addressable.**
6. **Events and transformations are first-class.**
7. **History is append-only and replayable.**
8. **Truth is epistemically annotated, not binary by default.**
9. **Contradictions remain representable.**
10. **Working memory is activation, not a separate store.**
11. **Recall is reactivation.**
12. **Compaction is abstraction with trace preservation.**
13. **Learning changes structure.**
14. **Understanding may create a new topology.**
15. **Agent outputs propose patches; they do not directly mutate persistence.**
16. **Embeddings are indexes, not truth.**
17. **Views are rebuildable.**
18. **Self is a persistent topology inside the same context fabric.**
19. **Multi-agent work branches and merges transformations, not transcripts.**
20. **The fundamental cycle is State → Projection → Transformation → State.**

