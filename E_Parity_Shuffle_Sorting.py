def solve():
    line1 = input().split()
    n = int(line1[0])
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    ops = []
    
    ops.append((1, n))
    if (a[0] + a[n-1]) % 2 == 0:
        a[0] = a[n-1]
    else:
        a[n-1] = a[0]
        
    for i in range(1, n - 1):
        if (a[0] + a[i]) % 2 != 0:
            ops.append((1, i + 1))
        else:
            ops.append((i + 1, n))
            
    print(len(ops))
    for l, r in ops:
        print(f"{l} {r}")

line = input().strip()
if line:
    test_cases = int(line)
    for _ in range(test_cases):
        solve()