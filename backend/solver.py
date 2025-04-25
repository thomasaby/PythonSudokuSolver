class SudokuSolver:
    def __init__(self, board):
        self.board = board  # 9x9 list of integers (0 = empty cell)

    def get_solution(self):
        if self._solve():
            return self.board
        return None

    def _solve(self):
        empty = self._find_empty()
        if not empty:
            return True  # puzzle solved

        row, col = empty
        for num in range(1, 10):
            if self._is_valid(num, row, col):
                self.board[row][col] = num
                if self._solve():
                    return True
                self.board[row][col] = 0  # backtrack

        return False  # trigger backtracking

    def _find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def _is_valid(self, num, row, col):
        # Check row
        if any(self.board[row][j] == num for j in range(9)):
            return False
        # Check column
        if any(self.board[i][col] == num for i in range(9)):
            return False
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        return True
