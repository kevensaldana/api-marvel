import httpx
import os

from app.contexts.characters.application.boundaries.get_all_character.get_all_character_input import \
    GetAllCharacterInput
from app.contexts.characters.infrastructure.datasources.error_timeout_marvel import ErrorTimeoutMarvel
from app.contexts.characters.infrastructure.datasources.http_error_marvel import HttpErrorMarvel
from app.contexts.characters.infrastructure.models.character_model import CharacterModel
from app.contexts.characters.infrastructure.models.list_character_model import ListCharacterModel


def transform_items(item):
    thumbnail = item.get('thumbnail')
    return CharacterModel(item.get('id'),
                          item.get('name'),
                          f"{thumbnail.get('path').replace('http', 'https')}.{thumbnail.get('extension')}",
                          item.get('description'))


class RemoteCharacterDataSource:
    url = 'https://gateway.marvel.com:443/v1/public/characters'

    async def list(self, params: GetAllCharacterInput):
        async with self.__get_client(params) as client:
            try:
                request = await client.get(self.url)
                request.raise_for_status()
                response = request.json()
                response = response.get('data')
                result = list(map(transform_items, response.get('results')))
                return ListCharacterModel(response.get('count'), response.get('limit'), result, response.get('total'))
            except httpx.HTTPError as err:
                response = err.response.json()
                raise HttpErrorMarvel(response.get('code'), response.get('status'))
            except (httpx.ConnectTimeout, httpx.ReadTimeout):
                raise ErrorTimeoutMarvel()

    @staticmethod
    def __get_client(params: GetAllCharacterInput):
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
        return httpx.AsyncClient(headers=headers, params=params, timeout=5.0)
