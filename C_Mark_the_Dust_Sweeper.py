def solve():
    n_str = input().strip()
    n = int(n_str)
    a = list(map(int, input().split()))

    first_nonzero = -1
    for i in range(n - 1):
        if a[i] > 0:
            first_nonzero = i
            break
            
    if first_nonzero == -1:
        print(0)
        return
    
    ans = 0
    for i in range(first_nonzero, n - 1):
        if a[i] == 0:
            ans += 1
        else:
            ans += a[i]
            
    print(ans)

line = input().strip()
if line:
    test_cases = int(line)
    for _ in range(test_cases):
        solve()