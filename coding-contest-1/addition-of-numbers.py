number_of_testcases = int(input())
test_cases = []
for _ in range(number_of_testcases):
  test_cases.append(input())

for value in test_cases:
  value = value.strip('')
  num1 = int(value[0])
  num2 = int(value[2])
  print(num1 + num2)