tests = int(input())

for _ in range(tests):
    m = int(input())
    h = list(map(int, input().split()))

    found = False
    for j in range(1, m - 1):
        if h[j-1] < h[j] and h[j] > h[j+1]:
            print('YES')
            print(f'{j} {j+1} {j+2}')
            found = True
            break
    if not found:
        print('NO')










# tests = int(input())

# for _ in range(tests):
#     m = int(input())
#     h = list(map(int, input().split()))
#     h = list(set(h))

#     if len(h) < 3:
#         print('NO')
#     else:
#         print('YES')
#         h = [str(i) for i in h]
#         print(' '.join(h[-3:]))