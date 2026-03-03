# Colliding Pointers

# def isSorted(arr, target) -> list:
#     left = 0
#     right = len(arr) - 1

#     while left < len(arr) and right > 0:
#         if arr[left] + arr[right] == target:
#             return arr[left], arr[right]
#         elif arr[left] + arr[right] > target:
#             right -= 1
#         else:
#             left += 1

#     return 0, 0

# arr = list(map(int, input().split()))
# target = int(input())
# print('Its', ' + '.join(str(num) for num in isSorted(arr, target)), 'you bum')

# Better solution

def isSorted(arr, target) -> list:
    left = 0
    right = len(arr) - 1

    while arr[left] + arr[right] != target:
        if arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1

    return left + 1, right + 1

arr = list(map(int, input().split()))
target = int(input())
print('Its', ' + '.join(str(num) for num in isSorted(arr, target)), 'you bum')