"""This module is designed to implement analyze_object function that find:
    - object type
    - methods and attributes of the object.
    - type of methods and attributes of the object."""


def analyze_object(obj: object) -> None:
    """Finds object type, methods and attributes of the object and their type."""
    print(f"Type of object: {type(obj)}")

    non_dunder_members: list[str] = []
    for member in dir(obj):
        if not member.startswith("__") and not member.endswith("__"):
            non_dunder_members.append(member)

    print("Attributes and methods (dunder methods not included):")
    for member in non_dunder_members:
        print(f"- {member}: {type(getattr(obj, member))}")
