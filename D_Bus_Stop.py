n, m = map(int, input().split())
a = list(map(int, input().split()))

buses_needed = 1
current_bus_load = 0

for group_size in a:
    if current_bus_load + group_size <= m:
        current_bus_load += group_size
    else:
        buses_needed += 1
        current_bus_load = group_size
        
print(buses_needed)