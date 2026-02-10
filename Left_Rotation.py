list_size, rotation = map(int, input().split())
arr = list(map(int, input().split()))

left = arr[rotation:]
left.extend(arr[:rotation])
print(left)