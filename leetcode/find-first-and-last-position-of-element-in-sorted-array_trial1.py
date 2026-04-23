class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            low, high = 0, len(nums) - 1
            result = -1
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if nums[mid] == target:
                    result = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return result
        
        def findRight():
            low, high = 0, len(nums) - 1
            result = -1
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if nums[mid] == target:
                    result = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return result
        
        return [findLeft(), findRight()]