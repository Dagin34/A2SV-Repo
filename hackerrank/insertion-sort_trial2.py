def insertionSort1(n, arr):
    value = arr[-1]
    idx = n - 2
    
    while idx >= 0 and arr[idx] > value:
        arr[idx + 1] = arr[idx]
        print(*arr)
        idx -= 1
    
    arr[idx + 1] = value
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)