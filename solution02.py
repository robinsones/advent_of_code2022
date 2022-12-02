with open('input02.txt') as f:
    lines = [l.rstrip("\n") for l in f]

# 2500 length
len(lines)

translation_dict = {"A": 1, "B": 2, "C": 3, "Y": 2, "Z": 3, "X": 1}

elf = []
me = []
for l in lines:
  elf.append(l[0])
  me.append(l[2])

my_nb = []
elf_nb = []

for elf_play, my_play in zip(elf, me):
  elf_nb.append(translation_dict.get(elf_play))
  my_nb.append(translation_dict.get(my_play))

outcome = 0

for elf_play, my_play in zip(elf_nb, my_nb):
  if elf_play == my_play: 
    outcome += 3 + my_play
  elif my_play == 3 and elf_play == 1: 
    outcome += my_play
  elif elf_play == 3 and my_play == 1: 
    outcome += my_play + 6
  elif elf_play > my_play:
    outcome += my_play
  else: 
    outcome += 6 + my_play
  
    
# Y is draw, Z is win, X is lose    
# Part 2

# so now we know how many points we get from our play for the win/loss part,
# but not for the what i play part 
# well if it's a draw i play the same thing as them and get that many points

winning_dict = {"X": 0, "Y": 3, "Z": 6}
winning_points = 0
for x in me: 
  winning_points += winning_dict.get(x)
  
# now for the choice points

choice_points = 0
for elf_play, my_play in zip(elf_nb, my_nb):
  if my_play == 2: 
    choice_points += elf_play
  # if i lose
  if my_play == 1:
    if elf_play == 1:
      choice_points += 3
    elif elf_play == 2:
      choice_points += 1 
    else: 
      choice_points += 2
  if my_play == 3:
    if elf_play == 1:
      choice_points += 2
    elif elf_play == 2:
      choice_points += 3 
    else: 
      choice_points += 1
     
# final_points
winning_points + choice_points

# Better way from Jake https://github.com/jakevoytko/advent2022/tree/main/02
# tips use dict of dicts and reading in can split and calculate at read in 

scoring_table = {
  'A': {
    'X': 3,
    'Y': 1,
    'Z': 2,
  },
  'B': {
    'X': 1,
    'Y': 2,
    'Z': 3,
  },
  'C': {
    'X': 2,
    'Y': 3,
    'Z': 1,
  }
}
win_table = {
  'X': 0,
  'Y': 3,
  'Z': 6,
}
score = 0

with open('input02.txt', 'r') as data:
  for line in data:
    other, strategy = line.strip().split(' ')
    score += win_table[strategy]
    score += scoring_table[other][strategy]
print(score)

