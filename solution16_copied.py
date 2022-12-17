import re 
from collections import defaultdict
import copy

valve_and_paths = defaultdict(str)

with open('input16.txt') as f:
  for l in f: 
    cur_valve = l.split(" has flow", 1)[0].split('Valve ', 1)[1]
    fr = [int(i) for i in re.findall("\\d+", l)]
    if "valves" in l:
      pt = [i.strip() for i in l.strip().split("lead to valves ",1)[1].split(',')]
    else:
      pt = [i.strip() for i in l.strip().split("leads to valve ",1)[1].split(',')]
    valve_and_paths[cur_valve] = {'flow_rate': fr[0], 'paths_to': pt}

# what did i learn
def task1(p_dict, start, limit):
  
  @cache
  def dfs(valve, time, visited):
      if time <= 1:
          return 0
      res = 0
      for link in p_dict[valve]['paths_to']:
          res = max(res, dfs(link, time - 1, visited))
      if valve not in visited and p_dict[valve]['flow_rate'] > 0:
          visited = tuple(sorted([*visited, valve]))
          res = max(res, dfs(valve, time - 1, visited) + p_dict[valve]['flow_rate'] * (time - 1))
      return res
    
  return dfs(start, limit, ())

task1(valve_and_paths, 'AA', 30)
