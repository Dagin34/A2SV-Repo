from collections import Counter

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        total_boomerangs = 0
        
        for p1 in points:
            distances = Counter()
            
            for p2 in points:
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                d_squared = dx*dx + dy*dy
                
                distances[d_squared] += 1

            for count in distances.values():
                total_boomerangs += count * (count - 1)
                
        return total_boomerangs