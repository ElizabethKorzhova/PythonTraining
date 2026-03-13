"""Script provides is_valid_password function to check the password."""
import re

pattern = re.compile(r'''
    (?=.*[a-z])
    (?=.*[A-Z])
    (?=.*[0-9])
    (?=.*[@#$%&-_.])
    (?!.*\s)
    .{8,}
''', re.VERBOSE)


def is_valid_password(password: str) -> bool:
    """
    Checks whether the specified password matches the given pattern.

    Args:
        password (str): the password to check.

    Returns:
        bool: if the password is valid return True; otherwise return False.
    """
    return bool(pattern.fullmatch(password))


if __name__ == '__main__':
    passwords = [
        "1fF&",
        "1111111111",
        "s_tT 6  8 D_Y",
        "aA9_aA9_",
    ]
    for pass_sample in passwords:
        print(f"{pass_sample}{' ' if is_valid_password(pass_sample) else ' not '.upper()}VALID")
