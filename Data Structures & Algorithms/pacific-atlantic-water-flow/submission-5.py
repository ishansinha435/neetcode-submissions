class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        pacific, atlantic = set(), set()

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def dfs(r, c, ocean, prev):
            if not in_bounds(r, c) or (r, c) in ocean or heights[r][c] < prev:
                return
            ocean.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc, ocean, heights[r][c])
        
        for r in range(R):
            dfs(r, 0, pacific, float('-inf'))
            dfs(r, C - 1, atlantic, float('-inf'))
        for c in range(C):
            dfs(0, c, pacific, float('-inf'))
            dfs(R - 1, c, atlantic, float('-inf'))
        return list(pacific & atlantic)