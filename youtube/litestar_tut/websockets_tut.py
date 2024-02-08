from litestar import WebSocket, websocket, Litestar
from litestar.handlers.websocket_handlers import WebsocketRouteHandler

# websocket vs. http: 
#   Websocket faster and higher frequency of data. (stocks, weather, energy, etc.)
#   As a result, they demand more from their servers. 
#   This limits horizontal scalability. 
#   If you could multiplex the state for a websocket to multiple servers though you should be fine.

# @websocket(path="/socket")
@WebsocketRouteHandler(path="/socket")
async def my_websocket_handler(socket: WebSocket) -> None:
    await socket.accept()
    await socket.send_json({"name": "Dayo", "age": 27})
    await socket.close()

app = Litestar(route_handlers=[my_websocket_handler])