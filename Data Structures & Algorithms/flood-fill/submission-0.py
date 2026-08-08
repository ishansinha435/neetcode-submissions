class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def in_bounds(r, c):
            return 0 <= r < R and 0 <= c < C

        old_color = image[sr][sc]
        if old_color == color:
            return image

        def dfs(r, c):
            if in_bounds(r, c) and image[r][c] == old_color:
                image[r][c] = color
                for dr, dc in dirs:
                    dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image