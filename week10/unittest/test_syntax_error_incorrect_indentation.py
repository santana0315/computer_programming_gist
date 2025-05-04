import unittest
import io
import sys
from unittest.mock import patch
from week10.file.syntax_error_incorrect_indentation import calculate_area, is_even, print_squares

class TestSyntaxErrorIncorrectIndentation(unittest.TestCase):
    def test_calculate_area(self):
        self.assertEqual(calculate_area(2, 3), 6)
        self.assertEqual(calculate_area(5, 4), 20)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    def test_print_squares(self):
        # Capture print output by redirecting stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_squares(3)
        finally:
            sys.stdout = sys.__stdout__  # Restore stdout
        # Split output into lines and strip whitespace
        output = captured_output.getvalue().strip().split('\n')
        self.assertEqual(output, ['0', '1', '4'])

if __name__ == '__main__':
    unittest.main()