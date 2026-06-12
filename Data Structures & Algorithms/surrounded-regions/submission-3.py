class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def capture(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            for d in directions:
                capture(r + d[0], c + d[1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)
        
        print(board)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        print(board)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        print(board)

                

        # first find all the 0s on the border - convert them

        # convert the remaining 0s to Xs

        # convert back the original border Xs