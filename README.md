# Church 100 W Bi-Color COB Light – Quiet & Reliability Upgrade

Plan for 25 no-name 100 W warm-white / daylight COB fixtures (6-ch DMX) that
have loud fans and dead warm or cool channels. This file grew as answers came
in; **the summary below is the current plan**. Later sections hold the
details and the reasoning. Shopping list: `PARTS_LIST.md`.

## Plan at a glance

| Area | Decision |
|---|---|
| COB | Replace all 25 (both halves have burned dies). Drop-in **40 × 40 mm, 34 × 34 mm M3 holes, ~20 mm LES**, bi-color, **common anode**, CRI ≥ 90, **Vf 28–32 V at 1.4 A**, rated **≥ 1.8 A per color**. A 200 W / 3 A-per-color COB is a good choice if it fits (see "200 W COB option"). The light output stays the same, but it runs cooler and lasts longer. Test 2 before ordering. |
| Measured | 30 V, blue 1.4 A + green 1.4 A, so ~84 W of LED power per fixture |
| Paste | Arctic MX-6 / Noctua NT-H2 (or PTM7950 pad), **full-coverage thin layer**, check the print on the first one |
| Fan | **Noctua NF-A8 PWM** (80 × 25 mm) + 12 V PWM temp controller. Step up to NF-A8 iPPC-3000 if the heatsink goes over 60 °C after 1 h at 100 %. |
| Frost | **Lee 410 Opal Frost** (~10–15 % loss) in a 2-plate frame on the front brackets (145 mm hole, holes 62 mm apart) |
| Aiming | 18 ft mounting: tilt house fixtures **~20–25° outward, never toward the stage**; center line and stage stay straight down |
| More fixtures | Not to start. Re-check with a lux app after phase 1. If needed, add 2–4 on a **new circuit**. |
| Power | ~100–105 W and ~0.9–1.4 A per fixture at 120 V, so **25 ≈ 22–34 A**, more than one 20 A circuit. **Measure one fixture with a watt meter**, and have an electrician confirm the circuits behind the switch before all 25 run at full again. |
| DMX | **One daisy chain** (25 < 32 devices, ~475 ft) with a **120 Ω terminator** at the end. If keeping your two runs, terminate both, and never Y-split. |

## What's in the fixture (from photos)

| Part | Marking | What it does |
|---|---|---|
| Power supply | RS-200W-36V-12V | **V1 = 12 V / 1 A** (logic + fan), **V2 = 36 V / 5.2 A** (LED power) |
| Main board | XF-THL-1-6080-20110820 | Generic RGBW driver board; only **B** and **G** channels populated (used for the two COB colors) |
| MCU | STC 608AD-5V (8051) | Reads DMX, runs the menu, makes PWM |
| DMX receiver | SN75176B | RS-485 / DMX input |
| 5 V regulator | LM2576S-5.0 + SS36 | Makes 5 V logic from 12 V |
| LED drivers | D-PAK MOSFET + 220 µH inductor + **R130 (0.13 Ω)** sense resistor + LM358 | Constant-current buck driver, one per color |
| Display board | XF-XHL-1-7645 (16-pin) | Address / mode menu |
| LED | 100 W two-color COB (cool + warm halves) | Several dark/burnt spots visible on the die |
| Fan | 2-wire, wired straight to 12 V | Runs full speed all the time → noise |

Heat budget: a 100 W COB turns roughly 60–70 W into heat at full output. That
heat has to leave through the heatsink. **Fully passive (no fan) is not
realistic in this housing** — it would need a heatsink several times larger.
The practical goal is a fan you can't hear at normal levels, and a thermal
path good enough that the COB stays cool.

## Why channels are dying

The burnt spots on the COB are the classic result of years of running hot
(dried-out thermal paste, dusty fins, a tired fan). Possible failure points,
most likely first:

