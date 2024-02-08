from pydantic import BaseModel, Json, conint
from typing import Annotated
from litestar import Litestar, get
from litestar.openapi.spec.example import Example
from litestar.openapi.spec.external_documentation import ExternalDocumentation
from litestar.params import Parameter

class Version(BaseModel):
	id: conint(ge=1, lt=10)
	specs: Json

VERSION={1: Version(id=1, specs='{"rain drop":"drop top"}')}

@get(path="/version/{version_id:int}", sync_to_thread=False)
def get_product_version(
	version_id: Annotated[
		int,
		Parameter(
			ge=1,
			lt=10,
			title="Everybody Dance Now",
			description="Give me the music Give me the music",
			examples=[Example(value=1)],
			external_docs=ExternalDocumentation(
				url="https://xkcd.com"
			) 
		)
	]) -> Version:
	return VERSION[version_id]

app = Litestar(route_handlers=[get_product_version])
