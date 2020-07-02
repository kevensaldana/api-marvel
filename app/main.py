from fastapi import FastAPI
from app.api.controllers.character_list_controller import CharacterListController

app = FastAPI()
app.add_api_route("/", CharacterListController.run)