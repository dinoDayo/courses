from asyncio import sleep
from datetime import datetime 
from collections.abc import AsyncGenerator
from litestar import Litestar, get, Request
from litestar.response import Stream 
from litestar.response import Template 
from litestar.serialization import encode_json 
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from pathlib import Path 

async def my_generator() -> AsyncGenerator[bytes, None]:
    while True:
        await sleep(.5)
        yield encode_json({"current_time": datetime.now()})

@get(path="/")
def stream_time() -> Stream:
    return Stream(my_generator())

@get(path="/info")
def info(request: Request) -> Template:
    return Template(template_name="info.html", context={"user":"Daniel"})

app=Litestar(route_handlers=[stream_time, info], template_config=TemplateConfig(directory=Path("templates"), engine=JinjaTemplateEngine))