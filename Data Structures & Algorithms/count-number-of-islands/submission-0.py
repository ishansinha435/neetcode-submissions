class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        hset, self.res = set(), 0

        def dfs(r, c, is_island):
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            if (r, c) not in hset and not is_island:
                self.res += 1
            if (r, c) not in hset:
                hset.add((r, c))
                dfs(r + 1, c, True)
                dfs(r - 1, c, True)
                dfs(r, c + 1, True)
                dfs(r, c - 1, True)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, False)
        return self.res
