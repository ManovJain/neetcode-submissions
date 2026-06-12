class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        posMap = {}
        for i in range(len(keyboard)):
            posMap[keyboard[i]] = i
        
        pos = posMap[word[0]]
        keyStrokes = pos

        for i in range(1, len(word)):
            keyStrokes += abs(posMap[word[i]] - pos)
            pos = posMap[word[i]]
        
        return keyStrokes


