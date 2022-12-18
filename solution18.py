lines = []

with open("input18.txt") as f:
  for l in f:
    x, y, z = l.strip().split(",")
    lines.append((int(x), int(y), int(z)))

non_touching_sides = 0

for ind, cube in enumerate(lines): 
  l_missing_cur = lines[:ind] + lines[ind+1:]
  if not any([lm[1] == cube[1] and lm[2] == cube[2] and lm[0]+1 == cube[0] for lm in l_missing_cur]):
    non_touching_sides += 1
  if not any([lm[1] == cube[1] and lm[2] == cube[2] and lm[0]-1 == cube[0] for lm in l_missing_cur]):
    non_touching_sides += 1
  if not any([lm[0] == cube[0] and lm[2] == cube[2] and lm[1]+1 == cube[1] for lm in l_missing_cur]):
    non_touching_sides += 1
  if not any([lm[0] == cube[0] and lm[2] == cube[2] and lm[1]-1 == cube[1] for lm in l_missing_cur]):
    non_touching_sides += 1
  if not any([lm[1] == cube[1] and lm[0] == cube[0] and lm[2]+1 == cube[2] for lm in l_missing_cur]):
    non_touching_sides += 1
  if not any([lm[1] == cube[1] and lm[0] == cube[0] and lm[2]-1 == cube[2] for lm in l_missing_cur]):
    non_touching_sides += 1

## Part 2
# what are the external sides?

