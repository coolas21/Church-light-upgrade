"""Relative house-light coverage model for the sanctuary.

Coordinates in feet, read from the hand-drawn plan:
  X = toward the stage (+) / toward the rear wall (-)
  Y = left (-) / right (+) facing the stage
All fixtures are assumed hung at the same height and aimed straight down.
Output is *relative* (1.0 = average over the seating), so it shows where the
dark spots are, not absolute foot-candles.

Usage: python3 tools/coverage.py [height_ft] [beam_deg] [N]
  N omitted -> plot the SUGGESTED extra positions
  N given   -> search for the N best extra positions
"""
import math
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
import numpy as np

FIXTURES = [
    # over the stage
    (32, 0), (34, -12), (34, 12), (24, -12), (24, 0), (24, 12),
    # house
    (16, 0), (13, -17), (13, 17), (11, -9.5), (11, 9.5), (8, 0),
    (6, -25), (6, 25), (3, -17), (3, 17),
    (0, -9.5), (0, 0), (0, 9.5), (-3, -24), (-3, 24),
    (-7, -15), (-7, -5), (-7, 5), (-7, 15),
]

# Suggested positions for the ~5 spare fixtures (30 owned - 25 hung)
SUGGESTED = [(8, -36), (8, 36), (-16, -30), (-16, 30), (-24, 0)]

ROOM = [(41, -23), (41, 23), (30, 23), (13, 42.5), (-15, 42.5), (-28, 19),
        (-28, -19), (-15, -42.5), (13, -42.5), (30, -23)]

# Stage front edge: arc through (19.5, 0) and (27, +/-26)
ARC_XC, ARC_R = 68.3, 48.8


def seating_mask(X, Y):
    inside = Path([(y, x) for x, y in ROOM]).contains_points(
        np.c_[Y.ravel(), X.ravel()]).reshape(X.shape)
    off_stage = (X - ARC_XC) ** 2 + Y ** 2 > ARC_R ** 2
    return inside & off_stage & (X < 30)


def illuminance(fixtures, X, Y, height, beam_deg):
    # cos^m beam: half intensity at beam_deg / 2
    m = math.log(0.5) / math.log(math.cos(math.radians(beam_deg / 2)))
    E = np.zeros_like(X)
    for fx, fy in fixtures:
        r2 = (X - fx) ** 2 + (Y - fy) ** 2
        d2 = r2 + height ** 2
        cos_t = height / np.sqrt(d2)
        E += cos_t ** m * cos_t / d2
    return E


def add_fixtures(n, X, Y, mask, height, beam_deg):
    """Greedy: add n fixtures that most raise the darkest 10% of seats."""
    base = illuminance(FIXTURES, X, Y, height, beam_deg)
    cands = [(cx, cy) for cx in range(-24, 20, 2) for cy in range(-40, 41, 2)
             if seating_mask(np.array([[cx]]), np.array([[cy]]))[0, 0]]
    added = []
    for _ in range(n):
        best = max(cands, key=lambda c: np.percentile(
            (base + illuminance([c], X, Y, height, beam_deg))[mask], 10))
        added.append(best)
        base = base + illuminance([best], X, Y, height, beam_deg)
        cands.remove(best)
    return added


def stats(E, mask):
    v = E[mask] / E[mask].mean()
    return v.min(), np.percentile(v, 10), (v < 0.5).mean()


def plot(ax, X, Y, E, mask, fixtures, added, title):
    rel = np.where(mask, E / E[mask].mean(), np.nan)
    im = ax.pcolormesh(Y, X, rel, cmap="inferno", vmin=0, vmax=1.8,
                       shading="auto")
    ax.contour(Y, X, np.nan_to_num(rel, nan=9), levels=[0.5], colors="cyan",
               linewidths=1)
    rx, ry = zip(*(ROOM + ROOM[:1]))
    ax.plot(ry, rx, color="0.5")
    t = np.linspace(-0.56, 0.56, 50)
    ax.plot(ARC_R * np.sin(t), ARC_XC - ARC_R * np.cos(t), color="0.5", ls="--")
    ax.scatter([f[1] for f in fixtures], [f[0] for f in fixtures], c="white",
               edgecolors="k", s=30, zorder=3, label="existing")
    if added:
        ax.scatter([f[1] for f in added], [f[0] for f in added], c="lime",
                   edgecolors="k", s=60, marker="*", zorder=4, label="add")
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("Y (ft)")
    ax.set_ylabel("X (ft)  stage ↑")
    ax.legend(loc="lower right", fontsize=7)
    return im


if __name__ == "__main__":
    height = float(sys.argv[1]) if len(sys.argv) > 1 else 22
    beam = float(sys.argv[2]) if len(sys.argv) > 2 else 50

    xs, ys = np.arange(-29, 42, 0.5), np.arange(-44, 44.5, 0.5)
    Y, X = np.meshgrid(ys, xs)
    mask = seating_mask(X, Y)

    E0 = illuminance(FIXTURES, X, Y, height, beam)
    if len(sys.argv) > 3:
        added = add_fixtures(int(sys.argv[3]), X, Y, mask, height, beam)
    else:
        added = SUGGESTED
    n_add = len(added)
    E1 = E0 + illuminance(added, X, Y, height, beam)
    # normalise both maps to the *current* average so they compare
    norm = E0[mask].mean()

    fig, axes = plt.subplots(1, 2, figsize=(13, 6.5))
    for ax, E, add, name in [(axes[0], E0, [], "Current"),
                             (axes[1], E1, added, f"+{n_add} relocated")]:
        v = E[mask] / norm
        im = plot(ax, X, Y, E * E0[mask].mean() / norm, mask, FIXTURES, add,
                  f"{name}: H={height:g} ft, beam={beam:g}°\n"
                  f"min {v.min():.2f}, darkest-10% {np.percentile(v, 10):.2f}, "
                  f"{(v < 0.5).mean():.0%} of seating < half avg")
    fig.colorbar(im, ax=axes, shrink=0.7, label="relative light (1 = current avg)")
    out = f"docs/coverage_H{height:g}_B{beam:g}.png"
    fig.savefig(out, dpi=110, bbox_inches="tight")

    s0 = stats(E0, mask)
    print(f"H={height} beam={beam}: current min={s0[0]:.2f} p10={s0[1]:.2f} "
          f"below-half={s0[2]:.0%}")
    v1 = E1[mask] / norm
    print(f"  with adds: min={v1.min():.2f} p10={np.percentile(v1, 10):.2f} "
          f"below-half={(v1 < 0.5).mean():.0%}")
    print("  add at (X, Y):", added)
    print("  ->", out)
