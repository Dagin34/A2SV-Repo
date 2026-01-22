amount = int(input())
test_cases = []
for _ in range(amount):
  test_cases.append(int(input()))

for n in test_cases:
  count = 0
  for a in range(n):
    for b in range(n):
      if a == n - b:
        count += 1
  print(count)