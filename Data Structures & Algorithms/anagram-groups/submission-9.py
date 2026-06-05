class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        output = []

        for i in strs:
            unscrambled = "".join(sorted(i))
            # print(unscrambled)
            anagramMap.setdefault(unscrambled, []).append(i)
        
        for i in anagramMap:
            output.append(anagramMap[i])
        
        return output