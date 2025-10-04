import unittest
from simple_calculator import SimpleCalculator   # assumes your class is in simple_calculator.py


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for add ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 7), 10)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -2), -7)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-3, 7), 4)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(10, 0), 10)

    # --- Tests for subtract ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(7, -3), 10)

    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Tests for multiply ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 5), -15)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # --- Tests for divide ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-9, -3), 3)

    def test_divide_mixed_numbers(self):
        self.assertEqual(self.calc.divide(-12, 4), -3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
