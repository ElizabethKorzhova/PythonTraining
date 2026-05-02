"""This script provides inserting test data to db."""
from assignment_11_nosql.products import init_products
from assignment_11_nosql.orders import create_order

if __name__ == '__main__':
    init_products()
    order_complete = create_order("Anna", [
        {"label": "Apple", "quantity": 2},
        {"label": "Potato", "quantity": 5}
    ])
