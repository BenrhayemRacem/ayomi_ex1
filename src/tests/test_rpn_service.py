import unittest
from src.services.rpn_service import RpnService


class TestRpnService(unittest.TestCase):

    def setUp(self):
        self.service = RpnService()

    def test_evaluate_simple_addition(self):
        result, _ = self.service.evaluate("2 3 +")
        self.assertEqual(result, 5)

    def test_evaluate_simple_subtraction(self):
        result, _ = self.service.evaluate("5 3 -")
        self.assertEqual(result, 2)

    def test_evaluate_simple_multiplication(self):
        result, _ = self.service.evaluate("2 3 *")
        self.assertEqual(result, 6)

    def test_evaluate_simple_division(self):
        result, _ = self.service.evaluate("6 3 /")
        self.assertEqual(result, 2)

    def test_evaluate_multiple_operations(self):
        result, _ = self.service.evaluate("2 3 + 5 *")
        self.assertEqual(result, 25)

    def test_evaluate_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.service.evaluate("2 0 /")

    def test_evaluate_invalid_token(self):
        with self.assertRaises(ValueError):
            self.service.evaluate("2 x +")

    def test_evaluate_missing_operand(self):
        with self.assertRaises(ValueError):
            self.service.evaluate("2 +")

    def test_evaluate_extra_operand(self):
        with self.assertRaises(ValueError):
            self.service.evaluate("2 3 4 +")

    def test_validate_valid_expression(self):
        self.service.validate("2 3 +")

    def test_validate_invalid_characters(self):
        with self.assertRaises(ValueError):
            self.service.validate("2 x +")

    def test_validate_missing_operands(self):
        with self.assertRaises(ValueError):
            self.service.validate("2 +")

    def test_validate_more_operators_than_operands(self):
        with self.assertRaises(ValueError):
            self.service.validate("2 + -")


if __name__ == "__main__":
    unittest.main()
