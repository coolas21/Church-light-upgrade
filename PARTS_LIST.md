# Parts List – 25-Fixture Rebuild

Quantities are for **25 fixtures plus 2 spares (27)**. Prices are rough (late 2026)
and are for budgeting only.

> **Buy a test batch first** (2 COBs, 2 fans, 2 controllers, 1 frost sheet). Rebuild one
> or two fixtures, run them at 100 % for an hour, and check fit, current and
> temperature before ordering the rest.

## Measurements
- [x] Fan: **NMB 3110KL-04W-B75, 80 × 80 × 25 mm, 12 V** ball bearing.
      Sibling models in this series run ~3,250–4,000 rpm and ~39–46 CFM,
      which is why it's loud.
- [x] COB: **40 × 40 mm base, 34 × 34 mm screw holes, 21 × 21 mm light area**
- [x] COB current per channel: 1.4 A each (blue, green)
- [ ] **Wall amps for one fixture** at 100 % both colors (watt meter), then have an electrician confirm the circuits behind the wall switch can carry 25 × that (see README "Power")
- [x] COB: **Vf 30 V; blue 1.4 A + green 1.4 A (~42 W per color, ~84 W total)**; yellow + black joined = **common + (confirmed common anode)**; both halves have burned spots, so replace all
- [x] Mounting height ~18 ft; yokes pivot and tilt
- [ ] Beam angle (optional, only to fine-tune aiming)
- [x] Lens 140 mm; front brackets 8.5 in apart, 3.5 in long, 2 holes 62 mm apart each (for the frost frame)

## Per-fixture rebuild parts

| # | Item | Spec / example | Qty | ~Each | ~Total |
|---|---|---|---|---|---|
| 1 | COB LED, **drop-in** | Bi-color (≈3000/3200 K + 5600/6000 K), 2 channels, **40 × 40 mm base, 34 × 34 mm M3 holes, ~20 × 20 mm LES**, CRI ≥ 90, **Vf 28–32 V per channel at ~1.4 A**, rated **≥ 1.8 A (≈ 55–60 W) per channel** so it runs at ~75–80 % of rating. Wiring: **common-anode 3-pad**, or 4 independent pads (join the two + pads). **Not common-cathode**. **Preferred: a 200 W / 3 A-per-color COB meeting the same size, wiring and Vf spec**: same power on this driver, cooler, longer life, ~10–15 % more light. Avoid 60 V-class 200 W COBs | 27 | $10–35 | ~$270–950 |
| 1b | COB LED, *alternative* | YUJILEDS 400H (CRI 95+, 3200/5600 K) is 46 × 40 mm with a larger light area. Needs new holes drilled and tapped in the heatsink, and must clear the reflector opening. Only if no good 40 × 40 part turns up | 14 packs | check site | — |
| 2 | Fan (quiet) | **Noctua NF-A8 PWM** (80 × 25 mm, 2200 rpm, 17.7 dB(A)) | 27 | $20–23 | ~$600 |
| 2b | Fan (if NF-A8 runs too hot) | Noctua NF-A8 industrialPPC-3000 PWM: about the stock airflow, quieter in tone, louder than 2 | 27 | ~$25 | ~$675 |
| 2c | Fan (budget) | Arctic P8 PWM PST (80 mm) | 27 | $8–10 | ~$250 |
| 3 | Fan temp controller | **Chosen:** 12 V 4-wire PWM controller, 25 kHz, ≤ 1.2 A fan, 50 k B3950 probe included, Po/Tu/Td settings (see README "Temperature controller") | 27 | $4–8 | ~$160 |
| 4 | Thermal paste | Arctic MX-6 or Noctua NT-H2 (~0.5 g per COB) | 20 g total | — | ~$20 |
| 4b | Thermal pad (upgrade alt.) | Honeywell PTM7950 sheet, cut to ~40 × 40 mm | enough for 27 | — | ~$40–60 |

Rough rebuild total: **about $700–1,500 including COBs** (fan choice and COB price drive it), plus frost and frames.

## Front diffusion (light frost, ~10–15 % loss): all fixtures

| Item | Spec / example | Qty |
|---|---|---|
| Light frost filter | **Lee 410 Opal Frost** (lightest; aim for ~10–15 % loss) or Rosco 114 Hamburg Frost (a bit softer, a bit more loss). Use the polyester/heat-rated version, not craft-store film | **6.5 × 6.5 in per fixture**: **3 sheets (21 × 24 in)** at 9 per sheet = 27 pieces, or 1 roll (48 in × 25 ft) for years of replacements |
| Frost frame plates | 0.040 in aluminum (or 1/16 in black ABS), ~9.5 × 7 in, 145 mm center hole, 2 holes per side 62 mm apart (see README "Frost frame") | 50 (2 per fixture) + 2 spare |
| Frame screws / nuts | to suit the front-bracket threads | ~110 |
| Flat-black paint | if using aluminum plates | 1–2 cans |
| Circle cutter or template + sharp knife | clean, identical cuts | 1 |

