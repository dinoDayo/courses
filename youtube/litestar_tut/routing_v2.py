from typing import TYPE_CHECKING
from starlette.applications import Starlette 
from starlette.responses import JSONResponse
from starlette.routing import Route
from litestar import Litestar, Request, asgi
from litestar.handlers.http_handlers import HTTPRouteHandler

# ASGI applications: 
#   Asynchronous Server Gateway Interface applications are a convention for webservers to forward requests to async python frameworks & applications. 
#   ASGI is good for low/moderate traffic simple APIs. 
#   WSGI (Web Server Gateway Interface) apps are better for more complex and higher traffic api's. Think websockets.

# route handling
async def index(request: Request) -> JSONResponse:
    return JSONResponse({"forwarded_path": request.url.path})

starlette_app = asgi(path="/asgi", is_mount=True)(
    Starlette(
        routes = [
            Route("/", index),
            Route("/abc/", index),
            Route("/123/another/sub-path/", index)
        ]
    )
)

# header specification
from litestar import HttpMethod, route
from litestar import Request as lRequest

# @route(path="/", http_method=[HttpMethod.GET, HttpMethod.POST])
@HTTPRouteHandler(path="/", http_method=[HttpMethod.GET, HttpMethod.POST])
async def indexing(request: Request) -> str:
    return f"Only GET and POST are allowed! Your request method: <{request.method}>"


app = Litestar(route_handlers=[starlette_app, indexing])