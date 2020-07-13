from app.contexts.characters.application.boundaries.get_all_character.get_all_character_input import \
    GetAllCharacterInput
from app.contexts.characters.infrastructure.datasources.remote_character_datasource import RemoteCharacterDataSource


class CharacterRepository:
    def __init__(self):
        self.__datasource = RemoteCharacterDataSource()

    async def list(self, params: GetAllCharacterInput):
        return await self.__datasource.list(params)