1. **COB half is dead** (most likely, given the visible burnt dies)
2. Driver channel on the main board (MOSFET, sense resistor, or diode)
3. Wiring / connector between board and COB

### 5-minute diagnosis per fixture

1. **Swap test:** at the board's output connector, swap the warm pair with the
   cool pair. If the dead color *moves*, the board is bad. If the *same* half
   stays dark, the COB is bad.
2. **Direct test:** feed each COB half from a current-limited bench supply
   (start ~30 V, limit 300 mA, raise slowly). Note the forward voltage at
   ~1 A — you need it to order the right replacement COB.

## The fix (per fixture)

### 1. Rebuild the thermal path (biggest reliability gain, nearly free)
- Remove COB, clean off the old paste, apply fresh compound
  (Arctic MX-6 / Noctua NT-H2), thin full-coverage layer, torque screws evenly.
- Blow dust out of the heatsink fins and housing vents.
- Replace the COB (all of them: both halves have burned dies).

### 2. Quiet fan + temperature control
- Replace the stock fan with a quality fluid-dynamic-bearing **4-pin PWM** fan
  of the same size: **80 × 80 × 25 mm** (stock is an NMB 3110KL-04W-B75).
- Add a small **12 V PWM fan temperature controller** with an NTC probe;
  stick the probe to the heatsink right under the COB with thermal epoxy or
  Kapton tape. The fan idles almost silent when the light is dimmed and only
  ramps up when it really needs to.
- Power stays on the PSU 12 V output (V1 = 1 A is plenty for logic + one fan).
- Set the controller so the fan is at ~30–40 % below ~40 °C heatsink and 100 %
  by ~55 °C. Never let it stop completely while the LED is on.

### 3. (Optional) Take 10–15 % off the maximum current
LEDs last far longer and run much cooler slightly below rating, and the eye
barely notices a 10–15 % drop. On this board the LED current is set by the
**R130 (0.13 Ω)** sense resistor: replacing it with **R150 (0.15 Ω)** cuts
current ~13 %. Do this on one test unit first and measure the current before
and after — only commit after confirming it behaves.

### 4. Health checks while it's open
- Look for bulging/leaking electrolytic capacitors on both boards (board is
  dated 2011, PSU 2016). Replace any suspect ones with 105 °C low-ESR parts.
- Reflow any cracked solder joints on the XLR and connector boards.

### 5. Validate (do on the first 1–2 units before doing all 25)
- Both channels at 100 % for 60 minutes in its normal hanging orientation.
- Measure the heatsink next to the COB: **target < 60 °C**; COB case
  **< 80 °C**. If over, raise the controller's fan curve or do step 3.
- Listen at the audience distance at normal service levels.

## Parts list

See **`PARTS_LIST.md`** for the current list, quantities and costs.

## Update: fixtures run at 100 % all the time (house / audience light)

This changes some choices above:

- **Fan:** a temp-controlled fan will sit near full speed at 100 % output, so
  the noise win comes from the *fan itself*: a quality fluid-dynamic-bearing
  fan (Noctua-class) is far quieter than a worn sleeve-bearing fan at the same
  airflow. Use the largest diameter the mount allows (a bigger, slower fan is
  quieter for the same airflow) and fit rubber anti-vibration mounts. Keep the
  temp controller anyway, because it adapts to room temperature and ramps up
  if a unit runs hot. Pick a static-pressure-rated model, since it blows into
  heatsink fins.
- **Current reduction (step 3):** this is still the best thing for long life
  at constant 100 %, but it costs some light. With LED efficiency, ~13 % less
  current gives roughly ~8–10 % less light. Skip it if light is the priority,
  or combine it with a more efficient COB (below).
- **More light without more heat:**
  1. Fix every dead half first. A one-color fixture is giving ~50 % output.
  2. Use **modern high-efficiency replacement COBs** (look for ≥130 lm/W,
     CRI ≥ 90) at the same wattage. That gives more light from the same
     heat, though no-name ratings are optimistic.
  3. Clean the reflectors and front glass.
  4. Do **not** fit a higher-wattage COB. The driver, heatsink and housing
     are sized for 100 W.
