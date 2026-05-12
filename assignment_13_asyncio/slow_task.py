"""This script demonstrate execution timeouts in asyncio."""
import asyncio


async def slow_task() -> None:
    """Simulates a time-consuming task."""
    await asyncio.sleep(10)
    print("Task completed")


async def main() -> None:
    """Executes a task with a predefined time limit."""
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Timeout exceeded")


if __name__ == "__main__":
    asyncio.run(main())
