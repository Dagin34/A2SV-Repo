test_cases = int(input())

def calculate_values(arr):
    current_max, total_sum = 0, 0
    for x in arr:
        if x > current_max:
            current_max = x
        total_sum += current_max
    return total_sum

for _ in range(test_cases):
    n = int(input().strip())
    a = list(map(int, input().split()))

    max_val = calculate_values(a)

    for i in range(n):
        for j in range(i + 1, n):
            a[i], a[j] = a[j], a[i]

            val = calculate_values(a)
            if val > max_val:
                max_val = val
            
            a[i], a[j] = a[j], a[i]
    
    print(max_val)