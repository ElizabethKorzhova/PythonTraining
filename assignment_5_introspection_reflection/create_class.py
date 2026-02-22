"""This script is designed to implement create_class function that creates a class
with the given name and methods"""

from typing import Callable


def create_class(class_name: str, methods: dict[str, Callable]) -> type:
    """Returns created class."""
    return type(class_name, (object,), methods)


if __name__ == '__main__':
    def say_hello(self):
        return "Hello!"


    def say_goodbye(self):
        return "Goodbye!"


    methods_dict: dict[str, Callable] = {
        "say_hello": say_hello,
        "say_goodbye": say_goodbye
    }

    MyDynamicClass = create_class("MyDynamicClass", methods_dict)

    obj = MyDynamicClass()
    print(obj.say_hello())
    print(obj.say_goodbye())
