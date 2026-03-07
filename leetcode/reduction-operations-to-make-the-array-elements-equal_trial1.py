class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        total_operations = 0
        current_step_cost = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                current_step_cost += 1
            
            total_operations += current_step_cost
                
        return total_operations