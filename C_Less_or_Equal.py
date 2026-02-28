n, k = map(int, input().split())
arr = list(map(int, input().split()))

goal = 0
max_number = 0
for num in arr:
    if num <= max_number:
        goal += 1

# not done yet

# while k != goal: