from litestar import Litestar, get, Request, Controller, Router
from typing import Any

class MyController(Controller):
    path="/controller"
    @get()
    def handler(self) -> str:
        return "From class controller!"

@get(["/","/index","/homepage"])
async def index() -> str:
    return "Multiple context routes!"

@get(["/some-path"])
async def route_handler(request: Request[Any, Any, Any]) -> None:
    @get("/sub-path")
    async def sub_path_handler() -> None:
        return None
    request.app.register(sub_path_handler)

internal = Router(path="/internal", route_handlers=[MyController])
external = Router(path="/external", route_handlers=[MyController])

app = Litestar(route_handlers=[index, route_handler, internal, external])

@get("/sub")
async def sub() -> str:
    return "This is also a registered path!"

app.register(sub)