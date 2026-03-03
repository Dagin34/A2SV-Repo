# Parallel Pointers

def isSorted(arr) -> bool:
    left, right = 0, 1
    while right < len(arr):
        if arr[left] > arr[right]:
            return False
        
        left += 1
        right += 1
    
    return True

arr = list(map(int, input().split()))
print(isSorted(arr))