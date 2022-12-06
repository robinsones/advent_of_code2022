with open('input06.txt') as f: 
  line = f.read().rstrip()

for i in range(4, len(line)): 
  previous_four = elves_str[i-4:i]
  if len(set(previous_four)) == 4: 
    print(i)
    break

for i in range(14, len(line)): 
  previous_fourteen = elves_str[i-14:i]
  if len(set(previous_fourteen)) == 14: 
    print(i)
    break
