"""This script is designed to implement analyze_object function that finds
parent class and all its methods (full inheritance)."""


def analyze_inheritance(cls: type) -> None:
    """Find parent class, all its methods and print these data (full inheritance)."""

    for current_class in cls.__mro__[:-1]:
        parent_class = current_class.__base__
        message = f"{current_class.__name__} class inherits:\n" if parent_class != object \
            else f"{current_class.__name__} class based on {parent_class.__name__}"

        if parent_class != object:
            for name_attribute, attribute in parent_class.__dict__.items():
                if (callable(attribute) and not name_attribute.startswith("__") and
                        not name_attribute.endswith("__")):
                    message += f"\t-{name_attribute} from {parent_class.__name__}\n"

        print(message)


if __name__ == '__main__':
    class GrandParent:
        def grand_parent_method(self):
            pass


    class Parent(GrandParent):
        def parent_method(self):
            pass


    class Child(Parent):
        def child_method(self):
            pass


    analyze_inheritance(Child)
