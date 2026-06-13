class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd = 0
        minEven = 100

        count = Counter(s)

        for cnt in count.values():
            if cnt % 2 == 0:
                minEven = min(minEven, cnt)
            else:
                maxOdd = max(maxOdd, cnt)
        
        return maxOdd - minEven
