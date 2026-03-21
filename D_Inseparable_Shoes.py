test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    s = list(map(int, input().split()))
    
    response = [0] * n
    i = 0
    posisble = True
    
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        if j - i == 1:
            posisble = False
            break
        
        for k in range(i, j - 1):
            response[k] = k + 2
        response[j - 1] = i + 1
        
        i = j
    
    if not posisble:
        print(-1)
    else:
        print(*response)