"""Development Server

Hot reloads pages on save
"""

from .dev_server import Application

def application_loop():
    app = Starlette(debug=True)

if __name__ == '__main__':
    uvicorn.run("server:run_server", host="127.0.0.1", port=8000, log_level="debug")
