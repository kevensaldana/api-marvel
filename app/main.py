from fastapi import FastAPI
from app.api.controllers.character_list_controller import CharacterListController

import pydevd_pycharm
pydevd_pycharm.settrace('host.docker.internal', port=4200, stdoutToServer=True, stderrToServer=True)

app = FastAPI()
app.add_api_route("/", CharacterListController.run)