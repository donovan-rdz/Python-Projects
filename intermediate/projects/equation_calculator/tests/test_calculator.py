"""
test_calculator.py
Unit tests for EquationCalculator.
"""

import unittest
from src.calculator import EquationCalculator


class TestEvaluate(unittest.TestCase):

    def setUp(self):
        self.calc = EquationCalculator()

    def test_simple_addition(self):
        result = self.calc.evaluate("2 + 3")
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 5)

    def test_expression_with_variable(self):
        result = self.calc.evaluate("2 * x + 1, x=4")
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 9)

    def test_exponentiation(self):
        result = self.calc.evaluate("2^3")
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 8)

    def test_invalid_expression(self):
        result = self.calc.evaluate("2 +* 3")
        self.assertFalse(result["success"])


class TestSolveLinear(unittest.TestCase):

    def setUp(self):
        self.calc = EquationCalculator()

    def test_simple_linear(self):
        result = self.calc.solve_linear("2x + 3 = 7")
        self.assertTrue(result["success"])
        self.assertIn("x = 2", result["result"])

    def test_negative_coefficient(self):
        result = self.calc.solve_linear("-x + 5 = 2")
        self.assertTrue(result["success"])
        self.assertIn("x = 3", result["result"])

    def test_missing_equals(self):
        result = self.calc.solve_linear("2x + 3")
        self.assertFalse(result["success"])


class TestSolveQuadratic(unittest.TestCase):

    def setUp(self):
        self.calc = EquationCalculator()

    def test_two_real_roots(self):
        result = self.calc.solve_quadratic("x^2 - 5x + 6 = 0")
        self.assertTrue(result["success"])
        self.assertIn("x₁", result["result"])

    def test_double_root(self):
        result = self.calc.solve_quadratic("x^2 - 2x + 1 = 0")
        self.assertTrue(result["success"])
        self.assertIn("double root", result["result"])

    def test_complex_roots(self):
        result = self.calc.solve_quadratic("x^2 + 1 = 0")
        self.assertTrue(result["success"])
        self.assertIn("complex roots", result["result"])


if __name__ == "__main__":
    unittest.main()
