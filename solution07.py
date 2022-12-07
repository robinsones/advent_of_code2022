import re 

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
for i, v in enumerate(list_commands_index):
  if i < len(list_commands_index) - 1:
    next_index = list_commands_index[i+1]
    dir_contents[command_inputs[v-1].removeprefix("$ cd ")] = command_inputs[v+1:next_index-1]
  else:
    dir_contents[command_inputs[v-1].removeprefix("$ cd ")] = command_inputs[v+1:]

dict_within_dict = {}
for k, e in dir_contents.items():
  dict_within_dict[k] = [v.removeprefix("dir ") for v in e if v.startswith("dir")] + [int(re.findall(r'\d+', v)[0]) for v in e if re.findall(r'\d+', v) != []]

while not all(isinstance(value, int) for value in dict_within_dict.values()):
  for k, e in dict_within_dict.items(): 
    if not isinstance(e, int):
      dict_within_dict[k] = flatten([dict_within_dict[v] if not isinstance(v, int) else v for v in e])
      if all(isinstance(value, int) for value in dict_within_dict[k]):
        dict_within_dict[k] = sum(dict_within_dict[k])

sum([v for v in dict_within_dict.values() if v <= 100000])

# debug
## FFFF DIRECTORIES HAVE THE SAME NAME

cd_commands = [(i, l.removeprefix("$ cd ")) for i, l in enumerate(command_inputs) if l.startswith("$ cd") and l != "$ cd .."]

command_dir = [x[1] for x in cd_commands]
