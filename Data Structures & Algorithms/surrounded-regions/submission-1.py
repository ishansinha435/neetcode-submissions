class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        border_reached = False

        def is_border(r, c):
            return r == 0 or r == R - 1 or c == 0 or c == C - 1

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(r, c):
            nonlocal border_reached
            if not in_bounds(r, c) or board[r][c]!= "O":
                return
            board[r][c] = "T"
            if is_border(r, c):
                border_reached = True
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
            if not border_reached:
                board[r][c] = "X"

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    dfs(r, c)
                    border_reached = False

        for r in range(R):
            for c in range(C):
                if board[r][c] == "T":
                    board[r][c] = "O" 