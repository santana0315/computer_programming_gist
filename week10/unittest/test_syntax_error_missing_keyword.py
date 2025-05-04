import unittest
import io
import sys
from week10.file.syntax_error_missing_keyword import calculate_area, is_positive, print_message

class TestSyntaxErrorMissingKeyword(unittest.TestCase):
    def test_calculate_area(self):
        self.assertEqual(calculate_area(2, 3), 6)
        self.assertEqual(calculate_area(5, 4), 20)

    def test_is_positive(self):
        self.assertTrue(is_positive(5))
        self.assertFalse(is_positive(-2))
        self.assertFalse(is_positive(0))

    def test_print_message(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_message("Hello")
        finally:
            sys.stdout = sys.__stdout__  # Restore stdout
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Hello")

if __name__ == '__main__':
    unittest.main()