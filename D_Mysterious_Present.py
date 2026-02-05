line1 = input().split()
if not line1: exit()
n, cw, ch = int(line1[0]), int(line1[1]), int(line1[2])

valid = []
for i in range(1, n + 1):
    w, h = map(int, input().split())
    if w > cw and h > ch:
        valid.append((w, h, i))

if not valid:
    print(0)
    exit()

valid.sort()

m = len(valid)
dp = [1] * m
parent = [-1] * m

for i in range(m):
    wi, hi, _ = valid[i]
    for j in range(i):
        wj, hj, _ = valid[j]
        if wi > wj and hi > hj:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

max_len = 0
best_idx = -1
for i in range(m):
    if dp[i] > max_len:
        max_len = dp[i]
        best_idx = i

path = []
curr = best_idx
while curr != -1:
    path.append(str(valid[curr][2]))
    curr = parent[curr]

print(max_len)
print(" ".join(path[::-1]))