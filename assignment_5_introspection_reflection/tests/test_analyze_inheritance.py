"""This script is designed to test analyze_inheritance function."""

from assignment_5_introspection_reflection.analyze_inheritance import analyze_inheritance


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)
