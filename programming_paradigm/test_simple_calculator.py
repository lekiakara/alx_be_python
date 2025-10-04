import unittest
from simple_calculator import SimpleCalculator   # assumes your class is in simple_calculator.py


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # Tests for addition
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 7), 10)
        self.assertEqual(self.calc.add(-5, -2), -7)
        self.assertEqual(self.calc.add(-3, 7), 4)

    # Tests for subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(7, -3), 10)

    # Tests for multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, -2), 6)
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # Tests for division
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(-12, 4), -3)
        self.assertIsNone(self.calc.divide(10, 0))

    
if __name__ == "__main__":
    unittest.main()
