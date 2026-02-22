"""This module is designed to implement analyze_object function that finds
parent class and all its methods"""


def analyze_inheritance(cls: type) -> None:
    """Find parent class, all its methods and print these data."""
    print(f"{cls.__name__} class inherits:")
    for name_attribute, attribute in cls.__base__.__dict__.items():
        if (callable(attribute) and not name_attribute.startswith("__") and
                not name_attribute.endswith("__")):
            print(f"\t-{name_attribute} from {cls.__base__.__name__}")
