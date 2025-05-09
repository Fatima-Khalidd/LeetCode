class Solution(object):
    def isSafe(self, board, row, column, digit):
        for col in range(9):
            if board[row][col] == digit:
                return False

        for r in range(9):
            if board[r][column] == digit:
                return False

        startRow = (row // 3) * 3
        startCol = (column // 3) * 3
        for r in range(startRow, startRow + 3):
            for c in range(startCol, startCol + 3):
                if board[r][c] == digit:
                    return False

        return True

    def sudokuSolver(self, board, row, col):
        if row == 9:
            return True

        nextRow, nextCol = row, col + 1
        if nextCol == 9:
            nextRow += 1
            nextCol = 0

        if board[row][col] != ".":
            return self.sudokuSolver(board, nextRow, nextCol)  

        for digit in map(str, range(1, 10)):
            if self.isSafe(board, row, col, digit):
                board[row][col] = digit
                if self.sudokuSolver(board, nextRow, nextCol):  # ✅ fixed call
                    return True
                board[row][col] = "."

        return False

    def solveSudoku(self, board):
        self.sudokuSolver(board, 0, 0)
