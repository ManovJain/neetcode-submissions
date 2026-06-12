class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        occurances = defaultdict(int)
        oddFound = False

        for c in s:
            occurances[c] += 1
        
        for char in occurances:
            if occurances[char] % 2 == 1:
                if oddFound == True:
                    return False
                else:
                    oddFound = True
        
        return True