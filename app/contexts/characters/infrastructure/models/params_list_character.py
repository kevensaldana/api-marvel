from enum import Enum


class ParamsListCharacterOrderBy(str, Enum):
    ASC_NAME = 'name'
    ASC_MODIFIED = 'modified'
    DES_NAME = '-name'
    DES_MODIFIED = '-modified'

    def __str__(self):
        return '%s' % self.value


class ParamsListCharacter:
    def __init__(self,
                 orderBy: ParamsListCharacterOrderBy = ParamsListCharacterOrderBy.ASC_NAME,
                 limit: int = 100,
                 offset: int = 0,
                 nameStartsWith: str = None
                 ):
        self.orderBy = orderBy
        self.limit = limit
        self.offset = offset
        self.nameStartsWith = nameStartsWith
