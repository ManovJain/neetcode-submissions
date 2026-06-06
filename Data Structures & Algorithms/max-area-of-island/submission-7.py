class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col) -> int:
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            total = 1
            for x, y in directions:
                total += dfs(row + x, col + y)
            return total
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col))
        
        return area
