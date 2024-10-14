import pytest
from calculator import sum, substraction, multiply, division

def test_sum():
    assert sum(1, 2) == 3
    assert sum(-1,2) == 1
    assert sum(-1,-2) == -3
    assert sum(0,0) == 0

def test_substraction():
    assert substraction(5,2) == 3
    assert substraction(-1,2) == -3
    assert substraction(-1,-2) == 1
    assert substraction(0,0) == 0

def test_multiply():
    assert multiply(5,2) == 10
    assert multiply(-1,2) == -2
    assert multiply(-1,-2) == 2
    assert multiply(0,0) == 0

def test_division():
    assert division(10,2) == 5
    assert division(-4,2) == -2
    assert division(-4,-2) == 2
    assert division(0,0) == "Error: Cannot divide by zero"