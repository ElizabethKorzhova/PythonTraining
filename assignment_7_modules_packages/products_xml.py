"""This module provides ProductsXMLManager class to manage products data in xml format."""
import os.path
import xml.etree.ElementTree as ElTree
from typing import List, Generator


class ProductsXMLManager:
    """Class to manage product data in xml format.

    Public methods:
        get_products():
            reads a xml file and returns a tuple of product name and quantity;
        change_quantity():
            changes quantity of product in xml file;
    """

    def __init__(self, file_path: str) -> None:
        """Initializes ProductsXMLManager instance. There are no public arguments."""

        if not os.path.exists(file_path):
            raise FileNotFoundError("File does not exist")

        self._file_path = file_path
        self._el_tree: ElTree.ElementTree = ElTree.parse(self._file_path)
        self._list_products: List[ElTree.Element] = self._el_tree.findall("product")

    def get_products(self) -> Generator:
        """Reads the given xml file and returns a tuple of product name and quantity."""
        for product in self._list_products:
            product_name = product.find("name")
            product_quantity = product.find("quantity")
            yield product_name, product_quantity

    def change_quantity(self, product_name: str, product_quantity: int) -> None:
        """Changes quantity of product in xml file."""
        if (isinstance(product_quantity, int) and product_quantity > 0
                and isinstance(product_name, str)):
            for product in self._list_products:
                if product.find("name").text == product_name:
                    product.find("quantity").text = str(product_quantity)

            self._el_tree.write(self._file_path)


if __name__ == '__main__':
    products = ProductsXMLManager("products.xml")
    generator = products.get_products()
    for name, quantity in generator:
        print(name, quantity)

    products.change_quantity("Milk", 100)
    print(tuple(products.get_products()))
