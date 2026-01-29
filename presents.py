# Number of testcases
n = int(input())
p = list(map(int, input().split()))

# List with size n
ans = [0] * n

for i in range(n):
  giver = p[i]
  
  ans[giver - 1] = i + 1
    
print(*(ans))