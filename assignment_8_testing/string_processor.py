"""Module provides StringProcessor class for future testing."""


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
