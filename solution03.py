import string

with open('input03.txt') as f: 
  lines = [l.rstrip("\n") for l in f]

shared_elements = []
for l in lines: 
  split = int(len(l)/2)
  first_half = l[:split]
  second_half = l[split:]
  common_element = set(second_half).intersection(first_half).pop()
  shared_elements.append(common_element)
  
all_letters = string.ascii_lowercase + string.ascii_uppercase

total_value = 0  
for element in shared_elements: 
  amount = all_letters.index(element)
  total_value += amount

## Problem 2 

value_sum = 0
for i in range(0, len(lines), 3):
  common_element1 = set(lines[i]).intersection(lines[i+1])
  badge = set(lines[i+2]).intersection(common_element1).pop()
  group_val = all_letters.index(badge)
  value_sum += group_val

  