Notes:
- Keep the frost **on the front glass, not near the COB**. LED fixtures run
  cool enough at the front for standard theatrical filter.
- Buy one sheet first. Check the loss with the lux app on one fixture before
  cutting all 25.
- Frost softens and widens every beam by roughly 10–15°. Re-check the aiming
  after it's fitted, since you may need slightly less tilt.

## Install supplies

| Item | Use | Qty |
|---|---|---|
| 99 % isopropyl alcohol + lint-free wipes | Clean old paste off the COB seat | 1 bottle + 1 pack |
| Aluminum foil tape or Kapton tape (or thermal epoxy) | Fix the probe to the COB plate next to the COB | 1 roll |
| 22 AWG red/black wire | Run 12 V to the controller | 1 spool each |
| Wago 221 lever connectors or solder + heat shrink | Splice the controller into 12 V | ~70 |
| Fork/ferrule crimp terminals | Controller power at the PSU V1 / G screw terminals | ~70 |
| Small zip ties + adhesive mounts | Secure controller board and wiring away from the fan | 1 bag each |
| Canned air / soft brush | Clean heatsink fins and vents | 2–3 cans |
| Labels | Mark each fixture's DMX address and rebuild date | 1 sheet |

## DMX

| Item | Spec | Qty |
|---|---|---|
| DMX cable | **already owned**. Check it's 110–120 Ω DMX cable, not mic cable | — |
| **120 Ω DMX terminator, 3-pin XLR** | in the last fixture's DMX OUT on each run | **2** (current two runs) **+ 1 spare** |
| 3-pin XLR male + female connectors | Neutrik NC3MXX / NC3FXX, for repairs and re-terminating damaged ends | ~5 of each |
| *Optional:* opto-isolated DMX splitter, 2–3 outputs | only if keeping split runs from one console output, or for fault isolation | 0–1 |
| Cable ties / J-hooks | support runs along the ceiling structure | as needed |

## Tools (one set)

| Tool | Why |
|---|---|
| Bench power supply, 0–60 V / 3 A+, current limit | Test COB halves and new COBs before install |
| Multimeter | Check voltages and current per channel |
| Thermocouple meter or IR thermometer | Heatsink-temperature test (target < 60 °C) |
| Soldering iron, flux, solder wick | COB leads, connector repairs, caps if needed |
| Phone lux-meter app | Before/after light map of the seating |
| DC clamp meter (optional, e.g. UNI-T UT210E) | Easiest way to read LED current |
| **Plug-in watt meter (Kill-A-Watt type)** | Measure one fixture's real wall amps before the repaired fixtures go back on the circuit |

## Optional phase 2: adding fixtures (only if edges are still dark)

Not needed to start. See README "Do we need more fixtures?" and "Power".

| Item | Qty |
|---|---|
| Additional fixtures (same type, or a modern quiet bi-color par) | 2–4 |
| Hanging hardware to match existing mounts (clamp/yoke) | per fixture |
| Safety cables (rated, one per fixture) | per fixture (plus check the existing 25) |
| **New circuit** for the added fixtures (~1–1.4 A each) | **electrician** |

## Only if needed (inspect first)

| Item | When |
|---|---|
| **Recap kit per fixture**: 105 °C low-ESR long-life electrolytics (Panasonic FR/FM, Nichicon HE/PW, Rubycon ZLH/ZLJ). Same µF, same or higher V (63 V on the 36 V rail), same size. List the values from one fixture first | **All 25: the 6 PSU output caps + C4** (~7 caps, ~$3–6 per fixture): 110 × Rubycon 50ZLJ470M10X20 (470 µF 50 V), 55 × Panasonic EEU-FR1E102 (1000 µF 25 V), 30 × 33 µF 50 V 6.3 × 11 low-ESR (see `CAP_LIST.md`). Driver board caps only if bulging, leaking, testing bad, or causing flicker/resets (README "Capacitor plan"). Buy from Digi-Key or Mouser |
| ESR / component tester ("LCR-T4" type, ~$20) | Test pulled caps and spot-check the 400 V bulk caps |
| 0.15 Ω 2512 1 W resistor (R150) | Only if you choose to lower the LED current. Costs ~8–10 % of the light |
| 0.11 Ω 2512 1 W resistor (R110), 2 per fixture | Only for the optional ~+15 % boost with 200 W COBs (README "200 W COB option"). Test one fixture first |
