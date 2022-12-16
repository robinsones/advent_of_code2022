import re 
from collections import defaultdict
import copy

valve_and_paths = defaultdict(str)

with open('ex_input16.txt') as f:
  for l in f: 
    cur_valve = l.split(" has flow", 1)[0].split('Valve ', 1)[1]
    fr = [int(i) for i in re.findall("\\d+", l)]
    if "valves" in l:
      pt = [i.strip() for i in l.strip().split("lead to valves ",1)[1].split(',')]
    else:
      pt = [i.strip() for i in l.strip().split("leads to valve ",1)[1].split(',')]
    valve_and_paths[cur_valve] = {'flow_rate': fr[0], 'paths_to': pt}

def find_path_to_endm(p_dict, cur_node, time_remaining, running_sum, cur_m, valves_running):
  if time_remaining <= 1:
    return max(running_sum, cur_m)
  next_nodes = p_dict[cur_node]['paths_to']
  frv = p_dict[cur_node]['flow_rate']
  # if flow rate is 0 or current valve is open, you move
  if frv == 0 or cur_node in valves_running:
    for valve_to_open in next_nodes:
      time_remaining -= 1
      return find_path_to_endm(p_dict, valve_to_open, time_remaining, running_sum, cur_m, valves_running)
  else:
    time_remaining -= 1
    running_sum += frv * (time_remaining)
    valves_running.append(cur_node)
    passed_vr = copy.deepcopy(valves_running)
    return find_path_to_endm(p_dict, cur_node, time_remaining, running_sum, cur_m, passed_vr)
    for valve_to_open in next_nodes:
      return find_path_to_endm(p_dict, valve_to_open, time_remaining, running_sum, cur_m, valves_running)

# this is right
find_path_to_endm(p_dict = valve_and_paths, cur_node = 'DD', time_remaining = 3, running_sum = 0, cur_m = 0, valves_running = [])

# this should be 93 but is 84
find_path_to_endm(p_dict = valve_and_paths, cur_node = 'AA', time_remaining = 6, running_sum = 0, cur_m = 0, valves_running = [])
