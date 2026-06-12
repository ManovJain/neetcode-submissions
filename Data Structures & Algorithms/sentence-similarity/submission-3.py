class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # sentence1 = sentence1.split()
        # sentence2 = sentence2.split()

        if len(sentence1) != len(sentence2):
            return False
        
        wordToSimilarWords = defaultdict(set)

        for word1, word2 in similarPairs:
            wordToSimilarWords[word1].add(word2)
            wordToSimilarWords[word2].add(word1)

        for index in range(len(sentence1)):
            if sentence1[index] == sentence2[index]:
                continue
            if sentence2[index] not in wordToSimilarWords[sentence1[index]]:
                return False
        
        return True