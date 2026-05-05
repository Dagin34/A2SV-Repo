class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        def compute(d):
            return sum((num + d - 1) // d for num in nums)
        
        while left <= right:
            mid = (left + right) // 2
            
            if compute(mid) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        
        return left