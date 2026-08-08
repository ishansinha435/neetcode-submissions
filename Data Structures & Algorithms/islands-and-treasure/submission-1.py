class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF, R, C = 2147483647, len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def bfs(sources):
            q, visited = deque(sources), set(sources)
            level = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == -1 or not in_bounds(r, c):
                        continue
                    if level < grid[r][c]:
                        grid[r][c] = level
                    for dr, dc in dirs:
                        if in_bounds(r + dr, c + dc) and (r + dr, c + dc) not in visited:
                            q.append((r + dr, c + dc))
                            visited.add((r + dr, c + dc))
                level += 1

        sources = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    sources.append((r, c))
        bfs(sources)