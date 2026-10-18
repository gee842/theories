from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-stock.txt','Stock.lean: a registration process run jointly with the stock → a process `R` run jointly with it (any process; Revising\'s link process is one); "observable" kept (the systems term).','lean:Stock',L+'/Stock.lean',[
("S1","For a registration process run jointly with\n  its stock, a course is executable exactly when the registration admits it and the stock\n  covers it","For a process run jointly with\n  its stock, a course is executable exactly when that process admits it and the stock\n  covers it"),
("S1","for any registration cycle run jointly with it,","for any cycle of a process run jointly with it,"),
("S1","An unending course of a registration process is carried","An unending course of a process is carried"),
("S1","/-- **Registration and stock, run jointly.** A course is executable exactly where the\nregistration process admits it and the stock covers it. -/","/-- **A process and stock, run jointly.** A course is executable exactly where the\nprocess `R` admits it and the stock covers it. -/"),
("S1","/-- **A registration cycle carried by stock.** Where a course returns the registration\nprocess to where it began,","/-- **A cycle carried by stock.** Where a course returns the process `R` to where it\nbegan,"),
("S1","A run of a registration process can be run","A run of a process `R` can be run"),
])
gen(D+'/edits/lean-gluing.txt','Gluing.lean: registrations in context → what the contexts show (S7, as Context); a context registers the claims it counts → they lie within it; the record id `contextual-registration` kept (ids are frozen).','lean:Gluing',L+'/Gluing.lean',[
("S7","fits a world exactly where its\nregistrations glue,","fits a world exactly where what its\ncontexts show glues,"),
("S7 the record's id stays","the next step of the record\nof contextual registration,","the next step of the record\nof claims shown in context (`contextual-registration`),"),
("S7","and which registrations of an actual unfolding are of this kind.","and which contextual systems of an actual unfolding are of this kind."),
("S7","/-- A context registers the claims it counts. -/","/-- The claims a context counts lie within it. -/"),
("S7","/-- What a context can show depends only on the claims it registers. -/","/-- What a context can show depends only on the claims within it. -/"),
("S7","some world registering what each context counts,","some world showing what each context counts,"),
("S7","/-- A pair of settings registers the outcome at each station under its setting,","/-- A pair of settings holds the outcome at each station under its setting,"),
("S7","each outcome is registered twice,","each outcome lies within two pairs,"),
])
gen(D+'/edits/lean-timedresponse.txt','TimedResponse.lean: past registration → past couplings (S2); explicitly observed → coupled by level.','lean:TimedResponse',L+'/TimedResponse.lean',[
("S2","the rest responds through its past registration.","the rest responds through its past couplings."),
("S2","/-- The condition enters support at this step, or is explicitly observed. Unlike\nthe whole-history registration envelope,","/-- The condition enters support at this step, or couples in by level. Unlike\nthe whole-history coupling envelope,"),
("S2","/-- Potential propagation, retaining the order of exchanges and past registration.","/-- Potential propagation, retaining the order of exchanges and past couplings."),
("S2","/-- A potential source route has entered something the reader registers by T. -/","/-- A potential source route has entered something that couples into the reader by T. -/"),
("S2","/-- Equality of registered levels suffices for the native registration, including support. -/","/-- Equality of the levels that couple in suffices for alikeness through the couplings, including\nsupport. -/"),
("S2","Factoring through complete registration is supplied.","Factoring through the complete couplings is supplied."),
("S2","passing through registration does not ensure use.","passing through the couplings does not ensure use."),
])
