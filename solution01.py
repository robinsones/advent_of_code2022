with open('input01.txt') as f:
    lines = [l.rstrip("\n") for l in f]

### Problem 1
calories = 0 
total_calories = []
for i in lines:
  if i == '':
    total_calories.append(calories)
    calories = 0
  else:
    calories += int(i)

max(total_calories)

### Problem 2
total_calories.sort()
sum(total_calories[-3:])
