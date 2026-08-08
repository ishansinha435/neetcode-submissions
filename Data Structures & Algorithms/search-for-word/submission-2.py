class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        res = False

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(i, r, c):
            nonlocal res
            if in_bounds(r, c) and (r, c) not in visited and board[r][c] == word[i]:
                if i + 1 == len(word):
                    res = True
                    return
                visited.add((r, c))
                for dr, dc in dirs:
                    dfs(i + 1, r + dr, c + dc)
                visited.remove((r, c))
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    dfs(0, r, c)
        return res
