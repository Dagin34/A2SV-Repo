import itertools

n = int(input())
a = str(input().strip())

colors = ['R', 'G', 'B']
patterns = list(itertools.permutations(colors))

min_recolors = float('inf')
best_garland = ''

for p in patterns:
    current_recolors = 0
    current_garland = []

    for i in range(n):
        target_color = p[i % 3]
        current_garland.append(target_color)
        if a[i] != target_color:
            current_recolors += 1
    
    if current_recolors < min_recolors:
        min_recolors = current_recolors
        best_garland = current_garland

print(min_recolors)
print(''.join(best_garland))