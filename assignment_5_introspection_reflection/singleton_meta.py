"""This script is designed to implement Singleton design pattern which ensures that only
one object of its kind exists and provides a single point of access to it for any other code."""


class SingletonMeta(type):
    """Metaclass of Singleton that create only one object and store it to _instance."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Create and return Singleton instance."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


if __name__ == '__main__':
    class Singleton(metaclass=SingletonMeta):
        def __init__(self):
            print("Creating instance")


    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1 is obj2)