- **Dead spots are usually a coverage problem, not a brightness problem.**
  Re-aim first, then add a *light* frost on fixtures aimed near dead spots:
  - Light frost (Rosco 114 Hamburg Frost / Lee 410 Opal Frost class): about
    10–20 % loss, softens hot spots and widens the beam.
  - Heavy diffusion (Lee 216 full white class): loses 50 %+, so avoid it.
  - Mount gel/diffusion in a gel frame at the front, not against the COB.
  - Adding a fixture or two over the dead areas usually helps more than any
    diffuser (see "Do we need more fixtures?").

## Room layout notes (from sanctuary photos)

- The house fixtures hang from a high, dark, open-truss ceiling in a roughly
  rectangular grid. The seating fans out in wedges around a curved stage, so
  the **outer wedges, side walls and rear corners** fall outside the grid.
  Those areas are the likely dead spots.
- From the booth the fixtures don't all match: some look bright and cool,
  others dimmer or warmer. That fits fixtures with one dead half. Once
  repaired, run **every fixture at the same warm/cool mix** so the room looks
  even (and on camera, if streamed).
- The dark ceiling reflects almost nothing, so all useful light must come
  straight down out of the fixtures.

### Fixing the dead spots
1. **Map it.** During a service-level look, take readings at seat height on a
   grid (every ~3rd row, aisle and wall seats included). A phone lux-meter app
   is fine for *relative* comparison. Mark anything well below the center.
2. **Repair every fixture first,** then re-measure. Many dark areas may simply
   be under a one-color fixture.
3. **Re-aim the outer row** of fixtures outward toward the side wedges and
   rear corners, rather than straight down.
4. **Check the beam overlap.** Beam diameter at the seats is about
   `2 × height × tan(beam angle ÷ 2)`. If that is smaller than the fixture
   spacing, there will be dark gaps between the pools of light. A light frost
   fixes that by widening every beam a little.
5. **Add fixtures where the grid doesn't reach** (optional, see "Do we need
   more fixtures?"). Fixtures hung over the outer wedges beat any diffuser.

## Recommended parts (rebuild of all fixtures)

### COB
Drop-in spec (from the measurements below): **40 × 40 mm base, 34 × 34 mm M3
holes, ~20 × 20 mm LES**, bi-color (≈3000–3200 K + 5600–6000 K), CRI ≥ 90,
**common anode** (or 4 pads with the two + joined), **Vf 28–32 V per color at
1.4 A**, rated **≥ 1.8 A per color**. Get the seller to confirm the hole
spacing, wiring and Vf in writing, and test 2 before ordering the rest.

The YUJILEDS 400H (46 × 40 mm, CRI 95+) is **not** a drop-in. It's only a
fallback if new holes are drilled and tapped and it clears the reflector.

### Fan: 4-pin PWM, same size as the original
| Size | Quiet pick | Budget pick |
|---|---|---|
| 80 mm (confirmed) | Noctua NF-A8 PWM (2200 rpm, 17.7 dB(A) max, 2.37 mm H2O) | Arctic P8 PWM PST |
| If too hot | Noctua NF-A8 industrialPPC-3000 PWM (about the stock airflow) | — |

Use the anti-vibration mounts that come with the fan. Because these run at
100 %, test the first unit: if the heatsink goes past ~60 °C with a Noctua at
full speed, step up to a higher-airflow model.

### Temperature controller
- A 12 V "4-wire PWM fan temperature controller" module with a 10 k NTC probe
  and an adjustable start temperature. It must drive the fan's **PWM pin**
  (25 kHz), not chop the 12 V supply.
- Power it from the PSU's V1 (12 V). Fix the probe to the heatsink next to the
  COB with Kapton tape or thermal epoxy.
