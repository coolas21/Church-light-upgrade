"""Estimate DMX daisy-chain routes and cable lengths for the 30 fixtures.

Assumes cable follows the ceiling structure (right-angle runs, so Manhattan
distance), plus a fixed drop/slack allowance at every fixture, plus a riser
from the booth up to ceiling height.

Usage: python3 tools/dmx_route.py [ceiling_height_ft]
"""
import itertools
import sys

import coverage as c

BOOTH = (-28, 0)       # rear-centre sound booth
SLACK_PER_FIXTURE = 6  # drop to the fixture + service loop, feet
SPLITTER = (0, 0)      # optional ceiling splitter location (centre of grid)

ZONES = {
    "A - left": lambda f: f[0] < 20 and f[1] < -5,
    "B - centre + stage": lambda f: f[0] >= 20 or abs(f[1]) <= 5,
    "C - right": lambda f: f[0] < 20 and f[1] > 5,
}


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def route(start, pts):
    """Nearest-neighbour chain from start, then 2-opt clean-up."""
    order, left, cur = [], list(pts), start
    while left:
        nxt = min(left, key=lambda p: dist(cur, p))
        order.append(nxt)
        left.remove(nxt)
        cur = nxt

    def length(o):
        return sum(dist(a, b) for a, b in zip([start] + o, o))

    improved = True
    while improved:
        improved = False
        for i, j in itertools.combinations(range(len(order)), 2):
            new = order[:i] + order[i:j + 1][::-1] + order[j + 1:]
            if length(new) < length(order) - 1e-9:
                order, improved = new, True
    return order, length(order)


def main():
    height = float(sys.argv[1]) if len(sys.argv) > 1 else 18
    fixtures = c.FIXTURES + c.SUGGESTED
    print(f"{len(fixtures)} fixtures, ceiling ~{height:g} ft\n")

    for label, origin, riser in [("Option 1: three home runs from the booth",
                                  BOOTH, height),
                                 ("Option 2: one run to a ceiling splitter",
                                  SPLITTER, 0)]:
        print(label)
        total = 0
        if origin == SPLITTER:
            feed = dist(BOOTH, SPLITTER) + height
            print(f"  booth -> splitter feed: {feed:.0f} ft")
            total += feed
        for name, test in ZONES.items():
            pts = [f for f in fixtures if test(f)]
            order, run = route(origin, pts)
            run += riser + SLACK_PER_FIXTURE * len(pts)
            total += run
            path = " -> ".join(f"({x:g},{y:g})" for x, y in order)
            print(f"  {name}: {len(pts)} fixtures, ~{run:.0f} ft\n    {path}")
        print(f"  TOTAL cable ~{total:.0f} ft (+15 % spare = "
              f"{total * 1.15:.0f} ft)\n")


if __name__ == "__main__":
    main()
