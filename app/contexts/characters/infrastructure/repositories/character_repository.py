from app.contexts.characters.infrastructure.datasources.remote_character_datasource import RemoteCharacterDataSource


class CharacterRepository:
    def __init__(self):
        self.__datasource = RemoteCharacterDataSource()

    def list(self, limit, offset):
        return self.__datasource.list(limit, offset)