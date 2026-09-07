class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        pacific, atlantic = set(), set()

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        def dfs(r, c, level, ocean):
            if in_bounds(r, c) and (r, c) not in ocean and heights[r][c] >= level:
                ocean.add((r, c))
                for dr, dc in dirs:
                    dfs(r + dr, c + dc, heights[r][c], ocean)
        
        for r in range(R):
            dfs(r, 0, float('-inf'), pacific)
            dfs(r, C - 1, float('-inf'), atlantic)

        for c in range(C):
            dfs(0, c, float('-inf'), pacific)
            dfs(R - 1, c, float('-inf'), atlantic)
        
        return list(pacific & atlantic)