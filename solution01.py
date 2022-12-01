with open('input01.txt') as f:
    lines = f.readlines()

### Problem 1
calories = 0 
total_calories = []
for i in lines:
  if i.startswith("\n"):
    total_calories.append(calories)
    calories = 0
  else:
    calories += int(i.replace("\n", ""))

max(total_calories)

### Problem 2
total_calories.sort()
sum(total_calories[-3:])

