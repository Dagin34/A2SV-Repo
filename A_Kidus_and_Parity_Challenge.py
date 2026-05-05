test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))

    evens, odds = 0, 0
    for x in a:
        if x % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    print(min(evens, odds))