"""This script is designed to implement log_methods decorator which logs calls to all its methods"""


def log_methods(cls: type) -> type:
    """Decorator which logs calls of class methods."""
    for attribute_name, attribute_method in cls.__dict__.items():
        if (callable(attribute_method) and not attribute_name.startswith("__")
                and not attribute_name.endswith("__")):

            def wrapper(self, *args, _method=attribute_method, _name=attribute_name, **kwargs):
                """Logs calls of class methods."""
                print(f"Logging: {_name} called with {args}")
                return _method(self, *args, **kwargs)

            setattr(cls, attribute_name, wrapper)
    return cls


if __name__ == '__main__':
    @log_methods
    class MyClass:
        def add(self, a, b):
            return a + b

        def subtract(self, a, b):
            return a - b


    obj = MyClass()
    obj.add(5, 3)
    obj.subtract(5, 3)
    print(obj.add(5, 3))
    print(obj.subtract(5, 3))
