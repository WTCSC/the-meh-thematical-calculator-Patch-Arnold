import pytest
from mehmatical import add, subtract, mult, div

"""add"""
def test_add_positive_numbers():
    """tests adding positives"""
    assert add(5, 3) == 8
def test_add_negative_numbers():
    """tests adding negative"""
    assert add(-5, -3) == -8
"""subtract"""
def test_subtract_postivites():
    """tests subtracting positives"""
    assert subtract(5, 3) == 2
def test_subtract_negatives():
    """tests subtracting negatives"""
    assert subtract(-5, -3) == -2
def test_subtract_into_negatives():
    """tests subtracting into negative domain"""
    assert subtract(3, 5) == -2
"""multiply"""
def test_multiply_positives():
    """tests positive multiplication"""
    assert mult(5, 3) == 15
def test_multiply_negatives():
    """tests negative mulitplication"""
    assert mult(-5, -3) == 15
def test_multiply_one_negative():
    """test negative and postive"""
    assert mult(-5, 3) == -15
"""divide"""
def test_division_postives():
    """tests positive division"""
    assert div(15, 3) == 5
def test_division_negative():
    """tests negative division"""
    assert div(-15, -3) == 5
def test_division_one_negative():
    """tests one negative, answer should be negative"""
    assert div(-15, 3) == -5