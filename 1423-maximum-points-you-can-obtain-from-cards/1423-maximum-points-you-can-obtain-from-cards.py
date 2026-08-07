class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints) : return sum(cardPoints)
        n = len(cardPoints)
        window = n - k
        total = sum(cardPoints)

        curr = sum(cardPoints[:window])
        minSum = curr

        for i in range(window, n):
            curr += cardPoints[i] - cardPoints[i - window]
            minSum = min(minSum, curr)

        return total - minSum

        



