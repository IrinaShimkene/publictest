import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 125, 5) == 25

    def test_substraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 18, 4) == 14

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 65, 13) == 78