- Set ~35 °C = slow, ~55 °C = full. Choose a module whose minimum speed is
  not zero.

### Thermal interface
- **Arctic MX-6** or **Noctua NT-H2** paste: non-curing, non-conductive, and
  resists pump-out. Each COB needs ~0.3–0.5 g, so ~15 g covers 25 fixtures.
  Buy 2 × 8 g or one 20 g tube.
- Upgrade option: **Honeywell PTM7950** phase-change pad cut to the COB size.
  It never dries out or pumps out, which suits fixtures running hot for hours.
  It needs one full-power warm-up to flow.
- Avoid thick silicone pads, liquid metal and electrically conductive pastes.
- Method: clean both surfaces with 99 % isopropyl, apply a thin even layer,
  tighten the screws a little at a time, alternating sides, and don't
  over-tighten.

## Fixture plan and coverage model

The hand-drawn plan (`docs/fixture_plan_sketch.jpg`) shows **25 hung
fixtures**: 6 over the stage and 19 over the seating. The room is about 85 ft
wide. Seating runs about 28 ft behind the X axis.

`tools/coverage.py` models relative light at seat level from that plan.
Fixtures hang **~18 ft above the floor, so ~15.5 ft above seat level**.
Beam angle isn't measured, so it was run at 45° (bare) and 60° (with frost):

- All house fixtures sit within Y = ±25 ft and X = −7…+16 ft. That leaves
  **a ~17 ft band along each side wall and a ~21 ft band at the rear with no
  fixture above it**. At only 15.5 ft, beams don't spread far enough to
  reach those bands.
- The front-center seats get well above the average (the stage-front row at
  X = 24 also spills there). Side walls and rear corners get 10–30 %.
- *If* 5 fixtures were added at **(X, Y) = (8, ±36), (−16, ±30), (−24, 0)**,
  the seating below half the average would drop from **43 % to 21 %** (60°),
  or from 47 % to 27 % (45°), all pointing straight down.

See `docs/coverage_H15.5_B60.png` and `docs/coverage_H15.5_B45.png`. Re-run:
`python3 tools/coverage.py <height_above_seats_ft> <beam_deg>`.

Full shopping list: `PARTS_LIST.md`.

## Aiming (tools/aiming.py)

The model's best result for the **25 hung fixtures** comes from one rule:

- **Tilt every house fixture ~20–25° away from the room's center line,**
  sideways or toward the rear, **never toward the stage** (that glares the
  platform). Leave the two center-line fixtures at (8, 0) and (16, 0) and the
  stage fixtures pointing straight down.
- With frost (60°): seating below half of today's average drops from
  **43 % to 28 %**. Without frost (45°): 47 % → 29 %. Going past 25° gains
  little and raises glare.
- What's left dark is the outer ~8–10 ft along each side wall and the rear
  ~10 ft. Only added fixtures fix that (see below).
- Map with arrows: `docs/aiming_H15.5_B60_25.png`. With 5 added fixtures:
  `docs/aiming_H15.5_B60.png` (10 % below half).

| Fixture (X, Y) | Aim beam center at (X, Y) |
|---|---|
| (13, ±17) | (13, ±24) |
| (11, ±9.5) | (11, ±16) |
| (6, ±25) | (6, ±32) |
| (3, ±17) | (3, ±24) |
| (0, ±9.5) | (−1, ±16) |
| (0, 0) | (−7, 0), toward the rear |
| (−3, ±24) | (−4, ±31) |
| (−7, ±15) | (−11, ±21) |
| (−7, ±5) | (−13, ±8) |

How to aim in the field:
1. Rule of thumb at this height: **the beam center lands ~7 ft outward** from
   directly under the fixture (15.5 ft × tan 24°). Mark the aim seat with
   tape and point the beam center at it.
