import re
from collections import defaultdict

# because numpy issues causing scipy issues
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

lines = []

with open('input15.txt') as f:
  for l in f:
    xs, ys, xb, yb = [int(s) for s in re.findall(r'-?\d+', l)]
    sensor_loc = (xs, ys)
    beacon_loc = (xb, yb)
    md = manhattan(sensor_loc, beacon_loc)
    lines.append([sensor_loc, beacon_loc, md])

row_y = 2000000

candidates = []
for l in lines:
  if abs(row_y - l[0][1]) <= l[2]:
    candidates.append(l)

beacons_on_row_y = set([l[1][0] for l in lines if l[1][1] == row_y])
no_beacons_set = set()

for c in candidates:
  y_diff = abs(row_y - c[0][1])
  x_max_diff = c[2] - y_diff
  nb_min = c[0][0] - x_max_diff
  nb_max = c[0][0] + x_max_diff
  for i in range(nb_min, nb_max+1):
    no_beacons_set.add(i)

len(no_beacons_set ^ beacons_on_row_y)

## Part 2
grid_min = 0
grid_max = 4000000
y_ranges = [[] for _ in range(grid_max+1)]

# borrowed from leetcode
def merge(intervals):
    intervals.sort(key =lambda x: x[0])
    merged =[]
    for i in intervals:
        if not merged or merged[-1][-1] + 1 < i[0]:
            merged.append(i)
        else:
            merged[-1][-1] = max(merged[-1][-1], i[-1])
    return merged

for l in lines:
  sensor_x = l[0][0]
  max_d = l[2]
  sensor_y = l[0][1]
  for cur_y in range(max(grid_min, sensor_y - max_d), min(grid_max+1, sensor_y + max_d + 1)):
    y_diff = abs(cur_y - sensor_y)
    x_max_diff = max_d - y_diff
    nb_min = sensor_x - x_max_diff
    nb_max = sensor_x + x_max_diff
    y_ranges[cur_y].append([max(nb_min, grid_min), min(nb_max, grid_max)])

res = [merge(yr) for yr in y_ranges]
y_res = [i for i, r in enumerate(res) if r != [[grid_min, grid_max]]]

(res[2908372][0][1]+1)*4000000 + y_res[0]
