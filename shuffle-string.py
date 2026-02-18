class Solution:
    def restoreString(s: str, indices: list[int]) -> str:
        final = ''
        for i in range(max(indices) + 1):
            final += s[indices.index(i)]
        
        return final