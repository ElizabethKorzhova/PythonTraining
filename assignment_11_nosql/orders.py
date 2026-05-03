"""This module provides functions to manage orders collection"""
from datetime import datetime, timezone
import uuid
from typing import List, Dict

from pymongo.results import InsertOneResult
from pymongo.errors import PyMongoError

from assignment_11_nosql.products import decrease_products_stock, is_available
from assignment_11_nosql.utils import get_db_collections

db, products_collection, orders_collection = get_db_collections()


def create_order(customer: str, products_cart: List[Dict[str, str | int]])\
        -> InsertOneResult | None:
    """
    Add order to orders collection

    Args:
        customer (str): customer name
        products_cart (List[Dict[str, str | int]]): list of products in cart
    Returns:
        InsertOneResult | None: insert result or None
    """
    if not is_available(products_cart):
        return None

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
        order = list(cursor["cursor"]["firstBatch"])
    except PyMongoError as ex:
        print(f"Aggregation error: {ex}")
        return None

    if not order:
        print(f"{customer} your cart is empty")
        return None

    decrease_products_stock(products_cart)

    return orders_collection.insert_one({
        "order_number": str(uuid.uuid4()),
        "customer": customer,
        "cart": order[0]["cart"],
        "total_price": order[0]["totalPrice"],
        "created_at": datetime.now(timezone.utc),
    })


def get_customer_total_spent(customer: str) -> int | float | None:
    """
    Calculate total spent of the given customer

    Args:
        customer (str): customer name
    Returns:
        int: total spent of the given customer
    """
    pipeline = [
        {
            "$match": {
                "customer": customer
            },
        },
        {
            "$group": {
                "_id": None,
                "total_spend": {
                    "$sum": "$total_price"
                }

            }
        }
    ]

    try:
        result = list(orders_collection.aggregate(pipeline=pipeline))[0]
    except PyMongoError as ex:
        print(f"Aggregation error: {ex}")
        return None
    return result["total_spend"]


def get_total_sold_products(start_date: datetime, end_date: datetime) -> int | None:
    """
    Calculate total products sold during the given period

    Args:
        start_date (datetime): start date
        end_date (datetime): end date
    Returns:
        int: total sold during the given period
    """
    pipeline = [
        {
            "$match": {
                "created_at": {"$gte": start_date, "$lte": end_date}
            }
        },
        {
            "$unwind": "$cart"
        },
        {
            "$group": {
                "_id": None,
                "total_quantity": {"$sum": "$cart.quantity"}
            }
        }
    ]

    try:
        result = list(orders_collection.aggregate(pipeline=pipeline))[0]
    except PyMongoError as ex:
        print(f"Aggregation error: {ex}")
        return None
    return result["total_quantity"]
