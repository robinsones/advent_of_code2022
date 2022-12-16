import re
from collections import defaultdict

# because numpy issues causing scipy issues
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

lines = []

with open('input15.txt') as f:
  for l in f:
    xs, ys, xb, yb = [int(s) for s in re.findall(r'\d+', l)]
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
# distress between 0 and 4000000
# multiply x by 4000000 and add y

# there is only one non possible one in entire grid
# hmm can we go like row by row?


