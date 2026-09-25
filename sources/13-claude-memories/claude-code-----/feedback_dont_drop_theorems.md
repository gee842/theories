---
name: dont-drop-theorems-for-sorry-count
description: "When a proof is hard, prove it — don't drop the theorem to avoid sorry. Generality matters more than mechanical sorry-count."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b62fd195-20c8-42c8-bfa2-df395d75b9c9
---

When a theorem is hard to prove in Lean, **prove it** — don't reach for "drop the theorem and rely on examples" as a way to keep the sorry-count at 0. General theorems are load-bearing; concrete examples don't substitute for them.

**Why:** A sorry-count of 0 is a means, not an end. The end is *the theorems being true and proved*. Mechanically deleting hard theorems trades real generality for a vanity metric. Examples can supplement but never replace a general statement when the user wants the general statement.

**How to apply:** If a Lean proof is technical/lengthy, attempt it (search Mathlib, use `apply List.ext_get` / `List.ofFn_get` style decompositions, try `simp` chains, native_decide for small finite cases). Only drop a theorem if the *math* is wrong or the *user* explicitly opts to omit it. Never drop just because the proof is annoying. If stuck after honest effort, surface "this needs X tactic / lemma — should I keep iterating or table it?" — don't unilaterally delete.

User correction quote (2026-05-16): "我们要一般定理, 0 sorry 不要这样机械执行"
