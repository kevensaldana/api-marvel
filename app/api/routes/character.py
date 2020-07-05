from fastapi import APIRouter
from app.contexts.characters.application.usecases.get_all_character_usecase import GetAllCharacterUseCase

router = APIRouter()


@router.get("/")
async def list():
    print('list')
    return GetAllCharacterUseCase().list(100, 0)