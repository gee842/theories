from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-coupling.txt','Coupling.lean: the record of a course kept (Experiment\'s sense); refutes a reading → excludes it (as the module\'s own `excludes`); registering → reading; the part\'s registration → its couplings.','lean:Coupling',L+'/Coupling.lean',[
("S5","read every move as its own and its record never refutes it;","read every move as its own and its record never excludes it;"),
("S1 the AI's reading","- Reading more, more is one's own: registering what forms a move makes the move formed through\n  what one is.","- Reading more, more is one's own: reading what forms a move makes the move formed through\n  what one is."),
("S2","the counterfactual's act read through the part's own\nregistration (`ExchangeLaw.Through`","the counterfactual's act read through the part's own\ncouplings (`ExchangeLaw.Through`"),
("S5","/-- **A recurrence with the move varied refutes the reading.** -/","/-- **A recurrence with the move varied excludes the reading.** -/"),
])
gen(D+'/edits/lean-exactrecordrunsinherited.txt','ExactRecordRunsInherited.lean: a run\'s registered record → the prefix of its course through a map (L-prefix, as ExactRecordRuns); the evidence\'s target kept (KnowledgeCorrespondence\'s term).','lean:ExactRecordRunsInherited',L+'/ExactRecordRunsInherited.lean',[
("L-prefix","# Exact readings of a run's registered record: the condition of resolution","# Exact readings of a run's prefix through a map: the condition of resolution"),
("L-prefix","the record a registration\nleaves along a run before step `t` as evidence","the prefix before step `t`\nof a run's course through a map as evidence"),
("L-prefix","Some reading of the record is exact","Some reading of the prefix is exact"),
("L-prefix","domain with one record before `t` have one value at `t`","domain with one prefix before `t` have one value at `t`"),
])
gen(D+'/edits/lean-sensitivitywebs.txt','SensitivityWebs.lean: the registrations of a web → its couplings; registering what it is sensitive to → the coupling of it (as Sensitivity).','lean:SensitivityWebs',L+'/SensitivityWebs.lean',[
("S2","the registrations of a web it reads through (`ExchangeLaw.Through`)","the couplings of a web it reads through (`ExchangeLaw.Through`)"),
("S2","does not read through registering what it is sensitive\n  to","does not read through the coupling of what it is sensitive\n  to"),
])
gen(D+'/edits/lean-boundaries.txt','Boundaries.lean: feedback registers → carries (as Feedback).','lean:Boundaries',L+'/Boundaries.lean',[
("S7","its own feedback registers at most its influence closure","its own feedback carries at most its influence closure"),
])
gen(D+'/edits/lean-contactcourses.txt','ContactCourses.lean: a registration through addressed contacts → the lumping through them (as Contacts); `blind_*` names in the names table.','lean:ContactCourses',L+'/ContactCourses.lean',[
("S1","`Becoming.Contacts` states what a registration through addressed contacts selects","`Becoming.Contacts` states what a lumping through addressed contacts selects"),
])
gen(D+'/edits/lean-mechanism.txt','Mechanism.lean: does not register → does not show.','lean:Mechanism',L+'/Mechanism.lean',[
("S7","A change of mechanism at a projected configuration not yet met does not\nregister before it happens. -/","A change of mechanism at a projected configuration not yet met does not\nshow before it happens. -/"),
])
gen(D+'/edits/lean-refinement.txt','Refinement.lean: a law read through a registration → through a map (S1).','lean:Refinement',L+'/Refinement.lean',[
("S1","determined law read through a registration (`Law.sameFuture_iff_classes`","determined law read through a map (`Law.sameFuture_iff_classes`"),
])
gen(D+'/edits/lean-typicality.txt','Typicality.lean: a record registers one course → shows one course (the record of a run kept).','lean:Typicality',L+'/Typicality.lean',[
("S7","A record registers one course, never a weight.","A record shows one course, never a weight."),
])
