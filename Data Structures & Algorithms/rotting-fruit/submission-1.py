class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def bfs(r, c):
            q, visited = deque(), set()
            q.append((r, c))
            visited.add((r, c))
            steps = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 2:
                        return steps
                    for dr, dc in dirs:
                        if (in_bounds(r + dr, c + dc) and
                            grid[r + dr][c + dc] != 0 and  
                            (r + dr, c + dc) not in visited):
                            q.append((r + dr, c + dc))
                            visited.add((r + dr, c + dc))
                steps += 1
            return -1

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    steps = bfs(r, c)
                    if steps == -1:
                        return -1
                    res = max(res, steps)
        return res
        