from collections import defaultdict
import copy

lines = []
with open("input14.txt") as f:
  for ind, l in enumerate(f):
    split_arrow = l.split(" -> ")
    cur_ent = []
    for i in split_arrow:
      cur_ent.append(tuple(map(int, i.split(','))))
    lines.append(cur_ent)

max_y = max([y for pt in lines for _, y in pt])

def draw_line(left, right, graph_d):
  sm_horiz = min(left[0], right[0])
  lg_horiz = max(left[0], right[0])
  sm_vert = min(left[1], right[1])
  lg_vert = max(left[1], right[1])
  for horiz in range(sm_horiz, lg_horiz+1):
    graph_d[(horiz, left[1])] = "rock"
  for vert in range(sm_vert, lg_vert+1):
    graph_d[(left[0], vert)] = "rock"

og_graph = defaultdict(str) 
for path_set in lines:
  for len_p in range(len(path_set)):
    if len_p <= len(path_set)-2:
      draw_line(path_set[len_p], path_set[len_p+1], og_graph)

copy_og_graph = copy.deepcopy(og_graph)

def sand_falling(gr, max_depth, cur_pos):
  if cur_pos[1] == max_depth:
    return True, cur_pos
  elif gr[(cur_pos[0], cur_pos[1]+1)] == '':
    cur_pos = (cur_pos[0], cur_pos[1]+1)
    return False, cur_pos
  elif gr[(cur_pos[0]-1, cur_pos[1]+1)] == '':
    cur_pos = (cur_pos[0]-1, cur_pos[1]+1)
    return False, cur_pos
  elif gr[(cur_pos[0]+1, cur_pos[1]+1)] == '':
    cur_pos = (cur_pos[0]+1, cur_pos[1]+1)
    return False, cur_pos
  else:
    gr[(cur_pos[0], cur_pos[1])] = "sand"
    return True, cur_pos

def one_grain(og_graph, max_depth):
  cp = (500, 0)
  while True:
    bool_val, cp = sand_falling(og_graph, max_depth, cp)
    if bool_val:
      break

for _ in range(2000):
  one_grain(og_graph, max_y)
  
len([k for k, v in og_graph.items() if v == "sand"])

## Part 2

floor = max_y + 2

def sand_fallingp2(gr, max_depth, cur_pos):
  if cur_pos[1] == max_depth-1:
    gr[(cur_pos[0], cur_pos[1])] = "sand"
    return True, cur_pos
  elif gr[(cur_pos[0], cur_pos[1]+1)] == '':
    cur_pos = (cur_pos[0], cur_pos[1]+1)
    return False, cur_pos
  elif gr[(cur_pos[0]-1, cur_pos[1]+1)] == '':
    cur_pos = (cur_pos[0]-1, cur_pos[1]+1)
    return False, cur_pos
  elif gr[(cur_pos[0]+1, cur_pos[1]+1)] == '':
    cur_pos = (cur_pos[0]+1, cur_pos[1]+1)
    return False, cur_pos
  else:
    gr[(cur_pos[0], cur_pos[1])] = "sand"
    return True, cur_pos

def one_grainp2(og_graph, max_depth):
  cp = (500, 0)
  while True:
    bool_val, cp = sand_fallingp2(og_graph, max_depth, cp)
    if bool_val:
      break

while copy_og_graph[(500, 0)] != "sand":
  one_grainp2(copy_og_graph, floor)
  
len([k for k, v in copy_og_graph.items() if v == "sand"])
