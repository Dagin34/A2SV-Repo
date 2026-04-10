class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        counter = Counter()
        left = 0
        min_heap = []
        max_heap = []
        max_length = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)

            while max_heap and min_heap and (-max_heap[0] - min_heap[0] > limit):
                num = nums[left]
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]
                
                while max_heap and counter[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                while min_heap and counter[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length