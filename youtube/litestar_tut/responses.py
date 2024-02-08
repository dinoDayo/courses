from litestar import Litestar, get, MediaType, Response
from pydantic import BaseModel
from litestar.status_codes import HTTP_202_ACCEPTED, HTTP_302_FOUND
from litestar.datastructures import Cookie 
from litestar.response import Redirect, File
from typing import List

import random, string
from pathlib import Path 

class Resource(BaseModel):
    id: int
    name: str 

@get(path="resources")
async def resources() -> List[Resource]:
    resources = []
    for i in range(10):
        resources.append(Resource(id=i, name=''.join(random.choices(string.ascii_uppercase + string.digits, k=10))))
    return resources

@get(path="/text", media_type=MediaType.TEXT)
async def text_response() -> str:
    return "1738. aye. I said hey whats up hello!"

@get(path="/msgpack", media_type=MediaType.MESSAGEPACK)
async def message_pack() -> dict[str,str]:
    return {"1738" : "Aye. I said heyWhatsUpHello!"}

@get(path="/html", media_type=MediaType.HTML)
async def html_response() -> str:
    return """
            <h1>1738</h1>
            <p>Aye. Im like hey whats up hello!</p>
           """

@get(path="/status_codes", status_code=HTTP_202_ACCEPTED)
async def status_codes() -> Resource:
    return Resource(id=1, name="202 HTTP status code")

@get(path="/redirect", status_code=HTTP_302_FOUND)
async def redirect() -> Redirect:
    return Redirect(path="/html")

@get(path="/file_download")
async def download_file() -> File:
    return File(path=Path(__file__).resolve(), filename="responses.py")

app = Litestar(route_handlers=[resources, text_response, message_pack, html_response, status_codes, redirect, download_file])