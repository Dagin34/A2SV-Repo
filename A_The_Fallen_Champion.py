youssef_combat_count, youssef_total_time = map(int, input().split())

champions = int(input())
opps = []

for _ in range(champions):
    opps_combat_count, opps_total_time = map(int, input().split())
    opps.append((opps_combat_count, opps_total_time))

is_best = True
for count, time in opps:
    if (count > youssef_combat_count or (count == youssef_combat_count and time < youssef_total_time)):
        is_best = False
        break
    
if is_best:
    print("The Champion Saves the Accused")
else:
    print("The Fallen Champion")