class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        response = []
        response.append(nums[0])
        for i in range(1, len(nums)):
            response.append(response[i-1] + nums[i])
        
        return response