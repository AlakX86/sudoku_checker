import pytest
from check_sudoku import check_sudoku

@pytest.mark.test_no_numbers
def test_incorrect4():
    assert check_sudoku([['a', 'b', 'c'],['b', 'c', 'a'],['c', 'a', 'b']]) == False
    