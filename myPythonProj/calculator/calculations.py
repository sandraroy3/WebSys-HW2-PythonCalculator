"""
This module contains utility functions for the calculations history.
"""

class Calculations:
    """ Manages the history of calculations. """

    history = []

    @classmethod
    def add_to_history(cls, calculation):
        """ Adds a calculation instance to history. """
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        """ Retrieves the most recent calculation. """
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        """ Clears the calculation history. """
        cls.history.clear()
