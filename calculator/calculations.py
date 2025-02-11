# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, line-too-long
from typing import List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def get_latest_calculation(cls) -> Calculation:
        return cls.history[-1]

    @classmethod
    def get_calculation_count(cls) -> int:
        return len(cls.history)

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        return [calculation for calculation in cls.history if calculation.operation.__name__ == operation_name]
