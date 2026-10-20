from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-quantum.txt','Quantum.lean: a quantum registration → what a quantum state shows (`Shows`), a line measured jointly; "observable" kept (the physical term).','lean:Quantum',L+'/Quantum.lean',[
("S7","as claims\nregistered in context: nine cells (`Square.Cell`), six lines (`Square.Line`), each line a context\nregistering its three cells,","as claims\nshown in context: nine cells (`Square.Cell`), six lines (`Square.Line`), each line a context\nholding its three cells,"),
("S7","This module gives the quantum registrations that realize the square.","This module gives the quantum states and observables that realize the square."),
("S7","(`obs_sq`), so it registers one of\n  two values,","(`obs_sq`), so it shows one of\n  two values,"),
("S7","so a line is a context that can be registered together,","so a line is a context that can be measured jointly,"),
("S7","* **The registrations.** Each observable","* **What a state shows.** Each observable"),
("S7","* **Quantum registrations are contextual.**","* **What quantum states show is contextual.**"),
("S7","Within each context the registrations are\n  definite","Within each context what is shown is\n  definite"),
("S7","/-- Every observable squares to the identity, so it registers `+1` or `-1`. -/","/-- Every observable squares to the identity, so it shows `+1` or `-1`. -/"),
("S7","/-! ## The registrations -/","/-! ## What a state shows -/"),
("S7","sends it to itself with that sign: a registration of the cell's observable with value `b`. -/","sends it to itself with that sign: the cell's observable measured with value `b`. -/"),
("S7","/-- Registered jointly at three cells,","/-- Shown jointly at three cells,"),
("S7","/-- **Quantum registrations keep each","/-- **What quantum states show keeps each"),
("S7","/-- A row's joint registration with the values","/-- A state showing on a row the values"),
("S7","/-- A column's joint registration with the values","/-- A state showing on a column the values"),
("S7","/-- A line's joint registration with the values","/-- A state showing on a line the values"),
("S7","/-! ## Lines: the registrations are the supports,","/-! ## Lines: what is shown is a support,"),
("S7","/-- **Quantum registrations are contextual.**","/-- **What quantum states show is contextual.**"),
])
