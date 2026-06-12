class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)

        for row in range(ROWS):
            mat[row] = set(mat[row])
        
        for low in mat[0]:
            found = False
            for i in range(1, len(mat)):
                if low not in mat[i]:
                    break
                if low in mat[i] and i == len(mat) - 1:
                    return low
        
        return -1
            
