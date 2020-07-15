from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from pydantic import BaseModel
from app.contexts.characters.application.boundaries.get_all_character.get_all_character_input import \
    GetAllCharacterInput, GetAllCharacterOrderByInput
from app.contexts.characters.application.usecases.get_all_character_usecase import GetAllCharacterUseCase
from app.contexts.characters.application.usecases.notify_hero_usecase import NotifyHeroUsecase
from app.contexts.characters.infrastructure.datasources.error_timeout_marvel import ErrorTimeoutMarvel
from app.contexts.characters.infrastructure.datasources.http_error_marvel import HttpErrorMarvel
from app.contexts.shared.notifications.infrastructure.http_error_fcm import HttpErrorFCM

router = APIRouter()


class ParamsListCharacter(GetAllCharacterInput):
    def __init__(self,
                 orderBy: Optional[GetAllCharacterOrderByInput] = GetAllCharacterOrderByInput.ASC_NAME,
                 limit: Optional[int] = 100,
                 offset: Optional[int] = 0,
                 nameStartsWith: Optional[str] = None):
        super().__init__(orderBy, limit, offset, nameStartsWith)


@router.get("")
async def list_character(params: ParamsListCharacter = Depends(ParamsListCharacter)):
    try:
        return await GetAllCharacterUseCase().list(params)
    except ErrorTimeoutMarvel as err:
        raise HTTPException(status_code=err.code)
    except HttpErrorMarvel as err:
        raise HTTPException(status_code=err.code, detail=err.message)


class ParamsPushNotification(BaseModel):
    token: str


@router.post("/push-notification")
async def send_push_notification(params: ParamsPushNotification):
    try:
        return await NotifyHeroUsecase().notify(params.token)
    except HttpErrorFCM as err:
        raise HTTPException(status_code=err.code, detail=err.message)
