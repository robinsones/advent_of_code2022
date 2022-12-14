from collections import defaultdict
lines = []
with open("input14.txt") as f:
  for ind, l in enumerate(f):
    split_arrow = l.split(" -> ")
    cur_ent = []
    for i in split_arrow:
      cur_ent.append(tuple(map(int, i.split(','))))
    lines.append(cur_ent)

# how deep does the cave go? It's the max of y

max_y = max([y for pt in lines for _, y in pt])
max_x = max([x for pt in lines for x, _ in pt])
min_x = min([x for pt in lines for x, _ in pt])

# sand starts from point 500, 0 
# it wants to go down until it hits a rock, then tries to go down left, then down right
# Possible approaches: 
# - make a matrix to represent the graph

# maybe while the next one is unoccupied, go down one? 
# if can't go down left, if can't go down right, if can't do any stop?
# dictionary of tuples with "rock" "empty" or "sand"?

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

# it can't fall off map 
def sand_falling(gr, max_depth):
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

for _ in range(3000):
  one_grain(og_graph, max_y)
  
len([k for k, v in og_graph.items() if v == "sand"])

## Part 2

floor = max_y + 2
p2_graph = defaultdict(str) 
for path_set in lines:
  for len_p in range(len(path_set)):
    if len_p <= len(path_set)-2:
      draw_line(path_set[len_p], path_set[len_p+1], p2_graph)

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

while p2_graph[(500, 0)] != "sand":
  one_grainp2(p2_graph, floor)
  
len([k for k, v in p2_graph.items() if v == "sand"])
