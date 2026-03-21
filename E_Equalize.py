t = int(input())
for _ in range(t):
    line = input().split()
    n = int(line[0])
    a = list(map(int, input().split()))

    unique_a = sorted(list(set(a)))
    m = len(unique_a)
    
    max_count = 0
    right = 0
    
    for left in range(m):
        while right < m and unique_a[right] - unique_a[left] < n:
            right += 1
        
        current_window_size = right - left
        if current_window_size > max_count:
            max_count = current_window_size
            
    print(max_count)