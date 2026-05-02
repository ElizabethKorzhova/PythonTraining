import uuid
from typing import List, Dict

from pymongo.results import InsertOneResult

from assignment_11_nosql.products import init_products
from assignment_11_nosql.utils import get_db_collections

_, products_collection, orders_collection = get_db_collections()


def add_to_cart(product: str, quantity: int) -> Dict | None:
    product_in_db = products_collection.find_one({"label": product})

    if not product_in_db:
        print(f"Product {product} not found")
        return None
    return {"label": product, "quantity": quantity, "price": product_in_db["price"],
            "totalPrice": quantity * product_in_db["price"]}


def order(customer: str, products_cart: List[Dict[str, str | int]]) -> InsertOneResult | None:
    cart = []
    total_price = 0
    for product in products_cart:
        product = add_to_cart(product["label"], product["quantity"])
        if product:
            total_price += product["totalPrice"]
            cart.append(product)

    if not cart:
        print(f"{customer}, your cart is empty")
        return None

    return orders_collection.insert_one({
        "order_number": str(uuid.uuid4()),
        "customer": customer,
        "cart": cart,
        "total_price": total_price
    })


if __name__ == '__main__':
    init_products()
    order_complete = order("Anna", [{"label": "Apple", "quantity": 2}, {"label": "Potato", "quantity": 5}])
