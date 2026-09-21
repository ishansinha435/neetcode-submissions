class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def dfs(r, c, i):
            if not in_bounds(r, c) or (r, c) in visited or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            res = any(dfs(r + dr, c + dc, i + 1) for dr, dc in dirs)
            visited.remove((r, c))
            return res


        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False