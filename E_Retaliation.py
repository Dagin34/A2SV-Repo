test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    
    possible = True
    if n > 1:
        difference = a[1] - a[0]
        for i in range(1, n - 1):
            if a[i+1] - a[i] != difference:
                possible = False
                break
    
    if not possible:
        print('NO')
        continue

    k = a[1] - a[0]
    number = a[0] - k
    den = n + 1

    if number >= 0 and number % den == 0:
        y = number // den
        x = y + k
        if x >= 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')