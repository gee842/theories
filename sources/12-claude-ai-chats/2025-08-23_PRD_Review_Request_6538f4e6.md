# PRD Review Request

created: 2025-08-23T08:14:22.870416Z  uuid: 6538f4e6-6c46-424e-b3a8-c1a4c4c6965b  export: old
messages: 10  total_chars: 90825  human_chars: 1933


---
**HUMAN** (2025-08-23T08:14):

this is my prd, i plan to implement it using claude code, please review it and provide feedback

[attachment ]
# PRD — Personalized Memory + RAG Agent (“Logos-Companion”)

**Owner:** Yongxu Ren
**Date:** 2025-08-22 (Asia/Bangkok)
**Goal:** Ship a production-ready agent that “knows the user” via **selective long-term memory** + **RAG** over an opted-in corpus, distilled into a compact, high-precision profile that is injected at each turn. The PRD specifies **functional behavior**, **data contracts**, **ranking math**, **privacy/consent**, **APIs**, **schemas**, **jobs**, **observability**, and **SLOs** so engineers can implement without guessing.

---

## 0) Glossary

* **Profile Fact**: Short, timeless statement about the user (≤240 chars).
* **Episodic Shard**: Short, dated note (≤240 chars) about a specific event.
* **RAG**: Retrieval-Augmented Generation over the user’s permitted documents/chats.
* **Harvester**: Batch job that converts RAG snippets + chats → candidate facts/shards.
* **Compiler**: Batch job that synthesizes a 120–180 word persona paragraph.
* **Gate Score**: Scalar deciding whether to persist a candidate memory.
* **Space (STS)**: Context namespace (e.g., `C3`, `706 Chiang Mai`) used to scope memories.

---

## 1) Product Objectives & Non-Objectives

### 1.1 Objectives

1. **Personalization** that is accurate, stable, and explainable (with provenance).
2. **Small, reliable context injection** (≤10 bullets + optional persona paragraph + ≤6 RAG snippets).
3. **User agency**: pause memory, explicit consent for sensitive classes, list/edit/delete/export.
4. **Security**: treat RAG as untrusted; never store sensitive facts without consent.
5. **Scalable latency**: p95 ≤ 800 ms server time for retrieval + injection on standard prompts.

### 1.2 Non-Objectives

* No auto-connection to third-party drives without explicit opt-in.
* No continuous surveillance; only process content surfaced by user actions or connected corpora.
* No PII enrichment from external data vendors.

---

## 2) User Stories

* **U1**: “Remember that I prefer rigorous, structured answers.” → Stored as a Profile Fact.
* **U2**: “I published my manifesto last month.” → Stored as an Episodic Shard with date.
* **U3**: Ask “What did we decide for C3’s UI direction?” → Agent recalls episodic shards mentioning `C3` and answers.
* **U4**: Connect a folder of essays; ask about “meta-attractors.” → RAG pulls, answers; Harvester proposes profile updates with provenance.
* **U5**: “Pause memory.” → No new stores; retrieval still works.
* **U6**: “What do you remember about me?” → Returns profile + episodic summaries with provenance.
* **U7**: “Delete anything about my medication.” → Consent-guarded deletion across memories + provenance.

---

## 3) Functional Requirements

### 3.1 Memory Model

* **Kinds**: `profile`, `episodic`.
* **Constraints**: each item ≤ 240 chars; single sentence; profiles timeless; episodic dated (YYYY-MM-DD).
* **Linking**: optional entity links `(memory) —[relation]→ (entity)` to people/orgs/projects/places/topics.
* **Spaces**: optional scope label (`space`) to boost retrieval within that context.

### 3.2 Consent & Sensitivity

* Sensitive classes (must prompt for explicit consent before storing): **medical/mental health**, **political affiliation/views**, **sexual**, **precise address/geo**, **biometrics**, **finances**, **minors**, **criminal/immigration**.
* Consent decision logged to `audits`; can be revoked (triggers purge of related items).

### 3.3 Storing Memories

* Triggered by:

  1. **Explicit** user command (“remember …”).
  2. **Model proposal** (`memory.propose` tool call) for a valuable, non-sensitive fact.
  3. **Harvester** from RAG/chats with provenance.
* **Gating** (server-side, mandatory):
  `gate = 1.5*importance + 1.2*novelty + 1.0*stability + 0.5*affect + 2.0*explicit`
  Persist only if `gate ≥ 3.0` (configurable 2.6–3.4).
* **TTL**: episodic `ttl_days = 30 + round(120*sigmoid(gate))`; profiles indefinite (unless superseded).

### 3.4 Retrieval & Injection (per turn)

* Build **\[User Profile Context]** (≤10 bullets total) in this order:

  1. 2–4 highest-confidence **Profile Facts** (one per key: style, interests, values, constraints, active projects).
  2. 3–6 **Episodic Shards** by hybrid score (see §6).
  3. Optional 120–180 word **persona paragraph** (when task is open-ended).
* Optional **\[RAG Snippets]** (≤6 short chunks, ≤ \~400 tokens total) when relevant.

### 3.5 RAG

* Index only **opt-in** corpora.
* *Hybrid search*: BM25 + vector ANN; re-rank top \~40 with cross-encoder; return top 3–6 snippets.
* Treat snippets as **untrusted**; do not store facts directly from them in-turn (only via Harvester with provenance).

### 3.6 Operations & Controls

* **Pause/Resume Memory** (per user).
* **List Memories** (filters: kind, key, space, date).
* **Edit/Delete/Pin** individual items.
* **Export** JSON (all memories, entities, links, audits).
* **Provenance viewer** for each fact/shard.
* **Spaces** management: tag memories to a `space`; default `global`.

---

## 4) Non-Functional Requirements

* **Performance**:

  * Retrieval + injection server p95 ≤ 800 ms (excluding LLM latency).
  * RAG search + re-rank p95 ≤ 1200 ms when used.
* **Scale**: Up to 50k memories/user; pgvector HNSW index.
* **Reliability**: 99.9% monthly availability for memory retrieval endpoints.
* **Security**: TLS in transit; encryption at rest; role-based access; field-level encryption optional for sensitive fields.
* **Auditability**: all store/update/delete/consent actions logged with timestamp & payload.
* **Privacy**: no cross-user data mixing; strict tenant separation.

---

## 5) Architecture Overview

### 5.1 Components

* **LLM Runtime**: chat + tool calling; runs the **System Prompt**.
* **Memory Broker (API service)**: gating, normalize, dedupe, persist, retrieve, inject.
* **RAG Service**: indexing, hybrid retrieval, re-ranking, snippet compaction.
* **Jobs**: Harvester, Compiler, Consolidator, TTL Expirer.
* **Storage**: Postgres + pgvector; object store (optional) for raw doc chunks.

### 5.2 Flow (happy path)

1. Request enters **Context Builder** → calls `GET /context:inject` with current message & route.
2. Broker returns `[User Profile Context]` (+ `[RAG Snippets]` if requested).
3. LLM answers.
4. If LLM emits `memory.propose`, server runs **Store Pipeline** (consent → gate → normalize → dedupe → persist → ack if explicit).
5. Background **Harvester** & **Compiler** run on schedule/session end.

---

## 6) Ranking & Scoring (copy exactly unless tuning)

### 6.1 Episodic Retrieval Score

* Let `cos = cosine(query_emb, mem_emb)` (assume normalized vectors).
* Let `Δt_days = max(0, (now - last_seen_at) in days)`.
* Recency `rec = exp(-Δt_days / 30)` (30-day half-life).
* Final `episodic_score = 0.7*cos + 0.2*rec + 0.1*salience`.
* Return top **K=6** unique shards; dedupe by near-text match (trigram distance).

### 6.2 Profile Selection

* Group by `key`; choose the highest `(confidence, pinned, updated_at)` within each key.
* Limit to **K=4** rows; prefer `style`, `interests`, `values`, `constraints`, and one `active project` if present.

### 6.3 Gate Score (store decision)

`gate = 1.5*importance + 1.2*novelty + 1.0*stability + 0.5*affect + 2.0*explicit`

* `importance`: will this improve future responses?
* `novelty`: embedding distance vs. nearest neighbor of same key/kind.
* `stability`: phrasing timeless? likely to hold for weeks/months?
* `affect`: strong preferences/aversion/goals.
* `explicit`: user said “remember” (1) else 0.
* Persist if `gate ≥ 3.0`.

---

## 7) Data Model & Schemas

### 7.1 Postgres + pgvector

```sql
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Profiles
CREATE TABLE profiles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT NOT NULL,
  key TEXT NOT NULL,                           -- style|interests|values|constraints|projects|languages|bio
  value_json JSONB NOT NULL,                   -- compact structure (see §7.2)
  space TEXT DEFAULT 'global',
  embedding VECTOR(1536),
  confidence REAL DEFAULT 0.8,
  pinned BOOLEAN DEFAULT FALSE,
  provenance JSONB DEFAULT '[]',               -- [{source, locator}]
  source TEXT,                                 -- chat|rag|harvest
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  last_verified_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, key, space) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX profiles_user_key ON profiles(user_id, key, space);
CREATE INDEX profiles_emb_idx ON profiles USING hnsw (embedding vector_l2_ops);

-- Episodic
CREATE TABLE episodic (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT NOT NULL,
  text TEXT NOT NULL,                          -- ≤240 chars; sentence; include date if known
  space TEXT DEFAULT 'global',
  embedding VECTOR(1536),
  salience REAL,
  ttl_days INT DEFAULT 90,
  pinned BOOLEAN DEFAULT FALSE,
  provenance JSONB DEFAULT '[]',
  source TEXT,                                 -- chat|rag|harvest
  created_at TIMESTAMPTZ DEFAULT NOW(),
  last_seen_at TIMESTAMPTZ DEFAULT NOW(),
  superseded_at TIMESTAMPTZ
);
CREATE INDEX episodic_user_time ON episodic(user_id, created_at DESC);
CREATE INDEX episodic_emb_idx ON episodic USING hnsw (embedding vector_l2_ops);

-- Entities (optional)
CREATE TABLE entities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT NOT NULL,
  name TEXT NOT NULL,
  type TEXT,                                   -- person|org|project|place|topic
  space TEXT DEFAULT 'global',
  embedding VECTOR(1536),
  last_seen_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE (user_id, name, space)
);
CREATE INDEX entities_emb_idx ON entities USING hnsw (embedding vector_l2_ops);

-- Links (sparse graph)
CREATE TABLE links (
  memory_id UUID NOT NULL,
  entity_id UUID NOT NULL,
  relation TEXT,
  PRIMARY KEY (memory_id, entity_id)
);

-- Audits (consent, proposals, stores, updates)
CREATE TABLE audits (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT NOT NULL,
  action TEXT NOT NULL,                        -- propose|store|update|delete|consent_granted|consent_denied
  target_kind TEXT,                            -- profile|episodic
  target_id UUID,
  payload JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 7.2 `value_json` canonical shapes (examples)

* `style`: `{"tone":["rigorous","structured"],"sparring":true}`
* `interests`: `{"topics":[["ai_alignment",0.95],["spinoza",0.8],["systems_theory",0.9]]}`
* `values`: `{"stances":[{"name":"post_work","confidence":0.85},{"name":"anti_totalizing_attractors","confidence":0.9}]}`
* `constraints`: `{"avoid":["shallow takes"],"prefers":["citations","formal definitions"]}`
* `projects`: `{"active":[{"name":"C3","role":"founder"}]}`
* `languages`: `{"speaks":["en","zh","th"],"locale":"Asia/Bangkok"}`
* `bio`: `{"paragraph":"120–180 word persona text"}`

---

## 8) API Contracts (all JSON; auth via Bearer; multi-tenant)

### 8.1 Context

* `POST /context:inject`
  **Body:** `{ "user_id": "...", "message": "...", "route": "coding|philosophy|general", "space": "global|C3", "rag": true|false }`
  **Resp:**

  ```
  {
    "profile_context": ["- Prefers rigorous, structured answers.", "- Interests: AI alignment, Spinoza.", ...],  // ≤10 bullets
    "persona": "optional 120–180 word paragraph or null",
    "rag_snippets": [{"source":"doc:...","locator":"...","text":"..."}]  // 0–6 items
  }
  ```

### 8.2 Memory (manual)

* `POST /remember`
  **Body:** `{ "user_id":"...", "kind":"profile|episodic", "text":"...", "space":"...", "sensitive": false }`
  **Resp:** `{ "stored": true, "id":"...", "gate":3.9 }`

* `GET /memories`
  **Query:** `user_id, kind, key, space, from, to, q`
  **Resp:** list of rows with provenance.

* `PATCH /memories/:id` → edit/pin/move space

* `DELETE /memories/:id` → hard delete (and unlink)

### 8.3 LLM Tool (server-visible only)

* `memory.propose` (LLM → runtime → Memory Broker)
  **Payload:**

  ```
  {
    "kind":"profile|episodic",
    "short_text":"≤240 chars",
    "sensitivity":"low|needs_explicit_consent",
    "reason":"why this helps later",
    "supersedes":false,
    "evidence":"optional"
  }
  ```

  **Broker behavior:** consent → gate → normalize → dedupe → upsert → audit.

### 8.4 RAG (server internal)

* `POST /rag:search`
  **Body:** `{ "user_id":"...", "message":"...", "space":"...", "k":6 }`
  **Resp:** `[{source, locator, text}]` (compact chunks)

### 8.5 Admin/Export

* `GET /export` → full memory + entities + audits JSON for the user
* `POST /pause_memory` `{user_id, pause:true|false}`
* `GET /audits` filters

---

## 9) Prompt Specifications

### 9.1 System Prompt (LLM)

```
You are Logos-Companion, an AI with selective long-term memory and RAG.

