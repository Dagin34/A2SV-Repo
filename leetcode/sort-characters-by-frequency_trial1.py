class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        result = [char*count for char, count in counter.items()]
        return ''.join(result)