# flow rate (pressure per minute) tunnels between valve
# take you one minute to open a valve and one to follow tunnel from one valve to another
# most pressure you could release
# take remaining minutes times pressure 
# Valve AA starts open
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

# you don't need to open valve to move between
# could make a graph wth each node as pressure flow?
# with 30 minutes we can 
# you can either move or open a valve each minute
# you have 30 actions
# so you could open 15 at most
# you multiply flow rate times time remaining (at most one can be open 28 minutes)

# recursion? 

running_sum_l = set()
vr_o = []

def find_path_to_end(p_dict, cur_node, time_remaining, running_sum, valves_running=None):
  if valves_running is None:
    valves_running = defaultdict(str)
  if time_remaining == 0:
    running_sum_l.add(running_sum)
    vr_o.append(valves_running)
    return 
  next_nodes = p_dict[cur_node]['paths_to']
  frv = p_dict[cur_node]['flow_rate']
  # if flow rate is 0 or current valve is open, you move
  if frv == 0 or cur_node in valves_running.keys():
    for valve_to_open in next_nodes:
      time_remaining -= 1
      if time_remaining == 0:
        running_sum_l.add(running_sum)
        return 
      #passed_vr = copy.deepcopy(valves_running)
      find_path_to_end(p_dict, valve_to_open, time_remaining, running_sum, valves_running)
  else:
    for movement in ["move", "open"]:
      time_remaining -= 1
      if movement == "open":
        running_sum += frv * (time_remaining+1)
        valves_running[cur_node] = frv * (time_remaining+1)
        if time_remaining == 0:
          running_sum_l.add(running_sum)
          vr_o.append(valves_running)
          return 
        passed_vr = copy.deepcopy(valves_running)
        find_path_to_end(p_dict, cur_node, time_remaining, running_sum, passed_vr)
      if movement == "move":
        for valve_to_open in next_nodes:
          if time_remaining == 0:
            running_sum_l.add(running_sum)
            vr_o.append(valves_running)
            return 
          #passed_vr = copy.deepcopy(valves_running)
          find_path_to_end(p_dict, valve_to_open, time_remaining, running_sum, valves_running)
     
# should be 40   
find_path_to_end(p_dict = valve_and_paths, cur_node = 'AA', time_remaining = 30, running_sum = 0)
find_path_to_end(p_dict = valve_and_paths, cur_node = 'DD', time_remaining = 4, running_sum = 0)
max(running_sum_l)
# 222 is too low 
