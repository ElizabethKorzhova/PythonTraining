"""This script is designed to test create_class function."""

from collections.abc import Callable
from assignment_5_introspection_reflection.create_class import create_class


# pylint: disable=missing-function-docstring,unused-argument
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
