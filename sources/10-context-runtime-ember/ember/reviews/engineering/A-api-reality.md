# Review A: API realism & model-adapter strategy (2026-07-29)

## 1. INTERPRET verdict: fiction. Demultiplex inside THINK.

- Anthropic Messages: ordered typed content blocks (thinking, redacted_thinking, text, tool_use, server_tool_use, compaction, fallback). Streaming = typed SSE: message_start → per block (content_block_start → deltas (text_delta|thinking_delta|input_json_delta|signature_delta) → content_block_stop) → message_delta (stop_reason, usage) → message_stop.
- Tool call never "parsed from thought" — arrives as tool_use block with id/name/input; input accumulates as partial JSON during streaming, complete+parseable exactly at content_block_stop. Eager input streaming GA. Act is *streaming* while block open, *requested* the instant block closes.
- Thinking is first-class typed part, interleaved (adaptive thinking on 4.6+, auto-interleaved): [thinking, text, tool_use, tool_use], continuation starts with new thinking. Thinking is not a preamble.
- stop_reason arrives only at message_delta: end_turn/tool_use/max_tokens/stop_sequence/pause_turn/refusal (+model_context_window_exceeded on 4.5+). Parallel tool set unknowable until message closes. Contract: execute ALL of turn's tool_use blocks, return ALL tool_results in single following user message.
- OpenAI: chat-completions = index-keyed delta.tool_calls[] with concatenated JSON string args (loads at end), finish_reason. Responses API = typed items (reasoning {id, summary[], encrypted_content}, message, function_call), semantic stream events (output_item.added/done, output_text.delta, function_call_arguments.delta, response.completed). OpenHands consumes exactly this (llm.py:1007–1073).
- Both converge: assistant turn = ordered stream of typed parts with open/delta/close boundaries + terminal stop reason + opaque continuity material echoed back verbatim (Anthropic: thinking signature + redacted_thinking.data; OpenAI: reasoning id + encrypted_content).
- Only residue: thin per-part decode/validate (json.loads OpenAI args, schema-check name) — mini's parse_toolcall_actions (actions_toolcall.py:30–76).

### 2026 thinking replay requirements (hard constraints):
1. Within tool-use turn, same model: thinking blocks passed back UNCHANGED (signature server-verified; API rejects tampering). redacted_thinking replays verbatim.
2. Thinking blocks FIRST in replayed assistant message — mini's _reorder_anthropic_thinking_blocks (anthropic_utils.py:11–28), pads empty text block if thinking-only.
3. Fable 5/Opus 5/4.8/4.7/Sonnet 5: display defaults "omitted" — blocks stream with EMPTY text but must still be echoed exactly (empty string included).
4. Replaying one model's thinking to different model: silently dropped (unbilled) — dream_model≠waking model works, but dream gets no continuity from waking thinking.
5. Violating 1–2 = LiteLLM users' #1 breakage (litellm#15601 "final assistant message must start with a thinking block").

