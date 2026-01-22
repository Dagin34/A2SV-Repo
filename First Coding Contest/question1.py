amount = int(input())
test_cases = []
for _ in range(amount):
  test_cases.append(str(input()))

for i in test_cases:
  a, b = i.split(' ')
  if a and b:
    print(f"{b[0] + a[1:]} {a[0] + b[1:]}")