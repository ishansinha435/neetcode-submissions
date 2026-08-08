class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        q, visited = deque(), set()

        def add_cell(r, c):
            if (0 <= r < R and 0 <= c < C and 
                grid[r][c] != 0 and 
                (r, c) not in visited):
                visited.add((r, c))
                q.append((r, c))

        fresh = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    add_cell(r, c)

        steps = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    fresh -= 1
                for dr, dc in dirs:
                    add_cell(r + dr, c + dc)
            steps += 1
        return max(0, steps) if fresh == 0 else -1
        