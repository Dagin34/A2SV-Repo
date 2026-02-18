class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        final = ''.join([s[indices.index(i)] for i in range(max(indices) + 1)])
        
        return final