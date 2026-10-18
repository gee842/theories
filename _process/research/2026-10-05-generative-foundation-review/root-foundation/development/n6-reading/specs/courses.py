from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-courses.txt','Courses.lean: a run\'s registrations at listed dates → the values a map takes at them (S1); the reach target and "observable" kept (local senses).','lean:Courses',L+'/Courses.lean',[
("S1","* **Fallible witnesses.** The registrations of a run at listed dates are fallible witnesses:","* **Fallible witnesses.** The values a map takes along a run at listed dates are fallible witnesses:"),
("S1","/-- `n` moves of a copy reading through a registration go along the orbit of its law. -/","/-- `n` moves of a copy reading through `read` go along the orbit of its law. -/"),
("S1","/-- **Registrations of a run at listed dates as fallible witnesses.** For every process and every\ntwo-valued registration, where two fault sets leave a common faithful date, no run's\nregistrations are explained",
 "/-- **The values a map takes along a run at listed dates as fallible witnesses.** For every\nprocess and every two-valued map, where two fault sets leave a common faithful date, no run's\nvalues through the map are explained"),
("S1","/-- **The registrations of every course tell two answers apart","/-- **The values of every course tell two answers apart"),
])
