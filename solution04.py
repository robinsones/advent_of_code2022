import re 

with open('input04.txt') as f: 
  lines = [l.rstrip("\n") for l in f]

overlapping_pairs = 0
for l in lines: 
  nbs = re.split(',|-', l)
  min1, max1, min2, max2 = [int(nb) for nb in nbs]
  if min1 >= min2 and max1 <= max2:
    overlapping_pairs += 1
  elif min2 >= min1 and max2 <= max1:
    overlapping_pairs += 1

## Problem 2
any_overlap = 0
for l in lines: 
  nbs = re.split(',|-', l)
  nbs = [int(nb) for nb in nbs]
  r1 = range(nbs[0], nbs[1] + 1)
  r2 = range(nbs[2], nbs[3] + 1)
  if len(set(r1).intersection(set(r2))):
    any_overlap += 1

