import unittest
from app.calculator import Calculator
from app.dividebyzero_exception import DivideByZeroMyException
 
class CalculatorTest(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        self.assertEqual(calc.add(2,2), 4)

    def test_calculator_divide_method_returns_correct_result(self):
        calc = Calculator()
        self.assertEqual(calc.divide(2,2), 1)

    def test_calculator_divide_method_should_raise_error_divide_by_zero(self):
        calc = Calculator()

        with self.assertRaises(DivideByZeroMyException) as context:
            calc.divide(2,0)

        self.assertTrue('Divisao por zero nao permitida!' in context.exception)