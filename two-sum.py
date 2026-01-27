class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    # { number: index }
    dict_for_response = {}
    
    for i, n in enumerate(nums):
      diff = target - n
        
      if diff in dict_for_response:
        return [dict_for_response[diff], i]
        
      # If not found, add the current number to the sheet
      dict_for_response[n] = i

    return dict_for_response