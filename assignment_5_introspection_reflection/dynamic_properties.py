"""This script is designed to implement DynamicProperties class, in which is possible to dynamically add properties via method."""


class DynamicProperties:
    """Class to work with dynamic properties."""

    def add_property(self, property_name, property_value):
        """Add property to DynamicProperties class."""
        storage_name = "__" + property_name

        def getter(self):
            """Get property value."""
            return getattr(self, storage_name)

        def setter(self, value):
            """Set property value."""
            setattr(self, storage_name, value)

        attribute = property(fget=getter, fset=setter)
        setattr(self.__class__, property_name, attribute)
        setattr(self, storage_name, property_value)


if __name__ == '__main__':
    obj = DynamicProperties()
    obj.add_property('name', 'default_name')
    print(obj.name)
    obj.name = "Python"
    print(obj.name)
