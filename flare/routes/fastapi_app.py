import importlib.metadata
from fastapi import FastAPI

from flare.domain.domain import Domain
from python_utils import fastapi_generic_routes as generic_routes
from python_utils import fastapi_middleware as catch_exceptions_middleware


class FastapiApp:
    def __init__(self, domain: Domain) -> None:
        package_name = "flare"
        version = importlib.metadata.version(package_name)
        self.app = FastAPI(version=version)  # pyright: ignore

        catch_exceptions_middleware.add_middleware(self.app)

        generic_routes.load_routes(self.app, package_name, version)
