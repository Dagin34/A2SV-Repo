class Solution:
  def majorityElement(self, nums: list[int]) -> list[int]:
    # Initialize the dictionary
    counts = {}
    n = len(nums)
    threshold = n // 3
    
    # Build the dictionary
    for num in nums:
      if num in counts:
        counts[num] += 1
      else:
        counts[num] = 1
            
    result = []
    for num in counts:
      if counts[num] > threshold:
        result.append(num)
            
    return result

  print(majorityElement(None, [3,2,3]))
  # print(majorityElement([1]))
  # print(majorityElement([1,2]))