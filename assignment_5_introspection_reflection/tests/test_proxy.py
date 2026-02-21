"""This script is designed to test Proxy class."""

from assignment_5_introspection_reflection.proxy import Proxy


class MyClass:
    def __init__(self, name="Alice"):
        self.name = name

    def greet(self, name: str, age: int) -> str:
        return f"Hello, {name}, you are {age} years old"


myclass_1 = MyClass()
proxy = Proxy(myclass_1)
result = proxy.greet("Alice", age=20)
print(result)
print(proxy.name)
