size1, size2 = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

left = 0
right = 0

result = []
while left < size1 and right < size2:
    if arr[left] <= arr2[right]:
        result.append(arr[left])
        left += 1
    else:
        result.append(arr2[right])
        right += 1

result.extend(arr[left:])
result.extend(arr2[right:])

print(' '.join(str(num) for num in result))