### Proposed §4.1 replacement (8 steps):
1 LEASE · 2 PERCEIVE · 3 ATTEND · 4 THINK (ModelPort streams typed parts; demux at part-close: text→spoke, reasoning→mused, tool call→act [decoded+validated at part close; act *requested* at part completion; while open exists only on EXPRESS surface]; message-close records verbatim thought; stream order: thought_request · parts in delivery order · thought) · 5 ACT (only if stop_reason=tool_use; dispatch WAITS for message-close — parallel set/truncation/refusal unknowable earlier; ALL observations return together in next moment's perception) · 6 SETTLE · 7 REMEMBER · 8 EXPRESS (continuous tap on THINK: part events + deltas; deltas ephemeral, never WAL).

- Granularity rule: stream records completed parts, never deltas. WAL appends at part-close. Aborted thought records closed parts + error with partial tail.
- Turns span moments: one provider turn = several ember moments (A1). Until turn ends, each moment's renderer replays turn's prior parts VERBATIM — thinking first, signatures/redacted/encrypted untouched, tool_use ids intact. `thought` = authoritative echo source; spoke/act/mused = derived fold-facing views.
- stop_reason perceived, not swallowed: tool_use→ACT; end_turn→span may end spoke; pause_turn→re-send next moment (server-side tool loops); max_tokens→truncation disposition; refusal→recorded with stop_details, policy decides; model_context_window_exceeded→forced sleep.

## 2. §2.2 changes

- ADD `mused`: completed reasoning part {text (may be empty/summary), provider_kind: thinking|redacted_thinking|reasoning_item, refs:{thought, part_index}}. Display text only — signatures/encrypted_content live ONCE in verbatim thought.
- REWRITE `act`: "a tool call as delivered by the model — typed part, not parsed from prose: tool_use_id, name, decoded+validated arguments; refs:{thought, part_index}". Decode failures recorded on act (invalid: reason) + answered with error tool_result (mini's FormatError path).
- TIGHTEN `thought`: verbatim must include all parts in delivery order incl. thinking blocks w/ signature, redacted_thinking.data, reasoning items w/ id/encrypted_content, tool_use ids; stop_reason, stop_details, usage, provider msg id, dialect/adapter stamp. Invariant: every part appears exactly once as part experience ref'ing the thought.
- EXTEND `thought_request`: dialect (litellm-chat/v1 | anthropic-messages/v1 | openai-responses/v1), adapter name+version, wire model id.
- `spoke`: emitted per completed text part (several per thought possible, interleaved with acts).
- `error`: reserve for transport failures/aborts. refusal/max_tokens/pause_turn are SUCCESSFUL responses (HTTP 200) in thought.stop_reason.

## 3. LiteLLM verdict: ADOPT as first adapter

Native handling (evidence): cache_control passthrough (mini set_cache_control cache_control.py; OpenHands _apply_prompt_caching llm.py:2599–2627); thinking_blocks returned RAW un-normalized (signatures incl.) + accepted back on input; normalized reasoning_content; streaming signatures since v1.63.0 (PR #11194); reasoning_effort mapped per-provider (OpenHands chat_options.py:49–50 — incl. Opus 4.5 output_config + beta header); parallel tool_calls + streaming deltas (OpenHands reassembles via litellm.stream_chunk_builder llm.py:2141–2166 — chunk dialect display-grade, not record-grade); Responses API surface (litellm.responses; OpenHands llm.py:1623–1955; replays reasoning items verbatim — id + encrypted_content — "so replays stay byte-identical and OpenAI's prefix cache keeps matching" message.py:100–119); cost accounting.

Quirk layer that remains YOURS (~200 lines, reference impls in donors):
1. Thinking-block reorder on replay (mini anthropic_utils.py).
2. Cache breakpoint placement policy (+ live bug: role:"tool" cache_control hoisted block→message level — litellm#6422, both donors).
3. Verbatim response persistence on every path incl. FormatError (mini litellm_model.py:87–106).
4. Model-quirk registry because LiteLLM metadata LAGS new model ids (OpenHands model_features.py — claude-fable-5 "listed explicitly until LiteLLM metadata recognizes it"; Bedrock cross-region ids).
5. Param hygiene: strip temperature/top_p for reasoning models (Anthropic 400s), max_tokens vs max_completion_tokens, forcing max_tokens with thinking, Bedrock budget clamp.
6. Process-global hazards: litellm.modify_params global needs locking (llm.py:2214–2281).
7. Gemini: explicit cache markers HARMFUL (~6–14× cost, freezes implicit cache) — exclude Gemini from marker list (model_features.py:155–158).

Pain points: thinking+tool-use multi-turn 400s (#15601 — LiteLLM silently DROPS thinking param as mitigation — must own the echo from verbatim thought); signature breakage via proxy translation; streaming tool_use.input empty on /v1/messages passthrough some models (#25390). Weekly releases; mid-2026 stability sprint; March 2026 supply-chain incident (litellm 1.82.7/.8 compromised ~40 min). Posture: PIN in programs/pyproject.toml (A6 makes free), stamp version into thought_request.

## 4. ModelPort design + stream recording

- Port contract: think(request) → part-event stream + final ThoughtRecord. Events: part_open{kind}, part_delta (EXPRESS-only, never WAL), part_close{completed part}, thought_close{stop_reason, stop_details, usage}. All adapters emit same schema — fold never changes shape when adapter changes.
- moment/request.json = EXACT object handed to the adapter, canonical JSON, in adapter dialect (not "provider wire shape" — true wire exists only inside LiteLLM). Port-boundary bytes + dialect stamp = what A1 needs (replay never re-calls).
- thought body = normalized part envelope, each part's payload = adapter's VERBATIM object, + full verbatim raw_response (inline or blob-ref):
  {dialect, adapter{name,version,wire_model}, stop_reason, stop_details, usage, provider_msg_id, parts:[{kind:"reasoning",raw:{...signature...}},{kind:"text",raw:{...}},{kind:"tool_call",id,name,input,raw:{...}}], raw_response:{...}}
- Optional debug: provider-raw wire capture via adapter logging callback → stream/blobs/ (not load-bearing).
- Replay: reducers fold part experiences dialect-free; renderer echoes prior thought.parts[].raw verbatim (thinking-first ordering applied); adapter/dialect switch mid-lineage = new waking epoch (cache cold anyway; foreign continuity dropped by design).
- §9.2 row: ModelPort first adapter = LiteLLM (chat dialect; Responses dialect for OpenAI reasoning models); alternates = direct anthropic SDK (REFERENCE adapter: 1:1 SSE→part mapping, day-one features), direct openai, raw HTTP debug.

## 5. Other spec contradictions

1. §1 layout + §5.4: "provider-shaped request.json" → "exact request in ModelPort adapter dialect (canonical JSON; dialect stamped)". §10 M2: "direct Anthropic adapter" → "ModelPort on LiteLLM adapter (Anthropic model first); direct-anthropic reference optional".
2. §5 renderers: cache breakpoints are a renderer duty, per-provider: Anthropic ≤4 explicit breakpoints (render order tools→system→messages — tool-set change invalidates everything; consistent w/ capabilities in stable tier), positions recorded in lineage.json; OpenAI: NO markers (automatic); Gemini: markers FORBIDDEN (cost). Turn-echo rule lives here too.
3. §3.4 waking epochs — three cache control planes, not one: Anthropic explicit (min cacheable 512–4096 tokens, TTL 5min/1h, write premium 1.25×/2×, reads ~0.1×); OpenAI automatic (≥1024, no markers, no write premium); Gemini implicit (explicit markers harmful). cached_prefix_tokens computed per provider rules. WARMTH IS TIME-BASED (TTL minutes) vs DAG epochs (timeless): UI shows cold-resume cost (guaranteed) vs warm-continue saving (TTL-conditional); resumed-after-an-hour pays full re-ingest inside one epoch; Anthropic re-warm costs 1.25–2× write premium. Caches are MODEL-scoped: dream_model≠waking model → dream neither reads nor disturbs waking cache (cheap dream brains cache-side-effect-free); epoch accounting per (model, dialect); adapter/dialect switch = epoch break.
4. §4.2/§4.4: map provider stop reasons: pause_turn → not an ending, re-send next moment; refusal → recorded on thought (200-success, NOT error experience), policy decides; max_tokens → truncation disposition; model_context_window_exceeded → forced-sleep trigger.
5. §2.2 act wording fix (INTERPRET fiction).
6. §8.1 Vercel adapter: map mused → protocol reasoning parts. §2.3: state part-close WAL granularity (EXPRESS deltas never touch stream).
