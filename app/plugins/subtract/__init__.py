'''This is a plugin that exits the program when called.'''
from app.commands import Command
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class SubtractCommand(Command):
    '''This class is a subclass of the Command class.'''
    def execute(self):
        '''This method exits the program when called'''
        try:
            a = input("Enter first number: ").strip()
            b = input("Enter second number: ").strip()
            a_decimal, b_decimal = map(Decimal, [a, b])
            result = Calculator.subtract(a_decimal, b_decimal)
            print(f"{a} - {b} = {result}")
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
