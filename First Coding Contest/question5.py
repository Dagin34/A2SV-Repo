n = int(input()) 
bars = list(map(int, input().split()))
m = int(input()) 
coupons = list(map(int, input().split()))

bars.sort()
temp = [0] * (n + 1)

for i in range(n):
  temp[i+1] = temp[i] + bars[i]
  
ans = []
for i in coupons:
  ans.append(temp[n] - bars[n-i])

print(*ans)