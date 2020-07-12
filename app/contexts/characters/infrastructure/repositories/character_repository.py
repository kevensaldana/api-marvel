from app.contexts.characters.infrastructure.datasources.remote_character_datasource import RemoteCharacterDataSource
from app.contexts.characters.infrastructure.models.params_list_character import ParamsListCharacter


class CharacterRepository:
    def __init__(self):
        self.__datasource = RemoteCharacterDataSource()

    async def list(self, params: ParamsListCharacter):
        return await self.__datasource.list(params)
