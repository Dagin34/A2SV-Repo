from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        remaining = []
        for num, freq in count.items():
            remaining.extend([num] * freq)

        result.extend(sorted(remaining))
        return result