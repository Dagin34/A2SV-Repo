class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = 0
        pairs = 0
        result = 1
        for r in range(1, len(s)):
            if s[r] == s[r - 1]:
                pairs += 1
            
            while pairs > 1:
                if s[l] == s[l + 1]:
                    pairs -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result