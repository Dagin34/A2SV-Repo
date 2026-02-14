test_cases = int(input())

for _ in range(test_cases):
    number_of_elements = int(input())
    arr = list(map(int, input().split()))

    # 1 1 3 = +1 +0 +2 = 3

    # [2, 3, 3, 4, 4, 5, 8, 9, 9] = +2 +1 +0 +1 +0 +1 +3 +1 +0 = 9 shit

    # arr.sort()
    # print('sui = ', arr)
    # response = arr[0] if number_of_elements != 1 else 1

    # for i in range(1, number_of_elements):
    #     if arr[i] > arr[i-1]:
    #         response += arr[i] - arr[i-1]
    #         # print(" = ", arr[i])
    #         # print(" = ", arr[i-1])
    ditinct_nums = len(set(arr))
    print(2 * ditinct_nums - 1)

    # print(response)