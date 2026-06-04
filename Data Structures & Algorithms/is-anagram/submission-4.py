class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False


        alphaArr = [0] * 26

        for i in range(len(s)):
            sIndex = ord('a') - ord(s[i])
            tIndex = ord('a') - ord(t[i])

            alphaArr[sIndex] += 1
            alphaArr[tIndex] -= 1
        
        for i in alphaArr:
            if i != 0:
                return False
        
        return True