# Parts List – 30-Fixture Rebuild

Quantities are for **30 fixtures plus spares**. Prices are rough (late 2026)
and are for budgeting only.

> **Buy a test batch first** (1 COB pack, 2 fans, 2 controllers). Rebuild one
> or two fixtures, run them at 100 % for an hour, and check fit, current and
> temperature before ordering the rest.

## Still to measure before ordering
- [ ] Fan size: screw-hole spacing 71.5 mm = 80 mm fan, 82.5 mm = 92 mm fan
- [ ] Fan thickness (normally 25 mm)
- [ ] Old COB outline and screw-hole spacing (new COB is 46 × 40 mm)
- [ ] Mounting height and beam angle (for the coverage model)

## Per-fixture rebuild parts

| # | Item | Spec / example | Qty | ~Each | ~Total |
|---|---|---|---|---|---|
| 1 | COB LED | YUJILEDS 400H, 100 W bi-color 3200 K / 5600 K, CRI 95+, 46 × 40 mm, 28–33 V, sold in 2-packs | 16 packs (32 COBs) | check site | — |
| 2 | Fan (quiet) | Noctua NF-A8 PWM (80 mm) **or** NF-A9 PWM (92 mm) | 32 | $20–23 | ~$700 |
| 2b | Fan (budget alt.) | Arctic P8 PWM PST (80 mm) or Arctic 92 mm PWM | 32 | $8–10 | ~$300 |
| 3 | Fan temp controller | 12 V 4-wire PWM fan controller, 10 k NTC probe, adjustable start temp, non-zero minimum speed | 32 | $4–8 | ~$200 |
| 4 | Thermal paste | Arctic MX-6 or Noctua NT-H2 (~0.5 g per COB) | 20 g total | — | ~$20 |
| 4b | Thermal pad (upgrade alt.) | Honeywell PTM7950 sheet, cut to 46 × 40 mm | enough for 32 | — | ~$40–60 |

Rough rebuild total: **about $1,000–1,800 plus the COBs**, depending on the fan choice.

## Install supplies

| Item | Use | Qty |
|---|---|---|
| 99 % isopropyl alcohol + lint-free wipes | Clean old paste off the COB seat | 1 bottle + 1 pack |
| Kapton tape (or thermal epoxy) | Fix the NTC probe to the heatsink | 1 roll |
| 22 AWG red/black wire | Run 12 V to the controller | 1 spool each |
| Wago 221 lever connectors or solder + heat shrink | Splice the controller into 12 V | ~70 |
| Fork/ferrule crimp terminals | Controller power at the PSU V1 / G screw terminals | ~70 |
| Small zip ties + adhesive mounts | Secure controller board and wiring away from the fan | 1 bag each |
| Canned air / soft brush | Clean heatsink fins and vents | 2–3 cans |
| Labels | Mark each fixture's DMX address and rebuild date | 1 sheet |

## DMX

| Item | Spec | Qty |
|---|---|---|
| Opto-isolated DMX splitter, 3+ outputs | at the booth | 1 |
| DMX cable, 110–120 Ω (Belden 9841 or DMX-rated) | bulk + XLR connectors, or pre-made | ~800 ft |
| 3-pin XLR male + female connectors (if bulk cable) | Neutrik NC3MXX / NC3FXX | ~70 of each |
| 120 Ω DMX terminator, 3-pin XLR | end of each run | 3 (+1 spare) |
| Cable ties / J-hooks | support runs along the ceiling structure | as needed |

## Tools (one set)

| Tool | Why |
|---|---|
| Bench power supply, 0–60 V / 3 A+, current limit | Test COB halves and new COBs before install |
| Multimeter | Check voltages and current per channel |
| Thermocouple meter or IR thermometer | Heatsink-temperature test (target < 60 °C) |
| Soldering iron, flux, solder wick | COB leads, connector repairs, caps if needed |
| Phone lux-meter app | Before/after light map of the seating |

## Relocating the ~5 spare fixtures (see coverage map)

Your plan shows 25 hung fixtures, and you own about 30. Once repaired, the
spares go to the dark areas.

| Item | Qty |
|---|---|
| Hanging hardware to match existing mounts (clamp/yoke) | 5 |
| Safety cables (rated, one per fixture) | 5 (plus check the existing 25) |
| Power to each new position | **have an electrician run it** |

## Only if needed (inspect first)

| Item | When |
|---|---|
| 105 °C low-ESR electrolytic capacitors (match µF / V) | Any bulging or leaking caps on the PSU or driver board |
| 0.15 Ω 2512 1 W resistor (R150) | Only if you choose to lower the LED current. Costs ~8–10 % of the light |
| Light frost: Rosco 114 or Lee 410 + gel frames | Only on fixtures that still leave gaps after re-aiming and relocating |
