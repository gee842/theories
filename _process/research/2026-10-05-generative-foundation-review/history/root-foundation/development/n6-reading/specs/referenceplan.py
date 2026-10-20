from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-referenceplan.txt','ReferencePlan.lean: a rule registers a failed address → contacts it; unregistered → unanswered (as Contacts); the installed registration → the lumping on installed contacts; the channel\'s target values kept (local sense); `revise_registers_failure`, `frozen_blind` are names, in the names table.','lean:ReferencePlan',L+'/ReferencePlan.lean',[
("S1","The revision rule\nregisters every failed address (`propose_answers`, `revise_registers_failure`); the frozen\nrule is blind to what failed and leaves some failure unregistered at every retained method",
 "The revision rule\ncontacts every failed address (`propose_answers`, `revise_registers_failure`); the frozen\nrule does not read what failed and leaves some failure unanswered at every retained method"),
("S1","/-- The address domain of the installed registration.","/-- The address domain of the lumping on installed contacts."),
("S1","/-- Direct reuse of `Registration.keeps_iff`, not a second definition of registration-based\nselection. -/","/-- Direct reuse of `Registration.keeps_iff`, not a second definition of selection through a\nlumping. -/"),
("S1","/-- Only constructed and installed contacts participate in this registration. -/","/-- Only constructed and installed contacts participate in this lumping. -/"),
("S1","At every retained method, some failure is left\nunregistered by the frozen rule;","At every retained method, some failure is left\nunanswered by the frozen rule;"),
])
gen(D+'/edits/lean-referenceplantraces.txt','ReferencePlanTraces.lean: as ReferencePlan; a round registers a choice → gains the choice through its lumping; `revise_registers`, `frozen_leaves_unregistered`, `first_round_registers`, `second_round_registers` are names, in the names table.','lean:ReferencePlanTraces',L+'/ReferencePlanTraces.lean',[
("S1","so the revised method registers the failure (`revise_registers`),","so the revised method contacts the failed address (`revise_registers`),"),
("S1","method some failure is left unregistered (`frozen_leaves_unregistered`).","method some failure is left unanswered (`frozen_leaves_unregistered`)."),
("S1","install and register each new contact","install each new contact and gain its choice"),
("S1","/-- **A revise step's method registers the failure it answers.** -/","/-- **A revise step's method contacts the failed address it answers.** -/"),
("S1","/-- **At every retained method some failure is left unregistered by every frozen step.** -/","/-- **At every retained method some failure is left unanswered by every frozen step.** -/"),
("S1","/-- **The first round gains the registered choice at contact 0**, which the start did not\nregister. -/","/-- **The first round gains the choice at contact 0 through the installed contacts**, which the\nstart did not have. -/"),
("S1","/-- **The second round gains the registered choice at contact 1**, which the first repair did not\nregister. -/","/-- **The second round gains the choice at contact 1 through the installed contacts**, which the\nfirst repair did not have. -/"),
])
