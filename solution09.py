import copy

with open("input09.txt") as f: 
  lines = [l.strip() for l in f]

list_lines = [[i[0], int(i[2:])] for i in lines]

def move_rope(directions, cur_pos):
  des = directions[0]
  if des == "U":
    cur_pos[0] += 1
  elif des == "D":
    cur_pos[0] -= 1
  elif des == "L":
    cur_pos[1] -= 1
  elif des == "R":
    cur_pos[1] += 1

def too_far(head_cur_pos, tail_cur_pos):
  if abs(head_cur_pos[0] - tail_cur_pos[0]) > 1 or abs(head_cur_pos[1] - tail_cur_pos[1]) > 1:
    return True 
  else:
    return False

def move_diagnoal(head_cur_pos, tail_cur_pos):
  if abs(head_cur_pos[0] - tail_cur_pos[0]) == 1:
    tail_cur_pos[0] = head_cur_pos[0]
    if head_cur_pos[1] > tail_cur_pos[1]:
      tail_cur_pos[1] += 1
    else:
      tail_cur_pos[1] -= 1
  elif abs(head_cur_pos[1] - tail_cur_pos[1]) == 1:
    tail_cur_pos[1] = head_cur_pos[1]
    if head_cur_pos[0] > tail_cur_pos[0]:
      tail_cur_pos[0] += 1
    else:
      tail_cur_pos[0] -= 1
  else:
    if head_cur_pos[1] > tail_cur_pos[1]:
      tail_cur_pos[1] += 1
    if head_cur_pos[1] < tail_cur_pos[1]: 
      tail_cur_pos[1] -= 1
    if head_cur_pos[0] > tail_cur_pos[0]:
      tail_cur_pos[0] += 1
    if  head_cur_pos[0] < tail_cur_pos[0]:
      tail_cur_pos[0] -= 1
  
def move_tail(head_cur_pos, tail_cur_pos, directions):
  while too_far(head_cur_pos, tail_cur_pos):
    if head_cur_pos[0] == tail_cur_pos[0] or head_cur_pos[1] == tail_cur_pos[1]:
      move_rope(directions, tail_cur_pos)
    else:
      move_diagnoal(head_cur_pos, tail_cur_pos)

cur_head_pos = [0, 0]
cur_tail_pos = [0, 0]
spots_visited = []

for tm in list_lines:
  for i in range(tm[1]):
    move_rope(tm, cur_head_pos)
    move_tail(cur_head_pos, cur_tail_pos, tm)
    cpt = copy.deepcopy(cur_tail_pos)
    if cpt not in spots_visited:
      spots_visited.append(cpt)

len(spots_visited)

## Problem 2 

tenth_spots_visited = []
all_positions = [[0, 0] for i in range(10)]

for tm in list_lines:
  for i in range(tm[1]):
    # first move the head as instructed
    move_rope(tm, all_positions[0])
    # then move the rest of the rope
    for p, r in enumerate(all_positions[1:], 1):
      move_tail(all_positions[p-1], all_positions[p], tm)
      dcpt = copy.deepcopy(all_positions[9])
      if dcpt not in tenth_spots_visited:
        tenth_spots_visited.append(dcpt)
        
len(tenth_spots_visited)
