import sys
input = sys.stdin.readline

test_cases = int(input())
for _ in range(test_cases):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    
    b.sort()
    a11 = b[0]
    expected = []
    
    for i in range(n):
        for j in range(n):
            expected.append(a11 + i * c + j * d)
    
    expected.sort()
    print("YES" if expected == b else "NO")