class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
    
        prefix = ""
        i = 0

        while i < len(strs[0]):
            letter = strs[0][i]
            print(letter)
            for s in strs[1:]:
                if s[i] != letter:
                    return prefix
            prefix += strs[0][i]
            i += 1
        
        return prefix