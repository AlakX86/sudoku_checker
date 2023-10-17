def check_square(sudoku):
    num_rows = len(sudoku)
    for row in sudoku:
        if len(row) != num_rows:
            return False
    return True

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
    print(check_square(correcto))
    print(check_square(incorrecto1))
    print(check_square(incorrecto2))
    print(check_square(incorrecto3))
    print(check_square(incorrecto4))
    print(check_square(incorrecto5))
    print(check_square(incorrecto6))