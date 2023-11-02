from check_columns import check_columns
from check_rows import check_rows
from check_square import check_square
from check_numbers import check_numbers
def check_sudoku(sudoku):
    return check_columns(sudoku) and check_rows(sudoku) and check_numbers(sudoku) and check_square(sudoku)
