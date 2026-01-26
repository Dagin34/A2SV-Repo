def union_of_arrays(a: list, b: list):
  return list(set(set(a) | set(b)))

a = [1, 2, 3]
b = [4, 5, 6]

print(union_of_arrays(a, b))