from pydantic import BaseModel
from litestar import Litestar, get
from datetime import datetime, UTC

class User(BaseModel):
	id: int
	name: str

class Order(BaseModel):
	id: int
	customer_id: int
	description: str

ORDERS_BY_DATETIME = {
	datetime.fromtimestamp(1667924386, tz=UTC): [
		Order(id=1, customer_id=1, description="Hello darkness my old friend"),
		Order(id=2, customer_id=1, description="Ive come to talk to you again"),
	]
}

USER_DB = {
	1: {"id": 1, "name": "Frederick Douglass"}
}

@get("/user/{user_id:int}", sync_to_thread=False)
async def get_user(user_id: int) -> User:
	return User.model_validate(USER_DB[user_id])

@get("/orders/{from_date:int}", sync_to_thread=False)
async def get_orders(from_date: datetime) -> list[Order]:
	return ORDERS_BY_DATETIME[from_date]

app = Litestar(route_handlers = [get_user, get_orders])
