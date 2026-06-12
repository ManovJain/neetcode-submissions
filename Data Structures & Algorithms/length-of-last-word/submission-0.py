class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastLen = 0
        letterFound = False
        n = len(s) - 1

        while n > -1:
            if letterFound == False and s[n] == " ":
                n -= 1
            if s[n].isalpha():
                letterFound = True
                lastLen += 1
                n -= 1
            if letterFound == True and s[n] == " ":
                return lastLen
        
        return lastLen

        
