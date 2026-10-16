"""Render analytic constructed trajectories; no fitted or empirical data."""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
floor = 24/29
all_t, all_c, all_b = [], [], []
tests = []
c0, b0 = floor, 1.0
for k in range(8):
    t = np.linspace(0,1,151)
    u = 1 if k % 2 == 0 else 0
    if u:
        c = 6/7+(c0-6/7)*np.exp(-7*t)
        b = b0-t
    else:
        c = c0*np.exp(-t)
        b = b0+3*t
    all_t.extend(k+t)
    all_c.extend(c)
    all_b.extend(b)
    c0,b0 = float(c[-1]),float(b[-1])
    if u:
        tests.append((k+1,c0,b0))
assert all(c >= floor for _,c,_ in tests)
assert min(all_b) >= -1e-12
assert min(all_c) < floor
assert abs(b0-9) < 1e-12
periodic_high = (6/7)*(1-math.exp(-7))/(1-math.exp(-8))

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
    "axes.spines.top":False,"axes.spines.right":False,
    "axes.labelcolor":"#26364A","text.color":"#172B42",
    "xtick.color":"#465467","ytick.color":"#465467"})
fig,axs = plt.subplots(2,1,figsize=(11.6,7.3),sharex=True,
                       gridspec_kw={"height_ratios":[1.15,1]})
fig.patch.set_facecolor("#FAFBFD")
blue,orange = "#2168A0","#BD6224"
for ax in axs:
    ax.set_facecolor("#FAFBFD")
    ax.grid(axis="y",color="#DDE3EB",linewidth=.6)
    ax.axvline(5,color="#7D8793",linestyle=":",linewidth=1.2)
    ax.set_xlim(0,8)

axs[0].plot(all_t,all_c,color=blue,lw=2.3,label="Maintenance timed to scheduled tests")
axs[0].plot([0,5],[floor,floor],color=orange,lw=3.3,
            label="Continuous-readiness optimum (ends at t = 5)")
axs[0].axhline(floor,color="#6D7785",linestyle="--",linewidth=1,
              label="Required reliability: 24/29")
axs[0].scatter([r[0] for r in tests],[r[1] for r in tests],s=45,
               color=blue,edgecolors="white",linewidths=1,zorder=5,
               label="Scheduled accuracy assessments")
axs[0].set_ylim(.25,1.08)
axs[0].set_ylabel("Observation reliability c")
axs[0].legend(loc="upper left",ncol=2,fontsize=9,frameon=False)
axs[0].text(5.16,.69,"Accuracy passes at the dots;\nreadiness is lost between them.",
             fontsize=10,color=blue,bbox={"facecolor":"#FAFBFD","edgecolor":"none","alpha":.9})

axs[1].plot(all_t,all_b,color=blue,lw=2.3)
axs[1].plot([0,5],[1,0],color=orange,lw=3.3)
axs[1].scatter([5],[0],s=55,color=orange,edgecolors="white",zorder=5)
axs[1].axhline(0,color="#6D7785",linestyle="--",linewidth=1)
axs[1].set_ylabel("Execution reserve b")
axs[1].set_xlabel("Time (model units)")
axs[1].set_ylim(-.6,10)
axs[1].text(5.16,1.0,"No allocation can extend the continuous\nguarantee beyond t = 5 from this initial state.",
             fontsize=10,color=orange)

fig.suptitle("Passing scheduled tests does not establish continuous readiness",
             x=.075,y=.965,ha="left",fontsize=17,fontweight="bold")
fig.text(.075,.914,"Same resources and repair laws; different timing requirements. Constructed example, not observed data.",
         fontsize=10.5,color="#526276")
fig.text(.075,.025,"α = 6, δ = 1, s = 4, q = 1 · error limit = 5/58 · initial c = 24/29, b = 1.\n"
         "Timed policy: alternate u = 1 and u = 0 each time unit. Continuous optimum: u = 4/5 until reserve exhaustion.",
         fontsize=9,color="#526276",linespacing=1.5)
fig.subplots_adjust(left=.095,right=.975,top=.855,bottom=.155,hspace=.13)
for ext in ("png","svg"):
    fig.savefig(HERE/f"continuous-readiness.{ext}",dpi=180,facecolor=fig.get_facecolor())
report = {"status":"passed","scope":"Analytic model trajectories sampled for a figure; not empirical data.",
    "time_range":[0,8],"scheduled_assessments":[{"time":t,"reliability":c,"reserve":b} for t,c,b in tests],
    "required_reliability":floor,"periodic_assessment_reliability":periodic_high,
    "minimum_timed_policy_reliability":min(all_c),"minimum_timed_policy_reserve":min(all_b),
    "continuous_readiness_deadline":5,"continuation_beyond_deadline_proved_impossible":True,
    "files":["continuous-readiness.png","continuous-readiness.svg"]}
(HERE/"FIGURE-CHECKS.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({"status":"passed","periodic_assessment_reliability":periodic_high,
                  "figure":str(HERE/"continuous-readiness.png")}))
