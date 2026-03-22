class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = len(blocks)
        white = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        
        result = white
        for i in range(k, count):
            if blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W':
                white -= 1
            
            if white < result:
                result = white
        
        return result