2. Aim with only that fixture on, both colors full, with the house dark. Use a
   phone-camera snapshot to find the hot spot.
3. Lock the pivot and tilt bolts firmly, and fit a safety cable on every
   fixture.
4. Check glare from the back rows and the platform. At 18 ft the fixtures
   are close to people, so if a lens is in a normal line of sight (looking at
   the stage or screens), back that fixture off 5°.
5. Fit the frost frames **after** aiming, then do a quick lux-app walk of the
   seating to confirm.

## Do we need more fixtures?

**Not to start.** Do the 25 first: repair (new COBs restore both colors),
aim, frost, then walk the room with the lux app.

| Setup (60° with frost) | Seating below half of avg |
|---|---|
| 25, straight down | 43 % |
| **25, aimed** | **28 %** |
| 30 (5 added), straight down | 21 % |
| 30 (5 added), aimed | 10 % |

- "Average" here assumes every fixture has both colors working. Today many
  have a dead half, so the **real improvement from the repairs is bigger**
  than this table shows.
- Moving center fixtures out to the edges doesn't help with only 25: it just
  makes a dark hole in the middle of the seating.
- If the edges are still too dark after phase 1, add **2–4 fixtures** at
  the rear corners (−16, ±30) first, then the side walls (8, ±36). Put them on
  a separate circuit (see Power).

## Power (one wall switch)

Per fixture, measured: LED 30 V × 2.8 A ≈ **84 W**. Add the fan and logic
(~4 W) and power-supply losses (~85 % efficient), and it's about **100–105 W
from the wall**. At 120 V that's **~0.9 A each**. If the supply has poor power
factor (common on cheap units), it could be up to ~1.4 A each.

| | Watts | Amps @ 120 V (good PF → poor PF) | 20 A circuits needed* |
|---|---|---|---|
| 25 fixtures | ~2,600 W | **~22 A → 34 A** | 2 (3 if poor PF) |
| 30 fixtures | ~3,100 W | **~26 A → 41 A** | 2–3 |
| Each extra fixture | ~105 W | ~0.9–1.4 A | — |

\* A 20 A breaker should carry **≤ 16 A continuous** (80 % rule for loads
running 3+ hours). That's ~15 fixtures per 20 A circuit, or ~10 with poor PF.

What this means:
- **25 fixtures can't be on a single 20 A circuit.** They are already on 2+
  circuits, or a 208/240 V circuit (halve the amps), or the wall switch drives
  a relay or contactor. Have an electrician confirm what the switch actually
  controls.
- **Watch out after the repair:** today many fixtures run only one color, so
  they draw roughly half power. Once every fixture has both colors back at
  100 %, the load goes **up**, and a circuit that's fine today could trip.
- **Measure one fixture first:** plug it into a watt meter (Kill-A-Watt) at
  100 % both colors and read the amps directly. Multiply by 25.
- **Inrush:** switching 25 power supplies on at once with one wall switch
  causes a big current spike. It can trip breakers or wear out the switch.
  If that happens, an electrician can add a contactor, or split the load
  across two switches.
- Adding fixtures means **adding a circuit**, not just plugging into the
  existing run.

## DMX wiring (tools/dmx_route.py)

### One chain or split?

**One chain through all 25 is fine here** and uses the least cable:

- 25 fixtures is well under the **32-device limit** for one DMX line. That only
  holds if nothing else (stage pars, hazer, etc.) shares the line. Count
  everything on it.
- The XLR in/out board on the back of each fixture is **passive** (traces
  straight from IN to OUT). A fixture that's off or failed still passes
  data. Only a bad cable or connector breaks the chain after that point.
- Length: ~305 ft along the ceiling plus drops and slack is about **475 ft**,
  well under the ~1,000 ft limit.

**When splitting is worth it:** if a cable fault going dark mid-service
would be a real problem, or you add more fixtures to the line. A cheap
2- or 3-output opto-splitter at the booth then limits a fault to one run.

