days, total_hours = map(int, input().split())
min_time, max_time = [], []
for i in range(days):
  just = input()
  min_time.append(int(just.split(' ')[0]))
  max_time.append(int(just.split(' ')[1]))

  total_min = sum(min_time)
  total_max = sum(max_time)

if total_min <= total_hours <= total_max:
  print("YES")
  
  schedule = list(min_time)
  current_sum = total_min
  
  for i in range(days):
    if current_sum < total_hours:
      can_add = max_time[i] - min_time[i]
      to_add = min(can_add, total_hours - current_sum)
      
      schedule[i] += to_add
      current_sum += to_add
  
  print(*(schedule))
else:
  print("NO")