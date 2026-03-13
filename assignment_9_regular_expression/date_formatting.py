"""Script provides change_date_format to change date format from DD/MM/YYYY to DD-MM-YYYY."""
import re

pattern = re.compile(r'''
    (?<=\d{2})
    /
    (?=\d{2,4})
''', re.VERBOSE)


def change_date_format(string: str) -> str:
    """
    Changes the string with the date format from DD/MM/YYYY to DD-MM-YYYY.

    Args:
        string (str): the string to change date format.

    Returns:
        str: the string with the date in the DD-MM-YYYY format.

    Raises:
        TypeError: if the given type of string is not str.
    """
    if not isinstance(string, str):
        raise TypeError('String must be of type str')

    return re.sub(pattern, '-', string)


if __name__ == '__main__':
    string_sample = "Date 15/07/2025 and date 09/07/2026 date/date 22//"

    print(f"{string_sample}\n{change_date_format(string_sample)}")
