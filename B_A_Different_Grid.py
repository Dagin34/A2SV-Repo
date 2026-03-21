test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.extend(map(int, input().split()))
    
    if n * m == 1:
        print(-1)
        continue
    
    b = grid[1:] + [grid[0]]
    
    idx = 0
    for i in range(n):
        print(*b[idx:idx+m])
        idx += m