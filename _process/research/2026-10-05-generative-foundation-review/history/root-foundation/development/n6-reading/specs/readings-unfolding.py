from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-readings.txt','Readings.lean: a contextual system\'s registrations → what its contexts show (S7, as Context); a reading registers a change → reads it; Ren\'s quoted "belief" kept.','lean:Readings',L+'/Readings.lean',[
("S7","Along a run, the registrations of a contextual\n  system (`Contextual`), each claim read with its context, are the relata of one world, each active\n  exactly where it is registered with its value",
 "Along a run, the claims of a contextual\n  system (`Contextual`), each read with its context, are the relata of one world, each active\n  exactly where its context shows it with its value"),
("S7","as for the Mermin–Peres square and quantum registrations","as for the Mermin–Peres square and what quantum states show"),
("S7","  the registrations glue at every configuration (`Contextual.fitsFree_iff` of `Becoming.Context`).","  what the contexts show glues at every configuration (`Contextual.fitsFree_iff` of `Becoming.Context`)."),
("S7","The two\n  register a change alike exactly where","The two\n  read a change alike exactly where"),
("S7","which fails for quantum\nregistrations;","which fails for what quantum\nstates show;"),
("S7","active exactly where its context registers it with its\nvalue.","active exactly where its context shows it with its\nvalue."),
("S7","/-- A context's registration is a relatum's activity. -/","/-- What a context shows is a relatum's activity. -/"),
("S7","/-- What each reading registers of the change of each condition across the step from `t`, as what\nit rose and what it fell: standing registers the rise and the fall of the level; exchange\nregisters what the flow gave beyond what it took, and took beyond what it gave. -/",
 "/-- What each reading reads of the change of each condition across the step from `t`, as what\nit rose and what it fell: standing reads the rise and the fall of the level; exchange\nreads what the flow gave beyond what it took, and took beyond what it gave. -/"),
("S7","/-- **Two readings register one change alike exactly where they balance.**","/-- **Two readings read one change alike exactly where they balance.**"),
])
gen(D+'/edits/lean-unfolding.txt','Unfolding.lean: a law read through a registration → through a map; registered future → future through the map (S1, as Identification); `section Registered` is a name, in the names table.','lean:Unfolding',L+'/Unfolding.lean',[
("S1","For a determined law read through a registration\n  (`Law.frameBy`), configurations are alike exactly where their registered futures are the\n  same (`Law.SameFuture`, `Law.alike_iff_sameFuture`), so there a description makes sense where\n  it identifies exactly the same registered futures,",
 "For a determined law read through a map\n  (`Law.frameBy`), configurations are alike exactly where their futures through the map are the\n  same (`Law.SameFuture`, `Law.alike_iff_sameFuture`), so there a description makes sense where\n  it identifies exactly the same futures through the map,"),
("S1","/-! ### A determined law: likeness is the same registered future -/","/-! ### A determined law: likeness is the same future through the map -/"),
("S1","/-- A determined law read through a registration: what is registered is what is claimed. -/","/-- A determined law read through a map: the map's value is what is claimed. -/"),
("S1","/-- The law read through a registration is determined. -/","/-- The law read through a map is determined. -/"),
("S1","the same registered future","the same future through the map"),
("S1","/-- The same registered future is a bisimulation. -/","/-- The same future through the map is a bisimulation. -/"),
("S1","their registered futures are\nthe same.**","their futures through the map are\nthe same.**"),
])
