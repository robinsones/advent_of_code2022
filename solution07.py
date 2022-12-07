import re 
import copy 

def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

with open('input07.txt') as f:
  command_inputs = [l.strip() for l in f]

list_commands_index = [i for i, l in enumerate(command_inputs) if l == "$ ls"]

dir_contents = {}
dir_paths = [[] for i in range(len(list_commands_index))]

for i, v in enumerate(list_commands_index):
  if i == 0:
    next_index = list_commands_index[i+1]
    dir_contents["/"] = [c.replace("dir ", "//") for c in command_inputs[v+1:next_index-1]]
    dir_paths[i] = ["/"]
  else:
    prv_index = list_commands_index[i-1]
    prv_cds = [s.removeprefix("$ cd ") for s in command_inputs[prv_index+1:v] if s.startswith("$ cd ")]
    dir_paths[i] = copy.deepcopy(dir_paths[i-1])
    for p in prv_cds: 
      if p != "..":
        dir_paths[i].append(p)
      elif p == "..":
        dir_paths[i] = dir_paths[i][:-1]
    dir_name = '/'.join(dir_paths[i])
    if 0 < i < len(list_commands_index) - 1:
      next_index = list_commands_index[i+1]
      dir_ent = [c.replace("dir ", dir_name + "/") for c in command_inputs[v+1:next_index-1]]
      dir_contents[dir_name] = dir_ent
    elif i == len(list_commands_index) - 1:
      dir_name = '/'.join(dir_paths[i])
      dir_ent = [c.replace("dir ", dir_name + "/") for c in command_inputs[v+1:]]
      dir_contents[dir_name] = dir_ent

dict_within_dict = {}
for k, e in dir_contents.items():
  dict_within_dict[k] = [v for v in e if v.startswith("//")] + [int(re.findall(r'\d+', v)[0]) for v in e if re.findall(r'\d+', v) != []]

while not all(isinstance(value, int) for value in dict_within_dict.values()):
  for k, e in dict_within_dict.items(): 
    if not isinstance(e, int):
      dict_within_dict[k] = flatten([dict_within_dict[v] if not isinstance(v, int) else v for v in e])
      if all(isinstance(value, int) for value in dict_within_dict[k]):
        dict_within_dict[k] = sum(dict_within_dict[k])

sum([v for v in dict_within_dict.values() if v <= 100000])

# Problem 2

space_to_delete = 30000000 - (70000000 - dict_within_dict["/"])

min([v for v in dict_within_dict.values() if v > space_to_delete])
