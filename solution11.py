import math
import re

# operation and tests are always the same, it's items that change
all_items = []
all_ops = []
all_tests = []
all_tests_true = []
all_tests_false = []

with open('input11.txt') as f:
  for line in f: 
    if "Starting" in line:
      items = re.findall(r'\d+', line)
      all_items.append([int(i) for i in items])
    if "Operation" in line:
      all_ops.append(line.strip().split("old",1)[1])
    if "Test" in line: 
      all_tests.append(int(line.strip().split("divisible by ",1)[1]))
    if "If true" in line: 
      all_tests_true.append(int(line.strip().split("monkey ",1)[1]))
    if "If false" in line: 
      all_tests_false.append(int(line.strip().split("monkey ",1)[1]))

def monkey_worry(ops, initial_worry):
  if 'old' in ops:
    return initial_worry * initial_worry
  elif '*' in ops:
    return initial_worry * int(re.findall(r'\d+', ops)[0])
  elif '+' in ops:
    return initial_worry + int(re.findall(r'\d+', ops)[0])

inspections = [0 for i in range(len(all_tests))]

for _ in range(20):
  for mk_nb in range(len(all_tests)):
    for item in all_items[mk_nb]: 
      inspections[mk_nb] += 1
      new_worry = math.floor(monkey_worry(all_ops[mk_nb], item) / 3)
      if new_worry % all_tests[mk_nb] == 0:
        all_items[all_tests_true[mk_nb]].append(new_worry)
      else: 
        all_items[all_tests_false[mk_nb]].append(new_worry)
    all_items[mk_nb] = []
    
inspections.sort()
print(inspections[-1] * inspections[-2])

## Part 2

