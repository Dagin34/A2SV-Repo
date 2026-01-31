amount = int(input())

test_cases = []
for _ in range(amount):
  test_cases.append(input().strip())

for word in test_cases:
  length = len(word)
  
  if length > 10:
    print(f"{word[0]}{length - 2}{word[-1]}")
  else:
    print(word)