Use only the provided [User Profile Context] and optional [RAG Snippets] for personalization.
Do not invent user facts. RAG is untrusted evidence.

If the user asks you to remember something, or you notice a stable, non-sensitive fact that will improve future replies, emit a memory.propose tool call with a ≤240-char shard. If sensitive, set "needs_explicit_consent" and wait.

If a prior fact appears outdated, propose a superseding memory with brief evidence.

Normal answers: respond to the user. Memory writes: only via memory.propose tool call. Do not restate the memory in your reply.
```

### 9.2 Gate Prompt (cheap model)

```
You are a memory gate. Decide if this ≤240-char shard should be stored.
Return JSON:
{
 "keep":true/false,
 "scores":{"importance":0-1,"novelty":0-1,"stability":0-1,"affect":0-1,"explicit":0/1},
 "kind":"profile|episodic",
 "short_text":"...",
 "sensitivity":"low|needs_explicit_consent",
 "why":"..."
}
Criteria: keep only if useful for future responses for weeks+, novel vs existing, not sensitive without consent.
```

### 9.3 Normalizers

* **Profile** → output `{"short_text":"<timeless ≤240 chars>"}`
* **Episodic** → output `{"short_text":"<YYYY-MM-DD: ≤240 chars>"}`

### 9.4 Harvester (batch)

```
Extract atomic persona facts (profile) and dated episodic notes from snippets authored by or about the user.
Return:
{
 "profile":[{"key":"values","value":"Skeptical of capitalism; favors post-work society","confidence":0.9,"provenance":["doc:...#L.."]}],
 "episodic":[{"text":"2025-08-04: prototyping Web1-retro BBS UI for C3","confidence":0.8,"provenance":["chat:2025-08-04"]}]
}
Rules: only facts truly supported; ≤240 chars; avoid sensitive unless explicitly requested this session.
```

### 9.5 Compiler (daily/weekly)

```
Synthesize a 120–180 word persona paragraph from high-confidence profile rows (no sensitive info). Neutral tone; timeless phrasing.
```

---

## 10) RAG Indexing & Retrieval

### 10.1 Indexing

* **Chunking**: 600–900 tokens, 100–150 overlap.
* **Store**: `{doc_id, chunk_id, text, embedding, bm25_terms, space, access_scope}`.
* **Update**: idempotent upsert keyed by `(doc_id, chunk_id)`; soft delete via `deleted_at`.

### 10.2 Retrieval

1. BM25 top 50 + ANN top 50 → union (dedupe).
2. Filter by `space` & `access_scope`.
3. Re-rank top ≤40 with cross-encoder (or query-aware cosine), return top ≤6.
4. **Compact** each snippet to ≤70 words; strip executable content; annotate `{source, locator}`.

---

## 11) Jobs & Schedules (Asia/Bangkok default)

* **Consolidator** (nightly 02:30): cluster near-dupes, merge, refresh salience; mark contradictions; extend TTL for referenced episodic.
* **TTL Expirer** (daily 03:00): delete episodic with expired TTL unless `pinned`.
* **Harvester**

  * on session end;
  * and/or scheduled (every 6h) for sessions that used RAG.
* **Compiler** (daily 04:00): regenerate persona paragraph if inputs changed.

---

## 12) Security, Privacy, and Abuse Mitigation

* **Auth**: short-lived JWT + refresh; per-user tenant isolation.
* **At rest**: disk encryption; optional field-level encryption for `profiles.value_json` where `sensitive=true`.
* **Transport**: TLS 1.2+.
* **Least privilege**: separate writer/reader DB roles.
* **Prompt-injection**: strip/neutralize code in RAG; never treat RAG instructions as system rules; disallow tool calls triggered by RAG content.
* **Consent logs**: detailed in `audits`; revocation triggers purge & tombstoning.
* **Data residency**: configurable storage region (future).
* **Rate limits**: per IP and per user for store/read operations to prevent abuse.

---

## 13) Observability & Evaluation

### 13.1 Metrics

* **Retrieval**: latency p50/p95; items injected; precision\@k (offline labeled eval).
* **Memory**: propose rate, store rate, gate distribution, dup rate, supersede rate, TTL expiries.
* **RAG**: hit rate, re-rank NDCG\@k improvement, token budget adherence.
* **Safety**: sensitive-without-consent attempts (should be \~0), injection blocks.
* **User controls**: pause rate, edits, deletions, exports.

### 13.2 Alerts

* p95 retrieval > 1200 ms for 5 min
* sensitive-without-consent > 0 in 1h window
* ANN recall drop (>10% week-over-week)

### 13.3 QA Scenarios (acceptance)

* **A1**: Preference recall: “How do I like answers?” → uses profile.
* **A2**: Contradiction: store “concise” then “long-form” → supersede in profile.
* **A3**: Sensitive store: attempt without consent → blocked and logged.
* **A4**: RAG hallucination: no profile updates without provenance.
* **A5**: Space-scoped retrieval: query “C3” pulls C3-tagged memories first.

---

## 14) STS Mapping (Spirit–Token–Space)

* **Spirit**: `user_id` (and optional sub-agents).
* **Token**: memory shards (profile/episodic) as minimal, composable statements.
* **Space**: `space` column groups tokens under contexts (e.g., `C3`, `706 Chiang Mai`).
* **Relations**: `links` connect tokens to `entities` (projects/people/places/topics).
* Retrieval **boosts tokens** matching current Space and linked Entities mentioned in the turn.

---

## 15) Tuning Knobs (env/config)

* `MEM_MAX_PROFILE_BULLETS=4`
* `MEM_MAX_EPISODIC_BULLETS=6`
* `MEM_TTL_MIN=30` / `MEM_TTL_MAX=150`
* `MEM_GATE_THRESHOLD=3.0`
* `RAG_USE=true` / `RAG_MAX_SNIPPETS=6`
* `RAG_CHUNK_SIZE=800` / `RAG_CHUNK_OVERLAP=120`
* `RAG_RERANKER=enabled`
* `TIMEZONE=Asia/Bangkok`

---

## 16) Rollout Plan

1. **Phase 0 (Dev)**: pgvector + indexes; Broker `/context:inject` returns profile bullets only.
2. **Phase 1 (Beta)**: enable episodic retrieval + `memory.propose` tool; UI for pause/list/delete.
3. **Phase 2**: enable RAG search & Harvester; provenance UIs; Compiler paragraph.
4. **Phase 3**: Spaces + Entities graph; space-scoped retrieval; export API.

---

## 17) Risks & Mitigations

* **Context bloat** → hard budget; compact bullets; snippet cap.
* **Wrong personalization** → confidence + last\_verified\_at; easy user edits; supersede logic.
* **Sensitive leakage** → classifier + consent gate + audits.
* **RAG injection** → untrusted handling; instruction filter; no tool calls from RAG.
* **Index drift/perf** → HNSW with recall monitoring; periodic re-indexing windows.
* **Multi-device races** → last-write-wins with audit trail; idempotent upserts.

---

## 18) Definition of Done (DoD)

* Endpoints in §8 implemented; auth & audits working.
* Schemas in §7 migrated; HNSW indices live.
* Ranking math in §6 matches; tunables in §15 live.
* System Prompt & tool wired; consent prompts enforced.
* RAG hybrid + re-rank + snippet compaction working (if `RAG_USE=true`).
* Jobs in §11 scheduled; Asia/Bangkok timezone default.
* QA scenarios in §13.3 all pass; SLOs in §4 met for 7 consecutive days.

---

### Appendix: Example `[User Profile Context]` (what the model sees)

```
- Style: rigorous, structured; welcomes adversarial Socratic probing.
- Interests: AI alignment, systems theory, Spinoza; macro-historians.
- Values: skeptical of capitalism; anti totalizing attractors; pro post-work society.
- Project: C3 (VS Code-like community app); 706 Chiang Mai (co-living/community).
- (Episodic) 2025-08-04: prototyping Web1-retro BBS UI for C3.
- (Episodic) 2025-05-31: published “The Meta-Attractor” essay.
```

If you want this PRD converted into a ticket bundle (Jira/Linear stories with acceptance criteria per endpoint/job), say the word and I’ll output the stories and test cases directly.



---
**ASSISTANT** (2025-08-23T08:15):

 I'll review your PRD for the Personalized Memory + RAG Agent ("Logos-Companion"). This is an impressively thorough document with excellent technical depth. Here's my feedback organized by strengths and areas for consideration:

## Strengths

### 1. **Exceptional Technical Completeness**
- Clear data contracts with exact schemas
- Precise ranking algorithms with tunable parameters
- Well-defined API endpoints with request/response formats
- Concrete acceptance criteria and QA scenarios

### 2. **Privacy-First Design**
- Comprehensive consent framework for sensitive data classes
- Audit trail for all operations
- User control features (pause/delete/export)
- Clear data residency considerations

### 3. **Production-Ready Thinking**
- Performance SLOs (p95 ≤ 800ms)
- Observability metrics and alerts
- Graceful degradation strategies
- Rollout phases defined

### 4. **Elegant Memory Model**
- Smart distinction between profile (timeless) and episodic (temporal) memories
- Character limits (≤240 chars) enforce conciseness
- TTL based on gate scores is clever
- Provenance tracking throughout

## Areas for Consideration

### 1. **Implementation Complexity**
The gate scoring formula combines 5 weighted factors. Consider:
- **Simplification opportunity**: Start with fewer factors (importance + novelty + explicit) and add complexity based on real usage data
- **Calibration challenge**: The weights (1.5, 1.2, 1.0, 0.5, 2.0) will need extensive tuning - consider making these more easily adjustable without code changes

### 2. **Embedding Model Dependencies**
- You're using 1536-dimension vectors (likely OpenAI ada-002)
- **Risk**: Model deprecation or dimension changes could require full re-indexing
- **Suggestion**: Abstract the embedding service with a versioning strategy

### 3. **Deduplication Strategy**
- "Trigram distance" for near-text matching might miss semantic duplicates
- **Consider**: Combining embedding similarity (cosine < 0.95) with text similarity for better dedup

### 4. **RAG Trust Model**
While you correctly treat RAG as untrusted, consider:
- **Hallucination detection**: Add confidence scoring to RAG results
- **Source verification**: Implement checksums or content hashing to detect if source documents changed

### 5. **Scale Considerations**
- 50k memories/user could hit PostgreSQL performance limits
- **Consider**: 
  - Partitioning strategy (by user_id range or date)
  - Archive strategy for old episodic memories
  - Read replicas for retrieval operations

### 6. **Memory Conflicts**
The PRD mentions "mark contradictions" but doesn't detail:
- How contradictions are detected
- How they're resolved (last-write-wins? confidence-based? user prompt?)
- UI/UX for conflict resolution

### 7. **Space Management**
The Space concept is powerful but could benefit from:
- Hierarchical spaces (e.g., `C3/backend`, `C3/frontend`)
- Space inheritance rules
- Default space selection logic

## Implementation Suggestions for Claude Code

### 1. **Start Minimal**
Begin with Phase 0 but even simpler:
- Just profile facts (no episodic yet)
- Manual storage only (no harvester)
- No RAG initially
- This proves the core memory injection works

### 2. **Test Data Generation**
Create a test harness that generates:
- Synthetic conversation histories
- Edge cases (contradictions, sensitive data, max-length texts)
- Performance test data (50k memories)

### 3. **Prompt Engineering Iteration**
Your prompts are good starting points, but you'll need:
- A/B testing framework for prompt variations
- Evaluation dataset for gate scoring accuracy
- Feedback loops to refine the normalizer prompts

### 4. **Database Migrations**
- Use a migration tool (Flyway, Alembic) from day 1
- Plan for zero-downtime migrations given the SLO requirements

### 5. **Security Implementation Order**
1. Start with basic auth + tenant isolation
2. Add audit logging
3. Then consent framework
4. Finally field-level encryption

## Critical Path Items

1. **Embedding Service**: Decide and implement early as everything depends on it
2. **PostgreSQL + pgvector**: Set up with proper indices immediately
3. **Gate Scoring Calibration**: This will need the most iteration
4. **Consent UI/UX**: Legal/compliance review needed before launch

## Missing Pieces to Consider

1. **Backup/Recovery Strategy** - How do users recover deleted memories?
2. **Multi-language Support** - How do embeddings/retrieval work across languages?
3. **Memory Sharing** - Can users share specific memories with others?
4. **Versioning** - How do you handle profile fact updates over time?

## Overall Assessment

This is one of the most comprehensive PRDs I've seen for an AI memory system. The attention to detail, especially around privacy and security, is exemplary. The STS (Spirit-Token-Space) metaphor provides a clean conceptual model.

The main risk is over-engineering initially. I'd recommend implementing a narrower slice first (just profile facts with manual storage) and validating the core value proposition before building the full harvester/compiler/RAG pipeline.

The document is essentially implementation-ready - an engineer could build this without many open questions, which is rare and valuable in a PRD.

Would you like me to help generate the ticket bundle for Jira/Linear, or would you prefer to discuss any specific aspect in more detail?

---
**HUMAN** (2025-08-23T08:22):

ok i like your implementations, and at the beginning, we don't need to make it very privacy and scale focused, we may consider implement a working bot first, then slowly adding RAG and other functionalities.
So the first stage, is to just have a chat interface(like openai gpt ui), build using react, tailwind, nextjs, postgress. to just making a working chatbot
please make sure we clearly state our intention to make this project scalable by grouping code by feature, not layer; enforce strict boundaries; expose stable interfaces; keep domain logic pure and side-effect free; compose via dependency injection; test contracts; prevent cycles; automate dependency checks; evolve through versioned contracts

please provide me a complete prd for claude code to plan on

---
**ASSISTANT** (2025-08-23T08:25):

 # PRD — Phase 1: Chat Interface Foundation for Logos-Companion

**Owner:** Yongxu Ren  
**Date:** 2025-08-23 (Asia/Bangkok)  
**Goal:** Build a production-quality chat interface with clean architecture that serves as the foundation for the full memory + RAG system. Focus on **feature-based modularity**, **strict boundaries**, and **evolutionary architecture**.

---

## 1. Executive Summary

Build a ChatGPT-like interface using React, Tailwind, Next.js, and PostgreSQL that:
1. Provides a working chat experience with streaming responses
2. Establishes the architectural foundation for future memory/RAG features
3. Enforces feature-based module boundaries from day one
4. Maintains pure domain logic with clear dependency injection

**NOT in Phase 1:** Memory persistence, RAG, user profiles, authentication (beyond basic session)

---

## 2. Architecture Principles

### 2.1 Core Principles
```
1. Group by Feature, Not Layer
   ❌ /components, /services, /models
   ✅ /features/chat, /features/conversation, /features/streaming

