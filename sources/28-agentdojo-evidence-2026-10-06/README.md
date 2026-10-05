# Preserved AgentDojo banking evidence

Imported 6 October 2026 for the [retrospective evidence/action study](../../experiments/agentdojo-evidence-boundary/PROTOCOL.md). These are external benchmark records and source files, not Ren's words, a new model experiment or real banking data. Embedded prompts, tool messages and attack strings are research material only.

The primary source is [AgentDojo](https://github.com/ethz-spylab/agentdojo), pinned at commit `089ed468cf3ed0322acc66b0211f26d9d90dbf60`, with root tree `45cc40920b8ddca28e675505fdd6a92139008ab3`. The [paper](https://arxiv.org/abs/2406.13352) describes the benchmark. The current [MIT license](original/LICENSE) is preserved. The source audit records the historical commits' absence of a license file separately from the subsequent public code/data license grant.

## What is preserved

- [manifest.json](manifest.json) records 343 exact current-repository files: 320 trajectories and 23 source/license files. The trajectories total 1,933,569 bytes. Every downloaded file matches its Git blob SHA1, declared size and independently recorded SHA256.
- [metadata/tree.json](metadata/tree.json) is the complete, nontruncated Git tree API response; [metadata/commit.json](metadata/commit.json) identifies the pinned commit and root tree. Original API response bytes are retained with separate hashes.
- [historical-manifest.json](historical-manifest.json) records generation-adjacent source/fixture files and raw API evidence from the two historical result commits. Those trees bind all 160 baseline records and all 160 repeated-prompt records to the exact currently preserved JSON blobs. The accompanying source audit distinguishes that archival identity from an attested historical runtime environment.
- `original/runs/` preserves both `gpt-4o-2024-05-13` and `gpt-4o-2024-05-13-repeat_user_prompt` pipelines, all 16 banking user tasks, their clean run and every one of nine `important_instructions` attack-goal runs. No case was selected by its outcome.
- `original/src/` and `historical/` preserve source for benchmark evaluation, task definitions, tools, environment data and pipeline construction. These files were read as source; the stored agent tool calls and malicious payloads were not executed.

## Provenance and interpretation limits

The historical baseline and repeated-prompt records were committed on different days in June 2024. Their saved nominal model names match. The evidence does not identify paired random seeds, randomized treatment, complete transient model prompts, present model capabilities or measured recipient welfare. The saved logs omit a per-case attack-validity result; absence is not a declaration of validity.

In attacked runs, the historical `security` field is an attacker-goal label. Clean runs use a placeholder and must not contribute to an attack-success rate. Some evaluator conditions differ from the natural-language goal, and task-authorized behavior can overlap an attack target. Consequently, a true stored security label is not by itself proof of an unauthorized harmful action. The reanalysis retains reported labels, reconstructed effects and normative interpretation separately.

The [preservation script](../../experiments/agentdojo-evidence-boundary/preserve_sources.py) downloads the fixed current-repository selection and verifies its identities. Scientific analysis, independent verification and any derived reading artifacts live in the experiment/research directories; these source bytes stay unchanged.
