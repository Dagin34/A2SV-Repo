class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0: -1}
        curr_sum = 0
        
        for i, num in enumerate(nums):
            curr_sum += num
            if k != 0:
                curr_sum %= k
            
            if curr_sum in map:
                if i - map[curr_sum] >= 2:
                    return True
            else:
                map[curr_sum] = i
        
        return False