class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = sorted([p[0] for p in points])
        
        max_width = 0
        for i in range(len(x_coords) - 1):
            width = x_coords[i+1] - x_coords[i]
            if width > max_width:
                max_width = width
                
        return max_width