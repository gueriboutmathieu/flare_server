import importlib.metadata
from fastapi import FastAPI

from flare.domain.domain import Domain
from flare.routes import auth_routes, search_routes
from flare.services.auth_service import AuthService
from python_utils import fastapi_generic_routes as generic_routes
from python_utils import fastapi_middleware as catch_exceptions_middleware



class FastapiApp:
    def __init__(self, domain: Domain, auth_service: AuthService) -> None:
        package_name = "flare"
        version = importlib.metadata.version(package_name)
        self.app = FastAPI(version=version)  # pyright: ignore

        catch_exceptions_middleware.add_middleware(self.app)

        generic_routes.load_routes(self.app, package_name, version)
        auth_routes.load_routes(self.app, domain)
        search_routes.load_routes(self.app, domain, auth_service)
