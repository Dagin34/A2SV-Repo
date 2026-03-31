from collections import defaultdict
import sys
input = sys.stdin.readline

test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))
    
    groups = defaultdict(list)    
    for i in range(n):
        groups[u[i]].append(s[i])
    
    answer = [0] * (n + 1)
    for g in groups.values():
        g.sort(reverse=True)
        
        prefix = [0]
        for x in g:
            prefix.append(prefix[-1] + x)
        
        m = len(g)
        for k in range(1, m + 1):
            usable = (m // k) * k
            if usable > 0:
                answer[k] += prefix[usable]
    
    print(*answer[1:])