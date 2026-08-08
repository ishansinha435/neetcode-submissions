class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def dfs(r, c):
            if in_bounds(r, c) and grid[r][c] == "1":
                grid[r][c] = "0"
                for dr, dc in dirs:
                    dfs(r + dr, c + dc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res