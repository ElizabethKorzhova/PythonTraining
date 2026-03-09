"""Module is designed for testing StringProcessor class."""
import unittest


class StringProcessor:
    """Class for string manipulations.

    Static methods:
        reverse_string(string):
            returns string in reverse order
        capitalize_string(string):
            returns string with capitalized first letter
        count_vowels(string):
            returns number of vowels in string
    """

    @staticmethod
    def reverse_string(string: str) -> str:
        """Reverses a string."""
        if not isinstance(string, str):
            raise TypeError("Argument must be a string")
        return string[::-1]

    @staticmethod
    def capitalize_string(string: str) -> str:
        """Capitalizes a first letter in string."""
        if not isinstance(string, str):
            raise TypeError("Argument must be a string")
        return string.capitalize()

    @staticmethod
    def count_vowels(string: str) -> int:
        """Counts number of vowels in string."""
        if not isinstance(string, str):
            raise TypeError("Argument must be a string")

        vowels = 'a', 'e', 'i', 'o', 'u'
        count = 0
        for char in string:
            if char.lower() in vowels:
                count += 1
        return count


class ModuleTestStringProcessor(unittest.TestCase):
    """Tests for StringProcessor class."""

    def setUp(self):
        """Creates StringProcessor instance before each test."""
        self.str_processor = StringProcessor()

    @unittest.skip
    def test_reverse_string_empty(self):
        """Test reverse_string with empty string."""
        self.assertEqual(self.str_processor.reverse_string(""), "")

    def test_reverse_string_correct_result(self):
        """Test reverse_string for compliance of the expected result with the actual result."""
        self.assertEqual(self.str_processor.reverse_string("hello "), " olleh")
        self.assertEqual(self.str_processor.reverse_string("12 21"), "12 21")
        self.assertEqual(self.str_processor.reverse_string("hI @9i"), "i9@ Ih")

    def test_capitalize_string_empty(self):
        """Test capitalize_string with empty string."""
        self.assertEqual(self.str_processor.capitalize_string(""), "")

    def test_capitalize_string_correct_result(self):
        """Test capitalize_string for compliance of the expected result with the actual result."""
        self.assertEqual(self.str_processor.capitalize_string("hello "), "Hello ")
        self.assertEqual(self.str_processor.capitalize_string("12Hello"), "12hello")
        self.assertEqual(self.str_processor.capitalize_string("aNNA @1"), "Anna @1")

    def test_count_vowels_empty(self):
        """Test count_vowels with empty string."""
        self.assertEqual(self.str_processor.count_vowels(""), 0)

    def test_count_vowels_correct_result(self):
        """Test capitalize_string for compliance of the expected result with the actual result."""
        self.assertEqual(self.str_processor.count_vowels("hello "), 2)
        self.assertEqual(self.str_processor.count_vowels("12 21"), 0)
        self.assertEqual(self.str_processor.count_vowels("hI @9i"), 2)
        self.assertEqual(self.str_processor.count_vowels("aNNA @1i Additional"), 8)

    def test_arguments_type_error(self):
        """Test argument type in all methods of StringProcessor class."""
        with self.assertRaises(TypeError):
            self.str_processor.reverse_string(1234)
        with self.assertRaises(TypeError):
            self.str_processor.capitalize_string(True)
        with self.assertRaises(TypeError):
            self.str_processor.count_vowels([])
