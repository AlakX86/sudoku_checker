def check_numbers(sudoku):
    range_number = [1,2,3,4,5,6,7,8,9]
    for row in sudoku:
        for num in row:
            if num in range_number[:len(sudoku)]:
                continue
            else:
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
    print(check_numbers(correcto))
    print(check_numbers(incorrecto1))
    print(check_numbers(incorrecto2))
    print(check_numbers(incorrecto3))
    print(check_numbers(incorrecto4))
    print(check_numbers(incorrecto5))
    print(check_numbers(incorrecto6))