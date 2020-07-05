import httpx
import os

from app.contexts.characters.infrastructure.models.character_model import CharacterModel


def transform_items(item):
    return CharacterModel(item.id, item.name, f"{item.thumbnail.path.replace('http', 'https')}.{item.thumbnail.extension}")


class RemoteCharacterDataSource:
    def list(self, limit, offset):
        print(self.__get_url())
        response = httpx.get(self.__get_url()).json()
        print(response)
        # result = map(transform_items, response.result)
        return response

    @staticmethod
    def __get_url():
        AM_TS = os.environ.get("AM_TS")
        AM_KEY = os.environ.get("AM_KEY")
        AM_HASH = os.environ.get("AM_HASH")
        return f'https://gateway.marvel.com:443/v1/public/characters?ts={AM_TS}&apikey={AM_KEY}&hash=${AM_HASH}'
