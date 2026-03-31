import sys
input = sys.stdin.readline

test_cases = int(input())
for _ in range(test_cases):
    n, k = map(int, input().split())
    s = input().strip()
    
    last = -10**9
    answer = 0
    
    for i in range(n):
        if s[i] == '1':
            if i - last >= k:
                answer += 1
            last = i
    
    print(answer)