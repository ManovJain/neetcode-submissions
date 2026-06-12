class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)

        for row in range(1, ROWS):
            mat[row] = set(mat[row])
        
        if len(mat) > 1:
            for low in mat[0]:
                for i in range(1, len(mat)):
                    if low not in mat[i]:
                        break
                    if low in mat[i] and i == len(mat) - 1:
                        return low
        else:
            return mat[0][0]
            
        return -1
            
