class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_needed = 0
        target = tickets[k]
        
        for i, t in enumerate(tickets):
            if i <= k:
                time_needed += min(t, target)
            else:
                time_needed += min(t, target - 1)
        
        return time_needed