class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if color == original:
            return image

        def recolor(row, column):
            if row < 0 or row >= len(image) or column < 0 or column >= len(image[0]) or image[row][column] != original:
                return
            
            image[row][column] = color
            
            recolor(row, column + 1)
            recolor(row + 1, column)
            recolor(row, column - 1)
            recolor(row - 1, column)
        
        recolor(sr, sc)

        return image