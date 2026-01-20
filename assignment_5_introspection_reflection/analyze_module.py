"""This module is designed to implement analyze_module function that takes the
module name (string) as input and print the list of all classes, functions and their
signatures in the module"""

import importlib
import inspect


def analyze_module(module_name: str) -> None:
    """Finds all functions and classes in the module and prints them with their signatures."""
    try:
        module = importlib.import_module(module_name)
        print(f"\n<<<MODULE {module_name}>>>\n")
        module_data = inspect.getmembers(module)

        functions: list[tuple[str, str]] = []
        classes: list[tuple[str, str]] = []
        for name, value in module_data:
            if not name.startswith("__") and not name.endswith("__"):
                is_function: bool = inspect.isbuiltin(value) or inspect.isfunction(value)
                is_class: bool = inspect.isclass(value)
                try:
                    if is_function:
                        functions.append((name, str(inspect.signature(value))))
                    if is_class:
                        classes.append((name, str(inspect.signature(value))))
                except ValueError:
                    if is_function:
                        functions.append((name, "()"))
                    if is_class:
                        classes.append((name, " "))

        print(f"Functions in module {module_name}:")
        if not functions:
            print(f"- <there are no functions in the {module_name} module>")
        for function, signatures in functions:
            print(f"- {function}{signatures}")

        print(f"\nClasses in module {module_name}:")
        if not classes:
            print(f"- <there are no classes in the {module_name} module>")
        for class_name, signatures in classes:
            print(f"- {class_name}{signatures}")

    except ModuleNotFoundError as ex:
        print(f"Error: {ex}")


if __name__ == "__main__":
    analyze_module("math")
    analyze_module("datetime")
    analyze_module("pathlib")
