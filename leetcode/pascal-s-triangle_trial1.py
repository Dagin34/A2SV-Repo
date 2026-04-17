class Solution:
    def generate(self, numRows: int) -> List[List[int]]:        
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows - 1)
        last_row = prev[-1]
        new_row = [1]
        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])
        new_row.append(1)
        
        prev.append(new_row)
        
        return prev