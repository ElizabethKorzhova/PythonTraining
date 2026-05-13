"""Main module for event-driven shop simulation."""

import threading
from queue import Empty, Queue
from typing import Any

from analytics_service import AnalyticsService
from event_bus import EventBus
from notification_service import send_order_created_email, send_order_paid_sms
from order_service import OrderService


EventQueue = Queue[tuple[str, dict[str, Any]]]


def worker(event_queue: EventQueue, bus: EventBus) -> None:
    """
    Read events from queue and process them through EventBus.

    Worker does not stop when listener raises an error.

    Args:
        event_queue: Queue with events.
        bus: EventBus instance.
    """
    while True:
        try:
            event_name, data = event_queue.get(timeout=1)

            if event_name == "STOP":
                event_queue.task_done()
                break

            try:
                bus.emit(event_name, data)
            except Exception as error:
                print(f"[WORKER ERROR] Failed to process event {event_name}: {error}")

            event_queue.task_done()

        except Empty:
            continue


if __name__ == "__main__":
    event_queue: EventQueue = Queue()
    bus = EventBus()
    analytics = AnalyticsService()
    order_service = OrderService(event_queue)

    bus.subscribe("order.created", send_order_created_email)
    bus.subscribe("order.created", analytics.track_order_created)

    bus.subscribe("order.paid", send_order_paid_sms)
    bus.subscribe("order.paid", analytics.track_order_paid)

    worker_thread = threading.Thread(
        target=worker,
        args=(event_queue, bus),
    )
    worker_thread.start()

    order_service.create_order(
        order_id=1,
        user_email="user@example.com",
        amount=250.0,
    )

    order_service.pay_order(
        order_id=1,
        phone_number="+380991112233",
    )

    order_service.create_order(
        order_id=2,
        user_email="customer@example.com",
        amount=500.0,
    )

    event_queue.put(("STOP", {}))

    event_queue.join()
    worker_thread.join()

    print("\nEvent log:")
    for event in bus.event_log:
        print(event)

    print("\nFinal analytics:")
    print(f"Created orders: {analytics.created_orders_count}")
    print(f"Paid orders: {analytics.paid_orders_count}")