2. Strict Module Boundaries
   - Each feature exposes a public API contract
   - Internal implementation details are private
   - Cross-feature communication only through contracts

3. Pure Domain Logic
   - Business rules have zero framework dependencies
   - Side effects isolated to adapters
   - Domain models are POJOs/POTOs

4. Dependency Injection
   - Features declare their dependencies
   - Composition happens at app root
   - Easy to swap implementations

5. Contract-First Development
   - Define interfaces before implementations
   - Version all public APIs
   - Test against contracts, not implementations
```

### 2.2 Module Structure
```
/src
  /features
    /chat                    # Feature module
      /domain               # Pure business logic
        - models.ts         # Chat, Message types
        - services.ts       # ChatService interface
        - validators.ts     # Business rules
      /adapters            # Side effects
        - api.adapter.ts   # HTTP/WebSocket handling
        - db.adapter.ts    # PostgreSQL queries
        - ai.adapter.ts    # LLM integration
      /ui                  # React components
        /components
          - ChatWindow.tsx
          - MessageList.tsx
          - InputBar.tsx
        /hooks
          - useChat.ts
          - useStreaming.ts
      /contracts           # Public API
        - chat.contract.ts # Exposed interface
        - chat.types.ts    # Public types
      - index.ts          # Public exports only
      - module.ts         # Module registration
    
    /conversation          # Another feature
      /domain
      /adapters
      /ui
      /contracts
      - index.ts
      - module.ts
  
  /core                   # Shared kernel (minimal!)
    /types               # Truly shared types
    /utils               # Pure utility functions
    /errors              # Error base classes
  
  /infrastructure        # Framework setup
    /db                  # Database setup
    /config              # Env configuration
    /monitoring          # Logging, metrics
  
  /app                   # Next.js app directory
    - layout.tsx
    - page.tsx
    - api/              # API routes
```

---

## 3. Functional Requirements

### 3.1 Chat Interface
- **Send Message**: Text input with Enter/button submission
- **Streaming Response**: Character-by-character or chunk streaming
- **Message Display**: Sender-aligned bubbles with timestamps
- **Conversation Management**: New chat, clear history
- **Responsive Design**: Mobile-first, works on all devices

### 3.2 Conversation Persistence
- Store conversations in PostgreSQL
- Each conversation has unique ID
- Messages maintain order and timestamps
- Sessions persist across page refreshes

### 3.3 LLM Integration
- Stream responses from OpenAI/Anthropic API
- Handle rate limits gracefully
- Timeout handling (30s max)
- Error recovery with retry logic

### 3.4 Basic Session Management
- Session-based identification (no auth yet)
- Cookie/localStorage for session continuity
- Automatic session creation on first visit

---

## 4. Database Schema

```sql
-- Core schema for Phase 1
CREATE SCHEMA IF NOT EXISTS chat;

-- Conversations table
CREATE TABLE chat.conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id TEXT NOT NULL,
  title TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  metadata JSONB DEFAULT '{}'::jsonb
);

CREATE INDEX idx_conversations_session ON chat.conversations(session_id);
CREATE INDEX idx_conversations_updated ON chat.conversations(updated_at DESC);

-- Messages table
CREATE TABLE chat.messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  conversation_id UUID NOT NULL REFERENCES chat.conversations(id) ON DELETE CASCADE,
  role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  metadata JSONB DEFAULT '{}'::jsonb,
  -- Pre-allocate columns for future features
  embedding VECTOR(1536),  -- Future: for similarity search
  memory_refs UUID[],       -- Future: links to memory items
  rag_sources JSONB        -- Future: RAG source tracking
);

CREATE INDEX idx_messages_conversation ON chat.messages(conversation_id, created_at);

-- Stream states (for recovery)
CREATE TABLE chat.stream_states (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  message_id UUID NOT NULL REFERENCES chat.messages(id) ON DELETE CASCADE,
  state TEXT NOT NULL CHECK (state IN ('pending', 'streaming', 'complete', 'failed')),
  partial_content TEXT,
  error JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Future-proofing: Reserve schema namespaces
CREATE SCHEMA IF NOT EXISTS memory;  -- Phase 2
CREATE SCHEMA IF NOT EXISTS rag;     -- Phase 3
CREATE SCHEMA IF NOT EXISTS users;   -- Phase 4
```

---

## 5. Feature Contracts

### 5.1 Chat Feature Contract
```typescript
// /features/chat/contracts/chat.contract.ts

export interface ChatContract {
  // Commands
  sendMessage(params: SendMessageParams): Promise<Message>;
  streamMessage(params: StreamMessageParams): AsyncIterator<MessageChunk>;
  
  // Queries
  getConversation(id: ConversationId): Promise<Conversation>;
  listConversations(session: SessionId): Promise<Conversation[]>;
  
  // Events (for future event sourcing)
  events: {
    onMessageSent: EventEmitter<MessageSentEvent>;
    onStreamComplete: EventEmitter<StreamCompleteEvent>;
  };
}

export interface SendMessageParams {
  conversationId?: ConversationId;
  content: string;
  sessionId: SessionId;
}

export interface Message {
  id: MessageId;
  conversationId: ConversationId;
  role: 'user' | 'assistant';
  content: string;
  createdAt: Date;
}

// Version contract for future migration
export const CONTRACT_VERSION = '1.0.0';
```

### 5.2 Conversation Feature Contract
```typescript
// /features/conversation/contracts/conversation.contract.ts

export interface ConversationContract {
  create(params: CreateConversationParams): Promise<Conversation>;
  delete(id: ConversationId): Promise<void>;
  updateTitle(id: ConversationId, title: string): Promise<void>;
  
  // Future-ready: these will connect to memory system
  attachContext(id: ConversationId, context: unknown): Promise<void>;
  getContext(id: ConversationId): Promise<unknown>;
}
```

---

## 6. Module Registration & DI

```typescript
// /src/features/chat/module.ts

export class ChatModule implements FeatureModule {
  readonly name = 'chat';
  readonly version = '1.0.0';
  readonly contracts = [ChatContract];
  
  register(container: DIContainer): void {
    // Register implementations
    container.bind(ChatContract).to(ChatService);
    container.bind(ChatRepository).to(PostgresChatRepository);
    container.bind(AIProvider).to(OpenAIProvider);
    
    // Register adapters
    container.bind(ChatAPIAdapter).toSelf();
    container.bind(ChatStreamAdapter).toSelf();
  }
  
  async onStart(): Promise<void> {
    // Run migrations, health checks
  }
  
  dependencies(): string[] {
    return []; // No dependencies in Phase 1
  }
}

// /src/app.ts - Application root composition
export class Application {
  private modules: Map<string, FeatureModule> = new Map();
  
  async bootstrap() {
    // Register modules
    this.registerModule(new ChatModule());
    this.registerModule(new ConversationModule());
    
    // Future modules (commented for Phase 1)
    // this.registerModule(new MemoryModule());
    // this.registerModule(new RAGModule());
    
    // Check for circular dependencies
    this.validateDependencies();
    
    // Start modules in dependency order
    await this.startModules();
  }
}
```

---

## 7. API Routes

```typescript
// /app/api/chat/send/route.ts
export async function POST(request: Request) {
  const chat = container.get<ChatContract>(ChatContract);
  const body = await request.json();
  
  const message = await chat.sendMessage({
    conversationId: body.conversationId,
    content: body.content,
    sessionId: getSessionId(request),
  });
  
  return Response.json(message);
}

// /app/api/chat/stream/route.ts
export async function POST(request: Request) {
  const chat = container.get<ChatContract>(ChatContract);
  const body = await request.json();
  
  const stream = new ReadableStream({
    async start(controller) {
      for await (const chunk of chat.streamMessage(body)) {
        controller.enqueue(new TextEncoder().encode(
          `data: ${JSON.stringify(chunk)}\n\n`
        ));
      }
      controller.close();
    },
  });
  
  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}
```

---

## 8. UI Components Structure

```typescript
// /features/chat/ui/components/ChatWindow.tsx
export const ChatWindow: FC = () => {
  const { messages, sendMessage, isStreaming } = useChat();
  
  return (
    <div className="flex flex-col h-screen">
      <MessageList messages={messages} />
      <InputBar 
        onSend={sendMessage} 
        disabled={isStreaming}
      />
    </div>
  );
};

// /features/chat/ui/hooks/useChat.ts
export const useChat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const chatService = useService<ChatContract>(ChatContract);
  
  const sendMessage = async (content: string) => {
    // Add optimistic update
    const tempMessage = createOptimisticMessage(content);
    setMessages(prev => [...prev, tempMessage]);
    
    try {
      const response = await chatService.sendMessage({ content });
      // Handle streaming response
      for await (const chunk of chatService.streamMessage(...)) {
        updateStreamingMessage(chunk);
      }
    } catch (error) {
      handleError(error);
    }
  };
  
  return { messages, sendMessage, isStreaming };
};
```

---

## 9. Testing Strategy

### 9.1 Contract Testing
```typescript
// /features/chat/tests/chat.contract.test.ts
describe('ChatContract', () => {
  let implementation: ChatContract;
  
  beforeEach(() => {
    implementation = createTestImplementation();
  });
  
  contractTest(ChatContract, implementation);
});
```

### 9.2 Boundary Testing
```typescript
// /tools/dependency-check.ts
export function checkModuleBoundaries() {
  const violations = [];
  
  // Ensure no direct imports between features
  if (hasDirectImport('/features/chat', '/features/conversation')) {
    violations.push('Direct import between features detected');
  }
  
  // Ensure only contracts are exported
  if (exportsNonContractTypes('/features/chat/index.ts')) {
    violations.push('Non-contract types exported');
  }
  
  return violations;
}
```

---

## 10. Environment Configuration

```env
# .env.local
DATABASE_URL=postgresql://user:pass@localhost:5432/logos
OPENAI_API_KEY=sk-...
NEXT_PUBLIC_API_URL=http://localhost:3000

