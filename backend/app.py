from fastapi import FastAPI
from uvicorn import run
from config.env import PORT, DEBUG
from routes.register import register_route

app = FastAPI(debug=DEBUG)

app.include_router(register_route, prefix="/api")

if __name__ == "__main__":
    run(app, host="localhost", port=PORT)