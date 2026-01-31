t = int(input())

for _ in range(t):
  nums = list(map(int, input().split()))
  
  for _ in range(5):
    nums.sort()
    nums[0] += 1
      
  a, b, c = nums
  print(a * b * c)