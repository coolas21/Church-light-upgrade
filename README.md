# Church 100 W Bi-Color COB Light – Quiet & Reliability Upgrade

Plan for ~30 no-name 100 W warm-white / daylight COB fixtures (6-ch DMX) that
have loud fans and dead warm or cool channels.

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
  (Arctic MX-4 / Noctua NT-H1 or similar), torque screws evenly.
- Blow dust out of the heatsink fins and housing vents.
- Replace the COB if a half is dead (see parts list).

### 2. Quiet fan + temperature control
- Replace the stock fan with a quality fluid-dynamic-bearing **4-pin PWM** fan
  of the same size (measure it — looks like 80 or 92 mm × 25 mm).
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

### 5. Validate (do on the first 1–2 units before doing all 30)
- Both channels at 100 % for 60 minutes in its normal hanging orientation.
- Measure the heatsink next to the COB: **target < 60 °C**; COB case
  **< 80 °C**. If over, raise the controller's fan curve or do step 3.
- Listen at the audience distance at normal service levels.

## Parts list (per fixture, rough prices)

| Item | Example | ~Cost |
|---|---|---|
| PWM fan, same size | Arctic P8 / P9 PWM, Noctua NF-A8 / NF-A9 PWM (quietest) | $8–$22 |
| PWM temp controller w/ NTC | "12 V 4-wire PWM fan temperature controller" module | $3–$8 |
| Thermal compound | Arctic MX-4 (one 20 g tube does all 30) | ~$1 |
| Replacement COB (if needed) | 100 W bi-color (≈3000 K + 6000 K), 2-channel, matching size & voltage | $8–$20 |
| Sense resistor (optional) | 0.15 Ω 2512 1 W | <$1 |

Roughly **$15–$50 per fixture**, vs ~$150–$300 each for a new quiet fixture.

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
  - Moving one or two repaired spare fixtures to the dead areas usually helps
    more than any diffuser.

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
5. **Add fixtures where the grid doesn't reach.** Repaired spares hung over
   the outer wedges beat any diffuser.

## Recommended parts (rebuild of all fixtures)

### COB: YUJILEDS 400H, 100 W bi-color, 3200 K / 5600 K, CRI 95+
- 46 × 40 mm module (the common 100 W footprint, so likely a drop-in. Measure
  the old COB and its screw holes before ordering).
- Forward voltage 28–33 V. That is good for this board's 36 V supply,
  because the buck driver needs a few volts of headroom.
- Sold in packs of two. **Order one pack first:** check fit, check that both
  channels light from the board, measure current per channel, and confirm it
  stays below the COB rating.
- 3200 K / 5600 K gives a far better color mix (and on-camera look) than the
  no-name originals.
- Source: https://store.yujiintl.com/products/yujileds-cri-95-100w-cob-led-3200k-5600k-400h

### Fan: 4-pin PWM, same size as the original
| Size | Quiet pick | Budget pick |
|---|---|---|
| 80 mm | Noctua NF-A8 PWM (2200 rpm, 17.7 dB(A) max, 2.37 mm H2O) | Arctic P8 PWM PST |
| 92 mm | Noctua NF-A9 PWM (2000 rpm) | Arctic P9-class PWM |

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
  resists pump-out. Each COB needs ~0.3–0.5 g, so ~15 g covers 30 fixtures.
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

`tools/coverage.py` models relative light at seat level from that plan. Since
the real height and beam angle are unknown, it was run for 18 ft / 40° and
24 ft / 60°:

- All house fixtures sit within Y = ±25 ft and X = −7…+16 ft. That leaves
  **a ~17 ft band along each side wall and a ~21 ft band at the rear with no
  fixture above it**.
- The front-center seats get 1.5–1.8× the average (the stage-front row at
  X = 24 also spills there). Side walls and rear corners get 10–30 %.
- Moving the ~5 spare fixtures to **(X, Y) = (8, ±36), (−16, ±30), (−24, 0)**
  cuts the seating area below half the average from **34 % to 14 %**
  (24 ft / 60°), or from 47 % to 26 % (18 ft / 40°).
