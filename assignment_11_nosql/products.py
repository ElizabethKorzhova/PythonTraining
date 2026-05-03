"""This module provides functions to manage products collection"""
from typing import List, Dict

from assignment_11_nosql.utils import get_db_collections

db, products_collection, _ = get_db_collections()


def init_products() -> None:
    """Insert test data to products collection"""
    if not "products" in db.list_collection_names():
        products_collection.insert_many([
            {
                "label": "Apple",
                "price": 1.2,
                "category": "fruits",
                "stock": 2
            },
            {
                "label": "Banana",
                "price": 2.5,
                "category": "fruits",
                "stock": 3
            },
            {
                "label": "Cucumber",
                "price": 3.0,
                "category": "vegetables",
                "stock": 10
            },
            {
                "label": "Potato",
                "price": 4.0,
                "category": "vegetables",
                "stock": 5
            }
        ])
        products_collection.create_index([("label", 1)], unique=True)
        products_collection.create_index([("category", 1), ("label", 1)])


def add_product(label: str, price: float | int, category: str, stock: int) -> None:
    """
    Add product to products collection

    Args:
        label (str): label of a product
        price (float | int): price of the product
        category (str): category of the product
        stock (int): count of the product in stock
    """
    products_collection.insert_one({
        "label": label,
        "price": price,
        "category": category,
        "stock": stock,
    })


def is_available(products_cart: List[Dict[str, str | int]]) -> bool:
    """
    Check if given products is available in collection

    Args:
        products_cart (List[Dict[str, str | int]]): list of products
    Returns:
        bool: True if all products are available otherwise False
    """
    for product in products_cart:
        product_in_db = products_collection.find_one({"label": product["label"]})

        if not product_in_db:
            print(f"Product {product['label']} not exist.")
            return False

        if product["quantity"] > product_in_db["stock"]:
            print("Order was not created due to stock issues.")
            return False
    return True


def decrease_products_stock(products_cart: List[Dict[str, str | int]]) -> None:
    """
    Decrease stock of products in products collection

    Args:
        products_cart (List[Dict[str, str | int]]): list of products
    """
    for product in products_cart:
        products_collection.update_one(
            {
                "label": product["label"],
                "stock": {"$gte": product["quantity"]}
            },
            {
                "$inc": {"stock": -product["quantity"]}
            }
        )
        delete_product(product["label"])


def delete_product(product_name: str) -> None:
    """
    Delete product from products collection where stock = 0

    Args:
        product_name (str): name of product
    """
    products_collection.delete_one({
        "label": product_name,
        "stock": 0
    })
