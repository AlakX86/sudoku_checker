def check_rows(sudoku):
    for row in sudoku:
        seen_numbers = []
        for number in row:
            if number in seen_numbers:
                return False
            seen_numbers.append(number)
    return True
