from app.contexts.characters.infrastructure.repositories.character_repository import CharacterRepository


class GetAllCharacterUseCase:
    def __init__(self):
        self.__repository = CharacterRepository()

    def list(self, limit, offset):
        return self.__repository.list(limit, offset)