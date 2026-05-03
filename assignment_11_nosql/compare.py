"""This script compares MongoDB database and Sqlite database."""
import sqlite3
from typing import List, Dict

from pymongo import MongoClient

PRODUCTS_DATA: List[Dict[str, str | int | float]] = [
    {"label": "Phone", "price": 100, "stock": 1},
    {"label": "Laptop", "price": 500, "stock": 1}
]

def crud_mongo() -> None:
    """Represents CRUD operations for MongoDB."""
    print("---MongoDB CRUD---")
    client = MongoClient("localhost", 27017)
    db = client.shop
    products = db.products

    products.delete_many({})

    print("\tInserting products...")
    products.insert_many(PRODUCTS_DATA)

    print("\tUpdating products with increment stock...")
    products.update_many({}, {"$inc": {"stock": 1}})

    print("\tGetting product by label...")
    phone = products.find_one({"label": "Phone"})
    print(f'\t\t{phone["label"]} - price {phone["price"]}, in stock {phone["stock"]}')

    print("\tGetting all products...")
    products_list = products.find()
    for item in products_list:
        print(f'\t\t{item["label"]} - price {item["price"]}, in stock {item["stock"]}')

    products.delete_one({"label": "Phone"})
    print("\tProduct phone was deleted from collection.\n")


def crud_sqlite():
    """Represents CRUD operations for SQLite."""
    print("---SQLite CRUD---")

    with sqlite3.connect("shop.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              label TEXT NOT NULL,
                              price FLOAT NOT NULL,
                              stock INTEGER NOT NULL
                          )""")

        print("\tInserting products...")
        for product in PRODUCTS_DATA:
            cursor.execute("""INSERT INTO products (label, price, stock)
                              VALUES (?, ?, ?)""",
                           (product["label"], product["price"], product["stock"]))
        connection.commit()

        print("\tUpdating products with increment stock...")
        cursor.execute("""UPDATE products SET stock = stock + 1""")
        connection.commit()

        print("\tGetting product by label...")
        phone = cursor.execute("""SELECT * FROM products WHERE label = ?""",
                               ("Phone",)).fetchone()
        print(f"\t\t{phone[1]} - price {phone[2]}, in stock {phone[3]}")

        print("\tGetting all products...")
        products_list = cursor.execute("""SELECT * FROM products""").fetchall()
        for item in products_list:
            print(f"\t\t{item[1]} - price {item[2]}, in stock {item[3]}")

        cursor.execute("""DELETE FROM products WHERE label = ?""", ("Phone",))
        connection.commit()
        print("\tProduct phone was deleted from collection.")


if __name__ == '__main__':
    crud_mongo()
    crud_sqlite()
