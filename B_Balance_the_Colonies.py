test_cases = int(input())

for _ in range(test_cases):
    participants = int(input())
    if participants <= 3:
        print(participants)
    else:
        print(participants % 2)