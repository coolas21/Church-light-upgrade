# Parts List – 30-Fixture Rebuild

Quantities are for **30 fixtures plus spares**. Prices are rough (late 2026)
and are for budgeting only.

> **Buy a test batch first** (1 COB pack, 2 fans, 2 controllers). Rebuild one
> or two fixtures, run them at 100 % for an hour, and check fit, current and
> temperature before ordering the rest.

## Still to measure before ordering
- [x] Fan: **NMB 3110KL-04W-B75, 80 × 80 × 25 mm, 12 V** ball bearing.
      Sibling models in this series run ~3,250–4,000 rpm and ~39–46 CFM,
      which is why it's loud.
- [x] COB: **40 × 40 mm base, 34 × 34 mm screw holes, 21 × 21 mm light area**
- [ ] COB voltage and current per channel at 100 % (see README, "Measurements")
- [ ] COB pad count / polarity: 4 pads (two separate channels) or 3 (shared +)
- [ ] Mounting height and beam angle (for the coverage model)
- [ ] Front lens / bezel diameter, and whether there is a gel-frame slot (for frost)

## Per-fixture rebuild parts

| # | Item | Spec / example | Qty | ~Each | ~Total |
|---|---|---|---|---|---|
| 1 | COB LED, **drop-in** | Bi-color (≈3000/3200 K + 5600/6000 K), 2 channels, **40 × 40 mm base, 34 × 34 mm M3 holes, ~20 × 20 mm LES**, CRI ≥ 90, per-channel Vf ≤ ~32 V at the measured current, same pad layout as the original | 32 | $10–25 | — |
| 1b | COB LED, *alternative* | YUJILEDS 400H (CRI 95+, 3200/5600 K) is 46 × 40 mm with a larger light area. Needs new holes drilled and tapped in the heatsink, and must clear the reflector opening. Only if no good 40 × 40 part turns up | 16 packs | check site | — |
| 2 | Fan (quiet) | **Noctua NF-A8 PWM** (80 × 25 mm, 2200 rpm, 17.7 dB(A)) | 32 | $20–23 | ~$700 |
| 2b | Fan (if NF-A8 runs too hot) | Noctua NF-A8 industrialPPC-3000 PWM: about the stock airflow, quieter in tone, louder than 2 | 32 | ~$25 | ~$800 |
| 2c | Fan (budget) | Arctic P8 PWM PST (80 mm) | 32 | $8–10 | ~$300 |
| 3 | Fan temp controller | 12 V 4-wire PWM fan controller, 10 k NTC probe, adjustable start temp, non-zero minimum speed | 32 | $4–8 | ~$200 |
| 4 | Thermal paste | Arctic MX-6 or Noctua NT-H2 (~0.5 g per COB) | 20 g total | — | ~$20 |
| 4b | Thermal pad (upgrade alt.) | Honeywell PTM7950 sheet, cut to ~40 × 40 mm | enough for 32 | — | ~$40–60 |

Rough rebuild total: **about $1,000–1,800 plus the COBs**, depending on the fan choice.

## Front diffusion (light frost, ~10–15 % loss): all fixtures

| Item | Spec / example | Qty |
|---|---|---|
| Light frost filter | **Lee 410 Opal Frost** (lightest; aim for ~10–15 % loss) or Rosco 114 Hamburg Frost (a bit softer, a bit more loss). Use the polyester/heat-rated version, not craft-store film | **1 roll (48 in × 25 ft)**: ~160 circles up to 9 in, or ~8 sheets (21 × 24 in) at 4 per sheet |
| Gel frame to fit the fixture's front slot, if it has one | measure slot width × height | 32 |
| Otherwise: cut to fit **inside the front bezel** against the glass, held by the retaining ring | no tape on the lens | — |
| Circle cutter or template + sharp knife | clean, identical cuts | 1 |

Notes:
- Keep the frost **on the front glass, not near the COB**. LED fixtures run
  cool enough at the front for standard theatrical filter.
- Buy one sheet first. Check the loss with the lux app on one fixture before
  cutting all 30.
- Frost softens and widens every beam by roughly 10–15°. Re-check the aiming
  after it's fitted, since you may need slightly less tilt.

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
