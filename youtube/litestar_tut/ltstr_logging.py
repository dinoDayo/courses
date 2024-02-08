import logging
from litestar import Litestar, Response, get 
from litestar.background_tasks import BackgroundTask

logger = logging.getLogger(__name__)

async def logging_task(identifier: str, message: str) -> None:
    logging.info(f"{identifier} - {message}")

@get(path="/", sync_to_thread=False)
def index(name: str) -> Response[dict[str, str]]:
    return Response({name : "Hello darkness my old friend"}, background=BackgroundTask(logging_task, identifier="greeter", message=f"{name} was called!"))

app = Litestar(route_handlers=[index])