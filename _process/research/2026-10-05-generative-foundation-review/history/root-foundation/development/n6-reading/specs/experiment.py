from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-experiment.txt','Experiment.lean: the run\'s record kept (physical sense); a model refuted by a run → excluded (S5, as Branching and Testing); registered → read; `varied_refutes` is a name, in the names table.','lean:Experiment',L+'/Experiment.lean',[
("S1","and fixes nothing where it does not, even with every configuration registered:","and fixes nothing where it does not, even where the whole configuration is read:"),
("S5","the wrong model is admitted at every step and never refuted\n  (`Confound.confounded`); varying the move against it, a later step refutes the model,","the wrong model is admitted at every step and never excluded\n  (`Confound.confounded`); varying the move against it, a later step excludes the model,"),
("S5 the AI's reading (D25)","what the reading leaves out is what can refute a wrong control; acts in step with it never refute\nit. With the registration of `Becoming.Testing` as the reading, an experiment through what registers\nis right where the unfolding factors through what registers;",
 "what the reading leaves out is what can exclude a wrong control; acts in step with it never exclude\nit. With what couples into a formation (`Becoming.Testing`) as the reading, an experiment through\nwhat couples in is right where the unfolding factors through it;"),
("S1","and that what is fixed is\nregistered by anything other than","and that what is fixed is\nread by anything other than"),
("S1","the record up to `t` fixes no outcome of `b` at `s`, whatever\nregisters:","the record up to `t` fixes no outcome of `b` at `s`, whatever\nis read:"),
("S5","/-- **A confound is never refuted.**","/-- **A confound is never excluded.**"),
("S5","the record never refutes the wrong projection. -/","the record never excludes the wrong projection. -/"),
("S5","/-- **Varying the move against the hidden bit refutes the projection.**","/-- **Varying the move against the hidden bit excludes the projection.**"),
])
