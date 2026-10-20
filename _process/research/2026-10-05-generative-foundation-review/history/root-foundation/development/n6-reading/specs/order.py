from gen_edits import gen
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
gen(D+'/edits/lean-order.txt','Order.lean: the order registers → the order makes a difference (S7); `order_registers` is a name, in the names table.','lean:Order',L+'/Order.lean',[
("S7 the AI's reading (D30)","an idle step registers nothing, and removing it changes nothing","an idle step makes no difference, and removing it changes nothing"),
("S7","Within the order, what registers\nis the order of exchanges","Within the order, what makes a difference\nis the order of exchanges"),
("S7","/-- **The order of exchanges joined by a dependence registers.**","/-- **The order of exchanges joined by a dependence makes a difference.**"),
("S7","/-- **The order of exchanges sharing a relatum registers.**","/-- **The order of exchanges sharing a relatum makes a difference.**"),
("S7","/-! ### Where the order registers, every footprint joins the two exchanges -/","/-! ### Where the order makes a difference, every footprint joins the two exchanges -/"),
])
