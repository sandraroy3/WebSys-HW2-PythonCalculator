"""
This module contains utility functions for the calculator.
"""

from decimal import Decimal, getcontext
from .calculations import Calculations
from .calculation import Calculation

# Set decimal precision
getcontext().prec = 28

class Calculator:
    """ A Calculator class to perform basic arithmetic operations with Decimal precision. """

    @staticmethod
    def add(operand1: Decimal, operand2: Decimal) -> Decimal:
        """ Adds two decimal numbers. """
        result = operand1 + operand2
        Calculations.add_to_history(Calculation(operand1, operand2, "add", result))
        return result

    @staticmethod
    def subtract(operand1: Decimal, operand2: Decimal) -> Decimal:
        """ Subtracts operand2 from operand1. """
        result = operand1 - operand2
        Calculations.add_to_history(Calculation(operand1, operand2, "subtract", result))
        return result

    @staticmethod
    def multiply(operand1: Decimal, operand2: Decimal) -> Decimal:
        """ Multiplies two decimal numbers. """
        result = operand1 * operand2
        Calculations.add_to_history(Calculation(operand1, operand2, "multiply", result))
        return result

    @staticmethod
    def divide(operand1: Decimal, operand2: Decimal) -> Decimal:
        """ Divides operand1 by operand2, handling division by zero. """
        if operand2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = operand1 / operand2
        Calculations.add_to_history(Calculation(operand1, operand2, "divide", result))
        return result
