class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen, distinct = set(), set()

        for i in arr:
            if i in distinct:
                seen.add(i)
                distinct.remove(i)
            elif i in seen:
                continue
            else:
                distinct.add(i)
        
        for i in arr:
            if i in distinct:
                k -= 1
                if k == 0:
                    return i
        
        return ""
