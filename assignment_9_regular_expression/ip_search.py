"""Script provides find_ip_address to find and return the IP address from the string."""
import re

pattern = re.compile(r'''
    ((?:0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.
    (?:0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5]))
''', re.VERBOSE)


def find_ip_address(string: str) -> list[str]:
    """
    Finds the IP address from the string.
    Args:
        string (str): the string to find the IP address.

    Returns:
        list[str]: all IP address from the string.
    """
    return re.findall(pattern, string)


if __name__ == '__main__':
    str_sample = "test test test 1.1.1.1 test 3.67.90.255 12.343"
    print(find_ip_address(str_sample))
