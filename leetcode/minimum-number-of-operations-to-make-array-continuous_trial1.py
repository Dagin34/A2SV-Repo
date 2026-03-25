class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        result = n
        i = 0
        
        for j in range(len(nums)):
            while nums[j] - nums[i] > n - 1:
                i += 1
            
            window_size = j - i + 1
            result = min(result, n - window_size)
        
        return result