with open('input08.txt') as f: 
  lines = [[int(i) for a,i in enumerate(l.strip())] for l in f]

outer_edge_size = len(lines[0]) * 2 + len(lines) * 2 - 4

running_count = 0
for i, l in enumerate(lines): 
  for ind, v in enumerate(l): 
    if ind not in (0, len(l) - 1) and i not in (0, len(l) - 1):
      col = [x[ind] for x in lines]
      if any((v > max(l[ind+1:]), v > max(l[:ind]), v > max(col[i+1:]), v > max(col[:i]))):
        running_count += 1

running_count + outer_edge_size

## Problem 2

# how many trees in each direction until i hit an equal or greater height?

def get_view(li, v):
  for x, y in enumerate(li):
    if y >= v:
      return x+1
  return len(li)

max_product = 0
for i, l in enumerate(lines): 
  for ind, v in enumerate(l): 
    if ind not in (0, len(l) - 1) and i not in (0, len(l) - 1):
      col = [x[ind] for x in lines]
      s1 = get_view(l[ind+1:], v)
      s2 = get_view(l[:ind][::-1], v)
      s3 = get_view(col[i+1:], v)
      s4 = get_view(col[:i][::-1], v)
      product = s1*s2*s3*s4
      if product > max_product:
        max_product = product
        lens = [s1, s2, s3, s4, ind, i]

