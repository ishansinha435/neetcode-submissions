class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, ocean, prev):
            if (min(r, c) < 0 or r >= rows or c >= cols or 
                (r, c) in ocean or heights[r][c] < prev):
                return
            ocean.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, ocean, heights[r][c])

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, pacific, float('-inf'))
                if r == rows - 1 or c == cols - 1:
                    dfs(r, c, atlantic, float('-inf'))
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res