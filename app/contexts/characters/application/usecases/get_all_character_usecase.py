from app.contexts.characters.infrastructure.models.params_list_character import ParamsListCharacter
from app.contexts.characters.infrastructure.repositories.character_repository import CharacterRepository


class GetAllCharacterUseCase:
    def __init__(self):
        self.__repository = CharacterRepository()

    def list(self, params: ParamsListCharacter):
        return self.__repository.list(params)