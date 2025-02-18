'''This document contains the Calculation class, which represents an arithmetic operation on two numbers.'''
import sys
from unittest import mock
import pytest
from main import calculate_and_print, main  # Ensure this import matches your project structure

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),  # Testing another invalid number input
    ('5','0','divide','An error occurred: Cannot divide by zero')  # Testing division by zero
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    '''Test the calculate_and_print function with various inputs'''
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

def test_main_execution(monkeypatch, capsys):
    """Test the main function with valid inputs."""
    monkeypatch.setattr(sys, "argv", ["main.py", "10", "5", "add"])
    with mock.patch("main.calculate_and_print") as mocked_calculate:
        main()
        mocked_calculate.assert_called_once_with("10", "5", "add")

def test_invalid_number_of_arguments(capsys, monkeypatch):
    """Test when incorrect number of CLI arguments are given."""
    monkeypatch.setattr(sys, "argv", ["main.py", "5"])  # Only 1 argument instead of 3
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 1
    captured = capsys.readouterr()
    assert "Usage: python calculator_main.py <number1> <number2> <operation>" in captured.out