### Your current setup: two runs, no terminator

1. **Find out how the two runs split.** If they come from two console outputs
   or a splitter, that's fine: keep them and **add a terminator to the end of
   each**. If they split from one output with a **Y-cable or a splice**,
   that's not allowed in DMX (it causes reflections and flicker). Either
   join them into one chain or put an opto-splitter where the Y is.
2. **Add a 120 Ω terminator** in the DMX OUT of the **last fixture on every
   run**. Without one, a long run can work most of the time but will flicker
   or glitch at random, which is classic "ghost" behavior.

### Single-chain order (`docs/dmx_single_chain.png`)

From the booth: center-rear → right side → stage → down the middle → left
side → **finish at the left rear (−3, −24) with the terminator**. The order
(X, Y):

(−7,5) → (0,9.5) → (−7,15) → (−3,24) → (6,25) → (3,17) → (13,17) → (11,9.5)
→ (34,12) → (24,12) → (24,−12) → (34,−12) → (32,0) → (24,0) → (16,0) → (8,0)
→ (0,0) → (−7,−5) → (−7,−15) → (0,−9.5) → (11,−9.5) → (13,−17) → (3,−17)
→ (6,−25) → **(−3,−24) T**

If you keep two runs, split this order where it's convenient, for example
right half + stage on one and middle + left on the other, and terminate both
ends. (`docs/dmx_runs.png` shows a three-run split, drawn for 30 fixtures.)

At each fixture:
- Leave a **service loop** big enough for full pan and tilt. Tie it to the yoke
  or hanging clamp so the cable never takes strain at the XLR.
- Label every cable with its chain position (e.g. 12 → 13) at both ends.
- Before closing up the ceiling, check each run with a DMX tester or the
  console: bring up each fixture's address and watch the right light respond.

Rules:
- **Daisy-chain only** (OUT of one fixture to IN of the next). Never Y-split
  a cable.
- **Use 110–120 Ω DMX cable** (e.g. Belden 9841 or a DMX/AES-rated cable),
  not mic cable. Mic cable causes flicker and dropouts on long runs.
- **Terminate** the last fixture of each run with a 120 Ω XLR terminator.
- Max **32 devices** and ~1,000 ft per run. The board's SN75176B is a
  standard one-unit-load receiver.
- **Run DMX at least a foot away from power,** and cross power at right angles.
- Label both ends of every cable, and tag each fixture with its address.

Addressing: 25 × 6 ch = 150 channels, so one universe. Give fixtures **in the
same zone the same start address** so the console sees a few zones instead of
25 fixtures. For example: front house, rear house, left side, right side,
stage. Fixtures sharing an address simply mirror each other.

## 200 W COB option (3 A per color)

**The driver board, not the COB, sets the current.** The R130 sense
resistors hold each color at ~1.4 A no matter what COB is fitted.

### Option 1: 200 W COB on the stock driver (recommended if it fits)
- Still ~1.4 A per color, ~84 W. **Same power, same heat, same amps at the
  wall.** No electrical changes.
- The COB runs at ~47 % of its rating. Each LED die runs cooler and a bit
  more efficiently, so expect **~10–15 % more light** and a **much longer
  life**. It's the most reliable choice for 100 % every service.
- Must still meet the drop-in spec: **40 × 40 mm, 34 × 34 mm holes, common
  anode**, and **Vf ≤ ~32 V per color at 1.4 A**. Avoid 200 W COBs built as
  60 V+ strings. This board's 36 V supply can't drive them, and they'll be
  dim or won't light.
- A 200 W COB often has a **larger light area** (≈ 28–30 mm). It still
  works, but the beam is a little wider and softer (fine with frost). Check
  it sits correctly under the reflector opening.

