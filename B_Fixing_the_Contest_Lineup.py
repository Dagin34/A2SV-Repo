tests = int(input())

for _ in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for k in range(n + 1):
        possible = True
        for i in range(k, n):
            if a[i - k] > b[i]:
                possible = False
                break
        
        if possible:
            print(k)
            break

# Failed
# tests = int(input())

# for _ in range(tests):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     ops = 0
#     for i in range(n):
#         if a[i] > b[i]:
#             a[i] = b[i]
#             ops += 1
    
#     print(ops // 2)

# Failed 
# tests = int(input())

# for _ in range(tests):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     left = right = 0
#     ops = 0

#     while left < n and right < n:
#         if a[left] <= a[right]:
#             left += 1
#         else:
#             ops += 1

#         right += 1
    
#     print(ops)