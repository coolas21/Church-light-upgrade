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

## Info still needed

- Fan size and voltage label (read the sticker)
- Which color is dead on each unit, and results of the swap test
- COB dimensions and forward voltage per half
- Ceiling mounting height, fixture spacing, and whether the yokes tilt
- Typical service level (if they run ~50–70 %, the temp-controlled fan will be
  near-silent almost all the time)
