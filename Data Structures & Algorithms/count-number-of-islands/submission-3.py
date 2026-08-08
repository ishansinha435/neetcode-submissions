class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        def in_bounds(row, col):
            return 0 <= row < R and 0 <= col < C
        
        def dfs(r, c):
            if in_bounds(r, c) and grid[r][c] == "1":
                grid[r][c] = "0"
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dfs(r + dr, c + dc)

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
        