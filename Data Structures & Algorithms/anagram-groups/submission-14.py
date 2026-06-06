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

        # anagrams = {}

        # for s in strs:
        #     unscrambled = [0] * 26
        #     for i in s:
        #         unscrambled[ord('a') - ord(i)] += 1
        #     key = tuple(unscrambled)
        #     anagrams.setdefault(key, []).append(s)
        
        # return list(anagrams.values())