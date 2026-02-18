"""Simple test runner to validate A* implementation in astar_navigator.py
Run with: python3 tests/test_astar_runner.py
"""
import numpy as np
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))  # add package root to import astar_navigator

from astar_navigator import AStar

class SimpleOccupancy:
    def __init__(self, width, height, origin=(0,0), obstacles=None, resolution=1.0):
        self.width = width
        self.height = height
        self.origin = origin
        self.resolution = resolution
        # obstacles is a set of grid coordinates (x,y) in world units
        self.obstacles = set(obstacles or [])
        self.thresh = 0.5

    def is_free(self, x):
        # x is a tuple or array with (x,y)
        x = tuple([float(v) for v in x])
        # check bounds
        if x[0] < 0 or x[0] > self.width or x[1] < 0 or x[1] > self.height:
            return False
        # treat obstacle coordinates as exact match on grid
        if (round(x[0]), round(x[1])) in self.obstacles:
            return False
        return True

    def plot(self, fig_num=0):
        pass


def run_simple_test():
    # create a 20x15 map with a wall of obstacles leaving a gap
    width, height = 20, 15
    obstacles = []
    # vertical wall at x=10 except gap at y=7
    for y in range(0, height+1):
        if y == 7:
            continue
        obstacles.append((10, y))

    occ = SimpleOccupancy(width=width, height=height, obstacles=obstacles)

    start = (2, 7)
    goal = (18, 7)

    astar = AStar(statespace_lo=(0,0), statespace_hi=(width,height), x_init=start, x_goal=goal, occupancy=occ, resolution=1)
    success = astar.solve()
    if not success:
        print("A*: No path found")
        return 2

    print("A*: Path found with %d nodes:" % len(astar.path))
    print(astar.path)
    return 0

if __name__ == '__main__':
    rc = run_simple_test()
    sys.exit(rc)
