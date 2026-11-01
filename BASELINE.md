# Baseline Light Readings (before repairs)

Phone light-meter readings (lux) taken around the room, written on the plan
(`docs/baseline_lux_sketch.jpg`). Positions are estimated from the sketch, in
the same X/Y feet as the fixture plan. Many fixtures currently have one
dead color, so this is the "before" picture.

| Spot (X, Y) | Area | Lux |
|---|---|---|
| (32, 0) / (34, ±12) | Stage, back | 370 / 335 / 324 |
| (24, 0) / (24, ±12) | Stage, front row of fixtures | 270 / 280 / 408 |
| (~20, −12) / (~19, 0) / (~20, +10) | Stage edge | 245 / 225 / 240 |
| (13, −17) / (13, +17) | Front seating | 250 / 267 |
| (8, 0) | Center seating | 291 |
| (−3, −24) | Left seating | 206 |
| (−7, 5) / (−7, 15) | Rear-center seating | 250 / 280 |
| (~13, +35) | Right front wedge, by side wall | **57** |
| (~−8, +38) | Right side wall, rear | **45** |
| (~−18, +18) | Right rear corner | **65** |
| (~−22, +5) | Rear wall, center | **63** |
| (~−14, −29) | Left rear corner | **37** |

**Takeaways**
- Seating under the fixture grid: **~200–290 lux (19–27 fc)**. That's plenty;
  100–200 lux is typical for congregation seating with reading.
- Side walls and rear corners: **37–65 lux (3–6 fc)**, about **15–25 % of
  the center**. These are the dead spots, and they're too dim to read
  comfortably.
- Stage readings include the stage lighting, so they weren't used for the fit.

## What the readings tell the model
Fitting `tools/coverage.py` to the 11 seating readings (fixtures 18 ft up,
~15.5 ft above the seats) gives a best match with an **effective beam of
~90°**, much wider than the 45–60° guessed earlier. The fit is within ~±18 %
at most points. (The left-rear 37 reads lower than the model's 55, likely a
fixture there with a dead half.) The default beam in the tools is now 90°.

Predicted at the dark spots (lux, same output as today):

| Spot | Today | Aimed (25 fixtures) | +5 fixtures at the edges |
|---|---|---|---|
| Right front wedge | 57 | ~77 | ~103 |
| Right side wall, rear | 45 | ~59 | ~65 |
| Right rear corner | 65 | ~79 | ~97 |
| Rear wall center | 63 | ~58 | ~109 |
| Left rear corner | 37 | ~78 | ~123 |
| Center seating | 250–290 | ~190–210 | ~250–340 |

- **Aiming helps the edges ~15–80 %** at the cost of the over-lit center
  (which stays ~200 lux, still plenty). It won't get the edges to 100 lux by
  itself, because the beams are already wide.
- **The repairs add on top of this** wherever a fixture now has a dead half.
- **To get the edges to ~100 lux (10 fc), fixtures need to be added** at the
  edges (see README "Do we need more fixtures?"). The rear side walls would
  need one placed further back, around (−6, ±36).

**After the rebuild:** take readings at the same spots, at night with the same
other lights on or off as today, and the same phone and app, to compare.
