from app.contexts.characters.domain.entities.character import Character


class CharacterModel(Character):
    def __init__(self, id, name, image, description):
        Character.__init__(self, id, name, image, description)
