test_cases = int(input())

for _ in range(test_cases):
    number_of_elements = int(input())
    arr = list(map(int, input().split()))

    # arr.sort()
    possible = True
    for i in range(number_of_elements):
        if arr[i] <= 2 * abs(number_of_elements - 1 - i): # Long shot
            possible = False
            break

    print('YES' if possible else 'NO')