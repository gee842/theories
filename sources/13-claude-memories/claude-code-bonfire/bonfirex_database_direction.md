---
name: bonfirex-database-direction
description: Exploratory authority-aware database direction for partially trusted humans, apps, and agents
metadata:
  node_type: memory
  type: project
  originSessionId: 1add0787-6e34-4b1d-8b5c-92d0123f37d5
---

This remains exploratory, not a shipped product decision: renovate Bonfire in
the same TypeScript/Postgres repo into an authority-aware database usable by
partially trusted humans, apps, and agents.

The design sentence is: **everything is a row; queries see; verbs act; you are
what you carry.** Reads should pass through one bounded query IR and visibility
folder; writes remain named verbs rather than raw SQL mutation. TypeScript
builder and text grammar may be co-equal skins, but neither may exceed the IR.

`docs/yi/50-surface-language-grammar.md` is the detailed exploration. Git now
tracks it even though its header still says “untracked”; its operative status
is “exploratory, not greenlit.” The planner/folder, scratch-kind on-ramp, text
parser, pg-wire gateway, and product control plane are not implemented.

Related: [[unified_mental_frame_direction]] [[ideal_yi_architecture]]
[[project_sdk_redesign_objective]].
