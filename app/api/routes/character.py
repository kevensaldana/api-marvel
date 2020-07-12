from fastapi import APIRouter, Depends, HTTPException
from app.contexts.characters.application.usecases.get_all_character_usecase import GetAllCharacterUseCase
from app.contexts.characters.infrastructure.datasources.error_timeout_marvel import ErrorTimeoutMarvel
from app.contexts.characters.infrastructure.datasources.http_error_marvel import HttpErrorMarvel
from app.contexts.characters.infrastructure.models.params_list_character import ParamsListCharacter

router = APIRouter()


@router.get("/")
async def list_character(params: ParamsListCharacter = Depends(ParamsListCharacter)):
    try:
        return await GetAllCharacterUseCase().list(params)
    except ErrorTimeoutMarvel as err:
        raise HTTPException(status_code=err.code)
    except HttpErrorMarvel as err:
        raise HTTPException(status_code=err.code, detail=err.message)
