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
  
letter_to_value_dict = {}
value = 1
for letter in string.ascii_lowercase + string.ascii_uppercase:
  letter_to_value_dict[letter] = value
  value += 1

total_value = 0  
for element in shared_elements: 
  amount = letter_to_value_dict.get(element)
  total_value += amount

## Problem 2 

value_sum = 0
for i in range(0, len(lines), 3):
  common_element1 = set(lines[i]).intersection(lines[i+1])
  badge = set(lines[i+2]).intersection(common_element1).pop()
  group_val = letter_to_value_dict.get(badge)
  value_sum += group_val
  
