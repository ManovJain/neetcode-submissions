class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints) - k

        total = sum(cardPoints[right:])
        points = total

        while right < len(cardPoints):
            total += cardPoints[left]
            total -= cardPoints[right]

            points = max(points, total)
            left += 1
            right += 1

        return points

