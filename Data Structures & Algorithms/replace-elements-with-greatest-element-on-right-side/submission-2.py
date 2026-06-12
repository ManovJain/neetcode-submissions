class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        n = len(arr) - 1

        while n > -1:
            large = largest
            largest = max(largest, arr[n])
            arr[n] = large
            n -= 1
        
        return arr