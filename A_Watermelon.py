weight, is_divisible_by_even = int(input()), False
for i in range(2, weight, 2):
  if weight % i == 0:
    is_divisible_by_even = True

print('YES' if is_divisible_by_even else 'NO')