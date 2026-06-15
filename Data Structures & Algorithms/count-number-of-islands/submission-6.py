class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(row, col):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)
        
        return islands

            