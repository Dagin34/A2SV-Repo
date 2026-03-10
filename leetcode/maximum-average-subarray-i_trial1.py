class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_avg = sum(nums[:k]) / k
        max_avg = window_avg

        for i in range(k, len(nums)):
            window_avg = ((window_avg * k) - nums[i-k] + nums[i]) / k
            max_avg = max(max_avg, window_avg)

        return max_avg