class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        return [[matrix[i][j] for i in range(rows)] for j in range(cols)]