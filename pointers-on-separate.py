# Colliding Pointers

def isSorted(arr, arr2) -> list:
    left = 0
    right = 0

    result = []
    while left < len(arr) and right < len(arr2):
        if arr[left] <= arr2[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr2[right])
            right += 1

    while left < len(arr):
        result.append(arr[left])
        left += 1

    while right < len(arr2):
        result.append(arr2[right])
        right += 1

    return result

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(isSorted(arr, arr2))