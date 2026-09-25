# Setting Claude code context to 500k

created: 2026-04-23T16:22:43.820361Z  uuid: fff3da9f-dcf9-43f1-bfa7-e2920f2c232a  export: new
messages: 10  total_chars: 14453  human_chars: 1569

summary: **Conversation Overview**

The person asked about configuring Claude Code's context window and auto-compaction settings, specifically targeting a 420K token compaction threshold. Claude explained that Claude Code does not offer a discrete 500K context setting — the options are 200K (default) or 1M on supported models (Opus 4.7, Opus 4.6, Sonnet 4.6) with eligible plans. Claude walked through two relevant environment variables: `CLAUDE_CODE_AUTO_COMPACT_WINDOW` (sets the effective window size) and `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` (sets the percentage threshold at which auto-compaction triggers).

Claude provided a one-liner to set compaction at 420K by combining `CLAUDE_CODE_AUTO_COMPACT_WINDOW=1000000` with `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=42`, appended to `~/.zshrc`. The person then shared `/context` output confirming their session was running Opus 4.7 on a 1M context window at 21.3K/1M tokens used. Claude interpreted the `Auto-compact window: 1m tokens` line as confirmation the window variable was applied, but noted the displayed `Autocompact buffer: 33k tokens (3.3%)` is a known display bug (referenced as claude-code#27189) — the `/context` UI hardcodes the default buffer display and does not reflect `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`. Claude also cited a second issue (claude-code#31806) explaining that the percentage override can only lower the threshold below the ~83% default, not raise it, due to a `Math.min` clamp. When the person asked for supporting evidence, Claude sourced all three claims to specific GitHub issues and a reverse-engineering guide, while flagging that the inference from the `/context` output was analytical rather than formally documented.

The person communicates tersely and values direct, technically precise answers with exact commands. They pushed back requesting supporting evidence for Claude's claims, indicating they expect cited sources for non-obvious technical assertions. The threshold formula documented in the conversation is: `threshold = min(floor(effectiveWindow * PCT/100), effectiveWindow - 13000)`.


---
**HUMAN** (2026-04-23T16:22):

can i set claude code context to 500k?

---
**ASSISTANT** (2026-04-23T16:23):

  The user is asking about Claude Code's context window settings and whether they can configure it to 500k tokens. I should check my product knowledge to give them accurate information about what's actually available.
```
This block is not supported on your current device yet.
```

 I'm looking up the specific context window limits for Claude Code.
```
This block is not supported on your current device yet.
```

 I'm clarifying the context window options for Claude Code — Opus 4.7, Opus 4.6, and Sonnet 4.6 all support 1M context, while there's no specific 500k setting available, just 200k or 1M, though 500k does appear as an option for certain Enterprise models.

I can also control auto-compaction thresholds with environment variables and disable the 1M context if needed, but since Ren's a heavy Claude Code user who understands these optimizations, I should give them a direct answer: there's no 500k option for Claude Code specifically — it's either the default 200k or 1M on supported plans.No — Claude Code doesn't expose a 500K setting. The context window is discrete, not a dial: it's either **200K** (default) or **1M** (on Opus 4.7, Opus 4.6, or Sonnet 4.6 with a plan that includes extended context).

What you *can* tune around 500K:

- **`CLAUDE_CODE_AUTO_COMPACT_WINDOW`** — sets the auto-compaction trigger. If you're on the 1M window and want compaction to kick in at ~500K (keep context in the high-quality zone before rot), this is the lever. Note: it's clamped to `Math.min(modelWindow, configured)`, so it only works if Claude Code actually recognizes 1M for your session.
- **Check what you've actually got:** `/context` shows `Xk/1000k` if 1M is live, `Xk/200k` if not.
- **Enable 1M:** Max/Team/Enterprise get it automatically on Opus 4.7. Pro needs `/extra-usage` to opt in. On the [1m] alias suffix for pinned models if you're on third-party providers.
- **Disable 1M:** `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`.

If the goal is "stay in the reliable retrieval band below where context rot bites" — running 1M but auto-compacting at 500K is the standard pattern. MRCR/GraphWalks benchmarks show meaningful degradation past ~256K even on 4.6/4.7, so compacting around half-fill is a reasonable heuristic.

Want me to pull the exact env var syntax or the `/model` + `[1m]` suffix setup?

---
**HUMAN** (2026-04-23T16:24):

how?

[attachment excerpt_from_previous_claude_message.txt]
CLAUDE_CODE_AUTO_COMPACT_WINDOW — sets the auto-compaction trigger. If you're on the 1M window and want compaction to kick in at ~500K (keep context in the high-quality zone before rot), this is the lever. Note: it's clamped to Math.min(modelWindow, configured), so it only works if Claude Code actually recognizes 1M for your session.


---
**ASSISTANT** (2026-04-23T16:24):

  The user is asking me to clarify how to actually set that environment variable and make it work in practice, so I need to look up the current documentation to verify the specifics.
```
This block is not supported on your current device yet.
```

 I need to verify the CLAUDE_AUTOCOMPACT_PCT_OVERRIDE variable and understand the key gotcha about how the percentage applies to the original window size. Since they're asking "how?" they want practical setup steps, so I should walk through the two environment variables that interact, how to configure them in shell and settings.json, and highlight the important gotchas around percentage calculations and window sizing.

For their use case of triggering compaction at 500K on a 1M window, Option A with `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` is cleaner than Option B since it directly sets the trigger point. Let me clarify what each variable actually does: the percentage override controls when compaction triggers as a percentage of the window, while the window size variable reduces the effective token limit itself. I should verify whether the default compaction percentage is actually 50% or if that was just a suggestion from the issue.Two env vars interact here. For "compact around 500K on a 1M window," the cleanest setup is:

```bash
# ~/.zshrc (or wherever you keep env)
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=1000000   # keep the full 1M as the window
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50        # trigger compaction at 50% = 500K
```

Then `source ~/.zshrc` and **restart Claude Code** (env vars only apply to new sessions — this is the #1 gotcha people hit).

### What each var actually does

- **`CLAUDE_CODE_AUTO_COMPACT_WINDOW`** — overrides the effective window size used for the compaction math. Capped by the real model window (`Math.min(modelWindow, configured)`), so you can't inflate past 1M, but you can shrink. Setting it to `500000` on a 1M model gives you a 500K effective window where default compaction kicks in near the top of that.
- **`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`** — percentage threshold. The percentage applies to the *overridden window*, not the real one. So `PCT=50` + `WINDOW=1000000` → compact at 500K. `PCT=50` + `WINDOW=500000` → compact at 250K (probably not what you want).

### Alternative via settings.json

If you'd rather keep it per-project or roll it out across machines, put it in `~/.claude/settings.json` under `env`:

```json
{
  "env": {
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
  }
}
```

Project-scoped: `.claude/settings.json` in repo root (same shape).

### Verify

- `/context` inside Claude Code — should show `Xk/1000k` and you can watch the fill.
- `/status` — confirms auth + active model.

### Gotchas worth knowing

1. **1M has to actually be active first.** If `/context` shows `/200k`, the override is clamped to 200K and 50% just means 100K. Check model is Opus 4.7 / 4.6 or Sonnet 4.6 and that you're on a plan that grants 1M (Max/Team/Enterprise auto; Pro needs `/extra-usage`).
2. **Don't set it too aggressively.** Under ~40% and you burn tokens on repeated compactions that shred continuity — worse than just letting it fill.
3. **500K is a reasonable-but-not-obvious target.** MRCR accuracy on 4.6/4.7 is strong through ~256K and degrades progressively past that. 50% on 1M = 500K is a balance: more headroom than 200K mode, compaction before heavy context-rot territory. If you're doing recall-critical work (tracing types across a large codebase, finding a function defined 400K ago), you might want `PCT=40` (compact at 400K) instead.

Given you've been hitting compaction pain on long OpenClaw sessions, I'd start with `PCT=50` and drop to 40 if you notice recall degrading before compaction hits.

---
**HUMAN** (2026-04-23T16:26):

ok give me command in one line that set to 420k

---
**ASSISTANT** (2026-04-23T16:26):

 ```bash
echo 'export CLAUDE_CODE_AUTO_COMPACT_WINDOW=1000000 CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=42' >> ~/.zshrc && source ~/.zshrc
```

Compacts at 42% of 1M = 420K. Restart Claude Code after.

---
**HUMAN** (2026-04-23T16:28):

/context
  ⎿  Context Usage
     ⛁ ⛁ ⛁ ⛁ ⛀ ⛀ ⛀ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   Opus 4.7 (1M context)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   claude-opus-4-7[1m]
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   21.3k/1m tokens (2%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   Estimated usage by category
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System prompt: 8.8k tokens (0.9%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System tools: 11.4k tokens (1.1%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Memory files: 301 tokens (0.0%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Skills: 692 tokens (0.1%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛁ Messages: 13 tokens (0.0%)
                                               ⛶ Free space: 945.7k (94.6%)
                                               ⛝ Autocompact buffer: 33k tokens (3.3%)
     Auto-compact window: 1m tokens
     MCP tools · /mcp (loaded on-demand)
     Available
     ├ mcp__claude_ai_Gmail__authenticate
     ├ mcp__claude_ai_Gmail__complete_authentication
     ├ mcp__claude_ai_Google_Calendar__authenticate
     ├ mcp__claude_ai_Google_Calendar__complete_authentication
     ├ mcp__claude_ai_Google_Drive__authenticate
     └ mcp__claude_ai_Google_Drive__complete_authentication
     Memory files · /memory
     └ ~/.claude/projects/-Users-ren-repos-bonfire/memory/MEMORY.md: 301 tokens
     Skills · /skill-creator

---
**ASSISTANT** (2026-04-23T16:29):

  Looking at the /context output Ren shared, I can see the auto-compact window is set to 1m tokens as expected, but the 33k autocompact buffer doesn't clearly indicate whether the 42% override is actually being applied.

Let me work through the math here. The display shows 21.3k used, 945.7k free, and 33k reserved as the autocompact buffer—which adds up to the full 1m window. That 33k buffer represents the headroom kept after compaction triggers, meaning compaction kicks in around 967k tokens used. If the PCT override to 42% were working, I'd expect to see a much larger buffer (around 580k), but I'm not seeing that in the output, so it looks like `CLAUDE_CODE_AUTO_COMPACT_WINDOW` is being recognized but the percentage override might not be taking effect.

I'm also noticing there might be some confusion around variable names—both `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` and `CLAUDE_CODE_AUTO_COMPACT_WINDOW` appear in different sources, and based on the bswen article, the percentage calculation might interact with the window size in a non-obvious way that I need to understand better. The window variable is definitely working based on the output, but that 33k autocompact buffer still looks like the default rather than reflecting the PCT=42 override I set up. I should have the user verify by actually loading files and watching when compaction triggers, or I need to double-check whether the variable name itself is correct.
```
This block is not supported on your current device yet.
```

 I'm seeing two critical bugs here. The `/context` display is hardcoded to show the default 33k buffer size even when PCT_OVERRIDE changes the actual trigger threshold, which is misleading. And PCT_OVERRIDE can only lower the threshold from its ~83% default, not raise it—so setting PCT=42 is the constraint we're working with.

Let me verify the math: with the formula `min(floor(effectiveWindow * PCT/100), effectiveWindow - 13000)` and PCT=42 on a 1M token window, the actual compaction trigger lands at 420K tokens, which is correct. The display showing "Auto-compact window: 1m tokens" confirms the window size is being picked up properly, but the 33k buffer display is just a static artifact that doesn't reflect the real PCT setting.

So the honest answer for Ren: the window size IS applied and visible, but the buffer percentage shown is a display bug and won't match reality. The actual trigger should fire at 420K, which we can only verify by watching it happen in practice or checking the statusline, since the `/context` display won't show it accurately.Good news and annoying news.

**Good:** `CLAUDE_CODE_AUTO_COMPACT_WINDOW=1000000` is picked up — see the `Auto-compact window: 1m tokens` line at the bottom.

**Annoying:** The `Autocompact buffer: 33k tokens (3.3%)` shown in `/context` is **a display bug** — it's hardcoded to the default formula and ignores `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`. Your actual trigger *is* at 420K; the display just lies about it. Tracked as [claude-code#27189](https://github.com/anthropics/claude-code/issues/27189).

The real trigger formula (reverse-engineered):

```
threshold = min(floor(effectiveWindow * PCT/100), effectiveWindow - 13000)
         = min(floor(1_000_000 * 0.42), 987_000)
         = 420_000  ✓
```

So your config is working. The `/context` UI will keep showing that misleading 33k buffer forever until Anthropic fixes the display.

**To actually verify** (since `/context` won't tell you):
- Load a bunch of files, watch the `Messages` line climb past ~420k and see if compaction fires. It should.
- Or add a statusline hook that reads the real threshold — `claudefa.st` has a template, but honestly for your workflow probably not worth the bother.

**One caveat worth knowing:** `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` can only *lower* the threshold below the ~83% default, never raise it (bug #31806 — `Math.min` clamp). You're setting 42%, which is well below 83%, so you're fine. If you ever wanted to push compaction to 90%, that silently wouldn't work.

---
**HUMAN** (2026-04-23T16:30):

supporting evidence?

---
**ASSISTANT** (2026-04-23T16:30):

  I need to back up my claims with actual evidence from the GitHub issues I found. Let me pull the specific citations for the display bug in #27189, the threshold formula details, and the 83% cap from #31806 so Ren can verify these directly.Three sources, all from my earlier searches:

**1. The `/context` display bug** — [claude-code#27189](https://github.com/anthropics/claude-code/issues/27189):

The /context command always displays the default autocompact buffer size (~33K tokens at 200K context), even when CLAUDE_AUTOCOMPACT_PCT_OVERRIDE is set. The env var correctly affects the actual autocompact trigger, but the display is wrong.

The issue also includes the reverse-engineered code path — the function that decides when to fire autocompact reads CLAUDE_AUTOCOMPACT_PCT_OVERRIDE and computes: threshold = min(floor(effectiveWindow * PCT/100), effectiveWindow - 13000) — while the display code path never calls the function that reads CLAUDE_AUTOCOMPACT_PCT_OVERRIDE. It hardcodes the default formula.

**2. The 83% upward clamp** — [claude-code#31806](https://github.com/anthropics/claude-code/issues/31806):

CLAUDE_AUTOCOMPACT_PCT_OVERRIDE is documented as allowing users to control when auto-compaction triggers, but it can only lower the threshold below the default — never raise it. Setting it to 95 (meaning "compact at 95% usage") has no effect because of a Math.min clamp in the threshold calculation.

**3. The 13k response buffer explanation** — TurboAI's reverse-engineering guide corroborates the formula and explains why the clamp exists: The ~83% cap exists because Claude Code reserves a buffer of approximately 13,000 tokens for response generation. On a 200K token context window, 83% equals ~166K tokens used, leaving ~34K for the response + system overhead.

Note the `- 13000` in the formula matches this reserve exactly.

**What I'm *not* directly citing** is the claim that your specific `/context` output confirms the window var is applied. That's my inference from the `Auto-compact window: 1m tokens` line at the bottom of your paste — which matches what v2.1.91 showed in [#43989](https://github.com/anthropics/claude-code/issues/43989) before the regression, so it's a reasonable read but not formally documented anywhere I found.

All three issues are open or closed-as-duplicate as of the searches (Feb–Mar 2026), so the behavior should still hold in current versions unless Anthropic shipped a fix in the last few weeks. If you want to be paranoid, the empirical test — fill context past 420K and watch — is the only ground truth.
