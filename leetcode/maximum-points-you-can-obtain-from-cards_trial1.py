class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window = n - k

        if window == 0:
            return sum(cardPoints)

        total = sum(cardPoints)
        curr = sum(cardPoints[:window])
        min_sum = curr

        for i in range(window, n):
            curr += cardPoints[i]
            curr -= cardPoints[i - window]
            min_sum = min(min_sum, curr)

        return total - min_sum