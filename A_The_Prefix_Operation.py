test_cases = int(input().strip())
for _ in range(test_cases):
    n, k = map(int, input().strip().split())
    s = input().strip()
    
    current_b = s.count('B')
    
    if current_b == k:
        print(0)
        
    else:
        print(1)
        suffix_b = current_b
        
        for i in range(1, n + 1):
            if s[i - 1] == 'B':
                suffix_b -= 1
            
            if current_b < k:
                if i + suffix_b == k:
                    print(f"{i} B")
                    break
                    
            else:
                if suffix_b == k:
                    print(f"{i} A")
                    break