class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        # while l < r and t < b:
        #     for i in range(r - l):
        #         temp = matrix[t][l + i]
        #         matrix[t][l + i] = matrix[b - i][l]
        #         matrix[b - i][l] = matrix[b][r - i]
        #         matrix[b][r - i] = matrix[t + i][r]
        #         matrix[t + i][r] = temp
        #     l += 1
        #     r -= 1
        #     t += 1
        #     b -= 1

        matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]