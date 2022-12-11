with open('input10.txt') as f:
  lines = [l.strip() for l in f]


X = 1
cycle = 0
nb_l = []
rel_cycl = [20, 60, 100, 140, 180, 220]

for i in lines:
  if i == "noop":
    cycle += 1
    if cycle in rel_cycl:
        nb_l.append(cycle * X)
  else:
    instr, am = i.split()
    if instr == "addx":
      cycle += 1
      if cycle in rel_cycl:
        nb_l.append(cycle * X)
      cycle += 1
      if cycle in rel_cycl:
        nb_l.append(cycle * X)
      X += int(am)

sum(nb_l)

## Part 2

def check_sprite(m_sprite_pos, gr): 
  row = len(gr) // 40
  cl = len(gr) - row*40
  if m_sprite_pos-1 <= cl <= m_sprite_pos+1:
    gr = gr + "#"
  else:
    gr = gr + "."
  return gr

grid = ""
mid_sprite_pos = 1

for i in lines:
  if i == "noop":
    grid = check_sprite(mid_sprite_pos, grid)
  else:
    instr, am = i.split()
    if instr == "addx":
      grid = check_sprite(mid_sprite_pos, grid)
      grid = check_sprite(mid_sprite_pos, grid)
      mid_sprite_pos += int(am)

grid[0:40]
grid[40:80]
grid[80:120]
grid[120:160]
grid[160:200]
grid[200:]


####.#..#.###..###..####.####..##..#....
...#.#..#.#..#.#..#.#....#....#..#.#....
..#..#..#.#..#.#..#.###..###..#....#....
.#...#..#.###..###..#....#....#....#....
#....#..#.#....#.#..#....#....#..#.#....
####..##..#....#..#.#....####..##..####.
