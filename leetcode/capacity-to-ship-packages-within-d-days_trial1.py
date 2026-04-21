class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            d = 1
            current = 0
            
            for w in weights:
                if current + w > cap:
                    d += 1
                    current = 0
                current += w
            
            return d <= days
        
        left, right = max(weights), sum(weights)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            
            if can_ship(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer