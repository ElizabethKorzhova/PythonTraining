"""This script provides inserting test data to db."""
from datetime import datetime, timedelta

from assignment_11_nosql.products import init_products
from assignment_11_nosql.orders import create_order, get_customer_total_spent, get_total_sold_products

if __name__ == '__main__':
    init_products()
    create_order("Anna", [
        {"label": "Apple", "quantity": 2},
        {"label": "Potato", "quantity": 5}
    ])
    create_order("Anna", [
        {"label": "Banana", "quantity": 1},
        {"label": "Cucumber", "quantity": 1}
    ])

    print(f"Anna spend: {get_customer_total_spent("Anna")}\n"
          f"Total sold per last day: {get_total_sold_products(datetime.now() - timedelta(days=1),
                                                              datetime.now())}")
