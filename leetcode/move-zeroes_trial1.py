class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        holder = 0
        seeker = 1

        while seeker < len(nums):
            if nums[holder] == 0 and nums[seeker] != 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
            if nums[holder] != 0:
                holder += 1
            seeker += 1