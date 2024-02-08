from litestar import Litestar, get

@get('/')
async def index() -> str:
	return "Hello darkness my old friend"

@get('/about')
async def about() -> str:
	return "I've come to talk to you again"

app = Litestar([index, about])
