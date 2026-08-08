class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(r, c):
            if in_bounds(r, c) and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + sum(dfs(r + dr, c + dc) for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)])
            else:
                return 0

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res