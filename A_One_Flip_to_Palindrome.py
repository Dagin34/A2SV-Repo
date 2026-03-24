tests = int(input())

for _ in range(tests):
    n = int(input())
    s = list(input())

    missed = []
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            missed.append(i)
            
    if not missed:
        print("Yes")
        continue

    left = missed[0]
    right = n - missed[-1] - 1

    for i in range(left, right):
        s[i] = '1' if s[i] == '0' else '0'
    
    print("Yes" if s == s[::-1] else "No")


# Failed test case two
# tests = int(input())

# for _ in range(tests):
#     n = int(input())
#     s = list(input())

#     missed = []
#     for i in range(n // 2):
#         if s[i] != s[n - i - 1]:
#             missed.append(i)
            
#     if not missed:
#         print("Yes")
#         continue

#     left = missed[0]
#     right = n - missed[0] - 1

#     for i in range(left, right - 1):
#         s[i] = '1' if s[i] == '0' else '0'
    
#     print("Yes" if s == s[::-1] else "No")