### Option 2: run it at a full 3 A per color (~200 W): **no**
| | Stock | 3 A per color |
|---|---|---|
| LED current | 2.8 A | 6 A: **over the PSU's 5.2 A rating** |
| LED power / heat | ~84 W / ~55–60 W | ~190 W / ~130 W: more than double; heatsink and NF-A8 can't cope |
| Driver | designed for ~1.4 A | MOSFETs, inductors and sense resistors not rated for it |
| Wall power (25 fixtures) | ~2,600 W, 22–34 A | **~5,500 W, ~46–70 A**: 4–5 circuits |

It would mean a new power supply, a new driver, a bigger heatsink, a louder
fan and new circuits. At that point, new fixtures are the better buy.

### Option 3: modest boost (only if more light is still needed)
Change the two R130 (0.13 Ω) resistors to **R110 (0.11 Ω)**: ~1.65 A per
color, ~+18 % current, ~+15 % light, ~100 W LED / ~120 W at the wall per
fixture (25 ≈ 3,000 W). Within the PSU rating, but heat rises ~20 %, so
expect the NF-A8 iPPC-3000 fan. **Try on one fixture**: measure the current
and the heatsink temperature after an hour, and check the driver MOSFETs
aren't too hot to touch, before doing more. Only worth it with a 200 W-rated
COB.

## Measurements (before ordering COBs)

Measured: COB **40 × 40 mm, holes 34 × 34 mm, light area 21 × 21 mm**. Fan is
**NMB 3110KL-04W-B75 (80 × 80 × 25 mm, 12 V)**. The YUJILEDS 400H (46 × 40)
is **not** a drop-in. Look for a 40 × 40 bi-color COB, or drill and tap new holes.

Take these on 2–3 fixtures, one with both colors working if possible. Use a
multimeter on **DC volts**. The power supply's input side carries mains
voltage: probe only the low-voltage output terminals and the driver board.

