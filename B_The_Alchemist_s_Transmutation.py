test_cases = int(input())

for _ in range(test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    target = int(input())

    if min(arr) <= target <= max(arr):
        print('YES')
    else:
        print('NO')