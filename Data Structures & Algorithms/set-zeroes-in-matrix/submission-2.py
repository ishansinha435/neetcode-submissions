class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        
        row_0, col_0 = 1, 1
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_0 = 0
                    else:
                        matrix[r][0] = 0
                    if c == 0:
                        col_0 = 0
                    else:
                        matrix[0][c] = 0

        for r in range(1, R):
            if matrix[r][0] == 0:
                for c in range(1, C):
                    matrix[r][c] = 0
        
        for c in range(1, C):
            if matrix[0][c] == 0:
                for r in range(1, R):
                    matrix[r][c] = 0

        if row_0 == 0:
            for c in range(C):
                matrix[0][c] = 0
        
        if col_0 == 0:
            for r in range(R):
                matrix[r][0] = 0
        