class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        anagrams = defaultdict(list)

        for string in strs:
            anagramArr = [0] * 26
            for character in string:
                anagramArr[ord(character) - ord('a')] += 1
            anagrams[tuple(anagramArr)].append(string)
        
        for group in anagrams:
            groups.append(anagrams[group])
        
        return groups