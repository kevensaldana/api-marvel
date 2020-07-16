from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import pydevd_pycharm
# pydevd_pycharm.settrace('host.docker.internal', port=4200, stdoutToServer=True, stderrToServer=True)
from app.api.routes import character

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4000",
    "https://angular.kevensaldana.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(character.router, prefix="/character", tags=["character"])
