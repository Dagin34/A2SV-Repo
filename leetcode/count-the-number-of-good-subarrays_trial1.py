class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left, pairs, result, n = 0, 0, 0, len(nums)

        for right in range(n):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while pairs >= k:
                result += (n - right)
                
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return result