- Narrow beams make it worse. Tilting the outer ring (6, ±25), (−3, ±24),
  (−7, ±15) outward 15–20° helps further.

See `docs/coverage_H24_B60.png` and `docs/coverage_H18_B40.png`. Re-run with the
real numbers: `python3 tools/coverage.py <height_ft> <beam_deg>`.

Full shopping list: `PARTS_LIST.md`.

## Aiming (tools/aiming.py)

With all 30 hung (25 existing + 5 spares), the model's best result comes
from one simple rule:

- **Tilt every house fixture 15–20° away from the room's center line,**
  sideways or toward the rear, **never toward the stage** (that glares the
  platform). Leave the two center-line fixtures at (8, 0) and (16, 0), the
  stage fixtures, and the 5 relocated spares pointing straight down.
- At 24 ft / 60°, the seating below half of today's average drops from
  14 % (spares added, all straight down) to **3 %**. At 18 ft / 40° it drops
  from 26 % to 15 %.
- Map with arrows: `docs/aiming_H24_B60.png`, `docs/aiming_H18_B40.png`.

How to aim in the field:
1. Aim offset on the floor = height × tan(tilt): at 24 ft, 18° is about 8 ft.
   Mark the aim point on a seat and point the beam center at it.
2. Aim with only that fixture on, both colors full, at night or with the house
   dark. Use a phone-camera snapshot to find the hot spot.
3. Lock the yoke bolts firmly and fit a safety cable on every fixture.
4. Check glare from the back row and the platform. If a lens is in someone's
   line of sight, back that fixture off 5°.

## DMX wiring (tools/dmx_route.py)

**Recommended: an opto-isolated DMX splitter at the booth with three home
runs** (left / center + stage / right, 9–12 fixtures each).

| | Option 1: splitter at booth | Option 2: splitter in ceiling |
|---|---|---|
| Cable (22 ft ceiling, incl. slack) | ~680 ft (~780 with spare) | ~660 ft (~750 with spare) |
| Power in ceiling | No | Yes, for the splitter |
| Troubleshooting | All at the booth | Need a lift |

The cable is about the same either way, so keep the electronics at the booth.

Rules:
- **Daisy-chain only** (OUT of one fixture to IN of the next). Never Y-split
  a cable; splitting is what the splitter's outputs are for.
- **Use 110–120 Ω DMX cable** (e.g. Belden 9841 or a DMX/AES-rated cable),
  not mic cable. Mic cable causes flicker and dropouts on long runs.
- **Terminate** the last fixture of each run with a 120 Ω XLR terminator.
- Each run stays well under the 32-device and ~1,000 ft limits. The board's
  SN75176B is a standard one-unit-load receiver.
- **Run DMX at least a foot away from power,** and cross power at right angles.
- Label both ends of every cable, and tag each fixture with its address.

Addressing: 30 × 6 ch = 180 channels, so one universe. Give fixtures **in the
same zone the same start address** so the console sees a few zones instead of
30 fixtures. For example: front house, rear house, left side, right side,
stage. Fixtures sharing an address simply mirror each other.

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
| 6 | Count the COB pads and read the +/− marks | Power off | 4 pads = separate channels, 3 = shared + | — |

From these, buy a COB whose **Vf per channel at that current is ≤ ~32 V**
(the 36 V supply needs headroom) and whose **rated current is ≥ the measured
current**. Watts per channel ≈ step 3 × step 4 current.

Tips: let it run 5 minutes before reading, because Vf drops a little as the
COB warms. If a reading jumps around, the channel isn't at full 100 %; set it
to full so the dimming PWM is off.

## Info still needed

- Which color is dead on each unit, and results of the swap test
- COB dimensions and forward voltage per half
- Ceiling mounting height and whether the yokes tilt
- Typical service level (if they run ~50–70 %, the temp-controlled fan will be
  near-silent almost all the time)
