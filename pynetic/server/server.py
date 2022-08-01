"""Development Server

Hot reloads pages on save
"""

import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


def application_loop():
    app = Starlette(debug=True)


if __name__ == "__main__":
    uvicorn.run("server:run_server", host="127.0.0.1", port=8000, log_level="debug")