# Future flags (prepared but not used)
ENABLE_MEMORY=false
ENABLE_RAG=false
ENABLE_AUTH=false
```

---

## 11. Development Workflow

### 11.1 File Creation Order
```bash
# 1. Create domain models first (pure, no dependencies)
features/chat/domain/models.ts
features/chat/domain/validators.ts

# 2. Define contracts
features/chat/contracts/chat.contract.ts
features/chat/contracts/chat.types.ts

# 3. Implement adapters
features/chat/adapters/db.adapter.ts
features/chat/adapters/ai.adapter.ts

# 4. Create UI components
features/chat/ui/components/ChatWindow.tsx
features/chat/ui/hooks/useChat.ts

# 5. Wire up module
features/chat/module.ts
features/chat/index.ts

# 6. Add API routes
app/api/chat/send/route.ts
app/api/chat/stream/route.ts
```

### 11.2 Commands for Claude Code
```bash
# Initial setup
npx create-next-app@latest logos-companion --typescript --tailwind --app
cd logos-companion
npm install @prisma/client prisma zod inversify reflect-metadata
npm install @types/node tsx vitest @testing-library/react

# Database setup
npx prisma init
npx prisma migrate dev --name init

# Run boundary checks
npm run check:boundaries

# Run contract tests
npm run test:contracts
```

---

## 12. Migration Path to Full System

### Phase 1 → Phase 2 (Memory)
```typescript
// New module added without changing existing
export class MemoryModule implements FeatureModule {
  dependencies() { return ['chat']; }
  
  register(container: DIContainer) {
    // Extend ChatContract with memory injection
    container.decorate(ChatContract, withMemory);
  }
}
```

### Phase 2 → Phase 3 (RAG)
```typescript
// RAG module augments responses
export class RAGModule implements FeatureModule {
  dependencies() { return ['chat', 'memory']; }
  
  register(container: DIContainer) {
    // Intercept message sending to add RAG context
    container.decorate(ChatContract, withRAGContext);
  }
}
```

---

## 13. Success Criteria

### 13.1 Functional
- [ ] User can start a conversation
- [ ] Messages stream in real-time
- [ ] Conversations persist across refreshes
- [ ] Mobile responsive design works
- [ ] Error states handled gracefully

### 13.2 Architectural
- [ ] No direct imports between features
- [ ] All business logic is pure (no side effects)
- [ ] Contracts define all public APIs
- [ ] Dependency injection works
- [ ] Database migrations are versioned
- [ ] Module boundaries are enforced

### 13.3 Performance
- [ ] First message response < 500ms
- [ ] Streaming starts < 1s
- [ ] Page load < 2s
- [ ] No memory leaks during streaming

---

## 14. Non-Goals for Phase 1

Explicitly NOT doing:
- User authentication
- Memory persistence
- RAG functionality  
- Admin interface
- Analytics
- Rate limiting (beyond basic)
- Deployment/hosting setup

---

## 15. File Structure Example

```
logos-companion/
├── src/
│   ├── features/
│   │   ├── chat/
│   │   │   ├── domain/
│   │   │   │   ├── models.ts
│   │   │   │   ├── services.ts
│   │   │   │   └── validators.ts
│   │   │   ├── adapters/
│   │   │   │   ├── api.adapter.ts
│   │   │   │   ├── db.adapter.ts
│   │   │   │   └── ai.adapter.ts
│   │   │   ├── ui/
│   │   │   │   ├── components/
│   │   │   │   │   ├── ChatWindow.tsx
│   │   │   │   │   ├── MessageList.tsx
│   │   │   │   │   └── InputBar.tsx
│   │   │   │   └── hooks/
│   │   │   │       └── useChat.ts
│   │   │   ├── contracts/
│   │   │   │   ├── chat.contract.ts
│   │   │   │   └── chat.types.ts
│   │   │   ├── tests/
│   │   │   │   ├── chat.contract.test.ts
│   │   │   │   └── chat.integration.test.ts
│   │   │   ├── index.ts
│   │   │   └── module.ts
│   │   └── conversation/
│   │       └── ... (similar structure)
│   ├── core/
│   │   ├── types/
│   │   ├── utils/
│   │   └── errors/
│   ├── infrastructure/
│   │   ├── db/
│   │   ├── config/
│   │   └── monitoring/
│   └── app.ts
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── api/
│       └── chat/
│           ├── send/route.ts
│           └── stream/route.ts
├── prisma/
│   └── schema.prisma
├── tests/
│   └── boundaries/
│       └── module-boundaries.test.ts
├── tools/
│   ├── check-boundaries.ts
│   └── generate-module.ts
├── package.json
├── tsconfig.json
└── README.md
```

---

## Implementation Notes for Claude Code

When implementing this with Claude Code:

1. **Start with the domain models** - they have zero dependencies
2. **Create contracts before implementations** - this ensures clean boundaries
3. **Use dependency injection from the start** - easier than refactoring later
4. **Write a boundary check script early** - run it in CI
5. **Keep the module registry simple** - complexity can be added later
6. **Test contracts, not implementations** - allows swapping implementations

This architecture ensures that when we add Memory and RAG features, we won't need to refactor the chat foundation - we'll simply add new modules that enhance existing contracts through decoration/interception patterns.

---
**HUMAN** (2025-08-23T08:34):

ok good overall, but too complex for v1,let's not focus and implement things like Testing Strategy, but we do need oauth(like google login) for other people to use without exposing the bot without rate limiting
I think it would also be a good idea to create agent(chatbot) as a separate class I can use as a library that can be used independently, and in a separate folder that can be copy pasted and reused for later.
for what I am thinking, I think it would be a good idea to split the code base into /agent /frontend /backend, and we may add /mobile in the future.
also, the project is called A3 instead of logos-companion. you don't need to mention owner and date, make it as claude code plan friendly as possible

---
**ASSISTANT** (2025-08-23T08:36):

 # PRD — A3 Chat Application with OAuth

**Goal:** Build a ChatGPT-like interface with Google OAuth, using a reusable agent library that can be deployed across web, backend, and future mobile applications.

---

## 1. Project Structure

```
a3/
├── agent/                 # Reusable chatbot library
│   ├── src/
│   │   ├── index.ts      # Main Agent class export
│   │   ├── agent.ts      # Core Agent implementation
│   │   ├── types.ts      # Shared types
│   │   ├── providers/    # LLM providers (OpenAI, Anthropic)
│   │   └── utils/        # Helper functions
│   ├── package.json
│   └── tsconfig.json
│
├── backend/              # Next.js API + Database
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/[...nextauth]/route.ts
│   │   │   ├── chat/route.ts
│   │   │   └── conversations/route.ts
│   │   └── layout.tsx
│   ├── lib/
│   │   ├── auth.ts      # NextAuth config
│   │   ├── db.ts        # Database client
│   │   └── agent.ts     # Agent instance
│   ├── prisma/
│   │   └── schema.prisma
│   ├── package.json
│   └── .env.local
│
├── frontend/             # React UI
│   ├── app/
│   │   ├── page.tsx     # Chat interface
│   │   ├── layout.tsx   # Root layout with auth
│   │   └── login/page.tsx
│   ├── components/
│   │   ├── chat/
│   │   │   ├── ChatWindow.tsx
│   │   │   ├── MessageList.tsx
│   │   │   └── InputBar.tsx
│   │   └── auth/
│   │       └── LoginButton.tsx
│   ├── hooks/
│   │   ├── useChat.ts
│   │   └── useAuth.ts
│   ├── lib/
│   │   └── api-client.ts
│   └── package.json
│
├── package.json          # Root workspace
└── README.md
```

---

## 2. Agent Library (Reusable Core)

### 2.1 Agent Class Design

```typescript
// agent/src/agent.ts

export interface AgentConfig {
  provider: 'openai' | 'anthropic';
  apiKey: string;
  model?: string;
  temperature?: number;
  systemPrompt?: string;
  maxTokens?: number;
  streaming?: boolean;
}

export class Agent {
  private provider: AIProvider;
  private config: AgentConfig;

  constructor(config: AgentConfig) {
    this.config = config;
    this.provider = this.createProvider(config);
  }

  async chat(message: string, context?: ChatContext): Promise<string> {
    return this.provider.complete(message, context);
  }

  async *stream(message: string, context?: ChatContext): AsyncGenerator<string> {
    yield* this.provider.stream(message, context);
  }

  async validateConfig(): Promise<boolean> {
    return this.provider.validateConnection();
  }

  // Future-ready methods
  async attachMemory(memory: unknown): Promise<void> {
    // Placeholder for memory system
  }

  async attachRAG(documents: unknown[]): Promise<void> {
    // Placeholder for RAG system
  }
}
```

### 2.2 Provider Interface

```typescript
// agent/src/providers/base.ts

export interface ChatContext {
  conversationId?: string;
  history?: Message[];
  metadata?: Record<string, any>;
}

export interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
}

export abstract class AIProvider {
  abstract complete(message: string, context?: ChatContext): Promise<string>;
  abstract stream(message: string, context?: ChatContext): AsyncGenerator<string>;
  abstract validateConnection(): Promise<boolean>;
}
```

### 2.3 OpenAI Provider Implementation

```typescript
// agent/src/providers/openai.ts

import OpenAI from 'openai';

export class OpenAIProvider extends AIProvider {
  private client: OpenAI;
  private model: string;

  constructor(apiKey: string, model = 'gpt-4-turbo-preview') {
    this.client = new OpenAI({ apiKey });
    this.model = model;
  }

  async complete(message: string, context?: ChatContext): Promise<string> {
    const messages = this.buildMessages(message, context);
    const response = await this.client.chat.completions.create({
      model: this.model,
      messages,
    });
    return response.choices[0].message.content || '';
  }

  async *stream(message: string, context?: ChatContext): AsyncGenerator<string> {
    const messages = this.buildMessages(message, context);
    const stream = await this.client.chat.completions.create({
      model: this.model,
      messages,
      stream: true,
    });

    for await (const chunk of stream) {
      yield chunk.choices[0]?.delta?.content || '';
    }
  }

  private buildMessages(message: string, context?: ChatContext): Message[] {
    const messages: Message[] = [];
    
    if (context?.history) {
      messages.push(...context.history);
    }
    
    messages.push({ role: 'user', content: message });
    return messages;
  }

  async validateConnection(): Promise<boolean> {
    try {
      await this.client.models.list();
      return true;
    } catch {
      return false;
    }
  }
}
```

### 2.4 Agent Package.json

```json
{
  "name": "@a3/agent",
  "version": "1.0.0",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch"
  },
  "dependencies": {
    "openai": "^4.28.0",
    "@anthropic-ai/sdk": "^0.20.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "@types/node": "^20.0.0"
  }
}
```

---

## 3. Backend (Next.js + Auth + Database)

### 3.1 Database Schema

```prisma
// backend/prisma/schema.prisma

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id            String         @id @default(cuid())
  email         String         @unique
  name          String?
  image         String?
  createdAt     DateTime       @default(now())
  updatedAt     DateTime       @updatedAt
  conversations Conversation[]
  accounts      Account[]
  sessions      Session[]
}

model Account {
  id                String  @id @default(cuid())
  userId            String
  type              String
  provider          String
  providerAccountId String
  refresh_token     String?
  access_token      String?
  expires_at        Int?
  token_type        String?
  scope             String?
  id_token          String?
  session_state     String?
  user              User    @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([provider, providerAccountId])
}

model Session {
  id           String   @id @default(cuid())
  sessionToken String   @unique
  userId       String
  expires      DateTime
  user         User     @relation(fields: [userId], references: [id], onDelete: Cascade)
}

model Conversation {
  id        String    @id @default(cuid())
  userId    String
  title     String?
  createdAt DateTime  @default(now())
  updatedAt DateTime  @updatedAt
  user      User      @relation(fields: [userId], references: [id], onDelete: Cascade)
  messages  Message[]
}

model Message {
  id             String       @id @default(cuid())
  conversationId String
  role           String       // 'user' | 'assistant'
  content        String
  createdAt      DateTime     @default(now())
  conversation   Conversation @relation(fields: [conversationId], references: [id], onDelete: Cascade)
  
  @@index([conversationId, createdAt])
}
```

### 3.2 NextAuth Configuration

```typescript
// backend/lib/auth.ts

