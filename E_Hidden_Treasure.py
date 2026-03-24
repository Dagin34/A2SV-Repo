n, m = map(int, input().split())
left_bound = 1
right_bound = n

for _ in range(m):
    clue = input().strip()
    parts = clue.split()
    i = int(parts[-1])

    if 'left' in clue:
        right_bound = min(right_bound, i - 1)
    else:
        left_bound = max(left_bound, i + 1)
    
if left_bound > right_bound:
    print(-1)
else:
    print(right_bound - left_bound + 1)