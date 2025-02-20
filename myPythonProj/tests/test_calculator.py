"""Unit tests for the Calculator module."""

import sys
import os
from decimal import Decimal  # Standard library import (first)
import pytest  # Third-party import (second)
"""Unit tests for the Calculator module."""
from calculator.operations import add, subtract, multiply, divide
from calculator.calculations import Calculations
from calculator.calculation import Calculation


# Add the parent directory to sys.path so that calculator module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



@pytest.fixture
def setup():
    """ Fixture to clear history before each test. """
    Calculations.clear_history()

def test_add(setup):
    """Tests the addition function of the Calculator."""
    _ = setup  # Suppresses pylint warning
    assert add(Decimal("2.5"), Decimal("3.5")) == Decimal("6.0")

def test_subtract(setup):
    """Tests the subtraction function of the Calculator."""
    _ = setup  # Suppresses pylint warning
    assert subtract(Decimal("5.5"), Decimal("2.5")) == Decimal("3.0")

def test_multiply(setup):
    """Tests the multiplication function of the Calculator."""
    _ = setup  # Suppresses pylint warning
    assert multiply(Decimal("2"), Decimal("3")) == Decimal("6")

def test_divide(setup):
    """Tests the division function of the Calculator."""
    _ = setup  # Suppresses pylint warning
    assert divide(Decimal("10"), Decimal("2")) == Decimal("5")

def test_divide_by_zero(setup):
    """Tests the division by 0 function of the Calculator."""
    _ = setup  # Suppresses pylint warning
    with pytest.raises(ZeroDivisionError):
        divide(Decimal("5"), Decimal("0"))

def test_history(setup):
    """Tests the history function of the Calculator."""
    _ = setup  # Suppresses pylint warning
    # Calculation.perform(Decimal("1"))
    assert len(Calculations.get_history()) == 0

