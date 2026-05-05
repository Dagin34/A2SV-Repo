test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]

    fixed = [0] * (2 * n + 2)
    for left, right in times:
        if left == right:
            fixed[left] += 1
    
    preference = [0] * (2 * n + 2)
    for i in range(1, 2 * n + 2):
        preference[i] = preference[i - 1] + (1 if fixed[i] > 0 else 0)

    result = []
    for left, right in times:
        if left == right:
            result.append('1' if fixed[left] == 1 else '0')
        else:
            result.append('1' if (preference[right] - preference[left - 1] < (right - left + 1)) else '0')

    print("".join(result))