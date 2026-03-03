# For while combo

size1, size2 = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

left = 0
right = 0
results = []

for i in range(size2):
    while left < size1 and arr[left] < arr2[i]:
        left += 1

    results.append(left)

print(' '.join(str(num) for num in results))