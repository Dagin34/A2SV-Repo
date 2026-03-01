test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    minimum = float('inf')
    for i in range(len(arr) - 2):
        if arr[i + 2] - arr[i] < minimum:
            minimum = arr[i + 2] - arr[i]
            
    print(minimum)