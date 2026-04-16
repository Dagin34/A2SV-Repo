class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        
        def decode():
            result = ""
            num = 0
            while self.i < len(s):
                char = s[self.i]
                if char.isdigit():
                    num = num * 10 + int(char)
                
                elif char == '[':
                    self.i += 1
                    decoded = decode()
                    result += decoded * num
                    num = 0
    
                elif char == ']':
                    return result
                
                else:
                    result += char
                
                self.i += 1
            return result
        return decode()