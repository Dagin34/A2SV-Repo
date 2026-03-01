class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        total = 0
        
        for col in zip(*nums):
            total += max(col)
        
        return total