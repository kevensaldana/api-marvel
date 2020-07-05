from app.contexts.characters.infrastructure.models.character_model import CharacterModel
from typing import List


class ListCharacter:
    def __init__(self, count: int, limit: int, result: List[CharacterModel], total):
        self.count = count
        self.limit = limit
        self.result = result
        self.total = total
