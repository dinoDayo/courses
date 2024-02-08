from litestar import Litestar, post, get, MediaType
from litestar.datastructures import UploadFile
from litestar.params import Body
from litestar.enums import RequestEncodingType
from typing import Annotated
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

@post(path="/")
async def index(data: dict[str, str]) -> dict[str,str]:
    return data

@get(path="/user")
async def user_path() -> User:
    return User(id=1, name="Gabriella")

@post(path="/create_user")
async def create_user(data: Annotated[User, Body(title="Create user!", description="Creation of new user!")]) -> User:
    return data

@post(path="/upload_file", MediaType=MediaType.TEXT) 
async def upload_file(data: Annotated[UploadFile, Body(title="Upload File!", description="Uploading a new file!", media_type=RequestEncodingType.MULTI_PART)]) -> str:
    content = await data.read()
    filename = data.filename
    print(f"\nFile contents: {content}\n")
    return f"filename: {filename} - size: {len(content)}"

app = Litestar(route_handlers=[index, user_path, create_user, upload_file])