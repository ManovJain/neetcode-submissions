class Solution:
    def longestPalindrome(self, s: str) -> int:
        charMap = defaultdict(int)
        pal = 0

        for c in s:
            charMap[c] += 1
            if charMap[c] % 2 == 0:
                pal += 2
        
        return pal + (pal < len(s))
