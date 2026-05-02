from pymongo import MongoClient

def get_db_collections():
    client = MongoClient("localhost", 27017)
    db = client.shop
    return db, db.products, db.orders
