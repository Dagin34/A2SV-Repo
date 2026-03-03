# Holder and Seeker

def isSorted(arr) -> list:
    holder = 0
    seeker = 0

    while seeker < len(arr):
        if arr[seeker] != 0:
            arr[holder], arr[seeker] = arr[seeker], arr[holder]
            holder += 1
        seeker += 1

    return arr

arr = list(map(int, input().split()))
print(isSorted(arr))