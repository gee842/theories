# Selective handoff pilot: execution provenance

6 October 2026. Prospective recording recipe for the proposed **4 archived packets × 3 evidence states × 2 instruction conditions = 24 fresh-context requests**. This audit made no participant calls and no external searches. It inspects the currently exposed collaboration contract and the [original experiment](../../../../sources/20-codex-theory-sessions-2026-10-05/sin/outputs/experiment-report.md), [protocol](../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/PROTOCOL.md), [independent data audit](../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/data-audit.md), and [recorded invocations](../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/orchestrator-invocations.json).

## Authentic historical artifacts, constructed new episode

Use the first four lexically ordered lineage folders whose maintenance response has a nonempty packet: **L02, L06, L08, L12**. This selection was checked against the archived JSON files. Their existence and original favorable results are already known. The new pilot conditions on these historical artifacts; it does not repeat donor acquisition, estimate a population of independently trained models, or show that a new founder learned a lesson.

Read each original response as bytes, decode UTF-8 strictly, parse JSON, select the string at key `packet`, and encode that string as UTF-8 **without added newline, quotation marks, whitespace stripping or Unicode normalization**. JSON escape decoding is part of extraction; JSON reserialization is not the packet representation. Keep the original response bytes as the primary source. The new full prompt has its own hash; verify that its packet span equals the extracted string exactly.

| Lineage | Original maintenance-response SHA-256 | Extracted UTF-8 packet bytes / SHA-256 |
|---|---|---|
| [L02][l02] | `3f1d4e6c7ab080e84c2f296b1784fc511489dbdbaea4d886500187247bf30303` | 455 / `70c16273e561d009482c67f6cbce972a112a74483003056c0f95647b553ac131` |
| [L06][l06] | `ed3c5361c54101ef5638315197477efe939d9a0a72846f24eb69e9dab91a0b97` | 574 / `18d5d9ef99869dce8d2354fb5f38aa258322cba131de66aaf9a0cccc29ff990f` |
| [L08][l08] | `3f1a8c8dbe20e8af1fb1dadeff1599efec477aa4e8234e6db4d834588ba31de7` | 395 / `16eed972af040b1dbe45c2081b217ca0b810443ee228939bf4093bd27a412512` |
| [L12][l12] | `ffff2865b6873cff5a2590c1707baf4c268b0c61d4170221a0e8d4a6d96d8199` | 460 / `fe2b4ef0b2d4f766a082c32d67cc5cf2da5e8aeb57f399fa8b786605136f0b37` |

Each linked response's directory also holds `baseline-prompt.txt`, `baseline-response.json`, `maintenance-prompt.txt` and `private.json`. The independent audit's “Ground truth, prompts and transmission” section checks the original evidence, rule correspondence and delivered packet bytes. The [independent audit code](../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/independent-data-audit.py) uses its own rule calculation. Private truth uses an internal field order; do not equate its numeric indices directly with the displayed field order. A historical rule's correctness does not establish applicability in the constructed new episode.

| Historical inputs | Maintenance prompt SHA-256 | Private fixture SHA-256 |
|---|---|---|
| [L02 prompt][p02], [fixture][t02] | `6ce097e9ba599970c5460307ea4ac0ff8cf6aba4525135866c0896ade2149f25` | `b8328668259c0cdc0376b33cb56ba99f14fbc0adff45559e99312c8194510d2f` |
| [L06 prompt][p06], [fixture][t06] | `7a9af470a1ad8de519f9c2e36703491ad40f70e9c56151274915c68035cd4e41` | `7fc65095081a56f1c0c8d861c29c051bd2057a0c129a84078219707cced74bfb` |
| [L08 prompt][p08], [fixture][t08] | `44a2e872367b8621fe441261b092d93c51fc86ec441092645a39ed4d3d280cb3` | `1548624b820d8412351b3ac355e54ca7da1561e8b3ad40f9b06b0115b0095301` |
| [L12 prompt][p12], [fixture][t12] | `988e3ed892ff56b7531dbaab63d73928caa634f9d262df5e9cd01489b2230f77` | `e0fc154ffbe92f9e7d5957bd6c9b434ecb900f129285d77904c7b6adbc7c4381` |

