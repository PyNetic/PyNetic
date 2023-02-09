"""
Serves the production code for testing
"""

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from starlette.routing import Mount, Route, Router, WebSocketRoute
from starlette.staticfiles import StaticFiles


def startup():
    print("Ready to go")


routes = []

app = Starlette(debug=True, routes=routes, on_startup=[startup])
