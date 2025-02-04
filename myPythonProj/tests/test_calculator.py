"""
Unit tests for calculator module.
"""

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10

def test_multiply():
    """Test multiplication function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5

def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(5, 0)
