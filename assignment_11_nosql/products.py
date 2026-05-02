"""This module provides functions to manage products collection"""
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
