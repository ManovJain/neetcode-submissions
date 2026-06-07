class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = defaultdict(list)

        for word in strs:
            anagramArr = [0] * 26
            for letter in word:
                anagramArr[ord(letter) - ord('a')] += 1
            anagrams[tuple(anagramArr)].append(word)
        
        for anagram in anagrams:
            result.append(anagrams[anagram])
        
        return result