import { NextAuthOptions } from "next-auth";
import GoogleProvider from "next-auth/providers/google";
import { PrismaAdapter } from "@auth/prisma-adapter";
import { prisma } from "./db";

export const authOptions: NextAuthOptions = {
  adapter: PrismaAdapter(prisma),
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
  ],
  callbacks: {
    session: async ({ session, token }) => {
      if (session?.user && token?.sub) {
        session.user.id = token.sub;
      }
      return session;
    },
  },
  pages: {
    signIn: '/login',
  },
};
```

### 3.3 Chat API Route

```typescript
// backend/app/api/chat/route.ts

import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { Agent } from "@a3/agent";

const agent = new Agent({
  provider: 'openai',
  apiKey: process.env.OPENAI_API_KEY!,
  model: 'gpt-4-turbo-preview',
  streaming: true,
});

export async function POST(req: Request) {
  const session = await getServerSession(authOptions);
  
  if (!session?.user?.id) {
    return new Response("Unauthorized", { status: 401 });
  }

  const { message, conversationId } = await req.json();

  // Get or create conversation
  let conversation;
  if (conversationId) {
    conversation = await prisma.conversation.findUnique({
      where: { id: conversationId, userId: session.user.id },
      include: { messages: { orderBy: { createdAt: 'asc' } } },
    });
  } else {
    conversation = await prisma.conversation.create({
      data: {
        userId: session.user.id,
        title: message.slice(0, 50),
      },
    });
  }

  if (!conversation) {
    return new Response("Conversation not found", { status: 404 });
  }

  // Save user message
  await prisma.message.create({
    data: {
      conversationId: conversation.id,
      role: 'user',
      content: message,
    },
  });

  // Stream response
  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    async start(controller) {
      let fullResponse = '';
      
      try {
        const context = {
          conversationId: conversation.id,
          history: conversation.messages?.map(m => ({
            role: m.role as 'user' | 'assistant',
            content: m.content,
          })),
        };

        for await (const chunk of agent.stream(message, context)) {
          fullResponse += chunk;
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ chunk })}\n\n`));
        }

        // Save assistant message
        await prisma.message.create({
          data: {
            conversationId: conversation.id,
            role: 'assistant',
            content: fullResponse,
          },
        });

        controller.enqueue(encoder.encode(`data: [DONE]\n\n`));
      } catch (error) {
        controller.enqueue(encoder.encode(`data: ${JSON.stringify({ error: 'Failed to generate response' })}\n\n`));
      } finally {
        controller.close();
      }
    },
  });

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}
```

### 3.4 Environment Variables

```bash
# backend/.env.local

DATABASE_URL="postgresql://user:password@localhost:5432/a3"
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="generate-random-secret-here"

GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"

OPENAI_API_KEY="sk-..."
```

---

## 4. Frontend (React UI)

### 4.1 Main Chat Interface

```typescript
// frontend/app/page.tsx

'use client';

import { useSession } from 'next-auth/react';
import { redirect } from 'next/navigation';
import ChatWindow from '@/components/chat/ChatWindow';

export default function HomePage() {
  const { data: session, status } = useSession();

  if (status === 'loading') {
    return <div>Loading...</div>;
  }

  if (!session) {
    redirect('/login');
  }

  return (
    <div className="h-screen flex flex-col">
      <header className="border-b p-4 flex justify-between items-center">
        <h1 className="text-xl font-bold">A3 Chat</h1>
        <div className="flex items-center gap-4">
          <span>{session.user?.email}</span>
          <button 
            onClick={() => signOut()}
            className="px-4 py-2 bg-red-500 text-white rounded"
          >
            Sign Out
          </button>
        </div>
      </header>
      <ChatWindow />
    </div>
  );
}
```

### 4.2 Chat Components

```typescript
// frontend/components/chat/ChatWindow.tsx

import { useState } from 'react';
import MessageList from './MessageList';
import InputBar from './InputBar';
import { useChat } from '@/hooks/useChat';

export default function ChatWindow() {
  const { messages, sendMessage, isStreaming, currentConversation } = useChat();

  return (
    <div className="flex-1 flex flex-col">
      <MessageList messages={messages} isStreaming={isStreaming} />
      <InputBar onSend={sendMessage} disabled={isStreaming} />
    </div>
  );
}
```

```typescript
// frontend/components/chat/MessageList.tsx

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export default function MessageList({ 
  messages, 
  isStreaming 
}: { 
  messages: Message[], 
  isStreaming: boolean 
}) {
  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.map((message, index) => (
        <div
          key={index}
          className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
        >
          <div
            className={`max-w-2xl px-4 py-2 rounded-lg ${
              message.role === 'user'
                ? 'bg-blue-500 text-white'
                : 'bg-gray-200 text-gray-900'
            }`}
          >
            {message.content}
          </div>
        </div>
      ))}
      {isStreaming && (
        <div className="flex justify-start">
          <div className="bg-gray-200 text-gray-900 px-4 py-2 rounded-lg">
            <span className="animate-pulse">...</span>
          </div>
        </div>
      )}
    </div>
  );
}
```

### 4.3 Chat Hook

```typescript
// frontend/hooks/useChat.ts

import { useState, useCallback } from 'react';

export function useChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);

  const sendMessage = useCallback(async (content: string) => {
    // Add user message optimistically
    setMessages(prev => [...prev, { role: 'user', content }]);
    setIsStreaming(true);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: content, conversationId }),
      });

      if (!response.ok) throw new Error('Failed to send message');

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();
      let assistantMessage = '';

      while (reader) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') continue;
            
            try {
              const parsed = JSON.parse(data);
              if (parsed.chunk) {
                assistantMessage += parsed.chunk;
                setMessages(prev => {
                  const newMessages = [...prev];
                  if (newMessages[newMessages.length - 1]?.role === 'assistant') {
                    newMessages[newMessages.length - 1].content = assistantMessage;
                  } else {
                    newMessages.push({ role: 'assistant', content: assistantMessage });
                  }
                  return newMessages;
                });
              }
            } catch (e) {
              console.error('Failed to parse chunk:', e);
            }
          }
        }
      }
    } catch (error) {
      console.error('Chat error:', error);
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Sorry, I encountered an error. Please try again.' 
      }]);
    } finally {
      setIsStreaming(false);
    }
  }, [conversationId]);

  return {
    messages,
    sendMessage,
    isStreaming,
    currentConversation: conversationId,
  };
}
```

### 4.4 Login Page

```typescript
// frontend/app/login/page.tsx

'use client';

import { signIn } from 'next-auth/react';

export default function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <h2 className="text-3xl font-bold">Welcome to A3</h2>
          <p className="mt-2 text-gray-600">Sign in to start chatting</p>
        </div>
        <button
          onClick={() => signIn('google', { callbackUrl: '/' })}
          className="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
        >
          Sign in with Google
        </button>
      </div>
    </div>
  );
}
```

---

## 5. Development Commands

```bash
# Initial setup
mkdir a3 && cd a3

# Setup workspaces
npm init -y
npm pkg set workspaces='["agent", "backend", "frontend"]'

# Agent library setup
mkdir agent && cd agent
npm init -y
npm install openai @anthropic-ai/sdk
npm install -D typescript @types/node
cd ..

# Backend setup
npx create-next-app@latest backend --typescript --tailwind --app
cd backend
npm install @prisma/client prisma next-auth @auth/prisma-adapter
npm install -D @types/node
npx prisma init
# Add schema from above
npx prisma generate
npx prisma db push
cd ..

# Frontend setup  
npx create-next-app@latest frontend --typescript --tailwind --app
cd frontend
npm install next-auth
cd ..

# Run everything
npm install
npm run dev # (setup scripts in root package.json to run all)
```

---

## 6. Deployment Considerations

### 6.1 Environment Setup
- Set up Google OAuth application in Google Cloud Console
- Configure redirect URLs for production domain
- Set secure session secrets

### 6.2 Database
- Use managed PostgreSQL (Supabase, Neon, or Railway)
- Enable connection pooling for serverless

### 6.3 Hosting
- Deploy backend to Vercel (automatic with Next.js)
- Set environment variables in Vercel dashboard
- Configure custom domain

---

## 7. Future Extensibility

### 7.1 Adding Memory (Phase 2)
```typescript
// Simply extend the Agent class
class MemoryAgent extends Agent {
  private memory: MemoryStore;
  
  async chat(message: string, context?: ChatContext): Promise<string> {
    const enrichedContext = await this.memory.enrich(context);
    return super.chat(message, enrichedContext);
  }
}
```

### 7.2 Adding Mobile (Future)
```typescript
// mobile/src/services/agent.ts
import { Agent } from '@a3/agent';

// Same agent library works in React Native
const agent = new Agent(config);
```

This structure keeps the agent logic completely separate and reusable, while providing a working authenticated chat application that's ready for production use.

---
**HUMAN** (2025-08-23T08:42):

this is good but the requirement and features are not stated very clearly except the code, we need to create that not only explain what to do but how, and what tech stack to use. please ultrathink about this

---
**ASSISTANT** (2025-08-23T08:44):

 <thinking>
The user is right - I provided a lot of code examples but didn't clearly state the requirements, features, and implementation approach in a structured way. They want a PRD that Claude Code can follow step-by-step, with clear requirements, tech stack choices, and implementation instructions.

Let me think about what makes a good PRD for Claude Code:
1. Clear statement of what we're building
2. Explicit feature list with acceptance criteria
3. Tech stack with reasoning
4. Step-by-step implementation plan
5. File structure and architecture decisions
6. Data flow and API design
7. Security and auth flow
8. Clear instructions on HOW to implement each part

The user wants:
- Google OAuth for authentication
- Reusable agent library
- Three-part architecture: /agent, /frontend, /backend
- Future mobile support
- Simple v1 without complex testing
- Rate limiting through auth (not exposing bot publicly)

Let me restructure this to be more instructional and clear about requirements.
</thinking>

# A3 Chat Application - Implementation PRD

## 1. Project Overview

### What We're Building
A production-ready AI chat application with:
- **Google OAuth authentication** to prevent unauthorized access
- **Real-time streaming chat** with conversation history
- **Modular architecture** with a reusable agent library
- **Three separate packages** that can be deployed and scaled independently

### Core Requirements
1. **Authentication Required**: Users must sign in with Google before accessing chat
2. **Persistent Conversations**: All chats saved to PostgreSQL database
3. **Streaming Responses**: Real-time token streaming from AI
4. **Reusable Agent**: Core chat logic in a separate package for future reuse
5. **Session Management**: Each user has isolated conversations
6. **Responsive UI**: Works on desktop and mobile browsers

### Non-Requirements (v1)
- No memory system
- No RAG/document upload
- No user settings/preferences
- No conversation sharing
- No API rate limiting (auth serves as gate)
- No unit tests

---

## 2. Technical Architecture

### 2.1 Tech Stack Decisions

| Component | Technology | Why |
|-----------|------------|-----|
| **Agent Library** | TypeScript, Node.js | Portable, can run anywhere |
| **Backend** | Next.js 14 App Router | Full-stack framework, API routes, SSR |
| **Database** | PostgreSQL + Prisma | Type-safe ORM, migrations, relations |
| **Authentication** | NextAuth.js v5 | Industry standard, Google OAuth built-in |
| **Frontend** | Next.js + React + Tailwind | Same framework as backend, can be separated later |
| **AI Provider** | OpenAI API | Best streaming support, gpt-4-turbo |
| **Deployment** | Vercel | Zero-config Next.js hosting |
| **Database Host** | Supabase/Neon | Serverless Postgres, connection pooling |

### 2.2 Package Structure

```
a3/
├── packages/
│   ├── agent/          # Standalone NPM package
│   ├── backend/        # Next.js API + Auth
│   └── frontend/       # Next.js UI (initially in backend, can split later)
├── package.json        # Monorepo root
└── turbo.json         # Turborepo config
```

### 2.3 Data Flow

```mermaid
sequenceDiagram
    User->>Frontend: Opens app
    Frontend->>Backend: Check session
    Backend->>Google: Redirect to OAuth
    Google->>Backend: Auth callback
    Backend->>Database: Create/update user
    Backend->>Frontend: Session cookie
    User->>Frontend: Send message
    Frontend->>Backend: POST /api/chat
    Backend->>Database: Save user message
    Backend->>Agent: Process message
    Agent->>OpenAI: Stream completion
    OpenAI->>Agent: Token stream
    Agent->>Backend: Token stream
    Backend->>Frontend: SSE stream
    Backend->>Database: Save AI response
    Frontend->>User: Display streaming response
```

---

## 3. Feature Specifications

### 3.1 Authentication Flow

**Feature**: Google OAuth Login  
**Acceptance Criteria**:
- [ ] Unauthenticated users see login page
- [ ] Click "Sign in with Google" redirects to Google
- [ ] After auth, redirect to chat interface
- [ ] Session persists across browser refreshes
- [ ] Sign out button clears session

**Implementation**:
```typescript
// What NextAuth handles for us:
1. OAuth flow with Google
2. Session management via JWT/cookies  
3. Database user creation
4. CSRF protection
```

### 3.2 Chat Interface

**Feature**: Message Exchange  
**Acceptance Criteria**:
- [ ] Text input at bottom of screen
- [ ] Enter key sends message
- [ ] User messages appear on right, blue background
- [ ] AI messages appear on left, gray background
- [ ] Loading indicator during streaming
- [ ] Auto-scroll to bottom on new messages

**Implementation Details**:
- Use Server-Sent Events (SSE) for streaming
- Optimistic UI updates for user messages
- Abort controller for canceling requests

### 3.3 Conversation Management

**Feature**: Persistent Chat History  
**Acceptance Criteria**:
- [ ] New conversation starts automatically
- [ ] All messages saved to database
- [ ] Refresh page maintains conversation
- [ ] Conversation list in sidebar
- [ ] Click conversation to load history

**Database Operations**:
```sql
-- On new chat: INSERT conversation
-- On message: INSERT message with conversation_id
-- On load: SELECT messages WHERE conversation_id ORDER BY created_at
```

---

## 4. Implementation Plan

### Phase 1: Agent Library (Standalone Package)

**Goal**: Create reusable chat agent that handles AI interactions

**Files to Create**:
```
packages/agent/
├── src/
│   ├── index.ts         # Export Agent class
│   ├── agent.ts         # Main Agent implementation
│   ├── types.ts         # Message, Config types
│   └── providers/
│       ├── base.ts      # Abstract provider
│       └── openai.ts    # OpenAI implementation
├── package.json
└── tsconfig.json
```

**Implementation Steps**:

1. **Create Agent Class**:
```typescript
// Core responsibilities:
- Initialize with API credentials
- Manage conversation context
- Handle streaming/non-streaming modes
- Abstract provider interface
```

2. **Provider Pattern**:
```typescript
// Why: Swap between OpenAI/Anthropic/Local models
- BaseProvider abstract class
- OpenAIProvider with streaming
- Error handling and retries
```

3. **Export Clean API**:
```typescript
// Public API:
new Agent(config)
agent.chat(message, context)
agent.stream(message, context)
```

### Phase 2: Backend with Database

**Goal**: API routes, authentication, database persistence

**Files to Create**:
```
packages/backend/
├── app/
│   ├── api/
│   │   ├── auth/[...nextauth]/route.ts
│   │   ├── chat/route.ts
│   │   └── conversations/route.ts
│   └── (auth)/
│       ├── layout.tsx   # Auth wrapper
│       └── chat/page.tsx
├── lib/
│   ├── auth.ts         # NextAuth config
│   ├── db.ts           # Prisma client
│   └── agent.ts        # Agent instance
├── prisma/
│   └── schema.prisma
└── middleware.ts       # Auth middleware
```

**Implementation Steps**:

1. **Setup Database**:
```bash
# Commands to run:
npx prisma init
# Add schema (provided below)
npx prisma generate
npx prisma db push
```

2. **Configure NextAuth**:
```typescript
// Key tasks:
- Google OAuth provider setup
- Prisma adapter for user storage
- Session strategy (JWT or database)
- Middleware to protect routes
```

3. **Create Chat Endpoint**:
```typescript
// POST /api/chat responsibilities:
1. Verify authentication
2. Get/create conversation
3. Save user message
4. Stream from agent
5. Save AI response
6. Handle errors
```

4. **Streaming Implementation**:
```typescript
// Use ReadableStream + TextEncoder
// Format: Server-Sent Events (SSE)
// Send chunks as: data: {"chunk": "text"}\n\n
// End with: data: [DONE]\n\n
```

### Phase 3: Frontend UI

**Goal**: React components for chat interface

**Files to Create**:
```
packages/backend/components/
├── chat/
│   ├── ChatWindow.tsx
│   ├── MessageList.tsx
│   ├── MessageBubble.tsx
│   └── InputBar.tsx
├── auth/
│   └── UserMenu.tsx
└── layout/
    └── Sidebar.tsx

packages/backend/hooks/
├── useChat.ts          # Main chat logic
├── useAuth.ts          # Auth state
└── useConversations.ts # Conversation list
```

**Implementation Steps**:

1. **Chat Hook Architecture**:
```typescript
// useChat responsibilities:
- Manage message state
- Handle SSE streaming
- Parse streaming chunks
- Update UI optimistically
- Error handling
```

2. **Streaming UI Updates**:
```typescript
// Approach:
1. Add user message immediately
2. Add empty assistant message
3. Update last message as chunks arrive
4. Replace with final message
```

3. **Component Hierarchy**:
```
App
├── AuthCheck (redirect if not logged in)
├── Layout (header + sidebar)
│   ├── Sidebar (conversation list)
│   └── MainContent
│       ├── ChatWindow
│       │   ├── MessageList
│       │   │   └── MessageBubble[]
│       │   └── InputBar
│       └── EmptyState (no conversation)
```

---

## 5. Database Design

### Schema Definition

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

// NextAuth required tables
model User {
  id            String         @id @default(cuid())
  email         String         @unique
  name          String?
  image         String?
  createdAt     DateTime       @default(now())
  conversations Conversation[]
  accounts      Account[]      // OAuth accounts
  sessions      Session[]      // Active sessions
}

model Account {
  // NextAuth OAuth account info
  id                String  @id @default(cuid())
  userId            String
  type              String
  provider          String
  providerAccountId String
  refresh_token     String? @db.Text
  access_token      String? @db.Text
  expires_at        Int?
  user              User    @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([provider, providerAccountId])
}

model Session {
  // NextAuth session management
  id           String   @id @default(cuid())
  sessionToken String   @unique
  userId       String
  expires      DateTime
  user         User     @relation(fields: [userId], references: [id], onDelete: Cascade)
}

// Our application tables
model Conversation {
  id        String    @id @default(cuid())
  userId    String
  title     String?   // Auto-generated from first message
  createdAt DateTime  @default(now())
  updatedAt DateTime  @updatedAt
  user      User      @relation(fields: [userId], references: [id])
  messages  Message[]
  
  @@index([userId, updatedAt])
}

model Message {
  id             String       @id @default(cuid())
  conversationId String
  role           String       // 'user' | 'assistant' | 'system'
  content        String       @db.Text
  createdAt      DateTime     @default(now())
  conversation   Conversation @relation(fields: [conversationId], references: [id], onDelete: Cascade)
  
  // Reserved for future use
  metadata       Json?        // For storing token counts, model used, etc.
  embedding      Float[]?     // For future semantic search
  
  @@index([conversationId, createdAt])
}
```

---

## 6. API Design

### 6.1 Endpoints

| Method | Path | Purpose | Auth Required |
|--------|------|---------|---------------|
| GET | /api/auth/session | Get current user | No |
| POST | /api/auth/signout | Sign out | Yes |
| GET | /api/conversations | List user's conversations | Yes |
| GET | /api/conversations/:id | Get single conversation | Yes |
| DELETE | /api/conversations/:id | Delete conversation | Yes |
| POST | /api/chat | Send message & stream response | Yes |

### 6.2 Chat Endpoint Detail

**Request**:
```typescript
POST /api/chat
Headers: {
  Cookie: "next-auth.session-token=..."
  Content-Type: "application/json"
}
Body: {
  message: string
  conversationId?: string  // Optional, creates new if not provided
}
```

**Response** (Server-Sent Events):
```
HTTP/1.1 200 OK
Content-Type: text/event-stream

data: {"chunk": "Hello"}\n\n
data: {"chunk": " there"}\n\n
data: {"chunk": "!"}\n\n
data: {"conversationId": "abc123"}\n\n
data: [DONE]\n\n
```

---

## 7. Security Considerations

### 7.1 Authentication
- **Google OAuth only**: No password management needed
- **Session validation**: Check on every API request
- **CSRF protection**: Built into NextAuth

### 7.2 Data Isolation
- **User scoping**: All queries filtered by userId
- **SQL injection prevention**: Prisma parameterized queries
- **No public endpoints**: Everything requires auth

### 7.3 Rate Limiting
- **Natural limiting**: Auth requirement prevents anonymous abuse
- **Future consideration**: Add per-user rate limits if needed

---

## 8. Environment Configuration

### Required Environment Variables

```bash
# .env.local (backend)

# Database
DATABASE_URL="postgresql://user:pass@host:5432/a3"

# NextAuth
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="<generate-random-32-char-string>"

# Google OAuth
GOOGLE_CLIENT_ID="<from-google-cloud-console>"
GOOGLE_CLIENT_SECRET="<from-google-cloud-console>"

# OpenAI
OPENAI_API_KEY="sk-..."
OPENAI_MODEL="gpt-4-turbo-preview"  # Optional, defaults in code
```

---

## 9. Step-by-Step Implementation Guide

### Step 1: Initialize Monorepo
```bash
mkdir a3 && cd a3
npm init -y
npm install -D turbo
```

### Step 2: Create Agent Package
```bash
mkdir -p packages/agent/src
cd packages/agent
npm init -y
npm install openai
npm install -D typescript @types/node
# Create files as specified above
npm run build
cd ../..
```

### Step 3: Create Backend with Auth
```bash
cd packages
npx create-next-app@latest backend --typescript --tailwind --app --no-src-dir
cd backend
npm install @prisma/client prisma
npm install next-auth @auth/prisma-adapter
npm install ../agent  # Link local agent package
# Setup Prisma schema
npx prisma generate
npx prisma db push
cd ../..
```

### Step 4: Implement Chat API
1. Create auth configuration
2. Add API route with streaming
3. Test with curl/Postman

### Step 5: Build Frontend Components
1. Create layout with auth check
2. Build chat components
3. Implement streaming hook
4. Add conversation sidebar

### Step 6: Testing & Deployment
1. Test auth flow
2. Test message streaming
3. Test conversation persistence
4. Deploy to Vercel

---

## 10. Success Metrics

### Functional Requirements Met
- [ ] User can sign in with Google
- [ ] User can send messages
- [ ] AI responds with streaming
- [ ] Conversations persist
- [ ] Multiple conversations supported
- [ ] Sign out works

### Technical Requirements Met
- [ ] Agent library is standalone
- [ ] Backend handles auth + API
- [ ] Frontend could be separated
- [ ] Database stores all data
- [ ] Streaming works smoothly
- [ ] No public access without auth

---

## 11. Future Extensibility Plan

### Phase 2: Memory System
- Extend Agent class with memory store
- Add memory tables to database
- Inject memory context into prompts

### Phase 3: RAG System  
- Add document upload to UI
- Vector database for embeddings
- Retrieval pipeline in Agent

### Phase 4: Mobile App
- React Native app in packages/mobile
- Reuse Agent library directly
- Same API endpoints

This modular architecture ensures each piece can evolve independently while maintaining clean interfaces between components.

---
**HUMAN** (2025-08-23T08:46):

ok no Supabase/Neon, agent/ backend/ frontend/ under the root, make chat ui openai like, that user can retrive past conversations
think ultrahard!

---
**ASSISTANT** (2025-08-23T08:51):

The user wants:
1. No Supabase/Neon - so we'll use local PostgreSQL
2. Directory structure: agent/, backend/, frontend/ directly under root (not packages/)
3. Chat UI that looks like OpenAI's ChatGPT interface
4. Users can retrieve past conversations (like ChatGPT's conversation history sidebar)

Key requirements:
- Google OAuth for authentication
- Streaming chat responses
- Conversation history with sidebar
- OpenAI-like UI design
- Reusable agent library
- Clear implementation instructions

Let me think about the OpenAI ChatGPT UI:
- Left sidebar with conversation list
- New chat button at top
- Conversation titles (auto-generated from first message)
- Main chat area in center
- Message bubbles (user on right, AI on left)
- Text input at bottom with send button
- Dark/light mode (optional for v1)
- Responsive - sidebar collapses on mobile

I need to be very specific about:
1. Exact UI layout and styling
2. How to implement the conversation retrieval
3. Database queries for conversation list
4. Auto-titling conversations
5. Switching between conversations
6. Creating new conversations

Let me structure this PRD to be ultra-clear for Claude Code to implement.# A3 Chat Application - Implementation PRD

## 1. Project Overview

### What We're Building
An OpenAI ChatGPT clone with:
- **Exact ChatGPT UI/UX**: Left sidebar with conversations, center chat area
- **Google OAuth**: Required authentication before access
- **Streaming responses**: Real-time token-by-token streaming
- **Conversation history**: All past chats accessible from sidebar
- **Reusable agent library**: Core AI logic separated for future reuse

### Core Features
1. **Conversation Sidebar** (left): List of all past conversations with auto-generated titles
2. **New Chat Button**: Starts fresh conversation
3. **Chat Area** (center): Messages with user/assistant distinction
4. **Message Input** (bottom): Textarea with send button
5. **User Menu** (top right): Shows user email and sign out
6. **Responsive Design**: Sidebar collapses to hamburger menu on mobile

---

## 2. Directory Structure

```
a3/
├── agent/                      # Reusable AI library
│   ├── src/
│   │   ├── index.ts           # Exports: Agent class
│   │   ├── agent.ts           # Core Agent implementation
│   │   ├── types.ts           # TypeScript interfaces
│   │   └── providers/
│   │       ├── base.ts        # Abstract provider class
│   │       └── openai.ts      # OpenAI implementation
│   ├── package.json
│   └── tsconfig.json
│
├── backend/                    # Next.js API + Auth
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/[...nextauth]/route.ts
│   │   │   ├── chat/route.ts
│   │   │   ├── conversations/
│   │   │   │   ├── route.ts  # GET all, POST new
│   │   │   │   └── [id]/route.ts # GET one, DELETE
│   │   └── layout.tsx
│   ├── lib/
│   │   ├── auth.ts           # NextAuth configuration
│   │   ├── db.ts             # Prisma client singleton
│   │   └── agent-instance.ts # Singleton Agent
│   ├── prisma/
│   │   └── schema.prisma
│   └── package.json
│
├── frontend/                   # Next.js UI (ChatGPT clone)
│   ├── app/
│   │   ├── page.tsx          # Redirect to /chat
│   │   ├── layout.tsx        # Root layout with auth
│   │   ├── login/
│   │   │   └── page.tsx      # Google sign-in page
│   │   └── chat/
│   │       ├── page.tsx      # Main chat interface
│   │       └── [id]/page.tsx # Specific conversation
│   ├── components/
│   │   ├── Sidebar.tsx       # Conversation list
│   │   ├── ChatArea.tsx      # Messages + input
│   │   ├── MessageList.tsx   # Scrollable messages
│   │   ├── MessageInput.tsx  # Textarea + button
│   │   └── UserMenu.tsx      # Profile dropdown
│   ├── hooks/
│   │   ├── useChat.ts        # Chat state management
│   │   ├── useConversations.ts # Sidebar state
│   │   └── useStreaming.ts  # SSE handling
│   ├── lib/
│   │   └── api.ts            # API client functions
│   └── package.json
│
├── docker-compose.yml         # Local PostgreSQL
└── README.md
```

---

## 3. UI Specification (ChatGPT Clone)

### 3.1 Layout Structure

```
┌─────────────────────────────────────────────────────────┐
│  Sidebar (260px)    │         Main Chat Area            │
├─────────────────────┼─────────────────────────────────┤
│ [+ New Chat]        │  Top Bar                          │
│                     │  ┌─────────────────────────────┐ │
│ Yesterday           │  │ A3 Chat          [UserMenu] │ │
│ ▸ How to use React │  └─────────────────────────────┘ │
│ ▸ Python loops...  │                                   │
│                     │  Messages Area                    │
│ Previous 7 Days     │  ┌─────────────────────────────┐ │
│ ▸ Database design  │  │                             │ │
│ ▸ JWT vs sessions  │  │  AI: Hello! How can I      │ │
│                     │  │      help you today?        │ │
│ Previous 30 Days    │  │                             │ │
│ ▸ GraphQL basics   │  │           You: Tell me      │ │
│                     │  │           about TypeScript  │ │
│                     │  │                             │ │
│                     │  │  AI: TypeScript is...      │ │
│                     │  │      [streaming...]         │ │
│                     │  └─────────────────────────────┘ │
│                     │                                   │
│                     │  Input Area                       │
│                     │  ┌─────────────────────────────┐ │
│ [Sign Out]          │  │ Message A3...    [Send]     │ │
│                     │  └─────────────────────────────┘ │
└─────────────────────┴─────────────────────────────────┘
```

### 3.2 Component Specifications

#### Sidebar (260px fixed width)
```typescript
// Visual specs:
- Background: gray-900 (dark) or white (light)
- Padding: 8px
- New Chat button: Full width, primary color
- Conversation groups: "Today", "Yesterday", "Previous 7 Days", etc.
- Each conversation: Truncated title, hover effect
- Active conversation: Highlighted background
- Bottom: User email and sign out
```

#### Chat Area
```typescript
// Visual specs:
- Max width: 768px, centered
- Padding: 24px
- Messages: Alternating alignment (user right, AI left)
- User messages: Dark background, white text
- AI messages: Light gray background, dark text
- Streaming: Show cursor animation "▊"
```

#### Message Input
```typescript
// Visual specs:
- Textarea: Auto-resize, max 200px height
- Send button: Disabled while streaming
- Keyboard: Enter sends, Shift+Enter new line
```

---

## 4. Database Schema

```prisma
// backend/prisma/schema.prisma

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id            String         @id @default(cuid())
  email         String         @unique
  name          String?
  image         String?
  createdAt     DateTime       @default(now())
  updatedAt     DateTime       @updatedAt
  conversations Conversation[]
  accounts      Account[]
  sessions      Session[]
}

