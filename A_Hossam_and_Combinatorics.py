t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mn = min(arr)
    mx = max(arr)
    
    if mn == mx:
        print(n * (n - 1))
    else:
        count_min = arr.count(mn)
        count_max = arr.count(mx)
        print(2 * count_min * count_max)