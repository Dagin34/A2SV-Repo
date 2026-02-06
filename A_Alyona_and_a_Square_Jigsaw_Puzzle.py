from cmath import sqrt

number_of_testcases = int(input())

for i in range(number_of_testcases):
    days = int(input())
    assembled = list(map(int, input().split(' ')))

    total, happy_days = 0, 0
    for j in assembled:
        total += j

        root = int(total ** 0.5)
        if root * root == total and root % 2 == 1:
            happy_days += 1

    print(happy_days)