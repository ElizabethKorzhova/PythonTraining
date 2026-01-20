"""This script is designed to test MutableClass."""

from assignment_5_introspection_reflection.mutable_class import MutableClass

obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)

obj.remove_attribute("name")
print(obj.name)
