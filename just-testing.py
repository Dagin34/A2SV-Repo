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
# def frequencySort(s: str) -> str:
#     counter = {}
#     for char in s:
#         if char in counter:
#             counter[char] += 1
#         else:
#             counter[char] = 1
    
#     counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
#     result = [char*count for char, count in counter.items()]
#     return ''.join(result)

# print(frequencySort('tree'))

# ===================================== BREAKER =====================================
# from collections import Counter

# def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
#     results = []
#     left, right = 0, 0
#     count = Counter(arr1)
#     print(count)
    
#     while left < len(arr2) and right < len(arr1):
#         if arr2[left] != arr1[right]:
#             right += 1
#         else:
#             # results.extend(arr1[right] * count.get(arr1[right]))
#             right = 0
#             left += 1
    
#     return results

# print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))

# ===================================== BREAKER =====================================
# def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
#     x_coords = sorted([p[0] for p in points])
    
#     max_width = 0
#     for i in range(len(x_coords) - 1):
#         width = x_coords[i+1] - x_coords[i]
#         if width > max_width:
#             max_width = width
            
#     return max_width
# list = [[8,7],[9,9],[7,4],[9,7]]
# print(maxWidthOfVerticalArea(list))
# list = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# print(maxWidthOfVerticalArea(list))
# list = [[1,5],[1,70],[3,1000],[55,700],[999876789,53],[987853567,12]]
# print(maxWidthOfVerticalArea(list))

# ===================================== BREAKER =====================================
# def appendCharacters(s: str, t: str) -> int:
#     left, right = 0, 0
#     while left < len(s) and right < len(t):
#         if s[left] == t[right]:
#             right += 1
#         left += 1
    
#     return len(t) - right

# print(appendCharacters(s = "coaching", t = "coding"))
# print(appendCharacters(s = "abcde", t = "a"))
# print(appendCharacters(s = "z", t = "abcde"))

# ===================================== BREAKER =====================================
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()

        left = 0
        right = 0
        matches = 0

        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                matches += 1
                left += 1
                right += 1
            else:
                right += 1

        return matches
    
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        result = [-1] * len(nums)
        
        if k == 0:
            return nums
        
        window = 2 * k + 1
        if window > len(nums):
            return result
        
        s = sum(nums[:window])
        result[k] = s // window
        
        for i in range(window, len(nums)):
            s += nums[i] - nums[i - window]
            result[i - k] = s // window
        
        return result
    
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        
        result = white
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W':
                white -= 1
            
            if white < result:
                result = white
        
        return result