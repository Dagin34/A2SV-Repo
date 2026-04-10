size = int(input())
a = list(map(int, input().split()))
double = a + a

max_rest = current_rest = 0
for hour in double:
    if hour == 1:
        current_rest += 1
        if current_rest > max_rest:
            max_rest = current_rest
    else:
        current_rest = 0

print(max_rest)