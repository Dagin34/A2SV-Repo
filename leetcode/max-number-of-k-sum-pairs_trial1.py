from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operations = 0

        for num in list(count.keys()):
            complement = k - num

            if complement not in count:
                continue

            if num == complement:
                operations += count[num] // 2
            else:
                pairs = min(count[num], count[complement])
                operations += pairs

            count[num] = 0
            count[complement] = 0

        return operations