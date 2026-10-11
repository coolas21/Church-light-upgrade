"""Suggest aim points for the house fixtures using the coverage model.

Each house fixture may be aimed at a floor point pushed outward from the room
centre: sideways or toward the rear, never toward the stage (that would glare
the platform). The script tries offsets and keeps whichever lifts the darkest
10 % of seats most, while the middle of the room must keep >= 85 % of its
straight-down level. Tilt is capped at MAX_TILT to limit glare.

Usage: python3 tools/aiming.py [height_ft] [beam_deg]
"""
import math
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import coverage as c

CENTRE = (2, 0)          # roughly the middle of the seating
OFFSETS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
MAX_TILT = 25            # degrees from straight down
STAGE_X = 20             # fixtures at/over the stage are left alone


def lit(fx, fy, ax, ay, X, Y, height, m):
    """Illuminance on the seat plane from one fixture aimed at (ax, ay)."""
    a = np.array([ax - fx, ay - fy, -height], float)
    a /= np.linalg.norm(a)
    vx, vy = X - fx, Y - fy
    d = np.sqrt(vx ** 2 + vy ** 2 + height ** 2)
    cos_beam = np.clip((a[0] * vx + a[1] * vy - a[2] * height) / d, 0, 1)
    return cos_beam ** m * (height / d) / d ** 2


def aim_point(f, off):
    dx, dy = min(f[0] - CENTRE[0], 0), f[1] - CENTRE[1]
    r = math.hypot(dx, dy) or 1
    return f[0] + dx / r * off, f[1] + dy / r * off


def main():
    height = float(sys.argv[1]) if len(sys.argv) > 1 else 15.5
    beam = float(sys.argv[2]) if len(sys.argv) > 2 else 50
    m = math.log(0.5) / math.log(math.cos(math.radians(beam / 2)))

    xs, ys = np.arange(-29, 42, 0.5), np.arange(-44, 44.5, 0.5)
    Y, X = np.meshgrid(ys, xs)
    mask = c.seating_mask(X, Y)

    fixtures = c.FIXTURES + c.SUGGESTED
    offs = [0] * len(fixtures)
    contrib = [lit(*f, *f, X, Y, height, m) for f in fixtures]
    total = sum(contrib)
    norm = c.illuminance(c.FIXTURES, X, Y, height, beam)[mask].mean()
    start = total[mask] / norm

    floor = 0.85 * np.median(total[mask])

    def score(E):
        if np.median(E[mask]) < floor:
            return -1
        return np.percentile(E[mask], 10)

    for _ in range(3):  # a few passes of coordinate descent
        for i, f in enumerate(fixtures):
            if f[0] >= STAGE_X:
                continue
            best = (score(total), offs[i], contrib[i])
            for off in OFFSETS:
                if math.degrees(math.atan(off / height)) > MAX_TILT:
                    continue
                ci = lit(*f, *aim_point(f, off), X, Y, height, m)
                s = score(total - contrib[i] + ci)
                if s > best[0] + 1e-9:
                    best = (s, off, ci)
            total = total - contrib[i] + best[2]
            offs[i], contrib[i] = best[1], best[2]

    end = total[mask] / norm
    print(f"H={height} beam={beam} (all 30 hung, relative to today's average)")
    print(f"  straight down : p10={np.percentile(start, 10):.2f} "
          f"below-half={(start < 0.5).mean():.0%}")
    print(f"  with aiming   : p10={np.percentile(end, 10):.2f} "
          f"below-half={(end < 0.5).mean():.0%}")
    print("  fixture (X,Y) -> aim at (X,Y), tilt")
    rows = []
    for f, off in zip(fixtures, offs):
        if f[0] >= STAGE_X or off == 0:
            continue
        ax, ay = aim_point(f, off)
        tilt = math.degrees(math.atan(off / height))
        rows.append((f, (round(ax, 1), round(ay, 1)), round(tilt)))
        print(f"    {f} -> ({ax:.0f}, {ay:.0f})  {tilt:.0f}°")

    fig, ax = plt.subplots(figsize=(7, 6.5))
    im = c.plot(ax, X, Y, total * c.illuminance(c.FIXTURES, X, Y, height, beam)[mask].mean()
                / norm, mask, c.FIXTURES, c.SUGGESTED,
                f"All 30 hung + aimed: H={height:g} ft, beam={beam:g}°\n"
                f"darkest-10% {np.percentile(end, 10):.2f}, "
                f"{(end < 0.5).mean():.0%} of seating < half of today's avg")
    for f, (ax_, ay_), _ in rows:
        ax.annotate("", xy=(ay_, ax_), xytext=(f[1], f[0]),
                    arrowprops=dict(arrowstyle="->", color="cyan", lw=1.2))
    fig.colorbar(im, ax=ax, shrink=0.7, label="relative light (1 = today's avg)")
    out = f"docs/aiming_H{height:g}_B{beam:g}.png"
    fig.savefig(out, dpi=110, bbox_inches="tight")
    print("  ->", out)


if __name__ == "__main__":
    main()
