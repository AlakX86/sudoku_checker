import pytest
from check_sudoku import check_sudoku

@pytest.mark.test_repeats
def test_correct():
    assert check_sudoku([[1, 2, 3],[2, 3, 1],[3, 1, 2]]) == True
@pytest.mark.test_repeats
def test_incorrect1():
    assert check_sudoku([[1, 2, 3, 4],[2, 3, 1, 3],[3, 1, 2, 3],[4, 4, 4, 4]]) == False
@pytest.mark.test_repeats
def test_incorrect2():
    assert check_sudoku([[1, 2, 3, 4],[2, 3, 1, 4],[4, 1, 2, 3],[3, 4, 1, 2]]) == False
@pytest.mark.test_repeats
def test_incorrect3():
    assert check_sudoku([[1, 2, 3, 4, 5],[2, 3, 1, 5, 6],[4, 5, 2, 1, 3],[3, 4, 5, 2, 1],[5, 6, 4, 3, 2]]) == False
@pytest.mark.test_repeats
def test_incorrect6():
    assert check_sudoku([[1, 0, 0, 0],[0, 1, 0],[0, 0, 0, 1]]) == False
