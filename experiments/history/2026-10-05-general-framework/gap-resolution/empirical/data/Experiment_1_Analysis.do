set more off
clear
capture log close
/*Set working Directory here if necc.*/
*cd ""

log using "output/Experiment_1_results.log", replace text
set seed 10242004
set scheme s1color

use "Experiment_1.dta"

/*Create total earnings and quiz performance summary data. 
(These statistics appear in the "Implementation Details" Section of the Paper */
gen session_subject = session+"_"+string(subject)
gen earnings = 20+8*g_totcontributedtopg -4*e_biginvestment if z_isenforcer == 1
replace earnings = (20-12*p_contributedtopg) + 8*g_o_otherconttopg - 24*p_ispunished if z_isenforcer == 0

collapse (sum) earnings  (mean) p_totquizscore p_quiz*, by(session_subject)
gen earnings_in_dollars = 7+earnings/30
egen quizscore = rsum(p_quiz1-p_quiz8)
summ earnings_in quizscore
tab quizscore
clear

use "Experiment_1.dta"

/* Generate Group, period, session indicator. used for clustering*/
egen g_p_s=group(group period session)

/* Generate Enforcement rule dummies*/
gen g_acc_low=g_accuracy==0
label var g_acc_low "Low accuracy"
gen g_acc_med=g_accuracy==1
label var g_acc_med "Medium accuracy"
gen g_acc_high=g_accuracy==2
label var g_acc_high "High accuracy"
gen e_enf_everyone=e_enforcementrule ==1
label var e_enf_everyone "Enforcement=Punish everyone"
gen e_enf_PATS=e_enforcementrule ==2
label var e_enf_PATS "Enforcement=Punish accused"
gen e_enf_antiPATS=e_enforcementrule ==3
label var e_enf_antiPATS "Enforcement=Punish innocents"

/*Table of authority choices -- Data for Table 1 in Paper*/
tab e_biginvestment e_enforcementrule  if z_isenforcer==1

/* Graph of average group contributions by period -- Figure 2 in the paper */
gen g_jittercont = g_totcontributedtopg + 0.4*uniform()-0.2 if z_isenforcer==1
#delimit;
twoway 
(lpolyci g_totcontributedtopg period if z_isenforcer ==1, lcolor(black) lpattern(dash) blcolor(none))
(scatter g_jittercont period if z_isenforcer ==1,msymbol(circle_hollow)) ,
/*title("Figure 1: Average Group Contributions by Period") */
ytitle("Contributions") 
ylabel(0(1)4, labsize(small) angle(horizontal) glcolor(gs12) grid) 
/*x-axis options*/
xtitle("Period", alignment(bottom)) 
xlabel(1(1)20, labsize(small)) 
/*General*/
xsize(3.5) ysize(3.5) 
aspectratio(1)
graphregion(fcolor(white) lcolor(white) ifcolor(white) ilcolor(white)) 
plotregion(fcolor(white) lcolor(black) ifcolor(white) ilcolor(white))
legend(off)
name(contovertime,replace);
graph export "output/Figure 2.pdf", as(pdf) replace;
#delimit cr

/*Graph Group-level contributions by accuracy and investment levels given PATS
enforcement strategy -- Figure 3 in the paper */
preserve
keep if z_isenforcer==1 & e_enf_PATS==1

matrix results = J(2,8,.)
bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 0 & g_accuracy == 0
matrix results[1,1]= e(b)
matrix temp = e(ci_percentile)
matrix results[1,2]= temp[1,1]
matrix results[1,3]= temp[2,1]
bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 0 & g_accuracy == 1
matrix results[1,4]= e(b)
matrix temp = e(ci_percentile)
matrix results[1,5]= temp[1,1]
matrix results[1,6]= temp[2,1]
ttest g_totcontributedtopg if e_biginvestment == 0, by( g_acc_med) unequal
matrix results[1,7]= -r(t)*r(se)
matrix results[1,8]= r(p)

bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 1 & g_accuracy == 1
matrix results[2,1]= e(b)
matrix temp = e(ci_percentile)
matrix results[2,2]= temp[1,1]
matrix results[2,3]= temp[2,1]
bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 1 & g_accuracy == 2
matrix results[2,4]= e(b)
matrix temp = e(ci_percentile)
matrix results[2,5]= temp[1,1]
matrix results[2,6]= temp[2,1]
ttest g_totcontributedtopg if e_biginvestment == 1, by( g_acc_high) unequal
matrix results[2,7]= -r(t)*r(se)
matrix results[2,8]= r(p)

svmat results
rename results1 mean0
rename results2 lb0
rename results3 ub0
rename results4 mean1
rename results5 lb1
rename results6 ub1
rename results7 diff
rename results8 pvalue

gen cat = "Small Investment" in 1
replace cat = "Big Investment" in 2

gen n = 1 in 1
gen n2 = 2.5 in 1
replace n = 4 in 2
replace n2 = 5.5 in 2

gen n3= (n+n2)/2
gen difflab = "diff. = "+string(round(diff,.001))
replace difflab = "diff. = 0"+string(round(diff,.001)) in 2/3
gen diffheight = 4
gen plab = "p = 0"+ string(round(pvalue,.001))
replace plab = "p < 0.001" if pvalue<0.001
gen pheight = 3.8
replace diffheight = 3.3 in 1
replace pheight = 3.1 in 1
replace difflab = "diff. = 0"+string(round(.405,.001)) in 3
replace n3 = 3.25 in 3
replace diffheight = 3.7 in 3
replace pheight = 3.5 in 3
replace plab = "p = 0"+ string(round(0.0079,.001)) in 3
l difflab in 1/10
#delimit;
twoway (bar mean0 n in 1, fcolor(white) lcolor(gs5) lwidth(thin)) 
(bar mean0 n in 2, fcolor(gs5) lcolor(gs5)) 
(bar mean1 n2 in 1, fcolor(gs12) lcolor(gs12))
(bar mean1 n2 in 2, fcolor(black) lcolor(black))
(rcap lb0 ub0 n in 1/3,lcolor(black)) (rcap lb1 ub1 n2 in 1/3,lcolor(black))
(scatter diffheight n3, mcolor(white) msize(zero) mlabel(difflab) mlabcolor(black) mlabposition(0))
(scatter pheight n3, mcolor(white) msize(zero) mlabel(plab) mlabcolor(black) mlabposition(0)),
ylabel(0(1)4, labsize(small) labgap(tiny) angle(horizontal) nogrid)
yscale(titlegap(2) outergap(0)) 
/*x-axis options*/
xscale(titlegap(2) outergap(0)) 
xlabel( 1 `" "1. Low Accuracy" "Small Investment" "' 2.5 `" "2. Medium Accuracy" "Small Investment" "' 
4 `" "3. Medium Accuracy" "Big Investment" "' 5.5 `" "4. High Accuracy" "Big Investment" "', noticks labsize(vsmall)) 
xtitle("")
/*General*/
yline(1(1)4, lcolor(gs12) lwidth(vvthin))
ytitle("Average Group Contribution")
xsize(2.5) ysize(2.5) 
aspectratio(1) 
graphregion(margin(small) fcolor(white) lcolor(white) ifcolor(white) ilcolor(white)) 
plotregion(margin(small) fcolor(white) lcolor(white) ifcolor(white) ilcolor(white))
name(bargraph, replace)
legend(off);
#delimit cr
graph export "output/Figure 3.pdf", as(pdf) replace
restore

/* Extrinsic Accuracy Effects -- in text of paper */
ttest g_totcontributedtopg if z_isenforcer == 1 & e_enf_PATS==1 & e_biginvestment ==0, by(g_accuracy) unequal
ttest g_totcontributedtopg if z_isenforcer == 1 & e_enf_PATS==1 & e_biginvestment ==1, by(g_accuracy) unequal

/* Regression Analysis for Robustness -- Table 3 in the paper */
* Individual-level analysis; base specification
regress p_contributedtopg e_biginvestment if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2, robust cluster(g_p_s)
outreg2 using "output/Table 3.tex", replace bracket se asterisk(se) bdec(3) 
* period dummies
regress p_contributedtopg e_biginvestment pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2, robust cluster(g_p_s)
outreg2 using "output/Table 3.tex", bracket se asterisk(se) bdec(3)
* Player's experience with average group contributions
regress p_contributedtopg e_biginvestment p_g_avglagcontpg pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2, robust cluster(g_p_s)
outreg2 using "output/Table 3.tex", bracket se asterisk(se) bdec(3)
* Player's experience with average levels of big investment
regress p_contributedtopg e_biginvestment p_avglagbiginvest pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2, robust cluster(g_p_s)
outreg2 using "output/Table 3.tex", bracket se asterisk(se) bdec(3)
* Ever been enforcer
regress p_contributedtopg e_biginvestment pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2 & p_everenforcerbefore==1, robust cluster(g_p_s)
outreg2 using "output/Table 3.tex", bracket se asterisk(se) bdec(3)
* Testing for effect of comprehension using the quiz score
regress p_contributedtopg e_biginvestment pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2 & p_totquizscore>=7, robust cluster(g_p_s) 
outreg2 using "output/Table 3.tex", bracket se asterisk(se) bdec(3)
* individual-level analysis, with person-level fixed effects
* restrict this fixed effects model to cases where the person actually appears multiple times in different investment levels
bysort unique_person_id: egen ct=count(p_contributedtopg) if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2
bysort unique_person_id: egen maxinv=max(e_biginvestment) if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2
bysort unique_person_id: egen mininv=min(e_biginvestment) if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2
* Subject fixed effects
xtreg p_contributedtopg e_biginvestment if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2 & ct>1 & maxinv~=mininv, fe i(unique_person_id) robust
outreg2 using "output/Table 3.tex", bracket se asterisk(se) bdec(3)
* Subject fixed effects and period dummies
xtreg p_contributedtopg e_biginvestment p_g_avglagcontpg p_avglagbiginvest pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2 & ct>1 & maxinv~=mininv, fe i(unique_person_id) robust
outreg2 using "output/Table 3.tex", bracket se asterisk(se) bdec(3)

/* Effect of Legitimating Action over Time -- Figure 4 in paper */
#delimit;
twoway (scatter g_jittercont period if z_isenforcer ==1 & e_enforcementrule==2 & g_accuracy==1 & e_biginvestment==1, mcolor(navy) yline(1 2 3, lcolor(gs12) lwidth(thin))) 
(lpoly g_totcontributedtopg period if z_isenforcer ==1 & e_enforcementrule==2 & g_accuracy==1 & e_biginvestment==1, lcolor(black) lpattern(solid)) 
(scatter g_totcontributedtopg period if z_isenforcer ==1 & e_enforcementrule==2 & g_accuracy==1 & e_biginvestment==0, mcolor(navy) msymbol(circle_hollow) yline(1 2 3, lcolor(gs12) lwidth(vvthin))) 
(lpoly g_totcontributedtopg period if z_isenforcer ==1 & e_enforcementrule==2 & g_accuracy==1 & e_biginvestment==0, lcolor(black) lpattern(dash)), 
ytitle("Contributions")  ylabel(0(1)4, labsize(small) angle(horizontal)) 
xtitle("Period", alignment(bottom)) 
xlabel(1(1)20, labsize(small)) xsize(3.5) ysize(3.5) 
graphregion(fcolor(white) lcolor(white) ifcolor(white) ilcolor(white)) 
plotregion(fcolor(white) lcolor(black) ifcolor(white) ilcolor(white)) 
legend(order(- "" 1 "" 2 "Big Investment" - "" 3 "" 4 "Small Investment") rows(2) size(small)  ring(0) position(8)) name(legittime,replace);
graph export "output/Figure 4.pdf", as(pdf) replace;
#delimit cr

/* Effect of Legitimating Action, first 10 and last 10 periods (discussed in text) */
regress p_contributedtopg e_biginvestment pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2 & period<=10, robust cluster(g_p_s)
regress p_contributedtopg e_biginvestment pd_* if z_isenforcer==0 & g_accuracy == 1 & e_enforcementrule ==2 & period>10, robust cluster(g_p_s)

log close
