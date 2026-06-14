class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bMap = defaultdict(int)

        for i in text:
            if i in "balloon":
                bMap[i] += 1
        
        if len(bMap) < 5:
            return 0

        bMap['l'] //= 2
        bMap['o'] //= 2

        return min(bMap.values())