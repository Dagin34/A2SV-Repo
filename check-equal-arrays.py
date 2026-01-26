def check_if_arrays_are_equal(a: list, b: list):
  return True if sorted(a) == sorted(b) else False

a = [1, 2, 4, 6, 0]
b = [0, 1, 5, 2, 6]

print(check_if_arrays_are_equal(a, b))