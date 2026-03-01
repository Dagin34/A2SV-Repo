import sys
input = sys.stdin.read().split()
arr_size = int(input[0])
ops = int(input[1])
arr = list(map(int, input[2:]))

arr = [n for n in arr if n != 0]
arr.sort()

prev = 0
count = 0
i = 0

while i < arr_size and count < ops:
    if arr[i] != prev:
        print(arr[i] - prev)
        prev = arr[i]
        count += 1
    i += 1

while count < ops:
    print(0)
    count += 1



# arr_size = int(input[0])
# ops = int(input[1])
# arr = list(map(int, input[2:]))

# arr = sorted(list(set(n for n in arr if n != 0)))

# subs = 0
# count = 0

# for num in arr:
#     if count >= ops:
#         break

#     diff = num - subs
#     print(diff)

#     subs = num
#     count += 1

# while count < ops:
#     print(0)
#     count += 1


# arr_size, ops = map(int, input().split())
# arr = list(map(int, input().split()))
# arr = list(map(int, input().split()))

# for i in range(ops):
#     arr = [n for n in arr if n != 0]

#     if not arr:
#         print(0)
#         continue

#     min_value = min(arr)
#     min_index = arr.index(min(arr))

#     print(min_value)
#     arr = [n - min_value for n in arr]

#     arr[min_index] = 0

    