class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res, area = 0, 0

        def dfs(r, c):
            nonlocal res, area
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            area += 1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
                res = max(res, area)
                area = 0
        return res