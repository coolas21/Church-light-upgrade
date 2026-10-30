# Capacitor List (fill in from one fixture)

Read the printing on the side of each cap. Measure size with calipers.
Use this list to order for all 25 (+ a few spares).

| Location | µF | Voltage | Temp | Size (mm) | Lead spacing | Qty / fixture | Order (25 + spares) | Replacement |
|---|---|---|---|---|---|---|---|---|
| PSU C5, C6, C9, C10 (36 V output) | 470 | 50 V | 105 °C | 10 × 20 (measured ~9) | 5.0 mm | 4 | **110** | **Rubycon 50ZLJ470M10X20** (10,000 h). Keep 50 V; a 63 V part is usually too big to fit |
| PSU C7, C8 (12 V output) | 1000 | 25 V | 105 °C | 10 × 20 | 5.0 mm | 2 | **55** | **Panasonic EEU-FR1E102** (10,000 h) |
| PSU C4 (controller supply) | 33 | 50 V | 105 °C | 6.3 × 11 (measured ~6) | 2.5 mm | 1 | **30** | Any low-ESR 105 °C long-life 33 µF 50 V, 6.3 × 11, 2.5 mm (Panasonic FR, Nichicon PW/HE, Rubycon ZLH/ZLJ). Pick one in stock |

Notes:
- "9 mm" and "6 mm" readings are almost certainly the standard **10 mm** and
  **6.3 mm** cans (the plastic sleeve throws calipers off a bit).
- Confirm the lead spacing once: **~5 mm** between the two legs on the big
  ones, **~2.5 mm** on C4. If the big ones measure ~3.5 mm instead, they're
  8 mm cans: tell me and I'll swap the part numbers.
- Buying 100+ of a part usually hits a price break, so order the full
  quantity in one go.

How to read and measure:
- **µF**: printed as e.g. `1000µF` or `1000uF`.
- **Voltage**: printed as e.g. `50V`. The new cap must be the **same or higher**.
- **Temp**: `105°C` (buy 105 °C).
- **Diameter**: across the top. **Height**: from the board to the top of the can.
  The new cap can be the same size or smaller, never wider or it won't fit.
- **Lead spacing**: center of one lead to the other where they enter the board
  (usually 2.0 / 2.5 / 3.5 / 5.0 / 7.5 mm). Measure on the solder side if the
  cap is still in.
- **Polarity**: the stripe on the can marks **negative (−)**. The board usually
  has a shaded half-circle or "+" mark. Photograph each spot before removing.

Ordering on Digi-Key or Mouser: filter by aluminum electrolytic → µF →
voltage → 105 °C → diameter → lead spacing, then sort by lowest ESR /
longest life (e.g. 5,000–10,000 h). Panasonic FR/FM, Nichicon HE/PW and
Rubycon ZLH/ZLJ are good series.
