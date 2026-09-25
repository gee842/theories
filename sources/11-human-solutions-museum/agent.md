# Agent Working Rules

## Confirmation Boundary

- If the user asks for judgment, explanation, strategy, or a plan, answer first and do not modify files.
- Treat phrases such as "怎么看", "咋办", "解释一下", "给我方案", and "继续聊" as discussion requests unless the user explicitly authorizes execution.
- Only mutate the workspace after the user clearly asks to do so, for example with "开始做", "写入", "创建", "修改", "执行", "提交", or "commit".
- Before making file edits, state what will be changed and wait if the request is ambiguous.
- Do not repeat the mistake of turning an exploratory answer into implementation without confirmation.

## Git Boundary

- `git commit` is allowed only when the user explicitly asks for a commit.
- Do not push, merge, reset, delete, or otherwise change git state unless explicitly requested.

## Current Project Context

- The project is currently being shaped from concept documents into a static interactive web experience.
- Discussion should first clarify content structure, product direction, and implementation plan.
- Implementation should begin only after the user confirms the proposed direction.
