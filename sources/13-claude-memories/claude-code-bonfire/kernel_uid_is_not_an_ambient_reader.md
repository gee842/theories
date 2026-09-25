---
name: kernel-uid-is-not-an-ambient-reader
description: "kernel.uid is the opaque root principal, not the system read caller; use the principal that owns the surface"
metadata:
  node_type: memory
  type: project
  originSessionId: 70c08fc7-6dcc-4191-9cb3-cd72cb328ec2
  modified: 2026-08-15T01:07:31.586Z
---

`kernel.uid` is a concrete principal. It is the structural root, but it is **not** the ambient system-read caller and does not automatically see community-held rows. A denied `rt.yi.read(row, kernel.uid)` returns `null`, the same surface result as absence.

Use the principal that owns the operation's surface. A community-installed wall or book acts as the community uid; a holder reads their own holdings as themself. Reserve `kernel.uid` for genuinely kernel-owned rows or an operation whose authority contract explicitly admits the root. Do not substitute it for the internal system caller.

This matters for helpers such as `crystallize` and `compost`, which first read the source and report `source item <uid> not found` when the chosen caller cannot see it. The current `docs/examples/witness-book/index.ts` demonstrates the correct posture: the community reads and crystallizes the Need, while each witness queries their own keepsakes.

When a newly written row appears missing or a count unexpectedly reads zero, check the reader principal before debugging the write.
