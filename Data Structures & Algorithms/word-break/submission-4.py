class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [False] * (len(s) + 1)
        check[len(s)] = True

        for i in range(len(s) - 1, -1 , -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    check[i] = check[i + len(w)]
                if check[i]:
                    break
        
        return check[0]