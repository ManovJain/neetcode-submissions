class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        
        if ROWS == 1 and COLS == 1:    # start is the goal
            return 1
        
        q = deque([(0,0)])
        grid[0][0] = 1

        moves = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0):
                        if nr == ROWS - 1 and nc == COLS - 1:
                            return moves + 1
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            moves += 1

        return - 1


