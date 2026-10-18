from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-revisionruns.txt','RevisionRuns.lean: the history of a run\'s registrations → of its lumpings (S1, as Revision).','lean:RevisionRuns',L+'/RevisionRuns.lean',[
("S1","history of a run's registrations","history of a run's lumpings"),
("S1","`Becoming.Revision` states that registering through a jointly retained old and new reading gains","`Becoming.Revision` states that lumping through a jointly retained old and new reading gains"),
("S1","`Revising.P`, that the registration with the link unformed cannot select","`Revising.P`, that the lumping with the link unformed cannot select"),
("S1","the history\nof the run's registrations through every step","the history\nof the run's lumpings through every step"),
("S1","the response false keeps the registration. -/","the response false keeps the lumping. -/"),
])
gen(D+'/edits/lean-tail.txt','Tail.lean: the least registration → the least coupling (as Sensitivity); "refutes" of a logical step kept.','lean:Tail',L+'/Tail.lean',[
("S2","the least registration","the least coupling"),
("S2","the\n  least registration","the\n  least coupling"),
("S2","the registrations it reads through have no least one","the couplings it reads through have no least one"),
("S2","/-- It reads through registering the conditions from any one on. -/","/-- It reads through the coupling of the conditions from any one on. -/"),
("S2","/-- **The registrations it reads through have no least one.**","/-- **The couplings it reads through have no least one.**"),
("S2","the law does not read through registering nothing. -/","the law does not read through the coupling of nothing. -/"),
])
