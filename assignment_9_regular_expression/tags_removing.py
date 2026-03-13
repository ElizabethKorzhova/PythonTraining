"""Script provides remove_tags function to delete tags from string."""
import re

pattern = re.compile(r'''
    <([a-z1-6]+)[^>]*?>
    \s*([^<>\n\t]*)\s*
    </\1>
''', re.VERBOSE)


def remove_tags(string: str) -> str:
    """
    Remove tags from the specified string.

    Args:
        string (str): the string to remove tags from it.

    Returns:
        str: the string without tags.
    """
    match = pattern.finditer(string)
    data = []
    for tag in match:
        data.append(tag.group(2))
    return "\n".join(data)


def read_html_file(file_path: str) -> str:
    """
    Read the specified HTML file.

    Args:
        file_path (str): the path to the HTML file.

    Returns:
        str: the content of the HTML file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    return data


if __name__ == '__main__':
    print(remove_tags(read_html_file("test.html")))
