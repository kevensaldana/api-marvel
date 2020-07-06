from app.contexts.characters.domain.entities.list_character_model import ListCharacter


class ListCharacterModel(ListCharacter):
    def __init__(self, count, limit, result, total):
        ListCharacter.__init__(self, count, limit, result, total)