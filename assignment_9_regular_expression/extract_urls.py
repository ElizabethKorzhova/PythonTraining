"""Script provides extract_urls to remove urls from the string."""
import re

pattern = re.compile(r'''
    https?://
    \S+
''', re.VERBOSE)


def extract_urls(string: str) -> str:
    """
    Extracts all urls from the string.
    Args:
        string (str): the string.

    Returns:
        str: the string without urls.
    """

    return pattern.sub("", string)


if __name__ == '__main__':
    str_sample = "test http://www.youtube.com/results?search_query= test https://github.com/"
    print(extract_urls(str_sample))
