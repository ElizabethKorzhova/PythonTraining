"""This module is designed to implement Proxy class which takes an object
and redirects calls to the methods of this object, additionally logging the calls"""


class Proxy:
    """Represents Proxy class which redirects calls to the methods of this
    object and logs the calls."""

    def __init__(self, obj: object) -> None:
        """Initializes Proxy class with protected obj attribute."""
        self._obj = obj

    def __getattr__(self, name_attribute: str) -> object:
        """Dunder method with calls the methods of this object and logs the calls."""
        obj_attribute = getattr(self._obj, name_attribute)
        if callable(obj_attribute):

            def wrapper(*args, **kwargs):
                log_message = f"Calling method:\n{name_attribute}"
                if args:
                    log_message += f" with args: {args}"
                if kwargs:
                    log_message += f" with kwargs: {kwargs}"
                print(log_message)
                return obj_attribute(*args, **kwargs)

            return wrapper
        print(f"Property: {name_attribute}")
        return obj_attribute
