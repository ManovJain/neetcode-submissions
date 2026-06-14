class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        occurances = [0] * ((n * n) + 1)
        result = [0, 0]

        for row in grid:
            for col in row:
                occurances[col] += 1

        for i in range(1, len(occurances)):
            if occurances[i] == 0:
                result[1] = i
            if occurances[i] == 2:
                result[0] = i
        
        return result