from app.contexts.characters.application.boundaries.get_all_character.get_all_character_input import \
    GetAllCharacterInput
from app.contexts.characters.infrastructure.repositories.character_repository import CharacterRepository


class GetAllCharacterUseCase:
    def __init__(self):
        self.__repository = CharacterRepository()

    async def list(self, params: GetAllCharacterInput):
        return await self.__repository.list(params)