## What the tool can document

The exposed `collaboration.spawn_agent` contract accepts `task_name`, `message`, `fork_turns`, and optional model/effort overrides. It states that `fork_turns:"none"` does not pass surrounding conversation context. Make a **new spawn for every participant**, with a neutral unique ID. Continuing an existing participant using `followup_task` is not a fresh context.

Include the entire frozen prompt in the dispatch message. Instruct the participant to use no tools, read no files, send no messages and return its answer directly. The orchestrator saves the returned text. This removes a required participant file-read step, but does not disable tools. Tool-declared context separation, shared model training and a shared filesystem must remain distinct.

Omit model and reasoning overrides unless separately authorized. Record those fields as omitted/inherited, not as a guessed exact model ID. The exposed API does not provide controls for seed, temperature or complete platform/system context. Available-model lists do not establish which model served a particular request. Record the exact serving revision, sampling settings, token billing and hidden platform context as unknown unless an actual receipt exposes them.

## Minimal recording recipe

1. **Before dispatch:** freeze protocol, all 24 complete prompt strings, source packet hashes, condition/fixture mapping, dispatch order, response schema, scoring and failure/retry policy. Save exact UTF-8 prompt bytes and the exact intended spawn arguments. Neutral task IDs should not disclose the condition beyond the prompt.
2. **At dispatch:** append request sequence, local UTC timestamp, prompt hash, `fork_turns:"none"`, omitted/explicit overrides and the complete tool arguments. Preserve the returned canonical agent identity and every visible acknowledgement/error immediately. A local clock or hash is not external notarization.
3. **At receipt:** retain the full visible delivery envelope and final text before parsing. Save its UTF-8 representation and hash. This is a transcript copy exposed to the orchestrator, not raw provider HTTP bytes or an independently authenticated platform export. If manually copied, label that fact. Preserve any extra messages, warnings or interruptions.
4. **After receipt:** parse into a separate derived file; never repair the original answer. Retain malformed, missing, refused and failed responses under the frozen policy. Record all actual retries and whether a new context was created; do not request answer improvement. Keep all planned slots in the accounting.
5. **Independent check:** compare dispatched strings with frozen prompt files and packet spans, map each returned identity to exactly one planned slot, reconstruct scores from raw answers, and audit deviations. The checker must not import the producer. It can certify saved-record consistency, not unseen access or platform internals.

The tool delivers final answers to the parent and offers status/messages. It does not promise a complete child tool/analysis transcript export. General desktop thread-summary tools are not automatically authenticated logs of collaboration participants. Mark unavailable traces as unavailable; a participant's assertion of no tool use is not independent verification.

## Defensible claim boundary

The record can support: “Twenty-four actual responses were requested in tool-declared fresh conversation contexts under the frozen supplied evidence/advice conditions, using four authentic archived packets.” Completion, valid-response count and results must await the run.

It cannot alone support OS/security isolation, independence of trained models, equal compute, complete absence of unseen communication, new donor learning, recipient welfare, or a general alignment guarantee. Shared instructions, tools and filesystem remain potential common influences. Any detected unauthorized access is a recorded deviation, not grounds for silently deleting an inconvenient outcome.

The prior study retained 128 submissions but reconstructed its invocation ledger retrospectively; it did not expose an exact model identifier or complete participant trace. Recording dispatches contemporaneously improves the new audit trail while retaining those platform limits. Any pilot result will concern selective use of inherited artifacts under supplied current evidence and goals, with ordinary rule inference and instruction-following as live alternatives.

[l02]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L02/maintenance-response.json
[l06]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L06/maintenance-response.json
[l08]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L08/maintenance-response.json
[l12]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L12/maintenance-response.json
[p02]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L02/maintenance-prompt.txt
[t02]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L02/private.json
[p06]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L06/maintenance-prompt.txt
[t06]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L06/private.json
[p08]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L08/maintenance-prompt.txt
[t08]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L08/private.json
[p12]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L12/maintenance-prompt.txt
[t12]: ../../../../sources/20-codex-theory-sessions-2026-10-05/sin/work/live/lineages/L12/private.json
