"""
This module contains utility functions for the calculator.
"""

from decimal import Decimal

class Calculation:
    """ Represents a single arithmetic calculation. """

    def __init__(self, operand1: Decimal, operand2: Decimal, operation: str, result: Decimal):
        """ init method. """
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation
        self.result = result

    def __str__(self):
        """ str function """
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"
