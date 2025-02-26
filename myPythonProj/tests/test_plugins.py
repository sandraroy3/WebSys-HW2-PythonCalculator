import pytest
from calculator.plugins.add import AddCommand
from calculator.plugins.greet import GreetCommand

def test_add(capsys):
    """
    Tests whether AddCommand executes correctly and correctly captures output.
    """
    command = AddCommand()
    
    # Run command with test values
    command.execute(5, 5)

    # Capture output
    captured = capsys.readouterr()

    # Extract numerical part from output (ignoring process name)
    result_str = captured.out.strip().split(":")[-1].strip()  # Extracts "Result = 10"
    
    # Convert to float and assert correctness
    assert float(result_str.split("=")[-1].strip()) == 10.0

def test_greet_command(capsys):
    """
    Tests whether GreetCommand prints the expected greeting.
    """
    command = GreetCommand()

    # Run command
    command.execute()

    # Capture printed output
    captured = capsys.readouterr()

    # Assert expected greeting message (ignoring process name)
    assert "Hello, World!" in captured.out
