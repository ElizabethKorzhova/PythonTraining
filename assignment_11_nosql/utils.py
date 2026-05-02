"""This module provides helper functions for managing database"""
from typing import Tuple

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

def get_db_collections() -> Tuple[Database, Collection, Collection]:
    """
    Create a MongoDB client and return database, products and orders collection

    Returns:
        Tuple[Database, Collection, Collection]: MongoDB database and MongoDB collections
    """
    client = MongoClient("localhost", 27017)
    db = client.shop
    return db, db.products, db.orders
