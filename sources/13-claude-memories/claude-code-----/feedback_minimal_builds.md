---
name: Minimize lake builds — slow + battery cost
description: Run `lake build SSBX` sparingly; full builds are 1-10 min on this machine and drain battery
type: feedback
originSessionId: cf6a07ef-8ca3-4a88-8fcd-004cad5499d5
---
Do NOT spam `lake build SSBX` (the full project build) between every small edit. Each full build takes 1-10 minutes and visibly drains the laptop battery. The user called this out 2026-05-15 after a session where I ran 7-8 full builds during a single iterative refactor.

**Why**: User runs this on a laptop. Full SSBX build is 3800+ jobs, lake's incremental cache helps but still touches lots of files. Battery + thermal cost is real.

**How to apply**:
- During iterative edits: use **targeted module build**, e.g. `lake build SSBX.Foundation.Atlas.Yi.Classical.Core.Yi` — 5-10 seconds.
- Batch related edits together; verify ONCE after the batch, not per-edit.
- If a subagent is already running a build, don't start a parallel one — wait for its result.
- Only run full `lake build SSBX` at commit checkpoints (or when a targeted module build won't catch the issue).
- When debugging cascade errors, grep error output for unique error types first, then fix in batch.
