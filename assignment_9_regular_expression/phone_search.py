"""Script provides find_phone_numbers function to find all phone numbers in the given string."""
import re

pattern = re.compile(r'''
    \(?\d{3}\)?[ ]?
    (?P<separator>[.-])?
    \d{3}
    (?P=separator)?
    [- ]?
    \d{4}
''', re.VERBOSE)


def find_phone_numbers(string) -> list[str]:
    """
    Finds all phone numbers in the given string.

    Args:
        string (str): the string to search phone numbers.

    Returns:
        list[str]: a list of phone numbers.

    Raises:
        ValueError: if the given type of string is not str.
    """
    if not isinstance(string, str):
        raise TypeError('String must be of type str.')

    match = pattern.finditer(string)
    phones = []
    for phone in match:
        phones.append(phone.group(0))

    return phones


if __name__ == '__main__':
    text_with_phones = ("phone 1: (123) 456-7890, phone 2: 123-456-7890, phone 3: 123.456.7890, "
                        "phone 4: 1234567890" "phone 5: (123) 4567890, phone 6: (123) 456 7890,")
    phones_list = find_phone_numbers(text_with_phones)
    print(phones_list)
