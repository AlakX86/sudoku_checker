import pytest
from check_sudoku import check_sudoku

@pytest.mark.test_float
def test_incorrect5():
    assert check_sudoku([[1, 1.5],[1.5, 1]]) == False
    