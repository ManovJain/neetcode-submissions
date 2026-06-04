class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = []

        for c in s:
            if c.isalpha():
                cleanedS.append(c.lower())
            elif c.isdigit():
                cleanedS.append(c)
        
        print(cleanedS)
        left, right = 0, len(cleanedS) - 1

        while left <= right:
            if cleanedS[left] != cleanedS[right]:
                return False
            left += 1
            right -= 1

        return True
