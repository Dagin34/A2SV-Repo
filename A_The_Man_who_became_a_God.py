number_of_testcases = int(input().strip())

for _ in range(number_of_testcases):
  number_of_villagers, numbber_of_groups = map(int, input().split())
  
  a = list(map(int, input().split()))
  
  diffs = []
  for i in range(number_of_villagers - 1):
    diffs.append(abs(a[i] - a[i+1]))
  
  diffs.sort()
  
  ans = sum(diffs[:number_of_villagers-numbber_of_groups])
  print(ans)