def check_square(sudoku):
    num_rows = len(sudoku)
    for row in sudoku:
        if len(row) != num_rows:
            return False
    return True
