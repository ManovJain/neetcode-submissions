class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        hashSet = set(arr)
        
        for i in arr:
            if i + 1 in hashSet:
                count += 1
        
        return count