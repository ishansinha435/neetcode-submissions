class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF, R, C = 2147483647, len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def bfs(source):
            r, c, level = source
            q, visited = deque(), set()
            q.append((r, c, level))
            visited.add((r, c))
            while q:
                r, c, level = q.popleft()
                if grid[r][c] == -1 or not in_bounds(r, c):
                    continue
                if level < grid[r][c]:
                    grid[r][c] = level
                for dr, dc in dirs:
                    if in_bounds(r + dr, c + dc) and (r + dr, c + dc) not in visited:
                        q.append((r + dr, c + dc, level + 1))
                        visited.add((r + dr, c + dc))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    bfs((r, c, 0))