n = int(input())
a = list(map(int, input().split()))

a.sort()

current_day = 1
for contest_size in a:
    if contest_size >= current_day:
        current_day += 1
        
print(current_day - 1)