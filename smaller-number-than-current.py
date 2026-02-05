class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    sorted_nums = sorted(nums)

    smaller_counts = {}
    for index, num in enumerate(sorted_nums):
        if num not in smaller_counts:
            smaller_counts[num] = index
            
    result = [smaller_counts[num] for num in nums]
    return result