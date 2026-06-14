class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bMap = defaultdict(int)
        word = "balloon"
        wordSet = set(word)

        for i in text:
            if i in word:
                bMap[i] += 1
        
        if len(bMap) < len(wordSet):
            return 0

        bMap['l'] //= 2
        bMap['o'] //= 2

        return min(bMap.values())