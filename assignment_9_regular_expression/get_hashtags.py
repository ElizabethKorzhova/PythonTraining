"""Script provides get_hashtags function to find hashtags in the specified string."""
import re

pattern = re.compile(r'#\w+')


def get_hashtags(string: str) -> list[str]:
    """
    Returns a list of hashtags found in the specified string.

    Args:
        string (str): the string to search for hashtags.

    Returns:
        list[str]: the list of hashtags found in the specified string.

    Raises:
        TypeError: if the given type of string is not str.
    """
    if not isinstance(string, str):
        raise TypeError('String must be of type str')

    return pattern.findall(string)


if __name__ == '__main__':
    string_sample = ("Git GitHub #10versionControl software ##development "
                     "#DeveloperTools#SoftwareEngineering #TechSkills10")
    print(get_hashtags(string_sample))
