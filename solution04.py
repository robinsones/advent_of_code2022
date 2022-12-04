import re 

with open('input04.txt') as f: 
  lines = [l.rstrip("\n") for l in f]

overlapping_pairs = 0
for l in lines: 
  nbs = re.split(',|-', l)
  nbs = [int(nb) for nb in nbs]
  if nbs[0] >= nbs[2] and nbs[1] <= nbs[3]:
    overlapping_pairs += 1
  elif nbs[2] >= nbs[0] and nbs[3] <= nbs[1]:
    overlapping_pairs += 1

## Problem 2
any_overlap = 0
for l in lines: 
  nbs = re.split(',|-', l)
  nbs = [int(nb) for nb in nbs]
  r1 = range(nbs[0], nbs[1] + 1)
  r2 = range(nbs[2], nbs[3] + 1)
  # is min number of one and max number of one smaller than max
  if len(set(r1).intersection(set(r2))):
    any_overlap += 1

