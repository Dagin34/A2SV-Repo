from collections import Counter

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    counts = Counter(arr)
    amazing_detective_slash_genius = False 

    for i in counts:
        if counts[i] % 2 != 0:
            amazing_detective_slash_genius = True
            break
    
    print("YES" if amazing_detective_slash_genius else "NO")