from fastapi import FastAPI
# import pydevd_pycharm
# pydevd_pycharm.settrace('host.docker.internal', port=4200, stdoutToServer=True, stderrToServer=True)
from app.api.routes import character

app = FastAPI()
app.include_router(character.router, prefix="/character", tags=["character"])
