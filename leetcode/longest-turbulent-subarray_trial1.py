class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        left = 0
        result = 1
        def cmp(a, b):
            if a > b: return 1
            if a < b: return -1
            return 0

        for right in range(1, n):
            c = cmp(arr[right - 1], arr[right])
            if c == 0:
                left = right
            elif right == n - 1 or c * cmp(arr[right], arr[right + 1]) != -1:
                result = max(result, right - left + 1)
                left = right

        return result