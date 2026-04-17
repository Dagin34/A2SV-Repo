def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()

    left = 0
    right = n - 1
    
    for i in range(n - 1):
        if s[i] == 'L':
            left += 1
        else:
            right -= 1
            
    results = []
    current_product = a[left] % m
    results.append(current_product)
    
    ptr_l = left
    ptr_r = right
    
    for i in range(n - 2, -1, -1):
        if s[i] == 'L':
            ptr_l -= 1
            current_product = (current_product * a[ptr_l]) % m
        else:
            ptr_r += 1
            current_product = (current_product * a[ptr_r]) % m
        results.append(current_product)
        
    print(*(results[::-1]))

line = input().strip()
if line:
    test_cases = int(line)
    for _ in range(test_cases):
        solve()