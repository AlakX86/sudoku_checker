def check_numbers(sudoku):
    range_number = [1,2,3,4,5,6,7,8,9]
    for row in sudoku:
        for num in row:
            if num in range_number[:len(sudoku)]:
                continue
            else:
                return False
    return True
