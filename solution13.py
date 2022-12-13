# pairs are separated by a blank line, are they in the right order?

# consistents of lists and integers
# each packet is always a list
# first value is called left and second is called right
# if both are int lower int should come first (left is lower than right is good)
# both are list, compare first val then second, left runs out of items first, inputs in right order, just about length
# if only one is int make list

# indices in right order, get sum
import ast

lines = []
with open('input13.txt') as f:
  for l in f:
    li = l.strip()
    if li != '':
      literal_l = ast.literal_eval(li)
      lines.append(literal_l)
    else:
      lines.append('')
  
# if two lists
# true is in order
def convert_to_list(potential_int):
  if isinstance(potential_int, int):
    return [potential_int]
  else:
    return potential_int

def check_if_nested(pot_net):
  return any(isinstance(i, list) for i in pot_net)

#  and not (len(l1) == 1 or len(l2) == 1)
def lists_in_order_rec(l1, l2):
  # given a list or intergers
  l1 = convert_to_list(l1)
  l2 = convert_to_list(l2)
  print("hazaah!")
  if (check_if_nested(l1) or check_if_nested(l2)):
    for lsp, rsp in zip(l1,l2):
      res = lists_in_order_rec(lsp, rsp)
      if not res:
        return False
  # check if just lots of []
  za = (check_if_nested(l1) or check_if_nested(l2))
  print(l1, l2)
  print("hello!", za)
  if any([in_ls > in_rs for in_ls, in_rs in zip(l1, l2)]):
    return False
  elif len(l1) > len(l2):
    return False
  else:
    return True
  
  # now they're not nested
  print(l1, l2)
  for lsp, rsp in zip(l1,l2):
    ls = convert_to_list(lsp)
    rs = convert_to_list(rsp)
    if check_if_nested(ls):
      lists_in_order_rec(ls, rs)
    if check_if_nested(rs):
      lists_in_order_rec(ls, rs)
    if any([in_ls > in_rs for in_ls, in_rs in zip(ls, rs)]):
      return False
    if len()
  if len(l1) > len(l2):
    return False
  else: 
    return True

nb_in_ro = 0
run_i = 0
for i, j in enumerate(range(0, len(lines), 3)):
  run_i += i+1
  all_in_order = True
  print(i, j)
  if lists_in_order_rec(lines[j], lines[j+1]):
    nb_in_ro += i+1

# how to compare [9, 2] to [[[i1, i2, i3, i4]], [i5, i6]]]
# compare 9 to [[i1, i2, i3, i4]], [i5, i6]]
# compare [9] to [[i1, i2, i3, i4]], [i5, i6]]
# compare [9] to [i1, i2, i3, i4]?
# so that's 9 to i1

# [0, 7, [[7, 10, 2, 7, 2], 7], [3, 7], 1] to [[], [[0, 5, 2]], 10, 9, 0] 
# compare 0 to []
# compare [0] to []

# [7, [10, 3, 3]] to [[7, 3], 7, 9, 2] 
# compare 7 to [7, 3]
# then compare [10, 3, 3] to 7 

# [7, [2, 3, 4]] to [3, 4, 5]
# compare 7 to [3, 4, 5]
# 
# more nesting needed?
def lists_in_order(l1, l2):
  l1 = convert_to_list(l1)
  l2 = convert_to_list(l2)
  for lsp, rsp in zip(l1,l2):
    ls = convert_to_list(lsp)
    rs = convert_to_list(rsp)
    if ls != []:
      while isinstance(ls[0], list):
        ls = ls[0]
        if ls == []:
          break
    if rs != []:
      while isinstance(rs[0], list):
        rs = rs[0]
        if rs == []:
          break
    if rs < ls:
      return False
    if ls < rs:
      return True
  if len(l1) > len(l2):
    return False
  else: 
    return True
def compare_nested_lists(nl1, nl2):
  for i, j in enumerate(nl1):
    while(check_if_nested(j)):
    lists_in_order(j, nl2[i])
    

for lsp, rsp in zip(lines[3], lines[4]):
  ls = convert_to_list(lsp)
  rs = convert_to_list(rsp)
  if check_if_nested(ls):
    lists_in_order_rec(ls, convert_to_list(rs))
  if check_if_nested(rs):
    lists_in_order_rec(convert_to_list(ls), rs)
  if rs < ls:
    False
  if ls < rs:
    True
    
# how do we compare [8, 1, 0] to [8, 8, [4, [6, 1], [6, 9, 8, 10, 10], 1, 0]]
# hm for 0 to [4, [6, 1]] etc
# just need to compare 0 to 4
