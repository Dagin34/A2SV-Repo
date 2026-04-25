import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        starts = sorted((intervals[i][0], i) for i in range(n))
        start_vals = [s[0] for s in starts]
        
        res = []
        
        for s, e in intervals:
            idx = bisect.bisect_left(start_vals, e)
            if idx < n:
                res.append(starts[idx][1])
            else:
                res.append(-1)
        
        return res