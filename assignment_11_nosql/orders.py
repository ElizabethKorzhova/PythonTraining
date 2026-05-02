"""This module provides functions to manage orders collection"""
import uuid
from typing import List, Dict

from pymongo.results import InsertOneResult

from assignment_11_nosql.utils import get_db_collections

db, products_collection, orders_collection = get_db_collections()


def create_order(customer: str, products_cart: List[Dict[str, str | int]]) -> InsertOneResult | None:
    """
    Add order to orders collection

    Args:
        customer (str): customer name
        products_cart (List[Dict[str, str | int]]): list of products in cart
    Returns:
        InsertOneResult | None: insert result or None
    """
    pipeline = [
        {
            "$documents": products_cart
        },
        {
            "$lookup": {
                "from": "products",
                "localField": "label",
                "foreignField": "label",
                "as": "product_info"
            }
        },
        {
            "$unwind": "$product_info"
        },
        {
            "$project":
                {
                    "label": 1,
                    "quantity": 1,
                    "price": "$product_info.price",
                    "totalPrice": {"$multiply": ["$quantity", "$product_info.price"]}
                }
        },
        {
            "$group":
                {
                    "_id": None,
                    "cart": {
                        "$push": "$$ROOT",
                    },
                    "totalPrice": {"$sum": "$totalPrice"}
                }
        }
    ]

    try:
        cursor = db.command("aggregate", 1, pipeline=pipeline, cursor={})
        order = list(cursor['cursor']['firstBatch'])
    except Exception as ex:
        print(f"Aggregation error: {ex}")
        return None

    if not order:
        print(f"{customer} your cart is empty")
        return None

    return orders_collection.insert_one({
        "order_number": str(uuid.uuid4()),
        "customer": customer,
        "cart": order[0]["cart"],
        "total_price": order[0]["totalPrice"]
    })
