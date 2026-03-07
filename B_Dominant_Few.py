# test_cases = int(input())
# for _ in range(test_cases):
#     num = int(input())
#     folks = list(map(int, input().split()))

#     folks.sort()
#     left, right = 0, num - 1

#     elite_sum, crowd_sum, elite_count, crowd_count = 0, 0, 0, 0
#     while left <= right:
#         crowd_count += 1
#         crowd_sum += folks[left]

#         if left != right:
#             elite_sum += folks[right]
#             elite_count += 1
#             right -= 1
#         left += 1

#     if elite_sum > crowd_sum and elite_count < crowd_count:
#         print('YES')
#     else:
#         print('NO')

test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    folks = list(map(int, input().split()))

    folks.sort(reverse=True)
    sums = [0] * (num + 1)
    for i in range(num):
        sums[i + 1] = sums[i] + folks[i]

    possible = False
    limit = (num // 2) + 1

    for k in range(1, limit):
        if 2 * k + 1 > num:
            break
            
        sum_elite = sums[k]
        sum_crowd = sums[2 * k + 1] - sums[k]

        if sum_elite > sum_crowd:
            possible = True
            break
    
    print('YES' if possible else 'NO')