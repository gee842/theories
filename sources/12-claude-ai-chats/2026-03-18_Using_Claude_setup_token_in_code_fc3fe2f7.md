# Using Claude setup token in code

created: 2026-03-18T09:55:58.703022Z  uuid: fc3fe2f7-aeea-4e38-b3cd-955fc7b345b7  export: old
messages: 2  total_chars: 2238  human_chars: 37

summary: **Conversation Overview**

The person asked how to use a Claude setup token in Claude Code. Claude researched the topic using web search and documentation tools, then provided a detailed explanation of the `claude setup-token` command. The conversation covered what the command does (generates a long-lived OAuth token for non-browser environments), who can use it (Pro and Max users), and step-by-step instructions for generating and deploying the token via the `CLAUDE_CODE_OAUTH_TOKEN` environment variable. Claude also covered common use cases including headless servers and CI/CD pipelines like GitHub Actions, and flagged a known bug where fresh containers may still trigger the onboarding wizard even with the token set, with the workaround of ensuring `~/.claude.json` contains `hasCompletedOnboarding: true`.

**Tool Knowledge**

Claude used `web_search` and `web_fetch` to retrieve up-to-date Claude Code authentication documentation, supplementing a local skill file check. The search query "Claude Code setup token authentication" returned relevant results. The official docs URL referenced was `https://code.claude.com/docs/en/authentication`. The docs map was fetched from `https://docs.anthropic.com/en/docs/claude-code/claude_code_docs_map.md` as a starting point for navigating Claude Code documentation structure.


---
**HUMAN** (2026-03-18T09:56):

use claude setup token in claude code

---
**ASSISTANT** (2026-03-18T09:56):

The user wants to know how to use a Claude setup token in Claude Code. Let me check the product self-knowledge skill for accurate information.Let me check the latest documentation on this, Ren.
```
This block is not supported on your current device yet.
```

Let me check the Claude Code docs map for setup token information.
```
This block is not supported on your current device yet.
```

Let me search for this.
```
This block is not supported on your current device yet.
```

Now I have good info on how to use `claude setup-token`.Here's how to use `claude setup-token` in Claude Code:

**What it does:** The `claude setup-token` command generates a long-lived OAuth authentication token that lets you use Claude Code in environments where browser-based login isn't possible (headless servers, CI/CD pipelines, GitHub Actions, etc.).

**Requirements:** Pro and Max users can generate this token by running `claude setup-token` locally.

**Steps:**

1. On a machine with a browser where Claude Code is already installed, run:
   ```
   claude setup-token
   ```

2. It will open a browser for OAuth authentication. Once complete, it outputs a token (valid for 1 year) that looks like `sk-ant-oat01-xxxxx...xxxxx`.

3. Export the token as an environment variable wherever you need it:
   ```bash
   export CLAUDE_CODE_OAUTH_TOKEN=<your-token>
   ```

**Common use cases:**

- **Headless servers / VPS:** On headless machines without a GUI, you can't authenticate via browser, so you generate the token on your local machine and transfer it via the environment variable. You'll also want a `~/.claude.json` file that marks onboarding as complete.

- **GitHub Actions (claude-code-action):** Add the token as a GitHub secret named `CLAUDE_CODE_OAUTH_TOKEN` and reference it in your workflow with `${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}`.

**Heads up:** There's been a known bug where starting Claude Code in a fresh container with only the exported token still triggers the onboarding wizard. If you hit that, make sure your `~/.claude.json` file has `hasCompletedOnboarding: true` set with the correct version number.

For the full authentication docs: https://code.claude.com/docs/en/authentication
