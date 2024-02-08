from litestar import Litestar, Request, get
from litestar.exceptions import NotFoundException
from litestar.response import Redirect
from litestar.status_codes import HTTP_302_FOUND

@get(["/some-path","/some-path/{id:int}","/some-path/{id:int}/{val:str}"], name="handler_name")
async def handler(id: int=1, val: str = "Default") -> str:
    return f"{id} -- {val}"

@get("/path-info")
async def path_info(request: Request) -> str:
    path_optional = request.app.route_reverse("handler_name")
    path_partial = request.app.route_reverse("handler_name", id=200)
    path_full = request.app.route_reverse("handler_name", id=200, val="Dayo")
    return f"{path_optional} - {[path_partial]} - {path_full}"

# route handling & redirects
@get("/abc", name="one")
async def f_one() -> str:
    return "One fish Two fish"

@get("/def", name="two")
async def f_two() -> str:
    return "Red fish Blue fish"

@get("/ghi/{param:int}", name="three")
async def f_three(param: int) -> str:
    return f"param = {param}"

@get("/{handler_name:str}", name="four")
async def f_four(request: Request, handler_name: str) -> Redirect:
    f_i = request.app.route_reverse(handler_name)
    if not f_i:
        raise NotFoundException(f"From there to here, from here to there, funny things are everywhere. Also no handler exists that matches this name: {handler_name}")
    return Redirect(path=f_i, status_code=HTTP_302_FOUND)

@get("/redirect/{param_value:int}", name="five")
async def f_five(param_value: int, request: Request) -> Redirect:
    return Redirect(path=request.app.route_reverse("three", param = param_value), status_code=HTTP_302_FOUND)

# the app
app = Litestar(route_handlers=[f_one, f_two, f_three, f_four, f_five, path_info, handler])