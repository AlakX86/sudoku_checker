# sudoku_checker
sudoku_checker es un set de 4 funciones y 1 funcional final que verifica que un sudoku está correctamente hecho<br>
Las 4 funciones son:<br>
  check_columns: Verify that there are no repeating numbers in the columns.<br>
  check_numbers: Verify that the inputs are integers from 1 to 9 as indicated in the sudoku rules.<br>
  check_rows: Checks for repeating numbers in rows.<br>
  check_square: Verifies that the sudoku is square, because if it is not, it is not a sudoku.<br>
Y la funcion final:<br>
  check_sudoku:Uses the 4 previous functions to return a boolean value that will indicate whether it is True or False.<br>
Además se comparten los casos test aparte en test_cases.py