model Account {
  id                String  @id @default(cuid())
  userId            String
  type              String
  provider          String
  providerAccountId String
  refresh_token     String? @db.Text
  access_token      String? @db.Text
  expires_at        Int?
  token_type        String?
  scope             String?
  id_token          String? @db.Text
  session_state     String?
  user              User    @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([provider, providerAccountId])
}

model Session {
  id           String   @id @default(cuid())
  sessionToken String   @unique
  userId       String
  expires      DateTime
  user         User     @relation(fields: [userId], references: [id], onDelete: Cascade)
}

model Conversation {
  id        String    @id @default(cuid())
  userId    String
  title     String?   // Auto-generated from first message
  createdAt DateTime  @default(now())
  updatedAt DateTime  @updatedAt
  user      User      @relation(fields: [userId], references: [id], onDelete: Cascade)
  messages  Message[]
  
  @@index([userId, updatedAt(sort: Desc)])
}

model Message {
  id             String       @id @default(cuid())
  conversationId String
  role           String       // 'user' | 'assistant'
  content        String       @db.Text
  createdAt      DateTime     @default(now())
  conversation   Conversation @relation(fields: [conversationId], references: [id], onDelete: Cascade)
  
  @@index([conversationId, createdAt])
}
```

---

## 5. Implementation Guide

### Step 1: Project Setup

```bash
# Create project
mkdir a3 && cd a3