| # | Where to probe | Fixture setting | Why | Expect |
|---|---|---|---|---|
| 1 | PSU **V2 to G** | Both channels 100 % | 36 V rail under load | ~36 V |
| 2 | PSU **V1 to G** | Any | 12 V rail for logic + fan | ~12 V |
| 3 | **Across each COB channel** (its + and − at the board's output connector or the COB pads) | That channel at 100 % | **Forward voltage (Vf)**, the number to match when buying | ~28–33 V |
| 4 | **Across each R130 resistor** (B and G channels) | That channel at 100 % | Current: **I = V ÷ 0.13** (e.g. 0.20 V → 1.5 A) | ~0.15–0.25 V |
| 5 | Same as 3 and 4 | Both channels 100 % together | Check that the current doesn't drop when both run | same as alone |
| 6 | Count the COB pads and read the +/− marks | Power off | 3 connections (one shared) = common terminal; 4 independent = separate | — |

From these, buy a COB whose **Vf per channel at that current is ≤ ~32 V**
(the 36 V supply needs headroom) and whose **rated current is ≥ the measured
current**. Watts per channel ≈ step 3 × step 4 current.

Tips: let it run 5 minutes before reading, because Vf drops a little as the
COB warms. If a reading jumps around, the channel isn't at full 100 %; set it
to full so the dimming PWM is off.

### Results so far
- **COB Vf = 30 V** (first fixture). That fits the ≤ 32 V target.
- **Current: blue 1.4 A and green 1.4 A** (both at 100 %), 2.75–2.8 A total.
  That's **~42 W per color, ~84 W of LED power**, and roughly 55–60 W of heat.
- **Yellow + black are soldered together on one tab: the common positive
  (confirmed).** The COB is **common anode**: common +, blue, green.
- **Both color halves have black spots** (burned dies), so every COB gets
  replaced, not just the ones with a dead color.
- **Old paste covered only part of the COB base** and had dried and crumbled.
  The edges of the base were barely touching the plate. This is the main
  reason the COBs overheated and burned out dies.

### Three ways to get the current (pick one)
1. **Across R130 (no tools to buy):** on the driver board, find the large
   black resistors printed **R130** next to the **B** and **G** labels. With
   that color at 100 %, touch the meter probes (DC volts) to the two metal
   ends of the resistor. Amps = reading ÷ 0.13. For example, 0.195 V → 1.5 A.
2. **DC clamp meter (easiest, ~$40–60):** it must say **DC A** (Hall effect,
   e.g. UNI-T UT210E or Klein CL390). AC-only clamps won't read. Zero it, then
   clamp around **one** wire of the channel at 100 %.
3. **Plug-in watt meter at the wall (rough):** both colors at 100 %:
   LED watts ≈ wall watts × 0.85, and amps per channel ≈ LED watts ÷ 2 ÷ Vf.
   For example, 110 W at the wall → ~93 W → ~1.55 A per channel at 30 V.

Avoid putting the multimeter in series on its amps jack. One slip with the
probes in amps mode shorts the 36 V supply, and the LED driver can spike when
the circuit closes.

### Re-pasting: get full coverage
1. Scrape off the old paste with a plastic card, then clean both faces with
   99 % isopropyl until shiny.
2. Check the plate is flat with a straightedge across the COB area. Sand any
   burrs around the screw holes flat.
3. Spread a **thin, even layer over the whole base** (a credit card works).
   Don't just put a dot in the middle: this base is large and square.
4. Tighten the 4 screws in an X pattern, a little at a time.
5. **On the first fixture, take it back apart** and check the paste print
   covers the whole base, then re-apply and tighten. If the
   COB plate bolts to the finned heatsink, that joint needs the same
   treatment.

## Frost frame (uses the existing front brackets)

The front has two curved accessory brackets (8.5 in apart, 3.5 in long, 2
screw holes 62 mm apart on each). Make a simple sandwich frame that screws to
them:

- **Two plates** of 0.040 in (1 mm) aluminum, or 1/16 in black ABS/PETG.
  The front glass of an LED fixture stays cool enough for plastic, but
  aluminum is the safer long-term choice.
  - Size: ~**9.5 × 7 in** (spans the brackets, covers the 140 mm / 5.5 in lens)
  - Center cut-out: **145 mm (5.7 in) circle**, slightly bigger than the lens
    so the frame doesn't shadow the beam
  - Holes: **2 per side, 62 mm apart**, matching the brackets. Drill to suit
    the bracket screws, and measure the exact side-to-side hole spacing on
    the fixture first.
- **Frost:** a ~**6.5 × 6.5 in** square sandwiched between the plates.
- Paint or anodize the plates black (or use black ABS) so there's no visible
  shine from the seats.
- Make one, test it, then use it as the drilling template for the rest. Or
  have a local sign/laser shop cut 64 plates from a drawing.

## Info status

Answered:
- ~~Dead color per unit / swap test~~: no longer needed. Both halves of the
  COB show burned dies, so every COB gets replaced.
- ~~COB dimensions and forward voltage~~: 40 × 40 mm, 34 × 34 mm holes,
  21 × 21 mm light area, Vf 30 V, 2.75 A total (common anode).
- ~~Fan size~~: NMB 3110KL-04W-B75, 80 × 80 × 25 mm, 12 V.
- ~~Typical service level~~: 100 %, all the time.
- ~~Per-color current~~: blue 1.4 A, green 1.4 A.
- ~~Mounting height / tilt~~: ~18 ft above the floor; yokes pivot and tilt.
- ~~Lens / frost mounting~~: 140 mm lens. Two front accessory brackets, 8.5 in
  apart, each 3.5 in long with 2 screw holes 62 mm apart
  (`docs/front_bracket.jpg`).

Still open:
- **Beam angle**, measured: point one fixture straight down, measure the
  width of the bright pool on the floor where it falls to about half
  brightness, then beam angle ≈ 2 × atan(width ÷ 2 ÷ 18 ft). Only needed to
  fine-tune the aiming.
