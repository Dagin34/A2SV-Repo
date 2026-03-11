class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[j]

        return pointer + 1
        