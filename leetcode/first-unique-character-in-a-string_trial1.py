class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx, char in enumerate(s):
            if char not in s[:idx] + s[idx+1:]:
                return idx
        return -1