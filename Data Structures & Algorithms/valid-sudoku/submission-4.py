class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = defaultdict(set)
        #rows
        for row in board:
            for n in row:
                if n == ".": continue
                if n in rows:
                    return False
                rows.add(n)
            rows.clear()
        #cols
        for i in range(9):
            for row in board:
                if row[i] == ".": continue
                if row[i] in cols:
                    return False
                cols.add(row[i])
            cols.clear()
        #boxes
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if board[r][c] in boxes[(r//3), (c//3)]:
                    return False
                boxes[(r//3), (c//3)].add(board[r][c])
        return True