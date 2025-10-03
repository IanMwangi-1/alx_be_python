import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        # integers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # floats
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7)
        # zero
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 4), -8)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(100000, 1000), 100000000)

    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_negative_numbers(self):
        self.assertAlmostEqual(self.calc.divide(-10, 2), -5)
        self.assertAlmostEqual(self.calc.divide(10, -2), -5)
        self.assertAlmostEqual(self.calc.divide(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()
