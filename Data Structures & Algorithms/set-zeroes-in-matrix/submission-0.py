class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        
        row_fill = [False] * R
        col_fill = [False] * C
        
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    row_fill[r] = True
                    col_fill[c] = True
        
        for r in range(R):
            if row_fill[r]:
                for c in range(C):
                    matrix[r][c] = 0
        
        for c in range(C):
            if col_fill[c]:
                for r in range(R):
                    matrix[r][c] = 0