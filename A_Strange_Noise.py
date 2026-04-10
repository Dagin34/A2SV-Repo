testcases = int(input())

for i in range(testcases):
    letters = int(input())
    s = input().strip().lower()

    if not s: print("NO")
    reduced = []
    if letters > 0:
        reduced.append(s[0])
        for i in range(1, letters):
            if s[i] != s[i-1]:
                reduced.append(s[i])
    
    result = ''.join(reduced)
    if result == 'meow': print("YES")
    else: print("NO")