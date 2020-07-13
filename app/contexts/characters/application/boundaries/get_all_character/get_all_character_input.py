from enum import Enum


class GetAllCharacterOrderByInput(str, Enum):
    ASC_NAME = 'name'
    ASC_MODIFIED = 'modified'
    DES_NAME = '-name'
    DES_MODIFIED = '-modified'

    def __str__(self):
        return '%s' % self.value


class GetAllCharacterInput:
    def __init__(self,
                 orderBy: GetAllCharacterOrderByInput,
                 limit: int,
                 offset: int,
                 nameStartsWith: str
                 ):
        self.orderBy = orderBy
        self.limit = limit
        self.offset = offset
        self.nameStartsWith = nameStartsWith
