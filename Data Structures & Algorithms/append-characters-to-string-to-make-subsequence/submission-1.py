class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPtr = tPtr = 0

        while sPtr < len(s) and tPtr < len(t):
            if t[tPtr] == s[sPtr]:
                tPtr += 1
            sPtr += 1
        
        return len(t) - tPtr