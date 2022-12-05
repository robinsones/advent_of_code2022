import re 
import copy

with open('input05.txt') as f: 
  lines = [l.rstrip("\n") for l in f]

movements = [l for l in lines if l.startswith('move')]
nb_movements = [[int(s) for s in re.findall(r'\d+', l)] for l in movements]

crates = [l for l in lines if '[' in l]
stacked_crates = [[] for i in range(9)]

for row in list(reversed(crates)): 
  for i, v in enumerate(range(1, len(row), 4)):
    if row[v] != ' ':
      stacked_crates[i].append(row[v])

second_stack = copy.deepcopy(stacked_crates)

for m in nb_movements: 
  nb_crates, from_stack, to_stack = m
  to_move = stacked_crates[from_stack-1][-nb_crates:][::-1]
  stacked_crates[from_stack-1] = stacked_crates[from_stack-1][:-nb_crates]
  stacked_crates[to_stack-1] += to_move

last_crates = [i[-1] for i in stacked_crates]
''.join(last_crates)

for m in nb_movements: 
  nb_crates, from_stack, to_stack = m
  to_move = second_stack[from_stack-1][-nb_crates:]
  second_stack[from_stack-1] = second_stack[from_stack-1][:-nb_crates]
  second_stack[to_stack-1] += to_move

last_crates_new_crane = [i[-1] for i in second_stack]
''.join(last_crates_new_crane)
