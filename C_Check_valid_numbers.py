test_cases = int(input())

for _ in range(test_cases):
    n, m, p, q = map(int, input().split(' '))

    number_of_blocks = n // p
    remaining = n % p

    if remaining == 0:
        if m == number_of_blocks * q:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")

# print(3//2)