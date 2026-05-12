"""Simple asynchronous web server using aiohttp."""
import asyncio
from aiohttp import web


async def hello(request: web.Request) -> web.Response:
    """Handles the root index route and returns web response."""
    return web.Response(text="Hello, World!")


async def slow(request: web.Request) -> web.Response:
    """Simulates a long-running asynchronous operation and returns web response."""
    await asyncio.sleep(5)
    return web.Response(text="Operation completed")


app = web.Application()
app.router.add_get("/", hello)
app.router.add_get("/slow", slow)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=8080)