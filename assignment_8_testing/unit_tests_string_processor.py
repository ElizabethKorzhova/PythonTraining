"""Module is designed for testing StringProcessor class."""
import unittest
from string_processor import StringProcessor


class ModuleTestStringProcessor(unittest.TestCase):
    """Tests for StringProcessor class."""

    def setUp(self) -> None:
        """Creates StringProcessor instance before each test."""
        self.str_processor = StringProcessor()

    @unittest.skip
    def test_reverse_string_empty(self) -> None:
        """Test reverse_string with empty string."""
        self.assertEqual(self.str_processor.reverse_string(""), "")

    def test_reverse_string_correct_result(self) -> None:
        """Test reverse_string for compliance of the expected result with the actual result."""
        self.assertEqual(self.str_processor.reverse_string("hello "), " olleh")
        self.assertEqual(self.str_processor.reverse_string("12 21"), "12 21")
        self.assertEqual(self.str_processor.reverse_string("hI @9i"), "i9@ Ih")

    def test_capitalize_string_empty(self) -> None:
        """Test capitalize_string with empty string."""
        self.assertEqual(self.str_processor.capitalize_string(""), "")

    def test_capitalize_string_correct_result(self) -> None:
        """Test capitalize_string for compliance of the expected result with the actual result."""
        self.assertEqual(self.str_processor.capitalize_string("hello "), "Hello ")
        self.assertEqual(self.str_processor.capitalize_string("12Hello"), "12hello")
        self.assertEqual(self.str_processor.capitalize_string("aNNA @1"), "Anna @1")

    def test_count_vowels_empty(self) -> None:
        """Test count_vowels with empty string."""
        self.assertEqual(self.str_processor.count_vowels(""), 0)

    def test_count_vowels_correct_result(self) -> None:
        """Test capitalize_string for compliance of the expected result with the actual result."""
        self.assertEqual(self.str_processor.count_vowels("hello "), 2)
        self.assertEqual(self.str_processor.count_vowels("12 21"), 0)
        self.assertEqual(self.str_processor.count_vowels("hI @9i"), 2)
        self.assertEqual(self.str_processor.count_vowels("aNNA @1i Additional"), 8)

    def test_arguments_type_error(self) -> None:
        """Test argument type in all methods of StringProcessor class."""
        with self.assertRaises(TypeError):
            self.str_processor.reverse_string(1234)
        with self.assertRaises(TypeError):
            self.str_processor.capitalize_string(True)
        with self.assertRaises(TypeError):
            self.str_processor.count_vowels([])
