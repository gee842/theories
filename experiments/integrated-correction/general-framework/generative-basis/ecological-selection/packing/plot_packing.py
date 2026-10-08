#!/usr/bin/env python3
"""Render this study's numerical results; does not redraw the published figure."""
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

HERE=Path(__file__).resolve().parent
result=json.loads((HERE/"packing-results.json").read_text())
vol=np.array([float(r["bounded_voronoi_volume_um3"])/17.44 for r in csv.DictReader((HERE/"voronoi-reading.csv").open())])
counts=np.array([float(r["estimated_cells_vc17_44"]) for r in csv.DictReader((HERE/"diameter-reading.csv").open())])
stats=result["packing"]["3.0"]
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"savefig.dpi":170})
fig, axes=plt.subplots(1,2,figsize=(11.8,4.5),layout="constrained")
ax=axes[0]
ax.hist(vol,bins=np.arange(0,27,.7),density=True,color="#95b7c7",alpha=.8,label="2,106 neighborhoods / 20 clusters")
x=np.linspace(1,27,500)
ax.plot(x,gamma.pdf(x,stats["k"],loc=1,scale=stats["scale_um3"]/17.44),color="#173c54",lw=2,label="Moment-based shifted gamma")
ax.axvline(2.02,color="#b04c25",ls="--",lw=1.5,label="Paper's confinement threshold")
ax.set(xlabel="Neighborhood volume / mean cell volume",ylabel="Probability density",xlim=(0,27),title="A. Reconstructed packing geometry")
ax.legend(fontsize=8,frameon=False)
ax.text(.98,.47,"k = 2.902; CDF error = 0.0216\nThreshold fraction: data 1.33%, model 2.63%",ha="right",va="top",transform=ax.transAxes,fontsize=9)
ax=axes[1]
ax.hist(counts,bins=np.arange(0,2201,25),color="#426d87",label="10,020 census observations")
ax.set_yscale("log")
ax.axvline(350,color="#b04c25",ls="--",lw=1.5,label="Approximate published plot limit")
ax.set(xlabel="Estimated cells: π × diameter³ / (6 × 17.44)",ylabel="Observations per 25-cell bin",xlim=(0,2150),title="B. Stated conversion of source diameters")
ax.text(.97,.82,"1,657 observations exceed 350\nMean = 195.3; maximum = 2,037.6",ha="right",va="top",transform=ax.transAxes,fontsize=9)
ax.legend(fontsize=8,frameon=False,loc="upper right")
fig.suptitle("Packing reconstruction and unresolved census conversion",fontsize=14)
fig.savefig(HERE/"packing-correspondence.png")
plt.close(fig)
