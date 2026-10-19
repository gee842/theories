#!/usr/bin/env python3
"""R25 (a): scope and order in AGENTS.md, the README lead and OPENING's AI-written footnotes
(twentieth review F5, D8). Writes edits_a_other.json for sub.py."""
import json
E = []
def r(p, old, new):
    E.append([p, old, new])

r('AGENTS.md',
  "The condition by itself orders nothing (mixed parts stay unordered, and every narrowing loses something); what ranks lies in calling widening better (C) and in the step of invariance, so never write that the ethics \"derives\" from the condition without saying this.",
  "The condition by itself orders nothing (mixed parts stay unordered, and every narrowing loses something): it fixes scope, whose losses count, and its content beyond the self's presupposition, the step of invariance, extends that scope to losses that return to no one. What ranks lies in calling widening better (C) alone. So the ethics rests on two premises with two roles, the condition for scope and C for order; name both wherever the ethics is summarized, and never write that the ethics \"derives\" from the condition without saying this.")

r('_process/navigation/README-LEAD.md',
  "With explicit practical commitments, the condition yields reasons addressed to every situated intelligence and a direction for AI alignment. The warrant of the condition is open, and so are the warrant of comparison by widening (C, which holds on level paths by definition) and of the step of invariance from what one's own continuation needs to the continuation of anything.",
  "The ethics rests on two premises with two roles: the condition fixes scope, whose losses count, and comparison by widening (C, which holds on level paths by definition) alone orders. With both and explicit practical commitments, the theory gives reasons addressed to every situated intelligence and a direction for AI alignment. The warrant of each premise is open: of C, and of the condition's step of invariance from what one's own continuation needs to the continuation of anything.")

r('theories/becoming/OPENING.md',
  "Acting on significance, through reasons, rankings and choices, also uses disclosed practical premises (A, L and the practical commitments on [the premise card](chapters/THE-THEORY-OF-BECOMING.md#0-前提卡--premise-card)). **Open:** the warrant of the condition and of its step of invariance;",
  "The condition fixes scope, whose losses count, and orders nothing; ranking uses comparison by widening (C), and acting on significance, through reasons and choices, also uses disclosed practical premises (A, L and the practical commitments on [the premise card](chapters/THE-THEORY-OF-BECOMING.md#0-前提卡--premise-card)). **Open:** the warrant of the condition and of its step of invariance, and the warrant of C;")

if __name__ == '__main__':
    json.dump(E, open(__file__.replace('.py', '.json'), 'w'), ensure_ascii=False, indent=0)
    print(len(E))
