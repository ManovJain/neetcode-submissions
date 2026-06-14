class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque()

        def dfs(row, col):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                return
            grid[row][col] = 2
            q.append((row, col))
            for d in directions:
                dfs(row + d[0], col + d[1])


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col)
                    break
            if q: break
        
        bridge = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (( 0 <= nr and nr < ROWS) and ( 0 <= nc and nc < COLS)):
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                        elif grid[nr][nc] == 1:
                            return bridge
            bridge += 1