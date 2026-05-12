"""This script demonstrate the Producer-Consumer pattern using asyncio."""
from typing import Optional

import asyncio


async def producer(queue: asyncio.Queue[Optional[str]]) -> None:
    """Generates tasks and adds them to the queue."""
    for i in range(1, 6):
        task = f"Task {i}"
        await queue.put(task)
        print(f"Produced: {task}")
        await asyncio.sleep(1)

    for _ in range(3):
        await queue.put(None)


async def consumer(queue: asyncio.Queue[str], name: str) -> None:
    """Processes tasks retrieved from the queue."""
    while True:
        task = await queue.get()

        if task is None:
            queue.task_done()
            print(f"{name} stopped")
            break

        print(f"{name} started {task}")
        await asyncio.sleep(2)
        print(f"{name} finished {task}")

        queue.task_done()


async def main() -> None:
    """Initializes shared asynchronous queue and runs consumers and producers."""
    queue: asyncio.Queue[Optional[str]] = asyncio.Queue()

    await asyncio.gather(
        producer(queue),
        consumer(queue, "Consumer 1"),
        consumer(queue, "Consumer 2"),
        consumer(queue, "Consumer 3"),
    )


if __name__ == "__main__":
    asyncio.run(main())
