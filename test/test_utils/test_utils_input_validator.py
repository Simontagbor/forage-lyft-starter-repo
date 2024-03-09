"""This Module Tests the utility functions in the input_validator module."""
import unittest
from datetime import datetime, date
from utils.input_validator import validate_date, validate_int, validate_bool, validate_array


class TestInputValidator(unittest.TestCase):
    """Tests for the input_validator module"""
    def test_validate_date_returns_date(self):
        """Test that the validate_date function returns a date object"""
        self.assertIsInstance(validate_date(datetime.now()), date)

    def test_validate_date_returns_correct_date(self):
        """Test that the validate_date function returns the correct date"""
        self.assertEqual(validate_date(datetime.now()), datetime.now().date())

    def test_validate_date_returns_correct_date_from_string(self):
        """Test that the validate_date function returns the correct date from a string"""
        self.assertEqual(validate_date('2021-01-01'), date(2021, 1, 1))

    def test_validate_date_raises_error(self):
        """Test that the validate_date function raises an error for invalid input"""
        with self.assertRaises(TypeError):
            validate_date(123)

    def test_validate_int_returns_int(self):
        """Test that the validate_int function returns an integer"""
        self.assertIsInstance(validate_int(123, 'test'), int)

    def test_validate_int_returns_correct_int(self):
        """Test that the validate_int function returns the correct integer"""
        self.assertEqual(validate_int(123, 'test'), 123)

    def test_validate_int_returns_correct_int_from_string(self):
        """Test that the validate_int function returns the correct integer from a string"""
        self.assertEqual(validate_int('123', 'test'), 123)

    def test_validate_int_raises_error(self):
        """Test that the validate_int function raises an error for invalid input"""
        with self.assertRaises(TypeError):
            validate_int('abc', 'test')

    def test_validate_bool_returns_bool(self):
        """Test that the validate_bool function returns a boolean"""
        self.assertIsInstance(validate_bool(True, 'test'), bool)

    def test_validate_bool_returns_correct_bool(self):
        """Test that the validate_bool function returns the correct boolean"""
        self.assertEqual(validate_bool(True, 'test'), True)

    def test_validate_bool_returns_correct_bool_from_string(self):
        """Test that the validate_bool function returns the correct boolean from a string"""
        self.assertEqual(validate_bool('true', 'test'), True)

    def test_validate_bool_raises_error(self):
        """Test that the validate_bool function raises an error for invalid input"""
        with self.assertRaises(TypeError):
            validate_bool('abc', 'test')
    # test array validator
    def test_validate_array_returns_list(self):
        """Test that the validate_array function returns a list"""
        self.assertIsInstance(validate_array([1, 2, 3], 'test'), list)

    def test_validate_array_returns_correct_list(self):
        """Test that the validate_array function returns the correct list"""
        self.assertEqual(validate_array([1, 2, 3], 'test'), [1, 2, 3])

    def test_validate_array_returns_correct_list_from_string(self):
        """Test that the validate_array function returns the correct list from a string"""
        self.assertEqual(validate_array('1,2,3', 'test'), [1, 2, 3])

    def test_validate_array_raises_error(self):
        """Test that the validate_array function raises an error for invalid input"""
        with self.assertRaises(TypeError):
            validate_array(123, 'test')

    def test_validate_array_raises_error_for_invalid_string(self):
        """Test that the validate_array function raises an error for invalid string input"""
        with self.assertRaises(TypeError):
            validate_array('abc', 'test')

    def test_validate_array_raises_error_for_invalid_list(self):
        """Test that the validate_array function raises an error for invalid list input"""
        invalid_input = {"not": "a list"} 
        with self.assertRaises(TypeError):
            validate_array(invalid_input, "invalid_input")

    def test_validate_array_raises_error_for_invalid_list_string(self):
        """Test that the validate_array function raises an error for invalid list string input"""
        with self.assertRaises(TypeError):
            validate_array('1,a,3', 'test')


if __name__ == '__main__':
    unittest.main()
