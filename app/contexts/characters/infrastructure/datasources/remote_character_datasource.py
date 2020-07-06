import httpx
import os
from app.contexts.characters.infrastructure.models.character_model import CharacterModel
from app.contexts.characters.infrastructure.models.list_character_model import ListCharacterModel
from app.contexts.characters.infrastructure.models.params_list_character import ParamsListCharacter


def transform_items(item):
    thumbnail = item.get('thumbnail')
    return CharacterModel(item.get('id'),
                          item.get('name'),
                          f"{thumbnail.get('path').replace('http', 'https')}.{thumbnail.get('extension')}",
                          item.get('description'))


class RemoteCharacterDataSource:
    url = 'https://gateway.marvel.com:443/v1/public/characters'

    def list(self, params: ParamsListCharacter):
        with self.__get_client(params) as client:
            request = client.get(self.url)
        print(request.json())
        response = request.json().get('data')
        result = list(map(transform_items, response.get('results')))
        return ListCharacterModel(response.get('count'), response.get('limit'), result, response.get('total'))

    @staticmethod
    def __get_client(params: ParamsListCharacter):
        headers = {'Content-Type': 'application/json'}
        params = {
            'ts': os.environ.get("AM_TS"),
            'apikey': os.environ.get("AM_KEY"),
            'hash': os.environ.get("AM_HASH"),
            'limit': params.limit,
            'offset': params.offset,
            'orderBy': params.orderBy
        }
        if not (params.get('nameStartsWith') is None):
            params.update({'nameStartsWith': params.get('nameStartsWith')})
        return httpx.Client(headers=headers, params=params)
