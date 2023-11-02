def check_columns(sudoku):
    for column in range(len(sudoku)):
        column_values = []
        for row in sudoku:
            column_values.append(row[column])

        for value in column_values:
            if column_values.count(value) > 1:
                return False
    return True
