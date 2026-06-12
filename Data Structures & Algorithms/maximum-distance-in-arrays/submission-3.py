class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        currentMin, currentMax = arrays[0][0], arrays[0][-1]

        dist = 0

        for i in range(1, len(arrays)):
            dist = max(arrays[i][-1] - currentMin, currentMax - arrays[i][0], dist)

            currentMin = min(arrays[i][0], currentMin)
            currentMax = max(arrays[i][-1], currentMax)
        
        return dist

