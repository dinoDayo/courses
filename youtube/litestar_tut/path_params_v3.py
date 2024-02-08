from pydantic import BaseModel
from typing import Annotated
from litestar import Litestar, get
from litestar.exceptions import NotAuthorizedException
from litestar.params import Parameter

USER_DB = {
	1: {
		"id": 1,
		"name": "Frederick" 
	},
	2: {
		"id": 2,
		"name": "Douglas"
	}
}

VALID_TOKEN="super-valid-token"
VALID_COOKIE="super-valid-cookie"

class User(BaseModel):
	id: int
	name: str

@get(path="/users/{user_id:int}")
def get_user(user_id: int, token: Annotated[str, Parameter(header="X-API-KEY")], cookie: Annotated[str, Parameter(cookie="my-cookie-param")]) -> User:
	if((token != VALID_TOKEN) or (cookie != VALID_COOKIE)):
		return NotAuthorizedException
	return User.model_validate(USER_DB[user_id]) 

app = Litestar(route_handlers=[get_user])
