"""Script provides is_valid_email function to check the email address."""
import re

pattern = re.compile(r'''
    ^\w+ 
    (?:\.[0-9a-zA-Z]+)*
    @\w+
    [.][a-zA-Z]{2,6}$
''', re.VERBOSE)


def is_valid_email(email: str) -> bool:
    """
    Checks whether the specified email address matches the given pattern.

    Args:
        email (str): the email address to check.

    Returns:
        bool: if the email is valid return True; otherwise return False.

    Raises:
        ValueError: in case of the email is not a string.
    """
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    return bool(pattern.match(email))


if __name__ == '__main__':
    emails_to_check = [
        ".example@domain.com",
        "example.@domain.com",
        "exam..ple@domain.com",
        "example.example@domain.com1",
        "example.exampledomain.com",
        "example.example@domaincom",
        "example.example@.com",
        "example@domain.com",
        "Example@domain.com",
        "1exam2ple@domain.com",
        "example1@domain.com",
        "EXAMPLE@domain.com",
        "EXAMPLE@DOMAIN.com",
        "EXAMPLE@DOMAIN1.com",
        "EXAMPLE@DOMAIN.COM",
        "example.example@domain.com",
        "example.example.example@domain.com",
        "e.x.a.m.p.l.e@domain.com",

    ]
    for email_sample in emails_to_check:
        print(f"{email_sample}{'' if is_valid_email(email_sample) else ' not'.upper()} VALID")
