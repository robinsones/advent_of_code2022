import ast

lines = []
with open('input13.txt') as f:
  for l in f:
    li = l.strip()
    if li != '':
      literal_l = ast.literal_eval(li)
      lines.append(literal_l)

def compair(left, right):
  match left, right:
    case int(), int(): return left - right
    case list(), list():
      for l, r in zip(left, right):
        # := returns the value
        # if compair(l, r) is 0 is false 
        # we continue checking differences if 0, otherwise return 
        if diff := compair(l, r):
          return diff
      return len(left) - len(right)
    case int(), list():
      return compair([left], right)
    case list(), int():
      return compair(left, [right])

nb_in_ro = 0
for i, j in enumerate(range(0, len(lines), 2)):
  if compair(lines[j], lines[j+1]) < 0:
    nb_in_ro += i+1

## Part 2
from functools import cmp_to_key
lines.append([[2]])
lines.append([[6]])
sl = sorted(lines, key=cmp_to_key(compair))
(sl.index([[6]]) + 1)*(sl.index([[2]])+1)
