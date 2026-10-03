"""Every date and number the film puts on screen comes from here.

One assumption: data-centre power keeps its official 2024-2030 growth rate until physics stops it.
Source for the base: IEA, Energy and AI (2025): ~415 TWh in 2024, ~945 TWh in 2030 (base case). Verify before release.
"""
import math

HOURS = 8766
P2024, P2030 = 415e12 / HOURS, 945e12 / HOURS          # W
G = (945 / 415) ** (1 / 6) - 1                          # growth per year
EARTH_AREA = 5.1e14                                     # m^2
OCEAN_KG = 1.4e21
EJECT_J_PER_KG = 6.5e7                                  # escape-speed kinetic energy carried off per kg vented


def year_at(power_w):
    return 2030 + math.log(power_w / P2030) / math.log(1 + G)


def power_at(year):
    return P2030 * (1 + G) ** (year - 2030)


WALLS = [
    ("1 TW of compute", 1e12),
    ("compute equals all human energy use today (~19 TW)", 1.9e13),
    ("waste heat 2 W/m^2, about half a CO2 doubling", 2 * EARTH_AREA),
    ("Kardashev I, 10 PW; waste heat ~20 W/m^2", 1e16),
    ("all the sunlight Earth absorbs (~1.2e17 W)", 1.2e17),
    ("the Sun's whole output (3.8e26 W)", 3.8e26),
]

if __name__ == "__main__":
    print(f"data centres: {P2024/1e9:.0f} GW (2024), {P2030/1e9:.0f} GW (2030); growth {G*100:.1f}%/yr; doubling {math.log(2)/math.log(1+G):.1f} yr")
    print(f"2026: {power_at(2026)/1e9:.0f} GW")
    for label, p in WALLS:
        print(f"{year_at(p):6.0f}  {label}")
    # Oceans as the heat sink: on an exponential, energy used so far ~ P / ln(1+G) (per year).
    tau_s = 3.156e7 / math.log(1 + G)
    p_end = OCEAN_KG * EJECT_J_PER_KG / tau_s
    print(f"{year_at(p_end):6.0f}  oceans spent as a heat sink (power {p_end:.1e} W)")
    for p in (1e16, 1e17):
        print(f"        at a constant {p:.0e} W the oceans would last {OCEAN_KG*EJECT_J_PER_KG/p/3.156e7:,.0f} years")
    print("beyond the Sun: light speed sets the pace; at 0.1c the galaxy (~100,000 ly) takes ~1,000,000 years")
