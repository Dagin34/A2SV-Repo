class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        outside_len, single_len = len(mat), len(mat[0])
        result = []
        
        for item in range(outside_len + single_len - 1):
            mid = []
            
            row = 0 if item < single_len else item - single_len + 1
            col = item if item < single_len else single_len - 1
            
            while row < outside_len and col >= 0:
                mid.append(mat[row][col])
                row += 1
                col -= 1
            
            if item % 2 == 0:
                mid.reverse()
            
            result.extend(mid)
        
        return result