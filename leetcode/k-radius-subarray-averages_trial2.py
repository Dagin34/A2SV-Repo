class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
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