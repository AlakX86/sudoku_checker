from check_columns import check_columns
from check_rows import check_rows
from check_square import check_square
from check_numbers import check_numbers
def check_sudoku(sudoku):
    return check_columns(sudoku) and check_rows(sudoku) and check_numbers(sudoku) and check_square(sudoku)

if __name__ == '__main__':

    correcto = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]

    incorrecto1 = [[1, 2, 3, 4],
                [2, 3, 1, 3],
                [3, 1, 2, 3],
                [4, 4, 4, 4]]

    incorrecto2 = [[1, 2, 3, 4],
                [2, 3, 1, 4],
                [4, 1, 2, 3],
                [3, 4, 1, 2]]

    incorrecto3 = [[1, 2, 3, 4, 5],
                [2, 3, 1, 5, 6],
                [4, 5, 2, 1, 3],
                [3, 4, 5, 2, 1],
                [5, 6, 4, 3, 2]]

    incorrecto4 = [['a', 'b', 'c'],
                ['b', 'c', 'a'],
                ['c', 'a', 'b']]

    incorrecto5 = [[1, 1.5],
                [1.5, 1]]

    incorrecto6 = [[1, 0, 0, 0],
                [0, 1, 0],
                [0, 0, 0, 1]]

# Casos test
    print(check_sudoku(correcto))
    print(check_sudoku(incorrecto1))
    print(check_sudoku(incorrecto2))
    print(check_sudoku(incorrecto3))
    print(check_sudoku(incorrecto4))
    print(check_sudoku(incorrecto5))
    print(check_sudoku(incorrecto6))