set more off
clear
capture log close
/*Set working Directory if necc.*/
*cd ""

log using "output/Experiment_2_results.log", replace text
set seed 10242004
set scheme s1color

use "Experiment_2.dta"
/*Create total earnings and quiz performance summary data. 
(These statistics appear in the "Implementation Details" Section of the Paper */
gen session_id = session+"_"+string(subject)
gen earnings = 20+8*g_totcontributedtopg*g_authoritypaidfrompg -4*e_biginvestment if z_isenforcer == 1
replace earnings = (20-12*p_contributedtopg) + 8*g_o_otherconttopg - 24*p_ispunished if z_isenforcer == 0
collapse (sum) earnings (mean) p_totquiz,by(session_id)
replace earnings=earnings/30+7
summ earnings p_tot
tab p_tot
clear

use "Experiment_2.dta"

* Group, period, session indicator. used for clustering
egen g_p_s=group(group period session)

/* Generate Enforcement rule dummies*/
gen g_acc_low=g_accuracy==0
label var g_acc_low "Low accuracy"
gen g_acc_high=g_accuracy==1
label var g_acc_high "High accuracy"
gen e_enf_everyone=e_enforcementrule ==1
label var e_enf_everyone "Enforcement=Punish everyone"
gen e_enf_PATS=e_enforcementrule ==2
label var e_enf_PATS "Enforcement=Punish accused"
gen e_enf_antiPATS=e_enforcementrule ==3
label var e_enf_antiPATS "Enforcement=Punish innocents"

/*Table of authority choices -- Data for Table 4 in the paper*/
tab e_big e_enforcementrule if z_isenforcer==1

/* Graph of average group contributions by period -- Figure 5 in paper */
gen g_jittercont = g_totcontributedtopg + 0.4*uniform()-0.2 if z_isenforcer==1
#delimit;
twoway 
(lpolyci g_totcontributedtopg period if z_isenforcer ==1, lcolor(black) lpattern(dash) blcolor(none))
(scatter g_jittercont period if z_isenforcer ==1, msymbol(circle_hollow)),
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
graph export "output/Figure 5.pdf", as(pdf) replace;
#delimit cr

/*Graph Group-level contributions by accuracy and investment levels given PATS
enforcement strategy -- Figure 6 in the paper */
preserve
matrix results = J(4,3,.)
keep if z_isenforcer==1 & e_enforcementrule==2
bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 0 & g_acc_low == 1 
matrix results[1,1]= e(b)
matrix temp = e(ci_percentile)
matrix results[1,2]= temp[1,1]
matrix results[1,3]= temp[2,1]
bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 1 & g_acc_low == 1 
matrix results[2,1]= e(b)
matrix temp = e(ci_percentile)
matrix results[2,2]= temp[1,1]
matrix results[2,3]= temp[2,1]
bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 0 & g_acc_high == 1 
matrix results[3,1]= e(b)
matrix temp = e(ci_percentile)
matrix results[3,2]= temp[1,1]
matrix results[3,3]= temp[2,1]
bootstrap r(mean), reps(1000) nodots nowarn: summ g_totcontributedtopg if e_biginvestment == 1 & g_acc_high == 1 
matrix results[4,1]= e(b)
matrix temp = e(ci_percentile)
matrix results[4,2]= temp[1,1]
matrix results[4,3]= temp[2,1]

svmat results
rename results1 mean0
rename results2 lb
rename results3 ub

gen n = 1 in 1
replace n = 2.5 in 2
replace n = 4 in 3
replace n = 5.5 in 4

gen difflab = "diff. = 0.46" in 1
replace difflab = "diff. = 0.12" in 2
gen labx = 1.75 in 1
replace labx = 4.75 in 2
gen laby = 4 in 1/2
gen plaby = 3.8 in 1/2
gen plab = "p = 0.049" in 1
replace plab = "p = 0.39" in 2

#delimit;
twoway (bar mean0 n in 1, fcolor(white) lcolor(gs5) lwidth(thin)) 
(bar mean0 n in 2, fcolor(gs12) lcolor(gs12)) 
(bar mean0 n in 3, fcolor(gs5) lcolor(gs5))
(bar mean0 n in 4, fcolor(black) lcolor(black))
(rcap lb ub n in 1/4,lcolor(black))
(scatter laby labx, mcolor(white) msize(zero) mlabel(difflab) mlabcolor(black) mlabposition(0))
(scatter plaby labx, mcolor(white) msize(zero) mlabel(plab) mlabcolor(black) mlabposition(0)),
ylabel(0(1)4, labsize(small) labgap(tiny) angle(horizontal) nogrid)
yscale(titlegap(2) outergap(0)) 
/*x-axis options*/
xscale(titlegap(2) outergap(0)) 
xlabel( 1 `" "Low Accuracy" "Small Investment" "' 2.5 `" "Low Accuracy" "Big Investment" "' 
4 `" "High Accuracy" "Small Investment" "' 5.5 `" "High Accuracy" "Big Investment" "', noticks labsize(vsmall)) 
xtitle("")
/*General*/
yline(1(1)4, lcolor(gs12) lwidth(vvthin))
ytitle("Average Group Contribution")
fxsize(75) fysize(75)
aspectratio(1) 
graphregion(margin(small) fcolor(white) lcolor(white) ifcolor(white) ilcolor(white)) 
plotregion(margin(small) fcolor(white) lcolor(white) ifcolor(white) ilcolor(white))
name(bargraph_pooled, replace)
legend(off);
graph export "output/Figure 6.pdf", as(pdf) replace;
#delimit cr
restore

/*Legitimating Action Effects given low and high accuracy -- in text of paper */
ttest g_totcontributedtopg if g_acc_low==0 & z_isenforcer==1 & e_enforcementrule==2, by(e_biginvest) unequal
ttest g_totcontributedtopg if g_acc_low==1  & z_isenforcer==1 & e_enforcementrule==2, by(e_biginvest) unequal

/*Pooling across accuracy levels and compensation mechanisms -- Table 5 in paper*/
/*Generate interaction terms*/
gen biginvestXauthpaid = e_biginvest*g_authoritypaid
*Basic regression
regress p_contributedtopg e_biginvestment g_acc_high if z_isenforcer==0 & e_enforcementrule==2, robust cluster(g_p_s)
outreg2 using "output/Table 5.tex", replace bracket se asterisk(se) bdec(3) 
*Adds controls
regress p_contributedtopg e_biginvestment g_acc_high p_g_avglagcontpg p_avglagbiginvest pd_* if z_isenforcer==0 & e_enforcementrule==2, robust cluster(g_p_s)
outreg2 using "output/Table 5.tex", bracket se asterisk(se) bdec(3) 
*Interact with compensation mechanism but don't condition on accuracy
*Basic regression
regress p_contributedtopg e_biginvestment  g_acc_high g_authoritypaid biginvestXauthpaid if z_isenforcer==0 & e_enforcementrule==2, robust cluster(g_p_s)
outreg2 using "output/Table 5.tex",  bracket se asterisk(se) bdec(3) 
lincom e_biginvestment+biginvestXauthpaid
*Adds controls
regress p_contributedtopg e_biginvestment g_acc_high g_authoritypaid biginvestXauthpaid p_g_avglagcontpg p_avglagbiginvest pd_* if z_isenforcer==0 & e_enforcementrule==2, robust cluster(g_p_s)
outreg2 using "output/Table 5.tex", bracket se asterisk(se) bdec(3) 
lincom e_biginvestment+biginvestXauthpaid