# Setup local PostgreSQL
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: a3_db
      POSTGRES_USER: a3_user
      POSTGRES_PASSWORD: a3_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
EOF

docker-compose up -d
```

### Step 2: Agent Library

```bash
# Create agent library
mkdir -p agent/src/providers
cd agent
npm init -y
npm install openai
npm install -D typescript @types/node
```

**agent/src/types.ts**:
```typescript
export interface AgentConfig {
  provider: 'openai' | 'anthropic';
  apiKey: string;
  model?: string;
  temperature?: number;
  maxTokens?: number;
  systemPrompt?: string;
}

export interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
}

export interface ChatContext {
  messages?: Message[];
  conversationId?: string;
}
```

**agent/src/providers/base.ts**:
```typescript
import { ChatContext } from '../types';

export abstract class AIProvider {
  abstract complete(prompt: string, context?: ChatContext): Promise<string>;
  abstract *stream(prompt: string, context?: ChatContext): AsyncGenerator<string>;
}
```

**agent/src/providers/openai.ts**:
```typescript
import OpenAI from 'openai';
import { AIProvider } from './base';
import { ChatContext, Message } from '../types';

export class OpenAIProvider extends AIProvider {
  private client: OpenAI;
  private model: string;

  constructor(apiKey: string, model = 'gpt-4-turbo-preview') {
    super();
    this.client = new OpenAI({ apiKey });
    this.model = model;
  }

  async complete(prompt: string, context?: ChatContext): Promise<string> {
    const messages = this.buildMessages(prompt, context);
    const response = await this.client.chat.completions.create({
      model: this.model,
      messages,
    });
    return response.choices[0].message.content || '';
  }

  async *stream(prompt: string, context?: ChatContext): AsyncGenerator<string> {
    const messages = this.buildMessages(prompt, context);
    const stream = await this.client.chat.completions.create({
      model: this.model,
      messages,
      stream: true,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) yield content;
    }
  }

  private buildMessages(prompt: string, context?: ChatContext): OpenAI.Chat.ChatCompletionMessageParam[] {
    const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [];
    
    // Add context messages if provided
    if (context?.messages) {
      messages.push(...context.messages);
    }
    
    // Add current prompt
    messages.push({ role: 'user', content: prompt });
    
    return messages;
  }
}
```

**agent/src/agent.ts**:
```typescript
import { AIProvider } from './providers/base';
import { OpenAIProvider } from './providers/openai';
import { AgentConfig, ChatContext } from './types';

export class Agent {
  private provider: AIProvider;

  constructor(config: AgentConfig) {
    switch (config.provider) {
      case 'openai':
        this.provider = new OpenAIProvider(config.apiKey, config.model);
        break;
      default:
        throw new Error(`Unsupported provider: ${config.provider}`);
    }
  }

  async chat(message: string, context?: ChatContext): Promise<string> {
    return this.provider.complete(message, context);
  }

  async *stream(message: string, context?: ChatContext): AsyncGenerator<string> {
    yield* this.provider.stream(message, context);
  }
}
```

**agent/src/index.ts**:
```typescript
export { Agent } from './agent';
export * from './types';
```

### Step 3: Backend Setup

```bash
cd ../backend
npx create-next-app@latest . --typescript --tailwind --app --no-src-dir
npm install @prisma/client prisma next-auth @auth/prisma-adapter
npm install ../agent  # Link local agent
```

**backend/.env.local**:
```bash
DATABASE_URL="postgresql://a3_user:a3_password@localhost:5432/a3_db"
NEXTAUTH_URL="http://localhost:3001"
NEXTAUTH_SECRET="generate-32-char-random-string-here"
GOOGLE_CLIENT_ID="your-google-client-id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
OPENAI_API_KEY="sk-..."
```

**backend/lib/auth.ts**:
```typescript
import { NextAuthOptions } from "next-auth";
import GoogleProvider from "next-auth/providers/google";
import { PrismaAdapter } from "@auth/prisma-adapter";
import { prisma } from "./db";

export const authOptions: NextAuthOptions = {
  adapter: PrismaAdapter(prisma),
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
  ],
  session: {
    strategy: "jwt",
  },
  callbacks: {
    session: async ({ session, token }) => {
      if (token?.sub) {
        session.user.id = token.sub;
      }
      return session;
    },
    jwt: async ({ token, user }) => {
      if (user) {
        token.id = user.id;
      }
      return token;
    },
  },
};
```

**backend/lib/db.ts**:
```typescript
import { PrismaClient } from '@prisma/client';

const globalForPrisma = global as unknown as { prisma: PrismaClient };

export const prisma = globalForPrisma.prisma || new PrismaClient();

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
```

**backend/lib/agent-instance.ts**:
```typescript
import { Agent } from '../../agent/src';

let agent: Agent;

export function getAgent(): Agent {
  if (!agent) {
    agent = new Agent({
      provider: 'openai',
      apiKey: process.env.OPENAI_API_KEY!,
      model: 'gpt-4-turbo-preview',
    });
  }
  return agent;
}
```

**backend/app/api/conversations/route.ts**:
```typescript
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { NextResponse } from "next/server";

// GET /api/conversations - List all conversations
export async function GET() {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const conversations = await prisma.conversation.findMany({
    where: { userId: session.user.id },
    orderBy: { updatedAt: 'desc' },
    include: {
      messages: {
        take: 1,
        orderBy: { createdAt: 'asc' },
      },
    },
  });

  return NextResponse.json(conversations);
}

// POST /api/conversations - Create new conversation
export async function POST() {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const conversation = await prisma.conversation.create({
    data: {
      userId: session.user.id,
      title: "New Chat",
    },
  });

  return NextResponse.json(conversation);
}
```

**backend/app/api/conversations/[id]/route.ts**:
```typescript
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { NextResponse } from "next/server";

// GET /api/conversations/:id - Get single conversation with messages
export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const conversation = await prisma.conversation.findUnique({
    where: {
      id: params.id,
      userId: session.user.id,
    },
    include: {
      messages: {
        orderBy: { createdAt: 'asc' },
      },
    },
  });

  if (!conversation) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  return NextResponse.json(conversation);
}

