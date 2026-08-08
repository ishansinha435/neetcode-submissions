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
                    return True
                visited.add((r, c))
                res = any(dfs(i + 1, r + dr, c + dc) for dr, dc in dirs)
                visited.remove((r, c))
                return res
        
        for r in range(R):
            for c in range(C):
                if dfs(0, r, c):
                    return True
        return False
