test_cases = int(input())

for _ in range(test_cases):
    n, k = map(int, input().split())
    s = input()

    if n == 1:
        print('NO')
    elif s < s[::-1]:
        print('YES')
    elif k == 0 or len(set(s)) == 1:
        print('NO')
    else:
        print('YES')