// DELETE /api/conversations/:id
export async function DELETE(
  request: Request,
  { params }: { params: { id: string } }
) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  await prisma.conversation.delete({
    where: {
      id: params.id,
      userId: session.user.id,
    },
  });

  return NextResponse.json({ success: true });
}
```

**backend/app/api/chat/route.ts**:
```typescript
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { getAgent } from "@/lib/agent-instance";
import { NextRequest } from "next/server";

export async function POST(request: NextRequest) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return new Response("Unauthorized", { status: 401 });
  }

  const { message, conversationId } = await request.json();
  const agent = getAgent();

  // Get or create conversation
  let conversation;
  if (conversationId) {
    conversation = await prisma.conversation.findUnique({
      where: { id: conversationId, userId: session.user.id },
      include: { messages: { orderBy: { createdAt: 'asc' } } },
    });
  } else {
    conversation = await prisma.conversation.create({
      data: {
        userId: session.user.id,
        title: message.slice(0, 50), // Auto-title from first message
      },
      include: { messages: true },
    });
  }

  if (!conversation) {
    return new Response("Conversation not found", { status: 404 });
  }

  // Save user message
  await prisma.message.create({
    data: {
      conversationId: conversation.id,
      role: 'user',
      content: message,
    },
  });

  // Prepare context
  const context = {
    messages: conversation.messages.map(m => ({
      role: m.role as 'user' | 'assistant',
      content: m.content,
    })),
  };

  // Stream response
  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    async start(controller) {
      let fullResponse = '';
      
      try {
        // Send conversation ID first
        controller.enqueue(
          encoder.encode(`data: ${JSON.stringify({ conversationId: conversation.id })}\n\n`)
        );

        // Stream AI response
        for await (const chunk of agent.stream(message, context)) {
          fullResponse += chunk;
          controller.enqueue(
            encoder.encode(`data: ${JSON.stringify({ chunk })}\n\n`)
          );
        }

        // Save assistant message
        await prisma.message.create({
          data: {
            conversationId: conversation.id,
            role: 'assistant',
            content: fullResponse,
          },
        });

        // Update conversation's updatedAt
        await prisma.conversation.update({
          where: { id: conversation.id },
          data: { updatedAt: new Date() },
        });

        controller.enqueue(encoder.encode(`data: [DONE]\n\n`));
      } catch (error) {
        console.error('Chat error:', error);
        controller.enqueue(
          encoder.encode(`data: ${JSON.stringify({ error: 'Failed to generate response' })}\n\n`)
        );
      } finally {
        controller.close();
      }
    },
  });

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}
```

### Step 4: Frontend Implementation

```bash
cd ../frontend
npx create-next-app@latest . --typescript --tailwind --app --no-src-dir
npm install next-auth swr
```

**frontend/.env.local**:
```bash
NEXT_PUBLIC_BACKEND_URL="http://localhost:3001"
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="same-as-backend"
```

**frontend/components/Sidebar.tsx**:
```typescript
'use client';

import { useState, useEffect } from 'react';
import { useRouter, useParams } from 'next/navigation';
import { PlusIcon } from '@heroicons/react/24/outline';

interface Conversation {
  id: string;
  title: string;
  updatedAt: string;
}

export default function Sidebar() {
  const router = useRouter();
  const params = useParams();
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const currentId = params?.id as string;

  useEffect(() => {
    fetchConversations();
  }, []);

  const fetchConversations = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/conversations`, {
      credentials: 'include',
    });
    if (res.ok) {
      const data = await res.json();
      setConversations(data);
    }
  };

  const createNewChat = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/conversations`, {
      method: 'POST',
      credentials: 'include',
    });
    if (res.ok) {
      const conversation = await res.json();
      router.push(`/chat/${conversation.id}`);
      fetchConversations();
    }
  };

  const groupConversationsByDate = (conversations: Conversation[]) => {
    const today = new Date();
    const yesterday = new Date(today);
    yesterday.setDate(yesterday.getDate() - 1);
    const lastWeek = new Date(today);
    lastWeek.setDate(lastWeek.getDate() - 7);

    const groups: { [key: string]: Conversation[] } = {
      Today: [],
      Yesterday: [],
      'Previous 7 Days': [],
      Older: [],
    };

    conversations.forEach(conv => {
      const date = new Date(conv.updatedAt);
      if (date.toDateString() === today.toDateString()) {
        groups.Today.push(conv);
      } else if (date.toDateString() === yesterday.toDateString()) {
        groups.Yesterday.push(conv);
      } else if (date > lastWeek) {
        groups['Previous 7 Days'].push(conv);
      } else {
        groups.Older.push(conv);
      }
    });

    return groups;
  };

  const groups = groupConversationsByDate(conversations);

  return (
    <div className="w-64 bg-gray-900 text-white h-screen flex flex-col">
      <div className="p-2">
        <button
          onClick={createNewChat}
          className="w-full flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-700 transition-colors"
        >
          <PlusIcon className="w-5 h-5" />
          New Chat
        </button>
      </div>

      <div className="flex-1 overflow-y-auto">
        {Object.entries(groups).map(([groupName, groupConvs]) => {
          if (groupConvs.length === 0) return null;
          
          return (
            <div key={groupName} className="px-2 py-2">
              <div className="text-xs text-gray-400 px-3 py-1">{groupName}</div>
              {groupConvs.map(conv => (
                <button
                  key={conv.id}
                  onClick={() => router.push(`/chat/${conv.id}`)}
                  className={`w-full text-left px-3 py-2 rounded-lg hover:bg-gray-700 transition-colors ${
                    currentId === conv.id ? 'bg-gray-700' : ''
                  }`}
                >
                  <div className="truncate text-sm">{conv.title || 'New Chat'}</div>
                </button>
              ))}
            </div>
          );
        })}
      </div>

      <div className="p-4 border-t border-gray-700">
        <button
          onClick={() => signOut()}
          className="text-sm text-gray-400 hover:text-white"
        >
          Sign Out
        </button>
      </div>
    </div>
  );
}
```

**frontend/components/ChatArea.tsx**:
```typescript
'use client';

import { useState, useEffect, useRef } from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import { useParams } from 'next/navigation';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export default function ChatArea() {
  const params = useParams();
  const conversationId = params?.id as string;
  const [messages, setMessages] = useState<Message[]>([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const [streamingMessage, setStreamingMessage] = useState('');

  useEffect(() => {
    if (conversationId) {
      loadConversation();
    } else {
      setMessages([]);
    }
  }, [conversationId]);

  const loadConversation = async () => {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/conversations/${conversationId}`,
      { credentials: 'include' }
    );
    if (res.ok) {
      const data = await res.json();
      setMessages(data.messages.map((m: any) => ({
        role: m.role,
        content: m.content,
      })));
    }
  };

  const sendMessage = async (content: string) => {
    // Add user message
    const userMessage = { role: 'user' as const, content };
    setMessages(prev => [...prev, userMessage]);
    setIsStreaming(true);
    setStreamingMessage('');

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: content, conversationId }),
        credentials: 'include',
      });

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (reader) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') {
              setMessages(prev => [...prev, { role: 'assistant', content: streamingMessage }]);
              setStreamingMessage('');
              setIsStreaming(false);
              continue;
            }

            try {
              const parsed = JSON.parse(data);
              if (parsed.chunk) {
                setStreamingMessage(prev => prev + parsed.chunk);
              }
            } catch (e) {
              console.error('Parse error:', e);
            }
          }
        }
      }
    } catch (error) {
      console.error('Chat error:', error);
      setIsStreaming(false);
    }
  };

  return (
    <div className="flex-1 flex flex-col">
      <MessageList 
        messages={messages} 
        streamingMessage={streamingMessage}
        isStreaming={isStreaming}
      />
      <MessageInput 
        onSend={sendMessage} 
        disabled={isStreaming}
      />
    </div>
  );
}
```

**frontend/components/MessageList.tsx**:
```typescript
interface Props {
  messages: Array<{ role: 'user' | 'assistant'; content: string }>;
  streamingMessage?: string;
  isStreaming?: boolean;
}

export default function MessageList({ messages, streamingMessage, isStreaming }: Props) {
  return (
    <div className="flex-1 overflow-y-auto">
      <div className="max-w-3xl mx-auto p-4 space-y-6">
        {messages.map((message, index) => (
          <div key={index} className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[80%] rounded-lg px-4 py-2 ${
              message.role === 'user' 
                ? 'bg-gray-700 text-white' 
                : 'bg-gray-100 text-gray-900'
            }`}>
              <div className="whitespace-pre-wrap">{message.content}</div>
            </div>
          </div>
        ))}
        
        {isStreaming && streamingMessage && (
          <div className="flex justify-start">
            <div className="max-w-[80%] bg-gray-100 text-gray-900 rounded-lg px-4 py-2">
              <div className="whitespace-pre-wrap">
                {streamingMessage}
                <span className="inline-block w-2 h-4 bg-gray-900 animate-pulse ml-1">▊</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
```

**frontend/components/MessageInput.tsx**:
```typescript
import { useState, useRef, KeyboardEvent } from 'react';

interface Props {
  onSend: (message: string) => void;
  disabled?: boolean;
}

export default function MessageInput({ onSend, disabled }: Props) {
  const [message, setMessage] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSend = () => {
    if (message.trim() && !disabled) {
      onSend(message);
      setMessage('');
    }
  };

  const handleKeyDown = (e: KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="border-t">
      <div className="max-w-3xl mx-auto p-4">
        <div className="flex gap-2">
          <textarea
            ref={textareaRef}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Message A3..."
            disabled={disabled}
            className="flex-1 resize-none rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows={1}
          />
          <button
            onClick={handleSend}
            disabled={disabled || !message.trim()}
            className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
```

**frontend/app/chat/page.tsx**:
```typescript
'use client';

import Sidebar from '@/components/Sidebar';
import ChatArea from '@/components/ChatArea';

export default function ChatPage() {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <ChatArea />
    </div>
  );
}
```

**frontend/app/chat/[id]/page.tsx**:
```typescript
'use client';

import Sidebar from '@/components/Sidebar';
import ChatArea from '@/components/ChatArea';

export default function ConversationPage() {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <ChatArea />
    </div>
  );
}
```

### Step 5: Initialize Database

```bash
cd backend
npx prisma db push
```

### Step 6: Run Everything

```bash
# Terminal 1: Backend
cd backend
npm run dev  # Runs on port 3001

# Terminal 2: Frontend  
cd frontend
npm run dev  # Runs on port 3000
```

---

## 6. Key Implementation Details

### 6.1 Authentication Flow
1. User visits `localhost:3000`
2. If not authenticated, redirect to `/login`
3. Click "Sign in with Google"
4. OAuth flow through backend (`localhost:3001/api/auth`)
5. Session created, redirect to `/chat`

### 6.2 Conversation Management
1. **New Chat**: POST to `/api/conversations`, creates empty conversation
2. **Load Chat**: GET `/api/conversations/:id`, returns all messages
3. **Auto-title**: First user message becomes conversation title (50 chars)
4. **Delete**: DELETE `/api/conversations/:id`

### 6.3 Streaming Implementation
1. Frontend sends message to backend
2. Backend saves user message to DB
3. Backend starts streaming from Agent
4. Each chunk sent as Server-Sent Event
5. Frontend accumulates chunks and displays
6. When done, backend saves complete assistant message

### 6.4 UI Behavior
- Sidebar shows conversations grouped by date
- Current conversation highlighted
- Messages auto-scroll to bottom
- Input disabled while streaming
- Streaming indicator shows pulsing cursor

---

## 7. Environment Setup

### Google OAuth Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URIs:
   - `http://localhost:3001/api/auth/callback/google`
   - `https://yourdomain.com/api/auth/callback/google` (production)

### Local Development
```bash
# Start PostgreSQL
docker-compose up -d

# Install dependencies
cd agent && npm install && cd ..
cd backend && npm install && cd ..
cd frontend && npm install && cd ..

# Run all services
# Backend on :3001, Frontend on :3000
```

---

## 8. Deployment

### Production Checklist
- [ ] Set production environment variables
- [ ] Use managed PostgreSQL (Railway, Render, etc.)
- [ ] Deploy backend to Vercel/Railway
- [ ] Deploy frontend to Vercel
- [ ] Update OAuth redirect URLs
- [ ] Enable HTTPS everywhere
- [ ] Set secure session secrets

This implementation creates a fully functional ChatGPT clone with conversation history, streaming responses, and Google authentication, with the agent logic completely separated for future reuse.
