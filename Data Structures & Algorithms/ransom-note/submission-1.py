class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        wordBank = [0] * 26
        
        for i in magazine:
            wordBank[ord('a') - ord(i)] += 1
        
        for i in ransomNote:
            letter = ord('a') - ord(i)
            wordBank[letter] -= 1
            if wordBank[letter] < 0:
                return False
            
        return True