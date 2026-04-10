import math
testcases = int(input())

for i in range(testcases):
    n = int(input())
    a = list(map(int, input().split(' ')))

    v = abs(a[0])
    target_small = math.ceil(n/2) - 1

    smaller = larger = 0
    for i in range(1, n):
        if abs(a[i]) < v: smaller += 1
        else: larger += 1
    
    positive = (smaller <= target_small <= smaller + larger)
    negative = (0 <= target_small <= larger)

    if positive or negative: print("YES")
    else: print("NO")