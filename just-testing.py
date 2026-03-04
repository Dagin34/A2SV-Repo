# ===================================== BREAKER =====================================
# def thirdMax(nums: list[int]) -> int:
#     nums = list(set(nums))
#     nums.sort(reverse=True)
#     if len(nums) < 3:
#         return nums[0]
#     else:
#         return nums[2]
    
# print(thirdMax([1,2]))
# print(thirdMax([3,2,1]))

# ===================================== BREAKER =====================================
# def smallestNumber(num: int) -> int:
#     if num > 0:
#         digits = list(map(int, str(num)))
#         digits.sort()
#     else:
#         digits = list(map(int, str(abs(num))))
#         digits.sort(reverse=True)

#     if len(digits) > 2 and digits[0] == 0 and num > 0:
#         checker = 1
#         while digits[checker] == 0:
#             checker += 1

#         digits[0], digits[checker] = digits[checker], digits[0]

#     return int(''.join(str(d) for d in digits)) if num > 0 else 0 - int(''.join(str(d) for d in digits))

# print(smallestNumber(310))
# print(smallestNumber(-7605))
# print(smallestNumber(95005))

# ===================================== BREAKER =====================================
def frequencySort(s: str) -> str:
    counter = {}
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    
    counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    result = [char*count for char, count in counter.items()]
    return ''.join(result)

print(frequencySort('tree'))