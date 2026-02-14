test_cases = int(input())

for _ in range(test_cases):
    number_of_elements = int(input())
    arr = list(map(int, input().split()))

    if sum(arr) % len(arr) != 0:
        # Dubs
        print(-1)
        continue

    k = 0
    avg = sum(arr) / len(arr) if arr != 0 else -1
    for i in range(number_of_elements):
        if arr[i] > avg:
            k += 1

    print(k)