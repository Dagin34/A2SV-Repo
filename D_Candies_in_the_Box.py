import math

n, k = map(int, input().split())

inside = 9 + 8 * (n + k)
sqrt_ans = int(math.sqrt(inside))

a = (-3 + sqrt_ans) // 2
e = n - a

print(e)