from fastapi import APIRouter, Depends
from app.contexts.characters.application.usecases.get_all_character_usecase import GetAllCharacterUseCase
from app.contexts.characters.infrastructure.models.params_list_character import ParamsListCharacter

router = APIRouter()


@router.get("/")
async def list_character(params: ParamsListCharacter = Depends(ParamsListCharacter)):
    return GetAllCharacterUseCase().list(params)
