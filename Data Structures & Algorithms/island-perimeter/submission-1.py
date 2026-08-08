class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def dfs(r, c):
            if in_bounds(r, c) and grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                return sum(dfs(r + dr, c + dc) for dr, dc in dirs)
            elif (r, c) in visited:
                return 0
            else:
                return 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return dfs(r, c)
